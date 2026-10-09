#!/usr/bin/env python3
"""Carrossel de SERVIÇOS (canto inferior direito) — 4 slides PNG + HTML animado.
Conteúdo: Rubini Coins · Intermediação · Service (cadastro !service) · RubinOT."""
import base64, math
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageFilter

F = "/home/user/twitch-pro/assets/fonts/"
L = "/home/user/twitch-pro/logos/final/"
OUT = "/home/user/twitch-pro/assets/"
import os
os.makedirs(OUT + "carrossel", exist_ok=True)

BG, SURF = (6, 8, 6), (18, 23, 18)
ACID, TOXIC, FOREST = (180, 255, 0), (92, 153, 0), (23, 51, 0)
TXT, TXT2 = (242, 255, 232), (154, 166, 154)
o9 = lambda s: ImageFont.truetype(F + "Orbitron-900.ttf", s)
c6 = lambda s: ImageFont.truetype(F + "ChakraPetch-600.ttf", s)
c5 = lambda s: ImageFont.truetype(F + "ChakraPetch-500.ttf", s)
LOGO = Image.open(L + "icone-512.png").convert("RGB")

W, H = 880, 480

def tracked(d, xy, text, font, fill, tr=0):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tr
    return x

def tw(d, text, font, tr=0):
    return sum(d.textlength(c, font=font) for c in text) + tr * (len(text) - 1)

def frame():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")
    # malha hexagonal
    s = 34
    dx, dy = 1.5 * s, math.sqrt(3) / 2 * s
    for row, yy in enumerate(range(-s, H + int(dy), int(dy))):
        off = dx / 2 if row % 2 else 0
        for xx in range(-int(dx), W + int(dx), int(dx)):
            pts = [(xx + off + s * .25 + math.cos(math.radians(a)) * s * .52,
                    yy + math.sin(math.radians(a)) * s * .52) for a in range(0, 360, 60)]
            d.polygon(pts, outline=(16, 26, 10, 60))
    # brilho central suave (screen: só clareia o centro — cantos permanecem com o fundo intacto)
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W // 2 - 340, H // 2 - 215, W // 2 + 340, H // 2 + 215], fill=(13, 28, 3))
    glow = glow.filter(ImageFilter.GaussianBlur(85))
    img = ImageChops.screen(img, glow)
    d = ImageDraw.Draw(img, "RGBA")
    # vinheta leve (cantos apenas levemente escurecidos, sem áreas mortas)
    vg = Image.radial_gradient("L").resize((W, H))
    img.paste((0, 0, 0), (0, 0), vg.point(lambda p: int(p / 255 * 95)))
    d = ImageDraw.Draw(img, "RGBA")
    # barra de energia topo
    for xx in range(0, W, 2):
        t = abs(xx - W / 2) / (W / 2)
        col = tuple(int(ACID[i] * (1 - t * .5)) for i in range(3))
        d.line([(xx, 0), (xx, 5)], fill=col)
    return img, d

def chrome(d, idx, label):
    """Elementos comuns: label PROMO, paginação, marca."""
    tracked(d, (36, 26), label, c6(20), ACID, 4)
    d.line([(36, 58), (36 + tw(d, label, c6(20), 4), 58)], fill=TOXIC, width=2)
    # paginação 0X/04
    pg = f"{idx:02d}/04"
    d.text((W - 40 - d.textlength(pg, font=c6(18)), 28), pg, font=c6(18), fill=TXT2)
    # marca rodapé
    logo = LOGO.resize((44, 44), Image.LANCZOS)
    return logo

def slide(nome, idx, label, draw_body):
    img, d = frame()
    logo = chrome(d, idx, label)
    draw_body(d, img)
    img.paste(logo, (36, H - 78))
    tracked(d, (92, H - 68), "EXORISERVICE", o9(20), TXT, 2)
    # moldura verde extremamente fina (2px aqui = 1px no widget em escala real)
    d.rectangle([2, 2, W - 3, H - 3], outline=ACID, width=2)
    img.save(OUT + f"carrossel/{nome}.png")
    print("•", nome + ".png")

