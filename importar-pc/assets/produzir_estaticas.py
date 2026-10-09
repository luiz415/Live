#!/usr/bin/env python3
"""Lote 4A — Artes estáticas: banner, offline, painéis, overlay PNG, fallbacks de telas."""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BG, SURF, SURF2 = (6, 8, 6), (18, 23, 18), (28, 36, 28)
ACID, TOXIC, FOREST = (180, 255, 0), (92, 153, 0), (23, 51, 0)
TXT, TXT2 = (242, 255, 232), (154, 166, 154)

F = "/home/user/twitch-pro/assets/fonts/"
o9 = lambda s: ImageFont.truetype(F + "Orbitron-900.ttf", s)
c6 = lambda s: ImageFont.truetype(F + "ChakraPetch-600.ttf", s)
c5 = lambda s: ImageFont.truetype(F + "ChakraPetch-500.ttf", s)

L = "/home/user/twitch-pro/logos/final/"
ICON = Image.open(L + "icone-512.png").convert("RGB")
OUT = "/home/user/twitch-pro/assets/"

def tracked(d, xy, text, font, fill, tr=0):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tr
    return x

def tw(d, text, font, tr=0):
    return sum(d.textlength(c, font=font) for c in text) + tr * (len(text) - 1)

def wordmark(d, x, y, size, tr=None, center_at=None):
    f = o9(size); tr = tr if tr is not None else size * 0.09
    w1, w2 = tw(d, "EXORI", f, tr), tw(d, "SERVICE", f, tr)
    if center_at is not None:
        x = center_at - (w1 + size * 0.35 + w2) / 2
    tracked(d, (x, y), "EXORI", f, ACID, tr)
    tracked(d, (x + w1 + size * 0.35, y), "SERVICE", f, TXT, tr)
    return w1 + size * 0.35 + w2

def base(w, h, grid_step=52, grid_alpha=28):
    """Fundo padrão: preto carbono + malha hexagonal sutil."""
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img, "RGBA")
    s = grid_step
    dx, dy = 1.5 * s, math.sqrt(3) / 2 * s
    for row, yy in enumerate(range(-s, h + int(dy), int(dy))):
        off = dx / 2 if row % 2 else 0
        for xx in range(-int(dx), w + int(dx), int(dx)):
            pts = [(xx + off + s * .25 + math.cos(math.radians(a)) * s * .52,
                    yy + math.sin(math.radians(a)) * s * .52) for a in range(0, 360, 60)]
            d.polygon(pts, outline=(16, 26, 10, grid_alpha))
    return img, d

def vignette(img, strength=140):
    w, h = img.size
    grad = Image.radial_gradient("L").resize((w, h))
    dark = Image.new("RGB", (w, h), (0, 0, 0))
    mask = grad.point(lambda p: int(p / 255 * strength))
    img.paste(dark, (0, 0), mask)
    return img

def glow_paste(img, piece, box, blur=18, color=None):
    """Cola a peça com halo verde atrás."""
    if color:
        pad = blur * 3
        gl = Image.new("RGB", (piece.width + pad * 2, piece.height + pad * 2), color)
        m = piece.split()[3].point(lambda p: 110) if piece.mode == "RGBA" else None
        big = img.copy()
        bd = ImageDraw.Draw(big)
        return big
    img.paste(piece, box, piece if piece.mode == "RGBA" else None)

def shard_cluster(d, cx, cy, n, size, flip=False, alpha=120):
    for i in range(n):
        s = size * (1 - i * 0.22)
        x = cx + i * size * 0.5 * (-1 if flip else 1)
        pts = [(x, cy), (x + s * .55 * (-1 if flip else 1), cy - s * .35), (x + s * .3 * (-1 if flip else 1), cy + s * .3)]
        col = [ACID, TOXIC, FOREST][i % 3]
        d.polygon(pts, fill=col + (alpha - i * 30,), outline=col + (min(255, alpha + 40),))

