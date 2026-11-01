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
  function schriftSetzen(stufe, leiste) {
    stufe = Math.max(0, Math.min(SCHRIFT_STUFEN.length - 1, stufe));
    document.documentElement.style.fontSize = (SCHRIFT_STUFEN[stufe] * 100) + "%";
    speicher.schreiben("nl-schrift", String(stufe));
    if (leiste) {
      /* An der kleinsten bzw. größten Stufe den jeweiligen Knopf sichtbar abschalten */
      var kleiner = leiste.querySelector('[data-aktion="kleiner"]');
      var groesser = leiste.querySelector('[data-aktion="groesser"]');
      kleiner.disabled = stufe === 0;
      groesser.disabled = stufe === SCHRIFT_STUFEN.length - 1;
      kleiner.title = kleiner.disabled ? "Das ist die kleinste Stufe" : "";
      groesser.title = groesser.disabled ? "Das ist die größte Stufe" : "";
    }
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

  function geraetZeigen(abschnitte, geraet, leiste, artikel) {
    /* Zeilen in „Kurz gesagt“ und Checkliste, die mit „iPhone“/„Android“/„Samsung“ beginnen (data-fuer) */
    artikel.querySelectorAll("[data-fuer]").forEach(function (el) {
      el.hidden = geraet !== "alle" && el.getAttribute("data-fuer") !== geraet;
    });
    var druck = artikel.querySelector("[data-druck-link]");
    if (druck) {
      druck.href = druck.href.replace(/&geraet=\w+/, "") + (geraet === "alle" ? "" : "&geraet=" + geraet);
    }
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
    var ruhig = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    /* Schwebender Stopp-Knopf: Die Leiste oben ist beim Vorlesen oft nicht mehr im Bild */
    var stopp = document.createElement("button");
    stopp.type = "button";
    stopp.className = "vorlesen-stopp";
    stopp.textContent = "■ Vorlesen anhalten";
    stopp.hidden = true;
    document.body.appendChild(stopp);

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
        /* Nur scrollen, wenn der Absatz nicht schon gut sichtbar ist */
        var r = el.getBoundingClientRect();
        if (r.top < 80 || r.bottom > window.innerHeight - 100) {
          el.scrollIntoView({ block: "center", behavior: ruhig ? "auto" : "smooth" });
        }
      }
    }
    function anhalten() {
      laeuft = false;
      window.speechSynthesis.cancel();
      markieren(null);
      knopf.setAttribute("aria-pressed", "false");
      knopf.textContent = "▶ Vorlesen";
      stopp.hidden = true;
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
      stopp.hidden = false;
      window.speechSynthesis.cancel();
      sprechen(bloecke(), 0);
    });
    stopp.addEventListener("click", function () { anhalten(); knopf.focus({ preventScroll: true }); });
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

  /* ---------------------------------------------- Erklärkästchen für Lexikon-Begriffe */
  function erklaerungen() {
    var links = document.querySelectorAll("a.begriff[data-erklaerung]");
    if (!links.length) { return; }
    var box = document.createElement("div");
    box.className = "erklaerung";
    box.hidden = true;
    box.setAttribute("role", "dialog");
    box.setAttribute("aria-labelledby", "erklaerung-titel");
    box.innerHTML = '<button type="button" class="erklaerung__zu" aria-label="Erklärung schließen">×</button>' +
      '<p class="erklaerung__titel" id="erklaerung-titel"></p><p class="erklaerung__text"></p>' +
      '<p class="erklaerung__mehr"><a></a></p>';
    document.body.appendChild(box);
    var aktiv = null;

    function zu(fokusZurueck) {
      box.hidden = true;
      if (aktiv) {
        aktiv.setAttribute("aria-expanded", "false");
        if (fokusZurueck) { aktiv.focus(); }
        aktiv = null;
      }
    }
    function auf(link) {
      if (aktiv) { zu(false); }
      aktiv = link;
      box.querySelector(".erklaerung__titel").textContent = link.getAttribute("data-begriff") + " – kurz erklärt";
      box.querySelector(".erklaerung__text").textContent = link.getAttribute("data-erklaerung");
      var mehr = box.querySelector(".erklaerung__mehr a");
      mehr.href = link.href;
      mehr.textContent = "Mehr dazu im Digital-Lexikon ›";
      box.hidden = false;
      if (window.matchMedia("(min-width: 40rem)").matches) {
        var r = link.getBoundingClientRect();
        var breite = box.offsetWidth;
        var xPos = Math.min(Math.max(12, r.left + window.scrollX), window.scrollX + document.documentElement.clientWidth - breite - 12);
        box.style.left = xPos + "px";
        box.style.top = (r.bottom + window.scrollY + 8) + "px";
      } else {
        box.style.left = "";
        box.style.top = "";
      }
      link.setAttribute("aria-expanded", "true");
      box.querySelector(".erklaerung__zu").focus();
    }
    links.forEach(function (link) {
      link.setAttribute("aria-haspopup", "dialog");
      link.setAttribute("aria-expanded", "false");
      link.addEventListener("click", function (e) {
        e.preventDefault();
        if (aktiv === link) { zu(true); } else { auf(link); }
      });
    });
    box.querySelector(".erklaerung__zu").addEventListener("click", function () { zu(true); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && aktiv) { zu(true); } });
    document.addEventListener("click", function (e) {
      if (aktiv && !box.contains(e.target) && !aktiv.contains(e.target)) { zu(false); }
    });
  }

  /* ---------------------------------------------- „Ist das echt?“-Check */
  function echtCheck() {
    var form = document.getElementById("echt-check");
    var datenEl = document.getElementById("echt-check-daten");
    if (!form || !datenEl) { return; }
    var daten = JSON.parse(datenEl.textContent);
    var schritte = Array.prototype.slice.call(form.querySelectorAll(".echt-check__schritt"));
    var steuerung = form.querySelector(".echt-check__steuerung");
    var zurueck = form.querySelector('[data-echt="zurueck"]');
    var weiter = form.querySelector('[data-echt="weiter"]');
    var ergebnis = document.getElementById("echt-ergebnis");
    var ohneJs = document.getElementById("echt-ohne-js");
    var index = 0;

    if (ohneJs) { ohneJs.hidden = true; }
    steuerung.hidden = false;

    function wert(name) {
      var gewaehlt = form.querySelector('input[name="' + name + '"]:checked');
      return gewaehlt ? gewaehlt.value : null;
    }
    function zeigen(i) {
      index = i;
      schritte.forEach(function (s, n) {
        s.hidden = n !== i;
        s.querySelector(".echt-check__zaehler").textContent = "Frage " + (n + 1) + " von " + schritte.length + ": ";
      });
      zurueck.hidden = i === 0;
      weiter.textContent = i === schritte.length - 1 ? "Ergebnis anzeigen ›" : "Weiter ›";
      var erstes = schritte[i].querySelector("input:checked") || schritte[i].querySelector("input");
      if (erstes) { erstes.focus({ preventScroll: true }); }
    }
    function liste(ul, eintraege, alsLink) {
      ul.innerHTML = "";
      (eintraege || []).forEach(function (e) {
        var li = document.createElement("li");
        if (alsLink) {
          var a = document.createElement("a");
          a.href = e.url;
          a.textContent = e.titel;
          li.appendChild(a);
        } else {
          li.textContent = e;
        }
        ul.appendChild(li);
      });
    }
    function auswerten() {
      var weg = wert("weg");
      var ja = function (id) { return wert(id) === "ja"; };
      var rot = ja("code") ||
        (ja("geld") && (ja("druck") || ja("angehoerig") || ja("amt"))) ||
        (ja("link") && (ja("druck") || ja("ueberraschend") || ja("geld")));
      var auffaellig = daten.fragen.some(function (id) { var w = wert(id); return w === "ja" || w === "unsicher"; });
      var stufe = rot ? "rot" : (auffaellig ? "gelb" : "gruen");
      var text = daten.ergebnisse[stufe];
      ergebnis.className = "echt-ergebnis echt-ergebnis--" + stufe;
      ergebnis.querySelector(".echt-ergebnis__titel").textContent = text.titel;
      ergebnis.querySelector(".echt-ergebnis__text").textContent = text.text;
      liste(ergebnis.querySelector(".echt-ergebnis__rat"), daten.ratschlaege[weg], false);
      liste(ergebnis.querySelector(".echt-ergebnis__links"), daten.weiterlesen[weg], true);
      form.hidden = true;
      ergebnis.hidden = false;
      ergebnis.scrollIntoView({ block: "start", behavior: "smooth" });
      ergebnis.focus({ preventScroll: true });
    }
    function vor() {
      if (!form.querySelector(".echt-check__schritt:not([hidden]) input:checked")) {
        var hinweis = schritte[index].querySelector(".echt-check__fehlt");
        if (!hinweis) {
          hinweis = document.createElement("p");
          hinweis.className = "echt-check__fehlt";
          hinweis.setAttribute("role", "alert");
          hinweis.textContent = index === 0 ? "Bitte wählen Sie eine Antwort aus." :
            "Bitte wählen Sie eine Antwort aus. Wenn Sie es nicht wissen, wählen Sie „Weiß nicht“.";
          schritte[index].appendChild(hinweis);
        }
        return;
      }
      if (index < schritte.length - 1) { zeigen(index + 1); } else { auswerten(); }
    }

    weiter.addEventListener("click", vor);
    zurueck.addEventListener("click", function () { if (index > 0) { zeigen(index - 1); } });
    form.addEventListener("change", function (e) {
      var fehlt = e.target.closest(".echt-check__schritt").querySelector(".echt-check__fehlt");
      if (fehlt) { fehlt.remove(); }
      setTimeout(vor, 350);
    });
    form.addEventListener("submit", function (e) { e.preventDefault(); vor(); });
    ergebnis.querySelector('[data-echt="neu"]').addEventListener("click", function () {
      form.reset();
      ergebnis.hidden = true;
      form.hidden = false;
      zeigen(0);
      form.scrollIntoView({ block: "start", behavior: "smooth" });
    });
    zeigen(0);
  }

  /* ---------------------------------------------- E-Mail-Adresse kopieren (falls kein Mailprogramm eingerichtet ist) */
  function kopierKnoepfe() {
    document.querySelectorAll("[data-kopieren]").forEach(function (b) {
      if (!navigator.clipboard || !window.isSecureContext) { return; }
      b.hidden = false;
      b.addEventListener("click", function () {
        navigator.clipboard.writeText(b.getAttribute("data-kopieren")).then(function () {
          b.textContent = "Kopiert ✓";
          setTimeout(function () { b.textContent = "Adresse kopieren"; }, 2500);
        }, function () { b.hidden = true; });
      });
    });
  }

  /* ---------------------------------------------- Start */
  function start() {
    var gespeichert = parseInt(speicher.lesen("nl-schrift") || "0", 10) || 0;
    var stufe = gespeichert;
    figurenBeleben();
    erklaerungen();
    echtCheck();
    kopierKnoepfe();

    var leiste = document.querySelector(".lesehilfe");
    var artikel = document.querySelector("article.artikel");
    if (!leiste || !artikel) { return; }
    leiste.hidden = false;

    leiste.querySelector('[data-aktion="kleiner"]').addEventListener("click", function () { stufe = schriftSetzen(stufe - 1, leiste); });
    leiste.querySelector('[data-aktion="groesser"]').addEventListener("click", function () { stufe = schriftSetzen(stufe + 1, leiste); });
    stufe = schriftSetzen(stufe, leiste);
    vorleser(artikel, leiste.querySelector('[data-aktion="vorlesen"]'));

    var rumpf = artikel.querySelector(".artikel__rumpf");
    if (rumpf) {
      var abschnitte = geraeteAbschnitte(rumpf);
      var gruppe = leiste.querySelector(".lesehilfe__geraet");
      if (abschnitte.iphone.length && abschnitte.android.length && gruppe) {
        gruppe.hidden = false;
        gruppe.querySelectorAll("[data-geraet]").forEach(function (b) {
          b.addEventListener("click", function () { geraetZeigen(abschnitte, b.getAttribute("data-geraet"), leiste, artikel); });
        });
        geraetZeigen(abschnitte, speicher.lesen("nl-geraet") || "alle", leiste, artikel);
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
