# Builds an animated dot-matrix SVG from a screenshot: hands drift toward each other, rows shimmer,
# and a word between them cycles with a "decrypt" (scramble -> settle) transition. Pure SVG, so GitHub renders it.
import sys, random, html
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
WORDS = "coding developing syncing building pushing deploy shipped merge testing".split()
SLOT, STEP, OUT_FRAMES = 3.6, 0.1, 3        # seconds per word, scramble step, scramble-out frames
POOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
CX, BASE_Y, CW, FS = 536, 336, 12.5, 19     # word centre x, baseline y, cell width, font size
random.seed(7)

im = Image.open(src).convert("L")
W, H = im.size
DX, DY = 6, 12
rows = {}
for y in range(DY // 2, H, DY):
    for x in range(DX // 2, W, DX):
        v = im.crop((x - DX // 2, y - DY // 2, x + DX // 2, y + DY // 2)).getextrema()[1]
        if v > 90:
            rows.setdefault(y, []).append((x, f'<circle cx="{x}" cy="{y}" r="{1 + 1.4 * v / 255:.1f}"/>'))

def hand(side):
    parts = []
    for n, y in enumerate(sorted(rows)):
        dots = "".join(c for x, c in rows[y] if (x < CX) == (side == "L"))
        if dots:
            parts.append(f'<g class="r" style="animation-delay:{(n * 0.12) % 3:.2f}s">{dots}</g>')
    return "".join(parts)

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
    .r {{ animation:shimmer 3s ease-in-out infinite; }}
    @keyframes shimmer {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:.45; }} }}
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