def chip_box(d, x, y, parts, font, pad=14, gap=8):
    """Chip chanfrado com uma ou mais partes [(texto, é_acido)]. MEDIDO — nunca transborda."""
    wtext = sum(tw(d, t, font) for t, _ in parts) + gap * (len(parts) - 1)
    w = wtext + pad * 2
    h = font.size + pad * 2
    d.polygon([(x + 10, y), (x + w, y), (x + w, y + h - 10), (x + w - 10, y + h), (x, y + h), (x, y + 10)],
              fill=(12, 17, 12, 240), outline=TOXIC + (200,), width=2)
    tx = x + pad
    for i, (t, acid) in enumerate(parts):
        tx = tracked(d, (tx, y + pad + 3), t, font, ACID if acid else TXT, 0)
        if i < len(parts) - 1:
            tx += gap
    return w

def chip_row(d, y, chips, font, cx=None, left=None, pad=14, gap=22):
    """Linha de chips MEDIDA: larguras reais, espaçamento fixo, centralizada em cx (ou a partir de left)."""
    widths = [sum(tw(d, t, font) for t, _ in parts) + 8 * (len(parts) - 1) + pad * 2 for parts in chips]
    total = sum(widths) + gap * (len(chips) - 1)
    x = (cx - total / 2) if cx is not None else left
    for parts, w in zip(chips, widths):
        chip_box(d, x, y, parts, font, pad)
        x += w + gap
    return total

def energy_bar(d, x0, x1, y, h=6):
    for xx in range(int(x0), int(x1)):
        t = (xx - x0) / max(1, (x1 - x0))
        col = tuple(int(ACID[i] * (1 - t) + TOXIC[i] * t) for i in range(3))
        d.line([(xx, y), (xx, y + h)], fill=col)

# ═══════════════ 1) BANNER DO PERFIL 1920×480 ═══════════════
def banner():
    img, d = base(1920, 480, grid_step=46)
    # halo do emblema
    emb = ICON.resize((330, 330), Image.LANCZOS)
    halo = Image.new("RGB", (500, 500), (10, 24, 2))
    hm = emb.copy().convert("L").point(lambda p: 90)
    hmask = hm.filter(ImageFilter.GaussianBlur(60))
    img.paste((0, 0, 0), (0, 0), hmask.resize((500, 500)).convert("L"))
    img.paste(emb, (105, 75))
    d = ImageDraw.Draw(img, "RGBA")
    wordmark(d, 0, 165, 84, center_at=560)
    chip_row(d, 285, [[("TIBIA", True), (" · RUBINOT · RPG ONLINE", False)]], c6(30), left=500)
    chip_row(d, 345, [[("SEG–SÁB", True), (" · 08H–22H", False)],
                      [("TWITCH.TV/", True), ("EXORISERVICE", False)]], c6(28), left=500)
    shard_cluster(d, 1560, 90, 4, 120, flip=True)
    shard_cluster(d, 1700, 300, 3, 90, flip=True)
    energy_bar(d, 0, 1920, 0, 8)
    energy_bar(d, 0, 1920, 474, 4)
    img = vignette(img, 110)
    img.save(OUT + "extras/banner-perfil-1920x480.png")
    print("banner ok")

# ═══════════════ 2) OFFLINE SCREEN 1920×1080 ═══════════════
def offline():
    img, d = base(1920, 1080)
    emb = ICON.resize((430, 430), Image.LANCZOS)
    img.paste(emb, (745, 165))
    d = ImageDraw.Draw(img, "RGBA")
    wordmark(d, 0, 640, 78, center_at=960)
    st = "T R A N S M I S S Ã O   E N C E R R A D A"
    f = c6(30)
    tracked(d, ((1920 - tw(d, st, f, 2)) / 2, 750), st, f, TXT2, 2)
    chip_row(d, 830, [[("LIVE ", True), ("SEG–SÁB · 08H–22H", False)],
                      [("TIBIA · RUBINOT", False)]], c6(26), cx=960)
    shard_cluster(d, 180, 200, 4, 130)
    shard_cluster(d, 1720, 830, 4, 130, flip=True)
    energy_bar(d, 0, 1920, 0, 8)
    energy_bar(d, 0, 1920, 1074, 4)
    # moldura verde extremamente fina
    d.rectangle([2, 2, 1917, 1077], outline=ACID, width=2)
    img = vignette(img, 150)
    img.save(OUT + "extras/offline-1920x1080.png")
    print("offline ok")

