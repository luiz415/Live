#!/usr/bin/env python3
"""Alertas v4 — INTENSIDADE MÁXIMA por tier.
T1 FOLLOW: ripple triplo do emblema + pontos ascendentes + streaks de entrada + scanline interna
T2 SUB: raios cônicos girando + 2 órbitas com satélites + 12 shards + pulso duplo de borda + feixes + pop do emblema
T3 TIP: 24 moedas (3 tamanhos/profundidade) + onda em tela cheia + choque horizontal + faíscas + jitter + métrica pulsante
T4 RAID: intro de 3,3s (escurecimento + chevrons de perigo + 3 ecos fantasma + palavra glitch + tempestade de 18 shards +
strobe x8 + barras convergentes) → banner com shake contínuo, radar, glowline, faíscas e vinheta pulsante"""
import base64, os, random

L = "/home/user/twitch-pro/logos/final/"
OUT = "/home/user/twitch-pro/assets/alertas/"
V4 = OUT + "streamelements/v4/"
os.makedirs(V4, exist_ok=True)
MINI96 = base64.b64encode(open(L + "mini-96.png", "rb").read()).decode()
random.seed(42)

CSS = """/* ═══ EXORISERVICE · CSS v4 MÁXIMO (aba CSS — igual para todos os tipos) ═══ */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Chakra+Petch:wght@500;600&display=swap');
.xal{--acid:#B4FF00;--toxic:#5C9900;--txt:#F2FFE8;--txt2:#9AA69A;position:relative;display:flex;align-items:center;gap:24px;
 width:860px;padding:22px 36px;background:rgba(6,8,6,.93);border:1px solid rgba(92,153,0,.85);
 clip-path:polygon(20px 0,100% 0,100% calc(100% - 20px),calc(100% - 20px) 100%,0 100%,0 20px);
 font-family:'Chakra Petch',sans-serif;box-shadow:0 0 34px rgba(180,255,0,.14),inset 0 0 30px rgba(23,51,0,.25);
 animation:xin .55s cubic-bezier(.2,.9,.3,1.2) both,xout .45s 5.6s both}
.xal::before{content:'';position:absolute;left:0;top:0;bottom:0;width:6px;
 background:linear-gradient(180deg,var(--acid),var(--toxic));animation:volt 3s steps(3) infinite}
.xal::after{content:'';position:absolute;left:-120%;top:0;bottom:0;width:60%;
 background:linear-gradient(90deg,transparent,rgba(180,255,0,.10),transparent);animation:sweep 2.6s .3s linear infinite}
@keyframes sweep{to{left:160%}}
@keyframes volt{50%{filter:brightness(1.8)}}
@keyframes xin{from{opacity:0;transform:translateX(-90px) skewX(-4deg)}to{opacity:1;transform:none}}
@keyframes xout{to{opacity:0;transform:translateX(70px) skewX(3deg)}}
.xal .hexf{position:relative;width:110px;height:110px;flex:0 0 110px;display:flex;align-items:center;justify-content:center}
.xal .hexf img{width:72px;height:72px;position:relative;z-index:2;filter:drop-shadow(0 0 10px rgba(180,255,0,.5))}
.xal .hexf svg{position:absolute;fill:none;stroke:var(--toxic);stroke-width:1.4;stroke-dasharray:10 6;animation:spin 10s linear infinite;opacity:.9}
.xal .hexf svg.b{stroke:var(--acid);stroke-dasharray:2 9;animation:spin 16s linear infinite reverse;opacity:.5}
@keyframes spin{to{transform:rotate(360deg)}}
.xal .mid{flex:1;min-width:0}
.xal .kind{font-size:17px;font-weight:600;letter-spacing:.34em;color:var(--acid);text-transform:uppercase;white-space:nowrap;overflow:hidden}
.xal .name{position:relative;font-family:'Orbitron',sans-serif;font-weight:900;font-size:38px;color:var(--txt);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-shadow:0 0 22px rgba(180,255,0,.25)}
.xal .name::before,.xal .name::after{content:attr(data-t);position:absolute;left:0;top:0;width:100%;opacity:0;pointer-events:none}
.xal .name::before{color:var(--toxic)}
.xal .name::after{color:rgba(255,255,255,.45)}
@keyframes ng1{0%,88%,100%{opacity:0}90%{opacity:.85;transform:translate(-4px,-2px);clip-path:inset(10% 0 60% 0)}94%{opacity:.85;transform:translate(3px,1px);clip-path:inset(64% 0 6% 0)}}
@keyframes ng2{0%,88%,100%{opacity:0}91%{opacity:.7;transform:translate(4px,2px);clip-path:inset(58% 0 12% 0)}95%{opacity:.7;transform:translate(-3px,-1px);clip-path:inset(6% 0 62% 0)}}
.xal .msg{font-size:15px;font-weight:500;color:var(--txt2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:3px}
.xal .right{text-align:right;flex:0 0 auto}
.xal .metric{font-family:'Orbitron',sans-serif;font-weight:900;font-size:44px;color:var(--acid);text-shadow:0 0 26px rgba(180,255,0,.45);line-height:1}
.xal .mlabel{font-size:12px;font-weight:600;letter-spacing:.3em;color:var(--txt2);text-transform:uppercase;margin-top:5px}
/* camadas globais novas */
.bgrid{position:absolute;inset:0;pointer-events:none;opacity:.12;
 background-image:radial-gradient(rgba(180,255,0,.55) 1px,transparent 1.6px);background-size:26px 22px;
 -webkit-mask-image:linear-gradient(90deg,transparent,#000 35% 75%,transparent);mask-image:linear-gradient(90deg,transparent,#000 35% 75%,transparent)}
.sideR{position:absolute;right:0;top:0;bottom:0;width:6px;background:linear-gradient(180deg,var(--toxic),var(--acid));animation:volt 3s steps(3) infinite;opacity:.65}
.bk{position:absolute;width:18px;height:18px;border:2px solid rgba(180,255,0,.5);pointer-events:none}
.bk1{top:7px;right:26px;border-right:0;border-bottom:0}.bk2{bottom:7px;right:26px;border-left:0;border-top:0}
.scanx{position:absolute;left:0;right:0;top:-30%;height:26%;pointer-events:none;
 background:linear-gradient(180deg,transparent,rgba(180,255,0,.08),transparent);animation:scanx 2.7s linear infinite}
@keyframes scanx{to{transform:translateY(560%)}}

/* ══ T1 · FOLLOW — ripple + pontos + streaks ══ */
.t1{width:800px;animation:xin .5s cubic-bezier(.2,.9,.3,1.25) both,xout .4s 5.6s both}
.t1 .name{font-size:34px}
.t1 .name::before{animation:ng1 3.8s .3s steps(2) infinite}
.t1 .name::after{animation:ng2 3.8s .3s steps(2) infinite}
.t1 .hexf svg{animation-duration:13s}.t1 .hexf svg.b{animation-duration:19s}
.rip{position:absolute;left:55px;top:50%;width:70px;height:70px;margin:-35px;border:2px solid rgba(180,255,0,.55);border-radius:50%;animation:rip 1.7s ease-out infinite;pointer-events:none}
.rip.d2{animation-delay:.57s}.rip.d3{animation-delay:1.14s}
@keyframes rip{0%{transform:scale(.4);opacity:.9}100%{transform:scale(2.7);opacity:0}}
.rdot{position:absolute;bottom:10px;width:4px;height:4px;border-radius:50%;background:var(--acid);box-shadow:0 0 9px var(--acid);animation:rise2 2.4s linear infinite;pointer-events:none}
@keyframes rise2{0%{transform:translateY(0);opacity:0}12%{opacity:.9}100%{transform:translateY(-140px);opacity:0}}
.streak{position:absolute;height:3px;width:90px;background:linear-gradient(90deg,transparent,var(--acid));box-shadow:0 0 12px rgba(180,255,0,.6);animation:stk .7s ease-out both;pointer-events:none}
@keyframes stk{0%{left:-110px;opacity:1}100%{left:-14px;opacity:0}}

/* ══ T2 · SUB — raios + órbitas + shards + pulso duplo + feixes + pop ══ */
.t2 .name::before{animation:ng1 2.6s .2s steps(2) infinite}
.t2 .name::after{animation:ng2 2.6s .2s steps(2) infinite}
.t2 .hexf img{animation:pop .9s cubic-bezier(.2,.9,.3,1.5) both}
@keyframes pop{0%{transform:scale(.35)}62%{transform:scale(1.22)}100%{transform:scale(1)}}
.rays{position:absolute;left:55px;top:50%;width:160px;height:160px;margin:-80px;border-radius:50%;pointer-events:none;
 background:repeating-conic-gradient(rgba(180,255,0,.15) 0 7deg,transparent 7deg 26deg);filter:blur(1px);
 animation:spin 6.5s linear infinite}
.orbit{position:absolute;left:55px;top:50%;width:96px;height:96px;margin:-48px;border:1px dashed rgba(180,255,0,.42);border-radius:50%;animation:spin 3.6s linear infinite;pointer-events:none}
.orbit::before{content:'';position:absolute;top:-4px;left:50%;width:8px;height:8px;margin-left:-4px;background:var(--acid);border-radius:50%;box-shadow:0 0 10px var(--acid)}
.orbit.o2{width:124px;height:124px;margin:-62px;animation-duration:6s;animation-direction:reverse}
.orbit.o2::before{background:var(--toxic);box-shadow:0 0 10px var(--toxic)}
.beam2{position:absolute;top:0;bottom:0;width:64px;background:linear-gradient(90deg,transparent,rgba(180,255,0,.11),transparent);animation:beamx 2.1s linear infinite;pointer-events:none}
@keyframes beamx{from{left:-25%}to{left:112%}}
.edgep{position:absolute;inset:-7px;border:1px solid rgba(180,255,0,0);pointer-events:none;animation:edgep 1.6s ease-out infinite}
.edgep.e2{animation-delay:.8s}
@keyframes edgep{0%{opacity:0;transform:scale(1.05)}20%{opacity:1;border-color:rgba(180,255,0,.8);box-shadow:0 0 26px rgba(180,255,0,.3),inset 0 0 18px rgba(180,255,0,.12)}100%{opacity:0;transform:scale(1)}}
.shx{position:absolute;left:30px;top:50%;width:0;height:0;pointer-events:none;
 border-left:11px solid transparent;border-right:11px solid transparent;border-bottom:19px solid var(--acid);
 animation:shardfly .95s cubic-bezier(.15,.8,.3,1) both}
.shx.g{border-bottom-color:var(--toxic)}.shx.s{border-left-width:7px;border-right-width:7px;border-bottom-width:12px}
@keyframes shardfly{from{transform:translate(0,0) rotate(0);opacity:1}to{transform:translate(var(--dx),var(--dy)) rotate(210deg);opacity:0}}

/* ══ T3 · TIP/BITS — moedas densas + onda + choque + faíscas + jitter ══ */
.t3{border-color:rgba(180,255,0,.95);box-shadow:0 0 52px rgba(180,255,0,.28),inset 0 0 34px rgba(23,51,0,.28);
 animation:xin .55s cubic-bezier(.2,.9,.3,1.25) both,jit3 .42s .5s steps(2) 10,xout .45s 7s both}
@keyframes jit3{50%{transform:translate(2px,-2px)}}
.t3 .name::before{animation:ng1 1.9s .2s steps(2) infinite}
.t3 .name::after{animation:ng2 1.9s .2s steps(2) infinite}
.t3 .metric{font-size:50px;animation:mpulse 1.15s ease-in-out infinite;display:inline-block}
@keyframes mpulse{50%{text-shadow:0 0 54px rgba(180,255,0,1);transform:scale(1.07)}}
.coin{position:absolute;top:-56px;width:15px;height:15px;border-radius:50%;pointer-events:none;
 background:radial-gradient(circle at 35% 35%,#eaffca,var(--acid) 45%,var(--toxic));
 box-shadow:0 0 12px rgba(180,255,0,.65);animation:coinfall linear infinite}
.coin.big{width:24px;height:24px;filter:blur(1px)}
.coin.small{width:9px;height:9px}
@keyframes coinfall{0%{transform:translateY(0) rotate(0);opacity:0}7%{opacity:1}100%{transform:translateY(340px) rotate(280deg);opacity:0}}
.wave{position:fixed;left:-35%;top:50%;width:55%;height:360px;transform:translateY(-50%);pointer-events:none;z-index:0;
 background:radial-gradient(ellipse at center,rgba(180,255,0,.15),transparent 66%);animation:wavex 2.3s ease-out infinite}
@keyframes wavex{from{left:-38%}to{left:108%}}
.shock{position:absolute;left:0;right:0;top:50%;height:2px;pointer-events:none;
 background:linear-gradient(90deg,transparent,var(--acid),transparent);box-shadow:0 0 24px rgba(180,255,0,.75);animation:shock 1.05s ease-out infinite}
.shock.k2{animation-delay:.5s}
@keyframes shock{0%{transform:scaleX(.15);opacity:1}100%{transform:scaleX(1.3);opacity:0}}
.spark{position:absolute;color:var(--acid);text-shadow:0 0 14px var(--acid);animation:spark 1.4s ease-out infinite;pointer-events:none;font-size:22px}
.spark.s2{animation-delay:.7s}
@keyframes spark{0%{transform:scale(0) rotate(0);opacity:1}100%{transform:scale(1.9) rotate(140deg);opacity:0}}
.energysweep{position:absolute;left:0;right:0;bottom:-16px;height:4px;pointer-events:none;
 background:linear-gradient(90deg,transparent,var(--acid),var(--toxic),var(--acid),transparent);
 background-size:200% 100%;animation:esweep 1.3s linear infinite;box-shadow:0 0 18px rgba(180,255,0,.6)}
@keyframes esweep{to{background-position:-200% 0}}

/* ══ T4 · RAID — MÁXIMO ABSOLUTO ══ */
.t4{border-color:var(--acid);box-shadow:0 0 70px rgba(180,255,0,.38),inset 0 0 34px rgba(23,51,0,.3);
 animation:xin .42s cubic-bezier(.2,.9,.3,1.3) both,shk4 .34s linear infinite,xout .5s 9s both}
@keyframes shk4{0%{transform:translate(2px,-1px)}25%{transform:translate(-2px,2px)}50%{transform:translate(2px,1px) skewX(.35deg)}75%{transform:translate(-1px,-2px)}}
.t4 .name{font-size:42px}
.t4 .name::before{animation:ng1 .85s .1s steps(2) infinite}
.t4 .name::after{animation:ng2 .85s .1s steps(2) infinite}
.t4 .metric{font-size:54px}
.t4 .hexf svg{animation-duration:4.5s}.t4 .hexf svg.b{animation-duration:7s;stroke:var(--acid)}
.t4 .hexf img{animation:pop .8s cubic-bezier(.2,.9,.3,1.5) both,mpulse2 1.6s .8s ease-in-out infinite}
@keyframes mpulse2{50%{filter:drop-shadow(0 0 18px rgba(180,255,0,.95)) drop-shadow(-4px 0 0 rgba(92,153,0,.6))}}
.glowline{position:absolute;left:0;right:0;top:0;height:2px;background:linear-gradient(90deg,transparent,var(--acid),transparent);animation:gline 1.2s steps(2) infinite;pointer-events:none}
@keyframes gline{0%,100%{opacity:.25;transform:scaleX(.55)}50%{opacity:1;transform:scaleX(1.05)}}
.radar{position:absolute;left:55px;top:50%;width:190px;height:190px;margin:-95px;border-radius:50%;border:1px solid rgba(180,255,0,.4);animation:radar 1.9s linear infinite;pointer-events:none}
.radar.r2{animation-delay:.95s}
@keyframes radar{0%{transform:scale(.45);opacity:.9}100%{transform:scale(1.8);opacity:0}}
.spk{position:absolute;bottom:4px;width:6px;height:7px;background:var(--acid);clip-path:polygon(50% 0,100% 100%,0 100%);animation:spkfly .9s linear infinite;pointer-events:none}
@keyframes spkfly{0%{transform:translateY(0);opacity:1}100%{transform:translateY(-80px) rotate(190deg);opacity:0}}
.tvig{position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at center,transparent 52%,rgba(180,255,0,.13) 100%);animation:vigf 1s ease-in-out infinite}
@keyframes vigf{50%{opacity:.35}}
/* ── intro 3,3s em tela cheia ── */
.xintro{position:fixed;inset:0;z-index:9;pointer-events:none;animation:introout 3.3s .05s forwards}
@keyframes introout{0%,82%{opacity:1}100%{opacity:0;visibility:hidden}}
.idim{position:absolute;inset:0;background:rgba(0,0,0,.6);animation:idim 3.3s both}
@keyframes idim{0%{opacity:0}14%{opacity:1}82%{opacity:1}100%{opacity:0}}
.chev{position:absolute;left:0;right:0;height:36px;opacity:.85;
 background:repeating-linear-gradient(135deg,rgba(180,255,0,.9) 0 24px,rgba(6,8,6,.2) 24px 48px);
 animation:chevm .8s linear infinite}
.chev.t{top:0;-webkit-mask-image:linear-gradient(180deg,#000,transparent);mask-image:linear-gradient(180deg,#000,transparent)}
.chev.b{bottom:0;-webkit-mask-image:linear-gradient(0deg,#000,transparent);mask-image:linear-gradient(0deg,#000,transparent)}
@keyframes chevm{to{background-position:96px 0}}
.ighost{position:absolute;left:50%;top:44%;width:56vmin;height:56vmin;transform:translate(-50%,-50%) scale(.55);opacity:0;
 filter:drop-shadow(0 0 46px rgba(180,255,0,.6));animation:igh 3.3s cubic-bezier(.2,.8,.3,1) both}
@keyframes igh{0%{opacity:0;transform:translate(-50%,-50%) scale(.5)}16%{opacity:.95}55%{opacity:.5}100%{opacity:0;transform:translate(-50%,-50%) scale(1.75)}}
.ighost.e1{animation-name:igh1}.ighost.e2{animation-name:igh2}
@keyframes igh1{0%{opacity:0}16%{opacity:.55;transform:translate(-54%,-50%) scale(.62)}60%{opacity:0;transform:translate(-70%,-50%) scale(1.1)}100%{opacity:0}}
@keyframes igh2{0%{opacity:0}16%{opacity:.45;transform:translate(-46%,-50%) scale(.62)}60%{opacity:0;transform:translate(-30%,-50%) scale(1.1)}100%{opacity:0}}
.iword{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);font-family:'Orbitron',sans-serif;font-weight:900;
 font-size:14vmin;color:var(--acid);letter-spacing:.3em;padding-left:.3em;text-shadow:0 0 7vmin rgba(180,255,0,.7);animation:iwd 3.3s both;white-space:nowrap}
@keyframes iwd{0%{opacity:0;transform:translate(-50%,-50%) scale(1.9);filter:blur(9px);letter-spacing:.8em}
 16%{opacity:1;transform:translate(-50%,-50%) scale(1);filter:blur(0);letter-spacing:.3em}
 24%{transform:translate(-51.5%,-50%) scale(1.04)}30%{transform:translate(-48.5%,-50%) scale(.99)}
 36%{transform:translate(-50%,-50%) scale(1.02)}82%{opacity:1}100%{opacity:0;transform:translate(-50%,-50%) scale(.9)}}
.isub{position:absolute;left:50%;top:58%;transform:translateX(-50%);font-family:'Chakra Petch',sans-serif;font-weight:600;
 font-size:2.6vmin;color:#F2FFE8;letter-spacing:.6em;padding-left:.6em;opacity:0;animation:isub 3.3s .5s both;white-space:nowrap}
@keyframes isub{0%{opacity:0;transform:translateX(-50%) translateY(14px)}22%{opacity:.95;transform:translateX(-50%)}82%{opacity:.95}100%{opacity:0}}
.storm{position:fixed;top:-8%;pointer-events:none;border-left:9px solid transparent;border-right:9px solid transparent;
 border-bottom:16px solid var(--acid);animation:stormfly 1.5s linear both}
.storm.g{border-bottom-color:var(--toxic)}
@keyframes stormfly{from{transform:translate(0,0) rotate(20deg);opacity:0}12%{opacity:1}to{transform:translate(var(--sx),118vh) rotate(240deg);opacity:0}}
.istrobe{position:absolute;inset:0;background:#F2FFE8;opacity:0;animation:istr .3s steps(2) 14}
@keyframes istr{50%{opacity:.12}}
.conv{position:absolute;left:0;right:0;height:5px;background:linear-gradient(90deg,transparent,var(--acid) 45%,var(--toxic) 55%,transparent);
 box-shadow:0 0 26px rgba(180,255,0,.7);animation:conv 3.3s cubic-bezier(.6,0,.3,1) both}
.conv.t{top:0;animation-name:convt}.conv.b{bottom:0;animation-name:convb}
@keyframes convt{0%{transform:translateY(0) scaleX(.3)}70%{transform:translateY(38vh) scaleX(1)}82%{transform:translateY(38vh) scaleX(1.2);opacity:1}100%{opacity:0;transform:translateY(38vh) scaleX(1.3)}}
@keyframes convb{0%{transform:translateY(0) scaleX(.3)}70%{transform:translateY(-38vh) scaleX(1)}82%{transform:translateY(-38vh) scaleX(1.2);opacity:1}100%{opacity:0;transform:translateY(-38vh) scaleX(1.3)}}
"""

