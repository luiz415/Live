#!/usr/bin/env python3
"""Lote 4B — SFX dos alertas + whoosh do stinger (síntese pura, WAV 44.1kHz mono)."""
import math, struct, wave, os

SR = 44100
OUT = "/home/user/twitch-pro/assets/alertas/sfx/"
os.makedirs(OUT, exist_ok=True)

def env(i, n, a=0.004, r=0.25):
    """Envelope: ataque rápido + decaimento exponencial."""
    t = i / SR
    dur = n / SR
    at = min(1, t / a) if a > 0 else 1
    rel = math.exp(-(t / (dur * r)))
    return at * rel

def tone(f, dur, shape="sine", vol=0.5, glide=1.0, a=0.004, r=0.25):
    n = int(dur * SR)
    out = []
    for i in range(n):
        t = i / SR
        fr = f * (glide ** (t / dur))
        ph = 2 * math.pi * fr * t
        if shape == "sine":
            s = math.sin(ph)
        elif shape == "square":
            s = 1.0 if math.sin(ph) >= 0 else -1.0
        elif shape == "saw":
            s = 2 * ((fr * t) % 1) - 1
        elif shape == "tri":
            s = 2 * abs(2 * ((fr * t) % 1) - 1) - 1
        out.append(s * env(i, n, a, r) * vol)
    return out

def silence(dur):
    return [0.0] * int(dur * SR)

def mix(*trks):
    n = max(len(t) for t in trks)
    return [sum(t[i] for t in trks if i < len(t)) for i in range(n)]

def seq(*parts):
    out = []
    for p in parts:
        out += p
    return out

def softclip(x):
    return math.tanh(x)

def save(name, samples, vol=0.85):
    peak = max(1e-9, max(abs(s) for s in samples))
    samples = [s / peak * vol for s in samples]
    with wave.open(OUT + name, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(b"".join(struct.pack("<h", int(s * 32767)) for s in samples))
    print(" •", name, f"({len(samples)/SR:.2f}s)")

# follow — dois blips ascendentes
save("sfx-follow.wav", seq(
    tone(880, .11, "sine", .6, r=.4), silence(.05),
    tone(1318, .14, "sine", .65, r=.45)))

# sub — impacto grave + subida
save("sfx-sub.wav", mix(
    seq(tone(140, .5, "sine", .8, glide=1.4, r=.5), silence(.3)),
    seq(silence(.1), tone(220, .4, "tri", .4, glide=2.6, r=.4))))

# resub — acorde curto de poder
save("sfx-resub.wav", mix(
    tone(330, .5, "sine", .35, r=.4),
    tone(494, .5, "sine", .3, r=.4),
    seq(silence(.12), tone(659, .38, "sine", .32, r=.35))))

# gift — arpejo brilhante
save("sfx-gift.wav", seq(
    tone(784, .09, "sine", .5, r=.5), tone(988, .09, "sine", .5, r=.5),
    tone(1319, .12, "sine", .55, r=.5), tone(1568, .16, "sine", .5, r=.5)))

# bits — moeda digital (square)
save("sfx-bits.wav", seq(
    tone(988, .07, "square", .3, r=.5), silence(.02),
    tone(1319, .16, "square", .3, r=.5),
    tone(1760, .2, "sine", .3, r=.5)))

# raid — alarme duplo + sweep
save("sfx-raid.wav", mix(
    seq(tone(440, .16, "square", .28, r=.5), silence(.06), tone(440, .16, "square", .28, r=.5), silence(.06),
        tone(587, .3, "square", .3, r=.4)),
    seq(silence(.75), tone(180, .5, "saw", .22, glide=4.5, r=.4))))

# doação — caixa registradora + acorde
save("sfx-tip.wav", mix(
    seq(tone(1200, .05, "square", .25, r=.4), tone(1600, .05, "square", .25, r=.4), silence(1.0)),
    seq(silence(.13), tone(523, .55, "sine", .32, r=.4), tone(659, .55, "sine", .3, r=.4), tone(784, .6, "sine", .3, r=.4))))

# whoosh do stinger — ruído filtrado descendo
n = int(.7 * SR)
whoosh = []
lp = 0.0
import random
random.seed(7)
for i in range(n):
    t = i / n
    cutoff = .55 * (1 - t) + .04
    noise = random.uniform(-1, 1)
    lp += cutoff * (noise - lp)
    whoosh.append(lp * math.sin(math.pi * t) ** 1.5 * .9)
hit = tone(90, .3, "sine", .9, glide=.7, r=.3)
save("sfx-stinger.wav", mix(whoosh, seq(silence(.42), hit)))
print("SFX completos em", OUT)
