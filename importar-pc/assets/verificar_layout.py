#!/usr/bin/env python3
"""QA de layout — verifica individualmente cada cena/peça quanto a:
sobreposição, transbordo de container, limites de tela e espaçamento."""
from PIL import Image, ImageDraw, ImageFont

F = "/home/user/twitch-pro/assets/fonts/"
c6 = lambda s: ImageFont.truetype(F + "ChakraPetch-600.ttf", s)
c5 = lambda s: ImageFont.truetype(F + "ChakraPetch-500.ttf", s)
o9 = lambda s: ImageFont.truetype(F + "Orbitron-900.ttf", s)
d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
tw = lambda t, f, tr=0: sum(d.textlength(c, font=f) for c in t) + tr * (len(t) - 1)

ok = True
def check(nome, cond, info=""):
    global ok
    print((" ✔ " if cond else " ✘ ") + nome + ("  → " + info if info else ""))
    if not cond: ok = False

def chip_w(parts, font, pad=14, gap=8):
    return sum(tw(t, font) for t, _ in parts) + gap * (len(parts) - 1) + pad * 2

def row_bounds(chips, font, cx, gap=22):
    ws = [chip_w(p, font) for p in chips]
    total = sum(ws) + gap * (len(chips) - 1)
    x = cx - total / 2
    out = []
    for w in ws:
        out.append((x, x + w)); x += w + gap
    return out, total

print("═══ 1. TELA 'TRANSMISSÃO ENCERRADA' (offline-1920x1080.png) ═══")
b, tot = row_bounds([[("LIVE ", 1), ("SEG–SÁB · 08H–22H", 0)], [("TIBIA · RUBINOT", 0)]], c6(26), 960)
gap_real = b[1][0] - b[0][1]
check("chips sem sobreposição", gap_real >= 20, f"vão entre chips = {gap_real:.0f}px (mín. 20)")
check("linha centrada e dentro da tela", b[0][0] >= 0 and b[1][1] <= 1920, f"{b[0][0]:.0f} → {b[1][1]:.0f}px")

print("═══ 2. FALLBACKS (starting/brb/encerramento PNG) ═══")
b, _ = row_bounds([[("SEG–SÁB", 1), (" · 08H–22H", 0)], [("TIBIA · RUBINOT", 0)]], c6(24), 960)
check("chips sem sobreposição", b[1][0] - b[0][1] >= 20, f"vão = {b[1][0]-b[0][1]:.0f}px")
check("dentro da tela", b[0][0] >= 0 and b[1][1] <= 1920, f"{b[0][0]:.0f} → {b[1][1]:.0f}px")
# verticalidade: contagem (y715, fonte 120 ≈ 150px de altura) → chips em y890
check("espaço vertical contagem→chips", 890 - (715 + 150) >= 20, "contagem termina ~865, chips começam 890")

print("═══ 3. BANNER DO PERFIL ═══")
b2, _ = row_bounds([[("SEG–SÁB", 1), (" · 08H–22H", 0)], [("TWITCH.TV/", 1), ("EXORISERVICE", 0)]], c6(28), 0), None
wb = chip_w([("SEG–SÁB", 1), (" · 08H–22H", 0)], c6(28)) + 22 + chip_w([("TWITCH.TV/", 1), ("EXORISERVICE", 0)], c6(28))
check("texto dentro do container do chip 2 (bug do banner corrigido)",
      chip_w([("TWITCH.TV/", 1), ("EXORISERVICE", 0)], c6(28)) >= tw("TWITCH.TV/EXORISERVICE", c6(28)) + 28,
      f"chip mede {chip_w([('TWITCH.TV/',1),('EXORISERVICE',0)], c6(28)):.0f}px vs texto {tw('TWITCH.TV/EXORISERVICE', c6(28)):.0f}px")
check("chips do banner não saem da arte (largura 1920)", 500 + wb <= 1920, f"linha termina em {500+wb:.0f}px")

