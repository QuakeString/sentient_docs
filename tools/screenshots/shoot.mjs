// Copyright © 2016-2025 The SENTIENT Authors
// Take every screenshot listed in manifest.yml from a running SENTIENT.
//
//   node shoot.mjs [--only id1,id2] [--out ../../static/images/st]
//
// Environment:
//   ST_DOCS_URL         SENTIENT address (default http://localhost:8080)
//   ST_DOCS_SYSADMIN    system administrator "email:password"
//   ST_DOCS_PASSWORD    password of docs@demo.plant (default as in seed.py)
// Writes <id>.webp (and <id>-dark.webp) and tools/screenshots/report.json.
import { chromium } from "playwright";
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import YAML from "yaml";
import sharp from "sharp";

const here = dirname(fileURLToPath(import.meta.url));
const arg = (name, def) => { const i = process.argv.indexOf(name); return i > 0 ? process.argv[i + 1] : def; };
const URL_ = (process.env.ST_DOCS_URL || "http://localhost:8080").replace(/\/$/, "");
const OUT = resolve(here, arg("--out", "../../static/images/st"));
const ONLY = (arg("--only", "") || "").split(",").filter(Boolean);
const manifest = YAML.parse(readFileSync(resolve(here, "manifest.yml"), "utf8"));
const D = manifest.defaults || {};
const [saUser, saPass] = (process.env.ST_DOCS_SYSADMIN || ":").split(/:(.*)/s);
const USERS = {
  tenant: ["docs@demo.plant", process.env.ST_DOCS_PASSWORD || "DocsDemo#2025"],
  sysadmin: [saUser, saPass],
};

// Freeze anything that moves so two runs give the same picture.
const STILL = `*,*::before,*::after{transition:none!important;animation-duration:0s!important;animation-delay:0s!important;caret-color:transparent!important}
.mat-mdc-progress-bar,mat-progress-bar{visibility:hidden!important}`;

async function api(token, path) {
  const r = await fetch(URL_ + path, { headers: { "X-Authorization": "Bearer " + token } });
  if (!r.ok) throw new Error(`${path} -> ${r.status}`);
  return r.json();
}
async function restLogin([username, password]) {
  const r = await fetch(URL_ + "/api/auth/login", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ username, password }) });
  if (!r.ok) throw new Error(`login ${username} -> ${r.status}`);
  return (await r.json()).token;
}
// {device:Name} -> id
async function expand(url, token) {
  const lookups = {
    device: async (n) => (await api(token, "/api/tenant/devices?deviceName=" + encodeURIComponent(n))).id.id,
    asset: async (n) => (await api(token, "/api/tenant/assets?assetName=" + encodeURIComponent(n))).id.id,
    dashboard: async (n) => (await api(token, "/api/tenant/dashboards?pageSize=50&page=0&textSearch=" + encodeURIComponent(n))).data.find((d) => d.title === n).id.id,
    ruleChain: async (n) => (await api(token, "/api/ruleChains?pageSize=50&page=0&textSearch=" + encodeURIComponent(n))).data.find((d) => d.name === n).id.id,
  };
  let out = url;
  for (const m of url.matchAll(/\{(device|asset|dashboard|ruleChain):([^}]+)\}/g)) out = out.replace(m[0], await lookups[m[1]](m[2]));
  return out;
}
// Close notices that are not part of the screen being documented.
async function dismiss(page) {
  for (const sel of ["mat-dialog-container:has-text('License') button:has-text('Close')",
                     ".st-notice button[aria-label='Dismiss']", "button:has-text('Got it')"]) {
    const b = page.locator(sel);
    if (await b.count()) { await b.first().click().catch(() => {}); await page.waitForTimeout(300); }
  }
}
async function formLogin(page, [user, pass]) {
  await page.goto(URL_ + "/login");
  await page.waitForSelector("#username-input");
  await dismiss(page);
  await page.fill("#username-input", user);
  await page.fill("#password-input", pass);
  await page.click("button[type=submit]");
  await page.waitForURL((u) => !u.pathname.startsWith("/login"), { timeout: 20000 });
}
async function settle(page) {
  await page.waitForLoadState("networkidle").catch(() => {});
  await page.waitForTimeout(600);
  await dismiss(page);
}

const browser = await chromium.launch();
const contexts = {};
async function contextFor(as, theme, size) {
  const key = `${as}|${theme}|${size}`;
  if (contexts[key]) return contexts[key];
  const ctx = await browser.newContext({ viewport: { width: size[0], height: size[1] }, deviceScaleFactor: 1, colorScheme: theme,
                                         locale: "en-US", timezoneId: "Asia/Kolkata" });
  await ctx.addInitScript((css) => { addEventListener("DOMContentLoaded", () => { const s = document.createElement("style"); s.textContent = css; document.head.appendChild(s); }); }, STILL);
  if (as !== "none") {
    const p = await ctx.newPage();
    await formLogin(p, USERS[as]);
    await p.close();
    ctx.token = await restLogin(USERS[as]);
  }
  return (contexts[key] = ctx);
}

mkdirSync(OUT, { recursive: true });
const report = [];
let failed = 0;
for (const s of manifest.shots) {
  if (ONLY.length && !ONLY.includes(s.id)) continue;
  const as = s.as || D.as || "tenant", size = s.size || D.size || [1440, 900];
  for (const theme of s.themes || D.themes || ["light"]) {
    const name = s.id + (theme === "dark" ? "-dark" : "");
    const t0 = Date.now();
    try {
      const ctx = await contextFor(as, theme, size);
      const page = await ctx.newPage();
      await page.goto(URL_ + (as === "none" ? s.url : await expand(s.url, ctx.token)));
      await settle(page);
      for (const st of s.steps || []) {
        if (st.click) await page.click(st.click);
        if (st.fill) await page.fill(st.fill[0], st.fill[1]);
        if (st.press) await page.keyboard.press(st.press);
        if (st.hover) await page.hover(st.hover);
        if (st.waitFor) await page.waitForSelector(st.waitFor);
        if (st.scroll) await page.locator(st.scroll).scrollIntoViewIfNeeded();
        if (st.wait) await page.waitForTimeout(st.wait);
        await settle(page);
      }
      const opts = { mask: (s.mask || []).map((m) => page.locator(m)), maskColor: "#9e9e9e" };
      if (s.clip) opts.clip = { x: s.clip[0], y: s.clip[1], width: s.clip[2], height: s.clip[3] };
      if (s.capture) {
        const box = await page.locator(s.capture).first().boundingBox();
        const pad = s.pad ?? 8;
        opts.clip = { x: Math.max(0, box.x - pad), y: Math.max(0, box.y - pad), width: box.width + 2 * pad, height: box.height + 2 * pad };
      }
      const png = await page.screenshot(opts);
      const file = resolve(OUT, name + ".webp");
      const info = await sharp(png).webp({ quality: 82 }).toFile(file);
      report.push({ id: name, ok: true, file, width: info.width, height: info.height, ms: Date.now() - t0 });
      console.log(`ok    ${name}  ${info.width}x${info.height}`);
      await page.close();
    } catch (e) {
      failed++;
      report.push({ id: name, ok: false, error: String(e.message || e).split("\n")[0] });
      console.log(`FAIL  ${name}  ${String(e.message || e).split("\n")[0]}`);
    }
  }
}
await browser.close();
writeFileSync(resolve(here, "report.json"), JSON.stringify({ url: URL_, at: new Date().toISOString(), shots: report }, null, 2));
console.log(`${report.length - failed} taken, ${failed} failed -> ${OUT}`);
process.exit(failed ? 1 : 0);
