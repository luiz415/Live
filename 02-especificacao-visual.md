# 🐉 Especificação Visual & Técnica — Projeto de Profissionalização do Canal
**Documento-base de todas as criações. Versão 1.0 — gerada após Levantamento de Requisitos.**

---

## 1. Perfil do Canal

| Item | Decisão |
|---|---|
| Conteúdo | Somente jogos — categoria fixa |
| Gênero predominante | RPG / Narrativo / Mundo aberto |
| Webcam | **Não utiliza** |
| Vibe da transmissão | Chill / Relaxada |
| Direção visual | E-sports / Competitivo |
| Nome do canal | **exoriservice** |
| Agenda das lives | Segunda a sábado, 08h–22h (domingo sem live) |
| Idioma | PT-BR |
| Resolução | 1080p @ 60fps (canvas 1920×1080) |
| Cenas OBS | Gameplay + Starting Soon + BRB + Encerramento + Just Chatting |
| Orçamento ferramentas | **Somente gratuito** |
| Links | ⚠️ Enviar depois (placeholders até lá) |

**Conceito criativo:** *agressividade geométrica de e-sports sobre um fundo profundo e calmo* — a identidade "grita" nas arestas e no verde ácido, mas o clima permanece relaxado pelo preto dominante e pelo respiro visual.

---

## 2. Paleta de Cores (oficial)

| Função | Cor | HEX |
|---|---|---|
| Base — fundo profundo | Preto carbono | `#060806` |
| Superfície — painéis/caixas | Grafite esverdeado | `#121712` |
| Superfície elevada | Grafite claro | `#1C241C` |
| **Acento primário** | **Verde ácido** | **`#B4FF00`** |
| Acento secundário (glow/sombra) | Verde tóxico escuro | `#5C9900` |
| Verde profundo (detalhes/fundos de ícone) | Verde floresta escuro | `#173300` |
| Texto principal | Branco esverdeado | `#F2FFE8` |
| Texto secundário | Cinza claro | `#9AA69A` |

**Regras de uso:**
- Verde ácido é cor de **destaque** (bordas, ícones, números, CTAs) — nunca de fundo grande (queima os olhos e cansa);
- Gradiente assinatura: `#B4FF00 → #5C9900` em linhas e barra de progresso;
- Glow padrão: verde ácido a 30–40% de opacidade, desfoque ~8px;
- Contraste mínimo de texto: 4.5:1 (legibilidade em compressão de stream).

---

## 3. Tipografia (100% gratuitas — Google Fonts)

| Uso | Fonte | Peso | Observação |
|---|---|---|---|
| Display / Títulos / Logo assist | **Orbitron** | 700–900 | Futurista, geométrica, caixa alta |
| Labels / Subtítulos / Números | **Chakra Petch** | 500–700 | Techy, condicionada, ótima legibilidade |
| Corpo / Chat / Textos longos | **Exo 2** | 400–600 | Techy neutra, confortável |

**Regras:** títulos em CAIXA ALTA com espaçamento +2–6%; números de contagem em Orbitron; PT-BR com acentos ok em todas.

---

## 4. Logo — ✅ OFICIAL (aprovado em etapa 3)

| Item | Decisão |
|---|---|
| Conceito | **HEX STRIKE** (variação C1) — cabeça de dragão agressiva em facetas poligonais dentro de badge hexagonal |
| Tratamento | Facetas grafite fosco + filetes e brilho em verde ácido; fundo do emblema já escuro (integra com overlays) |
| Arquivos finais | `twitch-pro/logos/final/`: avatar-800, icone-512/256/128/64/24, lockup-horizontal, lockup-vertical, logo-mono-branco, logo-mono-preto |
| Wordmark | "EXORI" (verde ácido) + "SERVICE" (branco), Orbitron 900, tracking ~7 |

**Regras de texto (v2):** o dragão existe **somente na logo** — nenhum texto do canal o menciona; telas de cena **não exibem comandos** (eles vivem no overlay de gameplay e no bot); textos mínimos e limpos em todas as telas.

**Regras de uso:** área de proteção = 8% do tamanho do logo ao redor; nunca distorcer; sobre fundos claros usar versão mono preta; versão mínima 24px (usar icone-24).

**Wordmark:** nome do canal em Orbitron Black, caixa alta, com corte angular assinatura (notch) em uma letra + detalhe verde ácido. ⚠️ *Aguardando o nome exato do canal.*

---

## 5. Linguagem Visual (elementos recorrentes em TODAS as peças)

- **Shards:** fragmentos/polígonos angulares verdes saindo das bordas;
- **Notch cut:** cantos "cortados" em 45° (chamfer) em caixas, frames e painéis — nunca cantos arredondados;
- **Grid tech:** malha hexagonal sutil de fundo (opacidade 4–8%);
- **Scanline/digital:** linha fina verde varrendo em animações;
- **Barra de energia:** linha horizontal gradiente `#B4FF00 → #5C9900` como divisor;
- **Número/destaque:** sempre Orbitron verde ácido;
- **Moldura fina (padrão v3):** filete verde ácido de 1–2px contornando a borda de **todas** as exibições de cena (telas, overlay, widgets, slides do carrossel, BG Just Chatting, offline e fallbacks).

---

## 6. Especificação das Peças (dimensões oficiais)

