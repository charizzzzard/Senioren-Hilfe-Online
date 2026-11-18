// Leistungsmessung unter festen mobilen Testbedingungen – Startseite, eine Anleitung, Ist-das-echt-Check.
// Misst nur hier im Test-Browser; auf netzleicht.de kommt dafür kein Skript und kein Tracking dazu.
//
//   node tools/leistung.mjs                  gebauter Stand aus _site (lokal, gzip wie bei GitHub Pages)
//   node tools/leistung.mjs --live           veröffentlichter Stand https://netzleicht.de (im Container über den Proxy)
//   Optionen: --laeufe 5   --speichern (an leistung/messungen.csv anhängen)   --seiten /,/ist-das-echt/
//
// Vergleich: immer mit dem letzten gespeicherten Lauf derselben Quelle (lokal/live) und desselben Profils.
// Regeln für „Verschlechterung“ und „bestätigt“: leistung/README.md.
import { createRequire } from "node:module";
import { createServer } from "node:http";
import { gzipSync } from "node:zlib";
import { execFileSync } from "node:child_process";
import { readFile, stat, appendFile, mkdir } from "node:fs/promises";
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

// ---------------------------------------------------------------- feste Testbedingungen (Profil)
// Ändert sich hier etwas, bekommt das Profil einen neuen Namen – sonst wären Vergleiche mit alten Läufen wertlos.
const PROFIL = "mobil-v1";
const GERAET = { breite: 412, hoehe: 823, dpr: 1.75 };          // Größe eines typischen Android-Handys
const NETZ = { latenzMs: 150, downKbit: 1600, upKbit: 750 };    // langsames Mobilnetz („4G, schwacher Empfang“)
const CPU_BREMSE = 4;                                           // Rechenleistung eines einfachen Handys
const UA = "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36";
const SEITEN = ["/", "/artikel/schrift-groesser-stellen/", "/ist-das-echt/"];
const LIVE = "https://netzleicht.de";

const SPALTEN = ["datum", "commit", "quelle", "profil", "seite", "laeufe", "ttfb_ms", "fcp_ms", "lcp_ms", "dcl_ms",
  "load_ms", "cls_laden", "cls_gesamt", "anfragen", "kb_gesamt", "kb_html", "kb_css", "kb_js", "kb_schrift", "kb_bild",
  "kb_sonst", "extern"];
const CSV = path.resolve("leistung/messungen.csv");

// ---------------------------------------------------------------- Aufruf
const argv = process.argv.slice(2);
const opt = (name, std) => { const i = argv.indexOf(name); return i >= 0 ? argv[i + 1] : std; };
const live = argv.includes("--live");
const speichern = argv.includes("--speichern");
const details = argv.includes("--details");
const laeufe = Number(opt("--laeufe", "5"));
const seiten = opt("--seiten", SEITEN.join(",")).split(",");

// ---------------------------------------------------------------- lokaler Server für _site (gzip wie bei GitHub Pages)
const TYPEN = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript", ".svg": "image/svg+xml",
  ".json": "application/json", ".xml": "application/xml", ".woff2": "font/woff2", ".webp": "image/webp",
  ".png": "image/png", ".jpg": "image/jpeg", ".ico": "image/x-icon", ".pdf": "application/pdf" };
const KOMPRIMIEREN = new Set([".html", ".css", ".js", ".svg", ".json", ".xml"]);