def chip(d, cx, y, text, font, acid_text=False):
    w = tw(d, text, font)
    x = cx - w / 2
    d.polygon([(x - 14, y), (x + w + 14, y), (x + w + 14, y + font.size + 18), (x + w + 4, y + font.size + 22),
               (x - 14, y + font.size + 22)], fill=(12, 17, 12, 240), outline=TOXIC + (200,))
    tracked(d, (x, y + 8), text, font, ACID if acid_text else TXT2, 1)

def fit(d, text, fontfn, maxw, tr=0, start=64, minsize=14):
    """Reduz a fonte em passos de 2 até o texto caber em maxw."""
    size = start
    f = fontfn(size)
    while tw(d, text, f, tr) > maxw and size > minsize:
        size -= 2
        f = fontfn(size)
    return f

# ── SLIDE 1 · RUBINI COINS ──
def s1(d, img):
    t = "RUBINI COINS"
    f = fit(d, t, o9, 800, 4, 72)
    tracked(d, ((W - tw(d, t, f, 4)) / 2, 118), t, f, ACID, 4)
    t2 = "1.000  =  R$ 90,00"
    f2 = fit(d, t2, o9, 800, 0, 46)
    d.text(((W - d.textlength(t2, font=f2)) / 2, 218), t2, font=f2, fill=TXT)
    chip(d, W / 2, 300, "Rapidez e Segurança", c5(22))
slide("slide-1-coins", 1, "PROMO · MOEDAS", s1)

# ── SLIDE 2 · INTERMÉDIO ──
def s2(d, img):
    t = "INTERMÉDIO"
    f = fit(d, t, o9, 800, 3, 64)
    tracked(d, ((W - tw(d, t, f, 3)) / 2, 96), t, f, TXT, 3)
    f2 = c6(34)
    t2 = "apenas de itens"
    d.text(((W - d.textlength(t2, font=f2)) / 2, 196), t2, font=f2, fill=ACID)
    f3 = c6(27)
    t3 = "com rapidez · segurança · preço justo"
    d.text(((W - d.textlength(t3, font=f3)) / 2, 258), t3, font=f3, fill=TXT2)
slide("slide-2-intermedio", 2, "PROMO · SERVIÇO", s2)

# ── SLIDE 3 · SERVICE (Soul War / Sanguine) ──
def s3(d, img):
    t = "SERVICE DE QUESTS"
    f = fit(d, t, o9, 800, 2, 42)
    tracked(d, ((W - tw(d, t, f, 2)) / 2, 88), t, f, TXT, 2)
    # dois painéis lado a lado
    bw, bh, gap = 330, 104, 28
    x1 = W / 2 - bw - gap / 2
    x2 = W / 2 + gap / 2
    y0 = 178
    d.polygon([(x1 + 12, y0), (x1 + bw, y0), (x1 + bw, y0 + bh - 12), (x1 + bw - 12, y0 + bh), (x1, y0 + bh), (x1, y0 + 12)],
              fill=(14, 20, 12, 250), outline=ACID, width=2)
    d.polygon([(x2 + 12, y0), (x2 + bw, y0), (x2 + bw, y0 + bh - 12), (x2 + bw - 12, y0 + bh), (x2, y0 + bh), (x2, y0 + 12)],
              fill=(12, 15, 12, 250), outline=TOXIC, width=2)
    fA = fit(d, "SOUL WAR", o9, 280, 2, 40)
    tA = "SOUL WAR"
    tracked(d, (x1 + (bw - tw(d, tA, fA, 2)) / 2, y0 + 30), tA, fA, ACID, 2)
    tB = "SANGUINE"
    fB = fit(d, tB, o9, 280, 2, 40)
    tracked(d, (x2 + (bw - tw(d, tB, fB, 2)) / 2, y0 + 22), tB, fB, TXT2, 2)
    fC = c6(17)
    tC = "EM BREVE"
    tracked(d, (x2 + (bw - tw(d, tC, fC, 4)) / 2, y0 + 76), tC, fC, TOXIC, 4)
    f3 = o9(34)
    t3 = "CADASTRE-SE:  !service"
    d.text(((W - d.textlength(t3, font=f3)) / 2, 330), t3, font=f3, fill=ACID)
    f4 = c5(19)
    t4 = "digite no chat e o streamer te chama"
    d.text(((W - d.textlength(t4, font=f4)) / 2, 392), t4, font=f4, fill=TXT2)
