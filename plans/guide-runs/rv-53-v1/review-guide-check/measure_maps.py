"""Measure place-letter spacing and circle sizes on the working (large) maps of
the final student PDFs, to test the guide's '10 mm circles, centres ~40 mm apart'
claim. Usage: python3 -I measure_maps.py <pdf> ..."""
import sys, math, warnings
warnings.filterwarnings("ignore")
import fitz
MM = 25.4 / 72
for path in sys.argv[1:]:
    doc = fitz.open(path)
    print("==", path.split("/")[-1])
    for pno, page in enumerate(doc, 1):
        # place circles: drawings whose rect is roughly square with side 8-12 mm
        circ = []
        for d in page.get_drawings():
            r = d["rect"]
            w, h = r.width * MM, r.height * MM
            if 8.5 <= w <= 11.5 and abs(w - h) < 0.6:
                circ.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2, w))
        # dedupe
        uniq = []
        for c in circ:
            if all(math.hypot(c[0]-u[0], c[1]-u[1]) > 2 for u in uniq):
                uniq.append(c)
        if len(uniq) < 2:
            print(f"  p{pno}: no large place shapes found"); continue
        dmin = min(math.hypot(a[0]-b[0], a[1]-b[1]) * MM for i, a in enumerate(uniq) for b in uniq[i+1:])
        sizes = sorted({round(c[2], 1) for c in uniq})
        print(f"  p{pno}: {len(uniq)} large place shapes, sizes {sizes} mm, min centre distance {dmin:.1f} mm")
