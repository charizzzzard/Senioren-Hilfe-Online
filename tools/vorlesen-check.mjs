// Prüft die Stimmenauswahl der Vorlese-Funktion (static/js/netzleicht.js, vorleser()).
// Nach tools/build.py bzw. tools/check.py ausführen: node tools/vorlesen-check.mjs [_site]
//
// Die Stimmen werden simuliert: Ein echter Browser im Container hat meist keine Stimmen, und welche Stimmen
// ein Leser hat, hängt von Browser und Gerät ab. Geprüft wird nur unsere Auswahl-Logik:
//   1. Eine deutsche Stimme auf dem Gerät (localService: true) geht vor einer Online-Stimme.
//   2. Gibt es nur deutsche Online-Stimmen, wird trotzdem vorgelesen – mit sichtbarem Hinweis vorher.
//   3. Kommt die Stimmenliste erst später („voiceschanged“), gilt dieselbe Auswahl.
//   4. Ohne deutsche Stimme entscheidet der Browser (Stimme leer, Sprache de-DE), kein Hinweis.
// Was das nicht prüft: ob ein Browser localService richtig meldet und wohin eine Online-Stimme den Text schickt.
import assert from "node:assert/strict";
import { stat } from "node:fs/promises";
import path from "node:path";
import { chromium } from "playwright";

const site = path.resolve(process.argv[2] || "_site");
const BASIS = "http://netzleicht.test";
const SEITE = "/artikel/schrift-groesser-stellen/";

const lokalDE = { name: "Lokal Deutsch", lang: "de-DE", localService: true, default: false };
const lokalAT = { name: "Lokal Österreich", lang: "de-AT", localService: true, default: false };
const onlineDE = { name: "Online Deutsch", lang: "de-DE", localService: false, default: true };
const lokalEN = { name: "Local English", lang: "en-US", localService: true, default: true };

const faelle = [
  { name: "Gerätestimme vor Online-Stimme", start: [onlineDE, lokalDE], stimme: "Lokal Deutsch", hinweis: false },
  { name: "de-DE vor de-AT, beide auf dem Gerät", start: [lokalAT, lokalDE, onlineDE], stimme: "Lokal Deutsch", hinweis: false },
  { name: "Gerätestimme de-AT vor Online-Stimme de-DE", start: [onlineDE, lokalAT], stimme: "Lokal Österreich", hinweis: false },
  { name: "nur Online-Stimme: vorlesen mit Hinweis", start: [onlineDE], stimme: "Online Deutsch", hinweis: true },
  { name: "Liste kommt später, Gerätestimme vorhanden", start: [], spaeter: [onlineDE, lokalDE], stimme: "Lokal Deutsch", hinweis: false },
  { name: "Liste kommt später, nur Online-Stimme", start: [], spaeter: [onlineDE], stimme: "Online Deutsch", hinweis: true },
  { name: "keine deutsche Stimme: Browser entscheidet", start: [lokalEN], stimme: null, hinweis: false },
];

function stimmenAttrappe(fall) {
  // Läuft vor dem Seitenskript im Browser: ersetzt speechSynthesis durch eine Attrappe.
  let stimmen = fall.start;
  const hoerer = [];
  window.__gesprochen = [];
  const synth = {
    speaking: false, pending: false, paused: false,
    getVoices: () => stimmen.slice(),
    speak: (u) => { window.__gesprochen.push({ stimme: u.voice ? u.voice.name : null, sprache: u.lang, text: u.text }); },
    cancel: () => {},
    addEventListener: (typ, fn) => { if (typ === "voiceschanged") hoerer.push(fn); },
    removeEventListener: () => {},
  };
  Object.defineProperty(window, "speechSynthesis", { value: synth, configurable: true });
  window.SpeechSynthesisUtterance = function (text) { this.text = text; this.voice = null; this.lang = ""; };
  if (fall.spaeter) {
    setTimeout(() => { stimmen = fall.spaeter; hoerer.forEach((fn) => fn(new Event("voiceschanged"))); }, 150);
  }
}

async function datei(url) {
  let p = path.join(site, decodeURIComponent(new URL(url).pathname));
  if (!p.startsWith(site)) return null;
  try { if ((await stat(p)).isDirectory()) p = path.join(p, "index.html"); await stat(p); return p; } catch { return null; }
}

