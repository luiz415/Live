#!/usr/bin/env python3
"""Party Tracker Tibia — HORIZONTAL COMPACTO (v3).
• Ediça de conteúdo ao vivo (Interagir): título, 5× vocação+level, VISÃO DO;
• SISTEMA DE AJUSTE igual ao Carrossel: E liga o modo edição → painel no topo
  (slider + botões −/+ + % + RESET), scroll do mouse redimensiona, arraste move,
  setas ajuste fino — posição/tamanho salvos sozinhos (localStorage);
• Animações elegantes: flutuação suave, glow respirando, sweep de brilho,
  cometa orbitando o widget e chip da vocação pulsando;
• "VISÃO DO:" acima do quadro (FORA dele) com vocação de 2 letras maiúsculas."""
import base64

F = "/home/user/twitch-pro/assets/fonts/"
L = "/home/user/twitch-pro/logos/final/"
OUT = "/home/user/twitch-pro/assets/"

b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
ORBIT9, C6, C5 = b64(F + "Orbitron-900.ttf"), b64(F + "ChakraPetch-600.ttf"), b64(F + "ChakraPetch-500.ttf")
MINI96 = b64(L + "mini-96.png")

PARTY = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Party Tracker — exoriservice</title><style>
@font-face{font-family:Orbitron;font-weight:900;src:url(data:font/ttf;base64,@@ORBIT9@@) format('truetype')}
@font-face{font-family:Chakra;font-weight:600;src:url(data:font/ttf;base64,@@C6@@) format('truetype')}
@font-face{font-family:Chakra;font-weight:500;src:url(data:font/ttf;base64,@@C5@@) format('truetype')}
:root{--acid:#B4FF00;--toxic:#5C9900;--txt:#F2FFE8;--txt2:#9AA69A}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:transparent;font-family:Chakra,monospace}
@property --pa{syntax:'<angle>';initial-value:0deg;inherits:false}

/* ══ posicionamento + ESCALA (salvos; mesma mecânica do carrossel) ══ */
.wrap{position:fixed;left:50%;bottom:calc(6.8vh + 14px);z-index:2;
 transform:translateX(-50%) scale(var(--ps,1));transform-origin:50% 100%}
/* flutuação suave + entrada (container próprio p/ não brigar com a escala) */
.floati{animation:boardin .55s cubic-bezier(.2,.9,.3,1.15) both}
@keyframes boardin{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:none}}
body.edit .floati{animation:none}
body.edit .floati{animation:none}

/* ── VISÃO DO: — acima, FORA do quadro ── */
.vhead{display:flex;align-items:center;justify-content:center;gap:8px;margin-bottom:6px;white-space:nowrap}
.vlbl{font-size:11px;font-weight:600;letter-spacing:.22em;color:var(--txt2)}
.vchip{min-width:46px;text-align:center;font-family:Orbitron;font-weight:900;font-size:18px;
 letter-spacing:.12em;padding:3px 8px 3px calc(8px + .12em);color:#060806;background:var(--acid);
 clip-path:polygon(6px 0,100% 0,100% calc(100% - 6px),calc(100% - 6px) 100%,0 100%,0 6px);
 animation:vglow 2.6s ease-in-out infinite}
@keyframes vglow{50%{filter:drop-shadow(0 0 7px rgba(180,255,0,.8))}}
.vchip.empty{background:rgba(92,153,0,.22);color:var(--toxic);animation:none}
/* ── QUEST: — seletor SOUL WAR (cinza neon) / SANGUINE (vermelho) ── */
.vsep{width:1px;height:16px;margin:0 8px;background:linear-gradient(180deg,transparent,rgba(154,166,154,.55),transparent)}
.qlbl{font-size:11px;font-weight:600;letter-spacing:.22em;color:var(--txt2)}
.qchip{font-family:Orbitron;font-weight:900;font-size:12px;letter-spacing:.1em;padding:4px 9px 4px calc(9px + .1em);
 white-space:nowrap;cursor:pointer;background:rgba(10,12,10,.92);
 clip-path:polygon(6px 0,100% 0,100% calc(100% - 6px),calc(100% - 6px) 100%,0 100%,0 6px)}
