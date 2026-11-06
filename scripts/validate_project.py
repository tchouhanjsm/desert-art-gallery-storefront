#!/usr/bin/env python3
"""Validate the DAG documentation foundation and M1 handoff using stdlib only."""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FOUNDATION_FILES = [
    ".github/ISSUE_TEMPLATE/.gitkeep",
    ".github/workflows/.gitkeep",
    "AGENTS.md",
    "README.md",
    "design/README.md",
    "design/approved/.gitkeep",
    "design/explorations/.gitkeep",
    "design/prototypes/.gitkeep",
    "docs/00-PROJECT-CHARTER.md",
    "docs/01-DESIGN-PHILOSOPHY.md",
    "docs/02-BRAND-IDENTITY.md",
    "docs/03-CREATIVE-DIRECTION.md",
    "docs/04-VISUAL-DESIGN-SYSTEM.md",
    "docs/05-ART-DIRECTION-AND-PHOTOGRAPHY.md",
    "docs/06-CONTENT-STRATEGY.md",
    "docs/07-INFORMATION-ARCHITECTURE.md",
    "docs/08-TECHNICAL-ARCHITECTURE.md",
    "docs/09-QUALITY-AND-ACCEPTANCE.md",
    "docs/10-ROADMAP.md",
    "docs/11-CUSTOMER-AND-MERCHANDISING-STRATEGY.md",
    "docs/12-MERCHANT-OPERATIONS.md",
    "docs/13-DESIGN-REVIEW-PROTOCOL.md",
    "docs/ADR-TEMPLATE.md",
    "docs/AI-BOOTSTRAP-PROMPT.md",
    "docs/AI-WORKING-PROTOCOL.md",
    "docs/DECISIONS.md",
    "docs/OWNER-INPUT-REGISTER.md",
    "docs/REFERENCE-RESEARCH-LOG.md",
]
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


def heading_slug(text: str) -> str:
    slug = text.strip().lower()
    slug = re.sub(r"[`*_]", "", slug)
    slug = re.sub(r"[^a-z0-9\- ]", "", slug)
    return re.sub(r"\s+", "-", slug).strip("-")


def markdown_links(text: str) -> list[str]:
    return [match.group(1).strip() for match in MARKDOWN_LINK_RE.finditer(text)]


def check_markdown_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    last_level = 0
    anchors: set[str] = set()
    for line_no, line in enumerate(text.splitlines(), 1):
        heading = HEADING_RE.match(line)
        if heading:
            level = len(heading.group(1))
            if last_level and level > last_level + 1:
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_no}: heading level jumps from H{last_level} to H{level}"
                )
            last_level = level
            anchors.add(heading_slug(heading.group(2)))
    for target in markdown_links(text):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith(("mailto:", "tel:")):
            continue
        raw_path = unquote(parsed.path)
        fragment = unquote(parsed.fragment)
        dest = (path.parent / raw_path).resolve() if raw_path else path.resolve()
        if not dest.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken internal link: {target}")
            continue
        if fragment and dest.is_file() and dest.suffix.lower() == ".md":
            dest_text = dest.read_text(encoding="utf-8")
            dest_anchors = {
                heading_slug(m.group(2))
                for line in dest_text.splitlines()
                if (m := HEADING_RE.match(line))
            }
            if fragment.lower() not in dest_anchors:
                errors.append(f"{path.relative_to(ROOT)}: broken anchor: {target}")
    return errors


class PrototypeParser(HTMLParser):
    VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.has_viewport = False
        self.has_lang_en = False
        self.images_without_alt: list[str] = []
        self.parse_errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if tag == "html" and attr.get("lang", "").lower() == "en":
            self.has_lang_en = True
        if tag == "meta" and attr.get("name", "").lower() == "viewport":
            self.has_viewport = True
        if tag == "img" and not (attr.get("alt") or "" ).strip():
            self.images_without_alt.append("img element has missing/empty alt text")
        if tag not in self.VOID_TAGS:
            self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in self.VOID_TAGS:
            return
        if tag not in self.stack:
            self.parse_errors.append(f"unexpected closing tag: {tag}")
            return
        if self.stack[-1] != tag:
            self.parse_errors.append(f"mismatched closing tag: {tag}; expected {self.stack[-1]}")
            return
        self.stack.pop()


