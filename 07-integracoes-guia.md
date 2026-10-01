# 🔗 Etapa 7 — Painéis + Integrações: Guia Completo
**Entregáveis:** este guia + `integracoes/links-master.md` (registro de links) + `integracoes/textos-paineis.md` (textos prontos dos painéis).
**Tempo total estimado: 35 minutos.**

---

## 1. StreamElements — conexão completa (10 min)

> Conta: `streamelements.com` → **Sign in with Twitch** → autorizar como `exoriservice`. Grátis, sem cartão.

### 1.1 Overlay de alertas (alimenta a fonte 🔔 do OBS)
1. **Dashboard → Streaming Tools → Overlays → + New Overlay** → nome `exoriservice-alerts`;
2. **+** → **Alert Box** → siga `assets/alertas/COMO-INSTALAR.md` (colar os 7 HTMLs + sons + duração 6s);
3. Copie a **URL do overlay** (botão no topo) → OBS → propriedades da fonte **🔔 ALERTAS · StreamElements** → cole (resolve o ⚠️ #1 da Etapa 5);
4. **Teste** com os botões *Test Follow / Test Sub / Test Raid* do editor.

### 1.2 Widget de chat (alimenta a fonte 💬 do OBS)
1. Crie um overlay **separado**: **+ New Overlay** → nome `exoriservice-chat` (1080p);
2. No editor: **+ (Adicionar Widget) → Stream Tools → "Your Stream's Chat"**;
3. Estique o widget para ocupar o **canvas inteiro** (ele preenche a fonte do OBS);
4. Configurações sugeridas: **Theme: Custom** · **Show Messages ✅** · **Message Delay: 0** · fundo **transparente** · fonte ~20–22px branca;
5. **Salvar** → copie a URL pelo **ícone de link no canto superior direito** do editor;
6. OBS → propriedades da fonte **💬 CHAT · StreamElements** → cole a URL (resolve o ⚠️ #2);
7. Posicione na cena 03 (Just Chatting) — a coleção importada já deixa no lugar (560×920).
> ⚠️ A URL do overlay contém um token privado — não compartilhe publicamente.
> 💡 O chat só renderiza mensagens quando alguém escrever — teste digitando no seu próprio chat.

### 1.3 Página de doação (Tip Page)
1. **Dashboard → Tip Page** → ative;
2. Personalize: título **Apoie o exoriservice**, descrição curta, e envie o `logos/final/avatar-800.png` como imagem;
3. **Settings → Payment** → conecte sua conta **PayPal** (é onde o dinheiro cai; o SE não cobra taxa além do PayPal);
4. Sua URL pública: `https://streamelements.com/exoriservice/tip` → já vai no painel Apoie, no `!apoiar` e no timer `apoio`;
5. Teste com uma doação mínima de R$ 1 feita por você (ou peça a alguém) — valida PayPal + alerta de doação de ponta a ponta.

## 2. Perfil da Twitch — identidade completa (15 min)

### 2.1 Imagens
| Item | Arquivo | Onde subir |
|---|---|---|
| Avatar | `logos/final/avatar-800.png` | Twitch → Config. do criador → Marca/Perfil → Imagem do perfil |
| Banner do canal | `assets/extras/banner-perfil-1920x480.png` | Marca → Imagem de capa do perfil |
| Banner do player (aparece offline) | `assets/extras/offline-1920x1080.png` | Marca → **Banner do player de vídeo** (1920×1080) |

### 2.2 Painéis (8)
Use `integracoes/textos-paineis.md`: cada painel = **imagem** (`assets/paineis/`) + título + texto colado + link quando houver. Ordem final: **Sobre → Horários → Discord → Apoie → Redes → Comandos → Regras → Setup**.

### 2.3 Informações do canal
- **Categoria principal:** Tibia (fixa o reconhecimento do canal pela categoria);
- **Tags sugeridas:** `Português`, `Chill`, `RPG`, `MMORPG`, `Jogando com os espectadores` (ajusta às disponíveis no dia);
- **Títulos de live — 3 modelos prontos:**
  1. `⚔️ HUNT DIÁRIA NO RUBINOT — seg a sáb · 08h às 22h`
  2. `🏰 [NOME DA HUNT/QUEST] — Tibia · RubinOT com o chat`
  3. `☕ LIVE CHILL DE TIBIA — pega o café e fica`
- **Recap automático:** ativa os *Clips sugeridos/Recaps* nas configurações do criador quando disponíveis para sua conta.

### 2.4 Moderação nativa da Twitch (complementa o Nightbot)
1. Config. do criador → **Moderação** → **AutoMod**: nível **Médio (2)**;
2. Ative: **Filtro de palavrões**, **Filtro de discriminação**, **Filtro de hostilidade** — mantendo o nível médio para não bloquear zoeira leve da comunidade;
3. Chat → **Exigir e-mail verificado** para comentar: ative **apenas se** aparecerem contas-troll anônimas (barreira de entrada para novos espectadores legítimos);
4. Adicione 1–2 mods humanos de confiança quando a comunidade crescer (comece sozinho: Nightbot + AutoMod dão conta).

## 3. Links — preenchendo os placeholders (5 min quando tiver os links)

1. Abra `integracoes/links-master.md` → registre cada URL real;
2. Siga a **Rotina de substituição** (seção 3 do documento): comandos `!commands edit`, timers no dashboard, `CFG.itens` do ticker, links nos painéis;
3. **Me envie os links no chat do projeto** — eu regenero qualquer arte/texto dependente e confirmo a consistência.

*Até lá, tudo funciona com os placeholders atuais (teleias, comandos e ticker já avisam "em breve" com elegância).*

## 4. Ciclo integrado de divulgação (como tudo se conecta)

```
TELA STARTING ─► marca + agenda (sem links — visual limpo)
OVERLAY TICKER ─► comandos girando o tempo todo durante o jogo
CHAT: COMANDOS ─► viewer pergunta → bot responde na hora (11 comandos)
CHAT: TIMERS ───► divulgação passiva a cada 20–55 min
PAINÉIS ────────► quem curtiu o canal clica direto (link permanente)
ALERTA DE DOAÇÃO ► fortalece o ciclo de apoio
```

**Regra de consistência:** um link novo nasce sempre em **3 lugares** (comando + painel + ticker/timer). O links-master garante que nada fique esquecido.

## 5. Testes da etapa (5 min)

- [ ] Alerta de teste aparece no OBS (fonte 🔔) com animação e som
- [ ] Chat do SE visível na cena 03 escrevendo no chat
- [ ] Tip Page abre publicamente e doação de teste dispara alerta
- [ ] Avatar + banner + banner do player aplicados
- [ ] 8 painéis no ar na ordem sugerida, com textos e links
- [ ] Categoria Tibia + tags aplicadas
- [ ] AutoMod nível 2 + filtros ativos
- [ ] links-master.md atualizado com tudo que existir até agora

---

*Próxima etapa — 8 · **Checklist final + Testes**: ensaio geral completo (gravação, transmissão de teste no Inspector, simulação de live inteira) e o checklist de go-live.*
