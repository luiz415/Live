#!/usr/bin/env python3
"""Lote 4B — STINGER de transição (0,73s): varredura de shards + emblema flash.
Renderiza frames RGBA (PIL) e codifica WebM VP8 com canal alfa (ffmpeg)."""
import math, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1920, 1080, 60
IN, HOLD, OUT = 16, 12, 16          # frames
TOTAL = IN + HOLD + OUT
FRAMES = "/home/user/twitch-pro/assets/stinger/frames/"
OUTDIR = "/home/user/twitch-pro/assets/stinger/"
os.makedirs(FRAMES, exist_ok=True)

ACID, TOXIC, FOREST, TXT = (180, 255, 0), (92, 153, 0), (23, 51, 0), (242, 255, 232)
F = "/home/user/twitch-pro/assets/fonts/"
L = "/home/user/twitch-pro/logos/final/"
o9 = lambda s: ImageFont.truetype(F + "Orbitron-900.ttf", s)

# ── sprites pré-renderizados ──
emblem = Image.open(L + "icone-512.png").convert("RGB").resize((340, 340), Image.LANCZOS)
glow_emblem = emblem.filter(ImageFilter.GaussianBlur(26))

def wordmark_img():
    img = Image.new("RGBA", (1100, 130), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = o9(78)
    x = 20
    for ch in "EXORI":
        d.text((x, 10), ch, font=f, fill=ACID + (255,))
        x += d.textlength(ch, font=f) + 8
    x += 22
    for ch in "SERVICE":
        d.text((x, 10), ch, font=f, fill=TXT + (255,))
        x += d.textlength(ch, font=f) + 8
    return img.crop((0, 0, int(x) + 30, 130))
wm = wordmark_img()
wm_glow = wm.filter(ImageFilter.GaussianBlur(18))

def paste_alpha(base, sprite, center, alpha):
    if alpha <= 0:
        return
    sp = sprite.copy()
    if sp.mode != "RGBA":
        sp = sp.convert("RGBA")
    if alpha < 1:
        a = sp.split()[3].point(lambda p: int(p * alpha))
        sp.putalpha(a)
    base.paste(sp, (int(center[0] - sp.width / 2), int(center[1] - sp.height / 2)), sp)

JAG = [70, -55, 95, -75, 55, -95, 40, -60]

def render(i):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img, "RGBA")

    if i < IN:                       # entra cobrindo (borda direita avança)
        bx = -2100 + (i + 1) / IN * (2100 + W + 60)
        cover_frac = max(0.0, min(1.0, (bx - 500) / (W - 300)))
    elif i < IN + HOLD:              # cobre tudo
        bx = W + 60
        cover_frac = 1.0
    else:                            # sai (borda esquerda avança)
        k = (i - IN - HOLD + 1) / OUT
        bx = -2100 + k * (2100 + W + 60)   # borda ESQUERDA da cobertura
        cover_frac = 1.0 - max(0.0, min(1.0, (bx + 700) / (W + 200)))

    entering = i < IN + HOLD
    # polígono da cobertura
    shift = (i * 9) % 90
    pts = []
    for y in range(-90, H + 180, 90):
        off = JAG[((y + shift) // 90) % len(JAG)]
        pts.append((bx + off, y))
    if entering:
        poly = [(-2400, -10)] + pts + [(-2400, H + 10)]
    else:
        poly = pts + [(W + 2400, H + 10), (W + 2400, -10)]
    d.polygon(poly, fill=(6, 8, 6, 252))

    # linha de borda brilhante (dupla)
    edge = [(x, y) for x, y in pts]
    d.line(edge, fill=TOXIC + (200,), width=16, joint="curve")
    d.line(edge, fill=ACID + (255,), width=6, joint="curve")

    # shards sobre a cobertura (fixos relativos à tela, aparecem onde há cobertura)
    for sx, sy, s, col in [(180, 160, 90, ACID), (1740, 220, 70, TOXIC), (120, 900, 80, TOXIC),
                           (1800, 880, 100, ACID), (960, 95, 60, ACID)]:
        d.polygon([(sx, sy - s), (sx + s * .58, sy + s * .35), (sx - s * .3, sy + s * .3)], fill=col + (60,))

    # emblema + wordmark com alpha proporcional à cobertura + pulso no hold
    pulse = 1.0
    if IN <= i < IN + HOLD:
        pulse = 1 + 0.035 * math.sin((i - IN) / HOLD * math.pi)
    if cover_frac > 0:
        e = emblem.resize((int(340 * pulse), int(340 * pulse)), Image.LANCZOS)
        paste_alpha(img, glow_emblem, (W / 2, H / 2 - 60), 0.55 * cover_frac)
        paste_alpha(img, e, (W / 2, H / 2 - 60), cover_frac)
        paste_alpha(img, wm_glow, (W / 2, H / 2 + 210), 0.5 * cover_frac)
        paste_alpha(img, wm, (W / 2, H / 2 + 210), cover_frac)
        d = ImageDraw.Draw(img, "RGBA")
        # barras de energia durante a cobertura
        if cover_frac > 0.6:
            for xx in range(0, W, 12):
                a = int(190 * cover_frac * (0.5 + 0.5 * math.sin(xx / 90 + i / 3)))
                d.line([(xx, 6), (xx + 12, 6)], fill=ACID + (a,))
                d.line([(xx, H - 6), (xx + 12, H - 6)], fill=ACID + (a,))

    return img

for i in range(TOTAL):
    render(i).save(FRAMES + f"f{i:03d}.png")
print(f"{TOTAL} frames renderizados")

# ── codificação WebM VP8 com alfa ──
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
cmd = [FF, "-y", "-framerate", str(FPS), "-i", FRAMES + "f%03d.png",
       "-c:v", "libvpx", "-pix_fmt", "yuva420p", "-auto-alt-ref", "0",
       "-crf", "22", "-b:v", "3M", "-quality", "realtime",
       OUTDIR + "stinger-transicao.webm"]
r = subprocess.run(cmd, capture_output=True, text=True)
print("webm:", "ok" if r.returncode == 0 else r.stderr[-500:])

# ── preview GIF (para visualizar aqui) ──
frames = [render(i).convert("RGB").resize((640, 360), Image.LANCZOS) for i in range(0, TOTAL, 2)]
frames[0].save(OUTDIR + "stinger-preview.gif", save_all=True, append_images=frames[1:],
               duration=33, loop=0, optimize=True)
print("preview gif ok")

# limpar frames (manter workspace enxuto)
for f in os.listdir(FRAMES):
    os.remove(FRAMES + f)
print("tamanho webm:", os.path.getsize(OUTDIR + "stinger-transicao.webm") // 1024, "KB")