HEXF = ('<div class="hexf"><svg width="96" height="96" viewBox="0 0 100 100"><polygon points="50,3 94,27 94,73 50,97 6,73 6,27"/></svg>'
        '<svg class="b" width="110" height="110" viewBox="0 0 100 100"><polygon points="50,3 94,27 94,73 50,97 6,73 6,27"/></svg>'
        f'<img src="data:image/png;base64,{MINI96}" alt=""></div>')

GLOBAL = '<div class="bgrid"></div><div class="sideR"></div><div class="bk bk1"></div><div class="bk bk2"></div><div class="scanx"></div>'

# ── FX por tier ──
T1_FX = (''.join(f'<div class="rip{" d2" if i==1 else " d3" if i==2 else ""}"></div>' for i in range(3))
         + ''.join(f'<div class="rdot" style="left:{40+i*95}px;animation-delay:{(i*0.3):.2f}s"></div>' for i in range(9))
         + '<div class="streak" style="top:24px"></div><div class="streak" style="top:64px;animation-delay:.08s"></div><div class="streak" style="top:104px;animation-delay:.16s"></div>')

SHARD_DIRS = [(-200,-130),(-280,-40),(-250,100),(-160,160),(-100,-170),(-70,180),(-320,60),(-130,-110)]
T2_SHARDS = "".join(
    f'<div class="shx{" g" if i%2 else ""}{" s" if i%3==2 else ""}" style="--dx:{dx}px;--dy:{dy}px;animation-delay:{i*0.05:.2f}s"></div>'
    for i, (dx, dy) in enumerate(SHARD_DIRS))
