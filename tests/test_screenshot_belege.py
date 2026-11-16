"""Bildzuordnung und Rückwärtskompatibilität, ohne Gerät oder Netzwerk.

Die 1x1-Testgrafik ist eine technische Fixture, kein echter Gerätescreenshot.
"""
import base64
import hashlib
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import build

PNG = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+j6y4AAAAASUVORK5CYII=")


class ScreenshotBelegeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.lauf_id = "2026-11-16-fixture"
        self.image = self.root / "static/img/geraetetest" / self.lauf_id / "vorher.png"
        self.image.parent.mkdir(parents=True)
        self.image.write_bytes(PNG)
        (self.root / "geraetelaeufe").mkdir()
        self.log = {
            "schema_version": 1, "id": self.lauf_id, "datum": "2026-11-16",
            "geraet": {"plattform": "android", "modell": "Fixture-Modell", "system": "Android 15",
                       "sprache": "Deutsch", "variante": "Testfixture"},
            "bilder": [{"id": "vorher", "datei": self.image.relative_to(self.root).as_posix(),
                        "sha256": hashlib.sha256(PNG).hexdigest(), "breite": 1, "hoehe": 1,
                        "freigabe": "bereinigt"}],
        }
        self.data = {"geraet": "android", "screenshot": {"lauf": self.lauf_id, "bild": "vorher"},
                     "alt": 'Regler vor der Änderung "Test"', "unterschrift": "Eine Fixture."}
        self.addCleanup(patch.stopall)
        patch.object(build, "ROOT", self.root).start()
        patch.object(build, "STATIC", self.root / "static").start()
        self.save_log()

    def save_log(self):
        (self.root / "geraetelaeufe" / (self.lauf_id + ".yaml")).write_text(
            yaml.safe_dump(self.log, allow_unicode=True), encoding="utf-8")

    def component(self, data=None):
        return build.komponenten("```bildschirm\n" + yaml.safe_dump(data or self.data, allow_unicode=True) + "```", "fixture.md")

    def test_renders_real_image_with_source_and_accessibility(self):
        html = self.component()
        self.assertIn(f'src="/img/geraetetest/{self.lauf_id}/vorher.png"', html)
        self.assertIn('width="1" height="1" loading="lazy"', html)
        self.assertIn("Echter Screenshot", html)
        self.assertIn("Fixture-Modell", html)
        self.assertIn("Originalgröße", html)
        class Images(HTMLParser):
            def handle_starttag(self, tag, attrs):
                if tag == "img":
                    self.alt = dict(attrs).get("alt")
        parser = Images()
        parser.feed(html)
        self.assertEqual(parser.alt, self.data["alt"])
        self.assertNotIn("Vereinfachte Darstellung", html)

    def test_changed_image_cannot_reuse_old_checksum(self):
        self.image.write_bytes(PNG + b"changed")
        with self.assertRaisesRegex(build.BuildError, "Prüfsumme"):
            self.component()

    def test_missing_export_or_unreviewed_image_rejected(self):
        self.log["bilder"] = []
        self.save_log()
        with self.assertRaises(build.BuildError):
            self.component()
        self.log["bilder"] = [{"id": "vorher", "freigabe": "offen"}]
        self.save_log()
        with self.assertRaises(build.BuildError):
            self.component()

    def test_dimensions_and_platform_must_match(self):
        self.log["bilder"][0]["breite"] = 2
        self.save_log()
        with self.assertRaisesRegex(build.BuildError, "Bildmaße"):
            self.component()
        self.log["bilder"][0]["breite"] = 1
        self.log["geraet"]["plattform"] = "ios"
        self.save_log()
        with self.assertRaisesRegex(build.BuildError, "Geräteplattform"):
            self.component()

    def test_external_or_traversing_path_rejected(self):
        for path in ("https://example.test/expired.png", "static/img/geraetetest/../other.png"):
            self.log["bilder"][0]["datei"] = path
            self.save_log()
            with self.assertRaises(build.BuildError):
                self.component()

    def test_missing_alt_or_duplicate_image_rejected(self):
        self.data.pop("alt")
        with self.assertRaisesRegex(build.BuildError, "alt-Text"):
            self.component()
        self.data["alt"] = "Fixture"
        self.log["bilder"].append(dict(self.log["bilder"][0]))
        self.save_log()
        with self.assertRaises(build.BuildError):
            self.component()

    def test_internal_photo_cannot_bypass_archive(self):
        data = {"geraet": "android", "unterschrift": "Fixture", "foto": {"src": "https://example.test/fake.png"}}
        with self.assertRaisesRegex(build.BuildError, "intern"):
            self.component(data)

    def test_existing_simplified_component_still_renders(self):
        html = self.component({"geraet": "android", "titel": "Fixture", "unterschrift": "Alte Syntax", "zeilen": ["[regler]"]})
        self.assertIn("Vereinfachte Darstellung", html)
        self.assertIn("bs__spur", html)
        self.assertNotIn("Echter Screenshot", html)


if __name__ == "__main__":
    unittest.main()
