from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs" / "18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md"


def relative_luminance(hex_color: str) -> float:
    """Return WCAG 2.x relative luminance for a six-digit sRGB HEX colour."""
    value = hex_color.lstrip("#")
    if not re.fullmatch(r"[0-9A-Fa-f]{6}", value):
        raise ValueError(f"Expected a six-digit HEX colour, got {hex_color!r}")
    channels = [int(value[index:index + 2], 16) / 255 for index in (0, 2, 4)]
    linear = [
        channel / 12.92 if channel <= 0.04045
        else ((channel + 0.055) / 1.055) ** 2.4
        for channel in channels
    ]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(first: str, second: str) -> float:
    luminances = sorted(
        (relative_luminance(first), relative_luminance(second)),
        reverse=True,
    )
    return (luminances[0] + 0.05) / (luminances[1] + 0.05)


def visual_options(source: str):
    pattern = re.compile(
        r"^## Option \d+ — (?P<title>[^\n]+)\n(?P<body>.*?)(?=^## Option \d+ — |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    for match in pattern.finditer(source):
        body = match.group("body")
        palette = {
            name.strip(): colour.upper()
            for _, name, colour in re.findall(
                r"^\|\s*([^|]+)\|\s*([^|]+)\|\s*`?(#[0-9A-Fa-f]{6})`?\s*\|$",
                body,
                re.MULTILINE,
            )
        }
        claims = re.findall(
            r"^\s*-\s*([^/\n:]+)/([^:\n]+):\s*([0-9]+(?:\.[0-9]+)?):1([^\n]*)$",
            body,
            re.MULTILINE,
        )
        yield match.group("title"), palette, claims


class VisualReviewContrastTests(unittest.TestCase):
    def test_every_documented_contrast_ratio_matches_its_hex_values(self):
        source = SPEC.read_text(encoding="utf-8")
        options = list(visual_options(source))
        self.assertEqual(len(options), 4, "Expected four unranked proposal specifications")
        for title, palette, claims in options:
            with self.subTest(option=title):
                self.assertGreater(len(palette), 0, "Option must define exact palette HEX values")
                self.assertGreater(len(claims), 0, "Option must document contrast pairings")
                for foreground, background, stated, note in claims:
                    with self.subTest(pair=f"{foreground}/{background}"):
                        self.assertIn(foreground.strip(), palette)
                        self.assertIn(background.strip(), palette)
                        calculated = round(
                            contrast_ratio(
                                palette[foreground.strip()],
                                palette[background.strip()],
                            ),
                            2,
                        )
                        self.assertEqual(
                            calculated,
                            float(stated),
                            f"{title}: claimed {stated}:1 but calculated {calculated}:1",
                        )

    def test_below_aa_pairings_are_explicitly_restricted_from_normal_text(self):
        source = SPEC.read_text(encoding="utf-8")
        below_aa = []
        for title, palette, claims in visual_options(source):
            for foreground, background, stated, note in claims:
                ratio = contrast_ratio(
                    palette[foreground.strip()],
                    palette[background.strip()],
                )
                if ratio < 4.5:
                    below_aa.append((title, foreground.strip(), background.strip(), note.lower()))
        self.assertTrue(below_aa, "Expected any below-AA pairing to be explicitly documented")
        for title, foreground, background, note in below_aa:
            with self.subTest(option=title, pair=f"{foreground}/{background}"):
                self.assertIn("not normal text", note)


if __name__ == "__main__":
    unittest.main()
