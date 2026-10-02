#!/usr/bin/env node
/* ─────────────────────────────────────────────────────────────────────────────
 * twitch-contador-server.js
 *
 * Proxy local para o widget "Contador de Espectadores da Twitch".
 * Roda em localhost:porta. O widget contador-twitch.html consome daqui.
 *
 * Por que um proxy local?
 *   - A Twitch exige Client Credentials (app access token), obtido por
 *     client_id + client_secret. Esse segredo NÃO PODE ir pro HTML público.
 *   - O browser_source do OBS não pode fazer CORS para a Twitch direto.
 *
 * Como usar:
 *   1. Criar app em https://dev.twitch.tv/console/apps  (categorização: "Other")
 *      Anotar CLIENT_ID e gerar um CLIENT_SECRET.
 *   2. Colar CLIENT_ID e CLIENT_SECRET em integracoes/.env ao lado deste script.
 *   3. Editar TWITCH_LOGIN abaixo (default "exoriservice").
 *   4. Abrir o cmd nesta pasta e rodar:  node twitch-contador-server.js
 *   5. O widget contador consome http://127.0.0.1:7777/twitch-viewers.
 *
 * Variáveis de ambiente (opcional, sobrescreve o .env):
 *   PORT         porta (default 7777)
 *   CLIENT_ID    obrigatório
 *   CLIENT_SECRET obrigatório
 *   TWITCH_LOGIN login do canal (default exoriservice)
 *
 * O arquivo .env (OPCIONAL) deve ficar em integracoes/.env com:
 *
 *   PORT=7777
 *   CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxx
 *   CLIENT_SECRET=yyyyyyyyyyyyyyyyyyyyyyyyy
 *   TWITCH_LOGIN=exoriservice
 * ────────────────────────────────────────────────────────────────────────── */
"use strict";

const http = require("http");

/* ─── carrega .env (sem dependências externas) ─── */
function loadEnv(file) {
  const fs   = require("fs");
  const path = require("path");
  try {
    const txt = fs.readFileSync(file, "utf8");
    for (const raw of txt.split(/\r?\n/)) {
      const m = raw.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/i);
      if (!m) continue;
      let v = m[2];
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      if (!process.env[m[1]]) process.env[m[1]] = v;
    }
  } catch (_) {}
}
loadEnv(require("path").join(__dirname, ".env"));

const PORT          = parseInt(process.env.PORT || "7777", 10);
const CLIENT_ID     = process.env.CLIENT_ID;
const CLIENT_SECRET = process.env.CLIENT_SECRET;
const TWITCH_LOGIN  = (process.env.TWITCH_LOGIN || "exoriservice").toLowerCase();

if (!CLIENT_ID || !CLIENT_SECRET) {
  console.error("Faltam CLIENT_ID e/ou CLIENT_SECRET. Coloque em integracoes/.env ou exporte como variáveis.");
  console.error("Veja cabeçalho deste arquivo.");
  process.exit(1);
}

/* ─── cache do app access token (válido por 1h, renovamos quando expira) ─── */
let tokenCache = { token: null, expiresAt: 0 };

async function getAppToken() {
  if (tokenCache.token && Date.now() < tokenCache.expiresAt - 60_000) return tokenCache.token;
  const body = new URLSearchParams({
    client_id: CLIENT_ID, client_secret: CLIENT_SECRET,
    grant_type: "client_credentials",
  });
  const r = await fetch("https://id.twitch.tv/oauth2/token", { method: "POST", body });
  if (!r.ok) throw new Error("oauth2 " + r.status);
  const j = await r.json();
  tokenCache = { token: j.access_token, expiresAt: Date.now() + j.expires_in * 1000 };
  return j.access_token;
}

/* ─── estado em cache da live (30 s) ─── */
let streamCache = { at: 0, payload: null };
const CACHE_MS = 30_000;

async function fetchStream() {
  if (streamCache.payload && Date.now() - streamCache.at < CACHE_MS) return streamCache.payload;
  const tok = await getAppToken();
  const r = await fetch("https://api.twitch.tv/helix/streams?user_login=" + encodeURIComponent(TWITCH_LOGIN), {
    headers: { "Client-ID": CLIENT_ID, "Authorization": "Bearer " + tok },
  });
  if (!r.ok) throw new Error("helix " + r.status);
  const j = await r.json();
  const s = j.data && j.data[0];
  const payload = s
    ? { online: true,  viewers: s.viewer_count, title: s.title, game: s.game_name, started_at: s.started_at }
    : { online: false, viewers: 0 };
  streamCache = { at: Date.now(), payload };
  return payload;
}

/* ─── HTTP server ─── */
function json(res, code, obj) {
  const body = JSON.stringify(obj);
  res.writeHead(code, {
    "Content-Type": "application/json; charset=utf-8",
    "Content-Length": Buffer.byteLength(body),
    "Access-Control-Allow-Origin": "*",
    "Cache-Control": "no-store",
  });
  res.end(body);
}

const server = http.createServer(async (req, res) => {
  try {
    if (req.method === "OPTIONS") { res.writeHead(204, { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET, OPTIONS" }); return res.end(); }
    if (req.url === "/" || req.url === "/health") return json(res, 200, { ok: true, service: "twitch-viewers", login: TWITCH_LOGIN });
    if (req.url === "/twitch-viewers") {
      const p = await fetchStream();
      return json(res, 200, { ...p, fetched_at: new Date().toISOString() });
    }
    return json(res, 404, { error: "not found" });
  } catch (e) {
    console.error(e.message || e);
    return json(res, 502, { online: false, viewers: 0, error: "twitch_unreachable", message: String(e.message || e) });
  }
});
server.listen(PORT, "127.0.0.1", () => {
  console.log("twitch-contador-server ouvindo em http://127.0.0.1:" + PORT + " — canal: " + TWITCH_LOGIN);
});
