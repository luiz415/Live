#!/usr/bin/env python3
"""Alertas v2 — formato para o editor ATUAL do StreamElements.
Gera: 7 fragmentos HTML (aba HTML) + 1 CSS compartilhado (aba CSS).
Fontes via Google Fonts @import (o OBS carrega o SE online)."""
import base64, os

L = "/home/user/twitch-pro/logos/final/"
OUT = "/home/user/twitch-pro/assets/alertas/streamelements/v2/"
os.makedirs(OUT, exist_ok=True)
MINI96 = base64.b64encode(open(L + "mini-96.png", "rb").read()).decode()

CSS = """/* ═══ EXORISERVICE · CSS DO ALERTA (colar na aba CSS — vale para TODOS os 7 tipos) ═══ */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Chakra+Petch:wght@500;600&display=swap');

.xal{--acid:#B4FF00;--toxic:#5C9900;--txt:#F2FFE8;--txt2:#9AA69A;position:relative;display:flex;align-items:center;gap:24px;
 width:860px;padding:22px 36px;background:rgba(6,8,6,.93);border:1px solid rgba(92,153,0,.85);
 clip-path:polygon(20px 0,100% 0,100% calc(100% - 20px),calc(100% - 20px) 100%,0 100%,0 20px);
 font-family:'Chakra Petch',sans-serif;box-shadow:0 0 34px rgba(180,255,0,.14),inset 0 0 30px rgba(23,51,0,.25);
 animation:xin .55s cubic-bezier(.2,.9,.3,1.2) both}
.xal::before{content:'';position:absolute;left:0;top:0;bottom:0;width:6px;
 background:linear-gradient(180deg,var(--acid),var(--toxic));animation:volt 3s steps(3) infinite}
.xal::after{content:'';position:absolute;left:-120%;top:0;bottom:0;width:60%;
 background:linear-gradient(90deg,transparent,rgba(180,255,0,.10),transparent);animation:sweep 2.6s .3s linear infinite}
@keyframes sweep{to{left:160%}}
@keyframes volt{50%{filter:brightness(1.7)}}
@keyframes xin{from{opacity:0;transform:translateX(-90px) skewX(-4deg)}to{opacity:1;transform:none}}
.xal .hexf{position:relative;width:110px;height:110px;flex:0 0 110px;display:flex;align-items:center;justify-content:center}
.xal .hexf img{width:72px;height:72px;position:relative;z-index:2;filter:drop-shadow(0 0 10px rgba(180,255,0,.5))}
.xal .hexf svg{position:absolute;fill:none;stroke:var(--toxic);stroke-width:1.4;stroke-dasharray:10 6;animation:spin 10s linear infinite;opacity:.9}
.xal .hexf svg.b{stroke:var(--acid);stroke-dasharray:2 9;animation:spin 16s linear infinite reverse;opacity:.5}
@keyframes spin{to{transform:rotate(360deg)}}
.xal .mid{flex:1;min-width:0}
.xal .kind{font-size:17px;font-weight:600;letter-spacing:.34em;color:var(--acid);text-transform:uppercase;white-space:nowrap;overflow:hidden}
.xal .name{position:relative;font-family:'Orbitron',sans-serif;font-weight:900;font-size:38px;color:var(--txt);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-shadow:0 0 22px rgba(180,255,0,.25)}
.xal .name::before,.xal .name::after{content:attr(data-t);position:absolute;left:0;top:0;width:100%;opacity:0;pointer-events:none}
.xal .name::before{color:var(--toxic);animation:ng1 3.2s .2s steps(2) infinite}
.xal .name::after{color:rgba(255,255,255,.45);animation:ng2 3.2s .2s steps(2) infinite}
@keyframes ng1{0%,88%,100%{opacity:0}90%{opacity:.85;transform:translate(-4px,-2px);clip-path:inset(10% 0 60% 0)}94%{opacity:.85;transform:translate(3px,1px);clip-path:inset(64% 0 6% 0)}}
@keyframes ng2{0%,88%,100%{opacity:0}91%{opacity:.7;transform:translate(4px,2px);clip-path:inset(58% 0 12% 0)}95%{opacity:.7;transform:translate(-3px,-1px);clip-path:inset(6% 0 62% 0)}}
.xal .msg{font-size:15px;font-weight:500;color:var(--txt2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:3px}
.xal .right{text-align:right;flex:0 0 auto}
.xal .metric{font-family:'Orbitron',sans-serif;font-weight:900;font-size:44px;color:var(--acid);text-shadow:0 0 26px rgba(180,255,0,.45);line-height:1}
.xal .mlabel{font-size:12px;font-weight:600;letter-spacing:.3em;color:var(--txt2);text-transform:uppercase;margin-top:5px}
.xal.raid{border-color:var(--acid);box-shadow:0 0 50px rgba(180,255,0,.30),inset 0 0 30px rgba(23,51,0,.25);animation:xin .55s cubic-bezier(.2,.9,.3,1.2) both,rshake .5s .1s both}
@keyframes rshake{0%{transform:translate(6px,-4px)}25%{transform:translate(-5px,3px)}50%{transform:translate(4px,2px)}75%{transform:translate(-3px,-2px)}100%{transform:none}}
"""