const browser = await chromium.launch();
let fehler = 0;
try {
  for (const fall of faelle) {
    const kontext = await browser.newContext({ viewport: { width: 390, height: 844 } });
    const extern = [];
    const jsFehler = [];
    await kontext.route("**/*", async (route) => {
      const url = route.request().url();
      if (!url.startsWith(BASIS)) { extern.push(url); return route.abort(); }
      const p = await datei(url);
      return p ? route.fulfill({ path: p }) : route.fulfill({ status: 404, body: "" });
    });
    await kontext.addInitScript(stimmenAttrappe, fall);
    const page = await kontext.newPage();
    page.on("pageerror", (e) => jsFehler.push(String(e)));
    try {
      await page.goto(BASIS + SEITE);
      await page.waitForTimeout(fall.spaeter ? 400 : 50);
      const knopf = page.locator('.lesehilfe [data-aktion="vorlesen"]');
      const hinweis = page.locator("#vorlesen-hinweis");

      assert.equal(await knopf.isVisible(), true, "Vorlesen-Knopf sichtbar");
      assert.equal(await hinweis.isVisible(), fall.hinweis, "Hinweis vor dem Antippen " + (fall.hinweis ? "sichtbar" : "verborgen"));
      assert.equal(await knopf.getAttribute("aria-describedby"), fall.hinweis ? "vorlesen-hinweis" : null,
        "Knopf verweist nur bei Online-Stimme auf den Hinweis");
      if (fall.hinweis) {
        assert.match(await hinweis.innerText(), /Online-Stimme/);
        assert.equal(await hinweis.locator("a").getAttribute("href"),
          "/datenschutz/#lesehilfen-schriftgroesse-handy-auswahl-und-vorlesen");
      }

      await knopf.click();
      const gesprochen = await page.evaluate(() => window.__gesprochen);
      assert.ok(gesprochen.length >= 1, "Es wird vorgelesen");
      assert.equal(gesprochen[0].stimme, fall.stimme, "gewählte Stimme");
      assert.equal(gesprochen[0].sprache, "de-DE");
      assert.equal(await knopf.getAttribute("aria-pressed"), "true");
      assert.equal(await page.locator(".vorlesen-stopp").isVisible(), true, "Stopp-Knopf sichtbar");

      await page.emulateMedia({ media: "print" });
      assert.equal(await hinweis.isVisible(), false, "Hinweis nicht im Ausdruck");
      assert.deepEqual(jsFehler, [], "keine JavaScript-Fehler");
      assert.deepEqual(extern, [], "keine fremden Ressourcen");
      console.log("ok      " + fall.name);
    } catch (e) {
      fehler += 1;
      console.log("FEHLER  " + fall.name + ": " + e.message);
    } finally {
      await kontext.close();
    }
  }

  // Ohne Sprachausgabe im Browser bleibt der Knopf verborgen (bisheriges Verhalten).
  const kontext = await browser.newContext();
  await kontext.route("**/*", async (route) => {
    const p = route.request().url().startsWith(BASIS) && (await datei(route.request().url()));
    return p ? route.fulfill({ path: p }) : route.abort();
  });
  await kontext.addInitScript(() => { delete window.speechSynthesis; delete Window.prototype.speechSynthesis; });
  const page = await kontext.newPage();
  await page.goto(BASIS + SEITE);
  const ohne = await page.evaluate(() => ("speechSynthesis" in window));
  if (!ohne) {
    const sichtbar = await page.locator('.lesehilfe [data-aktion="vorlesen"]').isVisible();
    if (sichtbar) { fehler += 1; console.log("FEHLER  ohne Sprachausgabe: Knopf sichtbar"); }
    else { console.log("ok      ohne Sprachausgabe: Knopf verborgen"); }
  } else {
    console.log("übersprungen  ohne Sprachausgabe (speechSynthesis ließ sich nicht entfernen)");
  }
  await kontext.close();
} finally {
  await browser.close();
}

if (fehler) {
  console.log(`\n${fehler} Fall/Fälle fehlgeschlagen.`);
  process.exit(1);
}
console.log("\nVorlesen: Stimmenauswahl in allen Fällen wie erwartet.");
