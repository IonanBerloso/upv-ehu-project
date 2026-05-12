# -*- coding: utf-8 -*-
"""
Extractor HTML -> Obsidian Markdown para el vault UPV/EHU.

Lee los HTML de ejercicios (Mecanica y Sistemas) y genera una ficha
.md por ejercicio en el vault de Obsidian con frontmatter YAML y
secciones compatibles con la plantilla del usuario.

Uso:
    python extract_html_to_obsidian.py
"""
from __future__ import annotations

import re
import sys
import subprocess
from pathlib import Path

# Forzar UTF-8 en stdout/stderr (Windows usa cp1252 por defecto)
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    sys.stderr.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

# --- asegurar beautifulsoup4 ---
try:
    from bs4 import BeautifulSoup, NavigableString  # type: ignore
except ImportError:
    print("[init] beautifulsoup4 no encontrado, instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup, NavigableString  # type: ignore

# ---------------------------------------------------------------------------
# RUTAS
# ---------------------------------------------------------------------------
ROOT = Path(r"c:\Users\Usuario\Desktop\Antigravity\upv-ehu-project")
VAULT = ROOT / "obsidian" / "Proyecto 2025 2026"
HTML_MEC = ROOT / "mecanica" / "ejercicios"
HTML_SIS = ROOT / "sistemas" / "ejercicios"
HTML_FLU_BOLETIN = ROOT / "fluidos" / "boletin"
HTML_FLU_EXAMENES = ROOT / "fluidos" / "examenes"

TEMAS_MECANICA = {
    1: "Cálculo Vectorial",
    2: "Geometría de Masas",
    3: "Estática del Sólido Rígido",
    4: "Rozamiento",
    5: "Cables",
    6: "Resistencia de Materiales",
    7: "Cinemática del Sólido Rígido",
    8: "Movimiento Plano",
}
TEMAS_SISTEMAS = {
    1: "Torneado",
    2: "Fresado",
    3: "Taladrado",
    4: "CNC",
}
# Fluidos UPV/EHU usa BLOQUES (conjuntos de temas), no temas individuales.
# El primer número del ejercicio = nº de bloque.
BLOQUES_FLUIDOS = {
    1: "Propiedades de los Fluidos (temas 1-2)",
    2: "Estática de Fluidos (temas 3-4 y 7-8)",
    3: "Dinámica y Medidores (temas 12-13)",
}
# Archivos del boletín de Fluidos (todos los ejercicios se colocan según su bloque)
BOLETIN_FLUIDOS = [
    "temas-01-02.html",
    "temas-03-04.html",
    "temas-07-08.html",
    "tema-12.html",
    "tema-13.html",
]

EXAM_MECANICA = {
    3: list(range(21, 28)),   # 3.21 - 3.27
    4: list(range(11, 23)),   # 4.11 - 4.22
    5: list(range(7, 17)),    # 5.7 - 5.16
    6: list(range(17, 23)),   # 6.17 - 6.22
}
EXAM_SISTEMAS = {
    1: [7, 8, 9],
    2: [7, 8, 9],
    3: [5, 6],
    4: list(range(1, 14)),  # todos
}
EXAM_FLUIDOS: dict[int, list[int]] = {}  # sin marcar nivel examen por ahora

# ---------------------------------------------------------------------------
# UTILIDADES DE CONVERSION
# ---------------------------------------------------------------------------
RE_DISPLAY_MATH = re.compile(r"\\\[(.+?)\\\]", re.DOTALL)
RE_INLINE_MATH = re.compile(r"\\\((.+?)\\\)", re.DOTALL)


def latex_to_obsidian(text: str) -> str:
    """Convierte \\(...\\) -> $...$ y \\[...\\] -> $$...$$."""
    text = RE_DISPLAY_MATH.sub(lambda m: f"\n$$\n{m.group(1).strip()}\n$$\n", text)
    text = RE_INLINE_MATH.sub(lambda m: f"${m.group(1).strip()}$", text)
    return text


def html_to_md(element, depth: int = 0) -> str:
    """Convierte un nodo BeautifulSoup en Markdown preservando LaTeX."""
    if element is None:
        return ""

    if isinstance(element, NavigableString):
        return str(element)

    parts: list[str] = []
    for child in element.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
            continue

        cls = child.get("class", []) if hasattr(child, "get") else []
        name = child.name

        if name in ("script", "style"):
            continue
        if name in ("strong", "b"):
            parts.append(f"**{html_to_md(child, depth + 1).strip()}**")
        elif name in ("em", "i"):
            parts.append(f"*{html_to_md(child, depth + 1).strip()}*")
        elif name == "br":
            parts.append("\n")
        elif name == "p":
            parts.append(html_to_md(child, depth + 1).rstrip() + "\n\n")
        elif name == "img":
            src = child.get("src", "")
            alt = child.get("alt", "")
            parts.append(f"\n![{alt}]({src})\n\n")
        elif name == "ul":
            for li in child.find_all("li", recursive=False):
                parts.append(f"- {html_to_md(li, depth + 1).strip()}\n")
            parts.append("\n")
        elif name == "ol":
            for i, li in enumerate(child.find_all("li", recursive=False), 1):
                parts.append(f"{i}. {html_to_md(li, depth + 1).strip()}\n")
            parts.append("\n")
        elif name == "table":
            parts.append(table_to_md(child))
        elif name == "div" and "nota" in cls:
            inner = html_to_md(child, depth + 1).strip()
            quoted = "\n".join(f"> {ln}" for ln in inner.splitlines() if ln.strip())
            parts.append(f"\n> [!note]\n{quoted}\n\n")
        elif name == "div" and "paso-titulo" in cls:
            # manejado en extract_pasos, aquí se ignora
            continue
        elif name in ("div", "span", "section", "article"):
            parts.append(html_to_md(child, depth + 1))
        elif name in ("h1", "h2", "h3", "h4"):
            level = int(name[1])
            parts.append("\n" + "#" * level + " " + html_to_md(child, depth + 1).strip() + "\n\n")
        else:
            parts.append(child.get_text())

    return latex_to_obsidian("".join(parts))


def table_to_md(table) -> str:
    rows = table.find_all("tr")
    if not rows:
        return ""
    header_cells = [html_to_md(c).strip().replace("\n", " ") for c in rows[0].find_all(["th", "td"])]
    if not header_cells:
        return ""
    lines = ["", "| " + " | ".join(header_cells) + " |", "|" + "|".join(["---"] * len(header_cells)) + "|"]
    for row in rows[1:]:
        cells = [html_to_md(c).strip().replace("\n", " ") for c in row.find_all(["td", "th"])]
        if not cells:
            continue
        # padear si alguna fila tiene menos columnas
        while len(cells) < len(header_cells):
            cells.append("")
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    return "\n".join(lines)


def extract_pasos(resolucion_body) -> str:
    md = ""
    pasos = resolucion_body.find_all("div", class_="paso")
    for i, paso in enumerate(pasos, 1):
        titulo_elem = paso.find("div", class_="paso-titulo")
        titulo = titulo_elem.get_text(strip=True) if titulo_elem else f"Paso {i}"
        titulo = latex_to_obsidian(titulo)

        # reconstruir contenido saltando el titulo
        parts: list[str] = []
        for child in paso.children:
            if isinstance(child, NavigableString):
                parts.append(str(child))
                continue
            cls = child.get("class", []) if hasattr(child, "get") else []
            if "paso-titulo" in cls:
                continue
            parts.append(html_to_md(child))
        # Aplicar latex_to_obsidian al contenido completo porque los nodos de texto
        # (como ecuaciones \[...\] sueltas entre párrafos) no pasan por html_to_md
        content = latex_to_obsidian("".join(parts)).strip()
        md += f"### {titulo}\n\n{content}\n\n"
    return md


# ---------------------------------------------------------------------------
# EXTRACCION POR EJERCICIO
# ---------------------------------------------------------------------------
RE_NUMERO = re.compile(r"(\d+)[.\s]+P?(\d+)", re.IGNORECASE)


def extract_exercise(panel, asignatura: str):
    tag_el = panel.find("div", class_="panel-tag")
    title_el = panel.find("h1", class_="panel-title")
    if not tag_el or not title_el:
        return None

    tag_text = tag_el.get_text(strip=True)  # "Ejercicio 4.1" o "T4.P1"
    m = RE_NUMERO.search(tag_text)
    if not m:
        return None
    tema_ex, num_ex = int(m.group(1)), int(m.group(2))
    numero = f"{tema_ex}.{num_ex}"

    title_raw = title_el.get_text(" ", strip=True)
    title = latex_to_obsidian(title_raw)

    meta_el = panel.find("div", class_="panel-meta")
    meta = meta_el.get_text(" ", strip=True) if meta_el else ""

    enun_el = panel.find("div", class_="enunciado")
    enunciado = html_to_md(enun_el).strip() if enun_el else ""

    fig_el = panel.find("div", class_="fig-wrap")
    figura = html_to_md(fig_el).strip() if fig_el else ""

    datos_md = ""
    conceptos_md = ""
    resolucion_md = ""
    for sec in panel.find_all("div", class_="section-wrap"):
        btn = sec.find("button", class_="sec-btn")
        body = sec.find("div", class_="sec-body")
        if not btn or not body:
            continue
        btn_text = btn.get_text(" ", strip=True)
        low = btn_text.lower()
        # Orden importante: "resoluc" antes que "solu" (solu está dentro de resolución)
        if "dato" in low:
            datos_md = html_to_md(body).strip()
        elif "resoluc" in low or "desarrollo" in low or "programa" in low:
            resolucion_md = extract_pasos(body) or html_to_md(body).strip()
        elif "concepto" in low or "teor" in low or "soluci" in low:
            conceptos_md = html_to_md(body).strip()

    res_el = panel.find("div", class_="resultado-final")
    resultado = ""
    if res_el:
        rfv = res_el.find("div", class_="rf-val")
        resultado = html_to_md(rfv).strip() if rfv else html_to_md(res_el).strip()

    veri_el = panel.find("div", class_="verificacion")
    verificacion = html_to_md(veri_el).strip() if veri_el else ""
    verificacion = re.sub(r"^\s*✓?\s*Verificaci[oó]n\s*", "", verificacion)

    err_el = panel.find("div", class_="errores")
    errores = html_to_md(err_el).strip() if err_el else ""
    errores = re.sub(r"^\s*⚠?\s*Error(?:es)?\s+frecuentes?\s*", "", errores)

    exam_map = {"mecanica": EXAM_MECANICA, "sistemas": EXAM_SISTEMAS, "fluidos": EXAM_FLUIDOS}[asignatura]
    is_exam = num_ex in exam_map.get(tema_ex, [])

    return {
        "numero": numero,
        "tema": tema_ex,
        "num_ex": num_ex,
        "title": title.strip(),
        "meta": meta,
        "is_exam": is_exam,
        "enunciado": enunciado,
        "figura": figura,
        "datos": datos_md,
        "conceptos": conceptos_md,
        "resolucion": resolucion_md,
        "resultado": resultado,
        "verificacion": verificacion,
        "errores": errores,
    }


# ---------------------------------------------------------------------------
# CONSTRUCCION DEL MARKDOWN
# ---------------------------------------------------------------------------
def strip_latex_for_title(text: str) -> str:
    text = re.sub(r"\$\$?(.+?)\$\$?", r"\1", text, flags=re.DOTALL)
    text = re.sub(r"\\([a-zA-Z]+)", r"\1", text)  # \\mu -> mu
    text = re.sub(r"[{}\\]", "", text)
    return text.strip()


def sanitize_filename(text: str) -> str:
    text = strip_latex_for_title(text)
    text = re.sub(r"[<>:\"|?*/\\]", "-", text)
    text = text.replace("·", "-")
    text = re.sub(r"\s+", " ", text)
    return text.strip()[:80]


def build_markdown(ex: dict, asignatura: str) -> str:
    asig_display = {
        "mecanica": "Mecánica Aplicada",
        "sistemas": "Sistemas de Producción",
        "fluidos": "Mecánica de Fluidos",
    }[asignatura]
    tags = ["ejercicio", f"asig/{asignatura}", f"tema/{ex['tema']}"]
    if ex["is_exam"]:
        tags.append("nivel/examen")

    title_clean = strip_latex_for_title(ex["title"]).replace('"', "'")

    tags_yaml = "\n".join(f"  - {t}" for t in tags)
    fm = (
        "---\n"
        f'title: "Ejercicio {ex["numero"]} — {title_clean}"\n'
        "aliases:\n"
        f'  - "Ejercicio {ex["numero"]}"\n'
        f'  - "{ex["numero"]}"\n'
        "tags:\n"
        f"{tags_yaml}\n"
        f"asignatura: {asig_display}\n"
        f"tema: {ex['tema']}\n"
        f'numero: "{ex["numero"]}"\n'
        "estado: pendiente\n"
        f"dificultad: {'⭐⭐⭐⭐' if ex['is_exam'] else '⭐⭐⭐'}\n"
        f"examen: {'nivel-examen' if ex['is_exam'] else ''}\n"
        "---\n\n"
    )

    body = f"# Ejercicio {ex['numero']} — {ex['title']}\n\n"

    if ex["meta"]:
        body += f"> [!info] Conceptos implicados\n> {ex['meta']}\n\n"

    if ex["is_exam"]:
        body += "> [!warning] Nivel examen\n> Este ejercicio es de nivel examen.\n\n"

    body += "## 📋 Enunciado\n\n" + ex["enunciado"].strip() + "\n\n"
    if ex["figura"]:
        body += ex["figura"].strip() + "\n\n"
    if ex["datos"]:
        body += "## 📐 Datos\n\n" + ex["datos"].strip() + "\n\n"
    if ex["conceptos"]:
        body += "## 💡 Conceptos clave\n\n" + ex["conceptos"].strip() + "\n\n"
    if ex["resolucion"]:
        body += "## 🧮 Resolución\n\n" + ex["resolucion"].strip() + "\n\n"
    if ex["resultado"]:
        body += (
            "## ✅ Resultado\n\n"
            f"> [!success] Resultado final\n> {ex['resultado']}\n\n"
        )
    if ex["verificacion"]:
        body += "## ✓ Verificación\n\n"
        veri = "\n".join(f"> {ln}" for ln in ex["verificacion"].splitlines() if ln.strip())
        body += f"> [!info] Comprobación\n{veri}\n\n"
    if ex["errores"]:
        body += "## ⚠️ Errores frecuentes\n\n"
        err = "\n".join(f"> {ln}" for ln in ex["errores"].splitlines() if ln.strip())
        body += f"> [!danger] Cuidado\n{err}\n\n"

    return fm + body


# ---------------------------------------------------------------------------
# PROCESO PRINCIPAL
# ---------------------------------------------------------------------------
def process_html(html_path: Path, out_dir: Path, asignatura: str) -> int:
    """Procesa un HTML donde todos los ejercicios van a la misma carpeta de salida."""
    if not html_path.exists():
        print(f"  ⚠ No existe {html_path.name}")
        return 0
    html = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    panels = soup.find_all("div", class_="topic-panel")
    out_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    for panel in panels:
        ex = extract_exercise(panel, asignatura)
        if not ex:
            continue
        md = build_markdown(ex, asignatura)
        title_clean = sanitize_filename(ex["title"])
        filename = f"Ejercicio {ex['numero']} - {title_clean}.md"
        (out_dir / filename).write_text(md, encoding="utf-8")
        count += 1
        marker = " ⭐" if ex["is_exam"] else ""
        print(f"    ✓ {ex['numero']}: {title_clean[:60]}{marker}")
    return count


def process_fluidos_boletin(html_path: Path, asignatura: str = "fluidos") -> int:
    """Procesa un HTML de boletín de Fluidos donde los ejercicios pueden
    pertenecer a varios temas. Cada ejercicio va a la carpeta de su tema."""
    if not html_path.exists():
        print(f"  ⚠ No existe {html_path.name}")
        return 0
    html = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    panels = soup.find_all("div", class_="topic-panel")

    count = 0
    for panel in panels:
        ex = extract_exercise(panel, asignatura)
        if not ex:
            continue
        # El primer número del ejercicio indica el BLOQUE en Fluidos (no el tema)
        bloque = ex["tema"]
        bloque_name = BLOQUES_FLUIDOS.get(bloque, f"Bloque {bloque}")
        out_dir = VAULT / "03 - Mecánica de Fluidos" / f"Bloque {bloque} - {bloque_name}" / "Ejercicios"
        out_dir.mkdir(parents=True, exist_ok=True)

        md = build_markdown(ex, asignatura)
        title_clean = sanitize_filename(ex["title"])
        filename = f"Ejercicio {ex['numero']} - {title_clean}.md"
        (out_dir / filename).write_text(md, encoding="utf-8")
        count += 1
        print(f"    ✓ {ex['numero']}: {title_clean[:60]}")
    return count


def main():
    print("=" * 70)
    print(" Extracción HTML → Markdown para vault Obsidian UPV/EHU")
    print("=" * 70)

    total = 0

    print("\n📚 MECÁNICA APLICADA")
    for tema in range(1, 9):
        nombre = TEMAS_MECANICA[tema]
        print(f"\n  Tema {tema} - {nombre}")
        out = VAULT / "01 - Mecánica Aplicada" / f"Tema {tema} - {nombre}" / "Ejercicios"
        n = process_html(HTML_MEC / f"tema{tema}.html", out, "mecanica")
        print(f"  → {n} ejercicios creados")
        total += n

    print("\n🏭 SISTEMAS DE PRODUCCIÓN")
    for tema in range(1, 5):
        nombre = TEMAS_SISTEMAS[tema]
        print(f"\n  T{tema} - {nombre}")
        out = VAULT / "02 - Sistemas de Producción" / f"T{tema} - {nombre}" / "Ejercicios"
        n = process_html(HTML_SIS / f"t{tema}.html", out, "sistemas")
        print(f"  → {n} ejercicios creados")
        total += n

    print("\n💧 MECÁNICA DE FLUIDOS")
    for filename in BOLETIN_FLUIDOS:
        print(f"\n  Boletín {filename}")
        n = process_fluidos_boletin(HTML_FLU_BOLETIN / filename, "fluidos")
        print(f"  → {n} ejercicios creados")
        total += n

    print("\n" + "=" * 70)
    print(f" ✅ TOTAL: {total} fichas de ejercicios generadas")
    print(f" 📁 Ubicación: {VAULT}")
    print("=" * 70)


if __name__ == "__main__":
    main()
