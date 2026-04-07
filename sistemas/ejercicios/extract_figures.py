#!/usr/bin/env python3
"""
extract_figures.py
Extrae las páginas con figuras del PDF de problemas y las guarda como PNG.
Genera también el mapeo ejercicio → imagen para insertar en los HTMLs.
"""

import fitz
from pathlib import Path
import json

PDF_PATH = Path(__file__).parent / "Problemas_ 2526_est.pdf"
OUT_DIR  = Path(__file__).parent / "img"
OUT_DIR.mkdir(exist_ok=True)

DPI_SCALE = 2.0   # 2× = ~144 Dpi — buena resolución en pantalla
MATRIX    = fitz.Matrix(DPI_SCALE, DPI_SCALE)

doc = fitz.open(str(PDF_PATH))
total = len(doc)
print(f"PDF: {total} páginas")

SKIP_PAGES = 4   # portada + blanco + TOC(2 pags) = 4 paginas a ignorar

# ── 1. Localizar dónde empieza cada tema (ignorar TOC) ──────────────────────
tema_starts = {}
for i in range(SKIP_PAGES, total):
    t = doc[i].get_text()
    for n in range(1, 9):
        key = f"Tema {n}:"
        # En contenido real viene seguido de texto largo; en TOC seguido de "Problema"
        # Basta con que la pagina contenga "Tema N:" y NO sea una pagina de TOC
        if key in t and n not in tema_starts:
            # Verificar que no sea pagina de TOC (TOC tiene muchos "Problema X" en pocas lineas)
            count_prob = t.count("Problema ")
            if count_prob < 5:   # en contenido real rara vez hay 5+ problemas en 1 pagina
                tema_starts[n] = i
                print(f"  Tema {n} -> pagina PDF {i+1}")

# ── 2. Para cada tema, localizar cada problema ──────────────────────────────
import re
mapping = {}

for tema in sorted(tema_starts):
    t_start = tema_starts[tema]
    t_end   = tema_starts.get(tema + 1, total)
    mapping[tema] = {}

    max_p = {1: 9, 2: 9, 3: 6, 4: 13}.get(tema, 15)

    problem_pages = {}
    for i in range(t_start, t_end):
        t = doc[i].get_text()
        for p in range(max_p, 0, -1):  # descending to get first occurrence
            # Patron: "Problema N" rodeado de espacios/newlines
            pat = rf'(?:^|\n)\s*Problema {p}\s*(?:\(|$|\n)'
            if re.search(pat, t) and p not in problem_pages:
                problem_pages[p] = i

    mapping[tema] = problem_pages
    for p, pg in sorted(problem_pages.items()):
        print(f"  T{tema}.P{p} -> pagina PDF {pg+1}")

# ── 3. Renderizar y guardar ─────────────────────────────────────────────────
saved = {}   # { "t4_p1": ["img/t4_p1_a.png", ...] }

for tema in mapping:
    tema_dir = OUT_DIR / f"t{tema}"
    tema_dir.mkdir(exist_ok=True)

    probs = sorted(mapping[tema].items())
    for idx, (p, pg_start) in enumerate(probs):
        # Determinar hasta qué página renderizar:
        # desde pg_start hasta el inicio del siguiente problema (o +3 máx)
        next_pg_start = probs[idx + 1][1] if idx + 1 < len(probs) else pg_start + 4
        pg_end = min(next_pg_start, pg_start + 3)  # máximo 3 páginas por problema

        key = f"t{tema}_p{p}"
        saved[key] = []

        for offset, pg_idx in enumerate(range(pg_start, pg_end)):
            if pg_idx >= total:
                break
            pix  = doc[pg_idx].get_pixmap(matrix=MATRIX)
            fname = f"p{p:02d}_{chr(97+offset)}.png"   # p01_a.png, p01_b.png ...
            out   = tema_dir / fname
            pix.save(str(out))
            rel   = f"img/t{tema}/{fname}"
            saved[key].append(rel)
            print(f"  Guardado: {rel}")

doc.close()

# ── 4. Escribir mapeo JSON para usarlo en HTML ──────────────────────────────
map_path = Path(__file__).parent / "fig_map.json"
with open(map_path, "w", encoding="utf-8") as f:
    json.dump(saved, f, indent=2, ensure_ascii=False)
print(f"\nMapeo guardado en {map_path}")
print("Listo.")
