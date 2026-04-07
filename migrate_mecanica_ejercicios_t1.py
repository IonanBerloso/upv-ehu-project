"""
Migrates mecanica/ejercicios/tema1.html to Kinetic Lab design system.
- Font: Inter → Space Grotesk
- :root{} tokens updated (purple accent preserved)
- All hardcoded dark colors → rgba tokens
- Adds figure to exercise 1.13
"""
import re, os

PATH = os.path.join(os.path.dirname(__file__), 'mecanica', 'ejercicios', 'tema1.html')

NEW_ROOT = """:root{
  --bg:#131313;
  --surface:rgba(255,255,255,.04);
  --surface2:rgba(255,255,255,.07);
  --border:rgba(255,255,255,.08);
  --border2:rgba(255,255,255,.12);
  --text:#e2e8f0;
  --text2:#94a3b8;
  --text3:#64748b;
  --accent:#c084fc;
  --accent-dim:rgba(192,132,252,.12);
  --accent-border:rgba(192,132,252,.28);
  --gold:#f59e0b;
  --gold-dim:rgba(245,158,11,.1);
  --gold-border:rgba(245,158,11,.28);
  --green:#10b981;
  --blue:#38bdf8;
  --orange:#fb923c;
  --yellow:#ffd93d;
  --ff:'Space Grotesk',system-ui,sans-serif;
  --ff-mono:'JetBrains Mono',monospace;
  --radius:10px;
  --radius-sm:6px;
  --transition:.22s cubic-bezier(.4,0,.2,1);
}"""

NEW_FONT = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

# Figure HTML to insert in ex13 enunciado
EX13_FIG = """
    <div style="text-align:center;margin:16px 0 4px">
      <img src="img/t1_ex13_fig.png" alt="Sistema de ejes: eje y con momento M, resultante R, puntos O-A-B sobre eje x, plano xz con distancias a y b" style="max-width:340px;width:100%;border-radius:8px;background:#fff;padding:10px">
    </div>"""

