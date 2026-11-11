#!/usr/bin/env python3
"""Run the five owner-approved M2-D customer journeys against a private DAG prototype.

The runner executes locally only. It renders the exact local HTML, CSS and JS
in memory, resolves the existing anchor destinations without network navigation,
and writes reports outside the public repository and prototype source directory.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

try:
    from .private_review_output import prepare_private_output_directory, write_private_artifacts
    from .validate_private_prototype import ROOT, validate_private_prototype
except ImportError:  # direct script execution
    from private_review_output import prepare_private_output_directory, write_private_artifacts
    from validate_private_prototype import ROOT, validate_private_prototype

VIEWPORT_WIDTHS = (390, 430, 768, 1280, 1440)
VIEWPORT_HEIGHT = 900

APPROVED_D017_COLORS = frozenset({
    "#FFFFFF", "#132A3A", "#174F6B", "#E5AD26", "#F3F7F8", "#D4E0E5"
})
D017_REQUIRED_TOKENS = {
    "--dag-canvas": "#FFFFFF",
    "--dag-ink": "#132A3A",
    "--dag-brand": "#174F6B",
    "--dag-accent": "#E5AD26",
    "--dag-surface": "#F3F7F8",
    "--dag-border": "#D4E0E5",
}
D017_REQUIRED_MARKERS = (
    '--font-display: "Source Serif 4"',
    "--font-body: Inter",
    "--content-max: 1440px",
    "--gutter: clamp(20px, 4vw, 56px)",
    "--section-gap: 80px",
    "font-size: 44px;",
    "font-size: 32px; line-height: 1.18;",
    "22px/1.25 var(--font-body)",
    "font-size: clamp(34px, 3.9vw, 56px);",
    "aspect-ratio: 16 / 9;",
    "aspect-ratio: 4 / 5;",
    "aspect-ratio: 1;",
    ".primary-nav a[aria-current]",
    "text-decoration-thickness: 2px;",
)


def audit_d017_visual_css(css_text: str) -> dict[str, Any]:
    """Check private prototype CSS against the owner's approved D-017 system."""
    colors = sorted(set(re.findall(r"#[0-9A-Fa-f]{3,8}\b", css_text)))
    normalized = {color.upper() for color in colors}
    errors: list[str] = []
    unexpected = sorted(normalized - APPROVED_D017_COLORS)
    if unexpected:
        errors.append("unapproved colour values: " + ", ".join(unexpected))
    for token, expected in D017_REQUIRED_TOKENS.items():
        pattern = rf"{re.escape(token)}\s*:\s*{re.escape(expected)}\s*;"
        if not re.search(pattern, css_text, flags=re.I):
            errors.append(f"D-017 token {token} must be {expected}")
    for marker in D017_REQUIRED_MARKERS:
        if marker not in css_text:
            errors.append(f"required D-017 layout/type value is missing: {marker}")
    for forbidden, label in (
        (r"gradient\s*\(", "gradients"),
        (r"box-shadow\s*:", "drop shadows"),
        (r"border-radius\s*:\s*(?!0(?:px)?\s*;)", "rounded card corners"),
        (r"@import\b", "remote or imported stylesheets"),
        (r"url\(\s*[\"']?https?://", "remote CSS assets"),
    ):
        if re.search(forbidden, css_text, flags=re.I):
            errors.append(f"unapproved visual treatment or external resource found: {label}")
    return {
        "ok": not errors,
        "approved_colors": colors,
        "palette_token_count": len(D017_REQUIRED_TOKENS),
        "required_value_count": len(D017_REQUIRED_MARKERS),
        "errors": errors,
    }


# The route paths and transitions are deliberately explicit. A changed page
# inventory or link destination must be reviewed rather than guessed by a test.
JOURNEY_ROUTE_PATHS = {
    "discover": ("index.html", "pages/shop.html", "pages/product.html"),
    "browse": ("pages/shop.html", "pages/collection.html", "pages/product.html"),
    "evaluate": ("pages/product.html",),
    "makers_stories": (
        "pages/about.html", "pages/makers.html", "pages/journal.html", "pages/article.html"
    ),
    "contact": ("pages/product.html", "pages/contact.html"),
}

