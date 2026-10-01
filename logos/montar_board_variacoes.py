#!/usr/bin/env python3
"""Board de apresentação — VARIAÇÕES do Conceito C (Hex Sigil)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BG      = (6, 8, 6)
SURF    = (18, 23, 18)
SURF2   = (28, 36, 28)
ACID    = (180, 255, 0)
TOXIC   = (92, 153, 0)
FOREST  = (23, 51, 0)
TXT     = (242, 255, 232)
TXT2    = (154, 166, 154)

F = "/home/user/twitch-pro/assets/fonts/"
orbitron9 = lambda s: ImageFont.truetype(F + "Orbitron-900.ttf", s)
chakra6   = lambda s: ImageFont.truetype(F + "ChakraPetch-600.ttf", s)
chakra5   = lambda s: ImageFont.truetype(F + "ChakraPetch-500.ttf", s)

def tracked(draw, xy, text, font, fill, tracking=0):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking
    return x

def tracked_width(draw, text, font, tracking=0):
    return sum(draw.textlength(c, font=font) for c in text) + tracking * (len(text) - 1)

def wordmark(draw, cx, y, size=64, tracking=6):
    f = orbitron9(size)
    t1, t2 = "EXORI", "SERVICE"
    w1 = tracked_width(draw, t1, f, tracking)
    w2 = tracked_width(draw, t2, f, tracking)
    total = w1 + w2 + size * 0.35
    x = cx - total / 2
    gx = x
    for ch in t1:
        draw.text((gx, y), ch, font=f, fill=TOXIC)
        gx += draw.textlength(ch, font=f) + tracking
    tracked(draw, (x, y), t1, f, ACID, tracking)
    tracked(draw, (x + w1 + size * 0.35, y), t2, f, TXT, tracking)

def center_crop_square(img):
    w, h = img.size
    s = min(w, h)
    return img.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))

CELL, GAP, MARG = 560, 48, 56
W = MARG * 2 + CELL * 2 + GAP
HEADER, FOOTER = 210, 150
CELL_H = CELL + 96
H = HEADER + CELL_H * 2 + GAP + FOOTER

board = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(board)
grid = Image.new("RGB", (W, H), BG)
gd = ImageDraw.Draw(grid)
for x in range(0, W, 44):
    gd.line([(x, 0), (x, H)], fill=(10, 14, 10), width=1)
for y in range(0, H, 44):
    gd.line([(0, y), (W, y)], fill=(10, 14, 10), width=1)
board = Image.blend(board, grid, 0.5)
d = ImageDraw.Draw(board)

d.polygon([(0, 0), (W, 0), (W, 10), (0, 10)], fill=ACID)
sub = "V A R I A Ç Õ E S   —   C O N C E I T O   C   ·   H E X   S I G I L"
f_sub = chakra6(22)
sw = tracked_width(d, sub, f_sub, 2)
tracked(d, ((W - sw) / 2, 66), sub, f_sub, TXT2, 2)
wordmark(d, W / 2, 96, size=76, tracking=8)
d.line([(MARG, 196), (W - MARG, 196)], fill=TOXIC, width=2)
d.polygon([(W / 2 - 60, 196), (W / 2 + 60, 196), (W / 2 + 48, 202), (W / 2 - 48, 202)], fill=ACID)

concepts = [
    ("variacao-c1.png", "VARIAÇÃO C1 — HEX STRIKE",
     "Mais agressivo: facetas afiadas e brilho verde intenso.",
     "Máxima presença em avatar e telas."),
    ("variacao-c2.png", "VARIAÇÃO C2 — HEX PURE",
     "Ultra-minimalista: pictograma icônico, espesso e limpo.",
     "Escala perfeito até em tamanhos pequenos (24px)."),
    ("variacao-c3.png", "VARIAÇÃO C3 — HEX CLAN",
     "Emblema frontal simétrico com anel hexagonal duplo.",
     "Ar de clã/guilda — combina com Tibia (RubinOT)."),
    ("variacao-c4.png", "VARIAÇÃO C4 — HEX LINE",
     "Monoline: linha fina contínua, muito respiro.",
     "O mais sofisticado e futurista do lote."),
]

positions = [(MARG, HEADER + 24), (MARG + CELL + GAP, HEADER + 24),
             (MARG, HEADER + 24 + CELL_H + GAP - 24), (MARG + CELL + GAP, HEADER + 24 + CELL_H + GAP - 24)]

for (fname, label, desc, d2), (px, py) in zip(concepts, positions):
    box = (px - 14, py - 14, px + CELL + 14, py + CELL_H - 6)
    d.polygon([(box[0] + 20, box[1]), (box[2], box[1]), (box[2], box[3] - 20),
               (box[2] - 20, box[3]), (box[0], box[3]), (box[0], box[1] + 20)],
              fill=SURF, outline=(28, 60, 0), width=2)
    img = Image.open(f"/home/user/twitch-pro/logos/{fname}").convert("RGB")
    img = center_crop_square(img).resize((CELL - 24, CELL - 24), Image.LANCZOS)
    board.paste(img, (px + 12, py + 12))
    d.polygon([(px + 12, py + 12), (px + CELL - 12, py + 12), (px + CELL - 12, py + 18), (px + 12, py + 18)], fill=ACID)
    tracked(d, (px + 6, py + CELL + 22), label, chakra6(24), ACID, 1)
    d.text((px + 6, py + CELL + 58), desc, font=chakra5(19), fill=TXT2)
    d.text((px + 6, py + CELL + 84), d2, font=chakra5(19), fill=TXT2)

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
d.text((MARG, fy + 52), "ESCOLHA A VARIANTE DEFINITIVA (ou misture elementos)   |   original: conceito-c.png",
       font=f_ft, fill=TXT2)

board.save("/home/user/twitch-pro/logos/board-variacoes-c.png", quality=95)
print("Board variações salvo:", board.size)
