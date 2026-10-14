"""Genera los badges con marco naranja y brillo LED en assets/.
Uso: python scripts/badges.py"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets")


def text_w(s, size):
    return int(len(s) * size * 0.66)


def badge(name, label, value, accent):
    pad, size, h = 14, 13, 34
    lw = text_w(label, size) + 2 * pad
    vw = text_w(value, size) + 2 * pad
    w = lw + vw
    m = 12  # margen para que el brillo no se corte
    W, H = w + 2 * m, h + 2 * m
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{label}: {value}">
  <defs>
    <filter id="glow" x="-30%" y="-60%" width="160%" height="220%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="c"><rect x="{m}" y="{m}" width="{w}" height="{h}" rx="8"/></clipPath>
  </defs>
  <rect x="{m}" y="{m}" width="{w}" height="{h}" rx="8" fill="none" stroke="#FF6A00" stroke-width="2.5" filter="url(#glow)">
    <animate attributeName="stroke-opacity" values="1;0.55;1" dur="2.4s" repeatCount="indefinite"/>
  </rect>
  <g clip-path="url(#c)">
    <rect x="{m}" y="{m}" width="{lw}" height="{h}" fill="#111827"/>
    <rect x="{m + lw}" y="{m}" width="{vw}" height="{h}" fill="{accent}"/>
  </g>
  <rect x="{m}" y="{m}" width="{w}" height="{h}" rx="8" fill="none" stroke="#FF8A3D" stroke-width="1.5"/>
  <g font-family="Segoe UI,Verdana,DejaVu Sans,sans-serif" font-size="{size}" font-weight="700" letter-spacing="1" fill="#fff" text-anchor="middle" dominant-baseline="central">
    <text x="{m + lw / 2}" y="{m + h / 2}">{label}</text>
    <text x="{m + lw + vw / 2}" y="{m + h / 2}">{value}</text>
  </g>
</svg>
'''
    with open(os.path.join(OUT, f"{name}.svg"), "w", encoding="utf-8") as f:
        f.write(svg)


os.makedirs(OUT, exist_ok=True)
badge("escaparate", "EL ESCAPARATE", "WEB DEV", "#FF6A00")
badge("linkedin", "LINKEDIN", "CONECTA", "#0A66C2")
