# 🚀 GUIA MASTER — Implementação Completa do Canal exoriservice
> **O que é:** o passo a passo definitivo, em ordem correta de execução, de TUDO que construímos.
> **Tempo total:** ~1h45 de configuração única + 1 ensaio geral (~40 min) + rotinas diárias de 10 min.
> **Como usar:** execute as fases na ordem. Cada fase tem pré-requisitos, passos e um ✅ de conclusão.
> Documentos de apoio detalhados: `05-obs-guia.md`, `06-nightbot-guia.md`, `07-integracoes-guia.md`, `assets/LEIA-ME.md`, `assets/alertas/COMO-INSTALAR.md`.

---

## 📋 VISÃO GERAL — as 8 fases

| Fase | O quê | Tempo | Depende de |
|---|---|---|---|
| 0 | Baixar e organizar os arquivos no PC | 10 min | — |
| 1 | Identidade visual no perfil da Twitch | 10 min | 0 |
| 2 | StreamElements (alertas, chat, doação) | 15 min | conta Twitch |
| 3 | Nightbot (comandos, timers, moderação) | 15 min | conta Twitch |
| 4 | OBS (importar cenas, ajustes, áudio, hotkeys) | 25 min | 0 e 2 |
| 5 | Painéis do perfil | 10 min | 0 |
| 6 | Ensaio geral (gravação + live de teste) | 40 min | 1–5 |
| 7 | PRIMEIRA LIVE 🎉 | 10 min de prep | 6 |
| 8 | Rotinas e manutenção | contínuo | — |

---

# FASE 0 · Baixar e organizar os arquivos (10 min)

1. Baixe do workspace a pasta **`twitch-pro/`** inteira para o PC;
2. No disco `C:`, crie a estrutura e copie assim:
```
C:\twitch\exoriservice\
├── assets\        ← conteúdo de twitch-pro\assets\
│   ├── telas\         (starting-soon.html, brb.html, encerramento.html + fallbacks)
│   ├── overlay\       (overlay-gameplay.html, party-tracker.html + fallback)
│   ├── alertas\       (preview + streamelements\ + sfx\)
│   ├── paineis\       (8 painéis PNG)
│   ├── extras\        (banner-perfil, offline)
│   └── stinger\       (stinger-transicao.webm)
└── logos\         ← conteúdo de twitch-pro\logos\final\
```
3. Confira que `C:\twitch\exoriservice\assets\stinger\stinger-transicao.webm` existe (o OBS vai apontar para ele).

✅ **Concluído quando:** a árvore acima existe no seu disco.

# FASE 1 · Identidade no perfil da Twitch (10 min)

1. **Painel do Criador:** `dash.twitch.tv` (ou avatar → Painel do Criador) → **Configurações → Canal** → aba **MARCA**:
   - Imagem de perfil → `logos\avatar-800.png`
   - Imagem de capa do perfil → `assets\extras\banner-perfil-1920x480.png`
   - **Banner do player de vídeo** (aparece offline) → `assets\extras\offline-1920x1080.png`
   - *Atalho alternativo para avatar/capa:* `twitch.tv/settings/profile`
2. Ainda em Configurações → Canal → aba **INFORMAÇÕES**: preencha a bio (2–3 linhas: Tibia/RubinOT + agenda) e as **redes sociais** nos campos de links sociais quando tiver;
3. Na próxima live: **categoria Tibia** + tags `Português`, `Chill`, `RPG`, `MMORPG`;
4. Título sugerido para a estreia: `⚔️ HUNT DIÁRIA NO RUBINOT — seg a sáb · 08h às 22h`.

✅ Avatar + 2 banners aplicados e categoria definida.

# FASE 2 · StreamElements (15 min)

1. `streamelements.com` → **Sign in with Twitch** (conta exoriservice) → autorizar;
2. **Overlays → + New Overlay** → nome `exoriservice-alerts` → **+ → Alert Box**;
3. Configure os 7 alertas pelo **fluxo v2** (editor atual do SE — detalhe passo a passo em `assets/alertas/COMO-INSTALAR.md`):
   - Na aba de cada tipo (FOLLOWER, SUBSCRIBER, RESUB, GIFT, CHEER, RAID, TIP): **Sound** → upload do **MP3** (`assets\alertas\sfx-mp3\sfx-TIPO.mp3` — o SE não aceita WAV) · **duração 6s**;
   - Rodapé da aba → **Enable custom CSS** → **Open Editor** → aba **HTML**: apagar padrão e colar `streamelements\v2\1-ABA-HTML_TIPO.txt` → aba **CSS**: colar `streamelements\v2\2-ABA-CSS_geral-para-todos.txt`;
   - O alerta só aparece com **evento de teste** (botão Test do editor);