NAV_CURRENT_BY_ROUTE = {
    "index.html": None,
    "pages/shop.html": ("../pages/shop.html", "page"),
    "pages/collection.html": ("../pages/collection.html", "page"),
    "pages/product.html": ("../pages/shop.html", "location"),
    "pages/about.html": ("../pages/about.html", "page"),
    "pages/makers.html": ("../pages/makers.html", "page"),
    "pages/journal.html": ("../pages/journal.html", "page"),
    "pages/article.html": ("../pages/journal.html", "location"),
    "pages/contact.html": ("../pages/contact.html", "page"),
}

CONTENT_SLOT_COUNTS = {
    "index.html": 11,
    "pages/shop.html": 6,
    "pages/collection.html": 3,
    "pages/product.html": 4,
    "pages/about.html": 2,
    "pages/makers.html": 1,
    "pages/journal.html": 6,
    "pages/article.html": 1,
    "pages/contact.html": 0,
}
BREADCRUMB_ROUTES = frozenset({
    "pages/collection.html", "pages/product.html", "pages/article.html"
})
JOURNEY_LABELS = {
    "discover": "Discover DAG and understand its identity",
    "browse": "Browse products, categories and collections",
    "evaluate": "Evaluate product imagery and verified information",
    "makers_stories": "Explore makers, materials and editorial stories",
    "contact": "Contact the gallery and obtain support information",
}


def _inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def _render_page(page: Any, root: Path, route_path: str, asset_errors: list[str]) -> None:
    """Render one exact local page in-memory with its local CSS and JS inlined.

    The in-memory origin avoids local HTTP/file navigation restrictions in
    managed browser environments while keeping all authored assets unchanged.
    Anchor clicks are intercepted and resolved with the browser URL algorithm;
    the next route is then rendered from the same private root.
    """
    source_path = (root / route_path).resolve()
    if not _inside(source_path, root) or not source_path.is_file():
        asset_errors.append(f"page route is missing or unsafe: {route_path}")
        return
    html = source_path.read_text(encoding="utf-8")

    css_blocks: list[str] = []
    for match in re.finditer(r"<link\b([^>]*?)>", html, re.I):
        attrs = match.group(1)
        rel_match = re.search(r"\brel=[\"']([^\"']+)[\"']", attrs, re.I)
        href_match = re.search(r"\bhref=[\"']([^\"']+)[\"']", attrs, re.I)
        if not rel_match or "stylesheet" not in rel_match.group(1).lower().split():
            continue
        if not href_match:
            asset_errors.append(f"stylesheet href is missing on {route_path}")
            continue
        raw = href_match.group(1)
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc or raw.startswith("//"):
            asset_errors.append(f"external stylesheet is not allowed: {raw}")
            continue
        sheet_path = (source_path.parent / unquote(parsed.path)).resolve()
        if not _inside(sheet_path, root) or not sheet_path.is_file():
            asset_errors.append(f"local stylesheet is missing or unsafe: {route_path}: {raw}")
            continue
        css_blocks.append(sheet_path.read_text(encoding="utf-8"))
    html = re.sub(r"<link\b[^>]*rel=[\"']stylesheet[\"'][^>]*>", "", html, flags=re.I)
    if css_blocks:
        style = "\n<style>\n" + "\n".join(css_blocks) + "\n</style>\n"
        html = html.replace("</head>", style + "</head>", 1)

    script_blocks: list[str] = []
    for match in re.finditer(r"<script\b([^>]*?)src=[\"']([^\"']+)[\"'][^>]*>\s*</script>", html, re.I):
        raw = match.group(2)
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc or raw.startswith("//"):
            asset_errors.append(f"external script is not allowed: {raw}")
            continue
        script_path = (source_path.parent / unquote(parsed.path)).resolve()
        if not _inside(script_path, root) or not script_path.is_file():
            asset_errors.append(f"local script is missing or unsafe: {route_path}: {raw}")
            continue
        script_blocks.append(script_path.read_text(encoding="utf-8"))
    html = re.sub(r"<script\b[^>]*src=[\"'][^\"']+[\"'][^>]*>\s*</script>", "", html, flags=re.I)

    route_script = f"""<script>
    document.body.dataset.dagRoute = {json.dumps(route_path)};
    document.addEventListener('click', event => {{
      const anchor = event.target.closest('a[href]');
      if (!anchor) return;
      const href = anchor.getAttribute('href') || '';
      if (href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) return;
      event.preventDefault();
      document.body.dataset.dagTarget = new URL(href, 'https://dag.invalid/' + document.body.dataset.dagRoute).pathname.slice(1);
    }});
    </script>"""
    inline_scripts = "\n".join(f"<script>\n{code}\n</script>" for code in script_blocks)
    html = html.replace("</body>", inline_scripts + route_script + "</body>", 1)
    page.set_content(html, wait_until="load")



