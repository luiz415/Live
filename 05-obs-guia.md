# 🛠 Etapa 5 — Estrutura Profissional do OBS
**Entregáveis:** `obs/exoriservice-cenas.json` (coleção de cenas pronta) + este guia.

---

## 1. Preparar a pasta dos arquivos (1×, 2 minutos)

O OBS precisa dos arquivos em um caminho fixo. No Windows, crie a pasta e copie o conteúdo do projeto:

```
C:\twitch\exoriservice\
├── assets\   (telas, overlay, alertas, painéis, stinger…)
└── logos\    (logo oficial e derivações)
```

> Usa Linux/macOS ou quer outro caminho? Tudo bem — após importar, ajuste o caminho em **4 fontes** (propriedades → selecionar arquivo de novo). A URL da tela Starting é `file:///C:/twitch/exoriservice/assets/telas/starting-soon.html?t=10` — edite se mudar o caminho.

## 2. Importar a coleção de cenas (1 minuto)

1. OBS → menu **Coleção de cenas → Importar** → selecione `exoriservice-cenas.json` → **Importar**;
2. Depois: **Coleção de cenas → EXORISERVICE** para ativá-la;
3. Você verá as 5 cenas no painel de cenas:

| # | Cena | Uso |
|---|---|---|
| 01 | STARTING | Abertura da live (contagem 10 min, reinicia a cada ativação) |
| 02 | GAMEPLAY | Tibia + overlay + party tracker + alertas |
| 03 | JUST CHATTING | Conversa: arte de fundo + chat do SE (captura do Tibia já inclusa, **invisível** — ative se quiser conversar "in-game") |
| 04 | BRB | Pausas + música |
| 05 | ENCERRAMENTO | Despedida + música |

A transição **⚡ STINGER EXORI** já vem configurada como padrão (stinger WebM, ponto de transição 50%).

## 3. Os 4 ajustes ⚠️ (obrigatórios, 5 minutos)

As fontes marcadas com ⚠️ são placeholders — é só clicar com o direito → **Propriedades**:

1. **🔔 ALERTAS · StreamElements** → cole a URL do seu overlay de alertas do SE (Dashboard → Overlays → ⚙️ → copiar URL). Use a URL `/embed/overlay/...` completa;
2. **💬 CHAT · StreamElements** → crie um widget **Chat** no mesmo overlay do SE (ou separado) → Properties → copiar a URL do chat;
3. **🎮 CAPTURA · Tibia** → modo Janela → selecione a janela do cliente **RubinOT** na lista;
4. **🎵 MÚSICA** → a coleção **não tem mais fonte de música** (v6+). Se quiser trilha, abra o player DMCA-free (ex.: Pretzel) fora do OBS — o som entra pela **captura de áudio da área de trabalho** (Spotify é proibido: DMCA).

## 4. Áudio profissional

### 4.1 Mixer — papéis e níveis

| Canal | Papel | Pico no medidor |
|---|---|---|
| 🎙 Mic | Voz | **–12 a –6 dB** |
| 🎮 Áudio da área de trabalho | Jogo (Tibia) | –20 dB |
| 🔔 Alertas (navegador) | SFX | –16 dB |
| 🎵 Música (navegador) | Música das telas | –25 dB |

> Dica pro: se o jogo tocar sempre na mesma janela, crie uma fonte **Saída de áudio de aplicativo** apontando para o cliente do Tibia e **mute** o "Áudio da área de trabalho" — assim sons do Windows/Discord nunca vazam para a live.

### 4.2 Cadeia de filtros do microfone (ordem exata)

Clique direito no mic → **Filtros** → adicione nesta ordem (valores iniciais, ajuste ao ouvir):

| # | Filtro | Configuração |
|---|---|---|
| 1 | **Supressão de Ruído** | Método: **RNNoise** (FFT alternativo se a CPU for fraca) |
| 2 | **Portão de Ruído** | Abrir: **–32 dB** · Fechar: **–40 dB** · Ataque: 3 ms · Espera: 150 ms · Liberação: 250 ms |
| 3 | **Compressor** | Proporção: **4:1** · Limiar: **–18 dB** · Ataque: 6 ms · Liberação: 250 ms · Ganho de saída: **2 dB** |
| 4 | **Limitador** | Limiar: **–3 dB** · Liberação: 60 ms |

