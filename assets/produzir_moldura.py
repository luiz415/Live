#!/usr/bin/env python3
"""MOLDURAS ANIMADAS v3 — APENAS O COMETA orbitando o perímetro + brackets nos cantos.
• Marching/energia removidos (pedido): nenhum traço percorrendo a borda — só o cometa;
• FAIXA DO TICKER LIVRE: no monitor e no Just Chatting o circuito do cometa sobe e
  fecha a 6,8vh do fundo ( nada de efeitos na faixa onde o Ticker · Comandos vive);
• moldura-jogo (miniatura 480×270 na cena Tela): retângulo fechado — na cena ela fica
  inteiramente ACIMA do ticker, sem conflito.
Gera: moldura-monitor.html · moldura-jogo.html (etiqueta JOGO) · moldura-jc.html."""
import base64

F = "/home/user/twitch-pro/assets/fonts/"
OUT = "/home/user/twitch-pro/assets/overlay/"
C6 = base64.b64encode(open(F + "ChakraPetch-600.ttf", "rb").read()).decode()

TPL = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Moldura @@ROTULO@@ — exoriservice</title><style>
@font-face{font-family:Chakra;font-weight:600;src:url(data:font/ttf;base64,@@C6@@) format('truetype')}
:root{--acid:#B4FF00;--toxic:#5C9900}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:transparent}
.frame{position:fixed;inset:0;pointer-events:none}

/* ── COMETA: única luz percorrendo o perímetro (volta completa contínua) ──
   monitor/jc: circuito fecha a 6,8vh do fundo → faixa do ticker 100% livre */
@property --a{syntax:'<angle>';initial-value:0deg;inherits:false}
.ring{position:absolute;inset:0 0 @@BASE@@ 0;padding:2px;
 background:conic-gradient(from var(--a),
  transparent 0deg 150deg,
  rgba(180,255,0,.14) 150deg,
  rgba(180,255,0,.9) 342deg,
  #F4FFD0 350deg,
  rgba(180,255,0,.9) 353deg,
  transparent 360deg);
 -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
 mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
 -webkit-mask-composite:xor;mask-composite:exclude;
 filter:drop-shadow(0 0 6px rgba(180,255,0,.7));
 animation:orbit 6s linear infinite}
@keyframes orbit{to{--a:360deg}}

/* ── trilho fixo sutil (por onde o cometa corre) ── */
.rail{position:absolute;inset:0 0 @@BASE@@ 0;border:1px solid rgba(180,255,0,.22)}

/* ── brackets pulsantes nos cantos (não percorrem a borda) ── */
.b{position:absolute;width:5vh;height:5vh;border:.75vh solid var(--acid);filter:drop-shadow(0 0 1.4vh rgba(180,255,0,.55));animation:bpulse 2.2s ease-in-out infinite}
.b1{top:.9vh;left:.9vh;border-right:0;border-bottom:0}
.b2{top:.9vh;right:.9vh;border-left:0;border-bottom:0;animation-delay:.28s}
.b3{bottom:calc(@@BASE@@ + .9vh);left:.9vh;border-right:0;border-top:0;animation-delay:.56s}
.b4{bottom:calc(@@BASE@@ + .9vh);right:.9vh;border-left:0;border-top:0;animation-delay:.84s}
@keyframes bpulse{50%{opacity:.45;transform:scale(.9)}}
@@CSS_EXTRA@@
</style></head><body>
<div class="frame">
  <div class="rail"></div>
  <div class="ring"></div>
  <div class="b b1"></div><div class="b b2"></div><div class="b b3"></div><div class="b b4"></div>
  @@TAG@@
</div>
</body></html>"""

TAG_CSS = """
.tag{position:absolute;top:1.1vh;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:1vh;
 background:var(--acid);color:#060806;font-family:Chakra;font-weight:600;font-size:2.3vh;
 letter-spacing:.26em;padding:.7vh 2.1vh .7vh calc(2.1vh + .26em);white-space:nowrap;
 clip-path:polygon(.9vh 0,100% 0,100% calc(100% - .9vh),calc(100% - .9vh) 100%,0 100%,0 .9vh);
 box-shadow:0 0 2vh rgba(180,255,0,.4)}
.tag .dot{width:1.1vh;height:1.1vh;background:#060806;border-radius:50%;animation:blink 1.6s infinite}
@keyframes blink{50%{opacity:.25}}"""

TAG_HTML = '<div class="tag"><span class="dot"></span>@@ROTULO@@</div>'

# (rotulo, arquivo, base) — base 6.8vh = circuito sobe acima da faixa do ticker; 0 = retângulo fechado
VARIANTES = [("", "moldura-monitor.html", "6.8vh"), ("JOGO", "moldura-jogo.html", "0"), ("", "moldura-jc.html", "6.8vh")]

for rotulo, arquivo, base in VARIANTES:
    tag_css = TAG_CSS if rotulo else ""
    tag_html = TAG_HTML.replace("@@ROTULO@@", rotulo) if rotulo else ""
    html = (TPL.replace("@@ROTULO@@", rotulo or "GERAL").replace("@@C6@@", C6)
            .replace("@@BASE@@", base).replace("@@CSS_EXTRA@@", tag_css).replace("@@TAG@@", tag_html))
    open(OUT + arquivo, "w").write(html)
    print(arquivo, "ok (" + str(len(html) // 1024) + " KB)")
