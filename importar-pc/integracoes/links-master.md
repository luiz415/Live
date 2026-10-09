# 🔗 LINKS MASTER — Registro Único de Links do Canal
> **Este é o documento-fonte.** Quando um link real existir, preencha a coluna URL e marque os locais ✅.
> Envie-me os links preenchidos e eu atualizo comandos, textos e artes que dependem deles.

## 1. Registro de links

| # | Item | URL (preencher) | Status |
|---|---|---|---|
| 1 | 🖥️ Site oficial | `____________________` | ⬜ pendente |
| 2 | 🎧 Discord (convite) | `____________________` | ⬜ pendente |
| 3 | 📸 Instagram | `____________________` | ⬜ pendente |
| 4 | 📺 Twitch | `https://twitch.tv/exoriservice` | ✅ |
| 5 | 💎 Doação (Tip StreamElements) | `https://streamelements.com/exoriservice/tip` | ✅ (ativar no SE — ver guia) |
| 6 | ➕ Outra rede (opcional: TikTok/X/YouTube) | `____________________` | ⬜ pendente |
| 7 | ➕ Outra rede (opcional) | `____________________` | ⬜ pendente |

## 2. Mapa "onde cada link é usado" (v2 — comandos reduzidos a 5)

| Link → | Comando Nightbot | Timer | Painel do perfil | Overlay ticker | Outro |
|---|---|---|---|---|---|
| Site | `!site` | — | *Redes Sociais* (link) | `!site — …` no CFG | — |
| Discord | — | — | *Discord* (link + texto) | — | — |
| Instagram | — | — | *Redes Sociais* (link) | — | — |
| Tip | — | — | *Apoie o Canal* (link) | — | Config. PayPal no SE |

**Arquivo do ticker:** `assets/overlay/overlay-gameplay.html` → bloco `const CFG` no final → troque o `!site` quando o link existir.

## 3. Rotina de substituição (quando o link chegar)

1. Preencha a URL na tabela acima;
2. Chat da live: `!commands edit !site 🖥️ Site oficial: https://SEULINK` (ver `06-nightbot-guia.md` §2.3);
3. OBS/ arquivo: edite o `CFG.itens` no `overlay-gameplay.html`;
4. Twitch → painéis → adicione o link no painel correspondente;
5. Me avise no chat do projeto — eu regenero artes/textos dependentes, se houver.
