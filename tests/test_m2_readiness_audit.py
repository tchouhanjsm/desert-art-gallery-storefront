import unittest
from scripts.audit_m2_readiness import audit_m2_readiness


class M2ReadinessAuditTests(unittest.TestCase):
    def test_d016_owner_decisions_and_conditional_prototype_scope_are_consistent(self):
        result = audit_m2_readiness()
        self.assertEqual(result["errors"], [])
        self.assertEqual(
            result["overall"],
            "M2_A_VISUAL_APPROVAL_RECORDED_PRIVATE_PROTOTYPE_IN_PROGRESS",
        )
        self.assertEqual(
            result["states"],
            {
                "M2-A": "REVISION2_OWNER_APPROVED_PRIVATE_PROTOTYPE_ONLY",
                "M2-B": "COHORT_PLAN_APPROVED_FIELDWORK_AUTHORIZATION_PENDING",
                "M2-C": "PLACEHOLDER_APPROACH_APPROVED_GENUINE_SAMPLE_PENDING",
                "M2-D": "OWNER_PRIORITY_APPROVED_AUTOMATION_PASSED_HUMAN_ACCEPTANCE_PENDING",
                "M2-E": "SIX_AREA_PRIVATE_PROTOTYPE_IMPLEMENTED_OWNER_REVIEW_PENDING",
            },
        )
        self.assertIn("M2-B_SEVEN_PERSON_JAPAN_COHORT", result["approved_plans"])
        self.assertIn("M2-E_OWNER_WALKTHROUGH_AND_RENDERED_BROWSER_ACCEPTANCE", result["pending_actions"])

    def test_d016_and_prior_d015_are_recorded(self):
        from pathlib import Path
        from scripts.audit_m2_readiness import ROOT

        decisions = (ROOT / "docs/DECISIONS.md").read_text(encoding="utf-8")
        self.assertIn("D-015", decisions)
        self.assertIn("D-016", decisions)
        self.assertIn("private non-transactional prototypes", decisions.lower())
        self.assertIn("only after the owner explicitly approves", decisions.lower())


if __name__ == "__main__":
    unittest.main()
