#!/usr/bin/env python3
"""Telas & widgets HTML — v3 AGRESSIVA + Party Tracker Tibia (editável ao vivo).
Autônomo: fontes/logo em base64. Alinhamentos corrigidos (compensação de tracking)."""
import base64

F = "/home/user/twitch-pro/assets/fonts/"
L = "/home/user/twitch-pro/logos/final/"
OUT = "/home/user/twitch-pro/assets/"

b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
ORBIT9, C6, C5 = b64(F + "Orbitron-900.ttf"), b64(F + "ChakraPetch-600.ttf"), b64(F + "ChakraPetch-500.ttf")
ICON256, MINI96 = b64(L + "icone-256.png"), b64(L + "mini-96.png")

HEXSVG = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='56' height='100' viewBox='0 0 56 100'>"
          "<path d='M28 0L56 16v34L28 66 0 50V16z M28 66l28 17v33M28 66L0 83v33' fill='none' stroke='%23142807' stroke-opacity='0.5' stroke-width='1'/></svg>")
GRAIN = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/></filter>"
         "<rect width='100%25' height='100%25' filter='url(%23n)' opacity='0.55'/></svg>")

# ══════════════════════ TELAS v3 ══════════════════════
TEMPLATE = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>@@TITULO@@ — exoriservice</title><style>
@font-face{font-family:Orbitron;font-weight:900;src:url(data:font/ttf;base64,@@ORBIT9@@) format('truetype')}
@font-face{font-family:Chakra;font-weight:600;src:url(data:font/ttf;base64,@@C6@@) format('truetype')}
@font-face{font-family:Chakra;font-weight:500;src:url(data:font/ttf;base64,@@C5@@) format('truetype')}
:root{--acid:#B4FF00;--toxic:#5C9900;--txt:#F2FFE8;--txt2:#9AA69A;--bg:#060806}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:var(--bg);font-family:Chakra,monospace}

/* ══ FUNDO ══ */
.hexbg{position:fixed;inset:-120px;background-image:url("@@HEXSVG@@");background-size:112px 200px;opacity:.5;animation:drift 26s linear infinite}
.hexbg.b{animation:driftb 38s linear infinite;opacity:.28;filter:blur(1px)}
@keyframes drift{to{transform:translate(112px,200px)}}
@keyframes driftb{to{transform:translate(-112px,-200px)}}
#rain{position:fixed;inset:0;z-index:1}
.core{position:fixed;left:50%;top:44%;width:1100px;height:1100px;transform:translate(-50%,-50%);
  background:radial-gradient(circle,rgba(23,51,0,.42) 0%,rgba(92,153,0,.10) 38%,transparent 68%);animation:corepulse 5.2s ease-in-out infinite}
@keyframes corepulse{50%{opacity:.55;transform:translate(-50%,-50%) scale(1.06)}}
.beam{position:fixed;top:-25%;height:150%;width:240px;transform:skewX(-18deg) translateX(-40vw);
  background:linear-gradient(90deg,transparent,rgba(180,255,0,.055),transparent);animation:beam 7.5s linear infinite}
.beam.b2{width:380px;animation-duration:12s;animation-delay:-6s;opacity:.6}
.beam.b3{width:140px;animation-duration:5.5s;animation-delay:-2.5s;opacity:.8}
@keyframes beam{to{transform:skewX(-18deg) translateX(150vw)}}
.scan{position:fixed;left:0;right:0;top:-170px;height:150px;
  background:linear-gradient(180deg,transparent,rgba(180,255,0,.05),transparent);animation:scan 8s linear infinite;z-index:2}
.scan.s2{height:60px;top:-70px;animation-duration:4.6s;animation-delay:-2s;opacity:.7}
.scan.s3{height:260px;top:-280px;animation-duration:13s;animation-delay:-7s;opacity:.4}
@keyframes scan{to{transform:translateY(1360px)}}
.grain{position:fixed;inset:-40px;background-image:url("@@GRAIN@@");opacity:.05;animation:grain 1.1s steps(4) infinite;z-index:2}
@keyframes grain{0%{transform:translate(0,0)}25%{transform:translate(-14px,9px)}50%{transform:translate(11px,-13px)}75%{transform:translate(-7px,-8px)}100%{transform:translate(0,0)}}
.vig{position:fixed;inset:0;background:radial-gradient(ellipse at 50% 44%,transparent 34%,rgba(0,0,0,.66) 100%);z-index:2}
.edge{position:fixed;inset:0;border:1px solid rgba(180,255,0,.4);z-index:2;pointer-events:none}

/* ══ RASGOS VHS ══ */
.tear{position:fixed;left:0;right:0;height:4px;background:rgba(180,255,0,.16);box-shadow:0 0 14px rgba(180,255,0,.28);opacity:0;z-index:3;animation:tear 9s linear infinite}
.tear.t1{top:18%}.tear.t2{top:64%;height:2px;animation-duration:6.5s;animation-delay:-3s}
.tear.t3{top:38%;height:8px;animation-duration:12s;animation-delay:-7s;background:rgba(242,255,232,.07)}
@keyframes tear{0%,4.4%{opacity:0;transform:translateX(-40px)}4.6%{opacity:1;transform:translateX(-24px)}5%{transform:translateX(18px)}5.4%,100%{opacity:0;transform:translateX(30px)}}

/* ══ RÉGUAS DE TICKS ══ */
.ruler{position:fixed;left:0;right:0;height:9px;z-index:2;background:repeating-linear-gradient(90deg,rgba(180,255,0,.22) 0 2px,transparent 2px 84px)}
.ruler.top{top:16px}.ruler.bot{bottom:16px;background:repeating-linear-gradient(90deg,rgba(180,255,0,.15) 0 2px,transparent 2px 118px)}

/* ══ BARRAS DE ENERGIA ══ */
.flow{position:fixed;left:0;right:0;height:7px;z-index:4;
  background:linear-gradient(90deg,transparent 0%,var(--acid) 25%,var(--toxic) 50%,var(--acid) 75%,transparent 100%);
  background-size:200% 100%;animation:flow 3.2s linear infinite,volt 5.5s steps(3) infinite;box-shadow:0 0 22px rgba(180,255,0,.5)}
.flow.top{top:0}.flow.bot{bottom:0;height:5px;animation-duration:4.1s,7s;animation-direction:reverse,normal}
@keyframes flow{to{background-position:-200% 0}}
@keyframes volt{50%{filter:brightness(1.5)}75%{filter:brightness(.8)}}

/* ══ BRACKETS ══ */
.corner{position:fixed;width:70px;height:70px;z-index:4;border:2px solid rgba(180,255,0,.55);animation:cpulse 2.6s ease-in-out infinite}
.c-tl{top:20px;left:20px;border-right:0;border-bottom:0}
.c-tr{top:20px;right:20px;border-left:0;border-bottom:0;animation-delay:.4s}
.c-bl{bottom:20px;left:20px;border-right:0;border-top:0;animation-delay:.8s}
.c-br{bottom:20px;right:20px;border-left:0;border-top:0;animation-delay:1.2s}
@keyframes cpulse{50%{opacity:.35;transform:scale(.92)}}

/* ══ SHARDS / PARTÍCULAS ══ */
.shard{position:fixed;bottom:-90px;pointer-events:none;animation:rise linear infinite;z-index:1}
@keyframes rise{to{transform:translateY(-120vh) rotate(170deg);opacity:0}}
.dot{position:fixed;border-radius:50%;background:var(--acid);pointer-events:none;z-index:1;animation:dotup linear infinite,twinkle 2.3s ease-in-out infinite}
@keyframes dotup{to{transform:translateY(-114vh)}}
@keyframes twinkle{50%{opacity:.15}}

/* ══ PALCO ══ */
.stage{position:fixed;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;z-index:3}
.embwrap{position:relative;width:300px;height:300px;display:flex;align-items:center;justify-content:center}
.emblem{width:200px;height:200px;animation:breathe 4.2s ease-in-out infinite;position:relative;z-index:2}
@keyframes breathe{
 0%,100%{filter:drop-shadow(-3px 0 0 rgba(92,153,0,.30)) drop-shadow(3px 0 0 rgba(180,255,0,.20)) drop-shadow(0 0 24px rgba(180,255,0,.30))}
 50%{filter:drop-shadow(-6px 0 0 rgba(92,153,0,.5)) drop-shadow(6px 0 0 rgba(180,255,0,.32)) drop-shadow(0 0 52px rgba(180,255,0,.55));transform:scale(1.03)}}
.ring{position:absolute;fill:none;opacity:.55}
.r1{width:232px;height:232px;animation:spin 14s linear infinite;stroke:var(--toxic);stroke-width:1.2;stroke-dasharray:12 7}
.r2{width:268px;height:268px;animation:spin 22s linear infinite reverse;stroke:var(--acid);stroke-width:.9;stroke-dasharray:4 10;opacity:.4}
.r3{width:300px;height:300px;animation:spin 9s linear infinite;stroke:rgba(154,166,154,.5);stroke-width:.7;stroke-dasharray:1 14;opacity:.5}
@keyframes spin{to{transform:rotate(360deg)}}

/* ══ WORDMARK + GLITCH ══ */
.wm{position:relative;font-family:Orbitron;font-weight:900;font-size:62px;letter-spacing:.085em;padding-left:.085em;color:var(--txt);animation:fadeup .7s .1s both}
.wm b{color:var(--acid);text-shadow:0 0 26px rgba(180,255,0,.55)}
.wm::before,.wm::after{content:attr(data-text);position:absolute;left:0;top:0;width:100%;opacity:0;pointer-events:none}
.wm::before{color:var(--toxic)}
.wm::after{color:rgba(255,255,255,.4)}
body.glitching .wm::before{opacity:.85;animation:g1 .22s steps(2) both}
body.glitching .wm::after{opacity:.7;animation:g2 .22s steps(2) both}
@keyframes g1{0%{transform:translate(-4px,-2px);clip-path:inset(12% 0 58% 0)}50%{transform:translate(3px,1px);clip-path:inset(62% 0 8% 0)}100%{transform:none;clip-path:inset(40% 0 40% 0)}}
@keyframes g2{0%{transform:translate(4px,2px);clip-path:inset(58% 0 12% 0)}50%{transform:translate(-3px,-1px);clip-path:inset(8% 0 62% 0)}100%{transform:none;clip-path:inset(40% 0 40% 0)}}
body.glitching .stage{animation:stagejit .22s steps(2) both}
@keyframes stagejit{50%{transform:translate(3px,-2px) skewX(.35deg)}}
body.glitching .emblem{animation:eshake .22s steps(2) both}
@keyframes eshake{33%{transform:translate(-5px,2px);filter:drop-shadow(6px 0 0 rgba(92,153,0,.6))}66%{transform:translate(4px,-3px);filter:drop-shadow(-6px 0 0 rgba(180,255,0,.5))}}
body.glitching #rain{animation:rainjit .22s steps(2) both}
@keyframes rainjit{50%{transform:translateX(9px)}}

/* ══ TEXTOS (alinhamento compensado) ══ */
.status{font-size:27px;font-weight:600;letter-spacing:.55em;text-indent:.55em;color:var(--txt2);text-transform:uppercase;white-space:nowrap;animation:fadeup .7s .2s both,flick 6.5s 1.5s ease-in-out infinite}
@keyframes flick{48%{opacity:1}50%{opacity:.35}52%{opacity:1}83%{opacity:1}84%{opacity:.55}85%{opacity:1}}
.sub{font-size:26px;font-weight:500;color:var(--txt2);animation:fadeup .7s .3s both}
.count{font-family:Orbitron;font-weight:900;font-size:128px;color:var(--acid);font-variant-numeric:tabular-nums;letter-spacing:.04em;padding-left:.04em;animation:fadeup .7s .25s both;
 text-shadow:-2px 0 0 rgba(92,153,0,.25),2px 0 0 rgba(242,255,232,.18),0 0 40px rgba(180,255,0,.42)}
.count.tick{animation:tickpulse 1s ease-out both}
@keyframes tickpulse{0%{transform:scale(1.06);text-shadow:-6px 0 0 rgba(92,153,0,.9),6px 0 0 rgba(242,255,232,.65),0 0 80px rgba(180,255,0,.85)}
 100%{transform:scale(1);text-shadow:-2px 0 0 rgba(92,153,0,.25),2px 0 0 rgba(242,255,232,.18),0 0 40px rgba(180,255,0,.42)}}
.count.end{font-size:54px;letter-spacing:.14em;padding-left:.14em;text-shadow:0 0 34px rgba(180,255,0,.7)}
.chips{display:flex;flex-wrap:wrap;justify-content:center;gap:16px;animation:fadeup .7s .45s both}
.chip{border:1px solid var(--toxic);background:rgba(18,23,18,.86);color:var(--txt);padding:10px 22px;font-size:20px;font-weight:600;letter-spacing:.12em;padding-left:calc(22px + .12em);clip-path:polygon(11px 0,100% 0,100% calc(100% - 11px),calc(100% - 11px) 100%,0 100%,0 11px)}
.chip b{color:var(--acid)}
@keyframes fadeup{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}

/* ══ IGNIÇÃO ══ */
.flash{position:fixed;inset:0;z-index:9;opacity:0;pointer-events:none;background:radial-gradient(circle at 50% 45%,rgba(180,255,0,.32) 0%,transparent 62%)}
body.ignite .flash{animation:flash .95s ease-out both}
@keyframes flash{0%{opacity:1}100%{opacity:0}}
body.ignite .stage{animation:shake .55s ease-out}
@keyframes shake{0%{transform:translate(7px,-5px)}20%{transform:translate(-6px,4px)}40%{transform:translate(5px,3px) skewX(.4deg)}60%{transform:translate(-4px,-2px)}80%{transform:translate(2px,1px)}100%{transform:none}}
body.ignite .r1{animation-duration:1.2s}
body.ignite .r2{animation-duration:2s}
body.ignite .r3{animation-duration:.7s}
body.ignite .flow{animation-duration:.9s,1.1s}
body.ignite .beam{animation-duration:1.8s}
body.ignite .scan{animation-duration:2.2s}
.strobe{position:fixed;inset:0;background:#F2FFE8;opacity:0;z-index:8;pointer-events:none}
/* faixa inferior (6,8vh) reservada ao TICKER · Comandos — nenhum efeito ali */
.fx{position:fixed;inset:0 0 6.8vh 0;overflow:hidden;transform:translateZ(0);z-index:0}
</style></head><body>
<div class="fx">
<div class="hexbg"></div><div class="hexbg b"></div><canvas id="rain"></canvas><div class="core"></div>
<div class="edge"></div>
<div class="beam"></div><div class="beam b2"></div><div class="beam b3"></div>
<div class="scan"></div><div class="scan s2"></div><div class="scan s3"></div>
<div class="tear t1"></div><div class="tear t2"></div><div class="tear t3"></div>
<div class="grain"></div><div class="vig"></div>
<div class="ruler top"></div><div class="ruler bot"></div>
<div class="flow top"></div><div class="flow bot"></div>
<div class="corner c-tl"></div><div class="corner c-tr"></div><div class="corner c-bl"></div><div class="corner c-br"></div>
<div class="flash"></div><div class="strobe" id="strobe"></div>
</div>
<div class="stage">
  <div class="embwrap">
    <svg class="ring r1" viewBox="0 0 100 100"><polygon points="50,3 94,27 94,73 50,97 6,73 6,27"/></svg>
    <svg class="ring r2" viewBox="0 0 100 100"><polygon points="50,3 94,27 94,73 50,97 6,73 6,27"/></svg>
    <svg class="ring r3" viewBox="0 0 100 100"><polygon points="50,3 94,27 94,73 50,97 6,73 6,27"/></svg>
    <img class="emblem" src="data:image/png;base64,@@ICON@@" alt="">
  </div>
  <div class="wm" data-text="EXORISERVICE"><b>EXORI</b>SERVICE</div>
  <div class="status" id="status">@@STATUS@@</div>
  @@BLOCO_MEIO@@
  <div class="chips">@@CHIPS@@</div>
</div>
<script>
/* ── scramble/decrypt no status ── */
(function(){const el=document.getElementById('status'),txt=el.textContent.trim();
const chars='▓▒░<>/[]#*+—EXORISVC0147';let f=0,T=34;
const iv=setInterval(()=>{f++;let o='';
for(let i=0;i<txt.length;i++){o+=(i/txt.length<f/T)?txt[i]:chars[Math.floor(Math.random()*chars.length)]}
el.textContent=o;if(f>=T){el.textContent=txt;clearInterval(iv)}},33)})();

/* ── chuva digital de glifos ── */
(function(){const cv=document.getElementById('rain'),cx=cv.getContext('2d');
function rs(){cv.width=innerWidth;cv.height=innerHeight}rs();addEventListener('resize',rs);
const CH='EXORISVC0147▓▒░<>/[]#*+',drops=[];
const cols=Math.ceil(innerWidth/90);
for(let i=0;i<cols;i++)drops[i]={x:i*90+30,y:Math.random()*innerHeight,s:1.2+Math.random()*2.4,n:6+Math.floor(Math.random()*9)};
setInterval(()=>{cx.clearRect(0,0,cv.width,cv.height);
for(const d of drops){for(let k=0;k<d.n;k++){const yy=d.y-k*22;if(yy<-20||yy>cv.height)continue;
const a=k===0?.30:.26*(1-k/d.n);cx.fillStyle='rgba(180,255,0,'+a+')';cx.font=(k===0?'15px':'13px')+' monospace';
cx.fillText(CH[Math.floor(Math.random()*CH.length)],d.x,yy)}
d.y+=d.s*8;if(d.y-d.n*22>cv.height){d.y=-30;d.x=Math.floor(Math.random()*cols)*90+30}}},46)})();

/* ── shards em profundidade ── */
var FX=document.querySelector('.fx');
for(let i=0;i<26;i++){const s=document.createElement('div');s.className='shard';
const size=6+Math.random()*26,deep=Math.random()<.35;
const cl=[['#B4FF00',.32],['#5C9900',.26],['#173300',.55]][i%3];
s.style.cssText='left:'+(Math.random()*100)+'%;border-left:'+size+'px solid transparent;'+
'border-right:'+size+'px solid transparent;border-bottom:'+(size*1.75)+'px solid '+cl[0]+';opacity:'+cl[1]+';'+
'animation-duration:'+(7+Math.random()*13)+'s;animation-delay:-'+(Math.random()*18)+'s;'+
(deep?'filter:blur(2.5px);':'');
FX.appendChild(s)}

/* ── partículas ── */
for(let i=0;i<22;i++){const p=document.createElement('div');p.className='dot';
const sz=2+Math.random()*3.5;
p.style.cssText='left:'+(Math.random()*100)+'%;bottom:-10px;width:'+sz+'px;height:'+sz+'px;'+
'box-shadow:0 0 '+(sz*3)+'px rgba(180,255,0,.8);opacity:'+(.3+Math.random()*.5)+';'+
'animation-duration:'+(9+Math.random()*14)+'s,'+(1.5+Math.random()*2)+'s;animation-delay:-'+(Math.random()*20)+'s,0s';
FX.appendChild(p)}

/* ── glitch ambiente + strobe ── */
(function amb(){setTimeout(()=>{document.body.classList.add('glitching');
setTimeout(()=>document.body.classList.remove('glitching'),230);amb()},4200+Math.random()*5200)})();
(function st(){setTimeout(()=>{const s=document.getElementById('strobe');let n=0;
const iv=setInterval(()=>{s.style.opacity=n%2?0:.08;if(++n>5){clearInterval(iv);s.style.opacity=0}},55);st()},7000+Math.random()*6000)})();
@@JS_EXTRA@@
</script></body></html>"""

def tela(nome, titulo, status, meio, chips, js_extra=""):
    chips_html = "".join('<div class="chip">' + c + "</div>" for c in chips)
    html = (TEMPLATE.replace("@@TITULO@@", titulo).replace("@@STATUS@@", status)
            .replace("@@BLOCO_MEIO@@", meio).replace("@@CHIPS@@", chips_html)
            .replace("@@JS_EXTRA@@", js_extra).replace("@@ORBIT9@@", ORBIT9)
            .replace("@@C6@@", C6).replace("@@C5@@", C5).replace("@@ICON@@", ICON256)
            .replace("@@HEXSVG@@", HEXSVG).replace("@@GRAIN@@", GRAIN))
    open(OUT + "telas/" + nome + ".html", "w").write(html)
    print(nome + ".html ok (" + str(len(html) // 1024) + " KB)")

JS_COUNT = """const q=new URLSearchParams(location.search);
let left=(parseFloat(q.get('t'))||10)*60;
const el=document.getElementById('count');
setInterval(()=>{if(left>0){left--;
const m=String(Math.floor(left/60)).padStart(2,'0'),s=String(left%60).padStart(2,'0');
el.textContent=m+':'+s;el.classList.remove('tick');void el.offsetWidth;el.classList.add('tick');
if(left===0){el.classList.add('end');el.textContent='JÁ VAI COMEÇAR';document.body.classList.add('ignite');}}},1000);"""

tela("starting-soon", "Starting Soon", "iniciando em",
     '<div class="count" id="count">10:00</div>',
     ['<b>SEG–SÁB</b>&nbsp;·&nbsp;08H–22H', 'TIBIA&nbsp;·&nbsp;RUBINOT'], js_extra=JS_COUNT)
tela("brb", "Pausa", "pausa rápida", '<div class="sub">já volto</div>', [])
tela("encerramento", "Encerramento", "obrigado pela live",
     '<div class="sub">até segunda, 08h</div>',
     ['<b>SEG–SÁB</b>&nbsp;·&nbsp;08H–22H', 'TIBIA&nbsp;·&nbsp;RUBINOT'])

# (Party Tracker movido para produzir_party.py — layout horizontal)

# ══════════════════════ OVERLAY (gameplay) ══════════════════════
OVERLAY = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Overlay Gameplay — exoriservice</title><style>
@font-face{font-family:Orbitron;font-weight:900;src:url(data:font/ttf;base64,@@ORBIT9@@) format('truetype')}
@font-face{font-family:Chakra;font-weight:600;src:url(data:font/ttf;base64,@@C6@@) format('truetype')}
@font-face{font-family:Chakra;font-weight:500;src:url(data:font/ttf;base64,@@C5@@) format('truetype')}
:root{--acid:#B4FF00;--toxic:#5C9900;--txt:#F2FFE8;--txt2:#9AA69A}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:transparent;font-family:Chakra,monospace}
.edge{position:fixed;inset:0 0 6.8vh 0;border:1px solid rgba(180,255,0,.35);border-bottom:none;pointer-events:none}
/* ── QUADRO DA MARCA — móvel/ajustável (tecla E) + efeitos: cometa na borda, glow e shimmer ── */
@property --ma{syntax:'<angle>';initial-value:0deg;inherits:false}
.head{position:fixed;left:32px;bottom:calc(6.8vh + 14px);display:flex;align-items:center;gap:12px;
 padding:9px 18px 9px 14px;background:rgba(6,8,6,.82);cursor:default;
 clip-path:polygon(10px 0,100% 0,100% calc(100% - 10px),calc(100% - 10px) 100%,0 100%,0 10px);
 animation:hglow 3.4s ease-in-out infinite;
 transform:scale(var(--ms,1));transform-origin:left center;will-change:transform}
@keyframes hglow{50%{box-shadow:0 0 26px rgba(180,255,0,.28)}}
.head::before{content:'';position:absolute;inset:0;padding:2px;pointer-events:none;
 background:conic-gradient(from var(--ma),transparent 0deg 170deg,rgba(180,255,0,.16) 170deg,
  rgba(180,255,0,.95) 344deg,#F4FFD0 351deg,rgba(180,255,0,.95) 354deg,transparent 360deg);
 -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
 mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
 -webkit-mask-composite:xor;mask-composite:exclude;
 filter:drop-shadow(0 0 5px rgba(180,255,0,.65));animation:ma 5s linear infinite}
@keyframes ma{to{--ma:360deg}}
.head img{width:46px;height:46px;filter:drop-shadow(0 0 10px rgba(180,255,0,.45));animation:himg 2.6s ease-in-out infinite}
@keyframes himg{50%{transform:scale(1.06)}}
.head .name{position:relative;font-family:Orbitron;font-weight:900;font-size:20px;letter-spacing:.18em;color:var(--txt);text-shadow:0 2px 8px rgba(0,0,0,.8);white-space:nowrap}
.head .name b{color:var(--acid)}
.head .name::after{content:'';position:absolute;inset:0;pointer-events:none;
 background:linear-gradient(105deg,transparent 20%,rgba(244,255,208,.55) 50%,transparent 80%);
 background-size:250% 100%;animation:hshim 4.5s ease-in-out infinite;mix-blend-mode:screen}
@keyframes hshim{0%{background-position:130% 0}55%,100%{background-position:-130% 0}}
.editing .head{cursor:grab;outline:2px dashed rgba(180,255,0,.9);outline-offset:4px;animation:none}
.editing .head:active{cursor:grabbing}
.mbar{position:fixed;top:12px;left:50%;transform:translateX(-50%);display:none;z-index:9;
 align-items:center;gap:8px;background:rgba(6,8,6,.95);border:1px solid var(--acid);
 padding:8px 12px;white-space:nowrap}
.editing .mbar{display:flex}
.mbar .lbl{color:#9AA69A;font-size:11px;letter-spacing:.05em}
.mbar button{width:32px;height:32px;border:0;background:var(--acid);color:#060806;
 font:700 17px/32px monospace;cursor:pointer;padding:0}
.mbar button:active{transform:scale(.92)}
.mbar input[type=range]{width:170px;accent-color:var(--acid);cursor:pointer}
.mbar .val{color:var(--acid);font:600 13px/1 monospace;min-width:44px;text-align:center}
.mbar .rst{width:auto;padding:0 10px;font:600 11px/32px monospace;letter-spacing:.08em}
.ticker{position:fixed;left:0;right:0;height:var(--th,56px);display:flex;top:0;border-top:1px solid rgba(92,153,0,.75);border-bottom:1px solid rgba(92,153,0,.55);background:rgba(6,8,6,.68)}
.ticker .zone{flex:1;overflow:hidden;display:flex;align-items:center}
.ticker .roll{display:inline-flex;align-items:center;white-space:nowrap;font-size:calc(var(--th,56px)*.32);letter-spacing:.06em;color:#CBD6CB;text-shadow:0 1px 5px rgba(0,0,0,.95);will-change:transform}
.roll b:first-of-type{text-shadow:0 0 .4em rgba(180,255,0,.6),0 0 1.1em rgba(180,255,0,.3)}
.roll b:last-of-type{color:var(--acid);margin:0 .6em 0 .45em;text-shadow:0 0 .5em rgba(180,255,0,.7)}
.roll i{font-style:normal;font-weight:700;font-size:.9em;color:#060806;background:var(--acid);
 display:inline-block;vertical-align:middle;padding:.14em .68em .14em calc(.68em + .14em);letter-spacing:.1em;
 clip-path:polygon(.45em 0,100% 0,100% calc(100% - .45em),calc(100% - .45em) 100%,0 100%,0 .45em);
 box-shadow:0 0 .55em rgba(180,255,0,.5)}
.roll .it{flex:0 0 auto;white-space:nowrap}
.roll .it>b:first-of-type{color:var(--acid);margin-right:.35em}
.roll strong{font-weight:600;color:#F2FFE8;text-shadow:0 .08em .25em rgba(0,0,0,.95)}
.roll em{font-style:normal;font-size:.72em;color:var(--toxic);margin:0 .6em;
 text-shadow:0 0 .5em rgba(92,153,0,.8)}
.roll .sep{display:inline-flex;align-items:center;flex:0 0 auto;margin:0 2.2em}
.roll .sep::before,.roll .sep::after{content:'';width:2em;height:.13em;border-radius:.1em}
.roll .sep::before{background:linear-gradient(90deg,transparent,rgba(180,255,0,.8))}
.roll .sep::after{background:linear-gradient(90deg,rgba(180,255,0,.8),transparent)}
.roll .sep .dm{width:.56em;height:.56em;background:var(--acid);border-radius:.13em;transform:rotate(45deg);
 margin:0 .75em;box-shadow:0 0 .55em rgba(180,255,0,.85),0 0 1.3em rgba(180,255,0,.3);
 animation:dpulse 2.8s ease-in-out infinite}
.roll .sep .sd{width:.22em;height:.22em;background:var(--toxic);border-radius:.05em;transform:rotate(45deg);
 margin:0 .55em;box-shadow:0 0 .4em rgba(92,153,0,.95)}
.roll .sep:nth-of-type(odd) .dm{animation-delay:-1.4s}
@keyframes dpulse{50%{box-shadow:0 0 .95em rgba(180,255,0,1),0 0 2.1em rgba(180,255,0,.45);transform:rotate(45deg) scale(1.14)}}
.roll .unit{display:inline-flex;align-items:center;flex:0 0 auto}
</style></head><body>
<div class="edge"></div>
<div class="head" id="head">
  <img src="data:image/png;base64,@@ICON@@" alt=""><div class="name"><b>EXORI</b>SERVICE&nbsp;·&nbsp;TIBIA&nbsp;(RUBINOT)</div>
</div>
<div class="mbar">
  <span class="lbl">TAMANHO</span>
  <button id="msub">−</button><input id="mrng" type="range" min="60" max="200" step="5" value="100"><button id="madd">+</button>
  <span class="val" id="mval">100%</span><button class="rst" id="mrst">RESET</button>
  <span class="lbl">· arraste o quadro = mover · scroll sobre ele = tamanho · E = sair</span>
 </div>
<div class="ticker"><div class="zone"><div class="roll" id="roll"></div></div></div>
<script>
const CFG={posicao:"base",mostrarRotulo:true,alturaTicker:56,ticker:false,itens:[
 "⚔️&nbsp;&nbsp;<b>SOUL WAR</b> <em>•</em> Precisa de Service para Soul War? <strong>Cadastre seu personagem!</strong> <b>→</b> <i>!service</i>",
 "💰&nbsp;&nbsp;<b>RUBINI COINS</b> <em>•</em> 1K por <strong>R$ 90,00</strong> <em>•</em> <strong>Estoque limitado!</strong> <b>→</b> <i>!coins</i>",
 "🤝&nbsp;&nbsp;<b>INTERMÉDIO</b> <em>•</em> Negocie seus itens com <strong>segurança!</strong> <b>→</b> <i>!intermedio</i>",
 "🕐&nbsp;&nbsp;<b>HORÁRIOS</b> <em>•</em> Não perca a próxima live! <strong>Confira os horários</strong> <b>→</b> <i>!horario</i>",
 "📜&nbsp;&nbsp;<b>REGRAS</b> <em>•</em> Respeito no Chat! <strong>Confira as regras!</strong> <b>→</b> <i>!regras</i>",
 "🖥️&nbsp;&nbsp;<b>SETUP</b> <em>•</em> Quer saber meu Setup? <strong>Confira!</strong> <b>→</b> <i>!setup</i>"]};
document.documentElement.style.setProperty('--th',(CFG.alturaTicker||56)+'px');
if(!CFG.ticker){document.querySelector('.ticker').style.display='none'}
const head=document.getElementById('head'),tick=document.querySelector('.ticker');
if(CFG.posicao==="base"){tick.style.cssText+="bottom:0;top:auto"}
else{head.style.bottom='auto';head.style.top=((CFG.alturaTicker||56)+14)+'px'}
if(!CFG.mostrarRotulo){head.style.display='none'}
const roll=document.getElementById('roll');
roll.innerHTML='';
var unit=document.createElement('span');unit.className='unit';
unit.innerHTML=CFG.itens.map(t=>'<span class="it">'+t+'</span>').join('<span class="sep"><span class="sd"></span><span class="dm"></span><span class="sd"></span></span>')+'<span class="sep"><span class="sd"></span><span class="dm"></span><span class="sd"></span></span>';
roll.appendChild(unit);
var W=unit.getBoundingClientRect().width||1;
var need=Math.max(2,Math.ceil((innerWidth+W*2)/W));
for(var k=1;k<need;k++)roll.appendChild(unit.cloneNode(true));
/* ══ RODAPÉ INFINITO REAL ══ A largura dos anúncios muda quando a fonte embutida
   termina de carregar (ou ao redimensionar). Sem re-medir, o período fica velho e a
   emenda "pula". Re-medimos preservando a FASE (rx proporcional) → nunca há salto. */
function remeasure(){var w=unit.getBoundingClientRect().width;if(!(w>1))return;
 if(Math.abs(w-W)>.5){rx=rx*w/W;W=w}
 var n=Math.max(2,Math.ceil((innerWidth+W*2)/W));
 while(roll.children.length<n)roll.appendChild(unit.cloneNode(true))}
var SPD=85,rx=0,prv=performance.now();
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(remeasure);
addEventListener('resize',remeasure);setInterval(remeasure,2000);
(function loop(now){var dt=Math.min(.05,(now-prv)/1000);prv=now;
 rx=(rx+SPD*dt)%W;if(!isFinite(rx))rx=0;
 roll.style.transform='translate3d(-'+rx+'px,0,0)';
 requestAnimationFrame(loop)})(prv);
/* ── QUADRO DA MARCA: modo edição (E) — painel + slider + scroll + arrastar ── */
(function(){
var h=document.getElementById('head'),rng=document.getElementById('mrng'),val=document.getElementById('mval');
var KEY='exoMarca',S=null;
try{S=JSON.parse(localStorage.getItem(KEY)||'null')}catch(e){}
function sc(){return parseFloat(getComputedStyle(h).getPropertyValue('--ms'))||1}
function apply(){if(!S)return;h.style.left=S.x+'%';h.style.top=S.y+'%';h.style.bottom='auto';
 h.style.setProperty('--ms',S.s)}
function pct(){return{x:h.offsetLeft/innerWidth*100,y:h.offsetTop/innerHeight*100}}
function save(){S={x:pct().x,y:pct().y,s:sc()};try{localStorage.setItem(KEY,JSON.stringify(S))}catch(e){}}
function syncUI(){var p=Math.round(sc()*100);rng.value=p;val.textContent=p+'%'}
function setS(v){v=Math.min(200,Math.max(60,v));h.style.setProperty('--ms',(v/100).toFixed(2));syncUI();save()}
apply();
var edit=false;
function toggle(){edit=!edit;document.body.classList.toggle('editing',edit);if(edit)syncUI()}
addEventListener('keydown',function(e){
 var k=e.key.toLowerCase();
 if(k==='e'){toggle();return}
 if(!edit)return;
 if(k==='escape'){toggle()}
 else if(k==='+'||k==='='){setS(sc()*100+5)}
 else if(k==='-'||k==='_'){setS(sc()*100-5)}
 else if(k==='r'){try{localStorage.removeItem(KEY)}catch(x){}location.reload()}
 else if(k.indexOf('arrow')===0){var p=pct(),d=e.shiftKey?2:.5;
  if(k==='arrowleft')h.style.left=(p.x-d)+'%';
  if(k==='arrowright')h.style.left=(p.x+d)+'%';
  if(k==='arrowup')h.style.top=(p.y-d)+'%';
  if(k==='arrowdown')h.style.top=(p.y+d)+'%';
  save();e.preventDefault()}
});
/* scroll sobre o quadro = tamanho */
h.addEventListener('wheel',function(e){if(!edit)return;e.preventDefault();
 setS(sc()*100+(e.deltaY<0?5:-5))},{passive:false});
rng.addEventListener('input',function(){setS(+rng.value)});
function hold(id,fn){var b=document.getElementById(id),iv=null;
 function stop(){if(iv){clearInterval(iv);iv=null}}
 b.addEventListener('pointerdown',function(e){e.preventDefault();fn();iv=setInterval(fn,110)});
 ['pointerup','pointerleave','pointercancel'].forEach(function(ev){b.addEventListener(ev,stop)})}
hold('msub',function(){setS(sc()*100-5)});
hold('madd',function(){setS(sc()*100+5)});
document.getElementById('mrst').onclick=function(){try{localStorage.removeItem(KEY)}catch(x){}location.reload()};
h.addEventListener('pointerdown',function(e){
 if(!edit)return;e.preventDefault();try{h.setPointerCapture(e.pointerId)}catch(x){}
 var p=pct(),sx=e.clientX,sy=e.clientY;
 function mv(e2){h.style.left=(p.x+(e2.clientX-sx)/innerWidth*100)+'%';
  h.style.top=(p.y+(e2.clientY-sy)/innerHeight*100)+'%';h.style.bottom='auto'}
 function up(){save();removeEventListener('pointermove',mv);removeEventListener('pointerup',up)}
 addEventListener('pointermove',mv);addEventListener('pointerup',up)});
})();
</script></body></html>"""

ov = OVERLAY.replace("@@ORBIT9@@", ORBIT9).replace("@@C6@@", C6).replace("@@C5@@", C5).replace("@@ICON@@", MINI96)
open(OUT + "overlay/overlay-gameplay.html", "w").write(ov)
print("overlay-gameplay.html ok (" + str(len(ov) // 1024) + " KB)")

# ════════════ TICKER INDEPENDENTE (fonte própria — móvel/redimensionável no OBS) ════════════
TICKER = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Ticker — exoriservice</title><style>
@font-face{font-family:Chakra;font-weight:600;src:url(data:font/ttf;base64,@@C6@@) format('truetype')}
@font-face{font-family:Chakra;font-weight:500;src:url(data:font/ttf;base64,@@C5@@) format('truetype')}
:root{--acid:#B4FF00;--toxic:#5C9900;--txt:#F2FFE8;--txt2:#9AA69A}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:transparent;font-family:Chakra,monospace}
/* fonte em vh = adapta-se a QUALQUER tamanho que você der à fonte no OBS */
.strip{position:fixed;inset:0;display:flex;border-top:1px solid rgba(180,255,0,.55);border-bottom:1px solid rgba(92,153,0,.65);background:rgba(6,8,6,.8)}
.zone{flex:1;overflow:hidden;display:flex;align-items:center}
.roll{display:inline-flex;align-items:center;white-space:nowrap;font-size:30vh;letter-spacing:.06em;color:#CBD6CB;text-shadow:0 .5vh 1.2vh rgba(0,0,0,.95);will-change:transform}
/* espaçamentos em EM → escalam com a fonte e FICAM VISÍVEIS (vh era microscópico) */
.roll b:first-of-type{text-shadow:0 0 .4em rgba(180,255,0,.6),0 0 1.1em rgba(180,255,0,.3)}
.roll b:last-of-type{color:var(--acid);margin:0 .6em 0 .45em;text-shadow:0 0 .5em rgba(180,255,0,.7)}
.roll i{font-style:normal;font-weight:700;font-size:.9em;color:#060806;background:var(--acid);
 display:inline-block;vertical-align:middle;padding:.14em .68em .14em calc(.68em + .14em);letter-spacing:.1em;
 clip-path:polygon(.45em 0,100% 0,100% calc(100% - .45em),calc(100% - .45em) 100%,0 100%,0 .45em);
 box-shadow:0 0 .55em rgba(180,255,0,.5)}
.roll .it{flex:0 0 auto;white-space:nowrap}
.roll .it>b:first-of-type{color:var(--acid);margin-right:.35em}
.roll strong{font-weight:600;color:#F2FFE8;text-shadow:0 .08em .25em rgba(0,0,0,.95)}
.roll em{font-style:normal;font-size:.72em;color:var(--toxic);margin:0 .6em;
 text-shadow:0 0 .5em rgba(92,153,0,.8)}
.roll .sep{display:inline-flex;align-items:center;flex:0 0 auto;margin:0 2.2em}
.roll .sep::before,.roll .sep::after{content:'';width:2em;height:.13em;border-radius:.1em}
.roll .sep::before{background:linear-gradient(90deg,transparent,rgba(180,255,0,.8))}
.roll .sep::after{background:linear-gradient(90deg,rgba(180,255,0,.8),transparent)}
.roll .sep .dm{width:.56em;height:.56em;background:var(--acid);border-radius:.13em;transform:rotate(45deg);
 margin:0 .75em;box-shadow:0 0 .55em rgba(180,255,0,.85),0 0 1.3em rgba(180,255,0,.3);
 animation:dpulse 2.8s ease-in-out infinite}
.roll .sep .sd{width:.22em;height:.22em;background:var(--toxic);border-radius:.05em;transform:rotate(45deg);
 margin:0 .55em;box-shadow:0 0 .4em rgba(92,153,0,.95)}
.roll .sep:nth-of-type(odd) .dm{animation-delay:-1.4s}
@keyframes dpulse{50%{box-shadow:0 0 .95em rgba(180,255,0,1),0 0 2.1em rgba(180,255,0,.45);transform:rotate(45deg) scale(1.14)}}
.roll .unit{display:inline-flex;align-items:center;flex:0 0 auto}
</style></head><body>
<div class="strip"><div class="zone"><div class="roll" id="roll"></div></div></div>
<script>
/* ═══ CONFIGURAÇÃO (mesma lista do overlay) ═══ */
const CFG={itens:[
 "⚔️&nbsp;&nbsp;<b>SOUL WAR</b> <em>•</em> Precisa de Service para Soul War? <strong>Cadastre seu personagem!</strong> <b>→</b> <i>!service</i>",
 "💰&nbsp;&nbsp;<b>RUBINI COINS</b> <em>•</em> 1K por <strong>R$ 90,00</strong> <em>•</em> <strong>Estoque limitado!</strong> <b>→</b> <i>!coins</i>",
 "🤝&nbsp;&nbsp;<b>INTERMÉDIO</b> <em>•</em> Negocie seus itens com <strong>segurança!</strong> <b>→</b> <i>!intermedio</i>",
 "🕐&nbsp;&nbsp;<b>HORÁRIOS</b> <em>•</em> Não perca a próxima live! <strong>Confira os horários</strong> <b>→</b> <i>!horario</i>",
 "📜&nbsp;&nbsp;<b>REGRAS</b> <em>•</em> Respeito no Chat! <strong>Confira as regras!</strong> <b>→</b> <i>!regras</i>",
 "🖥️&nbsp;&nbsp;<b>SETUP</b> <em>•</em> Quer saber meu Setup? <strong>Confira!</strong> <b>→</b> <i>!setup</i>"]};
const roll=document.getElementById('roll');
roll.innerHTML='';
var unit=document.createElement('span');unit.className='unit';
unit.innerHTML=CFG.itens.map(t=>'<span class="it">'+t+'</span>').join('<span class="sep"><span class="sd"></span><span class="dm"></span><span class="sd"></span></span>')+'<span class="sep"><span class="sd"></span><span class="dm"></span><span class="sd"></span></span>';
roll.appendChild(unit);
var W=unit.getBoundingClientRect().width||1;
var need=Math.max(2,Math.ceil((innerWidth+W*2)/W));
for(var k=1;k<need;k++)roll.appendChild(unit.cloneNode(true));
/* ══ RODAPÉ INFINITO REAL ══ A largura dos anúncios muda quando a fonte embutida
   termina de carregar (ou ao redimensionar). Sem re-medir, o período fica velho e a
   emenda "pula". Re-medimos preservando a FASE (rx proporcional) → nunca há salto. */
function remeasure(){var w=unit.getBoundingClientRect().width;if(!(w>1))return;
 if(Math.abs(w-W)>.5){rx=rx*w/W;W=w}
 var n=Math.max(2,Math.ceil((innerWidth+W*2)/W));
 while(roll.children.length<n)roll.appendChild(unit.cloneNode(true))}
var SPD=85,rx=0,prv=performance.now();
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(remeasure);
addEventListener('resize',remeasure);setInterval(remeasure,2000);
(function loop(now){var dt=Math.min(.05,(now-prv)/1000);prv=now;
 rx=(rx+SPD*dt)%W;if(!isFinite(rx))rx=0;
 roll.style.transform='translate3d(-'+rx+'px,0,0)';
 requestAnimationFrame(loop)})(prv);
</script></body></html>"""

tk = TICKER.replace("@@C6@@", C6).replace("@@C5@@", C5)
open(OUT + "overlay/ticker.html", "w").write(tk)
print("ticker.html ok (" + str(len(tk) // 1024) + " KB)")