def migrate():
    with open(PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Font
    html = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^"]*" rel="stylesheet">',
        NEW_FONT, html
    )

    # 2. :root
    html = re.sub(r':root\s*\{[^}]*\}', NEW_ROOT, html, count=1, flags=re.DOTALL)

    # 3. font-family Inter → var(--ff)
    html = re.sub(r"font-family:'Inter'[^;\"']*", "font-family:var(--ff)", html)

    # 4. theme-color + topbar bg
    html = html.replace('content="#000000"', 'content="#131313"')
    html = html.replace('rgba(0,0,0,.95)', 'rgba(19,19,19,.92)')
    html = html.replace('rgba(0,0,0,.98)', 'rgba(19,19,19,.95)')

    # 5. Topbar height 56px → 52px
    html = html.replace('height:56px}', 'height:52px}')

    # 6. Pill / ph-type
    html = html.replace(
        'background:#1a0a30;border:1px solid #3b1f6e;border-radius:20px;padding:4px 12px;font-size:.7em;font-weight:600;color:var(--accent)',
        'background:var(--accent-dim);border:1px solid var(--accent-border);border-radius:20px;padding:4px 12px;font-size:.7em;font-weight:600;color:var(--accent)'
    )
    html = html.replace(
        'background:#1a0a30;border:1px solid #3b1f6e;border-radius:20px;padding:3px 12px;font-size:.72em;font-weight:700;color:var(--accent)',
        'background:var(--accent-dim);border:1px solid var(--accent-border);border-radius:20px;padding:3px 12px;font-size:.72em;font-weight:700;color:var(--accent)'
    )

    # 7. Jump link hover
    html = html.replace(
        'background:#1a0a30;color:var(--accent);border-color:var(--accent)',
        'background:var(--accent-dim);color:var(--accent);border-color:var(--accent-border)'
    )
    # Jump link exam
    html = html.replace(
        'background:#1a0f00;border-color:#854d0e;color:#fbbf24}',
        'background:var(--gold-dim);border-color:var(--gold-border);color:var(--gold)}'
    )
    html = html.replace(
        'background:#2a1a00;color:#fde68a;border-color:#f59e0b}',
        'background:rgba(245,158,11,.15);color:var(--gold);border-color:var(--gold)}'
    )

    # 8. Ex card hover
    html = html.replace('.ex-header:hover{background:#111}', '.ex-header:hover{background:var(--surface2)}')

    # 9. Sections
    # s-datos
    html = html.replace(
        '.s-datos .sec-btn{background:#1a0a30;color:var(--accent);border:1px solid #3b1f6e}',
        '.s-datos .sec-btn{background:var(--accent-dim);color:var(--accent);border:1px solid var(--accent-border)}'
    )
    html = html.replace(
        '.s-datos .sec-body{background:#0e0520;border:1px solid #3b1f6e;border-top:none}',
        '.s-datos .sec-body{background:rgba(192,132,252,.04);border:1px solid var(--accent-border);border-top:none}'
    )
    # s-formulas
    html = html.replace(
        '.s-formulas .sec-btn{background:#1a0f00;color:var(--orange);border:1px solid #2a1800}',
        '.s-formulas .sec-btn{background:rgba(251,146,60,.1);color:var(--orange);border:1px solid rgba(251,146,60,.25)}'
    )
    html = html.replace(
        '.s-formulas .sec-body{background:#0f0800;border:1px solid #2a1800;border-top:none}',
        '.s-formulas .sec-body{background:rgba(251,146,60,.05);border:1px solid rgba(251,146,60,.2);border-top:none}'
    )
    # s-teoria
    html = html.replace(
        '.s-teoria .sec-btn{background:#0a1a2e;color:var(--blue);border:1px solid #0d2a44}',
        '.s-teoria .sec-btn{background:rgba(56,189,248,.1);color:var(--blue);border:1px solid rgba(56,189,248,.25)}'
    )
    html = html.replace(
        '.s-teoria .sec-body{background:#050e1a;border:1px solid #0d2a44;border-top:none}',
        '.s-teoria .sec-body{background:rgba(56,189,248,.05);border:1px solid rgba(56,189,248,.2);border-top:none}'
    )
    # s-resolucion
    html = html.replace(
        '.s-resolucion .sec-btn{background:#001a0a;color:var(--green);border:1px solid #003318}',
        '.s-resolucion .sec-btn{background:rgba(16,185,129,.1);color:var(--green);border:1px solid rgba(16,185,129,.25)}'
    )
    html = html.replace(
        '.s-resolucion .sec-body{background:#00100a;border:1px solid #003318;border-top:none}',
        '.s-resolucion .sec-body{background:rgba(16,185,129,.05);border:1px solid rgba(16,185,129,.2);border-top:none}'
    )

    # 10. Tables
    html = html.replace(
        '.t-datos th{background:#1e0a3a;color:var(--accent);padding:7px 10px;text-align:left;border:1px solid #3b1f6e}',
        '.t-datos th{background:var(--accent-dim);color:var(--accent);padding:7px 10px;text-align:left;border:1px solid var(--accent-border)}'
    )
    html = html.replace(
        '.t-datos td{padding:7px 10px;border:1px solid #1a1a2a;color:#d0c8ff}',
        '.t-datos td{padding:7px 10px;border:1px solid var(--border);color:var(--text2)}'
    )
    html = html.replace(
        '.t-datos tr:nth-child(even) td{background:#0a0518}',
        '.t-datos tr:nth-child(even) td{background:rgba(192,132,252,.04)}'
    )

    # 11. Formula box
    html = html.replace(
        '.formula-box{background:#110800;border-left:3px solid var(--orange);border-radius:4px;padding:8px 14px;margin:6px 0;color:#ffe0c0;overflow-x:auto}',
        '.formula-box{background:rgba(251,146,60,.06);border-left:3px solid var(--orange);border-radius:4px;padding:8px 14px;margin:6px 0;color:#fed7aa;overflow-x:auto}'
    )

    # 12. Paso
    html = html.replace(
        '.paso{margin-bottom:14px;padding:10px 14px;background:#001508;border-radius:8px;border-left:3px solid #2a5a30}',
        '.paso{margin-bottom:14px;padding:10px 14px;background:rgba(16,185,129,.06);border-radius:8px;border-left:3px solid rgba(16,185,129,.4)}'
    )

    # 13. Resultado final
    html = html.replace(
        '.resultado-final{background:#001a08;border:1px solid #2a6a30;border-radius:8px;padding:12px 16px;margin-top:12px}',
        '.resultado-final{background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.3);border-radius:8px;padding:12px 16px;margin-top:12px}'
    )
    html = html.replace('.rf-val{color:#c8ffcc;font-size:.92em;line-height:1.9}',
                        '.rf-val{color:#d1fae5;font-size:.92em;line-height:1.9}')

    # 14. Nota
    html = html.replace(
        '.nota{background:#1a0a00;border:1px solid #3a1a00;border-radius:6px;padding:8px 12px;font-size:.8em;color:var(--orange);margin-top:8px;font-style:italic}',
        '.nota{background:rgba(251,146,60,.08);border:1px solid rgba(251,146,60,.2);border-radius:6px;padding:8px 12px;font-size:.8em;color:var(--orange);margin-top:8px;font-style:italic}'
    )

    # 15. Soon
    html = html.replace(
        '.soon{background:#050505;border:1px solid #1a1a1a;border-radius:8px;padding:20px;text-align:center;color:#333;font-size:.85em;font-style:italic}',
        '.soon{background:var(--surface);border:1px solid var(--border2);border-radius:8px;padding:20px;text-align:center;color:var(--text3);font-size:.85em;font-style:italic}'
    )

    # 16. Exam card
    html = html.replace(
        '.ex-card-exam{border-color:#854d0e}',
        '.ex-card-exam{border-color:var(--gold-border)}'
    )
    html = html.replace(
        '.ex-card-exam .ex-header:hover{background:#1a0f00}',
        '.ex-card-exam .ex-header:hover{background:rgba(245,158,11,.06)}'
    )
    html = html.replace(
        '.ex-card-exam .ex-header-left h2{color:#fbbf24}',
        '.ex-card-exam .ex-header-left h2{color:var(--gold)}'
    )
    html = html.replace(
        '.ex-card-exam.open .ex-arrow{color:#fbbf24}',
        '.ex-card-exam.open .ex-arrow{color:var(--gold)}'
    )
    html = html.replace(
        '.exam-badge{display:inline-flex;align-items:center;gap:5px;background:#1a0f00;border:1px solid #854d0e;border-radius:20px;padding:3px 10px;font-size:.7em;font-weight:700;color:#fbbf24;margin-left:10px;vertical-align:middle;letter-spacing:.03em}',
        '.exam-badge{display:inline-flex;align-items:center;gap:5px;background:var(--gold-dim);border:1px solid var(--gold-border);border-radius:20px;padding:3px 10px;font-size:.7em;font-weight:700;color:var(--gold);margin-left:10px;vertical-align:middle;letter-spacing:.03em}'
    )

    # 17. Scrollbar
    html = html.replace(
        '::-webkit-scrollbar-thumb{background:#3b1f6e;border-radius:3px}',
        '::-webkit-scrollbar-thumb{background:rgba(192,132,252,.18);border-radius:3px}'
    )

    # 18. Tema picker dropdown
    html = html.replace(
        '.tema-picker-btn{background:#1a0a30;border:1px solid #3b1f6e;border-radius:20px;padding:4px 14px;font-size:.72em;font-weight:700;color:var(--accent);cursor:pointer;white-space:nowrap;display:flex;align-items:center;gap:6px;transition:.15s}',
        '.tema-picker-btn{background:var(--accent-dim);border:1px solid var(--accent-border);border-radius:20px;padding:4px 14px;font-size:.72em;font-weight:700;color:var(--accent);cursor:pointer;white-space:nowrap;display:flex;align-items:center;gap:6px;transition:.15s}'
    )
    html = html.replace(
        '.tema-picker-btn:hover{background:#240f44}',
        '.tema-picker-btn:hover{background:rgba(192,132,252,.2)}'
    )
    html = html.replace(
        '.tema-dropdown{display:none;position:absolute;right:0;top:calc(100% + 8px);background:#0d0d0d;border:1px solid #2a1a4a;border-radius:10px;padding:6px;min-width:250px;z-index:300;box-shadow:0 8px 32px rgba(0,0,0,.85)}',
        '.tema-dropdown{display:none;position:absolute;right:0;top:calc(100% + 8px);background:rgba(19,19,19,.98);border:1px solid var(--accent-border);border-radius:10px;padding:6px;min-width:250px;z-index:300;box-shadow:0 8px 32px rgba(0,0,0,.85)}'
    )
    html = html.replace(
        '.td-item.td-available:hover{background:#1a0a30;color:var(--accent)}',
        '.td-item.td-available:hover{background:var(--accent-dim);color:var(--accent)}'
    )
    html = html.replace(
        '.td-item.td-active{color:var(--accent);background:#1a0a30;font-weight:700;pointer-events:none}',
        '.td-item.td-active{color:var(--accent);background:var(--accent-dim);font-weight:700;pointer-events:none}'
    )
    html = html.replace(
        '.td-sep{padding:4px 12px 2px;font-size:.65em;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#4a3a6a;pointer-events:none;user-select:none;margin-top:2px}',
        '.td-sep{padding:4px 12px 2px;font-size:.65em;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text3);pointer-events:none;user-select:none;margin-top:2px}'
    )
    html = html.replace(
        '.td-sep-line{border:none;border-top:1px solid #1e1030;margin:4px 6px}',
        '.td-sep-line{border:none;border-top:1px solid var(--border);margin:4px 6px}'
    )

    # 19. Enunciado
    html = html.replace(
        '.enunciado{background:#080808;border-radius:8px;padding:14px 16px;font-size:.88em;line-height:1.75;margin-bottom:16px;border-left:3px solid #2a1a4a;white-space:pre-wrap}',
        '.enunciado{background:var(--surface2);border-radius:8px;padding:14px 16px;font-size:.88em;line-height:1.75;margin-bottom:16px;border-left:3px solid var(--accent-border);white-space:pre-wrap}'
    )

    # 20. Topbar title emoji removal
    html = html.replace('⚙️ Tema 1 · Fundamentos de Cálculo Vectorial — Ejercicios',
                        'Mecánica · Tema 1 <span style="color:var(--accent)">· Cálculo Vectorial</span>')

    # 21. Add figure to exercise 1.13 enunciado
    # Insert after opening <div class="ex-body"> of ex13
    old_ex13 = '<div class="ex-card ex-card-exam" id="ex13">'
    if old_ex13 in html:
        # Find the enunciado div inside ex13 and insert the figure after it
        # Look for the specific enunciado content of ex13
        html = html.replace(
            '<div class="ex-card ex-card-exam" id="ex13">',
            '<div class="ex-card ex-card-exam" id="ex13">'
        )
        # Insert figure between enunciado and first seccion in ex13
        target = (
            '<p>Se conocen los siguientes datos del sistema de dos vectores deslizantes'
        )
        if target in html:
            # Insert figure right before the enunciado paragraph opens
            html = html.replace(
                '  <div class="ex-body">\n\n    <div class="enunciado">\n      <p>Se conocen los siguientes datos',
                '  <div class="ex-body">\n' + EX13_FIG + '\n\n    <div class="enunciado">\n      <p>Se conocen los siguientes datos'
            )

    # 22. Clean extra blank lines
    html = re.sub(r'\n{3,}', '\n\n', html)

    with open(PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print('OK mecanica/ejercicios/tema1.html')


if __name__ == '__main__':
    migrate()
