#!/usr/bin/env python3
"""Read-only cross-document audit for DAG's owner-controlled M2 entry gates."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER_ROW_BY_GATE = {
    "M2-A": "M1-A",
    "M2-B": "M1-B",
    "M2-C": "M1-C",
    "M2-D": "M2-D",
    "M2-E": "M2-E",
}
GATES = tuple(OWNER_ROW_BY_GATE)


def pipe_cells(line: str) -> list[str]:
    if not line.lstrip().startswith("|"):
        return []
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def find_row(source: str, key: str, *, prefix: bool = False) -> list[str] | None:
    for line in source.splitlines():
        cells = pipe_cells(line)
        if not cells:
            continue
        first = cells[0]
        if (first.startswith(key) if prefix else first == key):
            return cells
    return None


def find_worksheet_gate_row(source: str, gate: str) -> list[str] | None:
    marker = "## Gate outcome record"
    if marker not in source:
        return None
    return find_row(source.split(marker, 1)[1], gate, prefix=True)


def classify_status(value: str) -> str | None:
    match = re.match(r"^\s*(Open|Confirmed)\b", value, re.IGNORECASE)
    return match.group(1).upper() if match else None


def decision_ids(value: str) -> set[str]:
    return set(re.findall(r"\bD-\d{3}\b", value))


def audit_m2_readiness(root: Path = ROOT) -> dict:
    """Compare each gate in three owner-controlled sources; never edit files."""
    required = {
        "owner": root / "docs" / "OWNER-INPUT-REGISTER.md",
        "decisions": root / "docs" / "DECISIONS.md",
        "roadmap": root / "docs" / "10-ROADMAP.md",
        "pack": root / "docs" / "23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md",
        "worksheet": root / "templates" / "prototypes" / "m2-owner-entry-decision.md",
    }
    missing = [name for name, path in required.items() if not path.is_file()]
    if missing:
        return {
            "errors": [f"missing required source: {name}" for name in missing],
            "states": {},
            "overall": "INCONSISTENT",
            "open_gates": list(GATES),
        }

    sources = {name: path.read_text(encoding="utf-8") for name, path in required.items()}
    errors: list[str] = []
    decision_headings = set(
        re.findall(r"^###\s+(D-\d{3})\b", sources["decisions"], re.MULTILINE)
    )
    if "confirms the reference relationship only" not in sources["decisions"].lower():
        errors.append("D-010 must remain a reference-hierarchy decision, not visual approval")

    states: dict[str, str] = {}
    for gate, owner_row_id in OWNER_ROW_BY_GATE.items():
        owner_row = find_row(sources["owner"], owner_row_id)
        pack_row = find_row(sources["pack"], gate, prefix=True)
        worksheet_row = find_worksheet_gate_row(sources["worksheet"], gate)

        if owner_row is None or len(owner_row) < 5:
            errors.append(f"{gate}: owner-input register row {owner_row_id} is missing or malformed")
            continue
        if pack_row is None or len(pack_row) < 3:
            errors.append(f"{gate}: M2 acceptance table row is missing or malformed")
            continue
        if worksheet_row is None or len(worksheet_row) < 3:
            errors.append(f"{gate}: worksheet outcome row is missing or malformed")
            continue

        owner_value = owner_row[4]
        pack_value = pack_row[2]
        worksheet_value = worksheet_row[1]
        worksheet_reference = worksheet_row[2]
        observed = {
            "owner-input register": classify_status(owner_value),
            "M2 acceptance pack": classify_status(pack_value),
            "owner worksheet": classify_status(worksheet_value),
        }
        if any(value is None for value in observed.values()):
            errors.append(
                f"{gate}: status must begin with Open or Confirmed in all three records ({observed})"
            )
            continue
        if len(set(observed.values())) != 1:
            errors.append(f"{gate}: conflicting statuses across records ({observed})")
            continue

        state = observed["owner-input register"]
        states[gate] = state
        if state == "CONFIRMED":
            references = {
                "owner-input register": decision_ids(owner_value),
                "M2 acceptance pack": decision_ids(pack_value),
                "owner worksheet": decision_ids(worksheet_reference),
            }
            for source_name, ids in references.items():
                if not ids:
                    errors.append(f"{gate}: confirmed status lacks a D-number in {source_name}")
                elif not ids.issubset(decision_headings):
                    errors.append(
                        f"{gate}: {source_name} references missing decision(s): "
                        + ", ".join(sorted(ids - decision_headings))
                    )

    open_gates = [gate for gate in GATES if states.get(gate) == "OPEN"]
    if open_gates:
        if "m2 has not started" not in sources["pack"].lower():
            errors.append("open owner gates conflict with the M2 pack's execution status")
        if "m2 execution has not started" not in sources["roadmap"].lower():
            errors.append("open owner gates conflict with the roadmap's execution status")

    if errors:
        overall = "INCONSISTENT"
    elif open_gates:
        overall = "BLOCKED"
    else:
        overall = "OWNER_GATES_CONFIRMED"

    return {"errors": errors, "states": states, "overall": overall, "open_gates": open_gates}


def main() -> int:
    result = audit_m2_readiness()
    if result["errors"]:
        print(f"M2 readiness audit: FAILED ({len(result['errors'])} issue(s))")
        for error in result["errors"]:
            print(f"- {error}")
        return 1

    print("M2 readiness audit: PASS — owner records are consistent")
    for gate in GATES:
        print(f"- {gate}: {result['states'][gate]}")
    if result["overall"] == "BLOCKED":
        print(
            "M2 execution: BLOCKED (expected); owner decisions remain open for "
            + ", ".join(result["open_gates"])
        )
    else:
        print(
            "Owner gates: CONFIRMED in the recorded sources. This audit does not "
            "authorize M2; obtain explicit owner authorization for the first route."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
