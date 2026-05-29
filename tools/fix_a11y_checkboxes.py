"""Añade aria-label a los checkboxes del plan de estudio de index.html.

Cada casilla solo envuelve un <span> vacío; el nombre del tema vive en un <a>
hermano, así que los lectores de pantalla la anuncian "sin etiquetar"
(WCAG 1.3.1 / 4.1.2). Aquí derivamos el nombre del tema y lo inyectamos como
aria-label en el <input>. Idempotente: salta los que ya lo tienen.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'index.html')
TAG = re.compile(r'<[^>]+>')

s = open(P, encoding='utf-8').read()
lines = s.split('\n')
n = 0
for i, line in enumerate(lines):
    if ('onchange="onPlanCheck' not in line or 'tema-name' not in line
            or 'aria-label=' in line):
        continue
    name_m = re.search(r'<span class="tema-name">(.*?)</span><span class="tema-arrow">', line)
    tag_m = re.search(r'<span class="tema-tag">(.*?)</span>', line)
    if not name_m:
        continue
    name = TAG.sub('', name_m.group(1)).replace('★', '').strip()
    tag = TAG.sub('', tag_m.group(1)).strip() if tag_m else ''
    label = 'Marcar como estudiado: ' + ((tag + ' · ' + name) if tag else name)
    label = label.replace('"', "'")
    lines[i] = line.replace('<input type="checkbox"',
                            '<input type="checkbox" aria-label="%s"' % label, 1)
    n += 1

open(P, 'w', encoding='utf-8').write('\n'.join(lines))
print('aria-label añadido a %d checkboxes del plan' % n)