T2_FX = (f'<div class="rays"></div><div class="orbit"></div><div class="orbit o2"></div>'
         + T2_SHARDS + '<div class="edgep"></div><div class="edgep e2"></div>'
         + '<div class="beam2" style="animation-delay:0s"></div><div class="beam2" style="animation-delay:1.05s"></div>')

COIN_COLS = [30, 90, 150, 215, 275, 335, 395, 455, 515, 575, 635, 695, 745, 790, 820, 60, 180, 300, 420, 540, 660, 760, 110, 360]
T3_COINS = "".join(
    f'<div class="coin{" big" if i%5==0 else " small" if i%3==0 else ""}" style="left:{l}px;animation-duration:{1.1+((i*37)%90)/100:.2f}s;animation-delay:{((i*53)%120)/100:.2f}s"></div>'
    for i, l in enumerate(COIN_COLS))
T3_FX = ('<div class="wave"></div>' + T3_COINS
         + '<div class="shock"></div><div class="shock k2"></div>'
         + '<div class="spark" style="right:88px;top:16px">✦</div><div class="spark s2" style="right:60px;bottom:22px">✦</div>'
         + '<div class="energysweep"></div>')

STORM = "".join(
    f'<div class="storm{" g" if i%2 else ""}" style="left:{4+((i*67)%92)}%;--sx:{-160+((i*97)%320)}px;animation-delay:{(0.9+(i*0.09)):.2f}s"></div>'
    for i in range(18))
