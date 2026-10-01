#!/usr/bin/env python3
"""Lote 4B — Pacote de ALERTAS exoriservice (StreamElements).
Gera: preview-alertas.html (demonstração) + 7 arquivos coláveis (HTML box do SE)."""
import base64

F = "/home/user/twitch-pro/assets/fonts/"
L = "/home/user/twitch-pro/logos/final/"
OUT = "/home/user/twitch-pro/assets/alertas/"
import os; os.makedirs(OUT + "streamelements", exist_ok=True)

b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
ORBIT9, C6, C5 = b64(F + "Orbitron-900.ttf"), b64(F + "ChakraPetch-600.ttf"), b64(F + "ChakraPetch-500.ttf")
MINI96 = b64(L + "mini-96.png")

CSS = """
.xal{--acid:#B4FF00;--toxic:#5C9900;--txt:#F2FFE8;--txt2:#9AA69A;position:relative;display:flex;align-items:center;gap:24px;
 width:860px;padding:22px 36px;background:rgba(6,8,6,.93);border:1px solid rgba(92,153,0,.85);
 clip-path:polygon(20px 0,100% 0,100% calc(100% - 20px),calc(100% - 20px) 100%,0 100%,0 20px);
 font-family:'Chakra Petch','Chakra',sans-serif;box-shadow:0 0 34px rgba(180,255,0,.14),inset 0 0 30px rgba(23,51,0,.25);
 animation:xin .55s cubic-bezier(.2,.9,.3,1.2) both,xout .45s 5.5s both}
.xal::before{content:'';position:absolute;left:0;top:0;bottom:0;width:6px;
 background:linear-gradient(180deg,var(--acid),var(--toxic));animation:volt 3s steps(3) infinite}
.xal::after{content:'';position:absolute;left:-120%;top:0;bottom:0;width:60%;
 background:linear-gradient(90deg,transparent,rgba(180,255,0,.10),transparent);animation:sweep 2.6s .3s linear infinite}
@keyframes sweep{to{left:160%}}
@keyframes volt{50%{filter:brightness(1.7)}}
@keyframes xin{from{opacity:0;transform:translateX(-90px) skewX(-4deg)}to{opacity:1;transform:none}}
@keyframes xout{to{opacity:0;transform:translateX(70px) skewX(3deg)}}
.xal .hexf{position:relative;width:92px;height:92px;flex:0 0 92px;display:flex;align-items:center;justify-content:center}
.xal .hexf img{width:64px;height:64px;position:relative;z-index:2;filter:drop-shadow(0 0 10px rgba(180,255,0,.5))}
.xal .hexf svg{position:absolute;inset:0;width:92px;height:92px;fill:none;stroke:var(--toxic);stroke-width:1.4;stroke-dasharray:10 6;animation:spin 10s linear infinite;opacity:.9}
.xal .hexf svg.b{width:110px;height:110px;top:-9px;left:-9px;stroke:var(--acid);stroke-dasharray:2 9;animation:spin 16s linear infinite reverse;opacity:.5}
@keyframes spin{to{transform:rotate(360deg)}}
.xal .mid{flex:1;min-width:0}
.xal .kind{font-size:17px;font-weight:600;letter-spacing:.34em;padding-left:.34em;color:var(--acid);text-transform:uppercase;white-space:nowrap;overflow:hidden}
.xal .name{position:relative;font-family:'Orbitron',sans-serif;font-weight:900;font-size:38px;letter-spacing:.03em;color:var(--txt);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-shadow:0 0 22px rgba(180,255,0,.25)}
.xal .name::before,.xal .name::after{content:attr(data-t);position:absolute;left:0;top:0;width:100%;opacity:0;pointer-events:none}
.xal .name::before{color:var(--toxic);animation:ng1 3.2s .2s steps(2) infinite}
.xal .name::after{color:rgba(255,255,255,.45);animation:ng2 3.2s .2s steps(2) infinite}
@keyframes ng1{0%,88%,100%{opacity:0}90%{opacity:.85;transform:translate(-4px,-2px);clip-path:inset(10% 0 60% 0)}94%{opacity:.85;transform:translate(3px,1px);clip-path:inset(64% 0 6% 0)}}
@keyframes ng2{0%,88%,100%{opacity:0}91%{opacity:.7;transform:translate(4px,2px);clip-path:inset(58% 0 12% 0)}95%{opacity:.7;transform:translate(-3px,-1px);clip-path:inset(6% 0 62% 0)}}
.xal .msg{font-size:15px;font-weight:500;color:var(--txt2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:3px}
.xal .right{text-align:right;flex:0 0 auto}
.xal .metric{font-family:'Orbitron',sans-serif;font-weight:900;font-size:44px;color:var(--acid);text-shadow:0 0 26px rgba(180,255,0,.45);line-height:1}
.xal .mlabel{font-size:12px;font-weight:600;letter-spacing:.3em;color:var(--txt2);text-transform:uppercase;margin-top:5px}
.xal.raid{border-color:var(--acid);box-shadow:0 0 50px rgba(180,255,0,.30),inset 0 0 30px rgba(23,51,0,.25);animation:xin .55s cubic-bezier(.2,.9,.3,1.2) both,rshake .5s .1s both,xout .45s 5.5s both}
@keyframes rshake{0%{transform:translate(6px,-4px)}25%{transform:translate(-5px,3px)}50%{transform:translate(4px,2px)}75%{transform:translate(-3px,-2px)}100%{transform:none}}
/* ── modo preview (loop) ── */
.xal.loop{animation:xloop 8s cubic-bezier(.2,.9,.3,1.2) infinite}
@keyframes xloop{0%{opacity:0;transform:translateX(-90px) skewX(-4deg)}7%,88%{opacity:1;transform:none}100%{opacity:0;transform:translateX(70px) skewX(3deg)}}
"""

