#!/usr/bin/env python3
"""Board de apresentação — conceitos de logo EXORISERVICE + wordmark oficial."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ---------- Paleta ----------
BG      = (6, 8, 6)        # #060806 preto carbono
SURF    = (18, 23, 18)     # #121712 grafite esverdeado
SURF2   = (28, 36, 28)     # #1C241C
ACID    = (180, 255, 0)    # #B4FF00 verde ácido
TOXIC   = (92, 153, 0)     # #5C9900
FOREST  = (23, 51, 0)      # #173300
TXT     = (242, 255, 232)  # #F2FFE8
TXT2    = (154, 166, 154)  # #9AA69A

F = "/home/user/twitch-pro/assets/fonts/"
orbitron9 = lambda s: ImageFont.truetype(F + "Orbitron-900.ttf", s)
orbitron7 = lambda s: ImageFont.truetype(F + "Orbitron-700.ttf", s)
chakra6   = lambda s: ImageFont.truetype(F + "ChakraPetch-600.ttf", s)
chakra5   = lambda s: ImageFont.truetype(F + "ChakraPetch-500.ttf", s)

def tracked(draw, xy, text, font, fill, tracking=0, anchor=None):
    """Desenha texto com espaçamento entre letras."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill, anchor=anchor)
        w = draw.textlength(ch, font=font)
        x += w + tracking
    return x

def tracked_width(draw, text, font, tracking=0):
    return sum(draw.textlength(c, font=font) for c in text) + tracking * (len(text) - 1)

def wordmark(draw, cx, y, size=64, tracking=6, glow=False):
    """EXORI (ácido) + SERVICE (branco), centrado em cx."""
    f = orbitron9(size)
    t1, t2 = "EXORI", "SERVICE"
    w1 = tracked_width(draw, t1, f, tracking)
    w2 = tracked_width(draw, t2, f, tracking)
    total = w1 + w2 + size * 0.35
    x = cx - total / 2
    if glow:
        # camada de brilho atrás
        gx = x
        for ch in t1:
            draw.text((gx, y), ch, font=f, fill=TOXIC)
            gx += draw.textlength(ch, font=f) + tracking
    tracked(draw, (x, y), t1, f, ACID, tracking)
    tracked(draw, (x + w1 + size * 0.35, y), t2, f, TXT, tracking)

def cut_corner(rect_draw, box, corner=18, invert=False):
    """Retângulo com canto chanfrado (notch cut)."""
    x0, y0, x1, y1 = box
    if invert:
        pts = [(x0, y0), (x1 - corner, y0), (x1, y0 + corner), (x1, y1),
               (x0 + corner, y1), (x0, y1 - corner)]
    else:
        pts = [(x0 + corner, y0), (x1, y0), (x1, y1 - corner),
               (x1 - corner, y1), (x0, y1), (x0, y0 + corner)]
    rect_draw.polygon(pts, fill=SURF, outline=TOXIC, width=2)

def center_crop_square(img):
    w, h = img.size
    s = min(w, h)
    return img.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))

# ================= BOARD =================
CELL, GAP, MARG = 560, 48, 56
W = MARG * 2 + CELL * 2 + GAP
HEADER, FOOTER = 210, 150
CELL_H = CELL + 96
H = HEADER + CELL_H * 2 + GAP + FOOTER

board = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(board)

# grade tech sutil de fundo
grid = Image.new("RGB", (W, H), BG)
gd = ImageDraw.Draw(grid)
for x in range(0, W, 44):
    gd.line([(x, 0), (x, H)], fill=(10, 14, 10), width=1)
for y in range(0, H, 44):
    gd.line([(0, y), (W, y)], fill=(10, 14, 10), width=1)
board = Image.blend(board, grid, 0.5)
d = ImageDraw.Draw(board)

# ---------- Header ----------
d.polygon([(0, 0), (W, 0), (W, 10), (0, 10)], fill=ACID)
sub = "C O N C E I T O S   D E   L O G O   —   D R A G Ã O   G E O M É T R I C O"
f_sub = chakra6(22)
sw = tracked_width(d, sub, f_sub, 2)
tracked(d, ((W - sw) / 2, 66), sub, f_sub, TXT2, 2)
wordmark(d, W / 2, 96, size=76, tracking=8, glow=True)
d.line([(MARG, 196), (W - MARG, 196)], fill=TOXIC, width=2)
d.polygon([(W / 2 - 60, 196), (W / 2 + 60, 196), (W / 2 + 48, 202), (W / 2 - 48, 202)], fill=ACID)