def _check_current_navigation(page: Any, route_path: str, errors: list[str]) -> None:
    """Assert that the approved six-link nav identifies the current page/section."""
    expected = NAV_CURRENT_BY_ROUTE.get(route_path)
    current = page.locator(".primary-nav a[aria-current]")
    if expected is None:
        if current.count() != 0:
            errors.append(f"Navigation: {route_path} must not mark a non-destination as current")
        return
    if current.count() != 1:
        errors.append(f"Navigation: {route_path} must expose exactly one current destination")
        return
    href, state = expected
    item = current.first
    if item.get_attribute("href") != href:
        errors.append(f"Navigation: {route_path} current link must target {href}")
    if item.get_attribute("aria-current") != state:
        errors.append(f"Navigation: {route_path} current link must use aria-current={state}")


def _check_navigation_disclosure(
    page: Any, root: Path, route_path: str, errors: list[str], asset_errors: list[str]
) -> dict[str, Any]:
    """Exercise the existing responsive navigation without adding destinations."""
    toggle = page.locator("[data-menu-toggle]")
    nav = page.locator("#primary-nav")
    width = (page.viewport_size or {}).get("width", 0)
    result = {"mode": "mobile" if width <= 700 else "desktop", "checks": 0}
    if toggle.count() != 1 or nav.count() != 1:
        errors.append(f"Navigation: {route_path} must retain one existing menu toggle and primary nav")
        return result
    if width > 700:
        if toggle.is_visible():
            errors.append(f"Navigation: desktop toggle must remain hidden at {width}px")
        if not nav.is_visible():
            errors.append(f"Navigation: desktop links must remain visible at {width}px")
        if toggle.get_attribute("aria-expanded") != "false":
            errors.append("Navigation: desktop menu toggle must not retain an expanded state")
        result["checks"] = 3
        return result
    if toggle.get_attribute("aria-expanded") != "false" or nav.is_visible():
        errors.append(f"Navigation: mobile menu must start collapsed on {route_path}")
    result["checks"] += 1
    try:
        toggle.click(timeout=5000)
        if toggle.get_attribute("aria-expanded") != "true" or not nav.is_visible():
            errors.append(f"Navigation: mobile menu did not open on {route_path}")
        result["checks"] += 1
        page.set_viewport_size({"width": width + 400, "height": VIEWPORT_HEIGHT})
        try:
            page.wait_for_function(
                "document.querySelector('[data-menu-toggle]').getAttribute('aria-expanded') === 'false'",
                timeout=1500,
            )
        except Exception:
            errors.append(f"Navigation: resizing to desktop must close the disclosure on {route_path}")
        if not nav.is_visible():
            errors.append(f"Navigation: desktop links must remain visible after resize on {route_path}")
        result["checks"] += 1
        page.set_viewport_size({"width": width, "height": VIEWPORT_HEIGHT})
        if toggle.get_attribute("aria-expanded") != "false" or nav.is_visible():
            errors.append(f"Navigation: returning to mobile must keep the disclosure collapsed on {route_path}")
        result["checks"] += 1
        toggle.click(timeout=5000)
        first_link = nav.locator("a[href]").first
        if first_link.count() != 1:
            errors.append(f"Navigation: mobile menu has no destination link on {route_path}")
            return result
        first_link.focus()
        page.keyboard.press("Escape")
        if toggle.get_attribute("aria-expanded") != "false" or nav.is_visible():
            errors.append(f"Navigation: Escape did not close the mobile menu on {route_path}")
        if not toggle.evaluate("element => document.activeElement === element"):
            errors.append(f"Navigation: Escape must restore focus to the menu toggle on {route_path}")
        result["checks"] += 2
        toggle.click(timeout=5000)
        expected_target = first_link.evaluate(
            "element => new URL(element.getAttribute('href'), 'https://dag.invalid/' + document.body.dataset.dagRoute).pathname.slice(1)"
        )
        first_link.click(timeout=5000)
        actual_target = page.locator("body").get_attribute("data-dag-target")
        if actual_target != expected_target:
            errors.append(
                f"Navigation: mobile link from {route_path} resolved to {actual_target!r}, expected {expected_target!r}"
            )
        if toggle.get_attribute("aria-expanded") != "false" or nav.is_visible():
            errors.append(f"Navigation: selecting a destination must close the mobile menu on {route_path}")
        result["checks"] += 2
        _render_page(page, root, route_path, asset_errors)
        _check_current_navigation(page, route_path, errors)
    except Exception as exc:
        errors.append(f"Navigation: responsive disclosure check failed on {route_path} ({type(exc).__name__})")
    return result



