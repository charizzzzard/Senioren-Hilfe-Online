// Holt den sichtbaren Text von Quellseiten (auch JavaScript-Seiten wie Apple-Handbuch, WhatsApp-Hilfe).
// Wird von tools/belegcheck.py aufgerufen; kann auch einzeln benutzt werden:
//   node tools/seitentext.mjs https://… https://…   → JSON auf stdout
// Pro Seite drei Varianten, damit Zitate auch über Symbole und eingeklappte Abschnitte hinweg gefunden werden:
//   sichtbar (innerText), alles (textContent), mit_bildtexten (innerText mit Alt-Texten der Symbole).
// Im Cloud-Container läuft der Verkehr über den Proxy aus HTTPS_PROXY.
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const urls = process.argv.slice(2);
const proxy = process.env.HTTPS_PROXY || process.env.https_proxy;
const browser = await chromium.launch(proxy ? { proxy: { server: proxy } } : {});
const seite = await browser.newPage({ locale: "de-DE" });
const ergebnis = {};

for (const url of urls) {
  try {
    const antwort = await seite.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
    await seite.waitForTimeout(6000);
    const texte = await seite.evaluate(() => {
      const wurzel = document.querySelector("main") || document.body;
      const kopie = wurzel.cloneNode(true);
      kopie.querySelectorAll("script, style, noscript").forEach((e) => e.remove());
      const mitBildern = wurzel.cloneNode(true);
      mitBildern.querySelectorAll("img").forEach((i) => i.replaceWith(document.createTextNode(` ${i.alt || ""} `)));
      document.body.appendChild(mitBildern);
      mitBildern.style.cssText = "position:absolute;left:-99999px;top:0;width:1000px";
      const mitBildtexten = mitBildern.innerText;
      mitBildern.remove();
      return { sichtbar: wurzel.innerText, alles: kopie.textContent, mit_bildtexten: mitBildtexten };
    });
    ergebnis[url] = { ok: true, status: antwort ? antwort.status() : null, endadresse: seite.url(), ...texte };
  } catch (e) {
    ergebnis[url] = { ok: false, fehler: String(e.message || e).split("\n")[0] };
  }
}

await browser.close();
process.stdout.write(JSON.stringify(ergebnis));
