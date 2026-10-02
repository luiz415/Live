# 007 — RODAPÉ ANIMADO (Interagir + tecla E)

Substitui o antigo `📨 TICKER · Comandos` (ticker.html, rolagem contínua
apenas, velocidade por ↑/↓, 6 mensagens hardcoded) por um rodapé com
editor embutido acessível via Interagir → E.

## Arquivos alterados
- assets/overlay/rodape.html (NOVO, ~90 KB, 6 motores + admin embutido)
- assets/overlay/ticker.html → ticker.html.old (backup)
- obs/exoriservice-cenas.json (fonte renomeada para 📨 RODAPÉ ANIMADO nas
  5 cenas 01/02/04/05/06; local_file → overlay/rodape.html)
- obs/gerar_colecao.py (N_TICKER renomeado; página → rodape.html)
- importar-pc/ sincronizado; LEIA-ME atualizado (novo bloco 6)

## 6 efeitos
1. Rolagem contínua (scroll infinito em loop perfeito)
2. Desliza por mensagem (entra dir → para → sai esq)
3. Fade (crossfade de opacidade)
4. Deslizamento lateral (próxima entra enquanto a atual sai)
5. Máquina de escrever (digita letra por letra + cursor piscante)
6. Estático (sem animação, troca a cada permanência)

## Persistência
localStorage chave `exoRodapeV1` (mesmo perfil, mesma fonte). Auto-salva
em 4 s de inatividade e ao fechar o painel.

## Uso
No OBS: selecionar "📨 RODAPÉ ANIMADO" → Interagir → clicar dentro → E.
Aviso: painel aberto aparece no stream (limitação do Interagir); saia
com E/Esc antes de deixar a cena no ar.

## A verificar manualmente no OBS
- Cada um dos 6 efeitos roda sem flicker/corte.
- Mensagens com HTML (<b>/<i>/<em>/<strong>) renderizam certo.
- Rolagem contínua loop perfeito em 1920×72.
- Painel E abre/fecha sem sobrepor conteúdo quando fechado.
