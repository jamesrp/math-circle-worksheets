"""Measure week-08-materials.pdf: page size, board squares and the scale line.

Run:  python3 check_materials.py ../materials.pdf
Needs PyMuPDF (`pip install pymupdf`); without it the check is skipped, since the
build itself needs only XeLaTeX.  Reads the vector drawing, not a render.

For each sheet it checks that the page is US Letter, that the board's grid
lines are 72 pt (1 inch) apart in both directions with the expected number of
rows and columns, that the whole board lies on the page with at least 0.24 inch
to spare, that a star outline sits in the bottom-left square on the sheets that
should have one, and that the scale line is 10 cm long (283.46 pt).
"""
import sys

try:
    import pymupdf
except ImportError:  # pragma: no cover
    try:
        import fitz as pymupdf
    except ImportError:
        print("check_materials: PyMuPDF not installed; skipped")
        sys.exit(0)

INCH = 72.0
TOL = 0.05                     # points
TEN_CM = 72.0 / 2.54 * 10      # 283.4646 pt
# (columns, rows, star in bottom-left square)
EXPECTED = [(8, 8, True), (5, 5, True), (4, 8, True), (4, 8, False)]


def segments(page):
    """Every straight line segment drawn on the page, as (x0, y0, x1, y1, width)."""
    out = []
    for d in page.get_drawings():
        w = d.get("width") or 0
        for item in d["items"]:
            if item[0] == "l":
                p, q = item[1], item[2]
                out.append((p.x, p.y, q.x, q.y, w))
            elif item[0] == "re":
                r = item[1]
                out += [(r.x0, r.y0, r.x1, r.y0, w), (r.x1, r.y0, r.x1, r.y1, w),
                        (r.x1, r.y1, r.x0, r.y1, w), (r.x0, r.y1, r.x0, r.y0, w)]
    return out


def distinct(values):
    vals = sorted(values)
    groups = []
    for v in vals:
        if groups and abs(v - groups[-1][-1]) < 0.5:
            groups[-1].append(v)
        else:
            groups.append([v])
    return [sum(g) / len(g) for g in groups]


def check_page(page, cols, rows, star):
    errors = []
    if abs(page.rect.width - 612) > 0.01 or abs(page.rect.height - 792) > 0.01:
        errors.append(f"page is {page.rect.width} x {page.rect.height}, not Letter")
    segs = segments(page)
    # board lines: grid (0.9 pt) and frame (1.4 pt), horizontal or vertical, at least 1 inch long
    board = [s for s in segs if s[4] in (0.9, 1.4) or abs(s[4] - 0.9) < 0.01 or abs(s[4] - 1.4) < 0.01]
    vert = [s for s in board if abs(s[0] - s[2]) < 0.01 and abs(s[1] - s[3]) >= INCH - TOL]
    horiz = [s for s in board if abs(s[1] - s[3]) < 0.01 and abs(s[0] - s[2]) >= INCH - TOL]
    xs = distinct([s[0] for s in vert])
    ys = distinct([s[1] for s in horiz])
    if len(xs) != cols + 1 or len(ys) != rows + 1:
        errors.append(f"found {len(xs) - 1} columns and {len(ys) - 1} rows, expected {cols} and {rows}")
        return errors, None
    gaps = [b - a for a, b in zip(xs, xs[1:])] + [b - a for a, b in zip(ys, ys[1:])]
    worst = max(abs(g - INCH) for g in gaps)
    if worst > TOL:
        errors.append(f"a square side differs from 1 inch by {worst:.3f} pt")
    width, height = xs[-1] - xs[0], ys[-1] - ys[0]
    margin = min(xs[0], 612 - xs[-1], ys[0], 792 - ys[-1]) / INCH
    if margin < 0.24:
        errors.append(f"board comes within {margin:.3f} in of the page edge")
    # the star: a closed outline inside the bottom-left square (PDF y grows downward)
    if star:
        sq = pymupdf.Rect(xs[0], ys[-2], xs[1], ys[-1])
        stars = [d for d in page.get_drawings()
                 if len(d["items"]) >= 9 and sq.contains(d["rect"]) and d["rect"].width > 0.4 * INCH]
        if not stars:
            errors.append("no star outline in the bottom-left square")
    # the scale line: the longest horizontal 1 pt line below the board
    scale = [s for s in segs if abs(s[1] - s[3]) < 0.01 and s[1] > ys[-1] and abs(s[4] - 1.0) < 0.01]
    if not scale:
        errors.append("no scale line below the board")
        length = None
    else:
        length = max(abs(s[2] - s[0]) for s in scale)
        if abs(length - TEN_CM) > TOL:
            errors.append(f"scale line is {length:.3f} pt, not 10 cm ({TEN_CM:.3f} pt)")
    summary = (f"{cols}x{rows} board {width / INCH:.4f} x {height / INCH:.4f} in, square sides "
               f"{min(gaps) / INCH:.4f}-{max(gaps) / INCH:.4f} in, {margin:.3f} in to the nearest edge, "
               f"scale line {length / 72 * 2.54:.4f} cm" if length else "")
    return errors, summary


def main(path):
    doc = pymupdf.open(path)
    errors = []
    if len(doc) != len(EXPECTED):
        errors.append(f"{len(doc)} pages, expected {len(EXPECTED)}")
    for i, (page, (cols, rows, star)) in enumerate(zip(doc, EXPECTED), 1):
        errs, summary = check_page(page, cols, rows, star)
        print(f"sheet {i}: " + (summary or "") + ("" if not errs else "  PROBLEMS: " + "; ".join(errs)))
        errors += [f"sheet {i}: {e}" for e in errs]
    if errors:
        print(f"{len(errors)} problem(s)")
        sys.exit(1)
    print("all sheets measure correctly")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "../materials.pdf")
