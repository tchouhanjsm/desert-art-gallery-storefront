from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.private_prototype_journey_review import (
    JOURNEY_LABELS,
    JOURNEY_ROUTE_PATHS,
    VIEWPORT_WIDTHS,
    run_journey_review,
)


class PrivatePrototypeJourneyReviewTests(unittest.TestCase):
    def test_exact_five_owner_prioritised_journeys_are_defined(self):
        self.assertEqual(
            tuple(JOURNEY_ROUTE_PATHS),
            ("discover", "browse", "evaluate", "makers_stories", "contact"),
        )
        self.assertEqual(set(JOURNEY_LABELS), set(JOURNEY_ROUTE_PATHS))
        self.assertEqual(
            JOURNEY_ROUTE_PATHS["discover"],
            ("index.html", "pages/shop.html", "pages/product.html"),
        )
        self.assertEqual(
            JOURNEY_ROUTE_PATHS["browse"],
            ("pages/shop.html", "pages/collection.html", "pages/product.html"),
        )
        self.assertEqual(JOURNEY_ROUTE_PATHS["evaluate"], ("pages/product.html",))
        self.assertEqual(
            JOURNEY_ROUTE_PATHS["makers_stories"],
            ("pages/about.html", "pages/makers.html", "pages/journal.html", "pages/article.html"),
        )
        self.assertEqual(
            JOURNEY_ROUTE_PATHS["contact"],
            ("pages/product.html", "pages/contact.html"),
        )

    def test_every_journey_uses_the_five_owner_review_widths(self):
        self.assertEqual(VIEWPORT_WIDTHS, (390, 430, 768, 1280, 1440))
        self.assertEqual(len(JOURNEY_ROUTE_PATHS) * len(VIEWPORT_WIDTHS), 25)

    def test_review_output_inside_private_prototype_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="dag-journey-root-") as tmp:
            root = Path(tmp)
            output = root / "review-output"
            result = run_journey_review(root, output)
        self.assertFalse(result["ok"])
        self.assertEqual(result["journeys_checked"], 0)
        self.assertIn("outside the prototype source directory", result["errors"][0])
        self.assertFalse(output.exists())

    def test_review_output_inside_public_repository_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="dag-journey-prototype-") as tmp:
            root = Path(tmp)
            output = Path(__file__).resolve().parents[1] / "journey-review-output-test"
            result = run_journey_review(root, output)
        self.assertFalse(result["ok"])
        self.assertEqual(result["journeys_checked"], 0)
        self.assertIn("outside the public repository", result["errors"][0])
        self.assertFalse(output.exists())

    def test_non_supported_viewport_width_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="dag-journey-prototype-") as tmp:
            root = Path(tmp)
            output = Path(tempfile.gettempdir()) / "dag-journey-width-test"
            result = run_journey_review(root, output, widths=(280,))
        self.assertFalse(result["ok"])
        self.assertEqual(result["journeys_checked"], 0)
        self.assertIn("widths >= 320px", result["errors"][0])


if __name__ == "__main__":
    unittest.main()