| Peça | Dimensão | Status |
|---|---|---|
| Avatar Twitch (800×800) | ✅ `logos/final/avatar-800.png` | Etapa 3 |
| Overlay Gameplay HTML + PNG fallback | 1920×1080 | ✅ `assets/overlay/` |
| **Party Tracker Tibia** (compacto, editável ao vivo) | 1920×1080 | ✅ `assets/overlay/party-tracker.html` |
| **Carrossel de Serviços** (4 slides automáticos) | 440×240 widget | ✅ `assets/overlay/carrossel-servicos.html` + slides em `assets/carrossel/` |
| BG de Just Chatting | 1920×1080 | ✅ `assets/extras/justchatting-1920x1080.png` |
| Tela Starting Soon (HTML animado + PNG) | 1920×1080 | ✅ `assets/telas/` |
| Tela BRB (HTML animado + PNG) | 1920×1080 | ✅ `assets/telas/` |
| Tela Encerramento (HTML animado + PNG) | 1920×1080 | ✅ `assets/telas/` |
| Banner do perfil | 1920×480 | ✅ `assets/extras/` |
| Painéis do perfil (8× 320×160) | PNG | ✅ `assets/paineis/` |
| Alertas (banner médio) | HTML | ✅ `assets/alertas/` (7 tipos + SFX) |
| Stinger de transição (WebM alfa) | 1920×1080 | ✅ `assets/stinger/stinger-transicao.webm` |
| Offline screen | 1920×1080 | ✅ `assets/extras/` |
| Mini-marca (watermark) | 256/96/72/24 | ✅ `logos/final/` |

---

## 7. Layout do Overlay de Gameplay (sem webcam) — v2 FAIXA INFERIOR

**Regra v2:** todos os elementos na **parte inferior** da tela; topo e centro 100% livres para o jogo:

```
┌──────────────────────────────────────────────────┐
│              ( GAMEPLAY LIVRE )                   │
│                                                    │
│ [🦬 marca EXORI]  [PARTY: 5 células]  [📣 SERVIÇOS]│ ← faixa inferior (acima do ticker)
│ ═════════════ ticker: !service !site !horario ═══│ ← borda inferior
└──────────────────────────────────────────────────┘
```
- **Canto inferior esquerdo:** moldura da marca (logo + EXORISERVICE · TIBIA (RUBINOT));
- **Rodapé central:** Party Tracker horizontal compacto (5 vocações + LV);
- **Canto inferior direito:** Carrossel de Serviços (4 slides automáticos);
- **Borda inferior:** ticker rotulado **COMANDOS** com os 5 comandos + anúncios (Soul War/Sanguine · Rubini Coins · Intermédio · RubinOT).

---

## 8. Alertas e Animações

| Item | Decisão |
|---|---|
| Estilo | **Banner médio uniforme** para todos os eventos (follow, sub, gift, bits, raid, doação) |
| Visual | Caixa com notch cut, borda verde ácido, glow, ícone do dragão, nome do espectador em Chakra Petch |
| Duração | ~6s por alerta + fila |
| Animação geral | **Agressiva v3** — tudo da v2 + chuva digital de glifos (canvas), rasgos VHS, strobe aleatório, 3º anel hexagonal girando, aberração cromática permanente no emblema, régua de ticks nas bordas, fissura de voltagem nas barras, split RGB no tick da contagem, shake + aceleração geral na ignição |
| Party Tracker | Quadro Tibia **horizontal compacto** (rodapé central), 5 células (vocação 2 letras + LV), editável ao vivo via Interagir do OBS, persistência automática, flash ao editar |
| Carrossel de Serviços | Canto inferior direito, 4 slides (Rubini Coins 1k=R$90 · **Intermédio** apenas de itens\* · Service com **Soul War / Sanguine (em breve)** + !service · **RubinOT com logo dark oficial**), ciclo automático de 28s, selo "SERVIÇOS", varredura e barra de progresso |
| Stinger de transição | ~0,5–1s, wipe de shards verdes |

---

## 9. Bot, Comandos e Moderação (detalhado na fase de ferramentas)

- Solução a recomendar sob restrição **100% gratuita**;
- Comandos oficiais (v4 — 8): `!service` `!coins` `!intermedio` `!wpp` `!horario` `!regras` `!setup` `!site`;
- Mensagens automáticas periódicas (services 20 min · coins 35 min · agenda 55 min);
- Moderação padrão profissional (anti-spam, links controlados, filtro de palavras).

---

## 10. ⚠️ Pendências (bloqueantes e não-bloqueantes)

| # | Item | Status | Bloqueia |
|---|---|---|---|
| 1 | Nome do canal | ✅ **Definido: exoriservice** | — |
| 2 | URLs dos links (site, discord, instagram…) | 🟡 Depois (uso placeholders) | Comandos finais, painéis de links |
| 3 | Horários das lives | ✅ **Definido: Seg–Sáb, 08h–22h** | — |
| 4 | Música nas telas de espera | 🟡 Default: sim, ambiente livre de copyright | Telas animadas |
| 5 | Modelo do microfone | 🟡 Coletar na fase de áudio | Filtros de voz |
| 6 | Monitor único ou duplo | 🟡 Coletar na fase OBS | Hotkeys |
| 7 | Jogo principal da categoria fixa | ✅ **Tibia (servidor RubinOT)** | Layout do overlay preservará a interface do cliente Tibia |

---

*Próximas etapas: **2) Escolha de ferramentas** → **3) Logo + validação da identidade** → produção das artes → OBS → bot → painéis → checklist final.*
