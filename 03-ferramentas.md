# 🧰 Etapa 2 — Stack de Ferramentas Oficial do Projeto
**Restrição: 100% gratuito.** Critérios: qualidade, confiabilidade, personalização e custo-benefício.
*Verificado em set/2026 — todas as ferramentas abaixo estão ativas e mantidas.*

---

## 1. Stack escolhida (resumo executivo)

| Finalidade | Ferramenta | Custo | Por que ganhou |
|---|---|---|---|
| Alertas, widgets e doações | **StreamElements** | Grátis | Única com personalização total via HTML/CSS/JS — as artes de alerta que eu criar entram colando o código pronto; processa tudo na nuvem (leve para o PC) |
| Bot de chat, comandos, timers, moderação | **Nightbot** | Grátis | Padrão do mercado, em nuvem (nada rodando no seu PC), comandos/timers/filtros maduros e confiáveis |
| Telas de cena (Starting/BRB/End) + overlay gameplay | **HTML local no OBS** (Browser Source → arquivo) | Grátis | Zero dependência externa, funciona offline, animações leves, 100% do código controlado por nós |
| Chat na cena Just Chatting | **Widget de chat do StreamElements** | Grátis | Customização completa do visual via CSS (meu código) |
| Moderação (visão de mod) | **Twitch Mod View** (nativo) | Grátis | Ferramenta oficial, sem conta extra |
| Música sem copyright (telas de espera) | **Pretzel Rocks (free)** ou **StreamBeats** | Grátis | Livres de DMCA; player removido do overlay a pedido (v5) — usar externo se quiser |
| Criação de artes | **Eu crio** (geração + composição programática) | Grátis | Dimensões exatas, transparência e textos sem erro |
| Retoques pontuais suas (futuro) | Photopea (navegador) ou GIMP | Grátis | Só se você quiser mexer em algo depois |
| Stinger (transição animada) | **Eu renderizo** WebM com canal alfa → OBS importa nativo | Grátis | Sob medida na identidade visual |
| Áudio (voz) | **Filtros nativos do OBS** + ReaPlugs (VST grátis) | Grátis | Cadeia profissional: supressão → gate → EQ → compressor |
| Testes de transmissão | Twitch Inspector + gravação local OBS | Grátis | Validação técnica antes de ir ao ar |

**Contas gratuitas que você vai criar (5 minutos, na fase de integrações):**
1. `streamelements.com` — entrar com a Twitch e autorizar;
2. `nightbot.tv` — entrar com a Twitch → "Join Channel" → digitar `/mod nightbot` no seu chat;
3. *(Opcional)* `pretzel.rocks` — entrar com a Twitch.

---

## 2. Análise por área (justificativas)

### 2.1 Alertas e widgets — StreamElements ✅

| Critério | StreamElements | Streamlabs | OBS puro |
|---|---|---|---|
| Preço | 100% grátis, sem plano pago obrigatório | Empurra Prime ($149/ano) | Grátis |
| Customização | **Total: HTML + CSS + JS** | Moderada, limitada ao editor deles | Manual, sem eventos (follows/subs/bits) já integrados |
| Peso no PC | Leve (processa na nuvem) | Pesado | — |
| Eventos Twitch (sub/bits/raid) | Já integrados | Já integrados | Exige desenvolver API na mão |

**Veredito:** StreamElements. É a única plataforma gratuita que aceita **código customizado completo** nos alertas — ou seja, o design de alerta "banner médio com dragão e verde ácido" que especificamos será implementado de verdade, sem template genérico. Os alertas rodam via Browser Source na nuvem (não consome seu PC) e a página de doações (tips) também é gratuita.

### 2.2 Bot de chat — Nightbot ✅

| Critério | Nightbot | StreamElements Bot | Fossabot | Bot local (Streamer.bot etc.) |
|---|---|---|---|---|
| Hospedagem | Nuvem | Nuvem | Nuvem | Seu PC 24/7 |
| Comandos custom + timers | ✅ | ✅ | ✅ | ✅ |
| Moderação (spam/links/palavras) | ✅ 6 filtros maduros | Básica | ✅ forte | ✅ máxima |
| Curva de aprendizado | Baixa | Baixa | Média | Alta |
| Custo | Grátis, sem plano pago | Grátis | Grátis | Grátis |