def _check_content_evidence(page: Any, route_path: str, errors: list[str]) -> dict[str, Any]:
    """Verify that every existing content slot is labelled and evidence-safe."""
    checks = 0
    frames = page.locator('.image-frame[role="img"]')
    expected_frames = CONTENT_SLOT_COUNTS.get(route_path)
    actual_frames = frames.count()
    checks += 1
    if expected_frames is None:
        errors.append(f"Content evidence: route is not in the closed nine-page inventory: {route_path}")
    elif actual_frames != expected_frames:
        errors.append(
            f"Content evidence: {route_path} expected {expected_frames} existing image slots, found {actual_frames}"
        )
    for index in range(actual_frames):
        frame = frames.nth(index)
        accessible = (frame.get_attribute("aria-label") or "").strip().lower()
        visible = " ".join(frame.locator(":scope > span").inner_text().split()).lower()
        checks += 1
        if not accessible or not visible:
            errors.append(f"Content evidence: {route_path} image slot {index + 1} needs visible and accessible labels")
            continue
        if "illustrative" not in accessible or "pending" not in accessible:
            errors.append(f"Content evidence: {route_path} image slot {index + 1} is not marked illustrative/pending")
        if accessible != visible:
            errors.append(f"Content evidence: {route_path} image slot {index + 1} visible and accessible labels differ")
        if "illustrative image frame — dag photograph pending" in visible:
            errors.append(f"Content evidence: {route_path} image slot {index + 1} still uses the generic placeholder label")

    breadcrumb = page.locator('nav[aria-label="Breadcrumb"]')
    checks += 1
    if route_path in BREADCRUMB_ROUTES:
        if breadcrumb.count() != 1:
            errors.append(f"Content semantics: {route_path} needs exactly one Breadcrumb navigation landmark")
        elif breadcrumb.locator('li[aria-current="page"]').count() != 1:
            errors.append(f"Content semantics: {route_path} breadcrumb needs one current-page item")
    elif breadcrumb.count():
        errors.append(f"Content semantics: unexpected breadcrumb landmark on {route_path}")

    if route_path == "pages/product.html":
        facts = page.locator("dl.facts")
        rows = facts.locator(":scope > .fact-row")
        labels = facts.locator("dt")
        values = facts.locator("dd")
        checks += 3
        if facts.count() != 1 or rows.count() != 4 or labels.count() != 4 or values.count() != 4:
            errors.append("Product Detail: the four existing product facts must be a semantic dl with four dt/dd pairs")
        for index in range(values.count()):
            checks += 1
            if "pending owner verification" not in values.nth(index).inner_text().lower():
                errors.append(f"Product Detail: fact value {index + 1} must remain visibly pending")
        price = page.locator(".price-line")
        checks += 1
        if price.count() != 1 or "pending owner confirmation" not in price.inner_text().lower():
            errors.append("Product Detail: price and currency must remain pending owner confirmation")
        if page.locator(".accordions details").count() != 4:
            errors.append("Product Detail: four existing information accordions must be preserved")

    if route_path == "pages/article.html":
        deck = page.locator(".article-deck")
        checks += 1
        if deck.count() != 1:
            errors.append("Article: existing introductory deck is missing")
        else:
            content = deck.inner_text().lower()
            for required in ("publication date", "authorship", "source credits", "pending"):
                if required not in content:
                    errors.append(f"Article: editorial metadata must explicitly identify {required} as pending")
    return {
        "route": route_path,
        "image_slots": actual_frames,
        "expected_image_slots": expected_frames,
        "breadcrumb_landmark": route_path in BREADCRUMB_ROUTES,
        "checks": checks,
    }


