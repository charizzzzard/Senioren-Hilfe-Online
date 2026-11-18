// Regressionen der Lesehilfen: nach tools/check.py mit node tools/ui-check.mjs ausführen.
import assert from "node:assert/strict";
import { createServer } from "node:http";
import { readFile, stat } from "node:fs/promises";
import path from "node:path";
import { chromium } from "playwright";

const site = path.resolve("_site");
const types = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript",
  ".woff2": "font/woff2", ".svg": "image/svg+xml", ".png": "image/png", ".webp": "image/webp", ".jpg": "image/jpeg" };
const server = createServer(async (req, res) => {
  try {
    let file = path.resolve(site, "." + new URL(req.url, "http://localhost").pathname);
    if (file !== site && !file.startsWith(site + path.sep)) throw new Error("Pfad außerhalb der Seite");
    if ((await stat(file)).isDirectory()) file = path.join(file, "index.html");
    res.writeHead(200, { "Content-Type": types[path.extname(file)] || "application/octet-stream" });
    res.end(await readFile(file));
  } catch { res.writeHead(404); res.end(); }
});
await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
const base = `http://127.0.0.1:${server.address().port}`;
let browser;
try {
  browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 }, reducedMotion: "reduce" });
  const external = [];
  page.on("request", (r) => { if (/^https?:/.test(r.url()) && new URL(r.url()).origin !== base) external.push(r.url()); });
  await page.goto(base + "/artikel/schrift-groesser-stellen/");
  await page.evaluate(() => document.fonts.ready);
  const item = page.locator(".artikel__rumpf ol:not(.klickpfad) > li").first();
  assert.equal(await item.getAttribute("role"), null, "Listeneintrag bleibt semantisch erhalten");
  const checkbox = item.getByRole("checkbox");
  await checkbox.focus();
  await page.keyboard.press("Space");
  assert.equal(await checkbox.isChecked(), true, "Leertaste hakt den Schritt ab");
  await page.keyboard.press("Space");
  assert.equal(await checkbox.isChecked(), false);

  // Ein Link innerhalb eines Schritts bleibt mit Enter bedienbar (kein Abfangen durch das li).
  await page.goto(base + "/artikel/betrugs-sms-erkennen/");
  const stepLink = page.locator('.artikel__rumpf li.abhakbar a[href^="#"]').first();
  assert.ok(await stepLink.count(), "Fixture enthält einen Link in einem Schritt");
  const target = await stepLink.getAttribute("href");
  await stepLink.focus();
  await page.keyboard.press("Enter");
  await page.waitForURL(base + "/artikel/betrugs-sms-erkennen/" + target);
  assert.equal(await stepLink.locator("xpath=ancestor::li[1]").getByRole("checkbox").isChecked(), false);
  await page.goto(base + "/artikel/schrift-groesser-stellen/");

  for (const width of [320, 390, 1280]) {
    await page.setViewportSize({ width, height: 900 });
    for (const scale of ["100%", "140%", "200%"]) {
      await page.evaluate((s) => { document.documentElement.style.fontSize = s; }, scale);
      const sizes = await page.evaluate(() => ({ content: document.documentElement.scrollWidth, viewport: innerWidth,
        overflow: [...document.querySelectorAll("main *")].filter((e) => e.getBoundingClientRect().right > innerWidth + 1).slice(0, 8).map((e) => e.className || e.tagName) }));
      assert.ok(sizes.content <= sizes.viewport + 1, `Kein Seitenüberlauf bei ${width}px / ${scale}: ${JSON.stringify(sizes)}`);
    }
  }
  await page.evaluate(() => { document.documentElement.style.fontSize = "100%"; });
  for (const selector of [".lesehilfe button:not([hidden])", ".abhaken-feld", ".navigation a", ".inhalt a", ".fuss nav a"]) {
    const sizes = await page.locator(selector).evaluateAll((els) => els.filter((e) => e.getClientRects().length).map((e) => ({ width: e.getBoundingClientRect().width, height: e.getBoundingClientRect().height })));
    assert.ok(sizes.length, selector + " gefunden");
    assert.ok(sizes.every((s) => s.width >= 48 && s.height >= 48), selector + " mindestens 48 × 48 CSS-Pixel");
  }
  await page.evaluate(() => { document.documentElement.style.fontSize = "140%"; });
  await page.emulateMedia({ media: "print" });
  assert.equal(await page.evaluate(() => getComputedStyle(document.documentElement).fontSize), "16px", "Gespeicherte Schriftstufe vergrößert den Ausdruck nicht");
  for (const selector of [".kopf", ".fuss", ".lesehilfe", ".abhaken-feld"]) {
    assert.equal(await page.locator(selector).first().isVisible(), false, selector + " im Druck verborgen");
  }
  assert.equal(await page.locator(".artikel__rumpf").isVisible(), true);
  await page.emulateMedia({ media: "screen" });

  await page.goto(base + "/ist-das-echt/");
  const first = page.locator("fieldset").first();
  await first.locator("input").first().focus();
  await page.keyboard.press("ArrowDown");
  await page.waitForTimeout(500); // frühere automatische Weiterschaltung: 350 ms
  assert.equal(await first.isVisible(), true, "Antwortauswahl löst keinen Seitenwechsel aus");
  await page.getByRole("button", { name: "Weiter" }).click();
  assert.equal(await first.isVisible(), false);
  assert.equal(await page.locator("fieldset").nth(1).isVisible(), true);
  assert.deepEqual(external, [], "Geprüfte Seiten laden nur eigene Ressourcen");
  console.log("UI: native Checkboxen, Links, Gerätebreiten, 200% Schrift, 48px Ziele, Druck und bewusste Navigation geprüft.");
} finally {
  if (browser) await browser.close();
  await new Promise((resolve) => server.close(resolve));
}
