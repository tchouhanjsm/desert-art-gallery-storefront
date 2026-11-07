#!/usr/bin/env python3
"""Read-only audit of DAG v2 owner gates and nine-page structural baseline."""
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


def audit_m2_readiness(root: Path = ROOT) -> dict:
    errors: list[str] = []
    pack_path = root / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md"
    inventory_path = root / "docs/PAGE-INVENTORY.md"
    if not pack_path.is_file() or not inventory_path.is_file():
        return {"errors": ["missing v2 M2 pack or page inventory"], "states": {}, "overall": "INCONSISTENT", "open_gates": list(GATES)}
    pack = pack_path.read_text(encoding="utf-8")
    inventory = inventory_path.read_text(encoding="utf-8")
    for gate in GATES:
        match = re.search(rf"^\|\s*{re.escape(gate)}\b[^\n]*$", pack, re.MULTILINE)
        if not match:
            errors.append(f"missing owner gate row {gate}")
        elif not re.search(r"\bOpen\b", match.group(0), re.IGNORECASE):
            errors.append(f"{gate} must remain explicitly open pending owner action")
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

    open_gates = list(GATES) if not errors else []
    return {
        "errors": errors,
        "states": {gate: "OPEN" for gate in open_gates},
        "overall": "BLOCKED" if open_gates and not errors else ("INCONSISTENT" if errors else "OWNER_GATES_CONFIRMED"),
        "open_gates": open_gates,
    }


def main() -> int:
    result = audit_m2_readiness()
    if result["errors"]:
        print(f"DAG v2 owner-gate audit: FAILED ({len(result['errors'])} issue(s))")
        for error in result["errors"]:
            print(f"- {error}")
        return 1
    print("DAG v2 owner-gate audit: PASS — all five owner gates are present and open")
    print("M2 execution: BLOCKED (expected); D-014 is structural adoption only.")
    print("Open gates: " + ", ".join(result["open_gates"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