4. Copie a **URL do overlay** → **guarde: é a URL-1**;
5. **Chat em cena (Just Chatting):** crie um overlay **separado** chamado `exoriservice-chat` → no editor, **+ (Adicionar Widget) → Stream Tools → "Your Stream's Chat"** → estique o widget para ocupar o canvas inteiro → personalize (tema Custom, fundo transparente, mensagem delay 0) → **Salvar** → copie a URL pelo **ícone de link (canto superior direito)** → cole na fonte **💬 CHAT** do OBS (560×920). ⚠️ Essa URL contém token — não divulgue;
6. **Tip Page**: ativar → conectar **PayPal** → personalizar com o avatar → URL pública: `streamelements.com/exoriservice/tip`;
7. Clique nos botões **Test** (follow/sub/raid) no editor para ver os alertas funcionando.

✅ URL-1 (alertas) e URL-2 (chat) anotadas + Tip Page ativa.

# FASE 3 · Nightbot (15 min)

1. `nightbot.tv` → entrar com Twitch → **Join Channel**;
2. No seu chat: `/mod nightbot` → teste `!uptime`;
3. Cole **uma a uma** as linhas de `nightbot\comandos-chat.txt` — **8 comandos oficiais**: `!service` (services + cadastro), `!coins` (Rubini Coins 1k = R$ 90), `!intermedio` (intermédio de itens), `!wpp` (WhatsApp comercial via wa.me — **número dedicado, nunca o pessoal**), `!horario`, `!regras`, `!setup`, `!site`. *(Se criou comandos de versões anteriores, use as linhas de limpeza do próprio arquivo para removê-los;)*
4. **Timers** (dashboard → Timers): crie `service` **20 min** · `coins` **35 min** · `agenda` **55 min** — os três ativos;
5. **Spam Protection**: ative os filtros com os valores da tabela do `06-nightbot-guia.md` §4 (Links 600s, Caps 50%/10s, Emotes 15/10s, Mensagens 15-per-30s/600s…);
6. **AutoMod da Twitch** (Config. do criador → Moderação): nível **2** + filtros de palavrão/discriminação/hostilidade.

✅ `!uptime` responde, comandos funcionam, filtros ativos.

# FASE 4 · OBS — montagem profissional (25 min)

1. Feche o OBS. Abra o OBS → **Coleção de cenas → Importar** → `obs\exoriservice-cenas.json` → importar → ativar a coleção **EXORISERVICE**;
   > 💡 **Já havia importado uma versão anterior?** A coleção atual (v8 — 6 cenas · 22 fontes · 34 itens) trouxe: música removida, **cena 06 · TELA**, **Ticker em todas as cenas** (y=1008), **Moldura · Just Chatting**, **Carrossel em todas as cenas**, miniatura do jogo acima do ticker (y=738) e **🎮 Captura do Tibia presente e VISÍVEL no fundo de TODAS as cenas** (estratégia anti-bug do hook: nunca ocultar — a cena cobre; ver seção 9 do guia do OBS). Importar do zero é o mais rápido — ou replique os ajustes manuais das seções anteriores;
2. **Os 3 ajustes ⚠️** (clique direito na fonte → Propriedades):
   - 🔔 ALERTAS → cole a **URL-1** (Fase 2);
   - 💬 CHAT → cole a **URL-2**;
   - 🎮 CAPTURA · Tibia → modo Janela → selecione a janela do **RubinOT**;
   - *(na cena 06 · TELA: 🖥 CAPTURA · Monitor → selecione o monitor)*
   > Música: removida do overlay por decisão do streamer — se quiser música nas telas, use um player fora do OBS (o som entra pelo "Áudio da área de trabalho", com volume baixo).
