import unittest
from scripts.audit_m2_readiness import audit_m2_readiness


class M2ReadinessAuditTests(unittest.TestCase):
    def test_d016_d017_owner_decisions_and_private_prototype_scope_are_consistent(self):
        result = audit_m2_readiness()
        self.assertEqual(result["errors"], [])
        self.assertEqual(
            result["overall"],
            "M2A_APPROVED_PRIVATE_PROTOTYPE_AUTHORIZED_NO_PRODUCTION",
        )
        self.assertEqual(
            result["states"],
            {
                "M2-A": "REVISION_2_VISUAL_DIRECTION_APPROVED_PRIVATE_PROTOTYPE_ONLY",
                "M2-B": "COHORT_PLAN_APPROVED_FIELDWORK_AUTHORIZATION_PENDING",
                "M2-C": "PLACEHOLDER_APPROACH_APPROVED_GENUINE_SAMPLE_PENDING",
                "M2-D": "OWNER_PRIORITY_APPROVED_AUTOMATION_PASSED_HUMAN_ACCEPTANCE_PENDING",
                "M2-E": "SIX_AREA_PRIVATE_PROTOTYPE_IMPLEMENTATION_AUTHORIZED",
            },
        )
        self.assertIn("M2-B_SEVEN_PERSON_JAPAN_COHORT", result["approved_plans"])
        self.assertIn("M2-E_BUILD_VALIDATE_AND_OWNER_REVIEW_PRIVATE_PROTOTYPE", result["pending_actions"])

    def test_d016_and_prior_d015_are_recorded(self):
        from pathlib import Path
        from scripts.audit_m2_readiness import ROOT

        decisions = (ROOT / "docs/DECISIONS.md").read_text(encoding="utf-8")
        self.assertIn("D-015", decisions)
        self.assertIn("D-016", decisions)
        self.assertIn("D-017", decisions)
        self.assertIn("private non-transactional prototypes", decisions.lower())
        self.assertIn("only after the owner explicitly approves", decisions.lower())


if __name__ == "__main__":
    unittest.main()
