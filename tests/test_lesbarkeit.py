"""Auswahlliste für Verständlichkeits-Überarbeitungen (tools/lesbarkeit.py), ohne Netzwerk."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import lesbarkeit  # noqa: E402


class LesbarkeitTests(unittest.TestCase):
    def test_lange_saetze_nutzt_die_satztrennung_aus_check(self):
        kurz = "Öffnen Sie WhatsApp."
        lang = ("Tippen Sie auf das Symbol für einen neuen Anruf, suchen Sie die Person und tippen Sie danach "
                "ganz in Ruhe auf die Videokamera im Chat.")
        html = f"<p>{kurz} {lang}</p><li>{kurz}</li>"
        self.assertEqual(lesbarkeit.lange_saetze(html), [lang])
        self.assertEqual(lesbarkeit.lange_saetze(html, grenze=30), [])

    def test_rangliste_umfasst_alle_texte_und_stellt_wochenschauen_ans_ende(self):
        daten = lesbarkeit.auswerten()
        root = Path(__file__).resolve().parents[1] / "content"
        erwartet = {f"artikel/{p.stem}" for p in (root / "artikel").glob("*.md")} | \
                   {f"lexikon/{p.stem}" for p in (root / "lexikon").glob("*.md")}
        self.assertTrue({e["text"] for e in daten} <= erwartet)
        wochenschau = [e["wochenschau"] for e in daten]
        self.assertEqual(wochenschau, sorted(wochenschau), "Wochenschauen stehen am Ende")
        andere = [e["ueber_richtwert"] for e in daten if not e["wochenschau"]]
        self.assertEqual(andere, sorted(andere, reverse=True), "absteigend nach langen Sätzen")


if __name__ == "__main__":
    unittest.main()