3. **Filtros do microfone** (direito no mic → Filtros, nesta ordem):
   - Supressão de Ruído: **RNNoise**
   - Portão de Ruído: abrir **–32 dB** / fechar **–40 dB** / espera 150 ms / liberação 250 ms
   - Compressor: **4:1**, limiar **–18 dB**, ataque 6 ms, liberação 250 ms, saída +2 dB
   - Limitador: **–3 dB**
4. **Níveis do mixer** (falando/jogando): mic pico **–12 a –6 dB** · alertas –16 · jogo –20 · música –25;
5. **Hotkeys** (Configurações → Atalhos): `Ctrl+1..5` cenas · `Ctrl+M` mudo · `Ctrl+P` Party Tracker · `Ctrl+Shift+T` live;
6. Confira as 5 cenas: **01 STARTING · 02 GAMEPLAY · 03 JUST CHATTING · 04 BRB · 05 ENCERRAMENTO** — transição padrão **⚡ STINGER EXORI** já ativa.

✅ Coleção ativa, 4 ajustes feitos, filtros e hotkeys configurados.

# FASE 5 · Painéis do perfil (10 min)

> ⚠️ **Onde NÃO procurar:** os painéis **não** ficam no Painel do Criador (Configurações do criador) nem no app móvel. É na **página do seu canal**, aba **Sobre**, e somente no **navegador do computador** (no celular, só via navegador pedindo "site do desktop").

1. No computador, acesse `twitch.tv` logado → clique no seu **avatar (canto superior direito) → Canal** (ou digite `twitch.tv/exoriservice`);
2. Na página do canal, clique na aba **SOBRE** (logo abaixo do nome do canal, ao lado de Vídeos/Clipes);
3. Role até o **final da seção Sobre** → ative o interruptor **"Editar painéis"** — o canal entra em modo de edição e aparece um botão grande **+**;
4. Clique no **+** para criar um painel. No formulário:
   - **Imagem:** adicionar/enviar o `assets\paineis\painel-*.png` do painel correspondente;
   - **Título:** como em `integracoes\textos-paineis.md`;
   - **Descrição:** cole o texto pronto do documento;
   - **Link (URL):** quando o painel tiver link (Apoie → `https://streamelements.com/exoriservice/tip`; Discord/Redes → quando tiver os links);
5. Clique **Enviar/Salvar**;
6. Repita para os **8 painéis** (ordem sugerida: Sobre → Horários → Discord → Apoie → Redes → Comandos → Regras → Setup);
7. Reordene **arrastando** os painéis;
8. Desative **"Editar painéis"** para ver o resultado como o espectador vê.

✅ 8 painéis publicados na ordem certa (confira com o interruptor desligado).

# FASE 6 · ENSAIO GERAL (40 min) — não pule esta fase!

### 6.1 Gravação local (10 min)
1. OBS → **Iniciar Gravação**;
2. Percorra: cena 01 (deixe a contagem correr 1 min) → 02 (jogue 3 min de RubinOT; edite o Party Tracker via **Interagir**: EK 250, ED 180…) → 03 (escreva no chat p/ ver o widget) → 04 → 05;
3. Pare a gravação e **assista com atenção**: stinger nas trocas? contagem reiniciou? overlay não cobre HUD do Tibia? party tracker no lugar? áudios equilibrados?

### 6.2 Ajustes finos com o jogo aberto
- Se o ticker do overlay cobrir algo importante do cliente do Tibia: edite `overlay-gameplay.html` → `CFG.posicao:"base"`;
- Mova/redimensione o Party Tracker se necessário (destrave a fonte, ajuste, torne a travar).

### 6.3 Live de teste (15 min)
1. Twitch → **inspector.twitch.tv** → iniciar sessão;
2. OBS → **Iniciar Transmissão** (o Inspector detecta a sessão de teste);
3. Verifique: **bitrate estável, 0% perda de frames, sem quadros renderizados a menos**;
4. Durante o teste: dispare **Test Raid** no SE (vê o alerta na live real), peça a alguém p/ digitar `!social` e postar um link sem permissão (vê o Nightbot agir);
5. Encerre a transmissão.

### 6.4 Checklist de aprovação
- [ ] Gravação revisada sem problemas visuais/áudio
- [ ] Inspector limpo (sem perda de frames por rede)
- [ ] Alerta de teste apareceu na live real
- [ ] Party Tracker editado ao vivo e persistiu após reiniciar o OBS
- [ ] Nightbot respondeu e moderou o link

