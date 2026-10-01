# 🤖 Etapa 6 — Nightbot: Guia Completo de Configuração
**Entregáveis:** este guia + `nightbot/comandos-chat.txt` (script de colar) + `nightbot/cheatsheet-ao-vivo.md` (consulta rápida durante a live).
**Tempo total estimado: 15 minutos.**

---

## 1. Ativar o Nightbot (3 min — só na primeira vez)

1. Acesse **nightbot.tv** → **Sign in with Twitch** → autorize com a conta `exoriservice`;
2. No dashboard, vá em **Dashboard → Join Channel** (canal `exoriservice`);
3. Abra seu chat na Twitch (pode ser durante uma live de teste) e digite:
   ```
   /mod nightbot
   ```
4. Teste digitando no chat: `!uptime` — se o Nightbot responder, está ativo. ✅

> O Nightbot roda **na nuvem** — não precisa de nada aberto no seu PC. Enquanto a conta existir e ele for mod, ele funciona.

## 2. Comandos personalizados (5 min)

### 2.1 Criar tudo de uma vez
Abra `nightbot/comandos-chat.txt` e cole as linhas **uma a uma** no seu chat. São os **6 comandos oficiais do canal (v3)**:

> ⚠️ **Veio da v1?** Se criou os comandos antigos (!discord, !instagram, !social, !apoiar, !jogo, !vods), remova-os primeiro com as linhas de limpeza no fim do arquivo.

| Comando | Resposta (resumo) | Cooldown sugerido |
|---|---|---|
| `!service` | **Comando principal** — services no RubinOT (leveling · quests · hunts · boss · intermediação) + Rubini Coins (1k = R$ 90,00) + "cadastre seu personagem no chat" | 20s |
| `!coins` | **Rubini Coins** — 1k = R$ 90,00, entrega rápida e segura; compra via chat ou `!wpp` | 15s |
| `!intermedio` | **Intermédio de itens** — rapidez, segurança e preço justo; contratação via chat ou `!wpp` | 15s |
| `!wpp` | Link direto do WhatsApp comercial (`wa.me` com mensagem pré-definida) — **use número dedicado/comercial, nunca o pessoal** | 15s |
| `!horario` | Agenda SEG–SÁB 08h–22h | 10s |
| `!regras` | 5 regras do chat | 10s |
| `!setup` | Seu setup *(preencher depois)* | 10s |
| `!site` | Site oficial *(placeholder até o link)* | 15s |

### 2.2 Definir cooldowns (dashboard, 2 min)
Para cada comando: **nightbot.tv → Commands → Custom → ✏️ (editar)**:
- Aba **Advanced** → **Cooldown: User** = valor da tabela acima (em segundos) → **Confirm**.

Cooldown evita spam do mesmo espectador martelando `!social`.

### 2.3 Preencher os placeholders quando os dados chegarem
Direto no chat (mais rápido):
```
!commands edit !site 🖥️ Site oficial: https://SEULINK
!commands edit !setup 🖥️ Setup: Ryzen 5 5600 · RTX 3060 · mic Fifine K669 ...
```

## 3. Mensagens automáticas — Timers (3 min)

**nightbot.tv → Timers → + Add Timer** — crie os 3 abaixo (v2, foco em services):

| # | Nome | Intervalo | Mensagem |
|---|---|---|---|
| 1 | `service` | **20 min** | ⚔️ Precisa de service? leveling · quests · hunts · intermediação — cadastre-se: !service |
| 2 | `coins` | **35 min** | 💰 Rubini Coins: 1k = R$ 90,00 — para negociar, chama no chat: !service |
| 3 | `agenda` | **55 min** | 📅 Lives de SEG a SÁB, 08h às 22h — !horario e ativa as notificações ⏰ |

> ⚠️ Veio da v1? Delete os timers antigos (`social`, `discord`, `apoio`) antes de criar estes.

**Como criar:** nome → habilitar ✅ → **Interval: X minutes** → em **Messages** clique em **+** e cole o texto → Save.

**Boa prática anti-spam:** comece com os timers **1 e 2 ativos**; ative o 3 e o 4 quando o chat estiver mais movimentado. Intervalos ≥20 min ficam confortáveis e dentro das boas práticas da Twitch.

## 4. Moderação profissional (3 min)

