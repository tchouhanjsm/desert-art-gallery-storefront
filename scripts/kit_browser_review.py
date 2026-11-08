#!/usr/bin/env python3
"""Run real Chromium checks against the owner-controlled nine-page DAG kit.

This is structural QA only. It does not approve brand identity, content,
production behaviour, or a visual redesign.
"""
from __future__ import annotations

import argparse
import json
import sys
import threading
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Iterator

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "design" / "owner-controlled-kit-v2"
ROUTES = (
    "index.html",
    "pages/shop.html",
    "pages/collection.html",
    "pages/product.html",
    "pages/about.html",
    "pages/makers.html",
    "pages/journal.html",
    "pages/article.html",
    "pages/contact.html",
)
VIEWPORT_WIDTHS = (390, 430, 768, 1280, 1440)
VIEWPORT_HEIGHT = 900
MOBILE_NAV_MAX_WIDTH = 900
SCREENSHOT_WIDTHS = {390, 1440}
EXPECTED_NAV_LINKS = 6

# Bounded journeys built only from D-014's existing links and controls.
JOURNEY_SCENARIOS = (
    "discover",
    "browse",
    "evaluate",
    "contextualize",
    "support",
)


class QuietHandler(SimpleHTTPRequestHandler):
    """Serve the static kit without noisy per-request access logs."""

    def log_message(self, _format: str, *_args: object) -> None:
        return


