from pathlib import Path
import unittest

from scripts.audit_kit_accessibility import ROUTES, audit_kit_accessibility

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "design" / "owner-controlled-kit-v2"


class KitAccessibilityTests(unittest.TestCase):
    def test_static_accessibility_audit_passes(self):
        self.assertEqual(audit_kit_accessibility(ROOT), [])

    def test_all_nine_pages_keep_the_main_landmark_and_page_heading(self):
        for relative in ROUTES:
            source = (KIT / relative).read_text(encoding="utf-8")
            with self.subTest(route=relative):
                self.assertIn('<main id="main-content">', source)
                self.assertEqual(source.count("<h1"), 1)
                self.assertIn('<html lang="en">', source)

    def test_mobile_navigation_remains_named_and_stateful(self):
        for relative in ROUTES:
            source = (KIT / relative).read_text(encoding="utf-8")
            with self.subTest(route=relative):
                self.assertIn('aria-expanded="false"', source)
                self.assertIn('aria-controls="primary-nav"', source)
                self.assertIn('id="primary-nav" aria-label="Primary navigation"', source)
                self.assertIn("Toggle navigation", source)

    def test_focus_indicator_uses_current_colour_not_a_new_brand_value(self):
        css = (KIT / "styles" / "components.css").read_text(encoding="utf-8")
        self.assertIn(":focus-visible", css)
        self.assertIn("outline: 2px solid currentColor", css)
        self.assertIn("outline-offset: 3px", css)
        self.assertNotIn("--dag-color-accent", css.split(":focus-visible", 1)[1])

    def test_reduced_motion_disables_existing_smooth_scroll(self):
        css = (KIT / "styles" / "layout.css").read_text(encoding="utf-8")
        self.assertIn("prefers-reduced-motion: reduce", css)
        self.assertIn("scroll-behavior: auto", css)

    def test_existing_disabled_controls_and_labels_are_preserved(self):
        shop = (KIT / "pages" / "shop.html").read_text(encoding="utf-8")
        collection = (KIT / "pages" / "collection.html").read_text(encoding="utf-8")
        product = (KIT / "pages" / "product.html").read_text(encoding="utf-8")
        contact = (KIT / "pages" / "contact.html").read_text(encoding="utf-8")
        self.assertIn("<label>Sort <select disabled>", shop)
        self.assertIn("<label>Sort <select disabled>", collection)
        self.assertIn('label for="variant"', product)
        self.assertIn("<label>Product or page reference<input disabled", contact)
        self.assertIn("<label>Your message<textarea disabled", contact)


if __name__ == "__main__":
    unittest.main()