slide("slide-3-service", 3, "PROMO · CADASTRO", s3)

# ── SLIDE 4 · RUBINOT (logo dark real) ──
def s4(d, img):
    logo = Image.open(OUT + "carrossel/rubinot-dark.png").convert("RGB")
    lw = 560
    lh = int(logo.height * lw / logo.width)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    # painel-moldura chanfrado
    pw, ph = 640, 260
    px, py = int(W / 2 - pw / 2), 92
    d.polygon([(px + 16, py), (px + pw, py), (px + pw, py + ph - 16), (px + pw - 16, py + ph), (px, py + ph), (px, py + 16)],
              fill=(10, 13, 10, 255), outline=TOXIC, width=2)
    img.paste(logo, (int(W / 2 - lw / 2), py + int((ph - lh) / 2)))
    d = ImageDraw.Draw(img, "RGBA")
    f2 = c6(26)
    t2 = "o servidor onde a live acontece"
    d.text(((W - d.textlength(t2, font=f2)) / 2, 380), t2, font=f2, fill=TXT)
slide("slide-4-rubinot", 4, "PROMO · SERVIDOR", s4)

# ═══ HTML do carrossel ═══
b64f = lambda p: base64.b64encode(open(p, "rb").read()).decode()
S1, S2, S3, S4 = (b64f(OUT + f"carrossel/slide-{n}.png") for n in
                  ("1-coins", "2-intermedio", "3-service", "4-rubinot"))
MINI = b64f(L + "mini-96.png")

HTML = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Carrossel de Serviços — exoriservice</title><style>
:root{--acid:#B4FF00;--toxic:#5C9900}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:transparent;font-family:'Chakra Petch',sans-serif}
/* ══ AJUSTÁVEL: a fonte no OBS define o tamanho — a caixa escala proporcional ══ */
.car{position:fixed;inset:0;pointer-events:none}
.box{position:absolute;right:1.8%;bottom:6%;width:22%;aspect-ratio:880/480;overflow:hidden;
 background:rgba(6,8,6,.9);border:1px solid rgba(180,255,0,.8);
 clip-path:polygon(16px 0,100% 0,100% calc(100% - 16px),calc(100% - 16px) 100%,0 100%,0 16px);
 box-shadow:0 0 26px rgba(180,255,0,.12);
 animation:carin .6s cubic-bezier(.2,.9,.3,1.15) both}
@keyframes carin{from{opacity:0;transform:translateX(60px)}to{opacity:1;transform:none}}
.box::after{content:'';position:absolute;left:-140%;top:0;bottom:0;width:50%;
 background:linear-gradient(90deg,transparent,rgba(180,255,0,.08),transparent);
 animation:sweep 5s linear infinite;z-index:5;pointer-events:none}
@keyframes sweep{to{left:160%}}
.slide{position:absolute;inset:0;opacity:0;transform:translateX(70px);
 animation:cyc 28s cubic-bezier(.25,.8,.35,1) infinite}
.slide img{width:100%;height:100%;object-fit:cover;display:block}
.s2{animation-delay:7s}.s3{animation-delay:14s}.s4{animation-delay:21s}
@keyframes cyc{0%{opacity:0;transform:translateX(70px)}
 2.5%,23%{opacity:1;transform:none}
 25.5%,100%{opacity:0;transform:translateX(-70px)}}
.badge{position:absolute;top:14px;right:16px;z-index:6;background:var(--acid);color:#060806;
 font-size:11px;font-weight:600;letter-spacing:.22em;padding:5px 12px 5px calc(12px + .22em);
 clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px);
 box-shadow:0 0 14px rgba(180,255,0,.4)}
