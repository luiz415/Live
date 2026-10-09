# 📦 Etapa 4A — Guia dos Arquivos de Arte

> Tudo nesta pasta já está na identidade oficial (dragão Hex Strike · preto + verde ácido `#B4FF00` · Orbitron/Chakra Petch).
> Os arquivos HTML são **totalmente autônomos** (fontes e logo embutidos) — funcionam sem internet.

## 🖥️ telas/ (adicionar no OBS como "Navegador" → ✅ Arquivo Local)

**Regras aplicadas:** dragão aparece somente na logo (nenhum texto o menciona) · telas sem comandos (comandos ficam no overlay de gameplay e no bot) · textos mínimos · efeitos agressivos (glitch RGB no wordmark, anéis hexagonais girando, scanlines, feixes de luz, grão, shards, partículas, scramble no status, flicker, barras de energia fluindo, brackets de canto e ignição com flash no zero).

| Arquivo | Cena | Textos exibidos |
|---|---|---|
| `starting-soon.html` | Iniciando em breve | status "iniciando em" + contagem + chips (SEG–SÁB · 08H–22H / TIBIA · RUBINOT) |
| `brb.html` | Pausa / BRB | status "pausa rápida" + "já volto" |
| `encerramento.html` | Fim da live | status "obrigado pela live" + "até segunda, 08h" + chips |
| `*-fallback.png` | Versões estáticas | Mesmos textos, sem animação |

**Contagem regressiva:** padrão 10 min. Para mudar: no OBS, edite a URL do navegador adicionando `?t=MINUTOS` (recurso "Atualizar navegador quando a cena ficar ativa" recomendado), ou altere o `10` no JS do arquivo. Quando chega a 00:00: flash de ignição + "JÁ VAI COMEÇAR" + anéis aceleram.

## 🕹️ overlay/

| Arquivo | Uso |
|---|---|
| `overlay-gameplay.html` | Overlay da gameplay — **quadro da marca MÓVEL e AJUSTÁVEL** (janela **Interagir** com **E**: painel no topo com slider + botões −/+ + % ao vivo + RESET, **scroll do mouse** sobre o quadro redimensiona, arraste move — salva sozinho) com **cometa orbitando a borda do quadro + shimmer no texto + logo pulsante**. Borda da tela termina acima da faixa do ticker; ticker embutido desativado (`CFG.ticker:false`) |
| `ticker.html` | **Ticker de anúncios (fonte própria e AJUSTÁVEL, sem rótulo)** — **6 anúncios**: ⚔️ SOUL WAR · 💰 RUBINI COINS (1K R$ 90,00 · estoque limitado) · 🤝 INTERMÉDIO · 🕐 HORÁRIOS · 📜 REGRAS · 🖥️ SETUP. Palavra-chave verde neon, chamadas em branco, seta → e comando em chip; **divisor “nó de circuito”** (losango ácido pulsante + 2 satélites + hairlines, 2,2em); **loop infinito REAL** — motor rAF com **re-medida automática** (fonte/resize, preservando a fase) = emenda 100% imperceptível para sempre. Presente em TODAS as 6 cenas (1920×72, y=1008) |
| `party-tracker.html` | **Party Tracker v3.1** — 5 células (vocação 2 letras + LV) editáveis ao vivo + linha acima do quadro com **“VISÃO DO:”** (vocação de 2 letras) e **“QUEST:”** com seletor **SOUL WAR** (cinza neon) / **SANGUINE** (vermelho) — clicável ao vivo, sem entrar em edição. **Ajuste igual ao carrossel**: E liga → painel no topo (slider + −/+ + % + RESET) · **scroll do mouse** redimensiona · **arraste** move · setas fino · salva sozinho. **Animações elegantes**: glow respirando, sweep de brilho, cometa orbitando o widget e logo/chip pulsando (sem flutuação) |
| `carrossel-servicos.html` | **Carrossel de anúncios AJUSTÁVEL ao vivo** — padrão **22% da largura**, canto inferior direito. Na janela **Interagir** do OBS: **E** liga → **painel no topo** (slider + botões −/+ que repetem ao segurar + % ao vivo + RESET) · **scroll do mouse** sobre a tela redimensiona · **arraste a caixa** move · **alça quadriculada 34px** no canto redimensiona · setas = ajuste fino · E/ESC saem. Posição/tamanho **salvam automaticamente** (localStorage) e valem para todas as cenas (mesma fonte). 4 slides (7s): Rubini Coins · Intermédio · Service c/ !service · RubinOT. **Presente em todas as cenas** na coleção v6 |
| `cobertura-chat.html` | **Cobertura do chat do jogo (PRIVACIDADE)** — fundo **escuro UNIFORME (cor única, 98%)** em toda a área: conversas do jogo invisíveis. Mantém varredura de luz, malha hexagonal e filete. Painel = canvas da fonte: redimensione no OBS |
| `moldura-monitor.html` / `moldura-jogo.html` / `moldura-jc.html` | **Molduras animadas v3 — SÓ O COMETA** orbitando o perímetro (traços/energia removidos) + brackets pulsantes nos cantos + trilho sutil. Monitor e JC fecham o circuito **a 6,8vh do fundo** → a faixa do **Ticker · Comandos fica 100% livre**; Jogo (miniatura) é retângulo fechado. Monitor e JC sem texto; Jogo com etiqueta JOGO |
| `overlay-gameplay-fallback.png` | Versão estática transparente (sem ticker) |