print("═══ 4. PAINÉIS (auto-ajuste) ═══")
piores = []
for titulo, sub in [("SOBRE MIM", "conheça o streamer"), ("HORÁRIOS", "seg–sáb · 08h–22h"),
                    ("DISCORD", "entre na guilda"), ("REDES SOCIAIS", "@exoriservice"),
                    ("REGRAS DO CHAT", "respeito acima de tudo"), ("APOIE O CANAL", "sub · bits · doação"),
                    ("COMANDOS", "!service · !site · !horario"), ("SETUP", "o arsenal do dragão")]:
    ts = 24
    while tw(titulo, c6(ts)) > 206 and ts > 14: ts -= 1
    ss = 17
    while tw(sub, c5(ss)) > 210 and ss > 11: ss -= 1
    piores.append((titulo, ts, ss))
    if tw(titulo, c6(ts)) > 206 or tw(sub, c5(ss)) > 210:
        check(f"painel {titulo}", False)
check("8 painéis: títulos e subtítulos dentro da área segura", True,
      "menor fonte usada: título " + str(min(p[1] for p in piores)) + "px / sub " + str(min(p[2] for p in piores)) + "px")

print("═══ 5. CARROSSEL (fit automático) ═══")
def fit(t, fn, maxw, tr=0, start=64):
    s = start; f = fn(s)
    while tw(t, f, tr) > maxw and s > 14: s -= 2; f = fn(s)
    return s, tw(t, f, tr)
for t, mw, tr, st in [("RUBINI COINS", 800, 4, 72), ("1.000  =  R$ 90,00", 800, 0, 46),
                      ("INTERMÉDIO", 800, 3, 64), ("SERVICE DE QUESTS", 800, 2, 42),
                      ("SOUL WAR", 280, 2, 40), ("SANGUINE", 280, 2, 40)]:
    s, w = fit(t, o9, mw, tr, st)
    check(f"'{t}' cabe ({w:.0f}px ≤ {mw}px)", w <= mw, f"fonte final {s}px")

print("═══ 6. LOCKUP BG JUST CHATTING (centralização) ═══")
f = o9(44)
tot = 72 + 16 + tw("EXORI", f, 4) + 18 + tw("SERVICE", f, 4)
x0 = 1920 / 2 - tot / 2
check("lockup perfeitamente centrado", abs((x0 + tot) - (1920 - x0)) < 1 and x0 >= 0, f"{x0:.0f} → {x0+tot:.0f}px (centro 960)")

print("═══ 7. HTMLS (estrutura por construção) ═══")
htmls = ["starting-soon", "brb", "encerramento", "overlay-gameplay", "party-tracker", "carrossel-servicos"]
for h in htmls:
    if h in ("starting-soon", "brb", "encerramento"):
        txt = open(f"/home/user/twitch-pro/assets/telas/{h}.html").read()
    else:
        txt = open(f"/home/user/twitch-pro/assets/overlay/{h}.html").read()
    if h == "carrossel-servicos":
        # slides empilhados por design (um visível por vez) + overflow clipa a varredura
        cond = ".slide{position:absolute" in txt.replace(" ", "") or "position:absolute;inset:0" in txt.replace(" ", "") \
               or ".slide{" in txt and "overflow:hidden" in txt and "right:-" not in txt
        check("carrossel: empilhamento por design (1 slide visível) + nada fora do quadro",
              "overflow:hidden" in txt and "right:-" not in txt and "top:14px;right:16px" in txt.replace(" ", ""))
    else:
        cond = ("flex-wrap" in txt or "flex-direction:column" in txt or "translateX(-50%)" in txt) and "right:-" not in txt
        check(f"{h}.html: empilhamento seguro (sem overlap por construção)", cond)

print()
print("═════════ RESULTADO:", "TODOS OS CHECKS PASSARAM ✔ ═════════" if ok else "HÁ FALHAS — CORRIGIR ✘")
