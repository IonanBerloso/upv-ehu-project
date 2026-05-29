"""Sube el contraste del token --text3 a >=4.5:1 (WCAG 1.4.3 AA) en todo el sitio.

#64748b (3.9:1 sobre #131313) y #475569 (2.45:1) -> #7d8a99.
Solo toca la DEFINICION del token (--text3:...), no los usos decorativos
(#475569 en trazos SVG, color:#475569 en .td-soon, etc.) ni el vault obsidian/.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEW = '#7d8a99'
REPLACEMENTS = [
    ('--text3:#64748b', f'--text3:{NEW}'),
    ('--text3:#475569', f'--text3:{NEW}'),
    ('--text3: #64748b', f'--text3: {NEW}'),
    ('--text3: #475569', f'--text3: {NEW}'),
]

changed = []
for dirpath, dirs, files in os.walk(ROOT):
    parts = dirpath.split(os.sep)
    if 'obsidian' in parts or '.git' in parts:
        dirs[:] = []
        continue
    for fn in files:
        if not fn.endswith('.html'):
            continue
        p = os.path.join(dirpath, fn)
        with open(p, encoding='utf-8') as f:
            s = f.read()
        orig = s
        for a, b in REPLACEMENTS:
            s = s.replace(a, b)
        if s != orig:
            with open(p, 'w', encoding='utf-8') as f:
                f.write(s)
            changed.append(os.path.relpath(p, ROOT))

print(f'Contraste --text3 actualizado en {len(changed)} archivos.')
for c in changed:
    print('  ', c)