def _expect_route(
    page: Any, root: Path, selector: str, target: str,
    description: str, errors: list[str], asset_errors: list[str], content_pages: list[dict[str, Any]]
) -> bool:
    locator = page.locator(selector).first
    if locator.count() == 0:
        errors.append(f"missing journey action: {description} ({selector})")
        return False
    try:
        locator.scroll_into_view_if_needed(timeout=5000)
        locator.click(timeout=7000)
        actual = page.locator("body").get_attribute("data-dag-target")
        if actual != target:
            errors.append(f"{description}: link resolved to {actual!r}, expected {target!r}")
            return False
        _render_page(page, root, target, asset_errors)
        content_pages.append(_check_content_evidence(page, target, errors))
        _check_current_navigation(page, target, errors)
        _check_navigation_disclosure(page, root, target, errors, asset_errors)
        if page.locator("main h1").count() != 1:
            errors.append(f"{description}: destination {target} does not expose one main h1")
            return False
        return True
    except Exception as exc:  # Browser errors become review findings.
        errors.append(f"{description}: transition to {target} failed ({type(exc).__name__})")
        return False


def _check_product_evaluation(page: Any, errors: list[str]) -> dict[str, Any]:
    thumb_count = page.locator(".thumb-grid .image-frame").count()
    record = {"thumbnail_frames": thumb_count, "accordions": 0, "disabled_controls": 0}
    if thumb_count != 3:
        errors.append(f"Product Detail: expected 3 supplied thumbnail frames, found {thumb_count}")

    accordions = page.locator(".accordions details")
    record["accordions"] = accordions.count()
    if accordions.count() != 4:
        errors.append(f"Product Detail: expected 4 existing information accordions, found {accordions.count()}")
    for index in range(accordions.count()):
        item = accordions.nth(index)
        summary = item.locator("summary")
        try:
            summary.click(timeout=5000)
            if not item.evaluate("element => element.open"):
                errors.append(f"Product Detail: accordion {index + 1} did not open")
        except Exception as exc:
            errors.append(f"Product Detail: accordion {index + 1} interaction failed ({type(exc).__name__})")

    disabled_controls = page.locator(".product-info button.disabled-control")
    record["disabled_controls"] = disabled_controls.count()
    if disabled_controls.count() < 2:
        errors.append("Product Detail: Options and Purchase controls must both remain present and disabled")
    for index in range(disabled_controls.count()):
        if not disabled_controls.nth(index).is_disabled():
            errors.append(f"Product Detail: control {index + 1} is unexpectedly enabled")
    return record


