#!/usr/bin/env node
/* ─────────────────────────────────────────────────────────────────────────────
 * twitch-contador-server.js
 *
 * Servidor local que faz DUAS coisas:
 *
 *   A. Proxy da Twitch  (GET  /twitch-viewers)
 *      - widget "Contador de Espectadores da Twitch" consome aqui.
 *      - evita CORS e segredos no HTML público.
 *
 *   B. State-bus do Party Tracker  (GET|POST /party-data)
 *      - painel admin (Custom Browser Dock) POSTa o JSON ao salvar.
 *      - widget público da cena 02 GETa o JSON a cada 2 s.
 *      - assim funciona MESMO quando o OBS roda browser-source e
 *        custom-dock em processos CEF separados (o localStorage não
 *        se compartilha).
 *      - o estado é persistido em party-data.json ao lado deste script
 *        para sobreviver a reinícios do servidor.
 *
 * Como usar:
 *   1. Criar app em https://dev.twitch.tv/console/apps  (categorização: "Other")
 *      Anotar CLIENT_ID e gerar um CLIENT_SECRET.
 *   2. Colar CLIENT_ID e CLIENT_SECRET em um arquivo .env ao lado deste script
 *      (ou exportar como variáveis de ambiente antes de rodar).
 *   3. Editar TWITCH_LOGIN abaixo (default "exoriservice").
 *   4. Abrir este terminal e rodar:  node twitch-contador-server.js
 *   5. O widget do contador consome     http://127.0.0.1:7777/twitch-viewers
 *      O widget do Party Tracker        http://127.0.0.1:7777/party-data  (GET)
 *      O painel admin do Party Tracker  http://127.0.0.1:7777/party-data  (POST)
 *
 * Variáveis de ambiente (opcional, sobrescreve o .env):
 *   PORT         porta (default 7777)
 *   CLIENT_ID    obrigatório (Twitch)
 *   CLIENT_SECRET obrigatório (Twitch)
 *   TWITCH_LOGIN login do canal (default exoriservice)
 *
 * O arquivo .env (OPCIONAL) deve ficar em /home/user/Live/integracoes/.env,
 * com o formato:
 *
 *   PORT=7777
 *   CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxx
 *   CLIENT_SECRET=yyyyyyyyyyyyyyyyyyyyyyyyy
 *   TWITCH_LOGIN=exoriservice
 * ────────────────────────────────────────────────────────────────────────── */
"use strict";

const http = require("http");
const fs   = require("fs");
const path = require("path");

/* ─── carrega .env (sem dependências externas) ─── */
function loadEnv(file) {
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
loadEnv(path.join(__dirname, ".env"));

const PORT          = parseInt(process.env.PORT || "7777", 10);
const CLIENT_ID     = process.env.CLIENT_ID;
const CLIENT_SECRET = process.env.CLIENT_SECRET;
const TWITCH_LOGIN  = (process.env.TWITCH_LOGIN || "exoriservice").toLowerCase();

if (!CLIENT_ID || !CLIENT_SECRET) {
  console.error("Faltam CLIENT_ID e/ou CLIENT_SECRET. Coloque em integracoes/.env ou exporte como variáveis.");
  console.error("Veja cabeçalho deste arquivo.");
  process.exit(1);
}

/* ─── Estado do Party Tracker (persistido em disco) ─── */
const PARTY_FILE = path.join(__dirname, "party-data.json");
const PARTY_FALLBACK = { title: "PARTY", view: "", quest: "sw",
  rows: [{v:"",l:""},{v:"",l:""},{v:"",l:""},{v:"",l:""},{v:"",l:""}] };
let partyState = (() => {
  try { const s = JSON.parse(fs.readFileSync(PARTY_FILE, "utf8"));
    return s && s.rows ? s : JSON.parse(JSON.stringify(PARTY_FALLBACK));
  } catch (_) { return JSON.parse(JSON.stringify(PARTY_FALLBACK)); }
})();
function savePartyToDisk() {
  try { fs.writeFileSync(PARTY_FILE, JSON.stringify(partyState, null, 2)); }
  catch (e) { console.error("falha ao gravar party-data.json:", e.message); }
}
/* ETag (monotônico) para o widget saber se mudou sem reenviar tudo */
let partyEtag = 1;

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

/* ─── util: body do POST (leitura de JSON) ─── */
function readBody(req, limit) {
  return new Promise((resolve, reject) => {
    let total = 0; const chunks = [];
    req.on("data", c => { total += c.length; if (total > limit) return reject(new Error("body too big")); chunks.push(c); });
    req.on("end", () => { try { resolve(Buffer.concat(chunks).toString("utf8")); } catch(e){ reject(e); } });
    req.on("error", reject);
  });
}

/* ─── HTTP server ─── */
function json(res, code, obj, extra) {
  const body = JSON.stringify(obj);
  const hdrs = {
    "Content-Type": "application/json; charset=utf-8",
    "Content-Length": Buffer.byteLength(body),
    "Access-Control-Allow-Origin": "*",
    "Cache-Control": "no-store",
  };
  if (extra) Object.assign(hdrs, extra);
  res.writeHead(code, hdrs);
  res.end(body);
}

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, If-None-Match",
};

