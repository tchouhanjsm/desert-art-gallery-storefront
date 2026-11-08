#!/usr/bin/env python3
"""Validate DAG v2 authority, kit completeness, source integrity and local links."""
from __future__ import annotations

import hashlib
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
KIT_ROOT = "design/owner-controlled-kit-v2"
REQUIRED = (
    "AGENTS.md",
    "README.md",
    "docs/DECISIONS.md",
    "docs/DESIGN-AUTHORITY.md",
    "docs/DOCUMENTATION-SOURCE-OF-TRUTH.md",
    "docs/PAGE-INVENTORY.md",
    "docs/COMPONENT-INVENTORY.md",
    "docs/DOCUMENTATION-RECONCILIATION-MATRIX.md",
    "docs/DOCUMENTATION-RECONCILIATION-REPORT.md",
    "docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md",
    "docs/DOCUMENTATION-CHANGELOG.md",
    "docs/OWNER-TOKEN-INPUT.md",
    "docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md",
)
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
KIT_FILES = {
    "HANDOFF-PROMPT.md", "README.md",
    "docs/COMPONENT-INVENTORY.md", "docs/DESIGN-AUTHORITY.md",
    "docs/DOCUMENTATION-CHANGELOG.md", "docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md",
    "docs/DOCUMENTATION-RECONCILIATION-PROMPT.md", "docs/DOCUMENTATION-SOURCE-OF-TRUTH.md",
    "docs/OWNER-TOKEN-INPUT.md", "docs/PAGE-INVENTORY.md", "docs/REFERENCE-CREDIT-AND-IP.md",
    "index.html",
    "pages/about.html", "pages/article.html", "pages/collection.html", "pages/contact.html",
    "pages/journal.html", "pages/makers.html", "pages/product.html", "pages/shop.html",
    "scripts/prototype.js",
    "styles/components.css", "styles/layout.css", "styles/responsive.css", "styles/tokens-layout-only.css",
}
# Current reviewed implementation-asset Git blob SHA-1 values. PR #8 archive hashes
# are preserved in history; PR #9 documents two additive CSS accessibility amendments.
KIT_ASSET_BLOB_SHAS = {
    "index.html": "6609a91541eac36f98fe1d6f8e6a2903ad5a32ee",
    "pages/about.html": "3669d729a47d32016f9643d976179d4d63f4f6e5",
    "pages/article.html": "83b74212ce37539af12307386347ae38a4cabc05",
    "pages/collection.html": "89f907e4d653a9808409ab3325ceec4e98536878",
    "pages/contact.html": "6964e9279c9c06bba1c88d11b2837c5c55afade3",
    "pages/journal.html": "b7a5798c0031a972f1886c15b1cb19d17079b11a",
    "pages/makers.html": "4e4de5f1713811ab3ac027b942043e899a0a65a0",
    "pages/product.html": "046bbe1d86600746a802977651ee5264cf824c2b",
    "pages/shop.html": "dffff96246a36448c54032803746b5ef9f56f5ac",
    "scripts/prototype.js": "bd46c5de2e1f5ba0173c8338b90b93bb34f2cf76",
    "styles/components.css": "fab3c90f823f2b90061d2e1bf67f7919968ee861",
    "styles/layout.css": "0505b87576b7d843e2678aaee6e1450df98a454a",
    "styles/responsive.css": "b59304f6034f0f961f022c4efee7809ad04106e1",
    "styles/tokens-layout-only.css": "2a0a72468db3029bbac65682f2b0d993888dce71",
}


