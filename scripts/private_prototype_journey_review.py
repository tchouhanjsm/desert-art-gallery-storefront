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
    from .validate_private_prototype import ROOT, validate_private_prototype
except ImportError:  # direct script execution
    from validate_private_prototype import ROOT, validate_private_prototype

VIEWPORT_WIDTHS = (390, 430, 768, 1280, 1440)
VIEWPORT_HEIGHT = 900

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


def _expect_route(
    page: Any, root: Path, selector: str, target: str,
    description: str, errors: list[str], asset_errors: list[str]
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
    console_errors: list[str] = []
    page.on("pageerror", lambda error: page_errors.append(str(error)))
    page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)

    def step(selector: str, target: str, description: str) -> None:
        before = page.locator("body").get_attribute("data-dag-route")
        passed = _expect_route(page, root, selector, target, description, errors, asset_errors)
        after = page.locator("body").get_attribute("data-dag-route")
        steps.append({"action": description, "from": before, "to": after, "passed": passed})

    try:
        start = JOURNEY_ROUTE_PATHS[journey_id][0]
        _render_page(page, root, start, asset_errors)
        if page.locator("main h1").count() != 1:
            errors.append(f"Journey start {start} does not expose one main h1")

        details: dict[str, Any] = {}
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

    output = output_dir.expanduser().resolve()
    repo = ROOT.resolve()
    if _inside(output, repo):
        return {"ok": False, "errors": ["journey review output must be outside the public repository"], "journeys_checked": 0}
    if _inside(output, root):
        return {"ok": False, "errors": ["journey review output must be outside the prototype source directory"], "journeys_checked": 0}
    if not widths or any(width < 320 for width in widths):
        return {"ok": False, "errors": ["review widths must be a non-empty tuple of widths >= 320px"], "journeys_checked": 0}

    validation = validate_private_prototype(prototype_path, ROOT)
    if not validation["ok"]:
        return {
            "ok": False,
            "errors": ["private-prototype entry validation failed before journey review", *validation["errors"]],
            "journeys_checked": 0,
        }

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"ok": False, "errors": ["Playwright is not installed; install requirements-browser.txt"], "journeys_checked": 0}

    output.mkdir(parents=True, exist_ok=True)
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
        "errors": fatal,
        "results": results,
    }
    (output / "private-prototype-journeys.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    rows = [
        "# DAG Private Prototype — Five-Journey Review",
        "",
        f"- Result: {'PASS' if summary['ok'] else 'FAIL'}",
        f"- Journey types: {summary['journey_types']}",
        f"- Viewports: {', '.join(str(width) for width in widths)} CSS px",
        f"- Journey/viewport checks: {passed}/{journey_total}",
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
    (output / "private-prototype-journeys.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
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