async function lokalerServer() {
  const wurzel = path.resolve("_site");
  if (!existsSync(wurzel)) throw new Error("_site fehlt – zuerst python tools/build.py ausführen");
  const server = createServer(async (req, res) => {
    try {
      let datei = path.resolve(wurzel, "." + decodeURIComponent(new URL(req.url, "http://x").pathname));
      if (datei !== wurzel && !datei.startsWith(wurzel + path.sep)) throw new Error("außerhalb");
      if ((await stat(datei)).isDirectory()) datei = path.join(datei, "index.html");
      const endung = path.extname(datei);
      let inhalt = await readFile(datei);
      const kopf = { "Content-Type": TYPEN[endung] || "application/octet-stream", "Cache-Control": "no-store" };
      if (KOMPRIMIEREN.has(endung) && /gzip/.test(req.headers["accept-encoding"] || "")) {
        inhalt = gzipSync(inhalt, { level: 6 });
        kopf["Content-Encoding"] = "gzip";
      }
      res.writeHead(200, kopf);
      res.end(inhalt);
    } catch { res.writeHead(404); res.end(); }
  });
  await new Promise((r) => server.listen(0, "127.0.0.1", r));
  return { server, basis: `http://127.0.0.1:${server.address().port}` };
}

// ---------------------------------------------------------------- Kennzahlen
function cls(verschiebungen) {
  // Größtes „Sitzungsfenster“ nach Googles Definition: Lücke > 1 s oder Fenster > 5 s beginnt ein neues Fenster.
  let best = 0, summe = 0, start = -Infinity, zuletzt = -Infinity;
  for (const [zeit, wert] of [...verschiebungen].sort((a, b) => a[0] - b[0])) {
    if (zeit - zuletzt > 1000 || zeit - start > 5000) { summe = 0; start = zeit; }
    summe += wert; zuletzt = zeit; best = Math.max(best, summe);
  }
  return best;
}
const median = (werte) => {
  const w = werte.filter((x) => x !== null && Number.isFinite(x)).sort((a, b) => a - b);
  if (!w.length) return null;
  const m = Math.floor(w.length / 2);
  return w.length % 2 ? w[m] : (w[m - 1] + w[m]) / 2;
};
const ART = { Document: "html", Stylesheet: "css", Script: "js", Font: "schrift", Image: "bild" };

async function einLauf(browser, url, herkunft) {
  const kontext = await browser.newContext({
    viewport: { width: GERAET.breite, height: GERAET.hoehe }, deviceScaleFactor: GERAET.dpr,
    isMobile: true, hasTouch: true, userAgent: UA, locale: "de-DE",
  });
  await kontext.addInitScript(() => {
    window.__messung = { lcp: null, verschiebungen: [] };
    new PerformanceObserver((l) => { for (const e of l.getEntries()) window.__messung.lcp = e.startTime; })
      .observe({ type: "largest-contentful-paint", buffered: true });
    new PerformanceObserver((l) => {
      for (const e of l.getEntries()) if (!e.hadRecentInput) window.__messung.verschiebungen.push([e.startTime, e.value]);
    }).observe({ type: "layout-shift", buffered: true });
  });
  const seite = await kontext.newPage();
  const cdp = await kontext.newCDPSession(seite);
  await cdp.send("Network.enable");
  await cdp.send("Network.setCacheDisabled", { cacheDisabled: true });
  await cdp.send("Network.emulateNetworkConditions", {
    offline: false, latency: NETZ.latenzMs,
    downloadThroughput: (NETZ.downKbit * 1000) / 8, uploadThroughput: (NETZ.upKbit * 1000) / 8,
  });
  await cdp.send("Emulation.setCPUThrottlingRate", { rate: CPU_BREMSE });
  const anfragen = new Map();
  cdp.on("Network.responseReceived", (e) => {
    // data:-Adressen (z. B. das eingebettete Papierkorn im CSS) sind keine Netzanfragen.
    if (!e.response.url.startsWith("data:")) anfragen.set(e.requestId, { art: e.type, url: e.response.url, bytes: 0 });
  });
  cdp.on("Network.loadingFinished", (e) => { const a = anfragen.get(e.requestId); if (a) a.bytes = e.encodedDataLength; });

  await seite.goto(url, { waitUntil: "load", timeout: 180000 });
  await seite.waitForTimeout(1500);
  const laden = await seite.evaluate(() => {
    const n = performance.getEntriesByType("navigation")[0];
    const fcp = performance.getEntriesByName("first-contentful-paint")[0];
    return { ttfb: n.responseStart, dcl: n.domContentLoadedEventEnd, load: n.loadEventEnd,
      fcp: fcp ? fcp.startTime : null, lcp: window.__messung.lcp, verschiebungen: window.__messung.verschiebungen.slice() };
  });
  // Danach langsam bis zum Ende scrollen: Verschiebungen durch spät geladene Bilder o. Ä. zählen in cls_gesamt.
  await seite.evaluate(async () => {
    for (let y = 0; y < document.documentElement.scrollHeight; y += Math.round(innerHeight * 0.8)) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 150));
    }
  });
  await seite.waitForTimeout(1500);
  const alle = await seite.evaluate(() => window.__messung.verschiebungen);
  await kontext.close();

  const kb = { html: 0, css: 0, js: 0, schrift: 0, bild: 0, sonst: 0 };
  const extern = new Set();
  for (const a of anfragen.values()) {
    kb[ART[a.art] || "sonst"] += a.bytes / 1024;
    try { const o = new URL(a.url).origin; if (o !== herkunft) extern.add(o); } catch { extern.add(a.url.slice(0, 40)); }
  }
  return {
    ttfb_ms: laden.ttfb, fcp_ms: laden.fcp, lcp_ms: laden.lcp, dcl_ms: laden.dcl, load_ms: laden.load,
    cls_laden: cls(laden.verschiebungen), cls_gesamt: cls(alle), anfragen: anfragen.size,
    kb_gesamt: Object.values(kb).reduce((s, x) => s + x, 0), ...Object.fromEntries(Object.entries(kb).map(([k, v]) => ["kb_" + k, v])),
    extern: [...extern].join(" "),
    einzeln: [...anfragen.values()].map((a) => [a.url.replace(herkunft, ""), ART[a.art] || "sonst", a.bytes / 1024]),
  };
}

