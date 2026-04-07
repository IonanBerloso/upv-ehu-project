"""
Crop exercise figures from exam PDF pages using PyMuPDF drawing detection.
Saves cropped images to fluidos/examenes/img/
"""
import fitz
import os

FOLDER = r'C:\Users\Usuario\Desktop\Antigravity\upv-ehu-project\fluidos\EXAMENES PDF'
PDF = os.path.join(FOLDER, os.listdir(FOLDER)[0])
OUT = r'C:\Users\Usuario\Desktop\Antigravity\upv-ehu-project\fluidos\examenes\img'
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
OFFSET = 6
DPI = 200
SCALE = DPI / 72

# Map: exam -> list of (doc_page, exercise_numbers_on_that_page)
# Determined by reading PDF content
EXAM_PAGES = {
    'junio2022': [
        (31, [1, 2]),
        (32, [3, 4, 5]),
        (33, [5, 6, 7]),
        (34, [8, 9, 10]),
        (35, [11]),
    ],
    'junio2022ef': [
        (36, [1, 2]),
        (37, [3, 4]),
        (38, [5, 6, 7, 8]),
        (39, [9]),
    ],
    'junio2023': [
        (40, [1, 2, 3]),
        (41, [4, 5]),
        (42, [6, 7, 8, 9]),
        (43, [9]),
    ],
    'junio2023ef': [
        (44, [1, 2, 3]),
        (45, [4, 5]),
        (46, [6, 7]),
        (47, [8]),
        (48, [9]),
    ],
    'mayo2024': [
        (49, [1, 2]),
        (50, [3, 4]),
        (51, [5, 6]),
        (52, [7, 8]),
    ],
    'junio2024ef': [
        (53, [1, 2]),
        (54, [3, 4]),
        (55, [5, 6]),
        (56, [7, 8]),
    ],
    'mayo2025': [
        (57, [1, 2, 3]),
        (58, [4, 5]),
        (59, [6, 7, 8]),
        (60, [9]),
        (61, []),
    ],
    'junio2025ef': [
        (62, [1, 2]),
        (63, [2, 3]),
        (64, [3, 4, 5]),
        (65, [6, 7, 8]),
        (66, [9]),
    ],
}


def get_figure_rects(page):
    """
    Return list of fitz.Rect bounding boxes of figure regions on the page.
    Strategy: cluster drawing paths into groups, filter out header/footer,
    return bboxes of significant clusters.
    """
    page_rect = page.rect
    pw, ph = page_rect.width, page_rect.height

    # Margins to skip (header/footer)
    HEADER_Y = ph * 0.08   # top 8%
    FOOTER_Y = ph * 0.93   # bottom 7%
    LEFT_MARGIN = pw * 0.05
    RIGHT_MARGIN = pw * 0.98

    drawings = page.get_drawings()
    if not drawings:
        return []

    # Collect all path bboxes in content area
    pts = []
    for d in drawings:
        r = d['rect']
        if not r:
            continue
        # Filter out header/footer lines and thin horizontal rules
        if r.y0 < HEADER_Y or r.y1 > FOOTER_Y:
            continue
        if r.height < 2 and r.width > pw * 0.5:
            continue  # horizontal rule
        if r.x0 < LEFT_MARGIN or r.x1 > RIGHT_MARGIN:
            continue
        pts.append(r)

    if not pts:
        return []

    # Cluster rectangles that are close together (within 30pt vertically)
    CLUSTER_GAP = 30
    pts_sorted = sorted(pts, key=lambda r: r.y0)

    clusters = []
    current = [pts_sorted[0]]
    for r in pts_sorted[1:]:
        prev_y1 = max(p.y1 for p in current)
        if r.y0 - prev_y1 < CLUSTER_GAP:
            current.append(r)
        else:
            clusters.append(current)
            current = [r]
    clusters.append(current)

    # Convert clusters to bounding rectangles, filter by minimum size
    MIN_AREA = pw * ph * 0.005  # at least 0.5% of page area
    result = []
    for cluster in clusters:
        x0 = min(r.x0 for r in cluster)
        y0 = min(r.y0 for r in cluster)
        x1 = max(r.x1 for r in cluster)
        y1 = max(r.y1 for r in cluster)
        area = (x1 - x0) * (y1 - y0)
        if area > MIN_AREA:
            # Add padding
            PAD = 8
            rect = fitz.Rect(
                max(0, x0 - PAD),
                max(0, y0 - PAD),
                min(pw, x1 + PAD),
                min(ph, y1 + PAD)
            )
            result.append(rect)

    return result


def crop_page_region(page, rect, scale):
    """Render a specific rect of a page at given scale."""
    mat = fitz.Matrix(scale, scale)
    clip = rect
    pix = page.get_pixmap(matrix=mat, clip=clip, colorspace=fitz.csRGB)
    return pix


# Process each exam
for exam_name, pages_info in EXAM_PAGES.items():
    print(f'\n=== {exam_name} ===')
    for doc_page, ex_nums in pages_info:
        pdf_idx = doc_page - 1 + OFFSET
        if pdf_idx >= len(doc):
            continue

        page = doc[pdf_idx]
        pw, ph = page.rect.width, page.rect.height
        fig_rects = get_figure_rects(page)
        print(f'  p{doc_page} (exs {ex_nums}): {len(fig_rects)} figure regions')

        # Save each figure region
        for fi, rect in enumerate(fig_rects):
            pix = crop_page_region(page, rect, SCALE)
            fname = f'{exam_name}_p{doc_page}_fig{fi+1}.png'
            out_path = os.path.join(OUT, fname)
            pix.save(out_path)
            kb = os.path.getsize(out_path) // 1024
            print(f'    fig{fi+1}: ({rect.x0:.0f},{rect.y0:.0f})-({rect.x1:.0f},{rect.y1:.0f}) -> {fname} {kb}KB')

print('\nDone.')