**nightbot.tv → Spam Protection** — para cada filtro, ative ✅ e clique na **engrenagem ⚙️** para configurar:

| Filtro | Configuração | Ação |
|---|---|---|
| **Links** | Exempt: Moderators ✅ · Regulars ✅ · Subscribers ✅ | Timeout **600s** (após 1 aviso) |
| **Caps (excessivo)** | Máx. **50%** maiúsculas · mínimo **10 caracteres** · exempts iguais | Timeout **10s** |
| **Symbols** | Máx. **30 símbolos** · mínimo 10 chars | Timeout **10s** |
| **Emotes** | Máx. **15 emotes** por mensagem | Timeout **10s** |
| **Spam (mensagens)** | Máx. **15 mensagens / 30s** | Timeout **600s** |
| **Message Length** | Máx. **400 caracteres** | Timeout **10s** |
| **Blacklist** | Vazio inicialmente — adicione palavrões/tópicos proibidos conforme surgirem | Timeout **600s** |

Comandos de moderação que já vêm prontos (para você e mods):

| Comando | Função |
|---|---|
| `!permit @usuario` | Permite que alguém poste **1 link** |
| `!timeout @usuario 300` | Silencia por 5 min |
| `!ban @usuario` / `!unban @usuario` | Banir / reverter |
| `!clear` | Limpa o chat (após spam pesado) |
| `!moderate` | Painel rápido de moderação |

**Regulars** (dashboard → **Community → Regulars**): cadastre espectadores de confiança — ficam imunes aos filtros suaves (caps/emotes/símbolos). Use com parcimônia.

## 5. Boas-vindas — decisão importante (leia)

O Nightbot **não possui saudação automática por entrada de espectador** no chat da Twitch ( recurso proposital: em canais grandes viraria spam ). Decisão profissional para o seu caso:

- **Recomendado (vibe chill):** saudação **pessoal sua** quando alguém novo comentar — nada bate uma comunidade acolhedora;
- **Quem agradece follow/sub na hora** são os **alertas visuais da Etapa 4B** (nome do espectador na tela) — impacto muito maior que mensagem de bot;
- Se um dia quiser boas-vindas 100% automáticas por entrada, o caminho é um bot local (Streamer.bot) — registrado como **upgrade futuro** no roadmap, sem custo agora.

## 6. Variáveis úteis do Nightbot (para criar comandos novos)

| Variável | Mostra | Exemplo de uso |
|---|---|---|
| `$(user)` | Quem digitou | `$(user) acabou de ganhar um abraço!` |
| `$(touser)` | 1º argumento após o comando | `!so $(touser)` (shoutout) |
| `$(channel)` | Seu canal | `Bem-vindo ao $(channel)!` |
| `$(count)` | Contador do comando | `!mortes → o exoriservice já morreu $(count) vezes` 💀 |
| `$(twitch $(channel) "{{uptime}}")` | Tempo de live | dentro de textos |

💡 Comando criativo sugerido para RPG: `!mortes` com contador — o chat **AMA** isso em lives de Tibia. Criar: `!commands add !mortes 💀 mortes do stream nesta saga: $(count)` — e digitar `!mortes` a cada wipe para incrementar 😄

## 7. Testes da etapa (5 min)

- [ ] `!uptime` respondeu (bot ativo)
- [ ] Script colado — os 5 comandos respondem (`!service`, `!horario`, `!regras`, `!setup`, `!site`)
- [ ] Cooldowns aplicados (teste digitar `!service` 2× rápido)
- [ ] Timers `service`, `coins` e `agenda` criados e ativos (aguarde 1 ciclo em live de teste)
- [ ] Filtros de moderação ativos (peça a alguém para POSTAR UM LINK sem permissão → deve levar timeout; depois `!permit` deve liberar)
- [ ] `!regras` e `!service` com textos corretos

## 8. Manutenção futura

- Novos comandos: `!commands add !comando texto` no chat;
- Trocar mensagens: `!commands edit !comando novo texto`;
- Pausar o bot em algum momento: dashboard → **Spam Protection/Commands** têm toggle individual, ou remova o mod ( `/unmod nightbot` ) — raramente necessário.

---

*Próxima etapa — 7 · **Painéis + Integrações**: subir painéis no perfil, conectar StreamElements (alertas/chat/doações), configurar links e o ciclo de divulgação.*