### 🐺 Party Tracker — como usar ao vivo

**Métodos de entrar em edição (janela "Interagir" do OBS):**
- Mova o mouse **em qualquer lugar** da janela → o botão **EDITAR** (grande, pulsando) aparece acima do quadro;
- Ou pressione a tecla **E** (liga/desliga a edição) — **ESC** sai da edição;
- Ou **clique duplo** sobre o quadro.

**Passo a passo:**
1. Copie o `party-tracker.html` atualizado para a pasta e clique com o direito na fonte no OBS → **Atualizar** (recarrega a versão nova);
2. Se a fonte estiver **travada** (🔒), destrave (clique no cadeado da lista de fontes) — elimina qualquer bloqueio;
3. Direito na fonte → **Interagir**;
4. Ao abrir, o botão EDITAR **pulsa sozinho por 6s** (confirma que a versão nova está ativa); mova o mouse e ele reaparece;
5. Clique em **EDITAR** (ou tecla E) → os campos viram caixas de texto → digite vocação (2 letras) e level;
6. **OK** para finalizar — salva sozinho e persiste entre reinícios.

Alternativa sem interação: preencher pela URL (`?title=GUILD&v1=EK&l1=250…`) — enquanto os parâmetros estiverem na URL eles vencem na inicialização.

Efeitos do quadro: entrada deslizante escalonada, flash na moldura ao alterar valor, scanline interna, barra de energia vertical fluindo, dot "ao vivo" pulsando.

### 🛡 Cobertura do chat do jogo (privacidade)

1. Fonte **Navegador → Arquivo Local** `cobertura-chat.html` na cena **02 · GAMEPLAY**, **acima da captura do jogo e abaixo dos widgets** (a coleção v3 já inclui na posição padrão: canto inferior esquerdo, 700×300);
2. **Redimensionar:** propriedades da fonte → mude Largura/Altura (pixels exatos) — ou arraste os cantos no preview. O painel preenche todo o canvas, então o tamanho da fonte = tamanho da cobertura;
3. **Posicionar:** arraste no preview até cobrir exatamente o chat do Tibia;
4. Ajustes finos no bloco `CFG` do arquivo: `forca` (0–1, quão escuro), `fadeTopo` (suavidade da transição), `borda`, `varredura`, `marca`.

## 🔔 alertas/ (Lote 4B)

| Item | Descrição |
|---|---|
| `preview-alertas.html` | Demonstração dos 7 alertas animados (abra no visualizador/navegador) |
| `streamelements/alerta-{follow,sub,resub,gift,bits,raid,tip}.html` | Código pronto para colar no StreamElements |
| `sfx/sfx-*.wav` | Sons de cada alerta + whoosh do stinger (síntese própria, sem copyright) |
| `COMO-INSTALAR.md` | Passo a passo no StreamElements + OBS |

## 🎬 stinger/ (Lote 4B)

- `stinger-transicao.webm` — transição animada (~0,73s, 60fps, **com canal alfa**): varredura de shards verde-ácido cobre a tela, emblema + wordmark em flash, barras de energia, e a cobertura sai varrendo;
- `stinger-preview.gif` — prévia rápida para visualizar;
- Instalação: OBS → cena → dock "Transições" → botão **+** → tipo **Stinger** → selecionar o `.webm` → **Ponto de transição: 50%**;
- ⚠️ Limitação do OBS: transições Stinger **não reproduzem áudio** nativamente. O `sfx/sfx-stinger.wav` está pronto caso queira tocar o whoosh manualmente (fonte de mídia + atalho) — opcional.

**Configuração rápida do overlay:** abra o arquivo num editor de texto e ajuste o bloco `const CFG` no final:
- `posicao`: `"topo"` ou `"base"` (local do ticker — testar qual cobre menos a interface do Tibia);
- `mostrarRotulo`: `true`/`false` (mostra/oculta o rótulo superior);
- `itens`: textos do ticker — **troque "em breve" pelos links reais quando os enviar.**

## 📑 paineis/ (8 painéis 320×160)

Subir no painel do canal Twitch: Editar painéis → Adicionar painel → Imagem → depois adicionar o link correspondente (a imagem não é clicável por si; o link é adicionado no editor do painel).

| Painel | Link sugerido |
|---|---|
| `painel-sobre.png` | — (texto no próprio painel) |
| `painel-horarios.png` | — |
| `painel-discord.png` | convite do Discord |
| `painel-redes.png` | instagram/links |
| `painel-regras.png` | — ou página de regras |
| `painel-apoie.png` | link de doação/sub |
| `painel-comandos.png` | — |
| `painel-setup.png` | — |

## 🎨 extras/

- `banner-perfil-1920x480.png` — banner do perfil (definir como imagem de capa do canal);
- `offline-1920x1080.png` — tela offline (usar na cena de encerramento após despedida, ou como banner de vídeo offline);
- `justchatting-1920x1080.png` — **BG da cena Just Chatting** (arte + emblema fantasma + lockup).

## 🔧 Manutenção

- Para regenerar tudo: `python3 produzir_estaticas.py` e `python3 produzir_html.py` (necessário apenas se mudar textos/agenda);
- Logos e wordmarks: `twitch-pro/logos/final/`.

## ⏭️ Próximo lote (4B)

- Pacote de alertas customizados (StreamElements, HTML colável): seguidor, sub, resub, gift, bits, raid, doação;
- Stinger de transição (vídeo WebM com transparência).
