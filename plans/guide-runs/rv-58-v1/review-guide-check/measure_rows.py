"""Measure printed widths of strip rows, X Y Z rows and the 4-5 P7 card row on the final
student PDFs (1 mm = 72/25.4 pt). Reports wide filled/stroked rectangles per page."""
import sys, warnings
warnings.filterwarnings('ignore')
import fitz
base = sys.argv[1]
MM = 72 / 25.4
for name, pages in [('grades-2-3.pdf', [3, 5, 6]), ('grades-4-5.pdf', [2, 3, 4, 5]), ('k-1.pdf', [4])]:
    doc = fitz.open(f'{base}/{name}')
    for pno in pages:
        page = doc[pno - 1]
        rows = {}
        for d in page.get_drawings():
            r = d['rect']
            if r.height > 5 and r.width > 20:
                key = round(r.y0)
                rows.setdefault(key, []).append(r)
        out = []
        for y, rs in sorted(rows.items()):
            x0 = min(r.x0 for r in rs); x1 = max(r.x1 for r in rs)
            widths = sorted(set(round(r.width / MM, 1) for r in rs))
            out.append(f'y={y}: span {round((x1 - x0) / MM, 1)} mm, piece widths {widths}')
        print(name, 'page', pno)
        for o in out[:8]:
            print('   ', o)