.qchip::after{content:'▾';font-family:Chakra;font-size:9px;margin-left:6px;opacity:.75}
.qchip.sw{color:#CFDCCF;border:1px solid rgba(190,205,190,.85);text-shadow:0 0 9px rgba(207,220,207,.55);animation:qgs 2.8s ease-in-out infinite}
@keyframes qgs{50%{filter:drop-shadow(0 0 6px rgba(207,220,207,.55))}}
.qchip.sa{color:#FF5252;border:1px solid rgba(255,80,80,.85);text-shadow:0 0 9px rgba(255,60,60,.6);animation:qrs 2.8s ease-in-out infinite}
@keyframes qrs{50%{filter:drop-shadow(0 0 6px rgba(255,60,60,.6))}}
.qchip.qhit{animation:qhit .4s ease-out}
@keyframes qhit{0%{transform:scale(1.12)}100%{transform:none}}
.vhead select{background:rgba(6,8,6,.95);border:1px solid var(--toxic);outline:none;color:var(--txt);
 font-family:Chakra;font-weight:600;font-size:12px;letter-spacing:.1em;padding:4px 6px;cursor:pointer}
.vhead select:focus{border-color:var(--acid);box-shadow:0 0 12px rgba(180,255,0,.35)}
.vconn{width:2px;height:7px;margin:0 auto 4px;background:linear-gradient(180deg,var(--acid),transparent);opacity:.7}

/* ══ quadro ══ */
.board{display:flex;align-items:stretch;position:relative;
 background:rgba(6,8,6,.86);border:1px solid rgba(180,255,0,.8);
 clip-path:polygon(14px 0,100% 0,100% calc(100% - 14px),calc(100% - 14px) 100%,0 100%,0 14px);
 box-shadow:0 0 24px rgba(180,255,0,.10);
 animation:bglow 3.4s ease-in-out infinite}
@keyframes bglow{50%{box-shadow:0 0 34px rgba(180,255,0,.24)}}
.board::after{content:'';position:absolute;inset:0;pointer-events:none;
 background:linear-gradient(105deg,transparent 30%,rgba(244,255,208,.10) 50%,transparent 70%);
 background-size:250% 100%;animation:psweep 6s ease-in-out infinite}
@keyframes psweep{0%{background-position:130% 0}55%,100%{background-position:-130% 0}}
.board.edit{border-color:var(--acid);box-shadow:0 0 30px rgba(180,255,0,.3)}

/* ── cometa orbitando o widget inteiro (assinatura da marca) ── */
.comet{position:absolute;inset:-7px;padding:2px;pointer-events:none;
 background:conic-gradient(from var(--pa),transparent 0deg 150deg,
  rgba(180,255,0,.13) 150deg,rgba(180,255,0,.85) 342deg,#F4FFD0 350deg,rgba(180,255,0,.85) 353deg,transparent 360deg);
 -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
 mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
 -webkit-mask-composite:xor;mask-composite:exclude;
 filter:drop-shadow(0 0 5px rgba(180,255,0,.6));animation:porbit 7s linear infinite}
@keyframes porbit{to{--pa:360deg}}
body.edit .comet{display:none}

/* ── cabeçalho enxuto ── */
.bhead{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;padding:8px 12px}
.bhead img{width:34px;height:34px;filter:drop-shadow(0 0 8px rgba(180,255,0,.45));animation:imgp 2.6s ease-in-out infinite}
@keyframes imgp{50%{transform:scale(1.07)}}
.btitle{font-family:Orbitron;font-weight:900;font-size:15px;letter-spacing:.14em;color:var(--txt);white-space:nowrap}
.dot{width:7px;height:7px;background:var(--acid);border-radius:50%;box-shadow:0 0 9px var(--acid);animation:blink 1.6s infinite}
@keyframes blink{50%{opacity:.2}}
.vbar{width:2px;margin:8px 0;background:linear-gradient(180deg,var(--acid),var(--toxic));opacity:.8}

/* ── células ── */
.cells{display:flex;gap:7px;padding:8px}
.pcell{width:104px;display:flex;flex-direction:column;align-items:center;gap:5px;padding:8px 5px 9px;position:relative;
 background:rgba(18,23,18,.92);border:1px solid rgba(92,153,0,.55);
 clip-path:polygon(8px 0,100% 0,100% calc(100% - 8px),calc(100% - 8px) 100%,0 100%,0 8px);
 animation:cellin .45s cubic-bezier(.2,.9,.3,1.15) both}
.pcell:nth-child(1){animation-delay:.06s}.pcell:nth-child(2){animation-delay:.12s}
.pcell:nth-child(3){animation-delay:.18s}.pcell:nth-child(4){animation-delay:.24s}
.pcell:nth-child(5){animation-delay:.3s}
@keyframes cellin{from{opacity:0;transform:translateY(26px)}to{opacity:1;transform:none}}
.pcell.flash{animation:cellflash .5s ease-out}
@keyframes cellflash{0%{border-color:var(--acid);box-shadow:0 0 20px rgba(180,255,0,.55);transform:scale(1.05)}100%{}}
.idx{position:absolute;top:4px;left:8px;font-size:9px;font-weight:600;color:var(--toxic)}
.voc{min-width:56px;text-align:center;font-family:Orbitron;font-weight:900;font-size:20px;letter-spacing:.1em;padding:3px 6px 3px calc(6px + .1em);
 color:#060806;background:var(--acid);clip-path:polygon(6px 0,100% 0,100% calc(100% - 6px),calc(100% - 6px) 100%,0 100%,0 6px)}
.voc.empty{background:rgba(92,153,0,.22);color:var(--toxic)}
.lvl{display:flex;align-items:baseline;gap:6px}
.lvl .lab{font-size:9px;font-weight:600;letter-spacing:.18em;color:var(--txt2)}
.lvl .num{font-family:Orbitron;font-weight:900;font-size:20px;color:var(--txt);min-width:40px;text-align:center}
.lvl .num.empty{color:var(--txt2);opacity:.45}

/* ══ MODO EDIÇÃO: botão, painel de tamanho, campos ══ */
.gear{position:absolute;top:-44px;right:0;opacity:0;transition:.25s;cursor:pointer;color:var(--txt2);
 font-family:Chakra;font-size:14px;font-weight:600;letter-spacing:.08em;border:1px solid rgba(180,255,0,.7);
 padding:9px 18px;background:rgba(6,8,6,.95);z-index:5;user-select:none;
 clip-path:polygon(6px 0,100% 0,100% calc(100% - 6px),calc(100% - 6px) 100%,0 100%,0 6px)}
.wrap.live .gear{opacity:1;animation:gpulse 1.8s ease-in-out infinite}
@keyframes gpulse{50%{box-shadow:0 0 20px rgba(180,255,0,.45);color:var(--acid)}}
.wrap:hover .gear{opacity:.95}
.gear:hover{color:var(--acid);border-color:var(--acid)}
body.edit .gear{opacity:1;color:var(--acid);border-color:var(--acid)}
.board input{background:rgba(6,8,6,.95);border:1px solid var(--toxic);color:var(--txt);outline:none;text-align:center;font-family:Orbitron;font-weight:900}
.board input:focus,.vhead input:focus{border-color:var(--acid);box-shadow:0 0 12px rgba(180,255,0,.35)}
.vin{width:64px;font-size:19px;padding:4px 2px;letter-spacing:.1em;text-transform:uppercase;color:var(--acid)}
.lin{width:64px;font-size:19px;padding:4px 2px}
.tin{width:110px;font-size:13px;letter-spacing:.14em;padding:3px 2px}
.vhead input{background:rgba(6,8,6,.95);border:1px solid var(--toxic);outline:none;text-align:center;
 font-family:Orbitron;font-weight:900;font-size:17px;letter-spacing:.12em;padding:3px 6px;width:56px;
 text-transform:uppercase;color:var(--acid)}
.editing{cursor:grab}
.hint{position:absolute;left:0;right:0;bottom:-30px;display:none;text-align:center;font-size:11px;color:var(--txt2)}
.wrap.edit .hint{display:block}
.hint b{color:var(--acid)}
/* painel de tamanho (mesmo padrão do carrossel) */
.bar{position:fixed;top:12px;left:50%;transform:translateX(-50%);z-index:10;display:none;
 align-items:center;gap:8px;background:rgba(6,8,6,.95);border:1px solid var(--acid);
 padding:8px 12px;white-space:nowrap}
body.edit .bar{display:flex}
.bar .lbl{color:#9AA69A;font-size:11px;letter-spacing:.05em}
.bar button{width:32px;height:32px;border:0;background:var(--acid);color:#060806;
 font:700 17px/32px monospace;cursor:pointer;padding:0}
.bar button:active{transform:scale(.92)}
.bar input[type=range]{width:170px;accent-color:var(--acid);cursor:pointer}
.bar .val{color:var(--acid);font:600 13px/1 monospace;min-width:44px;text-align:center}
.bar .rst{width:auto;padding:0 10px;font:600 11px/32px monospace;letter-spacing:.08em}
</style></head><body>
<div class="bar">
  <span class="lbl">TAMANHO</span>
  <button id="psub">−</button><input id="prng" type="range" min="60" max="200" step="5" value="100"><button id="padd">+</button>
  <span class="val" id="pval">100%</span><button class="rst" id="prst">RESET</button>
  <span class="lbl">· arraste o quadro = mover · scroll sobre ele = tamanho · campos: clique e digite · E = sair</span>
 </div>
<div class="wrap" id="wrap">
  <div class="floati">
   <div class="comet"></div>
   <div class="vhead" id="vhead">
     <span class="vlbl">VISÃO DO:</span><span class="vslot" id="vslot"><span class="vchip empty">··</span></span>
     <span class="vsep"></span>
     <span class="qlbl">QUEST:</span><span class="qslot" id="qslot"></span>
   </div>
   <div class="vconn"></div>
   <div class="board" id="board">
     <div class="bhead">
       <img src="data:image/png;base64,@@ICON@@" alt="">
       <div class="btitle" id="tlabel">PARTY</div>
       <div class="dot"></div>
     </div>
     <div class="vbar"></div>
     <div class="cells" id="rows"></div>
   </div>
  </div>
  <div class="gear" id="gear">EDITAR</div>
  <div class="hint">clique nos campos e digite · <b>OK</b> (ou tecla E) para sair</div>
</div>
<script>
const store={get(k){try{return localStorage.getItem(k)}catch(e){return this._m&&this._m[k]}},
 set(k,v){try{localStorage.setItem(k,v)}catch(e){this._m=this._m||{};this._m[k]=v}}};
const KEY='exoriPartyV1',PKEY='exoriPartyPos';
let data={title:'PARTY',view:'',quest:'sw',rows:[{v:'',l:''},{v:'',l:''},{v:'',l:''},{v:'',l:''},{v:'',l:''}]};
try{const s=JSON.parse(store.get(KEY)||'null');if(s&&s.rows)data=Object.assign(data,s)}catch(e){}
const q=new URLSearchParams(location.search);
if(q.get('title'))data.title=q.get('title').slice(0,14).toUpperCase();
if(q.get('view'))data.view=q.get('view').slice(0,2).toUpperCase();
if(q.get('quest'))data.quest=q.get('quest')==='sa'?'sa':'sw';
for(let i=1;i<=5;i++){if(q.get('v'+i))data.rows[i-1].v=q.get('v'+i).slice(0,2).toUpperCase();
 if(q.get('l'+i))data.rows[i-1].l=q.get('l'+i).replace(/[^0-9]/g,'').slice(0,4)}

const board=document.getElementById('board'),rowsEl=document.getElementById('rows'),
      wrap=document.getElementById('wrap'),vslot=document.getElementById('vslot'),qslot=document.getElementById('qslot');
let edit=false;

function render(){
 document.getElementById('tlabel').textContent=data.title||'PARTY';
 /* VISÃO DO: — 2 letras maiúsculas */
 if(edit){vslot.innerHTML='<input id="viewin" maxlength="2" value="'+(data.view||'')+'">';
  const vi=document.getElementById('viewin');
  vi.oninput=()=>{data.view=vi.value=vi.value.toUpperCase().replace(/[^A-Z]/g,'');save()};}
 else{vslot.innerHTML='<span class="vchip'+(data.view?'':' empty')+'">'+(data.view||'··')+'</span>'}
 /* QUEST: — modo edição: <select> · ao vivo: clique no chip alterna SOUL WAR/SANGUINE */
 if(edit){qslot.innerHTML='<select id="qsel"><option value="sw"'+(data.quest!=='sa'?' selected':'')
  +'>SOUL WAR</option><option value="sa"'+(data.quest==='sa'?' selected':'')+'>SANGUINE</option></select>';
  document.getElementById('qsel').onchange=function(){data.quest=this.value;save()}}
 else{qslot.innerHTML='<span class="qchip '+(data.quest==='sa'?'sa':'sw')+'" id="qchip">'
  +(data.quest==='sa'?'SANGUINE':'SOUL WAR')+'</span>';
  const qc=document.getElementById('qchip');
  qc.onclick=()=>{data.quest=data.quest==='sa'?'sw':'sa';save();
   qc.className='qchip '+(data.quest==='sa'?'sa':'sw');
   qc.textContent=data.quest==='sa'?'SANGUINE':'SOUL WAR';
   qc.classList.add('qhit');setTimeout(()=>qc.classList.remove('qhit'),420)}}
 rowsEl.innerHTML='';
 data.rows.forEach((r,i)=>{
  const cell=document.createElement('div');cell.className='pcell';
  cell.innerHTML='<div class="idx">'+String(i+1).padStart(2,'0')+'</div>'
   +'<div class="voc'+(r.v?'':' empty')+'">'+(edit?'<input class="vin" maxlength="2" value="'+r.v+'">':(r.v||'··'))+'</div>'
   +'<div class="lvl"><span class="lab">LV</span><span class="num'+(r.l?'':' empty')+'">'
   +(edit?'<input class="lin" maxlength="4" inputmode="numeric" value="'+r.l+'">':(r.l||'···'))+'</span></div>';
  rowsEl.appendChild(cell);
  if(edit){
   const vi=cell.querySelector('.vin'),li=cell.querySelector('.lin');
   vi.oninput=()=>{r.v=vi.value=vi.value.toUpperCase().replace(/[^A-Z]/g,'');save();flash(cell)};
   li.oninput=()=>{r.l=li.value=li.value.replace(/[^0-9]/g,'');save();flash(cell)};
  }
 });
 const tl=document.getElementById('tlabel');
 if(edit){const ti=document.createElement('input');ti.className='tin';ti.maxLength=14;ti.value=data.title;
  ti.style.display='block';tl.innerHTML='';tl.appendChild(ti);
  ti.oninput=()=>{data.title=ti.value.toUpperCase();save()}}
}
function flash(el){el.classList.remove('flash');void el.offsetWidth;el.classList.add('flash')}
function save(){store.set(KEY,JSON.stringify(data))}

/* ══ POSIÇÃO + TAMANHO (mesmo sistema do carrossel/marca) ══ */
var rng=document.getElementById('prng'),pval=document.getElementById('pval'),P=null;
try{P=JSON.parse(store.get(PKEY)||'null')}catch(e){}
function sc(){return parseFloat(getComputedStyle(wrap).getPropertyValue('--ps'))||1}
function applyP(){if(!P)return;wrap.style.left=P.x+'%';wrap.style.top=P.y+'%';wrap.style.bottom='auto';
 wrap.style.setProperty('--ps',P.s)}
function pct(){return{x:wrap.offsetLeft/innerWidth*100,y:wrap.offsetTop/innerHeight*100}}
function clampP(){var p=pct(),hw=wrap.offsetWidth/2/innerWidth*100,hh=wrap.offsetHeight/innerHeight*100;
 wrap.style.left=Math.min(100-hw,Math.max(hw,p.x))+'%';
 wrap.style.top=Math.min(100-hh,Math.max(0,p.y))+'%'}
function saveP(){P={x:pct().x,y:pct().y,s:sc()};store.set(PKEY,JSON.stringify(P))}
function syncUI(){var v=Math.round(sc()*100);rng.value=v;pval.textContent=v+'%'}
function setS(v){v=Math.min(200,Math.max(60,v));wrap.style.setProperty('--ps',(v/100).toFixed(2));
 clampP();syncUI();saveP()}
applyP();

function toggleEdit(){edit=!edit;board.classList.toggle('edit',edit);
 wrap.classList.toggle('edit',edit);document.body.classList.toggle('edit',edit);
 document.getElementById('gear').textContent=edit?'OK':'EDITAR';render();if(edit)syncUI()}
document.getElementById('gear').onclick=toggleEdit;
board.addEventListener('dblclick',()=>{if(!edit)toggleEdit()});

/* mouse em qualquer lugar revela o botão EDITAR (some após 3s parado) */
let hideT=null;
function gearLive(){if(edit)return;wrap.classList.add('live');clearTimeout(hideT);
 hideT=setTimeout(()=>wrap.classList.remove('live'),3000)}
document.addEventListener('mousemove',gearLive,{passive:true});
document.body.addEventListener('mouseleave',()=>{if(!edit)wrap.classList.remove('live')});
setTimeout(()=>{wrap.classList.add('live');setTimeout(()=>{if(!edit)wrap.classList.remove('live')},6000)},700);

/* teclado: E alterna edição; em edição: +/− tamanho · setas mover · R reset posição */
document.addEventListener('keydown',e=>{
 if((e.target&&e.target.tagName)==='INPUT'){if(e.key==='Escape')e.target.blur();return}
 if(e.key==='Escape'&&edit){toggleEdit();return}
 var k=e.key.toLowerCase();
 if(k==='e'){toggleEdit();return}
 if(!edit)return;
 if(k==='+'||k==='='){setS(sc()*100+5)}
 else if(k==='-'||k==='_'){setS(sc()*100-5)}
 else if(k==='r'){store.set(PKEY,null);location.reload()}
 else if(k.indexOf('arrow')===0){var p=pct(),d=e.shiftKey?2:.5;
  if(k==='arrowleft')wrap.style.left=(p.x-d)+'%';
  if(k==='arrowright')wrap.style.left=(p.x+d)+'%';
  if(k==='arrowup')wrap.style.top=(p.y-d)+'%';
  if(k==='arrowdown')wrap.style.top=(p.y+d)+'%';
  clampP();saveP();e.preventDefault()}
});
/* scroll sobre o widget = tamanho */
wrap.addEventListener('wheel',function(e){if(!edit)return;
 if(e.target&&e.target.closest&&e.target.closest('.bar,.gear'))return;
 e.preventDefault();setS(sc()*100+(e.deltaY<0?5:-5))},{passive:false});
/* slider + botões (repetem ao segurar) */
rng.addEventListener('input',function(){setS(+rng.value)});
function hold(id,fn){var b=document.getElementById(id),iv=null;
 function stop(){if(iv){clearInterval(iv);iv=null}}
 b.addEventListener('pointerdown',function(e){e.preventDefault();fn();iv=setInterval(fn,110)});
 ['pointerup','pointerleave','pointercancel'].forEach(function(ev){b.addEventListener(ev,stop)})}
hold('psub',function(){setS(sc()*100-5)});
hold('padd',function(){setS(sc()*100+5)});
document.getElementById('prst').onclick=function(){store.set(PKEY,null);location.reload()};
/* arrastar o widget = mover (ignora campos e botão) */
wrap.addEventListener('pointerdown',function(e){
 if(!edit)return;
 if(e.target&&(e.target.tagName==='INPUT'||(e.target.closest&&e.target.closest('.gear,.bar'))))return;
 e.preventDefault();try{wrap.setPointerCapture(e.pointerId)}catch(x){}
 var p=pct(),sx=e.clientX,sy=e.clientY;
 function mv(e2){wrap.style.left=(p.x+(e2.clientX-sx)/innerWidth*100)+'%';
  wrap.style.top=(p.y+(e2.clientY-sy)/innerHeight*100)+'%';wrap.style.bottom='auto';clampP()}
 function up(){saveP();removeEventListener('pointermove',mv);removeEventListener('pointerup',up)}
 addEventListener('pointermove',mv);addEventListener('pointerup',up)});
render();
</script></body></html>"""

pt = PARTY.replace("@@ORBIT9@@", ORBIT9).replace("@@C6@@", C6).replace("@@C5@@", C5).replace("@@ICON@@", MINI96)
open(OUT + "overlay/party-tracker.html", "w").write(pt)
print("party-tracker.html (v3 · ajustável + Visão do: + animações) ok (" + str(len(pt) // 1024) + " KB)")
