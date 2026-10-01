#!/usr/bin/env python3
"""BG de Just Chatting — compõe a arte IA com a identidade da marca."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

F = "/home/user/twitch-pro/assets/fonts/"
L = "/home/user/twitch-pro/logos/final/"
OUT = "/home/user/twitch-pro/assets/extras/"

ACID, TOXIC = (180, 255, 0), (92, 153, 0)
TXT, TXT2 = (242, 255, 232), (154, 166, 154)
o9 = lambda s: ImageFont.truetype(F + "Orbitron-900.ttf", s)
c6 = lambda s: ImageFont.truetype(F + "ChakraPetch-600.ttf", s)

W, H = 1920, 1080
art = Image.open(OUT + "jc-arte-bruta.png").convert("RGB")
# cortar/ajustar para 16:9
aw, ah = art.size
target = W / H
if aw / ah > target:
    nw = int(ah * target)
    art = art.crop(((aw - nw) // 2, 0, (aw + nw) // 2, ah))
else:
    nh = int(aw / target)
    art = art.crop((0, (ah - nh) // 2, aw, (ah + nh) // 2))
art = art.resize((W, H), Image.LANCZOS)
art = ImageEnhance.Brightness(art).enhance(0.82)   # mais escuro = área de leitura
art = ImageEnhance.Contrast(art).enhance(1.08)

img = art.copy()
d = ImageDraw.Draw(img, "RGBA")

# ── emblema fantasma central (marca d'água grande) ──
emb = Image.open(L + "icone-512.png").convert("RGB").resize((640, 640), Image.LANCZOS)
emb_g = emb.convert("L").point(lambda p: int(p * 0.55))
tint = Image.new("RGBA", (640, 640), (12, 34, 3, 0))
tint.putalpha(emb_g)
img.paste(tint, (W // 2 - 320, H // 2 - 320), tint)
d = ImageDraw.Draw(img, "RGBA")

# ── gradiente inferior (leitura do ticker/elementos) ──
for y in range(H - 220, H):
    a = int((y - (H - 220)) / 220 * 190)
    d.line([(0, y), (W, y)], fill=(6, 8, 6, a))
# ── gradiente superior leve ──
for y in range(0, 120):
    a = int((1 - y / 120) * 110)
    d.line([(0, y), (W, y)], fill=(6, 8, 6, a))

# ── lockup topo-centro ──
def tw(txt, font, tr=0):
    dd = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    return sum(dd.textlength(c, font=font) for c in txt) + tr * (len(txt) - 1)

def tracked(dd, xy, text, font, fill, tr=0):
    x, y = xy
    for ch in text:
        dd.text((x, y), ch, font=font, fill=fill)
        x += dd.textlength(ch, font=font) + tr

logo = Image.open(L + "icone-512.png").convert("RGB").resize((72, 72), Image.LANCZOS)
f = o9(44)
wEX = tw("EXORI", f, 4)
wSV = tw("SERVICE", f, 4)
total_lock = 72 + 16 + wEX + 18 + wSV
x0 = int(W / 2 - total_lock / 2)
img.paste(logo, (x0, 44))
d = ImageDraw.Draw(img, "RGBA")
tx = x0 + 72 + 16
tracked(d, (tx, 54), "EXORI", f, ACID, 4)
tracked(d, (tx + wEX + 18, 54), "SERVICE", f, TXT, 4)
sub = "J U S T   C H A T T I N G   ·   T I B I A   ( R U B I N O T )"
fs = c6(22)
tracked(d, ((W - tw(sub, fs, 2)) / 2, 128), sub, fs, TXT2, 2)
d.polygon([((W - tw(sub, fs, 2)) / 2 - 26, 168), ((W + tw(sub, fs, 2)) / 2 + 26, 168),
           ((W + tw(sub, fs, 2)) / 2 + 14, 174), ((W - tw(sub, fs, 2)) / 2 - 14, 174)], fill=ACID + (220,))

# ── energy bars ──
for xx in range(0, W, 2):
    t = abs(xx - W / 2) / (W / 2)
    col = tuple(int(ACID[i] * (1 - t) + TOXIC[i] * t) for i in range(3))
    d.line([(xx, 0), (xx, 6)], fill=col)
    d.line([(xx, H - 4), (xx, H)], fill=col)

# ── moldura verde extremamente fina ──
d.rectangle([2, 2, W - 3, H - 3], outline=ACID, width=2)

img.save(OUT + "justchatting-1920x1080.png")
print("justchatting-1920x1080.png ok")
