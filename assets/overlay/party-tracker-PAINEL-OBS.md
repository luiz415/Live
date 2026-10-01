# Party Tracker — editar pelo próprio OBS (sem abrir navegador)

Com o **Custom Browser Dock** do OBS você transforma a página administrativa
(`party-tracker-admin.html`) em um painel fixo do OBS. Assim você edita os
jogadores sem sair do OBS, sem abrir o Chrome, sem servidor e sem URL.

A widget pública (`party-tracker.html`) que já está na cena 02 continua
apenas leitura; ela lê a chave `exoriPartyV1` do `localStorage` a cada 5 s e
atualiza sozinha.

Requisito: **OBS 30 ou superior** (Custom Browser Docks é estável a partir do OBS 28,
recomendado o 30+).

---

## 1. Adicionar o painel uma única vez

1. No OBS, vá em **Visualizar → Painéis → Custom Browser Docks…**
   (em inglês: **View → Docks → Custom Browser Docks…**).

2. Clique em **"+"** (Add a new dock).

4. Preencha:
   - **Dock Name:** `Party Tracker Admin` (é o nome que aparece na aba do OBS).
   - **URL:** `file:///C:/twitch/exoriservice/assets/overlay/party-tracker-admin.html`
   - **Refresh browser when scene becomes active:** deixe **desmarcado** (a página
     não precisa recarregar).

5. Confirme. Uma nova aba chamada **Party Tracker Admin** aparece nos
   painéis do OBS. Arraste-a para o lado da sua tela onde preferir
   (direita, embaixo, onde quiser).

Pronto. Agora é só clicar nessa aba para editar.

---

## 2. Como editar durante a live

1. Clique na aba **Party Tracker Admin** dentro do OBS.

2. Edite TÍTULO, VISÃO, QUEST e os 5 jogadores (VOC + LV).

3. Clique em **SALVAR** (ou apenas espere 4 segundos — o salvamento
   é automático).

4. Mude para a aba **Cenas** ou olhe o preview: a widget do Party Tracker
   já mostra os valores novos. **Sem Interact, sem clicar no widget, sem
   sair do OBS.**

Os espectadores só veem o resultado, nunca os campos de edição.

---

## 3. O que aparece onde

| Lugar | O que você vê | Os espectadores veem? |
|---|---|---|
| Aba **Party Tracker Admin** (painel do OBS) | TÍTULO, VISÃO, QUEST, jogadores, botões | **não** — é só seu |
| Cena 02 (fonte `🐺 WIDGET · Party Tracker`) | Só o resultado: `PARTY · DR320 / MA410 / …` | sim |

A aba do painel não vai para a transmissão porque ela é um painel do OBS,
não uma fonte.

---

## 4. Persistência

Os dados ficam em `localStorage['exoriPartyV1']` no perfil do Chromium
embutido do OBS. Sobrevivem a:

- trocar de cena e voltar;
- ocultar/mostrar a fonte do widget;
- reiniciar o OBS.

Se você quiser apagar tudo, clique em **LIMPAR TUDO** na aba.

---

## 5. Quando você abrir o OBS em outro PC

O `localStorage` é por perfil de navegador. Se você migrar a coleção para
outro PC, o painel começa vazio. Para copiar os dados:

1. Na aba do painel, **COPIAR LINK** gera uma URL com `?title=...&v1=...&l1=...`.

2. No OBS novo: duplo-clique na fonte **🐺 WIDGET · Party Tracker** →
   cole a URL no campo **URL** → OK.

A widget lê os dados da URL quando ela abre; depois você pode editar pelo
painel normalmente.

---

## 6. Limitações conhecidas

- O Custom Browser Dock é uma janela do Chromium com `localStorage`
  próprio. Em outros programas de stream (Streamlabs, vMix etc.) ele não
  existe; aí use o método antigo (abrir a admin no navegador do sistema).

- `<select>` (dropdown) e `<input type=color>` dentro de Custom Browser
  Docks têm bugs conhecidos de foco no Chromium. Como a admin só usa
  `<input type=text>`, `<input type=number>` e `<select>` simples,
  isso não impede a edição. Se notar que o dropdown não abre, troque o
  `<select>` por dois botões "SOUL WAR" / "SANGUINE" — me avise que eu
  mando a versão.