ALERTS = [
    # (tipo-se, arquivo, classe, kind, metrica, label, msg)
    ("follower", "follow", "follow", "novo seguidor", "+1", "seguidor", "seja bem-vindo à comunidade!"),
    ("subscriber", "sub", "sub", "sub novo", "T{{tier}}", "tier", "obrigado pelo apoio!"),
    ("resub", "resub", "resub", "re-sub", "{{months}}", "meses", "{{message}}"),
    ("gift", "gift", "gift", "gift subs", "{{amount}}", "gifts", "obrigado por espalhar a comunidade!"),
    ("bits", "bits", "bits", "bits", "{{amount}}", "bits", "obrigado pelos bits!"),
    ("raid", "raid", "raid", "raid!", "{{viewers}}", "raiders", "que venha a horda! 🐉"),
    ("tip", "tip", "tip", "doação", "{{amount}}", "obrigado!", "{{message}}"),
]

NOME = {"follower": "{{name}}", "subscriber": "{{name}}", "resub": "{{name}}",
        "gift": "{{sender}}", "bits": "{{name}}", "raid": "{{name}}", "tip": "{{name}}"}

for tipo, arq, classe, kind, metrica, label, msg in ALERTS:
    frag = ("<!-- EXORISERVICE · aba HTML do alerta " + tipo.upper() + " (substitua TODO o conteúdo padrão) -->\n"
            '<div class="xal ' + classe + '">\n'
            '  <div class="hexf"><svg width="96" height="96" viewBox="0 0 100 100"><polygon points="50,3 94,27 94,73 50,97 6,73 6,27"/></svg>\n'
            '  <svg class="b" width="110" height="110" viewBox="0 0 100 100"><polygon points="50,3 94,27 94,73 50,97 6,73 6,27"/></svg>\n'
            '  <img src="data:image/png;base64,' + MINI96 + '" alt=""></div>\n'
            '  <div class="mid">\n'
            '    <div class="kind">' + kind + '</div>\n'
            '    <div class="name" data-t="' + NOME[tipo] + '">' + NOME[tipo] + '</div>\n'
            '    <div class="msg">' + msg + '</div>\n'
            '  </div>\n'
            '  <div class="right"><div class="metric">' + metrica + '</div><div class="mlabel">' + label + '</div></div>\n'
            '</div>\n')
    open(OUT + "1-ABA-HTML_" + arq + ".txt", "w").write(frag)
    print("•", "1-ABA-HTML_" + arq + ".txt")

open(OUT + "2-ABA-CSS_geral-para-todos.txt", "w").write(CSS)
print("•", "2-ABA-CSS_geral-para-todos.txt")
print("v2 completa em", OUT)