def validate_project(root: Path = ROOT) -> list[str]:
    errors: list[str] = []

    for item in REQUIRED_FOUNDATION_FILES:
        if not (root / item).is_file():
            errors.append(f"missing required foundation file: {item}")

    markdown_files = sorted(root.rglob("*.md"))
    for path in markdown_files:
        try:
            path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"Markdown is not UTF-8 readable: {path.relative_to(root)} ({exc})")
        errors.extend(check_markdown_file(path))

    readme = (root / "README.md").read_text(encoding="utf-8") if (root / "README.md").exists() else ""
    agents = (root / "AGENTS.md").read_text(encoding="utf-8") if (root / "AGENTS.md").exists() else ""
    decisions = (root / "docs/DECISIONS.md").read_text(encoding="utf-8") if (root / "docs/DECISIONS.md").exists() else ""
    roadmap = (root / "docs/10-ROADMAP.md").read_text(encoding="utf-8") if (root / "docs/10-ROADMAP.md").exists() else ""

    if "M1" not in readme or "owner review" not in readme.lower():
        errors.append("README must identify M1 and disclose that owner review is pending")
    if "English-only" not in agents or "English-only" not in readme:
        errors.append("English-only customer-facing requirement must be explicit in AGENTS.md and README.md")
    if "desert-art-gallery" not in agents or "not inherited" not in agents:
        errors.append("AGENTS.md must explicitly exclude the old repository's frontend/design")
    if "Japan" not in decisions or "jurisdiction" not in decisions or "UNRESOLVED" not in decisions:
        errors.append("Decision register must separate Japan-first from unresolved legal/jurisdiction decisions")
    if "owner selection pending" not in roadmap.lower():
        errors.append("Roadmap must disclose that the M1 creative territory still needs owner selection")

    m1_files = [
        "docs/14-JAPAN-FIRST-CUSTOMER-RESEARCH.md",
        "docs/15-CREATIVE-DIRECTION-OPTIONS.md",
        "docs/16-COMMERCIAL-MODEL-ASSESSMENT.md",
        "docs/M1-OWNER-REVIEW.md",
        "design/explorations/m1-territory-study.html",
    ]
    for item in m1_files:
        if not (root / item).is_file():
            errors.append(f"missing M1 deliverable: {item}")

    prototype_path = root / "design/explorations/m1-territory-study.html"
    if prototype_path.exists():
        parser = PrototypeParser()
        try:
            parser.feed(prototype_path.read_text(encoding="utf-8"))
            parser.close()
        except Exception as exc:  # HTMLParser errors should be reported, not hidden
            errors.append(f"prototype parser error: {exc}")
        if not parser.has_lang_en:
            errors.append("M1 prototype must declare English document language")
        if not parser.has_viewport:
            errors.append("M1 prototype must include a responsive viewport meta tag")
        if parser.stack:
            errors.append(f"M1 prototype has unclosed tags: {parser.stack}")
        errors.extend(parser.parse_errors)
        errors.extend(parser.images_without_alt)
        if "not a product" not in prototype_path.read_text(encoding="utf-8").lower():
            errors.append("M1 prototype must clearly label abstract placeholders as non-product imagery")

    forbidden_scaffolding = [
        "package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock",
        "composer.json", "Dockerfile", "docker-compose.yml", "docker-compose.yaml",
    ]
    for item in forbidden_scaffolding:
        if (root / item).exists():
            errors.append(f"out-of-scope application/infrastructure file introduced: {item}")

    if "Material Archive" not in roadmap or "Collected Colour" not in roadmap:
        errors.append("roadmap must link the actual M1 creative direction outcome")

    return errors


def main() -> int:
    errors = validate_project()
    if errors:
        print(f"DAG project validation: FAILED ({len(errors)} issue(s))")
        for error in errors:
            print(f"- {error}")
        return 1
    print("DAG project validation: PASS")
    print(f"- {len(REQUIRED_FOUNDATION_FILES)} original foundation archive files present")
    print("- Markdown files are UTF-8 readable")
    print("- Internal Markdown links and heading hierarchy validated")
    print("- M0/M1 stage, English-only rule and decision boundaries validated")
    print("- M1 deliverables and responsive visual study validated")
    print("- No application/framework/database/hosting scaffold introduced")
    return 0


if __name__ == "__main__":
    sys.exit(main())
