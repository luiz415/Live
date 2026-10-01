#!/usr/bin/env python3
"""COBERTURA DE PRIVACIDADE — fundo escuro UNIFORME (cor única) para tampar o chat do jogo
na cena Gameplay. Redimensionável: o painel preenche TODO o canvas da fonte,
então basta alterar largura/altura no OBS (ou arrastar) para o tamanho exato."""
import base64

F = "/home/user/twitch-pro/assets/fonts/"
L = "/home/user/twitch-pro/logos/final/"
OUT = "/home/user/twitch-pro/assets/overlay/"

b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
MINI96 = b64(L + "mini-96.png")

HEXSVG = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='56' height='100' viewBox='0 0 56 100'>"
          "<path d='M28 0L56 16v34L28 66 0 50V16z M28 66l28 17v33M28 66L0 83v33' fill='none' stroke='%23142807' stroke-opacity='0.55' stroke-width='1'/></svg>")

HTML = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Cobertura · Chat do Jogo — exoriservice</title><style>
:root{--acid:#B4FF00;--toxic:#5C9900}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:transparent}

/* ══ O PAINEL É O PRÓPRIO CANVAS: redimensione a fonte no OBS ══ */
.cover{position:fixed;inset:0;
 /* PRIVACIDADE TOTAL: cor ÚNICA e bem escura em toda a área — o chat do jogo
    fica invisível pros espectadores (sem degradê, sem transparência) */
 background:rgba(6,8,6,.98)}
.mesh{position:fixed;inset:0;background-image:url("@@HEXSVG@@");background-size:112px 200px;opacity:.32}
.edge{position:fixed;left:0;right:0;top:14%;height:2px;
 background:linear-gradient(90deg,transparent,rgba(180,255,0,.55) 30%,rgba(92,153,0,.35) 70%,transparent);
 box-shadow:0 0 12px rgba(180,255,0,.28)}
.mark{position:fixed;right:12px;bottom:10px;display:flex;align-items:center;gap:8px;opacity:.5}
.mark img{width:26px;height:26px;filter:grayscale(.2) brightness(1.1)}
.mark span{font-family:Chakra,monospace;font-size:11px;letter-spacing:.22em;color:#9AA69A}
.scan{position:fixed;left:0;right:0;height:70px;top:-80px;
 background:linear-gradient(180deg,transparent,rgba(180,255,0,.05),transparent);
 animation:scan 9s linear infinite}
@keyframes scan{to{transform:translateY(120vh)}}
</style></head><body>
<div class="cover" id="cover"><div class="mesh"></div></div>
<div class="edge" id="edge"></div>
<div class="scan" id="scan"></div>
<div class="mark" id="mark"><img src="data:image/png;base64,@@ICON@@" alt=""><span>EXORISERVICE</span></div>
<script>
/* ═══ CONFIGURAÇÃO RÁPIDA (edite aqui) ═══
   forca ......... 0 a 1 — opacidade da cor única do fundo (padrão .98)
   borda ......... true/false — filete verde no topo do painel
   varredura .... true/false — brilho lento descendo (elegância extra)
   marca ......... true/false — mini-assinatura no canto            */
const CFG={forca:.98,borda:true,varredura:true,marca:true};

const c=document.getElementById('cover');
c.style.background=`rgba(6,8,6,${CFG.forca})`;
document.getElementById('edge').style.display=CFG.borda?'':'none';
document.getElementById('scan').style.display=CFG.varredura?'':'none';
document.getElementById('mark').style.display=CFG.marca?'':'none';
</script></body></html>"""

html = HTML.replace("@@HEXSVG@@", HEXSVG).replace("@@ICON@@", MINI96)
open(OUT + "cobertura-chat.html", "w").write(html)
print("cobertura-chat.html ok (" + str(len(html) // 1024) + " KB)")
