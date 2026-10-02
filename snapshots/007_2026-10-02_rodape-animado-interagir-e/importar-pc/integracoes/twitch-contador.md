# Contador de Espectadores da Twitch — passo a passo deste snapshot

Esta página **não é tutorial genérico**. É a doc específica do que existe no
repositório após o snapshot 002. Lê junto com `integracoes/twitch-contador-server.js`
e `assets/overlay/contador-twitch.html`.

## O que é

- **Proxy local** (`integracoes/twitch-contador-server.js`): script Node que
  consulta a Twitch Helix API (`/helix/streams?user_login=exoriservice`) usando
  um **App Access Token** (OAuth 2.0 client credentials). Esse token é o único
  jeito oficial de ler `viewer_count` sem expor credenciais no OBS. O proxy
  escuta em `127.0.0.1:7777` (configurável com `PORT`).
- **Widget** (`assets/overlay/contador-twitch.html`): browser source do OBS que
  consome `http://127.0.0.1:7777/twitch-viewers` a cada 30 s. Mostra o número
  com a identidade verde-ácido do canal. Estados: carregando, online, offline,
  indisponível.

## Por que há um proxy

- O browser source do OBS não tem CORS liberado para `api.twitch.tv` no GET
  da API pública.
- O `client_secret` do app da Twitch **não pode** ir em código aberto
  (repositório é público).

## Como colocar no ar (ação manual no seu PC)

1. Criar app em https://dev.twitch.tv/console/apps — categoria "Other".
   Anotar **Client ID** e gerar um **Client Secret**.
2. Criar `integracoes/.env` com:
   ```
   PORT=7777
   CLIENT_ID=...
   CLIENT_SECRET=...
   TWITCH_LOGIN=exoriservice
   ```
3. Abrir um terminal e rodar: `node integracoes/twitch-contador-server.js`.
4. No OBS, adicionar uma nova **Fonte de Navegador** apontando para
   `file:///C:/twitch/exoriservice/assets/overlay/contador-twitch.html`,
   com `Largura=400`, `Altura=80`, `Controle da página web=1`.
5. Posicionar onde ficar bom (canto superior direito da gameplay).

## Endpoints do proxy

- `GET /` ou `/health` — `{ok:true, service, login}`
- `GET /twitch-viewers` —
  ```json
  { "online": true, "viewers": 1234, "title": "...", "game": "Tibia",
    "started_at": "2026-10-01T00:00:00Z", "fetched_at": "..." }
  ```
  ou
  ```json
  { "online": false, "viewers": 0 }
  ```
  em caso de falha upstream: HTTP 502 com `{online:false, error:"twitch_unreachable", message}`.

## Limites e tratamento de erro

- 30 s entre consultas (cache local no proxy) — bem abaixo dos limites da
  Twitch Helix (800 req/min para OAuth2, ~30 req/min para `/helix/streams`).
- Em erro de rede, o widget entra em modo "indisponível" e **não exibe um
  número antigo como se fosse atual** (requisito do item 6 do briefing).
- O widget só consulta a Twitch; não consulta YouTube, Kick ou outras.

## Onde está posicionado no novo layout

Canto superior direito da gameplay (região 1580,16 px, 320×80), ao lado da
moldura da webcam. Ver `obs/exoriservice-cenas.json` (snapshot 002).

## O que falta para terminar (depende de você)

- [ ] App Twitch criado em dev.twitch.tv
- [ ] `integracoes/.env` preenchido
- [ ] Terminal aberto com o server rodando durante as lives