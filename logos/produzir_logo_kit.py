#!/usr/bin/env python3
"""Kit final de assets do logo oficial EXORISERVICE — Hex Strike (C1)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

BG    = (6, 8, 6)
ACID  = (180, 255, 0)
TOXIC = (92, 153, 0)
TXT   = (242, 255, 232)

F = "/home/user/twitch-pro/assets/fonts/"
orbitron9 = lambda s: ImageFont.truetype(F + "Orbitron-900.ttf", s)

SRC = "/home/user/twitch-pro/logos/variacao-c1.png"
OUT = "/home/user/twitch-pro/logos/final"
os.makedirs(OUT, exist_ok=True)

def center_crop_square(img):
    w, h = img.size
    s = min(w, h)
    return img.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))

def tracked(draw, xy, text, font, fill, tracking=0):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking
    return x

def tracked_width(draw, text, font, tracking=0):
    return sum(draw.textlength(c, font=font) for c in text) + tracking * (len(text) - 1)

src = Image.open(SRC).convert("RGB")
sq = center_crop_square(src)

# ---------- 1) Avatar oficial 800×800 ----------
avatar = sq.resize((800, 800), Image.LANCZOS)
avatar.save(f"{OUT}/avatar-800.png")

for s in (512, 256, 128, 64, 24):
    sq.resize((s, s), Image.LANCZOS).save(f"{OUT}/icone-{s}.png")

# ---------- 2) Lockups (ícone + wordmark) ----------
ICON = 300
icon = sq.resize((ICON, ICON), Image.LANCZOS)

def make_lockup(horizontal=True):
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    size, tr = 96 if horizontal else 84, 7
    f = orbitron9(size)
    w1 = tracked_width(tmp, "EXORI", f, tr)
    w2 = tracked_width(tmp, "SERVICE", f, tr)
    gapw = size * 0.35
    text_w, text_h = w1 + gapw + w2, size
    pad = 40
    if horizontal:
        W = int(pad + ICON + 70 + text_w + pad)
        H = int(ICON + pad * 2)
        img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        img.paste(icon, (pad, pad))
        x = pad + ICON + 70
        y = (H - text_h) / 2 - 6
        d = ImageDraw.Draw(img)
        glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        tracked(gd, (x, y), "EXORI", f, TOXIC + (170,), tr)
        img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(12)))
        d = ImageDraw.Draw(img)
        tracked(d, (x, y), "EXORI", f, ACID + (255,), tr)
        tracked(d, (x + w1 + gapw, y), "SERVICE", f, TXT + (255,), tr)
    else:
        W = int(max(ICON, text_w) + pad * 2)
        H = int(pad + ICON + 56 + text_h + pad)
        img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        img.paste(icon, (int((W - ICON) / 2), pad))
        y = pad + ICON + 56
        x = (W - text_w) / 2
        d = ImageDraw.Draw(img)
        tracked(d, (x, y), "EXORI", f, ACID + (255,), tr)
        tracked(d, (x + w1 + gapw, y), "SERVICE", f, TXT + (255,), tr)
    return img

make_lockup(True).save(f"{OUT}/lockup-horizontal.png")
make_lockup(False).save(f"{OUT}/lockup-vertical.png")

# ---------- 3) Versões monocromáticas (alpha por luminância) ----------
g = sq.convert("L")
big = g.resize((1024, 1024), Image.LANCZOS)

def mono(color, name, gain=1.15):
    alpha = big.point(lambda p: min(255, int((255 - p) * gain)))
    img = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
    fill = Image.new("RGBA", (1024, 1024), color + (255,))
    img.putalpha(alpha)
    out = Image.alpha_composite(Image.new("RGBA", (1024, 1024), (0, 0, 0, 0)), img)
    solid = Image.new("RGBA", (1024, 1024), color + (255,))
    solid.putalpha(alpha)
    solid.save(f"{OUT}/{name}")

mono((255, 255, 255), "logo-mono-branco.png")
mono((0, 0, 0), "logo-mono-preto.png", gain=1.3)

print("Kit gerado em", OUT)
for f in sorted(os.listdir(OUT)):
    print(" •", f)