# FASE 7 · PRIMEIRA LIVE 🎉 (prep de 10 min)

**Rotina de estreia (dia seguinte ao ensaio):**
1. **07h50** — abra OBS + RubinOT + Nightbot dashboard; tome café ☕;
2. **07h55** — confira: cena 01 selecionada · mic no nível · `Ctrl+Shift+T` para IR AO AR;
3. **08h00–08h10** — cena Starting com contagem; interaja: "bom dia, chegando";
4. **08h10** — `Ctrl+2` → GAMEPLAY. Diga os comandos em voz alta: "rede no !social, regras no !regras";
5. Durante o dia — siga o `nightbot\cheatsheet-ao-vivo.md` (pausas a cada 3h, almoço 12h, encerramento 21h50);
6. **21h58** — `Ctrl+5` → Encerramento; agradeça por nome quem apareceu;
7. **22h05** — encerre a transmissão. **Nunca** deixe a tela de encerramento rodando por horas.

# FASE 8 · Rotinas e manutenção (contínuo)

**Diária (10 min):** ligar OBS → conferir cenas/níveis → título e categoria atualizados → ao final, encerrar corretamente.

**Semanal (30 min, sugestão: domingo):**
- Revisar clipes/vods da semana (reciclar melhores momentos nas redes);
- Checar `links-master.md`: links pendentes a registrar?
- Limpar blacklist do Nightbot (ajustar ao comportamento real do chat);
- Ativar timers `discord`/`apoio` quando o chat engatar;
- Atualizar painel de Setup quando mudar hardware.

**Quando os links chegarem (5 min cada):** siga a **Rotina de substituição** do `integracoes/links-master.md` (comando + timer + painel + ticker) e me avise no projeto para eu regenerar artes/textos dependentes.

---

## 🔧 DEU ALGO ERRADO? (respostas rápidas)

| Problema | Causa provável | Solução |
|---|---|---|
| Tela/navegador preto no OBS | caminho do arquivo errado | Propriedades da fonte → reverificar arquivo local (estrutura da Fase 0) |
| Alertas não aparecem | URL-1 errada ou SE desconectado | Regenere a URL no SE; confira se o overlay está salvo |
| Stinger sem som | **limitação do OBS** (documentado) | Normal — whoosh opcional via fonte de mídia + hotkey |
| Party Tracker não salva | editou fora do modo Interagir | Direito na fonte → Interagir → EDITAR |
| Contagem não reinicia | faltou "atualizar quando ativa" | Já vem ativo; senão, propriedades da fonte → marcar |
| Live com quadros caindo | internet/encoder | Inspector p/ diagnosticar; baixe o bitrate antes de mexer em resolução |
| Nightbot calado | perdeu o mod | `/mod nightbot` de novo |
| Não acho "Editar painéis" | está no lugar errado | Página do **canal** (não no Painel do Criador) → aba **Sobre** → rodapé → interruptor **Editar painéis** — só no navegador desktop |
| Voz sibilando/sopando | mic alto do demais | Ganho down, fale a ~10 cm, aumente a liberação do gate |

---

## ✅ CHECKLIST FINAL DE GO-LIVE

- [ ] Fase 0 — arquivos em `C:\twitch\exoriservice`
- [ ] Fase 1 — avatar, banner e banner offline no perfil
- [ ] Fase 2 — alertas + chat + Tip Page (URL-1 e URL-2 usadas)
- [ ] Fase 3 — Nightbot moder + 11 comandos + timers + filtros
- [ ] Fase 4 — coleção OBS importada + 4 ajustes + filtros de áudio + hotkeys
- [ ] Fase 5 — 8 painéis publicados
- [ ] Fase 6 — gravação revisada + Inspector limpo + alertas testados ao vivo
- [ ] Fase 7 — primeira live executada com a rotina
- [ ] Fase 8 — rotinas agendadas (diária + semanal)

**Canal profissional completo: identidade própria, telas cinematográficas, overlay ao vivo, alertas exclusivos, bot configurado, moderação em duas camadas e uma operação de transmissão padronizada. Bora brilhar — ao ar! 🐉⚡**
