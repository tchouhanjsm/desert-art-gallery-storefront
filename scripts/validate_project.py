#!/usr/bin/env python3
"""Validate DAG v2 documentation authority and reconciliation state.

This validator deliberately distinguishes a coherent governance baseline from
materialization of the owner-supplied source kit. A passing documentation
check does not authorize merging while the reconciliation checklist has
unclosed source-installation items.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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
    for phrase in ("owner-controlled", "english-only", "must remain disabled"):
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
    if "not yet present" not in report or "not ready to merge" not in report:
        errors.append("reconciliation report must disclose incomplete kit materialization")
    if "[ ] All 25 original kit files" not in checklist:
        errors.append("checklist must keep source-kit materialization visibly open")

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

    active_boards = (
        "design/explorations/visual-directions.html",
        "design/explorations/reference-led-directions.html",
    )
    for rel in active_boards:
        if (root / rel).exists():
            errors.append(f"historical proposal remains under active exploration path: {rel}")

    return errors


def main() -> int:
    errors = validate_project()
    if errors:
        print(f"DAG documentation validation: FAILED ({len(errors)} issue(s))")
        for error in errors:
            print(f"- {error}")
        return 1

    kit_path = ROOT / "design/owner-controlled-kit-v2"
    print("DAG documentation and authority validation: PASS")
    print(f"- {len(REQUIRED)} governance/report paths present")
    print("- D-014, superseded D-013 and retired visual proposals are explicit")
    print("- nine-page inventory and owner-only token inputs are consistent")
    if not kit_path.is_dir():
        print("SOURCE KIT MATERIALIZATION: BLOCKED — directory is not yet present")
        print("This is an expected draft-PR state, not evidence of kit installation.")
    else:
        print("SOURCE KIT DIRECTORY: present; byte-level archive verification is still required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
