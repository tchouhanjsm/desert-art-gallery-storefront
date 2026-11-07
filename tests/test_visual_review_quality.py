from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OwnerControlledIdentityTests(unittest.TestCase):
    def test_owner_identity_inputs_remain_pending(self):
        source = (ROOT / "docs/OWNER-TOKEN-INPUT.md").read_text(encoding="utf-8")
        self.assertIn("PENDING OWNER INPUT", source)
        self.assertIn("Primary brand colour", source)
        self.assertIn("Display/heading typeface", source)
        self.assertIn("Wordmark / logo artwork", source)
        self.assertIn("Photography art direction", source)

    def test_layout_tokens_are_explicitly_qa_only(self):
        source = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("layout-only", source)
        self.assertIn("qa fallback only", source)
        self.assertIn("not a dag palette", source)

    def test_rejected_and_superseded_proposals_are_not_active(self):
        decisions = (ROOT / "docs/DECISIONS.md").read_text(encoding="utf-8")
        self.assertIn("P-015", decisions)
        self.assertIn("Status: REJECTED", decisions)
        p016 = decisions.split("### P-016", 1)[1].split("\n### ", 1)[0]
        self.assertIn("SUPERSEDED", p016)
        stub = (ROOT / "docs/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md").read_text(encoding="utf-8")
        self.assertIn("HISTORICAL — NOT ACTIVE — DO NOT IMPLEMENT", stub)


if __name__ == "__main__":
    unittest.main()