ALERTS = [
    # (arquivo, classe, kind, html_nome, metrica_html, label, texto SE "Alert Text" sugerido)
    ("follow", "follow", "novo seguidor",
     '<div class="name" data-t="{{name}}">{{name}}</div>',
     '<div class="metric">+1</div><div class="mlabel">seguidor</div>', None),
    ("sub", "sub", "sub novo",
     '<div class="name" data-t="{{name}}">{{name}}</div>',
     '<div class="metric">T{{tier}}</div><div class="mlabel">tier</div>', None),
    ("resub", "resub", "re-sub",
     '<div class="name" data-t="{{name}}">{{name}}</div>',
     '<div class="metric">{{months}}</div><div class="mlabel">meses</div>', None),
    ("gift", "gift", "gift subs",
     '<div class="name" data-t="{{sender}}">{{sender}}</div>',
     '<div class="metric">{{amount}}</div><div class="mlabel">gifts</div>', None),
    ("bits", "bits", "bits",
     '<div class="name" data-t="{{name}}">{{name}}</div>',
     '<div class="metric">{{amount}}</div><div class="mlabel">bits</div>', None),
    ("raid", "raid", "raid!",
     '<div class="name" data-t="{{name}}">{{name}}</div>',
     '<div class="metric">{{viewers}}</div><div class="mlabel">raiders</div>', None),
    ("tip", "tip", "doação",
     '<div class="name" data-t="{{name}}">{{name}}</div>',
     '<div class="metric">{{amount}}</div><div class="mlabel">obrigado!</div>', None),
]

def bloco(classe, kind, nome_html, right_html, loop=False, nome_demo="Viewer"):
    cls = ("xal " + classe + (" loop" if loop else "")).strip()
    nome = nome_demo if loop else nome_html
    dt = nome_demo if loop else None
    inner = nome if loop else nome_html
    return ('<div class="' + cls + '">'
            '<div class="hexf"><svg viewBox="0 0 100 100"><polygon points="50,3 94,27 94,73 50,97 6,73 6,27"/></svg>'
            '<svg class="b" viewBox="0 0 100 100"><polygon points="50,3 94,27 94,73 50,97 6,73 6,27"/></svg>'
            '<img src="data:image/png;base64,' + MINI96 + '" alt=""></div>'
            '<div class="mid"><div class="kind">' + kind + '</div>' + inner +
            '<div class="msg">' + ("seja bem-vindo à comunidade!" if classe == "follow" else "obrigado pelo apoio!") + '</div></div>'
            '<div class="right">' + right_html.replace("{{", "").replace("}}", "") + '</div></div>')

