# Party Tracker — editar pelo próprio OBS (em tempo real, sem copiar URL)

Com o **Custom Browser Dock** do OBS você transforma a página administrativa
(`party-tracker-admin.html`) em um painel fixo do OBS. As edições são enviadas
ao **servidor local** (`twitch-contador-server.js` — o mesmo do contador da
Twitch) e a widget da cena 02 atualiza **sozinha em até 2 segundos**, sem
precisar clicar em "Atualizar" nem colar URL.

- Não precisa de janela do navegador aberta.
- Não precisa clicar "Refresh cache" no OBS.
- Não precisa copiar a URL de novo.
- O painel não vai para a transmissão: é um Dock, não uma fonte.

Requisitos:
- **OBS 30 ou superior** (Custom Browser Docks).
- **Node.js** instalado (já é requisito para o contador da Twitch).
- O terminal com `node twitch-contador-server.js` **aberto** durante a live
  (o mesmo terminal do contador).

---

## 1. Configurar o painel uma única vez

### 1.1 Ligar o servidor local (só na primeira sessão de live)

1. Abra o terminal (cmd) na pasta `integracoes` (ex:
   `C:\Users\lphil\OneDrive\Desktop\Nova pasta (4)\integracoes`).
2. Rode:
   ```
   node twitch-contador-server.js
   ```
3. Deixe esse terminal aberto. Ele serve **tanto o contador da Twitch quanto
   a sincronização do Party Tracker**.

   Você deve ver algo como:
   ```
   twitch-contador-server ouvindo em http://127.0.0.1:7777 — canal: exoriservice
   ```

### 1.2 Adicionar o Custom Browser Dock no OBS

1. No OBS, vá em **Visualizar → Painéis → Custom Browser Docks…**
   (em inglês: **View → Docks → Custom Browser Docks…**).

2. Clique em **"+"** (Add a new dock).

3. Preencha:
   - **Dock Name:** `Party Tracker Admin`
   - **URL:** `file:///C:/Users/lphil/OneDrive/Desktop/Nova%20pasta%20(4)/assets/overlay/party-tracker-admin.html`

     (Se sua pasta estiver em outro lugar, substitua o caminho até
     `party-tracker-admin.html`. Use `/` em vez de `\`, e espaços viram
     `%20`. Você também pode usar **"Copiar como caminho"** no Explorador e
     trocar as `\` por `/`.)

   - **Refresh browser when scene becomes active:** deixe **desmarcado**.

4. Confirme. Uma nova aba chamada **Party Tracker Admin** aparece nos
   painéis do OBS. Arraste-a para o lado da sua tela onde preferir.

Pronto.

---

## 2. Editar durante a live (em tempo real)

1. Clique na aba **Party Tracker Admin** dentro do OBS.
2. Edite TÍTULO, VISÃO, QUEST e os 5 jogadores (VOC + LV).
3. **Não precisa clicar em SALVAR**: o salvamento é automático depois de 4 s
   de inatividade (ou clique **SALVAR** para aplicar na hora).
4. Olhe o preview ou mude para a cena 02: a widget do Party Tracker
   **já mostra os valores novos** em até 2 segundos.

   O texto **"servidor: conectado ✓"** no alto do painel confirma que a
   sincronização está funcionando. Se aparecer **"servidor: offline"**,
   verifique se o `node twitch-contador-server.js` ainda está rodando.

Os espectadores só veem o resultado — nunca os campos de edição.

---

## 3. O que aparece onde

| Lugar | O que você vê | Os espectadores veem? |
|---|---|---|
| Aba **Party Tracker Admin** (painel do OBS) | TÍTULO, VISÃO, QUEST, jogadores, botões | **não** — é só seu |
| Cena 02 (fonte `🐺 WIDGET · Party Tracker`) | Só o resultado: `PARTY · DR320 / MA410 / …` | sim |

---

## 4. Persistência

- Os dados ficam gravados em `integracoes/party-data.json` (na mesma pasta do
  servidor local). Sobrevivem a:
  - trocar de cena e voltar;
  - reiniciar o OBS;
  - reiniciar o `node twitch-contador-server.js`.
- Uma cópia extra fica no `localStorage` do perfil Chromium do OBS.

Para apagar tudo, clique **LIMPAR TUDO** na aba do painel.

---

## 5. Abrir o OBS em outro PC

O arquivo `integracoes/party-data.json` pode ser copiado manualmente para o
novo PC (na mesma pasta do servidor). Alternativamente:

1. Na aba do painel, **COPIAR LINK** gera uma URL com
   `?title=…&v1=…&l1=…`.
2. No OBS novo: duplo-clique na fonte **🐺 WIDGET · Party Tracker** → cole a
   URL no campo **URL** (se a fonte estiver em "Local file", troque para
   "URL" ou cole o caminho do local file com os parâmetros).
3. Quando o servidor local estiver rodando no PC novo, as edições seguintes
   já sincronizam normalmente.

---

## 6. Se o servidor não estiver rodando (modo de contingência)

Se por qualquer motivo `node twitch-contador-server.js` não estiver rodando:

- O painel continua funcionando e salvando no `localStorage`.
- A widget **não** vai atualizar em tempo real (ela tenta o servidor por
  ~6 s e cai no `localStorage` — mas Browser Source e Custom Dock podem ter
  perfis Chromium diferentes no OBS, então esse fallback é só "melhor
  esforço").
- Apertar **COPIAR LINK** e colar a URL na fonte do widget sempre funciona,
  sem servidor.

Recomendação: mantenha o terminal com o servidor aberto durante a live, é o
modo confiável.

---

## 7. Solução de problemas

| Sintoma | Causa | Correção |
|---|---|---|
| A widget não atualiza depois de editar | Servidor não está rodando | Verifique o terminal com `node twitch-contador-server.js` |
| Painel diz "servidor: offline" | Mesmo motivo | Ligue o servidor; recarregue o painel (botão direito na aba → Recarregar) |
| A widget pisca ao trocar de cena | `shutdown` está ligado | Na coleção de cenas, a fonte `🐺 WIDGET · Party Tracker` deve ter **"Shutdown source when not visible" DESMARCADO** (a coleção que acompanha o pacote já vem assim) |
| "Falha ao conectar" no navegador | Firewall do Windows bloqueando 127.0.0.1 | Libere `node.exe` no firewall; o acesso é só local |