T4_INTRO = ('<div class="xintro"><div class="idim"></div><div class="chev t"></div><div class="chev b"></div>'
            f'<img class="ighost" src="data:image/png;base64,{MINI96}" alt="">'
            f'<img class="ighost e1" src="data:image/png;base64,{MINI96}" alt="">'
            f'<img class="ighost e2" src="data:image/png;base64,{MINI96}" alt="">'
            '<div class="iword">RAID!</div><div class="isub">VISITANTES A CAMINHO</div>'
            + STORM + '<div class="istrobe"></div><div class="conv t"></div><div class="conv b"></div></div>')
T4_FX = T4_INTRO + '<div class="tvig"></div><div class="glowline"></div><div class="radar"></div><div class="radar r2"></div>' + "".join(
    f'<div class="spk" style="left:{60+i*130}px;animation-delay:{(i*0.18):.2f}s"></div>' for i in range(7))

ALERTS = [
    ("follow", "t1", "novo seguidor", "{{name}}", "+1", "seguidor", "seja bem-vindo à comunidade!", T1_FX, 6),
    ("sub",    "t2", "sub novo", "{{name}}", "{{tier}}", "tier", "obrigado pelo apoio!", T2_FX, 6),
    ("resub",  "t2", "re-sub", "{{name}}", "{{months}}", "meses", "{{message}}", T2_FX, 6),
    ("gift",   "t2", "gift subs", "{{sender}}", "{{amount}}", "gifts", "obrigado por espalhar a comunidade!", T2_FX, 6),
    ("bits",   "t3", "bits", "{{name}}", "{{amount}}", "bits", "obrigado pelos bits!", T3_FX, 7),
    ("tip",    "t3", "doação", "{{name}}", "{{amount}}", "obrigado!", "{{message}}", T3_FX, 7),
    ("raid",   "t4", "raid!", "{{name}}", "{{viewers}}", "raiders", "que venha a horda!", T4_FX, 10),
]