def _check_contact_safety(page: Any, errors: list[str]) -> dict[str, Any]:
    form = page.locator("form")
    if form.count() != 1:
        errors.append(f"Contact: expected one disabled enquiry-form concept, found {form.count()}")
        return {"form_count": form.count(), "controls": 0, "disabled": False}

    controls = form.locator("input, select, textarea, button")
    if controls.count() != 4:
        errors.append(f"Contact: expected 3 enquiry fields and 1 submit control, found {controls.count()}")
    disabled = all(controls.nth(index).is_disabled() for index in range(controls.count()))
    if not disabled:
        errors.append("Contact: every enquiry field and submit control must remain disabled")
    if form.get_attribute("action") not in (None, "", "#"):
        errors.append("Contact: enquiry form must not have a submission endpoint")
    if (form.get_attribute("method") or "get").lower() != "get":
        errors.append("Contact: enquiry form must not use a write method")
    if page.locator("#gallery-contact").count() != 1:
        errors.append("Contact: gallery information panel is missing")
    pending_count = page.locator(".contact-row").filter(has_text="Pending owner confirmation").count()
    if pending_count != 4:
        errors.append(f"Contact: expected 4 factual contact fields to remain pending, found {pending_count}")
    return {"form_count": 1, "controls": controls.count(), "disabled": disabled, "pending_contact_rows": pending_count}


def _run_one_journey(browser: Any, root: Path, journey_id: str, width: int) -> dict[str, Any]:
    errors: list[str] = []
    steps: list[dict[str, Any]] = []
    asset_errors: list[str] = []
    context = browser.new_context(
        viewport={"width": width, "height": VIEWPORT_HEIGHT},
        device_scale_factor=1,
        reduced_motion="reduce",
        service_workers="block",
    )
    page = context.new_page()
    page_errors: list[str] = []
    content_pages: list[dict[str, Any]] = []
    console_errors: list[str] = []
    page.on("pageerror", lambda error: page_errors.append(str(error)))
    page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)

    def step(selector: str, target: str, description: str) -> None:
        before = page.locator("body").get_attribute("data-dag-route")
        passed = _expect_route(page, root, selector, target, description, errors, asset_errors, content_pages)
        after = page.locator("body").get_attribute("data-dag-route")
        steps.append({"action": description, "from": before, "to": after, "passed": passed})

    try:
        start = JOURNEY_ROUTE_PATHS[journey_id][0]
        _render_page(page, root, start, asset_errors)
        content_pages.append(_check_content_evidence(page, start, errors))
        _check_current_navigation(page, start, errors)
        navigation_details = _check_navigation_disclosure(page, root, start, errors, asset_errors)
        if page.locator("main h1").count() != 1:
            errors.append(f"Journey start {start} does not expose one main h1")

        details: dict[str, Any] = {"navigation_disclosure": navigation_details, "content_evidence_pages": content_pages}
        if journey_id == "discover":
            identity = page.locator(".hero-copy .eyebrow").inner_text()
            if "JAISALMER" not in identity.upper():
                errors.append("Homepage: Jaisalmer identity cue is missing from the first-view hero")
            if page.locator(".category-grid .category-card").count() != 3:
                errors.append("Homepage: expected the 3 approved category entry points")
            if page.locator(".product-grid .product-card").count() != 4:
                errors.append("Homepage: expected the 4 approved curated product slots")
            step('.hero-copy a[href="pages/shop.html"]', "pages/shop.html", "Open Shop from the homepage hero")
            step('.product-grid a[href="product.html"]', "pages/product.html", "Open a product from Shop")

        elif journey_id == "browse":
            shop_disabled = page.locator(".toolbar-controls button:disabled").count()
            if shop_disabled < 2:
                errors.append("Shop: Filter and Sort must remain disabled")
            step('.category-links a[href="collection.html"]', "pages/collection.html", "Open a category collection from Shop")
            collection_disabled = page.locator(".toolbar-controls button:disabled").count()
            details["disabled_filter_sort_controls"] = {"shop": shop_disabled, "collection": collection_disabled}
            if collection_disabled < 2:
                errors.append("Collection: Filter and Sort must remain disabled")
            step('.product-grid a[href="product.html"]', "pages/product.html", "Open a product from Collection")

        elif journey_id == "evaluate":
            details.update(_check_product_evaluation(page, errors))

        elif journey_id == "makers_stories":
            if page.locator(".editorial-split").count() != 2:
                errors.append("About: expected the two existing editorial split sections")
            step('footer a[href="../pages/makers.html"]', "pages/makers.html", "Continue from About to Makers")
            if page.locator(".maker-profile").count() != 1:
                errors.append("Makers: maker profile layout is missing")
            step('footer a[href="../pages/journal.html"]', "pages/journal.html", "Continue from Makers to Journal")
            if page.locator(".story-card").count() != 6:
                errors.append("Journal: expected the 6 existing story-card slots")
            step('.story-card a[href="article.html"]', "pages/article.html", "Open an editorial article from Journal")
            if page.locator(".article-body").count() != 1:
                errors.append("Article: long-form article body is missing")

        elif journey_id == "contact":
            step('.product-info a[href="contact.html"]', "pages/contact.html", "Open Contact from the product enquiry link")
            details.update(_check_contact_safety(page, errors))

        else:
            errors.append(f"Unknown journey: {journey_id}")

        for issue in asset_errors:
            errors.append(issue)
        for message in console_errors:
            errors.append(f"Browser console error: {message}")
        for message in page_errors:
            errors.append(f"Browser page error: {message}")

        return {
            "journey": journey_id,
            "label": JOURNEY_LABELS[journey_id],
            "viewport_width": width,
            "start_route": start,
            "steps": steps,
            "details": details,
            "passed": not errors,
            "errors": errors,
        }
    finally:
        context.close()