# ═══════════════ 3) FALLBACKS ESTÁTICOS DAS TELAS ═══════════════
def tela_fallback(nome, status, sub, countdown=None, chips=True):
    img, d = base(1920, 1080)
    emb = ICON.resize((400, 400), Image.LANCZOS)
    img.paste(emb, (760, 130))
    d = ImageDraw.Draw(img, "RGBA")
    wordmark(d, 0, 565, 74, center_at=960)
    f = c6(28)
    tracked(d, ((1920 - tw(d, status, f, 6)) / 2, 668), status, f, TXT2, 6)
    if countdown:
        fc = o9(120)
        d.text((960 - tw(d, countdown, fc) / 2, 715), countdown, font=fc, fill=ACID)
    else:
        f2 = c5(30)
        d.text((960 - tw(d, sub, f2) / 2, 730), sub, font=f2, fill=TXT2)
    if chips:
        chip_row(d, 890, [[("SEG–SÁB", True), (" · 08H–22H", False)],
                          [("TIBIA · RUBINOT", False)]], c6(24), cx=960)
    shard_cluster(d, 170, 190, 4, 120)
    shard_cluster(d, 1730, 820, 4, 120, flip=True)
    energy_bar(d, 0, 1920, 0, 8)
    energy_bar(d, 0, 1920, 1074, 4)
    # moldura verde extremamente fina
    d.rectangle([2, 2, 1917, 1077], outline=ACID, width=2)
    img = vignette(img, 150)
    img.save(OUT + f"telas/{nome}-fallback.png")
    print(nome, "fallback ok")

# ═══════════════ 4) PAINÉIS DO PERFIL 320×160 ═══════════════
def glyph(d, kind, cx, cy):
    col, w = ACID, 4
    d.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], outline=TOXIC, width=2)
    if kind == "sobre":
        d.line([(cx, cy - 12), (cx, cy + 4)], fill=col, width=w)
        d.ellipse([cx - 2, cy + 12, cx + 2, cy + 16], fill=col)
    elif kind == "horarios":
        d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], outline=col, width=w)
        d.line([(cx, cy), (cx, cy - 10)], fill=col, width=w)
        d.line([(cx, cy), (cx + 8, cy + 4)], fill=col, width=w)
    elif kind == "discord":
        d.polygon([(cx - 20, cy - 14), (cx + 20, cy - 14), (cx + 20, cy + 8),
                   (cx + 6, cy + 8), (cx - 2, cy + 18), (cx - 4, cy + 8), (cx - 20, cy + 8)], outline=col, width=w)
        for ox in (-9, 9):
            d.ellipse([cx + ox - 2, cy - 5, cx + ox + 2, cy - 1], fill=col)
    elif kind == "redes":
        d.ellipse([cx - 17, cy - 17, cx + 17, cy + 17], outline=col, width=w)
        d.ellipse([cx - 7, cy - 17, cx + 7, cy + 17], outline=col, width=3)
        d.line([(cx - 17, cy), (cx + 17, cy)], fill=col, width=3)
        d.line([(cx, cy - 17), (cx, cy + 17)], fill=col, width=3)
    elif kind == "regras":
        d.polygon([(cx, cy - 20), (cx + 18, cy - 12), (cx + 18, cy + 6), (cx, cy + 20),
                   (cx - 18, cy + 6), (cx - 18, cy - 12)], outline=col, width=w)
        d.line([(cx - 8, cy), (cx - 2, cy + 8)], fill=col, width=w)
        d.line([(cx - 2, cy + 8), (cx + 10, cy - 8)], fill=col, width=w)
    elif kind == "apoie":
        d.ellipse([cx - 12, cy - 12, cx - 1, cy - 1], outline=col, width=w)
        d.ellipse([cx + 1, cy - 12, cx + 12, cy - 1], outline=col, width=w)
        d.polygon([(cx - 11, cy - 3), (cx, cy + 18), (cx + 11, cy - 3)], outline=col, width=w)
    elif kind == "comandos":
        d.line([(cx - 14, cy - 10), (cx - 4, cy), (cx - 14, cy + 10)], fill=col, width=w)
        d.line([(cx + 2, cy + 10), (cx + 14, cy + 10)], fill=col, width=w)
    elif kind == "setup":
        for a in range(0, 360, 45):
            r1, r2 = 14, 22
            x1, y1 = cx + math.cos(math.radians(a)) * r1, cy + math.sin(math.radians(a)) * r1
            x2, y2 = cx + math.cos(math.radians(a)) * r2, cy + math.sin(math.radians(a)) * r2
            d.line([(x1, y1), (x2, y2)], fill=col, width=w)
        d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], outline=col, width=w)

