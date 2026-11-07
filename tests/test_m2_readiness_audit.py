from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_m2_readiness import audit_m2_readiness  # noqa: E402


GATES = {
    "M2-A": "M1-A",
    "M2-B": "M1-B",
    "M2-C": "M1-C",
    "M2-D": "M2-D",
    "M2-E": "M2-E",
}


def write_fixture(root: Path, states: dict[str, str], *, references: bool = True) -> None:
    decisions = [
        "# Decisions",
        "This decision confirms the reference relationship only.",
    ]
    owner_rows = [
        "| ID | Topic | Why it matters | Needed by | Status |",
        "|---|---|---|---|---|",
    ]
    pack_rows = [
        "| Gate | Required evidence | Status before M2 |",
        "|---|---|---|",
    ]
    worksheet_rows = [
        "## Gate outcome record",
        "| Gate | Status (Open / Confirmed) | Decision/evidence reference |",
        "|---|---|---|",
    ]
    for index, (gate, owner_id) in enumerate(GATES.items(), start=101):
        state = states[gate]
        reference = f"D-{index:03d}" if references else ""
        if state == "CONFIRMED":
            owner_status = f"Confirmed — {reference}"
            pack_status = f"Confirmed — {reference}"
            worksheet_reference = reference
            decisions.extend([f"### {reference} — {gate}", "Status: CONFIRMED"])
        else:
            owner_status = "Open — awaiting owner input"
            pack_status = "Open — owner confirmation required"
            worksheet_reference = ""
        owner_rows.append(f"| {owner_id} | topic | impact | before M2 | {owner_status} |")
        pack_rows.append(f"| {gate} — gate title | evidence | {pack_status} |")
        worksheet_rows.append(
            f"| {gate} — gate title | {state.title()} | {worksheet_reference} |"
        )

    files = {
        "docs/OWNER-INPUT-REGISTER.md": "\n".join(["# Owner register", *owner_rows]),
        "docs/DECISIONS.md": "\n".join(decisions),
        "docs/10-ROADMAP.md": "# Roadmap\nM2 execution has not started.\n",
        "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md": "\n".join(
            ["# M2 pack", "**Status:** M2 has not started.", *pack_rows]
        ),
        "templates/prototypes/m2-owner-entry-decision.md": "\n".join(
            ["# Worksheet", *worksheet_rows]
        ),
    }
    for relative, content in files.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


class M2ReadinessAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_all_open_gates_are_a_valid_expected_blocked_state(self):
        write_fixture(self.root, {gate: "OPEN" for gate in GATES})
        result = audit_m2_readiness(self.root)
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["overall"], "BLOCKED")
        self.assertEqual(result["open_gates"], list(GATES))

    def test_confirmed_gates_require_matching_decision_references(self):
        write_fixture(self.root, {gate: "CONFIRMED" for gate in GATES})
        result = audit_m2_readiness(self.root)
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["overall"], "OWNER_GATES_CONFIRMED")
        self.assertEqual(result["open_gates"], [])

    def test_mismatched_gate_status_is_rejected(self):
        write_fixture(self.root, {gate: "OPEN" for gate in GATES})
        owner_path = self.root / "docs" / "OWNER-INPUT-REGISTER.md"
        lines = owner_path.read_text(encoding="utf-8").splitlines()
        lines = [
            line.replace("Open — awaiting owner input", "Confirmed — D-103")
            if line.startswith("| M1-C |") else line
            for line in lines
        ]
        owner_path.write_text("\n".join(lines), encoding="utf-8")
        result = audit_m2_readiness(self.root)
        self.assertTrue(any("M2-C: conflicting statuses" in error for error in result["errors"]))
        self.assertEqual(result["overall"], "INCONSISTENT")

    def test_confirmed_gate_without_decision_record_is_rejected(self):
        states = {gate: "OPEN" for gate in GATES}
        states["M2-A"] = "CONFIRMED"
        write_fixture(self.root, states, references=False)
        result = audit_m2_readiness(self.root)
        self.assertTrue(any("M2-A: confirmed status lacks a D-number" in error for error in result["errors"]))

    def test_missing_owner_gate_row_is_rejected(self):
        write_fixture(self.root, {gate: "OPEN" for gate in GATES})
        owner_path = self.root / "docs" / "OWNER-INPUT-REGISTER.md"
        owner_path.write_text(
            "\n".join(
                line for line in owner_path.read_text(encoding="utf-8").splitlines()
                if not line.startswith("| M2-D |")
            ),
            encoding="utf-8",
        )
        result = audit_m2_readiness(self.root)
        self.assertTrue(any("M2-D: owner-input register row M2-D is missing" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