for arq, tier, kind, nome, metrica, label, msg, fx, dur in ALERTS:
    frag = (f"<!-- EXORISERVICE v4 MÁXIMO · aba HTML do alerta {arq.upper()} (tier {tier[-1]}) — substitua TODO o conteúdo padrão -->\n"
            f"<!-- Alert Duration sugerido: {dur}s -->\n"
            f'<div class="xal {tier}">\n'
            f'  {HEXF}\n'
            f'  <div class="mid">\n'
            f'    <div class="kind">{kind}</div>\n'
            f'    <div class="name" data-t="{nome}">{nome}</div>\n'
            f'    <div class="msg">{msg}</div>\n'
            f'  </div>\n'
            f'  <div class="right"><div class="metric">{metrica}</div><div class="mlabel">{label}</div></div>\n'
            f'  {GLOBAL}\n'
            f'  {fx}\n'
            f'</div>\n')
    open(V4 + f"1-ABA-HTML_{arq}.txt", "w").write(frag)
    print("•", f"1-ABA-HTML_{arq}.txt")

open(V4 + "2-ABA-CSS_geral-para-todos.txt", "w").write(CSS)
print("•", "2-ABA-CSS_geral-para-todos.txt")

# ═══ PREVIEW ═══
DEMOS = [("T1 · FOLLOW", "follow", "NovoViewer", "novo seguidor", "+1", "seguidor", "seja bem-vindo à comunidade!", T1_FX),
         ("T2 · SUB", "sub", "Subber", "sub novo", "T1", "tier", "obrigado pelo apoio!", T2_FX),
         ("T3 · TIP", "tip", "Apoiador", "doação", "R$ 50", "obrigado!", "apoio direto!", T3_FX),
         ("T4 · RAID", "raid", "RaidMaster", "raid!", "42", "raiders", "que venha a horda!", T4_FX)]