# ---------- Células ----------
concepts = [
    ("conceito-a.png", "CONCEITO A — SHARD DRAGON",
     "Perfil agressivo em estilhaços poligonais. Atitude e-sports pura,"),
    ("conceito-b.png", "CONCEITO B — X-WYRM",
     "Frontal simétrico com asas em X — incorpora a inicial do nome no símbolo."),
    ("conceito-c.png", "CONCEITO C — HEX SIGIL",
     "Badge hexagonal minimalista. Versátil: escala pequeno sem perder a forma."),
    ("conceito-d.png", "CONCEITO D — NEON CONTOUR",
     "Silhueta em traço fino e negativo. O mais clean e futurista dos quatro."),
]
desc2 = [
    "máximo impacto em avatar e telas.",
    "Perfeito como emblema de time/marca.",
    "Ideal para ícone, badge e favicon.",
    "Elegante sobre fundos escuros.",
]

positions = [(MARG, HEADER + 24), (MARG + CELL + GAP, HEADER + 24),
             (MARG, HEADER + 24 + CELL_H + GAP - 24), (MARG + CELL + GAP, HEADER + 24 + CELL_H + GAP - 24)]

for (fname, label, desc), (px, py) in zip([(c[0], c[1], c[2]) for c in concepts], positions):
    # caixa da célula
    box = (px - 14, py - 14, px + CELL + 14, py + CELL_H - 6)
    d.polygon([(box[0] + 20, box[1]), (box[2], box[1]), (box[2], box[3] - 20),
               (box[2] - 20, box[3]), (box[0], box[3]), (box[0], box[1] + 20)],
              fill=SURF, outline=(28, 60, 0), width=2)
    # imagem
    img = Image.open(f"/home/user/twitch-pro/logos/{fname}").convert("RGB")
    img = center_crop_square(img).resize((CELL - 24, CELL - 24), Image.LANCZOS)
    board.paste(img, (px + 12, py + 12))
    # barra ácida no topo da imagem
    d.polygon([(px + 12, py + 12), (px + CELL - 12, py + 12), (px + CELL - 12, py + 18), (px + 12, py + 18)], fill=ACID)
    # rótulo
    f_lbl = chakra6(24)
    tracked(d, (px + 6, py + CELL + 22), label, f_lbl, ACID, 1)
    # descrição
    idx = [c[0] for c in concepts].index(fname)
    f_d = chakra5(19)
    d.text((px + 6, py + CELL + 58), desc, font=f_d, fill=TXT2)
    d.text((px + 6, py + CELL + 84), desc2[idx], font=f_d, fill=TXT2)

# ---------- Footer ----------
fy = H - FOOTER + 26
d.line([(MARG, fy - 14), (W - MARG, fy - 14)], fill=TOXIC, width=2)
f_ft = chakra5(20)
d.text((MARG, fy + 8), "PALETA:", font=chakra6(20), fill=TXT)
chips = [(ACID, "#B4FF00"), (TOXIC, "#5C9900"), (FOREST, "#173300"), (SURF2, "#1C241C"), (TXT, "#F2FFE8")]
cx = MARG + 110
for color, hexc in chips:
    d.polygon([(cx, fy + 10), (cx + 34, fy + 10), (cx + 34, fy + 34), (cx, fy + 34)], fill=color, outline=TOXIC)
    d.text((cx + 42, fy + 10), hexc, font=f_ft, fill=TXT2)
    cx += 42 + d.textlength(hexc, font=f_ft) + 26
d.text((MARG, fy + 52), "TIPOGRAFIA: Orbitron (display)  •  Chakra Petch (labels)  •  Exo 2 (corpo)   |   ESCOLHA UM CONCEITO PARA REFINARMOS",
       font=f_ft, fill=TXT2)

board.save("/home/user/twitch-pro/logos/board-conceitos.png", quality=95)
print("Board salvo:", board.size)

# ================= WORDMARK standalone (transparente) =================
tmp = Image.new("RGBA", (10, 10))
td = ImageDraw.Draw(tmp)
size, tr = 110, 9
f = orbitron9(size)
w1 = tracked_width(td, "EXORI", f, tr)
w2 = tracked_width(td, "SERVICE", f, tr)
pad = 60
wm = Image.new("RGBA", (int(w1 + w2 + size * 0.35 + pad * 2), size + pad * 2), (0, 0, 0, 0))
wd = ImageDraw.Draw(wm)
x = pad
glow = Image.new("RGBA", wm.size, (0, 0, 0, 0))
gd2 = ImageDraw.Draw(glow)
tracked(gd2, (x, pad), "EXORI", f, TOXIC + (160,), tr)
glow = glow.filter(ImageFilter.GaussianBlur(10))
wm = Image.alpha_composite(wm, glow)
wd = ImageDraw.Draw(wm)
tracked(wd, (x, pad), "EXORI", f, ACID + (255,), tr)
tracked(wd, (x + w1 + size * 0.35, pad), "SERVICE", f, TXT + (255,), tr)
wm.save("/home/user/twitch-pro/logos/wordmark-exoriservice.png")
print("Wordmark salvo:", wm.size)
