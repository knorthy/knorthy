# Builds an animated dot-matrix SVG from a screenshot: hands drift toward each other, rows shimmer,
# and a word between them cycles with a "decrypt" (scramble -> settle) transition. Pure SVG, so GitHub renders it.
import sys, random, html
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
WORDS = "coding developing syncing building pushing deploy shipped merge testing".split()
SLOT, STEP, OUT_FRAMES = 3.6, 0.1, 3        # seconds per word, scramble step, scramble-out frames
POOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
CX, BASE_Y, CW, FS = 536, 336, 11.5, 18     # word centre x, baseline y, cell width, font size
random.seed(7)

im = Image.open(src).convert("L")
W, H = im.size
# The source is a halftone on a 6.86 x 12.92 px grid (found by autocorrelation); sample exactly at the dot centres.
PX, PY, OX, OY = 6.86, 12.92, 4.0, 12.25 % 12.92
import numpy as np
a = np.asarray(im, float)
rows = {}
j = 0
while OY + j * PY < H - 2:
    y = OY + j * PY; yi = int(round(y)); j += 1
    i = 0
    while OX + i * PX < W - 2:
        x = OX + i * PX; xi = int(round(x)); i += 1
        v = a[max(0, yi - 1):yi + 2, max(0, xi - 1):xi + 2].max()
        if v > 28:
            r = 0.7 + 2.1 * (v / 255) ** 1.2          # faint dots stay tiny, bright dots are full
            rows.setdefault(round(y, 1), []).append((x, f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}"/>'))

# Finger regions: (side, test(x, y), rotation pivot, degrees, seconds). Dots outside any region move with the hand only.
FINGERS = [
    ("L", lambda x, y: y >= 255 and 290 <= x < 345, (290, 255), 1.6, 5.2),
    ("L", lambda x, y: y >= 255 and 345 <= x < 400, (345, 255), 1.8, 5.8),
    ("L", lambda x, y: y >= 255 and 400 <= x < 475, (400, 255), 2.2, 6.4),
    ("R", lambda x, y: y < 340 and 612 <= x < 830, (830, 290), 1, 6.0),
    ("R", lambda x, y: y >= 340 and 700 <= x < 780, (780, 345), 1.8, 5.6),
    ("R", lambda x, y: y >= 340 and 780 <= x < 870, (870, 345), 2, 6.6),
]
TILT = {"L": (0, 300, 1.2), "R": (1175, 300, -1.2)}   # hand-wide tilt: pivot x, y, degrees

def rot(cx, cy, deg, dur, begin=0):
    return (f'<animateTransform attributeName="transform" type="rotate" values="0 {cx} {cy};{deg} {cx} {cy};0 {cx} {cy};{-deg} {cx} {cy};0 {cx} {cy}" '
            f'dur="{dur}s" begin="{begin}s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.25;.5;.75;1" '
            f'keySplines="{";".join([".45 0 .55 1"] * 4)}"/>')

def hand(side):
    ys = sorted(rows)
    fingers = [f for f in FINGERS if f[0] == side]
    buckets = {k: {} for k in range(-1, len(fingers))}       # -1 = rest of the hand
    for y in ys:
        for x, c in rows[y]:
            if (x < CX) != (side == "L"):
                continue
            k = next((i for i, f in enumerate(fingers) if f[1](x, y)), -1)
            buckets[k].setdefault(y, []).append(c)
    def rowgroups(b):
        return "".join(f'<g class="r" style="animation-delay:{(ys.index(y) * 0.12) % 3:.2f}s">{"".join(d)}</g>' for y, d in sorted(b.items()))
    out = rowgroups(buckets[-1])
    for i, (_, _, (cx, cy), deg, dur) in enumerate(fingers):
        out += f'<g>{rowgroups(buckets[i])}{rot(cx, cy, deg, dur, begin=-i * 0.7)}</g>'
    tx, ty, td = TILT[side]
    dx = 5 if side == "L" else -5
    drift = (f'<animateTransform attributeName="transform" type="translate" values="0 0;{dx} -4;0 0;{dx // 2} 4;0 0" dur="9s" '
             f'repeatCount="indefinite" calcMode="spline" keyTimes="0;.25;.5;.75;1" keySplines="{";".join([".37 0 .63 1"] * 4)}"/>')
    return f'<g><g>{out}{rot(tx, ty, td, 9)}</g>{drift}</g>'

L = SLOT * len(WORDS)
def f(t): return f"{t / L:.4f}".rstrip("0").rstrip(".") or "0"

def glyph(ch, x, intervals, cls):
    kt, vals = ["0"], ["0"]
    for a, b in intervals:
        kt += [f(a), f(b)]; vals += ["1", "0"]
    kt.append("1"); vals.append("0")
    return (f'<text class="{cls}" x="{x:.1f}" y="{BASE_Y}" text-anchor="middle" opacity="0">{html.escape(ch)}'
            f'<animate attributeName="opacity" dur="{L}s" repeatCount="indefinite" calcMode="discrete" '
            f'keyTimes="{";".join(kt)}" values="{";".join(vals)}"/></text>')

text = []
for w, word in enumerate(WORDS):
    t0 = w * SLOT
    x0 = CX - (len(word) - 1) * CW / 2
    for i, ch in enumerate(word):
        x = x0 + i * CW
        resolve = t0 + 0.3 + i * 0.12            # sequential reveal, start -> end
        t, n = t0 + 0.05, 0
        while t + STEP <= resolve:               # scramble glyphs until this letter settles
            text.append(glyph(random.choice(POOL), x, [(t, t + STEP)], "s")); t += STEP
        t_out = t0 + SLOT - OUT_FRAMES * STEP
        text.append(glyph(ch, x, [(resolve, t_out)], "w"))
        for k in range(OUT_FRAMES):               # scramble out before the next word
            text.append(glyph(random.choice(POOL), x, [(t_out + k * STEP, t_out + (k + 1) * STEP)], "s"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H - 200}" viewBox="0 150 {W} {H - 200}" role="img" aria-label="Two hands reaching toward each other while the words {", ".join(WORDS)} take turns appearing between them">
  <style>
    :root {{ --dot:#000; }}
    @media (prefers-color-scheme: dark) {{ :root {{ --dot:#fff; }} }}
    .hand {{ fill:var(--dot); }}
    .r {{ animation:shimmer 5s ease-in-out infinite; }}
    @keyframes shimmer {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:.7; }} }}
    text {{ font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:{FS}px; font-weight:600; }}
    .w {{ fill:var(--dot); }}
    .s {{ fill:var(--dot); fill-opacity:.4; }}
    @media (prefers-reduced-motion: reduce) {{ .r {{ animation:none; }} }}
  </style>
  <g class="hand">{hand("L")}<animateTransform attributeName="transform" type="translate" values="0 0;8 0;0 0" dur="6s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1" keyTimes="0;.5;1"/></g>
  <g class="hand">{hand("R")}<animateTransform attributeName="transform" type="translate" values="0 0;-8 0;0 0" dur="6s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1" keyTimes="0;.5;1"/></g>
  {"".join(text)}
</svg>
'''
open(out, "w", encoding="utf8").write(svg)
print(len(text), "glyph elements,", len(svg) // 1024, "KB")