def painel(titulo, sub, kind):
    img = Image.new("RGB", (320, 160), (10, 13, 10))
    d = ImageDraw.Draw(img, "RGBA")
    d.polygon([(14, 0), (320, 0), (320, 146), (306, 160), (0, 160), (0, 14)],
              fill=SURF, outline=TOXIC + (180,), width=2)
    for xx in range(0, 320, 40):
        d.line([(xx, 0), (xx, 160)], fill=(14, 20, 12, 90))
    glyph(d, kind, 48, 80)
    # auto-ajuste: título e subtítulo nunca ultrapassam a área segura
    ts = 24
    ft = c6(ts)
    while tw(d, titulo, ft) > 206 and ts > 14:
        ts -= 1
        ft = c6(ts)
    d.text((88, 52), titulo, font=ft, fill=ACID)
    ss = 17
    fs_ = c5(ss)
    while tw(d, sub, fs_) > 210 and ss > 11:
        ss -= 1
        fs_ = c5(ss)
    d.text((88, 86), sub, font=fs_, fill=TXT2)
    d.line([(88, 118), (292, 118)], fill=TOXIC + (160,), width=2)
    d.polygon([(88, 116), (112, 116), (104, 120), (88, 120)], fill=ACID)
    img.save(OUT + f"paineis/painel-{kind}.png")
    print("painel", kind, "ok")

# ═══════════════ 5) OVERLAY PNG (fallback estático) ═══════════════
def overlay_png():
    img = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    d = ImageDraw.Draw(img, "RGBA")
    # linha superior de energia
    for xx in range(1920):
        t = abs(xx - 960) / 960
        a = int(200 * (1 - t))
        col = tuple(int(ACID[i] * (1 - t * .5)) for i in range(3)) + (a,)
        d.line([(xx, 0), (xx, 4)], fill=col)
    # emblema central pequeno + wordmark
    emb = ICON.resize((74, 74), Image.LANCZOS)
    img.paste(emb, (923, 18))
    f = c6(24)
    w = tw(d, "E X O R I S E R V I C E", f)
    tracked(d, ((1920 - w) / 2, 100), "E X O R I S E R V I C E", f, TXT + (230,), 0)
    d.polygon([((1920 - w) / 2 - 20, 138), ((1920 + w) / 2 + 20, 138),
               ((1920 + w) / 2 + 8, 143), ((1920 - w) / 2 - 8, 143)], fill=ACID + (200,))
    # shards nos cantos superiores
    shard_cluster(ImageDraw.Draw(img, "RGBA"), 60, 60, 3, 90)
    shard_cluster(ImageDraw.Draw(img, "RGBA"), 1830, 60, 3, 90, flip=True)
    img.save(OUT + "overlay/overlay-gameplay-fallback.png")
    print("overlay png ok")

banner(); offline()
tela_fallback("starting", "I N I C I A N D O   E M", "", countdown="10:00")
tela_fallback("brb", "P A U S A   R Á P I D A", "já volto", chips=False)
tela_fallback("encerramento", "O B R I G A D O   P E L A   L I V E", "até segunda, 08h")
for t, s, k in [("SOBRE MIM", "conheça o streamer", "sobre"),
                ("HORÁRIOS", "seg–sáb · 08h–22h", "horarios"),
                ("DISCORD", "entre na guilda", "discord"),
                ("REDES SOCIAIS", "@exoriservice", "redes"),
                ("REGRAS DO CHAT", "respeito acima de tudo", "regras"),
                ("APOIE O CANAL", "sub · bits · doação", "apoie"),
                ("COMANDOS", "!service · !coins · !intermedio · !wpp", "comandos"),
                ("SETUP", "o arsenal do dragão", "setup")]:
    painel(t, s, k)
overlay_png()
print("≈≈≈ Lote 4A estático completo ≈≈≈")