const server = http.createServer(async (req, res) => {
  try {
    if (req.method === "OPTIONS") { res.writeHead(204, CORS); return res.end(); }

    /* ─── health ─── */
    if (req.url === "/" || req.url === "/health")
      return json(res, 200, { ok: true, services: ["twitch-viewers", "party-data"], login: TWITCH_LOGIN });

    /* ─── Twitch viewers ─── */
    if (req.url === "/twitch-viewers") {
      const p = await fetchStream();
      return json(res, 200, { ...p, fetched_at: new Date().toISOString() });
    }

    /* ─── Party Tracker: GET (widget polling) ─── */
    if (req.url === "/party-data" && req.method === "GET") {
      const inm = req.headers["if-none-match"];
      const tag = '"p' + partyEtag + '"';
      if (inm === tag) { res.writeHead(304, CORS); return res.end(); }
      return json(res, 200, { ...partyState, etag: partyEtag, updated_at: new Date().toISOString() }, { ETag: tag });
    }

    /* ─── Party Tracker: POST (admin salva) ─── */
    if (req.url === "/party-data" && req.method === "POST") {
      const raw = await readBody(req, 64 * 1024);
      let incoming; try { incoming = JSON.parse(raw); } catch (e) { return json(res, 400, { error: "invalid_json" }); }
      /* validação mínima */
      if (!incoming || !Array.isArray(incoming.rows) || incoming.rows.length !== 5)
        return json(res, 400, { error: "bad_shape" });
      const next = JSON.parse(JSON.stringify(PARTY_FALLBACK));
      next.title  = String(incoming.title  || "PARTY").slice(0, 14).toUpperCase();
      next.view   = String(incoming.view   || "").toUpperCase().replace(/[^A-Z]/g, "").slice(0, 2);
      next.quest  = incoming.quest === "sa" ? "sa" : "sw";
      for (let i = 0; i < 5; i++) {
        const r = incoming.rows[i] || {};
        next.rows[i].v = String(r.v || "").toUpperCase().replace(/[^A-Z]/g, "").slice(0, 2);
        next.rows[i].l = String(r.l || "").replace(/[^0-9]/g, "").slice(0, 4);
      }
      partyState = next;
      partyEtag += 1;
      savePartyToDisk();
      return json(res, 200, { ok: true, etag: partyEtag });
    }

    return json(res, 404, { error: "not found" }, CORS);
  } catch (e) {
    console.error(e.message || e);
    return json(res, 502, { online: false, viewers: 0, error: "server_error", message: String(e.message || e) }, CORS);
  }
});
server.listen(PORT, "127.0.0.1", () => {
  console.log("twitch-contador-server ouvindo em http://127.0.0.1:" + PORT + " — canal: " + TWITCH_LOGIN);
});