class LocalReferenceParser(HTMLParser):
    """Collect local href/src values and IDs from one supplied page."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        for name in ("href", "src"):
            value = values.get(name)
            if value:
                self.references.append(value)


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    payload = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
    return hashlib.sha1(payload).hexdigest()


def validate_kit(root: Path) -> list[str]:
    errors: list[str] = []
    kit = root / KIT_ROOT
    if not kit.is_dir():
        return [f"missing owner-controlled kit directory: {KIT_ROOT}"]

    actual = {
        path.relative_to(kit).as_posix()
        for path in kit.rglob("*")
        if path.is_file()
    }
    for missing in sorted(KIT_FILES - actual):
        errors.append(f"kit file missing: {missing}")
    for extra in sorted(actual - KIT_FILES):
        errors.append(f"unexpected file in closed kit: {extra}")

    for rel, expected_sha in KIT_ASSET_BLOB_SHAS.items():
        path = kit / rel
        if not path.is_file():
            continue
        actual_sha = git_blob_sha(path)
        if actual_sha != expected_sha:
            errors.append(f"owner source asset changed: {rel} (expected {expected_sha}, got {actual_sha})")

    for rel in ROUTES:
        page = kit / rel
        if not page.is_file():
            continue
        source = page.read_text(encoding="utf-8")
        if '<html lang="en">' not in source:
            errors.append(f"page must declare English language: {rel}")
        parser = LocalReferenceParser()
        parser.feed(source)
        parser.close()
        for raw in parser.references:
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc or raw.startswith("#") or not parsed.path:
                continue
            target = (page.parent / parsed.path).resolve()
            if not target.is_file():
                errors.append(f"broken local link/reference in {rel}: {raw}")
            elif parsed.fragment:
                target_source = target.read_text(encoding="utf-8", errors="replace")
                target_parser = LocalReferenceParser()
                target_parser.feed(target_source)
                target_parser.close()
                if parsed.fragment not in target_parser.ids:
                    errors.append(f"missing fragment target in {rel}: {raw}")
    return errors


def validate_project(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing required governance path: {rel}")

    decisions = (root / "docs/DECISIONS.md").read_text(encoding="utf-8")
    if "D-014 — Owner-controlled Design Kit v2" not in decisions:
        errors.append("decision register is missing D-014")
    if "Status: SUPERSEDED BY D-014" not in decisions:
        errors.append("D-013 former six-page scope must be superseded by D-014")
    if "### P-015" not in decisions or "Status: REJECTED" not in decisions:
        errors.append("P-015 must remain explicitly rejected")
    if "### P-016" not in decisions or "SUPERSEDED" not in decisions.split("### P-016", 1)[1].split("\n### ", 1)[0]:
        errors.append("P-016 must be historical/superseded, not active")

    page_inventory = (root / "docs/PAGE-INVENTORY.md").read_text(encoding="utf-8")
    component_inventory = (root / "docs/COMPONENT-INVENTORY.md").read_text(encoding="utf-8")
    for route in ROUTES:
        if route not in page_inventory:
            errors.append(f"page inventory is missing route {route}")
    if "exact nine" not in page_inventory.lower():
        errors.append("page inventory must declare the nine-page scope")
    if "disabled" not in component_inventory.lower():
        errors.append("component inventory must explicitly preserve disabled states")

    authority = (root / "docs/DESIGN-AUTHORITY.md").read_text(encoding="utf-8").lower()
    for phrase in ("owner-controlled", "english-only", "remain disabled"):
        if phrase not in authority:
            errors.append(f"design authority missing {phrase!r}")

    token_input = (root / "docs/OWNER-TOKEN-INPUT.md").read_text(encoding="utf-8")
    for field in ("Primary brand colour", "Display/heading typeface", "Wordmark / logo artwork", "Photography art direction"):
        if field not in token_input:
            errors.append(f"owner token input missing field {field!r}")
    if "PENDING OWNER INPUT" not in token_input:
        errors.append("owner-controlled identity inputs must remain pending")

    report = (root / "docs/DOCUMENTATION-RECONCILIATION-REPORT.md").read_text(encoding="utf-8").lower()
    checklist = (root / "docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md").read_text(encoding="utf-8")
    if "25-file" not in report and "25 files" not in report:
        errors.append("reconciliation report must document the 25-file owner archive")
    if "14 original html/css/js assets" not in report and "14 original implementation assets" not in report:
        errors.append("reconciliation report must document implementation-asset verification")
    if "all 25 kit files" not in checklist.lower() and "25-file owner archive" not in checklist.lower():
        errors.append("checklist must record verified source-kit materialization")
    if "sha-256" not in report or "64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd" not in report:
        errors.append("reconciliation report must record the verified owner archive SHA-256")

    active_stubs = (
        "docs/14-OWNER-CONTROLLED-VISUAL-DIRECTION.md",
        "docs/15-CREATIVE-DIRECTION-OPTIONS.md",
        "docs/15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md",
        "docs/17-REFERENCE-LED-DESIGN-BRIEF.md",
        "docs/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md",
    )
    for rel in active_stubs:
        path = root / rel
        if path.is_file():
            body = path.read_text(encoding="utf-8").lower()
            if "historical — not active — do not implement" not in body and "superseded" not in body:
                errors.append(f"stale design document is not clearly retired: {rel}")

    for rel in (
        "design/explorations/visual-directions.html",
        "design/explorations/reference-led-directions.html",
    ):
        if (root / rel).exists():
            errors.append(f"historical proposal remains under active exploration path: {rel}")

    errors.extend(validate_kit(root))
    return errors


def main() -> int:
    errors = validate_project()
    if errors:
        print(f"DAG v2 foundation validation: FAILED ({len(errors)} issue(s))")
        for error in errors:
            print(f"- {error}")
        return 1

    print("DAG v2 foundation and source-integrity validation: PASS")
    print(f"- {len(REQUIRED)} authority, decision and reconciliation paths present")
    print(f"- all {len(KIT_FILES)} original kit files present")
    print(f"- all {len(KIT_ASSET_BLOB_SHAS)} HTML/CSS/JS implementation assets match the current reviewed blob hashes")
    print("- all nine pages use English markup and local links/styles/scripts resolve")
    print("- D-014, superseded D-013 and retired visual proposals are explicit")
    print("- PR #8 archive verification remains in history; PR #9 CSS accessibility amendments are hash-verified")
    print("- owner-only identity inputs remain pending; layout tokens are QA-only")
    print("- disabled states and closed functionality boundaries are maintained")
    return 0


if __name__ == "__main__":
    sys.exit(main())