Fale a ~10 cm do mic no tom normal de live e calibre o ganho até a voz picar entre –12 e –6 dB.

### 4.3 Níveis por fonte de navegador
Propriedades da fonte → volume: Alertas ~70% · Música ~55% (já vem pré-ajustado na coleção).

## 5. Transições

- **⚡ STINGER EXORI** (padrão): uso geral entre cenas — é a sua assinatura visual;
- **Fade 300 ms**: reserve para transições "suaves" (ex.: entrando no BRB no meio da gameplay);
- **Corte**: para cortes secos rápidos (erro recover, troca de vantage);
- Como trocar na hora: dock **Transições** → selecione a transição ativa (atalho: **T** abre a lista de forçar transição).

## 6. Hotkeys sugeridas (OBS → Configurações → Atalhos)

| Ação | Sugestão |
|---|---|
| Alternar cena → 01 STARTING | `Ctrl+1` |
| Alternar cena → 02 GAMEPLAY | `Ctrl+2` |
| Alternar cena → 03 JUST CHATTING | `Ctrl+3` |
| Alternar cena → 04 BRB | `Ctrl+4` |
| Alternar cena → 05 ENCERRAMENTO | `Ctrl+5` |
| Alternar cena → 06 TELA | `Ctrl+6` |
| Silenciar microfone | `Ctrl+M` |
| Mostrar/ocultar Party Tracker | `Ctrl+P` (procure a fonte "🐺 WIDGET" na lista de fontes do atalho) |
| Iniciar/Parar transmissão | `Ctrl+Shift+T` *(cuidado: exige atenção para não encerrar sem querer)* |

> Trabalha com only 1 monitor? Priorize os atalhos de cena — com eles você nunca precisa abrir o OBS durante o jogo.

## 7. Convenções de organização (já aplicadas)

- **Fontes nomeadas por função** com emoji + categoria: `💤 TELAS`, `🕹 OVERLAY`, `🐺 WIDGET`, `🔔 ALERTAS`, `🎮 CAPTURA`, `🎵 MÚSICA`;
- **Itens travados** (🔒): elementos de layout que não devem ser arrastados por acidente (overlay, party tracker);
- **"Desligar fonte quando não visível"** ativo em todos os navegadores (economiza CPU/RAM);
- **"Atualizar navegador quando a cena ficar ativa"** na Starting (contagem sempre reinicia);
- Nenhuma fonte duplicada: alertas/captura/música são **compartilhados** entre cenas (mesma fonte, estados iguais).

## 8. Testes da etapa (15 minutos)

1. **Gravação local:** Configurações → Saída → Gravação (mesma qualidade da live) → grave 2 min trocando as 5 cenas;
2. Confira no vídeo: stinger nas trocas, contagem reiniciando, sem "buraco" preto, áudios no lugar;
3. **Party Tracker:** entre no RubinOT → cena 02 → direito na fonte → Interagir → EDITAR → preencha `EK 250` etc. → OK → reinicie o OBS e confira que persistiu;
4. **Alertas:** no dashboard do SE, dispare os botões de teste (follow/sub/raid) — animação + som + fila;
5. **Twitch Inspector** (`inspector.twitch.tv`): rode uma transmissão de teste de 5 min — sem perda de frames, bitrate estável;
6. **Níveis:** fale, jogue, dispare alerta — confira os picos da tabela 4.1.

## ✅ Checklist final da Etapa 5

- [ ] Pasta `C:\twitch\exoriservice` criada e preenchida
- [ ] Coleção importada e ativa
- [ ] URL dos alertas trocada
- [ ] URL do chat trocada
- [ ] Janela do Tibia selecionada na captura
- [ ] Trilha (opcional): player DMCA-free externo + áudio da área de trabalho
- [ ] Filtros do microfone aplicados (4 filtros, ordem certa)
- [ ] Níveis calibrados
- [ ] Hotkeys configuradas
- [ ] Gravação de teste revisada
- [ ] Inspector sem perdas

---

*Próxima etapa — 6 · **Nightbot**: comandos, timers, boas-vindas e moderação (configuração pronta para copiar/colar).*

## 9. 🔧 Problema: client do jogo não é reconhecido / captura fica preta

**Sintomas:** o OBS só reconhece o client se abrir DEPOIS do OBS; ao usar "Ocultar Fonte" → "Exibir Fonte" a captura fica preta e a janela some da lista (só volta abrindo outro client).