def run_journey_review(prototype_root: Path, output_dir: Path, widths: tuple[int, ...] = VIEWPORT_WIDTHS) -> dict[str, Any]:
    prototype_path = prototype_root.expanduser()
    if prototype_path.is_symlink():
        return {"ok": False, "errors": ["prototype root must not be a symlink"], "journeys_checked": 0}
    try:
        root = prototype_path.resolve(strict=True)
    except (OSError, RuntimeError):
        return {"ok": False, "errors": ["prototype root does not exist or cannot be resolved"], "journeys_checked": 0}

    if not widths or any(width < 320 for width in widths):
        return {"ok": False, "errors": ["review widths must be a non-empty tuple of widths >= 320px"], "journeys_checked": 0}
    output, output_errors = prepare_private_output_directory(
        output_dir,
        protected_roots=(("public repository", ROOT), ("prototype source directory", root)),
        reserved_paths=("private-prototype-journeys.json", "private-prototype-journeys.md"),
        label="private journey review",
    )
    if output_errors or output is None:
        return {"ok": False, "errors": output_errors or ["private journey review output path is invalid"], "journeys_checked": 0}

    validation = validate_private_prototype(prototype_path, ROOT)
    if not validation["ok"]:
        return {
            "ok": False,
            "errors": ["private-prototype entry validation failed before journey review", *validation["errors"]],
            "journeys_checked": 0,
        }


    css_path = root / "styles" / "site.css"
    if not css_path.is_file():
        return {
            "ok": False,
            "errors": ["D-017 visual audit failed: styles/site.css is missing"],
            "journeys_checked": 0,
        }
    visual_audit = audit_d017_visual_css(css_path.read_text(encoding="utf-8"))
    if not visual_audit["ok"]:
        return {
            "ok": False,
            "errors": ["D-017 visual audit failed before journey review", *visual_audit["errors"]],
            "journeys_checked": 0,
            "visual_system_audit": visual_audit,
        }

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"ok": False, "errors": ["Playwright is not installed; install requirements-browser.txt"], "journeys_checked": 0}

    output.mkdir(parents=True, exist_ok=True, mode=0o700)
    results: list[dict[str, Any]] = []
    fatal: list[str] = []
    try:
        with sync_playwright() as playwright:
            launch_options: dict[str, Any] = {"headless": True}
            executable = os.environ.get("DAG_CHROMIUM_EXECUTABLE", "").strip()
            if executable:
                launch_options["executable_path"] = executable
                launch_options["args"] = ["--no-sandbox"]
            browser = playwright.chromium.launch(**launch_options)
            try:
                for width in widths:
                    for journey_id in JOURNEY_ROUTE_PATHS:
                        result = _run_one_journey(browser, root, journey_id, width)
                        results.append(result)
                        fatal.extend(
                            f"{journey_id} at {width}px: {message}"
                            for message in result["errors"]
                        )
            finally:
                browser.close()
    except Exception as exc:
        fatal.append(f"Chromium journey review could not complete ({type(exc).__name__}): {exc}")

    journey_total = len(JOURNEY_ROUTE_PATHS) * len(widths)
    passed = sum(1 for result in results if result["passed"])
    summary = {
        "ok": not fatal and len(results) == journey_total,
        "journey_types": len(JOURNEY_ROUTE_PATHS),
        "viewports": list(widths),
        "journeys_checked": len(results),
        "journeys_expected": journey_total,
        "passed": passed,
        "failed": len(results) - passed,
        "visual_system_audit": visual_audit,
        "navigation_disclosure_checks": sum(
            item.get("details", {}).get("navigation_disclosure", {}).get("checks", 0)
            for item in results
        ),
        "content_evidence_page_checks": sum(
            len(item.get("details", {}).get("content_evidence_pages", [])) for item in results
        ),
        "errors": fatal,
        "results": results,
    }
    rows = [
        "# DAG Private Prototype — Five-Journey Review",
        "",
        f"- Result: {'PASS' if summary['ok'] else 'FAIL'}",
        f"- Journey types: {summary['journey_types']}",
        f"- Viewports: {', '.join(str(width) for width in widths)} CSS px",
        f"- Journey/viewport checks: {passed}/{journey_total}",
        f"- D-017 visual-system audit: {'PASS' if visual_audit['ok'] else 'FAIL'} ({len(visual_audit['approved_colors'])} approved colours; {visual_audit['palette_token_count']} required palette tokens)",
        f"- Responsive navigation disclosure checks: {summary['navigation_disclosure_checks']} (mobile open/Escape focus restoration/link close/resize; desktop nav visibility)",
        f"- Evidence-labelled content page checks: {summary['content_evidence_page_checks']} (route-specific image slots, breadcrumb semantics, product fact evidence and article metadata)",
        "- This is local/private automated journey evidence; it is not owner visual acceptance or participant usability research.",
        "",
        "| Journey | Width | Result | Transitions |",
        "|---|---:|---|---:|",
        *[
            f"| {item['label']} | {item['viewport_width']}px | {'PASS' if item['passed'] else 'FAIL'} | {sum(1 for step in item['steps'] if step['passed'])}/{len(item['steps'])} |"
            for item in results
        ],
    ]
    if fatal:
        rows.extend(["", "## Findings", *[f"- {error}" for error in fatal]])
    write_private_artifacts(output, {
        "private-prototype-journeys.json": json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        "private-prototype-journeys.md": "\n".join(rows) + "\n",
    })
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Run local/private automated M2-D customer journey checks.")
    parser.add_argument("--prototype-root", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        result = run_journey_review(args.prototype_root, args.output_dir)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"DAG private prototype five-journey review: FAIL — {type(exc).__name__}")
        return 1
    print("DAG private prototype five-journey review: " + ("PASS" if result["ok"] else "FAIL"))
    print(f"- Journey/viewport checks: {result.get('passed', 0)}/{result.get('journeys_expected', result.get('journeys_checked', 0))}")
    for error in result.get("errors", []):
        print(f"- {error}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
