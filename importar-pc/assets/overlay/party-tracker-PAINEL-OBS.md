# Party Tracker — editar pelo "Interagir" do OBS (tecla E)

A fonte **🐺 WIDGET · Party Tracker** já tem o editor embutido. Não precisa de
Custom Browser Dock, não precisa de navegador separado, não precisa copiar URL
nem manter servidor rodando para editar.

## Como editar

1. Na cena 02, selecione a fonte **🐺 WIDGET · Party Tracker**.
2. Clique com o botão direito na fonte → **Interagir** (ou menu **Fonte → Interagir**).
3. Uma janela pequena abre com o widget visível. **Clique dentro** dessa janela
   para dar foco.
4. Aperte a tecla **E** → o painel de edição aparece.
5. Edite TÍTULO, VISÃO, QUEST e os 5 jogadores.
   - Auto-salva depois de 4 segundos de inatividade, ou clique **SALVAR**.
6. Aperte **E** de novo (ou **Esc**, ou botão **SAIR**) para fechar o painel.
7. Feche a janela "Interagir". O público vê o widget atualizado.

> ⚠ **Aviso importante:** enquanto o painel estiver aberto ele aparece **sobre
> o widget**. Se a cena 02 estiver no ar, o público verá o painel.
> **Saia do modo edição (E/Esc) antes de sair da janela Interagir** — quando o
> painel está fechado o público vê só o widget, mesmo com a fonte selecionada.
> Para editar "escondido", troque para a cena BRB/Starting antes de abrir
> Interagir.

## Atalhos

| Tecla | O que faz |
|---|---|
| **E** | Alterna entre modo visualização / edição |
| **Esc** | Sai do modo edição (salva) |
| Botão SALVAR | Salva na hora |
| Botão LIMPAR TUDO | Apaga todos os dados |

## Persistência

- Os dados ficam em `localStorage` no perfil Chromium da própria fonte do OBS.
- Sobrevivem a: trocar de cena, reiniciar o OBS, desligar o PC.
- Para copiar os dados para outro PC: abra Interagir → E → anote os valores
  (ou use o console do DevTools para ler `localStorage.exoriPartyV1`).

## Solução de problemas

| Problema | Correção |
|---|---|
| Aperto E e não acontece nada | Clique **dentro** da janela Interagir antes de apertar E (a janela precisa ter foco). |
| Quando edito a live pisca | A fonte está com "Shutdown when not visible" — deixe **desmarcado** (a coleção já vem assim). |
| Quero ver o widget sem o painel durante a edição | Aperte E de novo ou Esc: o painel some e o widget continua atualizado. |
| Aparecem campos enquanto estou ao vivo | Saia do modo edição (E/Esc) antes de deixar a cena 02 ativa. |
