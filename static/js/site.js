/* SENTIENT Docs. Copyright © 2016-2025 The SENTIENT Authors */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var root = document.documentElement;
  var VERSION = ($('meta[name="st-docs-version"]') || {}).content || "";
  var BASE = ($('meta[name="st-docs-base"]') || {}).content || "";

  /* ---------- theme ---------- */
  function isDark() { return root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches; }
  function syncIcon() { var i = $("#themeIcon"); if (i) i.setAttribute("href", isDark() ? "#i-sun" : "#i-moon"); }
  /* screenshots with a -dark twin follow the theme */
  function syncShots() {
    var d = isDark();
    document.querySelectorAll("img[data-dark]").forEach(function (im) {
      var src = im.getAttribute("src"), dark = /-dark\.(webp|png)$/.test(src);
      if (d && !dark) im.setAttribute("src", src.replace(/\.(webp|png)$/, "-dark.$1"));
      if (!d && dark) im.setAttribute("src", src.replace(/-dark\.(webp|png)$/, ".$1"));
    });
  }
  syncIcon(); syncShots();
  matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function () { syncIcon(); syncShots(); });
  $("#themeBtn").addEventListener("click", function () {
    /* picking the theme the system already uses goes back to following the system */
    var want = isDark() ? "light" : "dark";
    var sys = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    if (want === sys) {
      delete root.dataset.theme;
      try { localStorage.removeItem("st-docs-theme"); } catch (e) {}
    } else {
      root.dataset.theme = want;
      try { localStorage.setItem("st-docs-theme", want); } catch (e) {}
    }
    syncIcon(); syncShots();
  });

  /* ---------- mobile nav ---------- */
  $("#menuBtn").addEventListener("click", function () { $("#nav").classList.toggle("open"); });
  var cur = $(".nav a[aria-current]");
  if (cur) { cur.scrollIntoView({ block: "center" }); window.scrollTo(0, 0); }

  /* ---------- version switcher ---------- */
  var vb = $("#verBtn"), vm = $("#verMenu");
  vb.addEventListener("click", function (e) { e.stopPropagation(); vm.classList.toggle("open"); vb.setAttribute("aria-expanded", vm.classList.contains("open")); });
  document.addEventListener("click", function () { vm.classList.remove("open"); vb.setAttribute("aria-expanded", "false"); });
  // versions.json: {"latest":"4.3.0.57","versions":[{"version":"4.3.0.57","path":"/","note":"Latest","releases":["4.3.0.57"]}, ...]}
  fetch("/versions.json").then(function (r) { return r.ok ? r.json() : null; }).then(function (data) {
    if (!data || !data.versions) return;
    var here = location.pathname;
    var mine = data.versions.filter(function (v) { return v.version === VERSION; })[0];
    var rel = mine && mine.path !== "/" && here.indexOf(mine.path) === 0 ? here.slice(mine.path.length - 1) : here;
    $("#verList").innerHTML = data.versions.map(function (v) {
      var href = (v.path === "/" ? "" : v.path.replace(/\/$/, "")) + rel;
      return '<a role="menuitem" href="' + href + '" data-root="' + v.path + '"><span class="v">' + v.version + '</span><span class="note">' + (v.note || "") +
        '</span><span class="sel">' + (v.version === VERSION ? "✓" : "") + "</span></a>";
    }).join("");
    $$("#verList a").forEach(function (a) {
      a.addEventListener("click", function (e) {
        // fall back to the version's home page when this page does not exist there
        e.preventDefault();
        var href = a.getAttribute("href"), home = a.dataset.root.replace(/\/$/, "") + "/docs/";
        fetch(href, { method: "HEAD" }).then(function (r) { location.href = r.ok ? href : home; }, function () { location.href = home; });
      });
    });
  }).catch(function () {});

  /* ---------- content enhancements ---------- */
  // tabs built from <div class="st-tabs"><div class="st-tab" data-label="..">
  $$(".st-tabs").forEach(function (box, n) {
    var tabs = $$(":scope > .st-tab", box);
    if (!tabs.length) return;
    var list = document.createElement("div");
    list.className = "st-tablist"; list.setAttribute("role", "tablist");
    tabs.forEach(function (t, i) {
      var b = document.createElement("button");
      b.type = "button"; b.setAttribute("role", "tab"); b.textContent = t.dataset.label || ("Option " + (i + 1));
      b.setAttribute("aria-selected", i === 0 ? "true" : "false");
      t.hidden = i !== 0; t.setAttribute("role", "tabpanel");
      b.addEventListener("click", function () {
        $$("button", list).forEach(function (x) { x.setAttribute("aria-selected", x === b ? "true" : "false"); });
        tabs.forEach(function (x) { x.hidden = x !== t; });
      });
      list.appendChild(b);
    });
    box.insertBefore(list, box.firstChild);
  });
  // wide tables scroll inside their own box
  $$(".prose table").forEach(function (t) {
    if (t.parentElement.classList.contains("tablewrap")) return;
    var w = document.createElement("div"); w.className = "tablewrap";
    t.parentNode.insertBefore(w, t); w.appendChild(t);
  });
  // copy buttons on code blocks
  $$(".prose pre").forEach(function (pre) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "copy"; b.textContent = "Copy";
    b.addEventListener("click", function () {
      var text = (pre.querySelector("code") || pre).innerText;
      var done = function () { b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy"; }, 1500); };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {});
    });
    pre.appendChild(b);
  });
  // heading anchors
  $$(".prose h2[id], .prose h3[id], .prose h4[id]").forEach(function (h) {
    var a = document.createElement("a"); a.className = "anchor"; a.href = "#" + h.id; a.textContent = "#"; a.setAttribute("aria-label", "Link to this section");
    h.appendChild(a);
  });
  // videos need the internet: show a link when offline
  $$(".prose iframe[src*='youtube']").forEach(function (f) {
    if (navigator.onLine) return;
    var d = document.createElement("div"); d.className = "offline-video";
    d.textContent = "This video needs an internet connection: " + f.src;
    (f.closest("#video") || f).replaceWith(d);
  });
  // image lightbox
  var lb = $("#lightbox");
  $$(".st-gallery figure, .prose p > img").forEach(function (el) {
    el.addEventListener("click", function () {
      var img = el.tagName === "IMG" ? el : $("img", el);
      $("img", lb).src = img.src; $("img", lb).alt = img.alt; lb.classList.add("open");
    });
  });
  lb.addEventListener("click", function () { lb.classList.remove("open"); });
  // on-this-page highlight
  var tocLinks = $$("#toc a[data-target]");
  if (tocLinks.length && "IntersectionObserver" in window) {
    var heads = tocLinks.map(function (a) { return document.getElementById(a.dataset.target); }).filter(Boolean);
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.toggle("on", a.dataset.target === en.target.id); });
        }
      });
    }, { rootMargin: "-70px 0px -70% 0px" });
    heads.forEach(function (h) { obs.observe(h); });
  }
  var cl = $("#copyLink");
  if (cl) cl.addEventListener("click", function (e) {
    e.preventDefault();
    if (navigator.clipboard) navigator.clipboard.writeText(location.href.split("#")[0]).then(function () { cl.lastChild.textContent = "Link copied"; });
  });
  $$("[data-helpful]").forEach(function (b) {
    b.addEventListener("click", function () { b.parentElement.firstChild.textContent = "Thanks for the feedback. "; });
  });

  /* ---------- search (Pagefind, fully offline) ---------- */
  var scrim = $("#scrim"), q = $("#q"), results = $("#results"), pf = null, area = "", sel = 0, hits = [], seq = 0;
  function loadPagefind() {
    if (pf) return Promise.resolve(pf);
    return import(BASE + "/pagefind/pagefind.js").then(function (m) { pf = m; return pf.options({ excerptLength: 18, baseUrl: BASE + "/" }).then(function () { return pf; }); });
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function render() {
    if (!hits.length) {
      results.innerHTML = q.value.trim() ? '<div class="empty">No results for "' + esc(q.value) + '".</div>' : '<div class="empty">Type to search. Try "modbus", "backup" or "alarm rules".</div>';
      return;
    }
    results.innerHTML = hits.map(function (h, i) {
      return '<a class="res' + (i === sel ? " on" : "") + '" href="' + h.url + '"><svg class="icon"><use href="#i-doc"/></svg><span><b>' + esc(h.meta.title || h.url) + "</b><small>" + h.excerpt + "</small></span></a>";
    }).join("");
  }
  function search() {
    var term = q.value.trim(), my = ++seq;
    if (!term) { hits = []; render(); return; }
    loadPagefind().then(function (p) {
      var opts = area ? { filters: { area: area } } : {};
      return p.debouncedSearch(term, opts, 150);
    }).then(function (res) {
      if (!res || my !== seq) return;
      return Promise.all(res.results.slice(0, 12).map(function (r) { return r.data(); }));
    }).then(function (data) {
      if (!data || my !== seq) return;
      hits = data; sel = 0; render();
    }).catch(function () {
      results.innerHTML = '<div class="empty">Search index not found. Build the site with tools/build.sh.</div>';
    });
  }
  function open(term) { scrim.classList.add("open"); q.value = term || ""; search(); setTimeout(function () { q.focus(); }, 10); loadPagefind().catch(function () {}); }
  function close() { scrim.classList.remove("open"); }
  $("#searchBtn").addEventListener("click", function () { open(); });
  var big = $("#bigSearch"); if (big) big.addEventListener("click", function () { open(); });
  $$(".popular button").forEach(function (b) { b.addEventListener("click", function () { open(b.dataset.q); }); });
  q.addEventListener("input", search);
  $$("#scope button").forEach(function (b) {
    b.addEventListener("click", function () {
      area = b.dataset.s; $$("#scope button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      search(); q.focus();
    });
  });
  scrim.addEventListener("click", function (e) { if (e.target === scrim) close(); });
  document.addEventListener("keydown", function (e) {
    var typing = /INPUT|TEXTAREA/.test(document.activeElement.tagName);
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") { e.preventDefault(); open(); return; }
    if (e.key === "/" && !typing) { e.preventDefault(); open(); return; }
    if (e.key === "Escape") { close(); lb.classList.remove("open"); }
    if (!scrim.classList.contains("open")) return;
    if (e.key === "ArrowDown") { sel = Math.min(sel + 1, hits.length - 1); render(); e.preventDefault(); }
    if (e.key === "ArrowUp") { sel = Math.max(sel - 1, 0); render(); e.preventDefault(); }
    if (e.key === "Enter" && hits[sel]) { location.href = hits[sel].url; }
  });
})();
