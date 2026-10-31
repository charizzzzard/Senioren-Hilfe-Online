/* Netzleicht – Lesehilfen
   Alles läuft nur im Browser: keine Cookies, kein Tracking, keine fremden Dienste.
   Gespeichert werden nur selbst gewählte Einstellungen (Schriftgröße, Gerät) im lokalen Speicher. */
(function () {
  "use strict";

  var SCHRIFT_STUFEN = [1, 1.12, 1.25, 1.4];
  var speicher = {
    lesen: function (k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } },
    schreiben: function (k, v) { try { window.localStorage.setItem(k, v); } catch (e) { /* privat */ } }
  };

  /* ---------------------------------------------- Figuren: kurz animieren, wenn sie ins Bild kommen */
  function figurenBeleben() {
    var figuren = document.querySelectorAll(".szene .figur, .figuren .figur");
    if (!("IntersectionObserver" in window)) {
      figuren.forEach(function (f) { f.classList.add("figur--aktiv"); });
      return;
    }
    var beobachter = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("figur--aktiv");
          beobachter.unobserve(e.target);
        }
      });
    }, { threshold: 0.4 });
    figuren.forEach(function (f) { beobachter.observe(f); });
  }

  /* ---------------------------------------------- Schriftgröße */
  function schriftSetzen(stufe) {
    stufe = Math.max(0, Math.min(SCHRIFT_STUFEN.length - 1, stufe));
    document.documentElement.style.fontSize = (SCHRIFT_STUFEN[stufe] * 100) + "%";
    speicher.schreiben("nl-schrift", String(stufe));
    return stufe;
  }

  /* ---------------------------------------------- Gerätewahl (iPhone / Android) */
  function geraeteAbschnitte(rumpf) {
    var abschnitte = { iphone: [], android: [] };
    var kinder = Array.prototype.slice.call(rumpf.children);
    var aktuell = null;
    var ebene = 0;
    kinder.forEach(function (el) {
      var m = /^H([23])$/.exec(el.tagName);
      if (m) {
        var lvl = Number(m[1]);
        var text = el.textContent;
        var iphone = /iPhone/.test(text), android = /Android/.test(text);
        if (iphone !== android) {
          aktuell = iphone ? "iphone" : "android";
          ebene = lvl;
          abschnitte[aktuell].push(el);
          return;
        }
        if (aktuell && lvl <= ebene) { aktuell = null; }
      }
      if (aktuell) { abschnitte[aktuell].push(el); }
    });
    return abschnitte;
  }

  function geraetZeigen(abschnitte, geraet, leiste) {
    ["iphone", "android"].forEach(function (g) {
      abschnitte[g].forEach(function (el) {
        el.hidden = geraet !== "alle" && geraet !== g;
        if (el.id) {
          var eintrag = document.querySelector('.inhalt a[href="#' + el.id + '"]');
          if (eintrag) { eintrag.parentElement.hidden = el.hidden; }
        }
      });
    });
    leiste.querySelectorAll("[data-geraet]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-geraet") === geraet));
    });
    speicher.schreiben("nl-geraet", geraet);
  }

  /* ---------------------------------------------- Vorlesen */
  function vorleser(artikel, knopf) {
    if (!("speechSynthesis" in window)) { knopf.hidden = true; return; }
    var laeuft = false;
    var markiert = null;

    function stimme() {
      var stimmen = window.speechSynthesis.getVoices();
      return stimmen.filter(function (s) { return /^de(-|_|$)/i.test(s.lang); })[0] || null;
    }
    function bloecke() {
      var auswahl = artikel.querySelectorAll(
        "h1, .kurz p, .kurz li, .artikel__rumpf > p, .artikel__rumpf > h2, .artikel__rumpf > h3, " +
        ".artikel__rumpf > ul > li, .artikel__rumpf > ol > li, .artikel__rumpf .admonition p, " +
        ".artikel__rumpf .szene__text p, .artikel__rumpf .klickpfad, .checkliste h2, .checkliste li");
      return Array.prototype.filter.call(auswahl, function (el) {
        return el.offsetParent !== null && el.textContent.trim();
      });
    }
    function markieren(el) {
      if (markiert) { markiert.classList.remove("wird-vorgelesen"); }
      markiert = el;
      if (el) {
        el.classList.add("wird-vorgelesen");
        el.scrollIntoView({ block: "center", behavior: "smooth" });
      }
    }
    function anhalten() {
      laeuft = false;
      window.speechSynthesis.cancel();
      markieren(null);
      knopf.setAttribute("aria-pressed", "false");
      knopf.textContent = "▶ Vorlesen";
    }
    function sprechen(liste, i) {
      if (!laeuft || i >= liste.length) { anhalten(); return; }
      var el = liste[i];
      var text = el.classList.contains("klickpfad")
        ? "Der Weg: " + Array.prototype.map.call(el.querySelectorAll("li"), function (li) { return li.textContent; }).join(", dann ")
        : el.textContent;
      var u = new SpeechSynthesisUtterance(text.replace(/\s+/g, " ").trim());
      u.lang = "de-DE";
      u.rate = 0.92;
      var s = stimme();
      if (s) { u.voice = s; }
      u.onend = function () { sprechen(liste, i + 1); };
      u.onerror = function () { anhalten(); };
      markieren(el);
      window.speechSynthesis.speak(u);
    }
    knopf.addEventListener("click", function () {
      if (laeuft) { anhalten(); return; }
      laeuft = true;
      knopf.setAttribute("aria-pressed", "true");
      knopf.textContent = "■ Vorlesen anhalten";
      window.speechSynthesis.cancel();
      sprechen(bloecke(), 0);
    });
    window.addEventListener("pagehide", anhalten);
  }

  /* ---------------------------------------------- Schritte und Checkliste abhaken */
  function abhaken(liste, hinweisVor) {
    liste.forEach(function (li) {
      li.setAttribute("role", "checkbox");
      li.setAttribute("aria-checked", "false");
      li.tabIndex = 0;
      li.classList.add("abhakbar");
      function umschalten() {
        var an = li.getAttribute("aria-checked") !== "true";
        li.setAttribute("aria-checked", String(an));
        li.classList.toggle("erledigt", an);
      }
      li.addEventListener("click", function (e) {
        if (e.target.closest("a, button")) { return; }
        umschalten();
      });
      li.addEventListener("keydown", function (e) {
        if (e.key === " " || e.key === "Enter") { e.preventDefault(); umschalten(); }
      });
    });
    if (hinweisVor) {
      var p = document.createElement("p");
      p.className = "abhaken-hinweis nicht-drucken";
      p.textContent = "Tipp: Tippen Sie einen Schritt an, um ihn abzuhaken. So behalten Sie den Überblick.";
      hinweisVor.parentNode.insertBefore(p, hinweisVor);
    }
  }

  /* ---------------------------------------------- Start */
  function start() {
    var gespeichert = parseInt(speicher.lesen("nl-schrift") || "0", 10) || 0;
    var stufe = gespeichert;
    figurenBeleben();

    var leiste = document.querySelector(".lesehilfe");
    var artikel = document.querySelector("article.artikel");
    if (!leiste || !artikel) { return; }
    leiste.hidden = false;

    leiste.querySelector('[data-aktion="kleiner"]').addEventListener("click", function () { stufe = schriftSetzen(stufe - 1); });
    leiste.querySelector('[data-aktion="groesser"]').addEventListener("click", function () { stufe = schriftSetzen(stufe + 1); });
    vorleser(artikel, leiste.querySelector('[data-aktion="vorlesen"]'));

    var rumpf = artikel.querySelector(".artikel__rumpf");
    if (rumpf) {
      var abschnitte = geraeteAbschnitte(rumpf);
      var gruppe = leiste.querySelector(".lesehilfe__geraet");
      if (abschnitte.iphone.length && abschnitte.android.length && gruppe) {
        gruppe.hidden = false;
        gruppe.querySelectorAll("[data-geraet]").forEach(function (b) {
          b.addEventListener("click", function () { geraetZeigen(abschnitte, b.getAttribute("data-geraet"), leiste); });
        });
        geraetZeigen(abschnitte, speicher.lesen("nl-geraet") || "alle", leiste);
      }
      var schritte = rumpf.querySelectorAll("ol:not(.klickpfad):not(.inhalt ol) > li");
      if (schritte.length) { abhaken(Array.prototype.slice.call(schritte), rumpf.querySelector("ol:not(.klickpfad)")); }
    }
    var checkliste = artikel.querySelectorAll(".checkliste li");
    if (checkliste.length) { abhaken(Array.prototype.slice.call(checkliste), null); }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