# ── arquivos coláveis no StreamElements (HTML box) ──
DEMOS = {"follow": "+1", "sub": "T1", "resub": "6", "gift": "5", "bits": "500", "raid": "42", "tip": "50"}
for arq, classe, kind, nome_html, right_html, _ in ALERTS:
    right_demo = right_html
    for var, val in [("+1", "+1"), ("T{{tier}}", "T1"), ("{{months}}", "6"), ("{{amount}}", "500" if classe in ("bits",) else ("5" if classe == "gift" else "50")), ("{{viewers}}", "42")]:
        right_demo = right_demo.replace(var, val)
    demo = bloco(classe, kind, nome_html, right_html, loop=True)
    html = ("<!-- ALERTA " + classe.upper() + " — exoriservice · colar no campo HTML do alert (StreamElements) -->\n"
            "<style>" + CSS.replace(".xal.loop{animation:xloop 8s cubic-bezier(.2,.9,.3,1.2) infinite}",
                                    "").replace("@keyframes xloop{0%{opacity:0;transform:translateX(-90px) skewX(-4deg)}7%,88%{opacity:1;transform:none}100%{opacity:0;transform:translateX(70px) skewX(3deg)}}", "")
            + "</style>\n"
            + bloco(classe, kind, nome_html, right_html).replace("<div class=\"msg\">obrigado pelo apoio!</div>",
                 "<div class=\"msg\">{{message}}</div>" if classe in ("tip", "resub") else "<div class=\"msg\">obrigado pelo apoio!</div>")
            + "\n")
    open(OUT + "streamelements/alerta-" + arq + ".html", "w").write(html)

# ── preview geral ──
rows = []
labels = {"follow": ("NOVO SEGUIDOR", "+1", "seguidor"), "sub": ("SUB NOVO", "T1", "tier"),
          "resub": ("RE-SUB", "6", "meses"), "gift": ("GIFT SUBS", "5", "gifts"),
          "bits": ("BITS", "500", "bits"), "raid": ("RAID!", "42", "raiders"), "tip": ("DOAÇÃO", "50", "obrigado!")}
nomes = ["NovoViewer", "Subber", "Veterano", "Presenteador", "BitLord", "RaidMaster", "Apoiador"]
for i, (arq, classe, kind, _, rh, _) in enumerate(ALERTS):
    k, m, ml = labels[arq]
    right = '<div class="metric">' + m + '</div><div class="mlabel">' + ml + '</div>'
    nome = '<div class="name" data-t="' + nomes[i] + '">' + nomes[i] + '</div>'
    b = blobo = bloco(classe, k.lower(), nome, right, loop=True)
    rows.append(b)

preview = ("<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>Alertas — exoriservice</title><style>"
           + CSS
           + "@font-face{font-family:Orbitron;font-weight:900;src:url(data:font/ttf;base64," + ORBIT9 + ") format('truetype')}"
           + "@font-face{font-family:Chakra;font-weight:600;src:url(data:font/ttf;base64," + C6 + ") format('truetype')}"
           + "@font-face{font-family:Chakra;font-weight:500;src:url(data:font/ttf;base64," + C5 + ") format('truetype')}"
           + "body{background:#060806;display:flex;flex-direction:column;align-items:center;gap:30px;padding:50px 20px;font-family:'Chakra',monospace}"
           + "h1{font-family:'Orbitron';font-weight:900;color:#F2FFE8;font-size:26px;letter-spacing:.1em}"
           + "h1 b{color:#B4FF00}.cap{color:#9AA69A;font-size:14px;letter-spacing:.2em;margin-top:-22px}"
           + ".xal{position:relative}"
           + "</style></head><body><h1><b>EXORI</b>SERVICE · ALERTAS</h1><div class='cap'>PREVIEW — 7 TIPOS · BANNER MÉDIO UNIFORME</div>"
           + "".join(rows) + "</body></html>")
open(OUT + "preview-alertas.html", "w").write(preview)
print("preview-alertas.html ok")
for f in sorted(os.listdir(OUT + "streamelements")):
    print(" • streamelements/" + f)
