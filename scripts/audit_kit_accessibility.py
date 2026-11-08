#!/usr/bin/env python3
"""Static semantic and accessibility-contract audit for the owner-controlled DAG kit."""
from __future__ import annotations

import re
import sys
from collections import Counter
from html.parser import HTMLParser
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


class PageAccessibilityParser(HTMLParser):
    """Collect semantic relationships without relying on tag-order regexes."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.main_ids: list[str] = []
        self.headings: list[int] = []
        self.controls: list[dict[str, str | bool]] = []
        self.labels: list[dict[str, str | bool]] = []
        self.links: list[dict[str, str]] = []
        self.buttons: list[dict[str, str]] = []
        self.images: list[dict[str, str | bool]] = []
        self.role_images: list[dict[str, str]] = []
        self.navs: list[dict[str, str]] = []
        self.aria_controls: list[str] = []
        self.aria_labelledby: list[str] = []
        self.positive_tabindex: list[str] = []
        self.menu_toggles: list[dict[str, str]] = []
        self.document_lang = ""
        self.title_text = ""
        self._in_title = False
        self._label_stack: list[dict[str, str | bool]] = []
        self._link_stack: list[dict[str, str]] = []
        self._button_stack: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: value or "" for name, value in attrs}
        element_id = values.get("id", "")
        if element_id:
            self.ids.append(element_id)
        if tag == "html":
            self.document_lang = values.get("lang", "").lower()
        if tag == "title":
            self._in_title = True
        if tag == "main":
            self.main_ids.append(element_id)
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings.append(int(tag[1]))
        if tag == "nav":
            self.navs.append(values)
        if tag == "label":
            label = {"for": values.get("for", ""), "contains_control": False}
            self.labels.append(label)
            self._label_stack.append(label)
        if tag in {"input", "select", "textarea"}:
            nested = bool(self._label_stack)
            for label in self._label_stack:
                label["contains_control"] = True
            self.controls.append({
                "tag": tag,
                "id": element_id,
                "aria-label": values.get("aria-label", ""),
                "aria-labelledby": values.get("aria-labelledby", ""),
                "nested_label": nested,
            })
        if tag == "a":
            link = {
                "href": values.get("href", ""),
                "aria-label": values.get("aria-label", ""),
                "aria-labelledby": values.get("aria-labelledby", ""),
                "text": "",
                "image_alt": "",
            }
            self.links.append(link)
            self._link_stack.append(link)
        if tag == "button":
            button = {
                "class": values.get("class", ""),
                "aria-expanded": values.get("aria-expanded", ""),
                "aria-controls": values.get("aria-controls", ""),
                "aria-label": values.get("aria-label", ""),
                "aria-labelledby": values.get("aria-labelledby", ""),
                "text": "",
                "image_alt": "",
            }
            self.buttons.append(button)
            self._button_stack.append(button)
            if "menu-toggle" in values.get("class", "").split():
                self.menu_toggles.append(button)
        if tag == "img":
            self.images.append({"has_alt": "alt" in values, "alt": values.get("alt", "")})
            for link in self._link_stack:
                link["image_alt"] += values.get("alt", "")
            for button in self._button_stack:
                button["image_alt"] += values.get("alt", "")
        if values.get("role") == "img":
            self.role_images.append(values)
        if values.get("aria-controls"):
            self.aria_controls.extend(values["aria-controls"].split())
        if values.get("aria-labelledby"):
            self.aria_labelledby.extend(values["aria-labelledby"].split())
        if values.get("tabindex", "").lstrip("+-").isdigit() and int(values["tabindex"]) > 0:
            self.positive_tabindex.append(values["tabindex"])

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_text += data
        for link in self._link_stack:
            link["text"] += data
        for button in self._button_stack:
            button["text"] += data

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if tag == "label" and self._label_stack:
            self._label_stack.pop()
        if tag == "a" and self._link_stack:
            self._link_stack.pop()
        if tag == "button" and self._button_stack:
            self._button_stack.pop()


def audit_html_page(source: str, relative: str) -> list[str]:
    """Return semantic/accessibility-contract findings for one page."""
    parser = PageAccessibilityParser()
    try:
        parser.feed(source)
        parser.close()
    except Exception as exc:
        return [f"{relative}: HTML parsing failed: {type(exc).__name__}: {exc}"]

    errors: list[str] = []
    ids = set(parser.ids)
    duplicate_ids = sorted(value for value, count in Counter(parser.ids).items() if count > 1)
    if duplicate_ids:
        errors.append(f"{relative}: duplicate id(s): {', '.join(duplicate_ids)}")
    if parser.document_lang != "en":
        errors.append(f"{relative}: document language must be English (lang=en)")
    if not parser.title_text.strip():
        errors.append(f"{relative}: document title must be non-empty")
    if len(parser.main_ids) != 1 or parser.main_ids[0] != "main-content":
        errors.append(f"{relative}: expected exactly one main landmark with id=main-content")
    if parser.headings.count(1) != 1:
        errors.append(f"{relative}: expected exactly one page-level h1")
    previous_level = 0
    for level in parser.headings:
        if previous_level and level > previous_level + 1:
            errors.append(f"{relative}: heading hierarchy skips from h{previous_level} to h{level}")
            break
        previous_level = level

    for link in parser.links:
        if not link["href"].strip():
            errors.append(f"{relative}: anchor is missing a non-empty href")
        named = bool(
            link["aria-label"].strip()
            or link["text"].strip()
            or link["image_alt"].strip()
        )
        if not named:
            named = bool(link["aria-labelledby"].split()) and all(
                target in ids for target in link["aria-labelledby"].split()
            )
        if not named:
            errors.append(f"{relative}: anchor has no accessible name")

    for button in parser.buttons:
        named = bool(
            button["aria-label"].strip()
            or button["text"].strip()
            or button["image_alt"].strip()
        )
        if not named:
            named = bool(button["aria-labelledby"].split()) and all(
                target in ids for target in button["aria-labelledby"].split()
            )
        if not named:
            errors.append(f"{relative}: button has no accessible name")

    explicit_label_targets = {
        str(label["for"]) for label in parser.labels if str(label["for"]).strip()
    }
    for label_target in explicit_label_targets:
        if label_target not in ids:
            errors.append(f"{relative}: label references missing control id: {label_target}")

    for control in parser.controls:
        control_id = str(control["id"])
        labelled = bool(
            control["nested_label"]
            or str(control["aria-label"]).strip()
            or (
                str(control["aria-labelledby"]).split()
                and all(target in ids for target in str(control["aria-labelledby"]).split())
            )
            or (control_id and control_id in explicit_label_targets)
        )
        if not labelled:
            errors.append(
                f"{relative}: {control['tag']} control must have a programmatic label"
            )

    for image in parser.images:
        if not image["has_alt"]:
            errors.append(f"{relative}: img element is missing an alt attribute")
    for role_image in parser.role_images:
        named = bool(role_image.get("aria-label", "").strip()) or (
            bool(role_image.get("aria-labelledby", "").split())
            and all(target in ids for target in role_image["aria-labelledby"].split())
        )
        if not named:
            errors.append(f"{relative}: role=img element must have an accessible name")

    for nav in parser.navs:
        named = bool(nav.get("aria-label", "").strip()) or (
            bool(nav.get("aria-labelledby", "").split())
            and all(target in ids for target in nav["aria-labelledby"].split())
        )
        if not named:
            errors.append(f"{relative}: navigation landmark must have an accessible name")

    for target in parser.aria_controls + parser.aria_labelledby:
        if target not in ids:
            errors.append(f"{relative}: ARIA relationship references missing id: {target}")
    if parser.positive_tabindex:
        errors.append(f"{relative}: positive tabindex values are not permitted")

    if len(parser.menu_toggles) != 1:
        errors.append(f"{relative}: expected exactly one supplied mobile navigation toggle")
    else:
        toggle = parser.menu_toggles[0]
        if toggle["aria-expanded"] != "false":
            errors.append(f"{relative}: mobile navigation toggle must start with aria-expanded=false")
        if toggle["aria-controls"] != "primary-nav":
            errors.append(f"{relative}: mobile navigation toggle must target primary-nav")
        if "Toggle navigation" not in toggle["text"]:
            errors.append(f"{relative}: mobile navigation toggle must retain its text label")
    primary_nav = [
        nav for nav in parser.navs
        if nav.get("id") == "primary-nav"
        and nav.get("aria-label") == "Primary navigation"
    ]
    if len(primary_nav) != 1:
        errors.append(f"{relative}: expected one labelled primary navigation landmark")

    return errors


def audit_kit_accessibility(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    kit = root / "design/owner-controlled-kit-v2"

    for relative in ROUTES:
        path = kit / relative
        if not path.is_file():
            errors.append(f"missing page: {relative}")
            continue
        errors.extend(audit_html_page(path.read_text(encoding="utf-8"), relative))

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
        if not re.search(
            r"@media\s*\(prefers-reduced-motion:\s*reduce\)[\s\S]*?scroll-behavior:\s*auto",
            css,
        ):
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
    print("- all nine pages have a valid document title, language, main landmark and h1")
    print("- anchors, buttons, form controls and navigation landmarks have accessible names")
    print("- image alternatives and all local ARIA ID relationships are present")
    print("- IDs are unique; heading hierarchy is sequential; positive tabindex is absent")
    print("- keyboard focus-visible styling uses currentColor")
    print("- reduced-motion preference disables the existing smooth-scroll behaviour")
    print("- this static audit does not claim screen-reader or brand-contrast acceptance")
    return 0


if __name__ == "__main__":
    sys.exit(main())
