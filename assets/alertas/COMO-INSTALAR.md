# 🔔 Como instalar os alertas — StreamElements (v4 · INTENSIDADE MÁXIMA)
> Fluxo validado para o editor atual do SE. Caminho: configurações da AlertBox → aba do tipo → rodapé → **Enable custom CSS** → **Open Editor** → abas **HTML/CSS**.

**Arquivos desta versão:**
- `streamelements/v4/1-ABA-HTML_<tipo>.txt` → 7 fragmentos (aba HTML) — **use a v4**;
- `streamelements/v4/2-ABA-CSS_geral-para-todos.txt` → CSS único (aba CSS, igual para todos);
- `sfx-mp3/sfx-<tipo>.mp3` → sons em MP3 para o campo **Sound**.

## 🎚 Níveis de impacto (v4 — MÁXIMO)

| Tier | Tipo | Efeitos | Duração |
|---|---|---|---|
| **T1** | Follower | Banner + ripple triplo do emblema, 9 pontos ascendentes, 3 streaks de entrada, scanline, malha de fundo | **6s** |
| **T2** | Sub / Resub / Gift | Raios cônicos girando, 2 órbitas com satélites, **12 shards explosivos**, pulso duplo de borda, 2 feixes móveis, pop do emblema | **6s** |
| **T3** | Tip / Bits | **24 moedas** em 3 profundidades, onda de energia em tela cheia, 2 choques horizontais, faíscas ✦, jitter, métrica pulsante, glow máximo | **7s** |
| **T4** | **Raid** | **Intro 3,3s**: escurecimento + chevrons de perigo + 3 ecos fantasma do emblema + "RAID!" glitchado + "VISITANTES A CAMINHO" + **tempestade de 18 shards** + 14 strobes + barras convergentes → banner: **shake contínuo**, radar duplo, glowline, 7 faíscas, vinheta pulsante, anéis 2× | **10s** |

**Camadas globais (todos os tiers):** malha de pontos de fundo, barra lateral direita, brackets de canto e scanline interna no banner.

## 1. Configurar cada tipo (como antes)

Para cada aba (FOLLOWER, SUBSCRIBER, TIP, RAID — e as demais se quiser):
1. **Sound** → upload do MP3 · **Alert Duration** conforme a tabela acima;
2. Rodapé → **Enable custom CSS** → **Open Editor**;
3. Aba **HTML**: Ctrl+A + colar `1-ABA-HTML_TIPO.txt` (v3) · Aba **CSS**: colar `2-ABA-CSS_geral-para-todos.txt`;
4. Fechar → **Salvar**.

## 2. ⚠️ POSICIONAMENTO NO OBS (correção do "alerta cortado")

O corte acontecia porque a fonte era menor que o **canvas do overlay** (1920×1080). A regra WYSIWYG:

1. **No OBS:** fonte 🔔 ALERTAS → largura **1920** × altura **1080**, posição **(0, 0)** — ocupando a cena inteira (fundo transparente, só o alerta aparece);
2. **No editor do SE:** selecione a **AlertBox** no canvas e arraste/posicione-a no **topo-centro** (ex.: X=520, Y=40) — onde o banner deve surgir;
3. Pronto: **o que você vê no editor é o que sai na live** — sem cortes.

> 💡 O mesmo vale para o overlay do chat (💬): fonte do tamanho do canvas do overlay correspondente.

## 3. Testar

- Botões de **teste** no editor do SE (aba de cada tipo) — o alerta aparece no canvas E na fonte do OBS em tempo real;
- Durações por tipo (campo Alert Duration): follow/sub/resub/gift **6s** · bits/tip **7s** · raid **10s** (a intro usa 3,3s antes do banner).

## 4. Solução de problemas

| Sintoma | Correção |
|---|---|
| Alerta cortado/deslocado no OBS | Fonte 1920×1080 em (0,0) + widget posicionado no editor (seção 2 acima) |
| Nada aparece | Dispare um Test no editor; confira se Salvou o overlay |
| Fontes diferentes no preview | Google Fonts carregam online (OBS ok; editor às vezes não) |
| `{{name}}` literal | Confira o fragmento do tipo certo (gift usa `{{sender}}`) |
| "TTier" no teste de sub | Era o prefixo "T" + preenchimento de teste do SE ("Tier") — corrigido na v4 (`{{tier}}` puro). Sub real = 1/2/3 |
| Campo "Alert Text / Available variables" | **Não precisa preencher** — com HTML customizado, o design já insere nome/valor. Deixe o padrão; esse campo só é usado pelo layout padrão do SE |

## ❓ Dúvidas frequentes

**O que é "Tier" na sub?** É o nível da inscrição na Twitch — definido pelo **espectador na hora de assinar**, não por você configurar nada:
- **Tier 1** — o padrão (≈ R$ 19,90 no Brasil) — a esmagadora maioria das subs;
- **Tier 2 e 3** — níveis opcionais de preço maior (≈ 2× e 5×) que dão os mesmos benefícios + mais emotes à medida que o canal cresce;
- **Prime Gaming** — 1 sub gratuita/mês para quem tem Amazon Prime (conta como Tier 1 para você);
- Você não precisa preencher nada no SE — a variável `{{tier}}` já chega preenchida pelo evento (1, 2 ou 3).

---
*Legado: `streamelements/` (v1) e `streamelements/v2/` permanecem como referência — em produção, use a **v3**.*