**Causa:** captura por *hook* (injeção) + privilégio diferente entre OBS e client. O Windows impede que um programa comum capture/liste processos com privilégio maior, e o hook "presa" (estado antigo) ao desativar/reactivar a fonte.

### Correção permanente (faça na ordem)

1. **Mesmo nível de privilégio** — o mais importante:
   - Feche tudo → botão direito no **OBS → Executar como administrador** → abra o client. Teste.
   - Para fixar: direito no atalho do OBS → **Propriedades → Compatibilidade → ✅ Executar este programa como administrador**.
   - E/ou: direito no .exe do client RubinOT → Propriedades → Compatibilidade → **❌ DESMARCAR** "Executar como administrador" (o importante é os dois no MESMO nível).
2. **Recuperar sem abrir outro client** (quando ficar preta): botão direito na fonte de captura → **Fechar Hook** → com o client aberto, reabra as Propriedades da fonte e selecione a janela de novo. Isso reinicializa a injeção.
3. **Limpar o cache do hook** (se persistir): feche o OBS (inclusive ícone da bandeja) → apague o conteúdo de `C:\ProgramData\obs-studio-hook` → abra o OBS → **recrie** a fonte de captura do zero.
4. **Alternativa mais estável (recomendada p/ testar):** fonte **Captura de Janela** → Propriedades → **Método de captura: Windows 10 (1903+)** (WGC). Esse método NÃO usa injeção — funciona independente da ordem de abertura e não quebra ao Ocultar/Exibir.
5. **Notebook com 2 placas de vídeo:** Configurações do Windows → Sistema → Tela → Gráficos → adicione `obs64.exe` e o .exe do client → ambos em **Alto desempenho** (mesma GPU).
6. **Desative overlays** que brigam com o hook: overlay do Discord, GeForce Experience/NVIDIA App, Xbox Game Bar e RTSS/MSI Afterburner.
7. **Evite Ocultar/Exibir na fonte do client** — prefira trocar de cena (a coleção já organiza isso); se precisar esconder, use o passo 2 para recuperar.

> Teste rápido após o passo 1: abra o client ANTES do OBS, aguarde logar, e veja se a janela agora aparece na lista. Se aparecer = problema de privilégio resolvido.

### ✅ ESTRATÉGIA DEFINITIVA (coleção v8): fonte SEMPRE ativa em todas as cenas

Como só a **Captura de Jogo** funciona com o client (Captura de Janela congela — normal em clientes OTClient/DX11), a regra de ouro é: **nunca ocultar a fonte**. Na coleção **v8** a 🎮 CAPTURA · Tibia está presente e VISÍVEL no **fundo** das 6 cenas — o hook fica vivo para sempre e o bug do Ocultar/Exibir desaparece. Onde o jogo não deve aparecer, a própria cena o cobre:

| Cena | Quem cobre a captura (imagem full-screen por cima) |
|---|---|
| 01 · Starting / 04 · BRB / 05 · Encerramento | Telas 💤/⏸/🏁 (fundo opaco 1920×1080) |
| 03 · Just Chatting | BG · Just Chatting |
| 06 · Tela | Captura do Monitor |
| 02 · Gameplay | (é a base da cena — nada cobre) |

**Para replicar manualmente no seu OBS atual (sem reimportar):**
1. Clique direito na fonte 🎮 CAPTURA · Tibia (na cena Gameplay) → **Copiar**;
2. Em cada uma das outras 5 cenas → clique direito na lista → **Colar (Referência)**;
3. Arraste a cópia para o **FUNDO da lista** (última posição — no OBS, o topo da lista fica na frente);
4. Confira que a imagem full-screen da cena está ACIMA dela na lista (telas/BG/monitor);
5. Nunca mais use "Ocultar Fonte" nela — troque de cena e pronto.
> Custo: o OBS renderiza a captura por baixo mesmo coberta (consumo extra desprezível). Ganho: zero tela preta ao trocar de cena.

**Recuperar uma captura travada sem abrir outro client** (versões sem "Fechar Hook"):
- Selecione a fonte → na barra de ferramentas das Fontes use **Desativar fonte** → **Ativar fonte** (reinicia a captura por completo, refaz o hook) — ou desmarque/remarque a janela nas Propriedades.
