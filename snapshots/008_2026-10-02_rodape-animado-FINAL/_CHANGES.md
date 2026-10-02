# 008 — RODAPÉ ANIMADO (final)

Snapshot final do Rodapé Animado gerado diretamente do workspace após o
push do commit 6f6e8a9. Substitui o antigo `📨 TICKER · Comandos`.

## Como usar (resumo rápido)
1. Copiar a pasta `importar-pc/` para C:\Users\lphil\OneDrive\Desktop\Nova pasta (4)\
   (ou o caminho antigo C:\twitch\exoriservice\ — ajustar o caminho na fonte
   se necessário).
2. No OBS, importar `exoriservice-cenas.json` (ou só abrir propriedades da
   fonte "📨 TICKER · Comandos" → apontar o arquivo local para rodape.html
   e renomear para "📨 RODAPÉ ANIMADO" se a coleção não for reimportada).
3. Selecionar a fonte em qualquer cena → Interagir → clicar dentro → E.
4. Escolher efeito (1 a 6), ajustar sliders, editar mensagens.
5. E / Esc para sair SEMPRE antes de voltar ao ar.

## Arquivos-chave
- importar-pc/assets/overlay/rodape.html  — widget + editor embutido
- importar-pc/assets/overlay/party-tracker.html  — Party Tracker (E)
- importar-pc/exoriservice-cenas.json  — coleção OBS com fonte renomeada
- importar-pc/LEIA-ME.txt  — instruções (bloco 6: Rodapé Animado)

## Persistência
- localStorage chave `exoRodapeV1` (rodapé) e `exoriPartyV1` (party tracker).
- Auto-save 4 s. Backup manual em _backup/.