rows = []
for i, (cap, arq, nome, kind, met, lab, msg, fx) in enumerate(DEMOS):
    rows.append(f'<div class="demo"><div class="cap2">{cap}</div>'
                f'<div class="xal {arq}">{HEXF}<div class="mid"><div class="kind">{kind}</div>'
                f'<div class="name" data-t="{nome}">{nome}</div><div class="msg">{msg}</div></div>'
                f'<div class="right"><div class="metric">{met}</div><div class="mlabel">{lab}</div></div>{GLOBAL}{fx}</div></div>')

F = "/home/user/twitch-pro/assets/fonts/"
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
preview = ("<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>Alertas v4 MÁXIMO — exoriservice</title><style>"
           + CSS
           + "@font-face{font-family:Orbitron;font-weight:900;src:url(data:font/ttf;base64," + b64(F + "Orbitron-900.ttf") + ") format('truetype')}"
           + "@font-face{font-family:Chakra;font-weight:600;src:url(data:font/ttf;base64," + b64(F + "ChakraPetch-600.ttf") + ") format('truetype')}"
           + "@font-face{font-family:Chakra;font-weight:500;src:url(data:font/ttf;base64," + b64(F + "ChakraPetch-500.ttf") + ") format('truetype')}"
           + "body{background:#060806;display:flex;flex-direction:column;align-items:center;gap:52px;padding:70px 20px;font-family:'Chakra',monospace}"
           + "h1{font-family:'Orbitron';font-weight:900;color:#F2FFE8;font-size:24px;letter-spacing:.1em}"
           + "h1 b{color:#B4FF00}.sub{color:#9AA69A;font-size:13px;letter-spacing:.22em;margin-top:-36px}"
           + ".cap2{color:#5C9900;font-size:13px;font-weight:600;letter-spacing:.3em;margin-bottom:14px;text-align:center}"
           + ".demo{position:relative;width:860px}"
           + ".xal{position:relative}"
           + "</style></head><body><h1><b>EXORI</b>SERVICE · ALERTAS v4 — MÁXIMO</h1>"
           + "<div class='sub'>4 NÍVEIS · FOLLOW → SUB → TIP → RAID (ciclo reinicia a cada 12s)</div>"
           + "".join(rows)
           + "<script>setInterval(()=>{document.querySelectorAll('.demo').forEach(d=>{const h=d.innerHTML;d.innerHTML=h})},12000)</script>"
           + "</body></html>")
open(OUT + "preview-alertas.html", "w").write(preview)
print("preview-alertas.html ok")
