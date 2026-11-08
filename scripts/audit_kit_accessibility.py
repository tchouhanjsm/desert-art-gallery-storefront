#!/usr/bin/env python3
"""Static source audit for accessibility support in the owner-controlled DAG kit."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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


def audit_kit_accessibility(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    kit = root / "design/owner-controlled-kit-v2"

    for relative in ROUTES:
        path = kit / relative
        if not path.is_file():
            errors.append(f"missing page: {relative}")
            continue

        source = path.read_text(encoding="utf-8")
        if '<html lang="en">' not in source:
            errors.append(f"{relative}: document language must remain English")
        if len(re.findall(r"<main\b", source, re.IGNORECASE)) != 1:
            errors.append(f"{relative}: expected exactly one main landmark")
        if not re.search(r'<main\b[^>]*id="main-content"', source, re.IGNORECASE):
            errors.append(f"{relative}: main landmark must retain id=main-content")
        if len(re.findall(r"<h1\b", source, re.IGNORECASE)) != 1:
            errors.append(f"{relative}: expected exactly one page-level h1")

        toggle = re.search(r'<button\b[^>]*class="menu-toggle"[^>]*>', source, re.IGNORECASE)
        if not toggle:
            errors.append(f"{relative}: supplied mobile navigation toggle is missing")
        else:
            attrs = toggle.group(0)
            if 'aria-expanded="false"' not in attrs or 'aria-controls="primary-nav"' not in attrs:
                errors.append(f"{relative}: mobile navigation toggle must expose its initial state and target")
            if not re.search(r'<nav\b[^>]*id="primary-nav"[^>]*aria-label="Primary navigation"', source, re.IGNORECASE):
                errors.append(f"{relative}: primary navigation landmark must retain its accessible name and target id")
            if "Toggle navigation" not in source:
                errors.append(f"{relative}: mobile navigation toggle needs its supplied text label")

    components = kit / "styles/components.css"
    layout = kit / "styles/layout.css"
    if not components.is_file():
        errors.append("missing styles/components.css")
    else:
        css = components.read_text(encoding="utf-8")
        if ":focus-visible" not in css:
            errors.append("components.css: explicit keyboard focus-visible treatment is missing")
        if "outline: 2px solid currentColor" not in css or "outline-offset: 3px" not in css:
            errors.append("components.css: focus indicator must use currentColor and an offset outline")

    if not layout.is_file():
        errors.append("missing styles/layout.css")
    else:
        css = layout.read_text(encoding="utf-8")
        if "prefers-reduced-motion: reduce" not in css:
            errors.append("layout.css: reduced-motion media query is missing")
        if not re.search(r"@media\s*\(prefers-reduced-motion:\s*reduce\)[\s\S]*?scroll-behavior:\s*auto", css):
            errors.append("layout.css: reduced-motion preference must disable smooth scrolling")

    return errors


def main() -> int:
    errors = audit_kit_accessibility()
    if errors:
        print(f"DAG kit accessibility source audit: FAIL ({len(errors)} finding(s))")
        for error in errors:
            print(f"- {error}")
        return 1

    print("DAG kit accessibility source audit: PASS")
    print("- all nine pages retain English language, one main landmark and one h1")
    print("- all nine mobile navigation toggles expose an accessible name, state and target")
    print("- keyboard focus-visible styling is present and uses currentColor")
    print("- reduced-motion preference disables the existing smooth-scroll behaviour")
    print("- no browser rendering, assistive-technology or brand-contrast claim is made")
    return 0


if __name__ == "__main__":
    sys.exit(main())
