#!/usr/bin/env python3
"""Read-only audit of current owner M2 decisions and conditional prototype scope."""
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
    "M2-A": ("revision 2 visual direction approved under d-017",),
    "M2-B": ("cohort approved as a plan; fieldwork authorization pending",),
    "M2-C": ("placeholder approach approved; sample pending",),
    "M2-D": ("priority approved; automation passed; human review pending",),
    "M2-E": ("private prototype implementation authorized",),
}


def audit_m2_readiness(root: Path = ROOT) -> dict:
    errors: list[str] = []
    pack_path = root / "docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md"
    inventory_path = root / "docs/PAGE-INVENTORY.md"
    decisions_path = root / "docs/DECISIONS.md"
    proposal_path = root / "docs/27-M2-A-REFERENCE-LED-VISUAL-PROPOSAL.md"
    research_path = root / "docs/28-M2-B-RESEARCH-OPERATIONS-PLAN.md"
    walkthrough_path = root / "docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md"
    token_path = root / "docs/OWNER-TOKEN-INPUT.md"
    required = (
        pack_path, inventory_path, decisions_path, proposal_path,
        research_path, walkthrough_path, token_path,
    )
    if not all(path.is_file() for path in required):
        missing = [str(path.relative_to(root)) for path in required if not path.is_file()]
        return {
            "errors": ["missing required M2 owner-decision/proposal artifact: " + ", ".join(missing)],
            "states": {}, "overall": "INCONSISTENT", "pending_actions": [], "approved_plans": [],
        }

    pack = pack_path.read_text(encoding="utf-8")
    inventory = inventory_path.read_text(encoding="utf-8")
    decisions = decisions_path.read_text(encoding="utf-8")
    proposal = proposal_path.read_text(encoding="utf-8")
    research = research_path.read_text(encoding="utf-8")
    walkthrough = walkthrough_path.read_text(encoding="utf-8")
    token_input = token_path.read_text(encoding="utf-8")

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
        if route not in pack or route not in inventory:
            errors.append(f"current D-014 route missing from M2 pack or inventory: {route}")

    for phrase in ("D-014", "D-015", "D-016", "D-017", "revision 2", "human review pending"):
        if phrase.lower() not in pack.lower():
            errors.append(f"M2 acceptance pack is missing required current decision/evidence: {phrase!r}")

    if "D-016 — Owner authorization for M2 visual proposal" not in decisions:
        errors.append("decision register must include D-016 owner authorization")
    if "POJ Studio is the primary reference" not in decisions or "Macaroni Shoten is secondary" not in decisions:
        errors.append("D-016 must preserve the POJ-primary/Macaroni-secondary hierarchy")
    for area in (
        "Homepage", "Shop and Collections", "Product Detail",
        "About and Makers", "Journal and Stories", "Contact and Support",
    ):
        if area not in decisions or area not in walkthrough:
            errors.append(f"six-area private prototype scope is missing {area!r}")
    if "only after the owner explicitly approves" not in decisions.lower():
        errors.append("D-016 must gate branded prototype implementation on explicit M2-A approval")
    for phrase in ("local/private", "non-transactional", "outside the public repository", "public deployment"):
        if phrase not in decisions.lower() and phrase not in pack.lower():
            errors.append(f"private prototype boundary is missing {phrase!r}")

    for colour in ("#FFFFFF", "#132A3A", "#174F6B", "#E5AD26", "#F3F7F8", "#D4E0E5"):
        if colour not in proposal:
            errors.append(f"visual proposal is missing exact proposed colour {colour}")
    if "OWNER APPROVED FOR PRIVATE PROTOTYPE IMPLEMENTATION" not in proposal or "D-017" not in proposal:
        errors.append("visual proposal must reflect the recorded D-017 approval")
    d017 = decisions.split("### D-017", 1)[1].split("\n### ", 1)[0] if "### D-017" in decisions else ""
    if "M2-A VISUAL DIRECTION APPROVED" not in d017:
        errors.append("D-017 must explicitly approve the M2-A visual direction")
    if "APPROVED FOR PRIVATE PROTOTYPE" not in token_input.upper() or "PENDING OWNER INPUT" not in token_input:
        errors.append("owner token register must distinguish approved prototype values from remaining pending inputs")

    cohort = ("home/interior shoppers", "craft/material enthusiasts", "trade/design professional", "gift")
    for item in cohort:
        if item not in research.lower():
            errors.append(f"research plan is missing approved cohort quota {item!r}")
    for phrase in ("no recruitment", "external contact", "spending", "consent", "retention"):
        if phrase not in research.lower():
            errors.append(f"research plan is missing authorization/privacy boundary {phrase!r}")

    states = {
        "M2-A": "REVISION_2_VISUAL_DIRECTION_APPROVED_PRIVATE_PROTOTYPE_ONLY",
        "M2-B": "COHORT_PLAN_APPROVED_FIELDWORK_AUTHORIZATION_PENDING",
        "M2-C": "PLACEHOLDER_APPROACH_APPROVED_GENUINE_SAMPLE_PENDING",
        "M2-D": "OWNER_PRIORITY_APPROVED_AUTOMATION_PASSED_HUMAN_ACCEPTANCE_PENDING",
        "M2-E": "SIX_AREA_PRIVATE_PROTOTYPE_IMPLEMENTATION_AUTHORIZED",
    }
    return {
        "errors": errors,
        "states": states if not errors else {},
        "overall": (
            "M2A_APPROVED_PRIVATE_PROTOTYPE_AUTHORIZED_NO_PRODUCTION"
            if not errors else "INCONSISTENT"
        ),
        "pending_actions": [
            "M2-B_SEPARATE_FIELDWORK_AUTHORIZATION",
            "M2-C_GENUINE_PRODUCT_PHOTO_AND_FACT_SAMPLE",
            "M2-D_OWNER_WALKTHROUGH_AND_HUMAN_USABILITY_ACCEPTANCE",
            "M2-E_BUILD_VALIDATE_AND_OWNER_REVIEW_PRIVATE_PROTOTYPE",
        ] if not errors else [],
        "approved_plans": [
            "M2-B_SEVEN_PERSON_JAPAN_COHORT",
            "M2-C_LABELLED_PLACEHOLDERS_AND_IMAGE_FRAMES",
            "M2-D_FIVE_JOURNEY_PRIORITY",
            "M2-E_SIX_AREA_PRIVATE_NONTRANSACTIONAL_SCOPE",
        ] if not errors else [],
    }


def main() -> int:
    result = audit_m2_readiness()
    if result["errors"]:
        print(f"DAG v2 M2 decision audit: FAILED ({len(result['errors'])} issue(s))")
        for error in result["errors"]:
            print(f"- {error}")
        return 1

    print("DAG v2 M2 decision audit: PASS — D-016/D-017 approvals, private prototype scope and remaining M2 gates are consistent")
    print("Owner-approved plans: " + ", ".join(result["approved_plans"]))
    print("Pending actions: " + ", ".join(result["pending_actions"]))
    print("Revision 2 tokens are approved for the local/private prototype only; fieldwork, production work and public deployment remain unauthorized.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
