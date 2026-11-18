"""Herkunftsprüfung: externe Ladevorgänge blockieren, normale Quellenlinks zulassen."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from check import Seitenparser, css_ressourcen, externe_ressource


class RessourcenTests(unittest.TestCase):
    def test_new_hosts_and_protocol_relative_urls_are_blocked(self):
        for url in ("https://unknown.test/widget.js", "//fonts.googleapis.com/css", "http://netzleicht.de/x", "data:text/javascript,alert(1)"):
            with self.subTest(url=url):
                self.assertTrue(externe_ressource(url, "https://netzleicht.de"))
        for url in ("/js/netzleicht.js?v=1", "https://netzleicht.de/css/style.css", "//netzleicht.de/img/x.webp"):
            self.assertFalse(externe_ressource(url, "https://netzleicht.de"))
        self.assertFalse(externe_ressource("data:image/svg+xml,...", "https://netzleicht.de", bild=True))

    def test_sources_are_links_but_scripts_fonts_frames_and_srcset_are_resources(self):
        p = Seitenparser()
        p.feed('''<a href="https://source.test/">Quelle</a>
          <script src="https://cdn.test/x.js"></script>
          <link rel="preload" as="font" href="https://font.test/font.woff2">
          <iframe src="https://video.test/"></iframe>
          <img src="/x.webp" srcset="/small.webp 640w, https://images.test/large.webp 1200w" alt="" width="640" height="400">''')
        self.assertNotIn(("a", "https://source.test/"), p.ressourcen)
        self.assertEqual([url for tag, url in p.ressourcen if externe_ressource(url, "https://netzleicht.de")],
                         ["https://cdn.test/x.js", "https://font.test/font.woff2", "https://video.test/", "https://images.test/large.webp"])
        self.assertEqual(p.bilder_ohne_groesse, [])

    def test_missing_or_invalid_dimensions_fail(self):
        p = Seitenparser()
        p.feed('<img src="/a.webp" alt=""><img src="/b.webp" width="100%" height="0" alt="">')
        self.assertEqual(p.bilder_ohne_groesse, ["/a.webp", "/b.webp"])

    def test_css_font_import_and_background_are_checked(self):
        css = '''/* url(https://ignored.test/) */
          @import "https://fonts.test/font.css";
          @import url('//other.test/x.css');
          @font-face { src: url("https://fonts.test/x.woff2"); }
          body { background: url(data:image/svg+xml,%3Csvg%3E); }'''
        urls = css_ressourcen(css)
        self.assertEqual({url for url in urls if externe_ressource(url, "https://netzleicht.de", bild=True)},
                         {"https://fonts.test/font.css", "//other.test/x.css", "https://fonts.test/x.woff2"})

    def test_inline_css_is_checked_too(self):
        p = Seitenparser()
        p.feed('''<style>@import "https://fonts.test/x.css";</style>
          <p style="background: url(//images.test/x.webp)">Text</p>''')
        self.assertEqual([url for _, url in p.ressourcen], ["https://fonts.test/x.css", "//images.test/x.webp"])


if __name__ == "__main__":
    unittest.main()
