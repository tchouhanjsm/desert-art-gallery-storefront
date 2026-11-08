#!/usr/bin/env python3
"""Read-only audit of DAG v2 owner gates and the D-015 review authorization."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATES = ("M2-A", "M2-B", "M2-C", "M2-D", "M2-E")
ROUTES = (
    "index.html", "pages/shop.html", "pages/collection.html",
    "pages/product.html", "pages/about.html", "pages/makers.html",
    "pages/journal.html", "pages/article.html", "pages/contact.html",
)
EXPECTED_DISPOSITIONS = {
    "M2-A": ("blocked on owner input",),
    "M2-B": ("recommendation prepared", "owner adoption pending"),
    "M2-C": ("blocked on sample/evidence",),
    "M2-D": ("execution matrix implemented", "owner priority/human acceptance pending"),
    "M2-E": ("authorized for bounded structural review only",),
}


def audit_m2_readiness(root: Path = ROOT) -> dict:
    errors: list[str] = []
    pack_path = root / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md"
    inventory_path = root / "docs/PAGE-INVENTORY.md"
    decisions_path = root / "docs/DECISIONS.md"
    if not pack_path.is_file() or not inventory_path.is_file() or not decisions_path.is_file():
        return {
            "errors": ["missing v2 M2 pack, page inventory or decision register"],
            "states": {},
            "overall": "INCONSISTENT",
            "open_gates": list(GATES),
            "authorized_gates": [],
        }

    pack = pack_path.read_text(encoding="utf-8")
    inventory = inventory_path.read_text(encoding="utf-8")
    decisions = decisions_path.read_text(encoding="utf-8")

    for gate in GATES:
        match = re.search(rf"^\|\s*{re.escape(gate)}\b[^\n]*$", pack, re.MULTILINE)
        if not match:
            errors.append(f"missing owner gate row {gate}")
            continue
        row = match.group(0).lower()
        for phrase in EXPECTED_DISPOSITIONS[gate]:
            if phrase not in row:
                errors.append(f"{gate} disposition is missing expected text: {phrase!r}")

    for route in ROUTES:
        if route not in pack:
            errors.append(f"M2 pack missing current route {route}")
        if route not in inventory:
            errors.append(f"page inventory missing current route {route}")

    if "D-014" not in pack:
        errors.append("M2 pack must reference D-014")
    if "D-013" not in pack or "superseded" not in pack.lower():
        errors.append("M2 pack must record the former six-page scope as superseded")
    if "no production application development" not in pack.lower():
        errors.append("M2 pack must preserve the no-production authorization boundary")
    if "D-015" not in decisions or "limited non-production review scope" not in decisions.lower():
        errors.append("decision register must record D-015 limited non-production review authorization")
    if "D-015" in decisions and "bounded M2 structural journey-review implementation" not in decisions.lower():
        errors.append("D-015 must define the bounded M2 structural journey-review implementation")

    states = {
        "M2-A": "BLOCKED_OWNER_INPUT",
        "M2-B": "RECOMMENDATION_PENDING_OWNER_ADOPTION",
        "M2-C": "BLOCKED_SOURCE_EVIDENCE",
        "M2-D": "AUTOMATION_READY_OWNER_ACCEPTANCE_PENDING",
        "M2-E": "AUTHORIZED_BOUNDED_REVIEW",
    }
    open_gates = ["M2-A", "M2-B", "M2-C", "M2-D"]
    authorized_gates = ["M2-E"] if not errors else []
    return {
        "errors": errors,
        "states": states if not errors else {},
        "overall": "BOUNDED_REVIEW_AUTHORIZED_WITH_OWNER_INPUTS_PENDING" if not errors else "INCONSISTENT",
        "open_gates": open_gates if not errors else [],
        "authorized_gates": authorized_gates,
    }


def main() -> int:
    result = audit_m2_readiness()
    if result["errors"]:
        print(f"DAG v2 M2 gate audit: FAILED ({len(result['errors'])} issue(s))")
        for error in result["errors"]:
            print(f"- {error}")
        return 1

    print("DAG v2 M2 gate audit: PASS — five dispositions and D-015 authorization are consistent")
    print("Bounded non-production structural review: AUTHORIZED (M2-E)")
    print("Owner/human acceptance remains pending: " + ", ".join(result["open_gates"]))
    print("Branded identity, genuine product/photo evidence, external research and production work remain gated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
