import fitz
import os

# Get PDF path dynamically to handle special chars in filename
FOLDER = r'C:\Users\Usuario\Desktop\Antigravity\upv-ehu-project\fluidos\EXAMENES PDF'
PDF = os.path.join(FOLDER, os.listdir(FOLDER)[0])
OUT = r'C:\Users\Usuario\Desktop\Antigravity\upv-ehu-project\fluidos\examenes\img'
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
print(f'Total pages: {len(doc)}')

# Find offset: scan for junio2022 exam header
offset = 5  # default
for i, page in enumerate(doc):
    t = page.get_text()
    if '2 de Junio de 2022' in t and 'EXAMEN FINAL' in t:
        offset = i - 30  # doc page 31 = this PDF index i
        print(f'junio2022 found at PDF index {i}, offset={offset}')
        break

# Exam page ranges (document page numbers, 1-based, inclusive)
exams = {
    'junio2022':   (31, 35),
    'junio2022ef': (36, 39),
    'junio2023':   (40, 43),
    'junio2023ef': (44, 48),
    'mayo2024':    (49, 52),
    'junio2024ef': (53, 56),
    'mayo2025':    (57, 61),
    'junio2025ef': (62, 66),
}

DPI = 180
MAT = fitz.Matrix(DPI/72, DPI/72)

for exam_name, (doc_start, doc_end) in exams.items():
    print(f'\n{exam_name} (doc pp {doc_start}-{doc_end}):')
    for doc_page in range(doc_start, doc_end + 1):
        pdf_idx = doc_page - 1 + offset
        if pdf_idx >= len(doc):
            print(f'  p{doc_page}: out of range')
            continue
        page = doc[pdf_idx]
        pix = page.get_pixmap(matrix=MAT, colorspace=fitz.csRGB)
        out_file = os.path.join(OUT, f'{exam_name}_p{doc_page}.png')
        pix.save(out_file)
        kb = os.path.getsize(out_file) // 1024
        print(f'  Saved {exam_name}_p{doc_page}.png ({kb} KB)')

print('\nAll done.')