// ---------------------------------------------------------------- Vergleich mit dem letzten Lauf
function csvLesen() {
  if (!existsSync(CSV)) return [];
  const [kopf, ...zeilen] = readFileSync(CSV, "utf-8").trim().split("\n");
  const namen = kopf.split(",");
  return zeilen.map((z) => Object.fromEntries(z.split(",").map((w, i) => [namen[i], w])));
}
// Grenzen (siehe leistung/README.md): Größen sind lokal reproduzierbar, Zeiten schwanken – darum großzügiger.
const GRENZEN = {
  kb_gesamt: { rel: 0.05, abs: 2 }, kb_html: { rel: 0.05, abs: 2 }, kb_css: { rel: 0.05, abs: 2 }, kb_js: { rel: 0.05, abs: 2 },
  kb_schrift: { rel: 0.05, abs: 2 }, kb_bild: { rel: 0.05, abs: 2 }, anfragen: { rel: 0, abs: 1 },
  fcp_ms: { rel: 0.2, abs: 200 }, lcp_ms: { rel: 0.2, abs: 200 }, load_ms: { rel: 0.2, abs: 300 },
  cls_laden: { rel: 0, abs: 0.02 }, cls_gesamt: { rel: 0, abs: 0.02 },
};
function vergleichen(alt, neu) {
  const befunde = [];
  for (const [k, g] of Object.entries(GRENZEN)) {
    const a = Number(alt[k]), n = Number(neu[k]);
    if (!Number.isFinite(a) || !Number.isFinite(n)) continue;
    const diff = n - a;
    if (diff > g.abs && diff > a * g.rel) befunde.push(`${k}: ${a} → ${n} (+${+(diff).toFixed(3)})`);
  }
  return befunde;
}

// ---------------------------------------------------------------- Ablauf
const proxy = process.env.HTTPS_PROXY || process.env.https_proxy;
let lokal = null;
const basis = live ? LIVE : (lokal = await lokalerServer()).basis;
const browser = await chromium.launch(live && proxy ? { proxy: { server: proxy } } : {});
const commit = (() => { try { return execFileSync("git", ["rev-parse", "--short=12", "HEAD"]).toString().trim(); } catch { return "-"; } })();
const datum = new Date().toLocaleString("sv-SE", { timeZone: "Europe/Berlin" }).replace(" ", "T").slice(0, 16);
const quelle = live ? "live" : "lokal";
const alt = csvLesen().filter((z) => z.quelle === quelle && z.profil === PROFIL);
const ergebnisse = [];
let verdacht = 0;