@contextmanager
def serve_kit() -> Iterator[str]:
    handler = partial(QuietHandler, directory=str(KIT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    server.daemon_threads = True
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address
        yield f"http://{host}:{port}/"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)


def _check(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def _route_slug(route: str) -> str:
    return route.replace("/", "-").replace(".html", "")


def _navigate_from_primary_nav(page, label: str, target: str) -> None:
    nav = page.locator("#primary-nav")
    if not nav.is_visible():
        toggle = page.locator(".menu-toggle")
        if not toggle.is_visible():
            raise AssertionError("primary navigation is hidden and no mobile toggle is available")
        toggle.click()
    nav.get_by_role("link", name=label, exact=True).click()
    page.wait_for_url(f"**/{target}", timeout=10000)


def _run_customer_journey(page, base_url: str, journey: str) -> list[str]:
    """Exercise current structural links; never enable commerce or submit forms."""
    errors: list[str] = []
    starts = {
        "discover": "index.html",
        "browse": "pages/shop.html",
        "evaluate": "pages/product.html",
        "contextualize": "pages/about.html",
        "support": "pages/product.html",
    }
    visited: list[str] = [starts[journey]]
    page.goto(base_url + starts[journey], wait_until="networkidle", timeout=20000)

    try:
        if journey == "discover":
            page.locator('a.button--primary[href="pages/shop.html"]').click()
            page.wait_for_url("**/pages/shop.html", timeout=10000)
            visited.append("pages/shop.html")
            page.locator(".category-links a[href='collection.html']").first.click()
            page.wait_for_url("**/pages/collection.html", timeout=10000)
            visited.append("pages/collection.html")

        elif journey == "browse":
            page.locator(".category-links a[href='collection.html']").first.click()
            page.wait_for_url("**/pages/collection.html", timeout=10000)
            visited.append("pages/collection.html")
            page.locator('a.product-card[href="product.html"]').first.click()
            page.wait_for_url("**/pages/product.html", timeout=10000)
            visited.append("pages/product.html")

        elif journey == "evaluate":
            accordions = page.locator(".details-list details")
            _check(accordions.count() == 4,
                   "Product Detail must retain four supplied information accordions", errors)
            for index in range(accordions.count()):
                item = accordions.nth(index)
                item.locator("summary").click()
                _check(item.get_attribute("open") is not None,
                       f"Product information accordion {index + 1} did not open", errors)
            _check(page.locator("#variant").is_disabled(),
                   "Variant control must remain disabled in the structural kit", errors)
            _check(page.locator("button.button--primary").is_disabled(),
                   "Purchase action must remain disabled in the structural kit", errors)

        elif journey == "contextualize":
            _navigate_from_primary_nav(page, "Makers", "pages/makers.html")
            visited.append("pages/makers.html")
            _navigate_from_primary_nav(page, "Journal", "pages/journal.html")
            visited.append("pages/journal.html")
            page.locator('a.story-card[href="article.html"]').first.click()
            page.wait_for_url("**/pages/article.html", timeout=10000)
            visited.append("pages/article.html")

        elif journey == "support":
            page.locator('a.button--secondary[href="contact.html"]').click()
            page.wait_for_url("**/pages/contact.html", timeout=10000)
            visited.append("pages/contact.html")
            _check(page.locator(".contact-panel input").is_disabled(),
                   "Product reference field must remain disabled", errors)
            _check(page.locator(".contact-panel textarea").is_disabled(),
                   "Message field must remain disabled", errors)
            _check(page.locator(".contact-panel button").is_disabled(),
                   "Enquiry submission must remain disabled without an approved endpoint", errors)

        _check(page.locator("main#main-content").count() == 1,
               "Journey destination must retain one main landmark", errors)
        _check(page.locator("h1").count() == 1,
               "Journey destination must retain one page h1", errors)
    except Exception as exc:
        errors.append(f"{journey} journey raised {type(exc).__name__}: {exc}")

    return errors


def run_review(output_dir: Path) -> dict[str, object]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:  # pragma: no cover - depends on CI environment
        raise RuntimeError(
            "Playwright is not installed. Install requirements-browser.txt first."
        ) from exc

    output_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir = output_dir / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, object]] = []
    failures: list[str] = []
    keyboard_sequences = 0

    with serve_kit() as base_url, sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            for route in ROUTES:
                for width in VIEWPORT_WIDTHS:
                    route_errors: list[str] = []
                    page_errors: list[str] = []
                    failed_assets: list[str] = []
                    layout_diagnostics: list[dict[str, object]] = []
                    page = browser.new_page(
                        viewport={"width": width, "height": VIEWPORT_HEIGHT},
                        device_scale_factor=1,
                    )
                    page.on("pageerror", lambda error: page_errors.append(str(error)))
                    page.on(
                        "requestfailed",
                        lambda request: failed_assets.append(
                            f"{request.method} {request.url}: {request.failure}"
                        )
                        if request.url.startswith(base_url)
                        and request.resource_type in {"document", "stylesheet", "script"}
                        else None,
                    )

                    url = base_url + route
                    try:
                        response = page.goto(url, wait_until="networkidle", timeout=20000)
                        _check(response is not None and response.status == 200,
                               f"{route} at {width}px: document did not return HTTP 200",
                               route_errors)

                        heading_count = page.locator("h1").count()
                        main_count = page.locator("main#main-content").count()
                        _check(heading_count == 1,
                               f"{route} at {width}px: expected one h1, found {heading_count}",
                               route_errors)
                        _check(main_count == 1,
                               f"{route} at {width}px: expected one main#main-content, found {main_count}",
                               route_errors)

                        semantic_state = page.evaluate(
                            """() => {
                              const issues = [];
                              const ids = Array.from(document.querySelectorAll("[id]"))
                                .map((element) => element.id);
                              const duplicates = ids.filter((id, index) => ids.indexOf(id) !== index);
                              if (duplicates.length) issues.push(`duplicate IDs: ${[...new Set(duplicates)].join(", ")}`);

                              const hasLabelledByName = (element) => {
                                const ids = (element.getAttribute("aria-labelledby") || "").trim().split(/\\s+/).filter(Boolean);
                                return ids.length > 0 && ids.every((id) => {
                                  const target = document.getElementById(id);
                                  return target && (target.textContent || "").trim().length > 0;
                                });
                              };
                              const hasName = (element) => Boolean(
                                (element.getAttribute("aria-label") || "").trim() ||
                                hasLabelledByName(element) ||
                                (element.cloneNode(true).textContent || "").trim() ||
                                Array.from(element.querySelectorAll("img[alt]")).some((img) => img.alt.trim())
                              );

                              for (const element of document.querySelectorAll("a")) {
                                if (!element.hasAttribute("href") || !element.getAttribute("href").trim()) {
                                  issues.push("anchor is missing a non-empty href");
                                }
                                if (!hasName(element)) issues.push("anchor has no accessible name");
                              }
                              for (const element of document.querySelectorAll("button")) {
                                if (!hasName(element)) issues.push("button has no accessible name");
                              }
                              for (const element of document.querySelectorAll("input, select, textarea")) {
                                if (!(element.labels && element.labels.length) &&
                                    !(element.getAttribute("aria-label") || "").trim() &&
                                    !hasLabelledByName(element)) {
                                  issues.push(`${element.tagName.toLowerCase()} control has no programmatic label`);
                                }
                              }
                              for (const image of document.querySelectorAll("img")) {
                                if (!image.hasAttribute("alt")) issues.push("image is missing an alt attribute");
                              }
                              for (const element of document.querySelectorAll('[role="img"]')) {
                                if (!(element.getAttribute("aria-label") || "").trim() && !hasLabelledByName(element)) {
                                  issues.push("role=img element has no accessible name");
                                }
                              }
                              for (const element of document.querySelectorAll("[aria-controls]")) {
                                for (const id of element.getAttribute("aria-controls").split(/\\s+/).filter(Boolean)) {
                                  if (!document.getElementById(id)) issues.push(`aria-controls references missing id: ${id}`);
                                }
                              }
                              for (const element of document.querySelectorAll("[aria-labelledby]")) {
                                for (const id of element.getAttribute("aria-labelledby").split(/\\s+/).filter(Boolean)) {
                                  if (!document.getElementById(id)) issues.push(`aria-labelledby references missing id: ${id}`);
                                }
                              }
                              const positiveTabindex = Array.from(document.querySelectorAll("[tabindex]"))
                                .filter((element) => Number(element.getAttribute("tabindex")) > 0);
                              if (positiveTabindex.length) issues.push("positive tabindex values are not permitted");
                              return {issues: [...new Set(issues)]};
                            }"""
                        )
                        for semantic_issue in semantic_state["issues"]:
                            route_errors.append(f"{route} at {width}px: accessibility semantics: {semantic_issue}")

                        stylesheet_state = page.locator('link[rel="stylesheet"]').evaluate_all(
                            "(links) => links.map((link) => ({href: link.href, loaded: Boolean(link.sheet)}))"
                        )
                        unloaded_styles = [item["href"] for item in stylesheet_state if not item["loaded"]]
                        _check(
                            len(stylesheet_state) == 4 and not unloaded_styles,
                            f"{route} at {width}px: expected four loaded kit stylesheets; "
                            f"found {len(stylesheet_state)}, unloaded={unloaded_styles}",
                            route_errors,
                        )

                        dimensions = page.evaluate(
                            """() => {
                              const viewportWidth = window.innerWidth;
                              const documentWidth = Math.max(
                                document.documentElement.scrollWidth,
                                document.body.scrollWidth
                              );
                              const offenders = Array.from(document.body.querySelectorAll("*"))
                                .map((element) => {
                                  const rect = element.getBoundingClientRect();
                                  const style = getComputedStyle(element);
                                  return {
                                    tag: element.tagName.toLowerCase(),
                                    className: element.getAttribute("class") || "",
                                    id: element.id || "",
                                    left: Math.round(rect.left),
                                    right: Math.round(rect.right),
                                    width: Math.round(rect.width),
                                    scrollWidth: element.scrollWidth,
                                    clientWidth: element.clientWidth,
                                    minWidth: style.minWidth,
                                    display: style.display,
                                    gridTemplateColumns: style.gridTemplateColumns
                                  };
                                })
                                .filter((item) => item.right > viewportWidth + 1 || item.left < -1)
                                .sort((a, b) => b.right - a.right)
                                .slice(0, 12);
                              return {viewportWidth, documentWidth, offenders};
                            }"""
                        )
                        overflow = int(dimensions["documentWidth"]) - int(dimensions["viewportWidth"])
                        layout_diagnostics = dimensions["offenders"] if overflow > 1 else []
                        _check(
                            overflow <= 1,
                            f"{route} at {width}px: horizontal overflow of {overflow}px "
                            f"(document {dimensions['documentWidth']}px, viewport {dimensions['viewportWidth']}px); "
                            f"offending elements={layout_diagnostics}",
                            route_errors,
                        )

                        nav = page.locator("#primary-nav")
                        toggle = page.locator(".menu-toggle")
                        nav_visible_before = nav.is_visible()
                        toggle_visible = toggle.is_visible()
                        if width <= MOBILE_NAV_MAX_WIDTH:
                            _check(toggle_visible,
                                   f"{route} at {width}px: mobile navigation toggle is not visible",
                                   route_errors)
                            _check(not nav_visible_before,
                                   f"{route} at {width}px: mobile navigation should start closed",
                                   route_errors)
                            if toggle_visible:
                                toggle.click()
                                _check(nav.is_visible(),
                                       f"{route} at {width}px: navigation did not open",
                                       route_errors)
                                _check(toggle.get_attribute("aria-expanded") == "true",
                                       f"{route} at {width}px: aria-expanded did not become true",
                                       route_errors)
                                _check(nav.locator("a").count() == EXPECTED_NAV_LINKS,
                                       f"{route} at {width}px: expected {EXPECTED_NAV_LINKS} nav links",
                                       route_errors)
                                toggle.click()
                                _check(not nav.is_visible(),
                                       f"{route} at {width}px: navigation did not close",
                                       route_errors)
                                _check(toggle.get_attribute("aria-expanded") == "false",
                                       f"{route} at {width}px: aria-expanded did not return to false",
                                       route_errors)

                                # Exercise native keyboard activation using both supported
                                # button keys; focus must remain on the disclosure control.
                                for key in ("Enter", "Space"):
                                    toggle.focus()
                                    page.keyboard.press(key)
                                    _check(nav.is_visible(),
                                           f"{route} at {width}px: {key} did not open mobile navigation",
                                           route_errors)
                                    _check(toggle.get_attribute("aria-expanded") == "true",
                                           f"{route} at {width}px: {key} did not set aria-expanded=true",
                                           route_errors)
                                    page.keyboard.press(key)
                                    _check(not nav.is_visible(),
                                           f"{route} at {width}px: {key} did not close mobile navigation",
                                           route_errors)
                                    _check(toggle.get_attribute("aria-expanded") == "false",
                                           f"{route} at {width}px: {key} did not set aria-expanded=false",
                                           route_errors)
                                    focus_retained = toggle.evaluate(
                                        "(element) => document.activeElement === element"
                                    )
                                    _check(focus_retained,
                                           f"{route} at {width}px: {key} moved focus away from the toggle",
                                           route_errors)
                                    keyboard_sequences += 1
                        else:
                            _check(not toggle_visible,
                                   f"{route} at {width}px: mobile toggle should be hidden on desktop",
                                   route_errors)
                            _check(nav_visible_before,
                                   f"{route} at {width}px: desktop primary navigation is not visible",
                                   route_errors)

                        # Save review evidence at narrow and wide endpoints only;
                        # layout assertions still run at all five required widths.
                        if width in SCREENSHOT_WIDTHS:
                            screenshot_path = screenshots_dir / f"{_route_slug(route)}-{width}.png"
                            page.screenshot(path=str(screenshot_path), full_page=True)

                        # Keyboard focus is exercised after the screenshot so
                        # the evidence capture starts in the page's default state.
                        page.keyboard.press("Tab")
                        focus_state = page.evaluate(
                            """() => {
                              const active = document.activeElement;
                              const style = getComputedStyle(active);
                              return {
                                tag: active ? active.tagName : null,
                                outlineStyle: style.outlineStyle,
                                outlineWidth: style.outlineWidth
                              };
                            }"""
                        )
                        _check(
                            focus_state["outlineStyle"] == "solid"
                            and focus_state["outlineWidth"] == "2px",
                            f"{route} at {width}px: first keyboard focus target lacks the "
                            f"authored 2px focus-visible outline ({focus_state})",
                            route_errors,
                        )

                        _check(
                            not page_errors,
                            f"{route} at {width}px: browser page errors: {page_errors}",
                            route_errors,
                        )
                        _check(
                            not failed_assets,
                            f"{route} at {width}px: local asset requests failed: {failed_assets}",
                            route_errors,
                        )
                    except Exception as exc:
                        route_errors.append(f"{route} at {width}px: browser review raised {type(exc).__name__}: {exc}")
                        try:
                            page.screenshot(
                                path=str(screenshots_dir / f"{_route_slug(route)}-{width}-failure.png"),
                                full_page=True,
                            )
                        except Exception:
                            pass
                    finally:
                        page.close()

                    result = {
                        "route": route,
                        "viewport_width": width,
                        "status": "PASS" if not route_errors else "FAIL",
                        "errors": route_errors,
                        "layout_diagnostics": layout_diagnostics,
                    }
                    results.append(result)
                    failures.extend(route_errors)

            # Exercise five customer journeys at mobile, tablet and desktop widths.
            journey_results: list[dict[str, object]] = []
            for journey in JOURNEY_SCENARIOS:
                for width in VIEWPORT_WIDTHS:
                    journey_page = browser.new_page(
                        viewport={"width": width, "height": VIEWPORT_HEIGHT},
                        device_scale_factor=1,
                    )
                    page_errors: list[str] = []
                    failed_assets: list[str] = []
                    journey_page.on("pageerror", lambda error: page_errors.append(str(error)))
                    journey_page.on(
                        "requestfailed",
                        lambda request: failed_assets.append(
                            f"{request.method} {request.url}: {request.failure}"
                        )
                        if request.url.startswith(base_url)
                        and request.resource_type in {"document", "stylesheet", "script"}
                        else None,
                    )
                    journey_errors = _run_customer_journey(journey_page, base_url, journey)
                    journey_errors.extend(f"browser page error: {error}" for error in page_errors)
                    journey_errors.extend(f"local asset request failed: {asset}" for asset in failed_assets)
                    journey_results.append({
                        "journey": journey,
                        "viewport_width": width,
                        "status": "PASS" if not journey_errors else "FAIL",
                        "errors": journey_errors,
                    })
                    failures.extend(
                        f"{journey} at {width}px: {error}" for error in journey_errors
                    )
                    journey_page.close()

            reduced_context = browser.new_context(
                viewport={"width": 390, "height": VIEWPORT_HEIGHT},
                reduced_motion="reduce",
            )
            try:
                reduced_page = reduced_context.new_page()
                reduced_page.goto(base_url + "index.html", wait_until="networkidle", timeout=20000)
                scroll_behavior = reduced_page.evaluate(
                    "getComputedStyle(document.documentElement).scrollBehavior"
                )
                if scroll_behavior != "auto":
                    failures.append(
                        "reduced-motion context: expected scroll-behavior:auto, "
                        f"received {scroll_behavior!r}"
                    )
                reduced_page.close()
            finally:
                reduced_context.close()
        finally:
            browser.close()

    passed = len(results) - sum(1 for item in results if item["status"] == "FAIL")
    journey_passed = len(journey_results) - sum(1 for item in journey_results if item["status"] == "FAIL")
    summary: dict[str, object] = {
        "browser": "Chromium (Playwright)",
        "routes": list(ROUTES),
        "viewport_widths": list(VIEWPORT_WIDTHS),
        "viewport_height": VIEWPORT_HEIGHT,
        "route_viewport_checks": len(results),
        "passed_route_viewport_checks": passed,
        "failed_route_viewport_checks": len(results) - passed,
        "reduced_motion_check": "PASS" if not any("reduced-motion" in e for e in failures) else "FAIL",
        "keyboard_navigation_sequences": keyboard_sequences,
        "journey_scenarios": list(JOURNEY_SCENARIOS),
        "journey_viewport_checks": len(journey_results),
        "passed_journey_viewport_checks": journey_passed,
        "failed_journey_viewport_checks": len(journey_results) - journey_passed,
        "journey_results": journey_results,
        "status": "PASS" if not failures else "FAIL",
        "results": results,
        "failures": failures,
        "screenshots": sorted(
            str(path.relative_to(output_dir))
            for path in screenshots_dir.glob("*.png")
        ),
    }

    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    table = [
        "| Route | " + " | ".join(f"{width}px" for width in VIEWPORT_WIDTHS) + " |",
        "|---|" + "---:|" * len(VIEWPORT_WIDTHS),
    ]
    for route in ROUTES:
        statuses = [
            next(item["status"] for item in results
                 if item["route"] == route and item["viewport_width"] == width)
            for width in VIEWPORT_WIDTHS
        ]
        table.append("| " + route + " | " + " | ".join(statuses) + " |")
    markdown = [
        "# DAG structural kit browser review",
        "",
        f"**Status:** {summary['status']}",
        f"**Browser:** {summary['browser']}",
        f"**Route/viewport runs:** {passed}/{len(results)} passed",
        f"**Reduced motion:** {summary['reduced_motion_check']}",
        f"**Keyboard activation / focus-retention sequences:** {keyboard_sequences}",
        f"**Customer journey checks:** {journey_passed}/{len(journey_results)} passed",
        "",
        "## Viewport results",
        "",
        *table,
        "",
        "## Customer journey results",
        "",
        "| Journey | " + " | ".join(f"{width}px" for width in VIEWPORT_WIDTHS) + " |",
        "|---|" + "---:|" * len(VIEWPORT_WIDTHS),
        *[
            "| " + journey + " | " + " | ".join(
                next(item["status"] for item in journey_results
                     if item["journey"] == journey and item["viewport_width"] == width)
                for width in VIEWPORT_WIDTHS
            ) + " |"
            for journey in JOURNEY_SCENARIOS
        ],
        "",
        "## Failures",
        "",
        *(["- None."] if not failures else [f"- {failure}" for failure in failures]),
        "",
        "## Evidence",
        "",
        f"{len(summary['screenshots'])} screenshots are included in the CI artifact.",
        "This automated run does not claim screen-reader, colour-contrast, WCAG or owner visual approval.",
        "",
    ]
    (output_dir / "summary.md").write_text("\n".join(markdown), encoding="utf-8")

    print(f"DAG structural kit browser review: {summary['status']}")
    print(f"- {passed}/{len(results)} route/viewport checks passed")
    print(f"- reduced-motion: {summary['reduced_motion_check']}")
    print(f"- keyboard navigation sequences: {keyboard_sequences}")
    print(f"- customer journeys: {journey_passed}/{len(journey_results)}")
    print(f"- screenshots: {len(summary['screenshots'])}")
    for failure in failures:
        print(f"FAIL: {failure}")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "artifacts" / "kit-browser-review",
        help="Directory for JSON/Markdown summaries and screenshots.",
    )
    args = parser.parse_args()
    summary = run_review(args.output_dir.resolve())
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
