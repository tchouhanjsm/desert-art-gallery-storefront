import unittest
from scripts.audit_m2_readiness import audit_m2_readiness


class M2ReadinessAuditTests(unittest.TestCase):
    def test_five_gate_dispositions_and_bounded_authorization_are_consistent(self):
        result = audit_m2_readiness()
        self.assertEqual(result["errors"], [])
        self.assertEqual(
            result["overall"],
            "BOUNDED_REVIEW_AUTHORIZED_WITH_OWNER_INPUTS_PENDING",
        )
        self.assertEqual(result["open_gates"], ["M2-A", "M2-B", "M2-C", "M2-D"])
        self.assertEqual(result["authorized_gates"], ["M2-E"])
        self.assertEqual(
            result["states"],
            {
                "M2-A": "BLOCKED_OWNER_INPUT",
                "M2-B": "RECOMMENDATION_PENDING_OWNER_ADOPTION",
                "M2-C": "BLOCKED_SOURCE_EVIDENCE",
                "M2-D": "AUTOMATION_READY_OWNER_ACCEPTANCE_PENDING",
                "M2-E": "AUTHORIZED_BOUNDED_REVIEW",
            },
        )

    def test_d015_is_recorded_in_the_owner_decision_register(self):
        from pathlib import Path
        from scripts.audit_m2_readiness import ROOT

        decisions = (ROOT / "docs/DECISIONS.md").read_text(encoding="utf-8")
        self.assertIn("D-015", decisions)
        self.assertIn("limited non-production review scope", decisions.lower())
        self.assertIn("bounded structural review", decisions.lower())


if __name__ == "__main__":
    unittest.main()
