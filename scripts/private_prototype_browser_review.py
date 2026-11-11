#!/usr/bin/env python3
"""Run a local-only responsive and interaction review of a D-016 private prototype.

This tool requires a passing private-prototype manifest first. It writes review
screenshots and summaries to a user-selected local directory outside the public
repository; it never uploads or commits private prototype data.
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
from urllib.parse import urlsplit

try:
    from .private_review_output import ensure_private_directory, prepare_private_output_directory, write_private_artifacts, write_private_bytes
    from .validate_private_prototype import ROOT, ROUTES, validate_private_prototype
except ImportError:  # direct script execution
    from private_review_output import ensure_private_directory, prepare_private_output_directory, write_private_artifacts, write_private_bytes
    from validate_private_prototype import ROOT, ROUTES, validate_private_prototype

VIEWPORT_WIDTHS = (390, 430, 768, 1280, 1440)
VIEWPORT_HEIGHT = 900
SCREENSHOT_WIDTHS = {390, 1440}


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, _format, *_args: object) -> None:
        return


@contextmanager
def serve_private_root(root: Path) -> Iterator[str]:
    handler = partial(QuietHandler, directory=str(root))
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


def run_private_review(prototype_root: Path, output_dir: Path) -> dict[str, object]:
    prototype_path = prototype_root.expanduser()
    if prototype_path.is_symlink():
        return {"ok": False, "errors": ["prototype root must not be a symlink"], "checks": 0}
    try:
        root = prototype_path.resolve(strict=True)
    except (OSError, RuntimeError):
        return {"ok": False, "errors": ["prototype root does not exist or cannot be resolved"], "checks": 0}
    output, output_errors = prepare_private_output_directory(
        output_dir,
        protected_roots=(("public repository", ROOT), ("prototype source directory", root)),
        reserved_paths=("private-prototype-review.json", "private-prototype-review.md", "screenshots"),
        label="private browser review",
    )
    if output_errors or output is None:
        return {"ok": False, "errors": output_errors or ["private browser review output path is invalid"], "checks": 0}

    validation = validate_private_prototype(prototype_path, ROOT)
    if not validation["ok"]:
        return {
            "ok": False,
            "errors": ["private-prototype entry validation failed before browser review", *validation["errors"]],
            "checks": 0,
        }

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"ok": False, "errors": ["Playwright is not installed; install requirements-browser.txt"], "checks": 0}

    ensure_private_directory(output)
    screenshots = output / "screenshots"
    screenshots.mkdir(mode=0o700, exist_ok=False)
    checks: list[dict[str, object]] = []
    failures: list[str] = []
    blocked_external: set[str] = set()

    with serve_private_root(root) as base_url, sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            for route in ROUTES:
                for width in VIEWPORT_WIDTHS:
                    page = browser.new_page(
                        viewport={"width": width, "height": VIEWPORT_HEIGHT},
                        device_scale_factor=1,
                        reduced_motion="reduce",
                        service_workers="block",
                    )
                    page_errors: list[str] = []
                    console_errors: list[str] = []
                    request_errors: list[str] = []
                    response_errors: list[str] = []
                    page.on("pageerror", lambda error: page_errors.append(str(error)))
                    page.on(
                        "console",
                        lambda message: console_errors.append(message.text)
                        if message.type == "error"
                        else None,
                    )
                    page.on(
                        "requestfailed",
                        lambda request: request_errors.append(
                            f"{request.url} ({request.failure or 'request failed'})"
                        ),
                    )

                    def capture_response(response):
                        if response.status >= 400:
                            response_errors.append(f"{response.status} {response.url}")

                    page.on("response", capture_response)

                    def network_guard(request_route):
                        parsed = urlsplit(request_route.request.url)
                        expected = urlsplit(base_url)
                        if parsed.hostname == expected.hostname and parsed.port == expected.port:
                            request_route.continue_()
                        else:
                            blocked_external.add(parsed.hostname or "unknown-host")
                            request_route.abort()

                    page.route("**/*", network_guard)
                    url = base_url + route
                    local_errors: list[str] = []
                    focus = False
                    try:
                        response = page.goto(url, wait_until="networkidle", timeout=20000)
                        _check(response is not None and response.status == 200,
                               f"{route} at {width}px: document did not return HTTP 200", local_errors)
                        _check(page.locator("main").count() == 1,
                               f"{route} at {width}px: expected one main landmark", local_errors)
                        _check(page.locator("h1").count() == 1,
                               f"{route} at {width}px: expected one h1", local_errors)
                        layout = page.evaluate(
                            """() => ({
                              width: document.documentElement.scrollWidth,
                              viewport: window.innerWidth,
                              reduced: matchMedia('(prefers-reduced-motion: reduce)').matches,
                              title: document.title.trim(),
                              lang: document.documentElement.lang,
                              viewportMeta: Boolean(document.querySelector('meta[name="viewport"]')),
                              images: Array.from(document.images).map(image => ({
                                alt: image.alt,
                                complete: image.complete,
                                naturalWidth: image.naturalWidth
                              }))
                            })"""
                        )
                        _check(layout["width"] <= layout["viewport"],
                               f"{route} at {width}px: horizontal overflow {layout['width']} > {layout['viewport']}",
                               local_errors)
                        _check(layout["reduced"], f"{route} at {width}px: reduced-motion preference not applied", local_errors)
                        _check(bool(layout["title"]), f"{route} at {width}px: document title is empty", local_errors)
                        _check(layout["lang"] == "en", f"{route} at {width}px: document language is not en", local_errors)
                        _check(layout["viewportMeta"], f"{route} at {width}px: viewport meta tag is missing", local_errors)
                        for image in layout["images"]:
                            _check(bool(image["alt"].strip()), f"{route} at {width}px: image has no alt text", local_errors)
                            _check(image["complete"] and image["naturalWidth"] > 0,
                                   f"{route} at {width}px: local image failed to load", local_errors)
                        semantics = page.evaluate(
                            """() => {
                              const name = el => Boolean(
                                (el.getAttribute('aria-label') || '').trim() ||
                                (el.textContent || '').trim() ||
                                Array.from(el.querySelectorAll('img[alt]')).some(img => img.alt.trim())
                              );
                              return {
                                unnamedLinks: Array.from(document.querySelectorAll('a')).filter(el => !name(el)).length,
                                unnamedButtons: Array.from(document.querySelectorAll('button')).filter(el => !name(el)).length,
                                duplicateIds: (() => { const ids = Array.from(document.querySelectorAll('[id]')).map(el => el.id); return ids.length - new Set(ids).size; })(),
                                activeSubmit: Array.from(document.querySelectorAll('button[type="submit"]')).filter(el => !el.disabled).length,
                                activeFormControls: Array.from(document.querySelectorAll('form input, form select, form textarea, form button')).filter(el => !el.disabled).length
                              };
                            }"""
                        )
                        _check(semantics["unnamedLinks"] == 0,
                               f"{route} at {width}px: unnamed links={semantics['unnamedLinks']}", local_errors)
                        _check(semantics["unnamedButtons"] == 0,
                               f"{route} at {width}px: unnamed buttons={semantics['unnamedButtons']}", local_errors)
                        _check(semantics["duplicateIds"] == 0,
                               f"{route} at {width}px: duplicate IDs={semantics['duplicateIds']}", local_errors)
                        _check(semantics["activeSubmit"] == 0 and semantics["activeFormControls"] == 0,
                               f"{route} at {width}px: active form/submit control detected", local_errors)
                        page.keyboard.press("Tab")
                        focus = page.evaluate("() => Boolean(document.activeElement && document.activeElement !== document.body)")
                        _check(focus, f"{route} at {width}px: Tab did not move focus to a control", local_errors)
                        for browser_error in console_errors:
                            local_errors.append(f"{route} at {width}px: browser console error: {browser_error}")
                        for request_error in request_errors:
                            local_errors.append(f"{route} at {width}px: failed request: {request_error}")
                        for response_error in response_errors:
                            local_errors.append(f"{route} at {width}px: unsuccessful resource response: {response_error}")

                        if width in SCREENSHOT_WIDTHS:
                            screenshot = screenshots / f"{route.replace('/', '-')}-{width}.png"
                            screenshot.parent.mkdir(parents=True, exist_ok=True)
                            write_private_bytes(screenshot, page.screenshot(full_page=True))
                        check = {
                            "route": route,
                            "viewport_width": width,
                            "overflow_free": layout["width"] <= layout["viewport"],
                            "reduced_motion": layout["reduced"],
                            "image_count": len(layout["images"]),
                            "keyboard_focus": focus,
                            "page_errors": page_errors,
                            "console_errors": console_errors,
                            "failed_requests": request_errors,
                            "http_errors": response_errors,
                            "errors": local_errors,
                        }
                        checks.append(check)
                        failures.extend(local_errors)
                        if page_errors:
                            failures.extend(f"{route} at {width}px: browser error {err}" for err in page_errors)
                    except Exception as exc:
                        message = f"{route} at {width}px: {type(exc).__name__}: {exc}"
                        local_errors.append(message)
                        failures.append(message)
                        checks.append({"route": route, "viewport_width": width, "errors": local_errors})
                    finally:
                        page.close()
        finally:
            browser.close()

    if blocked_external:
        failures.append("external network requests were blocked: " + ", ".join(sorted(blocked_external)))

    result = {
        "ok": not failures,
        "routes": len(ROUTES),
        "viewports": len(VIEWPORT_WIDTHS),
        "checks": len(checks),
        "passed": sum(1 for check in checks if not check.get("errors")),
        "screenshot_count": len(list(screenshots.glob("*.png"))),
        "blocked_external_hosts": sorted(blocked_external),
        "errors": failures,
        "results": checks,
    }
    rows = [
        "# DAG Private Prototype Browser Review",
        "",
        f"- Result: {'PASS' if result['ok'] else 'FAIL'}",
        f"- Routes: {result['routes']}",
        f"- Viewports: {', '.join(str(width) for width in VIEWPORT_WIDTHS)}",
        f"- Checks: {result['passed']}/{result['checks']}",
        f"- Screenshots: {result['screenshot_count']}",
        "- This is local/private automated evidence, not owner visual acceptance or participant usability research.",
        "",
        "| Route | Width | Result |",
        "|---|---:|---|",
        *[
            f"| {item['route']} | {item['viewport_width']}px | {'PASS' if not item.get('errors') else 'FAIL'} |"
            for item in checks
        ],
    ]
    if failures:
        rows.extend(["", "## Findings", *[f"- {error}" for error in failures]])
    write_private_artifacts(output, {
        "private-prototype-review.json": json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        "private-prototype-review.md": "\n".join(rows) + "\n",
    })
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a local/private DAG prototype browser review.")
    parser.add_argument("--prototype-root", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        result = run_private_review(args.prototype_root, args.output_dir)
    except (OSError, RuntimeError) as exc:
        print(f"DAG private prototype browser review: FAIL — {type(exc).__name__}")
        return 1
    print("DAG private prototype browser review: " + ("PASS" if result["ok"] else "FAIL"))
    print(f"- Responsive checks: {result.get('passed', 0)}/{result.get('checks', 0)}")
    print(f"- Screenshots: {result.get('screenshot_count', 0)}")
    for error in result["errors"]:
        print(f"- {error}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