**Veredito:** **Nightbot** como bot principal (comandos `!site`, `!discord`, `!instagram`, timers de divulgação, boas-vindas, moderação completa — tudo em nuvem, confiável há uma década). O bot do StreamElements fica como reforço opcional no futuro (loyalty points, por exemplo). Bots locais (Streamer.bot) são um upgrade de power user que não faz sentido agora — exigiriam seu PC ligado 24/7 para o bot ficar ativo.

### 2.3 Telas de cena e overlay — HTML local no OBS ✅

- Eu entrego cada tela (Starting Soon, BRB, Encerramento) e o overlay como **arquivo HTML animado autônomo** → você adiciona no OBS como Browser Source apontando para o arquivo local ("Arquivo Local" ✅);
- Vantagens: animação fluida e leve, zero dependência de serviço externo (se a internet do widget cair, sua tela continua), ajustes de texto direto no arquivo;
- Alertas e chat **não** são locais — precisam do StreamElements para receber os eventos da Twitch — por isso a stack é híbrida: *telas/overlay = local; alertas/chat = nuvem SE*.

### 2.4 Música sem copyright — decisão na fase de áudio

- **Pretzel Rocks (grátis):** app dedicado, catálogo grande, livre de DMCA; o plano free exige atribuição automática no chat (bot faz sozinho);
- **StreamBeats (grátis):** playlists prontas para streamers, sem atribuição;
- Ambos atendem; escolhemos junto com a configuração de áudio.

### 2.5 Áudio

Cadeia profissional com filtros nativos do OBS + ReaPlugs (suite VST gratuita): Supressão de Ruído (RNNoise) → Noise Gate → EQ (ReaEQ) → Compressor (RCC). Detalhado na fase de áudio, após informar o modelo do microfone.

### 2.6 Testes e QA

- **Twitch Inspector** — valida bitrate/queda de frames em transmissões de teste;
- **Gravação local no OBS** — valida layout/alertas/áudio sem ir ao ar;
- Checklist final da Etapa 8 consolida tudo.

---

## 3. Arquitetura da transmissão

```
                        ┌──────────────────────────────────┐
                        │           OBS STUDIO             │
                        │  Cenas: Starting│Gameplay│JC│BRB│End
                        │  ┌────────────────────────────┐  │
   Arquivos locais ────►│  │ Browser Sources            │  │
   (eu entrego):        │  │ • telas HTML (local)       │  │
   • telas animadas     │  │ • overlay HTML (local)     │  │
   • overlay gameplay   │  │ • alertas SE (nuvem) ◄─────┼──┼── StreamElements
   • stinger WebM       │  │ • chat SE (nuvem)   ◄─────┼──┼── (alertas/chat/tips)
                        │  └────────────────────────────┘  │
                        │  Áudio: mic (filtros)│jogo│música│
                        └──────────────┬───────────────────┘
                                       │ RTMP
                                       ▼
                              TWITCH.TV/exoriservice
                                       ▲
                       Nightbot (nuvem)│comandos, timers, moderação
                       Música DMCA-safe│Pretzel/StreamBeats
```

---

## 4. Cronograma do projeto a partir daqui

| Fase | Entrega | Depende de |
|---|---|---|
| 3 | Conceitos de logo (dragão geométrico) + wordmark — sua escolha | Sua aprovação da stack |
| 4 | Todas as artes: telas, overlay, avatar, banner, painéis, alertas | Logo aprovado |
| 5 | Estrutura profissional do OBS (cenas, fontes, áudio, hotkeys, transições) | ✅ `obs/exoriservice-cenas.json` + `05-obs-guia.md` | — |
| 6 | Nightbot: comandos, timers, moderação (config pronta para copiar) | ✅ `06-nightbot-guia.md` + `nightbot/` | — |
| 7 | Painéis + integrações (links, SE, doações) | ✅ `07-integracoes-guia.md` + `integracoes/` | — |
| 8 | Checklist final + testes (ensaio geral + go-live) | ✅ `08-guia-master-implementacao.md` | Tudo acima |

---

*Stack definida. Próximo passo: conceitos de logo para o **exoriservice**.*
