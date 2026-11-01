// Erzeugt aus allen Checklisten-Druckseiten (_site/artikel/<slug>/checkliste/) ein PDF unter _site/checklisten/<slug>.pdf.
// Aufruf nach dem Bauen:  node tools/pdf.mjs
// Läuft im Deploy (GitHub Actions) mit Playwright/Chromium. Bricht ab, wenn ein PDF fehlt.
import { createServer } from "node:http";
import { readFile, readdir, mkdir, stat } from "node:fs/promises";
import { createRequire } from "node:module";
import path from "node:path";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const SITE = path.resolve(process.argv[2] || "_site");
const TYPEN = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript",
  ".woff2": "font/woff2", ".svg": "image/svg+xml", ".png": "image/png", ".webp": "image/webp", ".jpg": "image/jpeg" };

const server = createServer(async (req, res) => {
  try {
    let datei = path.join(SITE, decodeURIComponent(new URL(req.url, "http://x").pathname));
    if ((await stat(datei)).isDirectory()) datei = path.join(datei, "index.html");
    res.writeHead(200, { "Content-Type": TYPEN[path.extname(datei)] || "application/octet-stream" });
    res.end(await readFile(datei));
  } catch {
    res.writeHead(404); res.end();
  }
});
await new Promise((ok) => server.listen(0, "127.0.0.1", ok));
const basis = `http://127.0.0.1:${server.address().port}`;

const slugs = [];
for (const slug of await readdir(path.join(SITE, "artikel"))) {
  try { await stat(path.join(SITE, "artikel", slug, "checkliste", "index.html")); slugs.push(slug); } catch { /* keine Checkliste */ }
}

await mkdir(path.join(SITE, "checklisten"), { recursive: true });
const browser = await chromium.launch();
const seite = await browser.newPage();
let fehler = 0;
for (const slug of slugs) {
  const ziel = path.join(SITE, "checklisten", `${slug}.pdf`);
  try {
    await seite.goto(`${basis}/artikel/${slug}/checkliste/`, { waitUntil: "networkidle" });
    await seite.evaluate(() => document.fonts.ready);
    await seite.pdf({ path: ziel, format: "A4", printBackground: true, preferCSSPageSize: true });
    const groesse = (await stat(ziel)).size;
    console.log(`PDF: ${slug}.pdf (${Math.round(groesse / 1024)} KB)`);
  } catch (e) {
    fehler++;
    console.error(`FEHLER bei ${slug}: ${e.message}`);
  }
}
await browser.close();
server.close();
if (fehler || !slugs.length) { console.error(`${fehler} Fehler, ${slugs.length} Checklisten`); process.exit(1); }