console.log(`Profil ${PROFIL}: ${GERAET.breite}×${GERAET.hoehe} px, DPR ${GERAET.dpr}, ${NETZ.latenzMs} ms Latenz, ` +
  `${NETZ.downKbit}/${NETZ.upKbit} kbit/s, CPU ÷${CPU_BREMSE}, kalter Cache, ${laeufe} Läufe je Seite (Median). Quelle: ${quelle} (${basis})\n`);
try {
  for (const pfad of seiten) {
    const einzel = [];
    for (let i = 0; i < laeufe; i++) einzel.push(await einLauf(browser, basis + pfad, new URL(basis).origin));
    const zeile = { datum, commit, quelle, profil: PROFIL, seite: pfad, laeufe };
    for (const k of SPALTEN.slice(6)) {
      if (k === "extern") { zeile[k] = [...new Set(einzel.flatMap((e) => e.extern.split(" ").filter(Boolean)))].join(" ") || "-"; continue; }
      const m = median(einzel.map((e) => e[k]));
      zeile[k] = m === null ? "" : k.startsWith("cls") ? m.toFixed(4) : k.startsWith("kb") ? m.toFixed(1) : Math.round(m);
    }
    ergebnisse.push(zeile);
    console.log(`${pfad}\n  TTFB ${zeile.ttfb_ms} ms · FCP ${zeile.fcp_ms} ms · LCP ${zeile.lcp_ms} ms · DOM fertig ${zeile.dcl_ms} ms · ` +
      `geladen ${zeile.load_ms} ms\n  CLS beim Laden ${zeile.cls_laden} · nach Scrollen ${zeile.cls_gesamt}\n` +
      `  ${zeile.anfragen} Anfragen, ${zeile.kb_gesamt} KB übertragen (HTML ${zeile.kb_html}, CSS ${zeile.kb_css}, ` +
      `JS ${zeile.kb_js}, Schrift ${zeile.kb_schrift}, Bild ${zeile.kb_bild}, sonst ${zeile.kb_sonst}) · fremde Herkunft: ${zeile.extern}`);
    if (details) {
      for (const [url, art, kb] of einzel[0].einzeln) console.log(`    ${art.padEnd(7)} ${kb.toFixed(1).padStart(6)} KB  ${url}`);
    }
    const vorher = alt.filter((z) => z.seite === pfad).at(-1);
    if (!vorher) {
      console.log("  Vergleich: kein früherer Lauf mit diesem Profil – dieser Lauf ist die Basis.\n");
    } else {
      const befunde = vergleichen(vorher, zeile);
      verdacht += befunde.length;
      console.log(`  Vergleich mit ${vorher.datum} (${vorher.commit}): ` +
        (befunde.length ? "VERDACHT auf Verschlechterung – " + befunde.join("; ") : "keine Verschlechterung über den Grenzen") + "\n");
    }
  }
} finally {
  await browser.close();
  if (lokal) lokal.server.close();
}

if (speichern) {
  await mkdir(path.dirname(CSV), { recursive: true });
  if (!existsSync(CSV)) await appendFile(CSV, SPALTEN.join(",") + "\n");
  await appendFile(CSV, ergebnisse.map((z) => SPALTEN.map((k) => String(z[k] ?? "")).join(",")).join("\n") + "\n");
  console.log(`Gespeichert in ${path.relative(process.cwd(), CSV)}.`);
}
if (verdacht) {
  console.log(`${verdacht} Verdacht/Verdachtsfälle. Bestätigt ist eine Verschlechterung erst, wenn eine zweite Messung ` +
    "sie wiederholt (Größen: lokal sofort reproduzierbar). Siehe leistung/README.md.");
}