.progress{position:absolute;left:0;bottom:0;height:3px;background:linear-gradient(90deg,var(--acid),var(--toxic));
 width:0;animation:prog 7s linear infinite;z-index:6}
@keyframes prog{to{width:100%}}
/* ══ MODO EDIÇÃO (tecla E na janela Interagir do OBS) ══ */
.edit .car{pointer-events:auto}
.edit .box{cursor:grab;outline:2px dashed rgba(180,255,0,.9);outline-offset:4px}
.edit .box:active{cursor:grabbing}
.rz{position:absolute;right:0;bottom:0;width:34px;height:34px;z-index:9;display:none;cursor:nwse-resize;
 background:repeating-linear-gradient(45deg,var(--acid) 0 6px,#3E6B00 6px 12px);
 outline:2px solid var(--acid);box-shadow:0 0 12px rgba(180,255,0,.55)}
.edit .rz{display:block}
.bar{position:absolute;top:12px;left:50%;transform:translateX(-50%);z-index:10;display:none;
 align-items:center;gap:8px;background:rgba(6,8,6,.95);border:1px solid var(--acid);
 padding:8px 12px;white-space:nowrap}
.edit .bar{display:flex}
.bar .lbl{color:#9AA69A;font-size:11px;letter-spacing:.05em}
.bar button{width:32px;height:32px;border:0;background:var(--acid);color:#060806;
 font:700 17px/32px monospace;cursor:pointer;padding:0}
.bar button:active{transform:scale(.92)}
.bar input[type=range]{width:170px;accent-color:var(--acid);cursor:pointer}
.bar .val{color:var(--acid);font:600 13px/1 monospace;min-width:44px;text-align:center}
.bar .rst{width:auto;padding:0 10px;font:600 11px/32px monospace;letter-spacing:.08em}
</style></head><body>
<div class="car">
 <div class="box">
  <div class="badge">SERVIÇOS</div>
  <div class="slide s1"><img src="data:image/png;base64,@@S1@@" alt=""></div>
  <div class="slide s2"><img src="data:image/png;base64,@@S2@@" alt=""></div>
  <div class="slide s3"><img src="data:image/png;base64,@@S3@@" alt=""></div>
  <div class="slide s4"><img src="data:image/png;base64,@@S4@@" alt=""></div>
  <div class="progress"></div>
  <div class="rz"></div>
 </div>
 <div class="bar">
  <span class="lbl">TAMANHO</span>
  <button id="bsub">−</button><input id="rng" type="range" min="8" max="60" step="1" value="22"><button id="badd">+</button>
  <span class="val" id="bval">22%</span><button class="rst" id="brst">RESET</button>
  <span class="lbl">· arraste = mover · scroll sobre a tela = tamanho · E = sair</span>
 </div>
</div>
<script>
(function(){
var box=document.querySelector('.box'),car=document.querySelector('.car');
var rng=document.getElementById('rng'),val=document.getElementById('bval');
var KEY='exoCarrossel',S=null;
try{S=JSON.parse(localStorage.getItem(KEY)||'null')}catch(e){}
function apply(){if(!S)return;box.style.right='auto';box.style.bottom='auto';
 box.style.left=S.x+'%';box.style.top=S.y+'%';box.style.width=S.w+'%'}
function ensureXY(){if(box.style.left)return;var p=pct(box);box.style.right='auto';box.style.bottom='auto';
 box.style.left=p.x+'%';box.style.top=p.y+'%';box.style.width=p.w+'%'}
function pct(){var p=car.offsetWidth?car:document.body;
 return{x:box.offsetLeft/p.offsetWidth*100,y:box.offsetTop/p.offsetHeight*100,w:box.offsetWidth/p.offsetWidth*100}}
function clamp(){var p=pct(box),h=box.offsetHeight/(car.offsetHeight||document.body.offsetHeight)*100;
 box.style.left=Math.min(100-p.w,Math.max(0,p.x))+'%';
 box.style.top=Math.min(100-h,Math.max(0,p.y))+'%'}
function save(){S=pct(box);try{localStorage.setItem(KEY,JSON.stringify(S))}catch(e){}}
function syncUI(){var w=Math.round(pct(box).w);rng.value=w;val.textContent=w+'%'}
function setW(w){ensureXY();w=Math.min(60,Math.max(8,w));box.style.width=w+'%';clamp();syncUI();save()}
apply();
var edit=false;
function toggle(){edit=!edit;document.body.classList.toggle('edit',edit);if(edit)syncUI()}
addEventListener('keydown',function(e){
 var k=e.key.toLowerCase();
 if(k==='e'){toggle();return}
 if(!edit)return;
 if(k==='escape'){toggle()}
 else if(k==='+'||k==='='){setW(pct(box).w+1)}
 else if(k==='-'||k==='_'){setW(pct(box).w-1)}
 else if(k==='r'){try{localStorage.removeItem(KEY)}catch(x){}location.reload()}
 else if(k.indexOf('arrow')===0){ensureXY();var p=pct(box),d=e.shiftKey?2:.5;
  if(k==='arrowleft')box.style.left=(p.x-d)+'%';
  if(k==='arrowright')box.style.left=(p.x+d)+'%';
  if(k==='arrowup')box.style.top=(p.y-d)+'%';
  if(k==='arrowdown')box.style.top=(p.y+d)+'%';
  clamp();save();e.preventDefault()}
});
/* SCROLL em qualquer lugar = redimensionar (modo edição) */
car.addEventListener('wheel',function(e){if(!edit)return;
 if(e.target&&e.target.closest&&e.target.closest('.bar'))return;
 e.preventDefault();setW(pct(box).w+(e.deltaY<0?1:-1))},{passive:false});
/* slider + botões (repetem enquanto segurar) */
rng.addEventListener('input',function(){setW(+rng.value)});
function hold(id,fn){var b=document.getElementById(id),iv=null;
 function stop(){if(iv){clearInterval(iv);iv=null}}
 b.addEventListener('pointerdown',function(e){e.preventDefault();fn();iv=setInterval(fn,110)});
 ['pointerup','pointerleave','pointercancel'].forEach(function(ev){b.addEventListener(ev,stop)})}
hold('bsub',function(){setW(pct(box).w-1)});
hold('badd',function(){setW(pct(box).w+1)});
document.getElementById('brst').onclick=function(){try{localStorage.removeItem(KEY)}catch(x){}location.reload()};
/* arrastar: caixa = mover · alça = redimensionar */
function drag(el,mode){el.addEventListener('pointerdown',function(e){
 if(!edit)return;e.preventDefault();try{el.setPointerCapture(e.pointerId)}catch(x){}
 ensureXY();var p=pct(box),sx=e.clientX,sy=e.clientY;
 function mv(e2){var dx=(e2.clientX-sx)/car.offsetWidth*100,dy=(e2.clientY-sy)/car.offsetHeight*100;
  if(mode==='move'){box.style.left=(p.x+dx)+'%';box.style.top=(p.y+dy)+'%'}
  else{box.style.width=Math.min(60,Math.max(8,p.w+dx))+'%';syncUI()}
  clamp()}
 function up(){save();syncUI();removeEventListener('pointermove',mv);removeEventListener('pointerup',up)}
 addEventListener('pointermove',mv);addEventListener('pointerup',up)})}
drag(box,'move');drag(document.querySelector('.rz'),'size');
})();
</script>
</body></html>"""

html = (HTML.replace("@@S1@@", S1).replace("@@S2@@", S2)
        .replace("@@S3@@", S3).replace("@@S4@@", S4))
open(OUT + "overlay/carrossel-servicos.html", "w").write(html)
print("carrossel-servicos.html ok (" + str(len(html) // 1024) + " KB)")
