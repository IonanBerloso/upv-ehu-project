#!/usr/bin/env python3
"""
inject_figures.py
Inserta las imágenes extraídas del PDF en los archivos HTML de ejercicios.
"""

import re
import json
from pathlib import Path

BASE = Path(__file__).parent

# CSS a añadir justo antes del cierre </style> en cada HTML
FIG_CSS = """\
/* ── FIGURAS PDF ── */
.fig-plano{background:#fff;border-radius:8px;padding:10px 12px;margin:14px 0 6px;text-align:center;border:1px solid #2a2a2a}
.fig-plano img{max-width:100%;height:auto;border-radius:4px;display:block;margin:0 auto}
.fig-plano+.fig-plano{margin-top:4px}
"""

# Mapeo: nombre_archivo_html → { num_problema: [rutas_imagen] }
# Solo para T4 (los únicos HTMLs con ejercicios CNC que necesitan figuras)
FIGURA_MAP = {
    "t1.html": {
        # P1-P4 no tienen figura de pieza, solo texto
        5:  ["img/t1/p05_a.png"],
        6:  ["img/t1/p06_a.png"],
        7:  ["img/t1/p07_a.png"],
        8:  ["img/t1/p08_a.png"],
        9:  ["img/t1/p09_a.png"],
    },
    "t2.html": {
        2:  ["img/t2/p02_a.png"],
        3:  ["img/t2/p03_a.png"],
        5:  ["img/t2/p05_a.png", "img/t2/p05_b.png"],
        7:  ["img/t2/p07_a.png"],
        8:  ["img/t2/p08_a.png"],
        9:  ["img/t2/p09_a.png", "img/t2/p09_b.png"],
    },
    "t3.html": {
        4:  ["img/t3/p03_a.png"],   # P4 figura está en la pagina de P3 del PDF (busqueda detectó P4 en pag22)
        5:  ["img/t3/p05_a.png"],
        6:  ["img/t3/p06_a.png", "img/t3/p06_b.png"],
    },
    "t4.html": {
        1:  ["img/t4/p01_a.png"],
        2:  ["img/t4/p02_a.png"],
        3:  ["img/t4/p03_a.png"],
        4:  ["img/t4/p04_a.png"],
        5:  ["img/t4/p05_a.png", "img/t4/p05_b.png"],
        6:  ["img/t4/p06_a.png"],
        7:  ["img/t4/p07_a.png"],
        8:  ["img/t4/p08_a.png", "img/t4/p08_b.png"],
        9:  ["img/t4/p09_a.png"],
        10: ["img/t4/p10_a.png"],
        11: ["img/t4/p11_a.png"],
        12: ["img/t4/p12_a.png", "img/t4/p12_b.png"],
        13: ["img/t4/p13_a.png", "img/t4/p13_b.png"],
    },
}

def make_fig_html(imgs):
    parts = []
    for src in imgs:
        # Verificar que la imagen existe
        if not (BASE / src).exists():
            print(f"  AVISO: no encontrada {src}")
            continue
        alt = src.split("/")[-1].replace(".png","")
        parts.append(f'<div class="fig-plano"><img src="{src}" alt="{alt}" loading="lazy"></div>')
    return "\n    ".join(parts)

def inject(html_file, prob_imgs):
    path = BASE / html_file
    if not path.exists():
        print(f"HTML no encontrado: {html_file}")
        return

    html = path.read_text(encoding="utf-8")
    original = html

    # 1. Añadir CSS si no existe ya
    if "fig-plano" not in html:
        html = html.replace("</style>", FIG_CSS + "</style>", 1)
        print(f"  CSS añadido a {html_file}")

    # 2. Para cada problema, insertar figura después del cierre de .enunciado
    #    Los cards en t4.html usan id="ex1", "ex2", ...
    #    En t1/t2/t3 usan id="ex1", "ex2", ...
    for prob_num, imgs in sorted(prob_imgs.items()):
        fig_html = make_fig_html(imgs)
        if not fig_html:
            continue

        # Buscar el card que contiene el ejercicio N
        # El card lleva id="exN" y dentro tiene <div class="enunciado">
        # Queremos insertar fig justo DESPUÉS de </div> de enunciado

        # Patrón: id del card con numero prob_num, y su primer cierre de enunciado
        # Necesitamos saber que hay un único </div> después de .enunciado
        # Buscamos: id="exN" ... <div class="enunciado"> ... </div>
        # e insertamos el fig justo después del </div> que cierra .enunciado

        # Estrategia: buscar la sección del card exN y dentro localizar el enunciado
        card_id = f'id="ex{prob_num}"'
        pos_card = html.find(card_id)
        if pos_card == -1:
            print(f"  Card ex{prob_num} no encontrado en {html_file}")
            continue

        # Dentro del card, buscar la primera ocurrencia de cierre de enunciado
        search_start = pos_card
        enun_close = html.find('</div>', html.find('<div class="enunciado">', search_start))
        if enun_close == -1:
            print(f"  .enunciado no encontrado para P{prob_num} en {html_file}")
            continue

        # Insertar fig justo después del </div> del enunciado
        insert_pos = enun_close + len('</div>')

        # Verificar que no haya ya una fig-plano insertada
        next_chunk = html[insert_pos:insert_pos+200]
        if "fig-plano" in next_chunk:
            print(f"  P{prob_num}: figura ya presente, omitiendo")
            continue

        fig_block = f"\n    {fig_html}"
        html = html[:insert_pos] + fig_block + html[insert_pos:]
        print(f"  P{prob_num}: {len(imgs)} imagen(es) insertada(s)")

    if html != original:
        path.write_text(html, encoding="utf-8")
        print(f"  {html_file} guardado.")
    else:
        print(f"  {html_file}: sin cambios.")

# ── Main ────────────────────────────────────────────────────────────────────
for fname, prob_imgs in FIGURA_MAP.items():
    print(f"\n=== {fname} ===")
    inject(fname, prob_imgs)

print("\nListo.")
