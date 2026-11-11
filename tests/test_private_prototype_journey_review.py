from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.private_prototype_journey_review import (
    JOURNEY_LABELS,
    BREADCRUMB_ROUTES,
    CONTENT_SLOT_COUNTS,
    JOURNEY_ROUTE_PATHS,
    NAV_CURRENT_BY_ROUTE,
    VIEWPORT_WIDTHS,
    audit_d017_visual_css,
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


    def test_all_nine_routes_have_an_explicit_approved_navigation_state(self):
        self.assertEqual(
            tuple(NAV_CURRENT_BY_ROUTE),
            (
                "index.html", "pages/shop.html", "pages/collection.html",
                "pages/product.html", "pages/about.html", "pages/makers.html",
                "pages/journal.html", "pages/article.html", "pages/contact.html",
            ),
        )
        self.assertIsNone(NAV_CURRENT_BY_ROUTE["index.html"])
        self.assertEqual(NAV_CURRENT_BY_ROUTE["pages/shop.html"][1], "page")
        self.assertEqual(NAV_CURRENT_BY_ROUTE["pages/product.html"][1], "location")
        self.assertEqual(NAV_CURRENT_BY_ROUTE["pages/article.html"][1], "location")


    def test_image_slot_counts_match_the_closed_nine_page_inventory(self):
        self.assertEqual(
            CONTENT_SLOT_COUNTS,
            {
                "index.html": 11,
                "pages/shop.html": 6,
                "pages/collection.html": 3,
                "pages/product.html": 4,
                "pages/about.html": 2,
                "pages/makers.html": 1,
                "pages/journal.html": 6,
                "pages/article.html": 1,
                "pages/contact.html": 0,
            },
        )
        self.assertEqual(len(CONTENT_SLOT_COUNTS), 9)

    def test_breadcrumb_landmarks_are_limited_to_existing_breadcrumb_pages(self):
        self.assertEqual(
            BREADCRUMB_ROUTES,
            frozenset({"pages/collection.html", "pages/product.html", "pages/article.html"}),
        )
        self.assertTrue(BREADCRUMB_ROUTES.issubset(CONTENT_SLOT_COUNTS))

    def test_every_journey_uses_the_five_owner_review_widths(self):
        self.assertEqual(VIEWPORT_WIDTHS, (390, 430, 768, 1280, 1440))
        self.assertEqual(len(JOURNEY_ROUTE_PATHS) * len(VIEWPORT_WIDTHS), 25)


    def test_d017_visual_css_accepts_the_approved_palette_and_layout_values(self):
        result = audit_d017_visual_css(self._approved_css())
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["palette_token_count"], 6)

    def test_d017_visual_css_rejects_unapproved_colour_values(self):
        css = self._approved_css().replace("#E5AD26", "#B07A40")
        result = audit_d017_visual_css(css)
        self.assertFalse(result["ok"])
        self.assertTrue(any("unapproved colour" in error for error in result["errors"]))

    def test_d017_visual_css_rejects_gradients_and_shadows(self):
        css = self._approved_css() + " .frame { background: linear-gradient(#FFFFFF, #F3F7F8); box-shadow: 0 1px 2px #132A3A; }"
        result = audit_d017_visual_css(css)
        self.assertFalse(result["ok"])
        self.assertTrue(any("gradients" in error for error in result["errors"]))
        self.assertTrue(any("drop shadows" in error for error in result["errors"]))

    def test_d017_visual_css_rejects_quoted_remote_assets(self):
        css = self._approved_css() + ' .frame { background-image: url("https://example.invalid/image.svg"); }'
        result = audit_d017_visual_css(css)
        self.assertFalse(result["ok"])
        self.assertTrue(any("remote CSS assets" in error for error in result["errors"]))

    @staticmethod
    def _approved_css():
        return """
        :root {
          --dag-canvas: #FFFFFF; --dag-ink: #132A3A; --dag-brand: #174F6B;
          --dag-accent: #E5AD26; --dag-surface: #F3F7F8; --dag-border: #D4E0E5;
          --font-display: "Source Serif 4", Georgia, serif; --font-body: Inter, Arial, sans-serif;
          --content-max: 1440px; --gutter: clamp(20px, 4vw, 56px); --section-gap: 80px;
        }
        h1 { font-size: 44px; } h2 { font-size: 32px; line-height: 1.18; }
        h3 { font: 600 22px/1.25 var(--font-body); }
        .hero { font-size: clamp(34px, 3.9vw, 56px); }
        .hero-frame { aspect-ratio: 16 / 9; } .product-frame { aspect-ratio: 4 / 5; }
        .thumb-frame { aspect-ratio: 1; }
        .primary-nav a[aria-current] { text-decoration-thickness: 2px; }
        """

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

    def test_journey_review_refuses_to_overwrite_existing_private_reports(self):
        with tempfile.TemporaryDirectory(prefix="dag-journey-output-") as tmp:
            base = Path(tmp)
            prototype = base / "prototype"
            prototype.mkdir()
            output = base / "review"
            output.mkdir()
            existing = output / "private-prototype-journeys.json"
            existing.write_text('{"owner":"keep"}', encoding="utf-8")
            result = run_journey_review(prototype, output)
        self.assertFalse(result["ok"])
        self.assertEqual(result["journeys_checked"], 0)
        self.assertTrue(any("refusing to overwrite" in error for error in result["errors"]))
        self.assertEqual(existing.read_text(encoding="utf-8"), '{"owner":"keep"}')

    def test_journey_review_rejects_symlinked_output_directory(self):
        with tempfile.TemporaryDirectory(prefix="dag-journey-output-link-") as tmp:
            base = Path(tmp)
            prototype = base / "prototype"
            prototype.mkdir()
            target = base / "target"
            target.mkdir()
            link = base / "review-link"
            try:
                link.symlink_to(target, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("directory symlinks are unavailable on this runner")
            result = run_journey_review(prototype, link)
        self.assertFalse(result["ok"])
        self.assertEqual(result["journeys_checked"], 0)
        self.assertTrue(any("symbolic link" in error for error in result["errors"]))
        self.assertEqual(list(target.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
