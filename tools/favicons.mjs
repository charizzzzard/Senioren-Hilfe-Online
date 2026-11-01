// Erzeugt die Favicon-Dateien aus static/favicon.svg (einmalig bzw. nach Logo-Änderung ausführen):
//   node tools/favicons.mjs
// Ergebnis in static/: favicon.ico (16/32/48 px), favicon-192.png, apple-touch-icon.png (180 px, ohne Rundung).
// Hintergrund: Die Google-Suche zeigt keine SVG-Favicons an (unterstützt u. a. ICO und PNG, empfohlen ab 48 × 48 px):
// https://developers.google.com/search/docs/appearance/favicon-in-search?hl=de
import { readFile, writeFile } from "node:fs/promises";
import { createRequire } from "node:module";
import path from "node:path";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const STATIC = path.resolve("static");
const svg = await readFile(path.join(STATIC, "favicon.svg"), "utf8");

const browser = await chromium.launch();
const page = await browser.newPage();

async function png(quelle, groesse) {
  const groessenSvg = quelle.replace("<svg ", `<svg width="${groesse}" height="${groesse}" `);
  await page.setViewportSize({ width: groesse, height: groesse });
  await page.setContent(`<html><body style="margin:0;background:transparent">${groessenSvg}</body></html>`);
  return page.locator("svg").screenshot({ omitBackground: true });
}

// ICO-Datei mit eingebetteten PNG-Bildern (von allen aktuellen Browsern und Windows unterstützt)
function ico(bilder) {
  const kopf = Buffer.alloc(6 + 16 * bilder.length);
  kopf.writeUInt16LE(0, 0);
  kopf.writeUInt16LE(1, 2);
  kopf.writeUInt16LE(bilder.length, 4);
  let versatz = kopf.length;
  bilder.forEach(({ groesse, daten }, i) => {
    const o = 6 + 16 * i;
    kopf.writeUInt8(groesse >= 256 ? 0 : groesse, o);
    kopf.writeUInt8(groesse >= 256 ? 0 : groesse, o + 1);
    kopf.writeUInt8(0, o + 2);
    kopf.writeUInt8(0, o + 3);
    kopf.writeUInt16LE(1, o + 4);
    kopf.writeUInt16LE(32, o + 6);
    kopf.writeUInt32LE(daten.length, o + 8);
    kopf.writeUInt32LE(versatz, o + 12);
    versatz += daten.length;
  });
  return Buffer.concat([kopf, ...bilder.map((b) => b.daten)]);
}

const icoBilder = [];
for (const groesse of [16, 32, 48]) icoBilder.push({ groesse, daten: await png(svg, groesse) });
await writeFile(path.join(STATIC, "favicon.ico"), ico(icoBilder));
await writeFile(path.join(STATIC, "favicon-192.png"), await png(svg, 192));
// iOS rundet die Ecken selbst – daher hier ohne eigene Rundung und ohne Transparenz
await writeFile(path.join(STATIC, "apple-touch-icon.png"), await png(svg.replace(/rx="[^"]*"/, 'rx="0"'), 180));

await browser.close();
console.log("Favicons erzeugt: favicon.ico, favicon-192.png, apple-touch-icon.png");
