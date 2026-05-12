# -*- coding: utf-8 -*-
"""
Constructor del Cerebro UPV-EHU: vault Obsidian unificado.

Genera un vault nuevo en `C:\\Users\\Usuario\\Desktop\\Cerebro UPV-EHU\\`
con:
 - Teoría extraída de HTML para Mecánica, Sistemas y Fluidos
 - 236 fichas de ejercicios ya extraídas (portadas del vault v1)
 - Exámenes de Fluidos (14 HTMLs convertidos)
 - Formularios y utilidades (propiedades, colebrook, errores, etc.)
 - PDFs originales como adjuntos
 - Imágenes copiadas a _attachments
 - MOCs, HOME, plantillas

Uso: python build_cerebro_vault.py
"""
from __future__ import annotations

import re
import sys
import shutil
import subprocess
from pathlib import Path

# UTF-8 stdout en Windows
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    sys.stderr.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

try:
    from bs4 import BeautifulSoup, NavigableString  # type: ignore
except ImportError:
    print("[init] beautifulsoup4 no encontrado, instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup, NavigableString  # type: ignore


# ---------------------------------------------------------------------------
# RUTAS
# ---------------------------------------------------------------------------
SRC = Path(r"c:\Users\Usuario\Desktop\Antigravity\upv-ehu-project")
OLD_VAULT = SRC / "obsidian" / "Proyecto 2025 2026"
VAULT = Path(r"c:\Users\Usuario\Desktop\Cerebro UPV-EHU")

MECANICA = VAULT / "01 - Mecánica Aplicada"
SISTEMAS = VAULT / "02 - Sistemas de Producción"
FLUIDOS = VAULT / "03 - Mecánica de Fluidos"
MATES = VAULT / "04 - Matemáticas (apoyo)"
ATTACH = VAULT / "_attachments"


# ---------------------------------------------------------------------------
# UTILIDADES MARKDOWN/LATEX
# ---------------------------------------------------------------------------
RE_DISPLAY_MATH = re.compile(r"\\\[(.+?)\\\]", re.DOTALL)
RE_INLINE_MATH = re.compile(r"\\\((.+?)\\\)", re.DOTALL)


def latex_to_obsidian(text: str) -> str:
    text = RE_DISPLAY_MATH.sub(lambda m: f"\n$$\n{m.group(1).strip()}\n$$\n", text)
    text = RE_INLINE_MATH.sub(lambda m: f"${m.group(1).strip()}$", text)
    return text


def strip_latex(text: str) -> str:
    text = re.sub(r"\$\$?(.+?)\$\$?", r"\1", text, flags=re.DOTALL)
    text = re.sub(r"\\([a-zA-Z]+)", r"\1", text)
    text = re.sub(r"[{}\\]", "", text)
    return text.strip()


def sanitize_filename(text: str, maxlen: int = 80) -> str:
    text = strip_latex(text)
    text = re.sub(r"[<>:\"|?*/\\]", "-", text)
    text = text.replace("·", "-")
    text = re.sub(r"\s+", " ", text)
    return text.strip()[:maxlen]


def html_to_md(element, depth: int = 0) -> str:
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
        elif name == "div" and any(c in cls for c in ("box", "box-note", "note-box")):
            inner = html_to_md(child, depth + 1).strip()
            btype = "note"
            if "warn" in cls:
                btype = "warning"
            elif "danger" in cls or "alert" in cls:
                btype = "danger"
            elif "tip" in cls or "hint" in cls:
                btype = "tip"
            quoted = "\n".join(f"> {ln}" for ln in inner.splitlines() if ln.strip())
            parts.append(f"\n> [!{btype}]\n{quoted}\n\n")
        elif name in ("div", "span", "section", "article"):
            parts.append(html_to_md(child, depth + 1))
        elif name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(name[1])
            parts.append("\n" + "#" * level + " " + html_to_md(child, depth + 1).strip() + "\n\n")
        else:
            parts.append(child.get_text())
    return latex_to_obsidian("".join(parts))


def table_to_md(table) -> str:
    rows = table.find_all("tr")
    if not rows:
        return ""
    headers = [html_to_md(c).strip().replace("\n", " ") for c in rows[0].find_all(["th", "td"])]
    if not headers:
        return ""
    lines = ["", "| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows[1:]:
        cells = [html_to_md(c).strip().replace("\n", " ") for c in row.find_all(["td", "th"])]
        if not cells:
            continue
        while len(cells) < len(headers):
            cells.append("")
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 1 · SCAFFOLDING DEL VAULT
# ---------------------------------------------------------------------------
def build_scaffolding():
    print("📁 Creando estructura del vault...")
    folders = [
        VAULT / "00 - INICIO",
        MECANICA / "Teoría",
        MECANICA / "Ejercicios",
        MECANICA / "Exámenes",
        SISTEMAS / "Teoría",
        SISTEMAS / "Ejercicios",
        FLUIDOS / "Teoría",
        FLUIDOS / "Ejercicios",
        FLUIDOS / "Exámenes",
        FLUIDOS / "Utilidades",
        MATES,
        VAULT / "99 - Conceptos atómicos",
        VAULT / "_templates",
        ATTACH / "pdf" / "mecanica" / "teoria",
        ATTACH / "pdf" / "mecanica" / "ejercicios",
        ATTACH / "pdf" / "mecanica" / "examenes",
        ATTACH / "pdf" / "sistemas",
        ATTACH / "pdf" / "fluidos",
        ATTACH / "img" / "mecanica",
        ATTACH / "img" / "fluidos",
    ]
    for f in folders:
        f.mkdir(parents=True, exist_ok=True)
    print(f"  ✓ {len(folders)} carpetas creadas")


# ---------------------------------------------------------------------------
# 2 · EXTRACCIÓN DE TEORÍA (topic-panel con sections)
# ---------------------------------------------------------------------------
def extract_theory_from_html(html_path: Path, out_dir: Path, asig_slug: str, asig_name: str):
    if not html_path.exists():
        print(f"  ⚠ No existe {html_path}")
        return 0
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    panels = soup.find_all("div", class_="topic-panel")
    count = 0
    for panel in panels:
        tema_id = panel.get("id", "").lstrip("t")
        try:
            tema_num = int(tema_id)
        except ValueError:
            continue
        title_el = panel.find("h1", class_="panel-title")
        if not title_el:
            continue
        title = title_el.get_text(" ", strip=True)

        body_parts = []
        for sec in panel.find_all("div", class_="section", recursive=True):
            label_el = sec.find("div", class_="section-label")
            if label_el:
                label = label_el.get_text(" ", strip=True)
                body_parts.append(f"\n## {label}\n")
            for child in sec.children:
                if isinstance(child, NavigableString):
                    continue
                cls = child.get("class", []) if hasattr(child, "get") else []
                if "section-label" in cls:
                    continue
                if "prose" in cls:
                    body_parts.append(html_to_md(child).strip() + "\n\n")
                elif "fkey" in cls or "fblock" in cls:
                    flabel_el = child.find("div", class_="flabel")
                    flabel = flabel_el.get_text(" ", strip=True) if flabel_el else ""
                    # extraer el LaTeX inline que sigue al flabel
                    raw = child.get_text(" ", strip=True)
                    if flabel:
                        raw = raw.replace(flabel, "", 1).strip()
                    formula_md = latex_to_obsidian(raw)
                    callout_type = "abstract" if "fkey" in cls else "info"
                    body_parts.append(
                        f"\n> [!{callout_type}] {flabel}\n> {formula_md}\n\n"
                    )
                elif "box" in cls:
                    title_el = child.find("div", class_="box-title")
                    btitle = title_el.get_text(" ", strip=True) if title_el else ""
                    btype = "note"
                    if "warn" in cls:
                        btype = "warning"
                    elif "danger" in cls or "error" in cls:
                        btype = "danger"
                    elif "tip" in cls:
                        btype = "tip"
                    inner_text = child.get_text("\n", strip=True)
                    if btitle:
                        inner_text = inner_text.replace(btitle, "", 1).strip()
                    inner_text = latex_to_obsidian(inner_text)
                    quoted = "\n".join(f"> {ln}" for ln in inner_text.splitlines() if ln.strip())
                    body_parts.append(f"\n> [!{btype}] {btitle}\n{quoted}\n\n")
                else:
                    sub = html_to_md(child).strip()
                    if sub:
                        body_parts.append(sub + "\n\n")

        body = "".join(body_parts).strip()
        title_clean = sanitize_filename(title)
        filename = f"Tema {tema_num} - {title_clean}.md"
        fm = (
            "---\n"
            f'title: "Tema {tema_num} — {title}"\n'
            f'aliases: ["T{tema_num} teoría", "Teoría tema {tema_num}"]\n'
            "tags:\n"
            "  - teoria\n"
            f"  - asig/{asig_slug}\n"
            f"  - tema/{tema_num}\n"
            f"asignatura: {asig_name}\n"
            f"tema: {tema_num}\n"
            "tipo: teoria\n"
            "---\n\n"
        )
        header = f"# Tema {tema_num} — {title}\n\n"
        header += f"> [!info] Teoría oficial UPV/EHU\n> Asignatura: {asig_name}\n\n"
        (out_dir / filename).write_text(fm + header + body, encoding="utf-8")
        count += 1
        print(f"    ✓ {filename}")
    return count


# ---------------------------------------------------------------------------
# 3 · EXTRACCIÓN DE EXÁMENES (Fluidos — ex-card)
# ---------------------------------------------------------------------------
def extract_exam_from_html(html_path: Path, out_dir: Path):
    if not html_path.exists():
        return 0
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    cards = soup.find_all("div", class_="ex-card")
    stem = html_path.stem  # e.g. "mayo2020"

    # Extraer título del examen
    h1 = soup.find("h1")
    exam_title = h1.get_text(" ", strip=True) if h1 else stem

    # Agrupar todos los ejercicios del examen en un único MD
    body = [f"# Examen {stem} — {exam_title}\n\n"]
    body.append("> [!info] Examen oficial UPV/EHU\n> Fuente: boletín publicado · Convenio g=9,8 m/s²\n\n")

    for card in cards:
        card_id = card.get("id", "")
        h2 = card.find("h2")
        ex_title = h2.get_text(" ", strip=True) if h2 else card_id
        body.append(f"## {ex_title}\n\n")

        # enunciado
        enun = card.find("div", class_="enunciado")
        if enun:
            body.append(html_to_md(enun).strip() + "\n\n")

        # secciones internas (datos, conceptos, resolución, resultado, verificación)
        for sec in card.find_all("div", class_="section-wrap"):
            btn = sec.find("button", class_="sec-btn")
            bd = sec.find("div", class_="sec-body")
            if not btn or not bd:
                continue
            btn_text = btn.get_text(" ", strip=True)
            body.append(f"### {btn_text}\n\n")
            # Resolución → buscar pasos
            if "resoluc" in btn_text.lower():
                pasos = bd.find_all("div", class_="paso")
                if pasos:
                    for paso in pasos:
                        pt = paso.find("div", class_="paso-titulo")
                        ptitle = pt.get_text(" ", strip=True) if pt else ""
                        content = []
                        for ch in paso.children:
                            if isinstance(ch, NavigableString):
                                content.append(str(ch))
                                continue
                            cls = ch.get("class", []) if hasattr(ch, "get") else []
                            if "paso-titulo" in cls:
                                continue
                            content.append(html_to_md(ch))
                        pcontent = latex_to_obsidian("".join(content)).strip()
                        body.append(f"#### {ptitle}\n\n{pcontent}\n\n")
                else:
                    body.append(html_to_md(bd).strip() + "\n\n")
            else:
                body.append(html_to_md(bd).strip() + "\n\n")

        # resultado final
        rf = card.find("div", class_="resultado-final")
        if rf:
            rfv = rf.find("div", class_="rf-val")
            rfv_md = html_to_md(rfv).strip() if rfv else html_to_md(rf).strip()
            body.append(f"### ✅ Resultado\n\n> [!success]\n> {rfv_md}\n\n")

        body.append("\n---\n\n")

    fm = (
        "---\n"
        f'title: "Examen Fluidos {stem}"\n'
        f'aliases: ["Examen {stem}", "{stem}"]\n'
        "tags:\n"
        "  - examen\n"
        "  - asig/fluidos\n"
        f"  - examen/{stem}\n"
        "asignatura: Mecánica de Fluidos\n"
        "tipo: examen\n"
        "---\n\n"
    )
    (out_dir / f"Examen {stem}.md").write_text(fm + "".join(body), encoding="utf-8")
    print(f"    ✓ Examen {stem}.md")
    return 1


# ---------------------------------------------------------------------------
# 4 · EXTRACCIÓN DE FORMULARIO FLUIDOS (block + frow)
# ---------------------------------------------------------------------------
def extract_formulario_fluidos(html_path: Path, out_dir: Path):
    if not html_path.exists():
        return 0
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    body = [
        "# 🌊 Formulario — Mecánica de Fluidos\n\n",
        "> [!info] Formulario completo UPV/EHU\n> Convenio: g = 9,8 m/s², P_atm = 101 325 Pa\n\n",
    ]

    for block in soup.find_all("div", class_="block"):
        title_el = block.find("div", class_="block-title")
        btitle = title_el.get_text(" ", strip=True) if title_el else "Bloque"
        body.append(f"## {btitle}\n\n")
        for row in block.find_all("div", class_="frow"):
            name_el = row.find("span", class_="fname")
            math_el = row.find("span", class_="fmath")
            if name_el and math_el:
                fname = name_el.get_text(" ", strip=True)
                fmath_raw = math_el.get_text(" ", strip=True)
                fmath = latex_to_obsidian(fmath_raw)
                body.append(f"- **{fname}**: {fmath}\n")
        body.append("\n")
        # condiciones
        for cond in block.find_all("div", class_="cond"):
            body.append(f"> [!note]\n> {cond.get_text(' ', strip=True)}\n\n")

    fm = (
        "---\n"
        'title: "Formulario de Mecánica de Fluidos"\n'
        'aliases: ["Formulario Fluidos", "Fórmulas Fluidos"]\n'
        "tags: [formulario, asig/fluidos]\n"
        "asignatura: Mecánica de Fluidos\n"
        "tipo: formulario\n"
        "---\n\n"
    )
    (out_dir / "Formulario - Mecánica de Fluidos.md").write_text(fm + "".join(body), encoding="utf-8")
    print("    ✓ Formulario - Mecánica de Fluidos.md")
    return 1


# ---------------------------------------------------------------------------
# 5 · EXTRACCIÓN GENÉRICA DE HTML COMO MD ÚNICO (propiedades, colebrook, etc.)
# ---------------------------------------------------------------------------
def extract_generic_html_to_md(html_path: Path, out_path: Path, title: str, tags: list[str], asig: str):
    if not html_path.exists():
        return False
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    # Eliminar sidebars, topbars, scripts
    for tag in soup.find_all(["script", "style", "nav", "header", "aside"]):
        tag.decompose()
    for cls in ("topbar", "sidebar", "side-bar", "breadcrumb", "sb", "sb-list", "sb-head", "toc"):
        for el in soup.find_all(class_=cls):
            el.decompose()

    main = soup.find("main") or soup.find("div", class_="content") or soup.body
    if main is None:
        return False
    body_md = html_to_md(main).strip()

    # Limpieza de líneas repetidas/vacías excesivas
    body_md = re.sub(r"\n{3,}", "\n\n", body_md)

    tags_yaml = "\n".join(f"  - {t}" for t in tags)
    fm = (
        "---\n"
        f'title: "{title}"\n'
        "tags:\n"
        f"{tags_yaml}\n"
        f"asignatura: {asig}\n"
        "---\n\n"
    )
    out_path.write_text(fm + f"# {title}\n\n" + body_md, encoding="utf-8")
    print(f"    ✓ {out_path.name}")
    return True


# ---------------------------------------------------------------------------
# 6 · COPIAR ATTACHMENTS (PDFs e imágenes)
# ---------------------------------------------------------------------------
def copy_attachments():
    print("📎 Copiando PDFs e imágenes...")

    # PDFs Mecánica Teoría
    for pdf in (SRC / "mecanica" / "teoria").glob("*.pdf"):
        dst = ATTACH / "pdf" / "mecanica" / "teoria" / pdf.name
        shutil.copy2(pdf, dst)
        print(f"  ✓ {pdf.name}")

    # PDFs Mecánica Ejercicios (los propios generados)
    for pdf in (SRC / "mecanica" / "ejercicios" / "pdf").glob("*.pdf"):
        dst = ATTACH / "pdf" / "mecanica" / "ejercicios" / pdf.name
        shutil.copy2(pdf, dst)
        print(f"  ✓ ejercicios/{pdf.name}")

    # PDFs Mecánica Exámenes
    if (SRC / "mecanica" / "examenes").exists():
        for pdf in (SRC / "mecanica" / "examenes").glob("*.pdf"):
            dst = ATTACH / "pdf" / "mecanica" / "examenes" / pdf.name
            shutil.copy2(pdf, dst)
            print(f"  ✓ examenes/{pdf.name}")

    # PDFs Sistemas
    for pdf in (SRC / "sistemas" / "ejercicios").glob("*.pdf"):
        dst = ATTACH / "pdf" / "sistemas" / pdf.name
        shutil.copy2(pdf, dst)
        print(f"  ✓ sistemas/{pdf.name}")

    # PDFs Fluidos ejercicios
    for pdf in (SRC / "fluidos" / "ejercicios").glob("*.pdf"):
        dst = ATTACH / "pdf" / "fluidos" / pdf.name
        shutil.copy2(pdf, dst)
        print(f"  ✓ fluidos/{pdf.name}")

    # PDFs Fluidos examenes
    if (SRC / "fluidos" / "EXAMENES PDF").exists():
        for pdf in (SRC / "fluidos" / "EXAMENES PDF").glob("*.pdf"):
            dst = ATTACH / "pdf" / "fluidos" / pdf.name
            shutil.copy2(pdf, dst)
            print(f"  ✓ fluidos/{pdf.name}")

    # Imágenes Mecánica
    mec_img_src = SRC / "mecanica" / "ejercicios" / "img"
    if mec_img_src.exists():
        mec_img_dst = ATTACH / "img" / "mecanica"
        mec_img_dst.mkdir(parents=True, exist_ok=True)
        for img in mec_img_src.glob("*.png"):
            shutil.copy2(img, mec_img_dst / img.name)
        png_count = len(list(mec_img_src.glob("*.png")))
        print(f"  ✓ {png_count} imágenes Mecánica")

    # Imágenes Fluidos
    flu_img_src = SRC / "fluidos" / "examenes" / "img"
    if flu_img_src.exists():
        flu_img_dst = ATTACH / "img" / "fluidos"
        flu_img_dst.mkdir(parents=True, exist_ok=True)
        for img in flu_img_src.glob("*.png"):
            shutil.copy2(img, flu_img_dst / img.name)
        png_count = len(list(flu_img_src.glob("*.png")))
        print(f"  ✓ {png_count} imágenes Fluidos")


# ---------------------------------------------------------------------------
# 7 · PORTAR EJERCICIOS DEL VAULT VIEJO AL NUEVO
# ---------------------------------------------------------------------------
def port_exercises():
    print("🧮 Portando ejercicios del vault v1 al nuevo...")
    # Mecánica Aplicada → Ejercicios por tema
    count_mec = 0
    for tema in range(1, 9):
        src_dirs = list((OLD_VAULT / "01 - Mecánica Aplicada").glob(f"Tema {tema} - */Ejercicios"))
        if not src_dirs:
            continue
        dst_dir = MECANICA / "Ejercicios" / src_dirs[0].parent.name
        dst_dir.mkdir(parents=True, exist_ok=True)
        for md in src_dirs[0].glob("*.md"):
            shutil.copy2(md, dst_dir / md.name)
            count_mec += 1
    print(f"  ✓ {count_mec} ejercicios Mecánica")

    # Sistemas
    count_sis = 0
    for tema in range(1, 5):
        src_dirs = list((OLD_VAULT / "02 - Sistemas de Producción").glob(f"T{tema} - */Ejercicios"))
        if not src_dirs:
            continue
        dst_dir = SISTEMAS / "Ejercicios" / src_dirs[0].parent.name
        dst_dir.mkdir(parents=True, exist_ok=True)
        for md in src_dirs[0].glob("*.md"):
            shutil.copy2(md, dst_dir / md.name)
            count_sis += 1
    print(f"  ✓ {count_sis} ejercicios Sistemas")

    # Fluidos — estructura de bloques
    count_flu = 0
    src_flu = OLD_VAULT / "03 - Mecánica de Fluidos"
    if src_flu.exists():
        for bloque_dir in src_flu.glob("Bloque *"):
            dst_dir = FLUIDOS / "Ejercicios" / bloque_dir.name
            dst_dir.mkdir(parents=True, exist_ok=True)
            for md in (bloque_dir / "Ejercicios").glob("*.md"):
                shutil.copy2(md, dst_dir / md.name)
                count_flu += 1
    print(f"  ✓ {count_flu} ejercicios Fluidos")


# ---------------------------------------------------------------------------
# 8 · PORTAR PLANTILLAS
# ---------------------------------------------------------------------------
def port_templates():
    print("📋 Copiando plantillas...")
    src = OLD_VAULT / "05 - Templates"
    if not src.exists():
        return
    for md in src.glob("*.md"):
        shutil.copy2(md, VAULT / "_templates" / md.name)
        print(f"  ✓ {md.name}")


# ---------------------------------------------------------------------------
# 9 · CREAR MOCs Y HOME
# ---------------------------------------------------------------------------
def write_mocs_and_home():
    print("🗺️ Creando MOCs y HOME...")

    home = """---
title: "HOME — Cerebro UPV/EHU"
tags: [moc, home]
---

# 🧠 Cerebro UPV/EHU

> [!abstract] Dashboard principal
> Vault Obsidian unificado: teoría + ejercicios + exámenes + formularios.
> Curso **2025-2026** · Ingeniería Industrial UPV/EHU.

## 📚 Asignaturas

| Asignatura | MOC | Prioridad | Temas | Ejercicios |
|------------|-----|-----------|-------|------------|
| Mecánica Aplicada | [[MOC - Mecánica Aplicada]] | alta | 8 | 152 |
| Sistemas de Producción | [[MOC - Sistemas de Producción]] | alta | 4 | 37 |
| Mecánica de Fluidos | [[MOC - Mecánica de Fluidos]] | media (mayo 2026) | 3 bloques | 57 |

## 📐 Convenios UPV/EHU

> [!warning] Importante
> - **g = 9,8 m/s²** (nunca 9,81)
> - Ejercicios con **(*)** = laboratorio
> - En CNC: sintaxis **Fagor 8025M/T**
> - Presión atmosférica: 101 325 Pa

## 🎯 Qué hay aquí

- **Teoría oficial** extraída de los HTML publicados
- **Ejercicios resueltos**: 246 fichas con estructura Enunciado/Datos/Conceptos/Resolución/Resultado/Verificación/Errores
- **Exámenes** resueltos o con enunciados
- **Formularios** con ecuaciones clave
- **PDFs originales** como adjuntos

## 🔗 Enlaces rápidos

- [[MOC - Mecánica Aplicada]]
- [[MOC - Sistemas de Producción]]
- [[MOC - Mecánica de Fluidos]]
- [[Formulario - Mecánica de Fluidos]]

## 🛠️ Utilidades y apoyo

- [[04 - Matemáticas (apoyo)/Guía]] — apoyo matemático

## 📂 Adjuntos

Los PDFs originales del profesor están en `_attachments/pdf/...`.
Las imágenes (figuras de ejercicios y exámenes) en `_attachments/img/...`.
"""
    (VAULT / "00 - INICIO" / "HOME.md").write_text(home, encoding="utf-8")
    print("  ✓ 00 - INICIO/HOME.md")

    instr = """---
title: "Cómo usar este vault"
tags: [moc, ayuda]
---

# 📖 Cómo usar este vault

## Estructura

- `00 - INICIO/` → HOME y guía
- `01 - Mecánica Aplicada/` → Teoría + Ejercicios + Exámenes
- `02 - Sistemas de Producción/` → Teoría + Ejercicios
- `03 - Mecánica de Fluidos/` → Teoría + Ejercicios + Exámenes + Formulario + Utilidades
- `04 - Matemáticas (apoyo)/` → Apoyo matemático
- `99 - Conceptos atómicos/` → Zettelkasten (crece con el tiempo)
- `_templates/` → Plantillas de Obsidian
- `_attachments/` → PDFs e imágenes originales

## Navegación

- Usa los **MOCs** (Mapas de Contenido) para orientarte
- Los **tags** `#asig/mecanica`, `#tema/4`, `#nivel/examen` filtran contenido
- Cada ejercicio está en su carpeta de tema

## Tags principales

- `#ejercicio` → fichas de ejercicios resueltos
- `#teoria` → fichas de teoría oficial
- `#examen` → fichas de exámenes
- `#formulario` → formularios y tablas
- `#asig/mecanica` | `#asig/sistemas` | `#asig/fluidos`
- `#tema/N` → número de tema (1-8 Mecánica, 1-4 Sistemas, bloques 1-3 Fluidos)
- `#nivel/examen` → ejercicios de nivel examen

## RAG con IA local

Este vault también es la base de conocimientos del **RAG** conectado a LM Studio + Open WebUI. Cuando se edita una ficha, se puede re-sincronizar con `Workspace → Conocimiento → Sincroniza Directorio`.
"""
    (VAULT / "00 - INICIO" / "Cómo usar este vault.md").write_text(instr, encoding="utf-8")
    print("  ✓ 00 - INICIO/Cómo usar este vault.md")

    # MOC Mecánica
    moc_mec = """---
title: "MOC - Mecánica Aplicada"
tags: [moc, asig/mecanica]
asignatura: Mecánica Aplicada
---

# 🔩 MOC · Mecánica Aplicada

> [!info] Estructura de la asignatura
> 8 temas · 152 ejercicios (67 nivel examen) · Convenio: g = 9,8 m/s²

## 📚 Temas

| # | Tema | Teoría | Ejercicios | Nivel examen |
|---|------|--------|------------|--------------|
| 1 | Cálculo Vectorial | [[Tema 1 - Fundamentos de Cálculo Vectorial]] | 18 | — |
| 2 | Geometría de Masas | [[Tema 2 - Geometría de Masas y Superficies Planas]] | 17 | — |
| 3 | Estática del Sólido Rígido | [[Tema 3 - Estática del Sólido Rígido]] | 27 | 3.21-3.27 ⭐ |
| 4 | Rozamiento | [[Tema 4 - Rozamiento]] | 22 | 4.11-4.22 ⭐ |
| 5 | Cables | [[Tema 5 - Cables]] | 16 | 5.7-5.16 ⭐ |
| 6 | Resistencia de Materiales | [[Tema 6 - Principios de Resistencia de Materiales]] | 22 | 6.17-6.22 ⭐ |
| 7 | Cinemática del Sólido Rígido | [[Tema 7 - Cinemática del Sólido Rígido]] | 10 | — |
| 8 | Movimiento Plano | [[Tema 8 - Movimiento Plano del Sólido Rígido]] | 10 | — |

## 🎓 Exámenes

Los PDFs están en `_attachments/pdf/mecanica/examenes/`:
- 2017-18 Dinámica
- 2018-19 Dinámica (2)
- 2018-19 Estática (2)
- 2324 Enero Estática
- 2425 Ordinaria Estática
- 2425 Extraordinaria Estática

## 🔗 PDFs originales

- Teoría: `_attachments/pdf/mecanica/teoria/`
- Ejercicios: `_attachments/pdf/mecanica/ejercicios/`
"""
    (MECANICA / "MOC - Mecánica Aplicada.md").write_text(moc_mec, encoding="utf-8")
    print("  ✓ 01 - Mecánica Aplicada/MOC.md")

    # MOC Sistemas
    moc_sis = """---
title: "MOC - Sistemas de Producción"
tags: [moc, asig/sistemas]
asignatura: Sistemas de Producción
---

# 🏭 MOC · Sistemas de Producción

> [!info] Estructura de la asignatura
> 4 temas · 37 ejercicios · CNC con sintaxis Fagor 8025M/T en T4

## 📚 Temas

| # | Tema | Teoría | Ejercicios |
|---|------|--------|------------|
| 1 | Torneado | [[Tema 1 - Fundamentos de Mecanizado - Torneado]] | 9 |
| 2 | Fresado | [[Tema 2 - Fresado]] | 9 |
| 3 | Taladrado | [[Tema 3 - Taladrado]] | 6 |
| 4 | CNC ⭐ | [[Tema 4 - CNC]] | 13 (todos nivel examen) |

## 🎯 Conceptos transversales

- Ecuación de Taylor (vida de herramienta)
- Fuerza específica de corte: $p_s = K \\cdot h^{-m}$ (Kienzle)
- Velocidad de corte $v_c$
- Rugosidad: $R_t = f^2 \\cdot 1000/(8 r_\\varepsilon)$
- Ciclo CSS (velocidad de corte constante)

## 🔧 Códigos CNC Fagor (Tema 4)

- G96 / G97 → velocidad constante vs rpm fija
- G37 / G38 → entrada / salida tangencial
- G22 / G20 / G24 → subrutinas
- G73 → giro de coordenadas
- G81 / G83 → taladrado simple / profundo
- G86 → roscado (torneado)
- G88 / G89 → cajera rectangular / circular
- G41 / G40 → compensación radio herramienta
- G43 / G44 → corrección longitud

## 🔗 PDFs originales

- Boletín oficial: `_attachments/pdf/sistemas/Problemas_ 2526_est.pdf`
- Tema 5 Rectificado: `_attachments/pdf/sistemas/Tema 5 - Rectificado.pdf`
"""
    (SISTEMAS / "MOC - Sistemas de Producción.md").write_text(moc_sis, encoding="utf-8")
    print("  ✓ 02 - Sistemas de Producción/MOC.md")

    # MOC Fluidos
    moc_flu = """---
title: "MOC - Mecánica de Fluidos"
tags: [moc, asig/fluidos]
asignatura: Mecánica de Fluidos
---

# 💧 MOC · Mecánica de Fluidos

> [!warning] Prioridad: mayo 2026
> Asignatura no prioritaria hasta mayo 2026.

> [!info] Estructura por BLOQUES
> UPV/EHU organiza el boletín en **3 bloques** (conjuntos de temas), no por temas individuales.

## 📚 Bloques de ejercicios

| # | Bloque | Temas UPV | Contenido | Ejercicios |
|---|--------|-----------|-----------|------------|
| 1 | Propiedades de los Fluidos | 1-2 | Viscosidad, compresibilidad, capilaridad | 13 |
| 2 | Estática de Fluidos | 3-4 y 7-8 | Manómetros, compuertas, empujes | 24 |
| 3 | Dinámica y Medidores | 12-13 | Bernoulli, bombas, venturímetros | 20 |

## 📖 Teoría

- Teoría general completa (ver carpeta `Teoría/`)

## 📋 Formularios y utilidades

- [[Formulario - Mecánica de Fluidos]]
- Propiedades de fluidos
- Ecuación de Colebrook
- Errores frecuentes
- Estrategia de resolución
- Simulacro examen
- Banco de problemas

## 🎓 Exámenes

- Mayo 2020, 2021, 2024, 2025
- Junio 2020, 2021, 2022, 2023 (ordinaria y extraordinaria)

Los PDFs: `_attachments/pdf/fluidos/`

## 🎯 Conceptos clave

- Ecuación de Bernoulli
- Ecuación de continuidad
- Número de Reynolds
- Pérdidas por fricción (Darcy-Weisbach)
- Cavitación
- Golpe de ariete
- Viscosidad absoluta vs cinemática
- Capilaridad
- Empuje sobre superficies planas / curvas
- Venturímetro, diafragma, Pitot

## 🔗 Convenios

> [!abstract]
> - g = 9,8 m/s² (no 9,81)
> - Densidad relativa: `s` (Specific gravity)
> - Presión: Pa o kgf/cm² según enunciado
> - Ejercicios (*) = laboratorio
"""
    (FLUIDOS / "MOC - Mecánica de Fluidos.md").write_text(moc_flu, encoding="utf-8")
    print("  ✓ 03 - Mecánica de Fluidos/MOC.md")


# ---------------------------------------------------------------------------
# 10 · MAIN
# ---------------------------------------------------------------------------
def main():
    print("=" * 70)
    print(" 🧠 Constructor del CEREBRO UPV-EHU")
    print("=" * 70)
    print(f" Source: {SRC}")
    print(f" Target: {VAULT}")
    print("=" * 70)

    # 1. Scaffolding
    build_scaffolding()

    # 2. Teoría
    print("\n📖 Extrayendo TEORÍA de Mecánica...")
    extract_theory_from_html(
        SRC / "mecanica" / "teoria.html",
        MECANICA / "Teoría",
        "mecanica",
        "Mecánica Aplicada",
    )

    print("\n📖 Extrayendo TEORÍA de Sistemas...")
    extract_theory_from_html(
        SRC / "sistemas" / "teoria.html",
        SISTEMAS / "Teoría",
        "sistemas",
        "Sistemas de Producción",
    )

    print("\n📖 Extrayendo TEORÍA de Fluidos...")
    # Fluidos teoria.html también tiene topic-panel
    extract_theory_from_html(
        SRC / "fluidos" / "teoria.html",
        FLUIDOS / "Teoría",
        "fluidos",
        "Mecánica de Fluidos",
    )

    # 3. Formulario y utilidades Fluidos
    print("\n📋 Extrayendo FORMULARIO y UTILIDADES de Fluidos...")
    extract_formulario_fluidos(SRC / "fluidos" / "formulario.html", FLUIDOS)

    flu_utils = [
        ("propiedades.html", "Propiedades de los fluidos", ["utilidad", "asig/fluidos", "propiedades"]),
        ("colebrook.html", "Ecuación de Colebrook-White", ["utilidad", "asig/fluidos", "colebrook"]),
        ("errores.html", "Errores frecuentes en Fluidos", ["utilidad", "asig/fluidos", "errores"]),
        ("estrategia.html", "Estrategia de resolución Fluidos", ["utilidad", "asig/fluidos", "estrategia"]),
        ("simulacro.html", "Simulacro de examen Fluidos", ["utilidad", "asig/fluidos", "simulacro"]),
        ("banco.html", "Banco de problemas Fluidos", ["utilidad", "asig/fluidos", "banco"]),
        ("bombas-calc.html", "Calculadora de bombas", ["utilidad", "asig/fluidos", "bombas"]),
    ]
    for src_name, title, tags in flu_utils:
        extract_generic_html_to_md(
            SRC / "fluidos" / src_name,
            FLUIDOS / "Utilidades" / f"{title}.md",
            title, tags, "Mecánica de Fluidos",
        )

    # 4. Formulario Mecánica
    print("\n📋 Extrayendo FORMULARIO de Mecánica...")
    extract_generic_html_to_md(
        SRC / "mecanica" / "formulario.html",
        MECANICA / "Formulario - Mecánica Aplicada.md",
        "Formulario - Mecánica Aplicada",
        ["formulario", "asig/mecanica"],
        "Mecánica Aplicada",
    )

    # 5. Matemáticas apoyo
    print("\n📐 Extrayendo MATEMÁTICAS (apoyo)...")
    extract_generic_html_to_md(
        SRC / "matematicas" / "guia.html",
        MATES / "Guía matemáticas.md",
        "Guía matemáticas (apoyo)",
        ["utilidad", "apoyo", "matematicas"],
        "Matemáticas",
    )

    # 6. Exámenes Fluidos
    print("\n🎓 Extrayendo EXÁMENES de Fluidos...")
    exam_dir = SRC / "fluidos" / "examenes"
    count = 0
    if exam_dir.exists():
        for html in exam_dir.glob("*.html"):
            count += extract_exam_from_html(html, FLUIDOS / "Exámenes")
    print(f"  → {count} exámenes Fluidos creados")

    # 7. Portar ejercicios del vault viejo
    print("\n🧮 Portando EJERCICIOS del vault anterior...")
    port_exercises()

    # 8. Plantillas
    print("\n📋 Plantillas...")
    port_templates()

    # 9. PDFs e imágenes
    print()
    copy_attachments()

    # 10. MOCs y HOME
    print()
    write_mocs_and_home()

    print("\n" + "=" * 70)
    print(" ✅ CEREBRO UPV-EHU construido")
    print(f" 📁 Ubicación: {VAULT}")
    print("=" * 70)


if __name__ == "__main__":
    main()
