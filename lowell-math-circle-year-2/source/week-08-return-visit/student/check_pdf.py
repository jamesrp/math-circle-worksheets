"""Optional final-PDF geometry checks and page renders; requires PyMuPDF."""
from pathlib import Path
import json
import math
import sys
import tempfile
import pymupdf
from check_math import NIM, COINS, ROOKS, COIN_EXAMPLE, ROOK_EXAMPLE

ROOT = Path(__file__).resolve().parent.parent
if len(sys.argv) < 2:
    raise SystemExit("Usage: python check_pdf.py PDF [QA_OUTPUT_DIR]; requires PyMuPDF")
PDF = Path(sys.argv[1]).resolve()
QA = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path(tempfile.mkdtemp(prefix="return-visit-pdf-qa-"))
QA.mkdir(parents=True, exist_ok=True)
TOL = 0.06  # PDF points; allows TeX coordinate rounding, not a size change.


def point(x, y):
    return (72*x, 72*y)


def circles(page):
    return [((d["rect"].x0+d["rect"].x1)/2,
             (d["rect"].y0+d["rect"].y1)/2)
            for d in page.get_drawings()
            if d["fill"] is not None
            and tuple(item[0] for item in d["items"]) == ("c",)*4]


def same_centers(actual, expected):
    assert len(actual) == len(expected), (len(actual), len(expected))
    remaining = list(actual)
    for center in expected:
        nearest = min(remaining, key=lambda p: math.dist(p, center))
        assert math.dist(nearest, center) < TOL, (nearest, center)
        remaining.remove(nearest)


def lines(page):
    return [(tuple(item[1]), tuple(item[2]))
            for d in page.get_drawings() for item in d["items"]
            if item[0] == "l"]


def matches_line(actual, a, b):
    return ((math.dist(actual[0],a) < TOL and math.dist(actual[1],b) < TOL)
            or (math.dist(actual[0],b) < TOL and math.dist(actual[1],a) < TOL))


def check_grid(page, x, y, cell, side):
    segments = lines(page)
    for i in range(side+1):
        a,b = point(x+i*cell,y), point(x+i*cell,y+side*cell)
        assert sum(matches_line(s,a,b) for s in segments) == 1
        a,b = point(x,y+i*cell), point(x+side*cell,y+i*cell)
        assert sum(matches_line(s,a,b) for s in segments) == 1


def check_row(page, x, y, cell):
    segments = lines(page)
    for i in range(13):
        a,b = point(x+i*cell,y), point(x+i*cell,y+cell)
        # The left wall is an additional heavy line at the first boundary.
        assert sum(matches_line(s,a,b) for s in segments) == (2 if i == 0 else 1)
    for yy in (y,y+cell):
        assert sum(matches_line(s,point(x,yy),point(x+12*cell,yy)) for s in segments) == 1
    words = [w for w in page.get_text("words")
             if w[4].isdigit() and x*72-TOL <= (w[0]+w[2])/2 <= (x+12*cell)*72+TOL
             and (y+cell+.01)*72 < (w[1]+w[3])/2 < (y+cell+.2)*72]
    assert len(words) == 12, (x,y,len(words))
    for i,w in enumerate(sorted(words,key=lambda w:w[0]),1):
        assert w[4] == str(i)
        assert abs((w[0]+w[2])/2 - (x+(i-.5)*cell)*72) < TOL


def coin_centers(x,y,cell,state):
    return [point(x+(i-.5)*cell,y+.5*cell) for i in state]


def rook_centers(x,y,cell,state):
    return [point(x+(state[0]+.5)*cell,y+(3.5-state[1])*cell),
            point(x+4*cell+.16+(state[2]+.5)*cell,y+(3.5-state[3])*cell)]


def main():
    doc = pymupdf.open(PDF)
    assert len(doc) == 5
    outside = []
    for n,page in enumerate(doc,1):
        assert page.rect == pymupdf.Rect(0,0,792,612)
        assert "F08-RV-v1" in page.get_text()
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines",[]):
                for span in line.get("spans",[]):
                    if not page.rect.contains(pymupdf.Rect(span["bbox"])):
                        outside.append([n,span["text"],span["bbox"]])
    assert not outside, outside
    expected=[]
    for i,state in enumerate(NIM):
        x,y = .55+2.6*(i%4), 2.18+1.19*(i//4)
        for p,amount in enumerate(state):
            expected.extend(point(x+.36+.48*p,y+.23+.13*n) for n in range(amount))
    same_centers(circles(doc[0]), expected)
    assert len(expected) == 50
    assert "with at" in doc[0].get_text() and "least one counter" in doc[0].get_text()
    assert "Rule:" in doc[0].get_text()
    for p in (1,2):
        expected=[]
        if p == 1:
            for x,state in zip((.4,4.1,7.8),COIN_EXAMPLE):
                expected.extend(coin_centers(x,1.91,.23,state))
                check_row(doc[p],x,1.91,.23)
            starts=COINS[:6]
            top,step=3.24,.84
        else:
            starts=COINS[6:]
            top,step=1.66,.93
        for i,state in enumerate(starts):
            x,y=(.55 if i%2==0 else 5.85),top+step*(i//2)+.23
            expected.extend(coin_centers(x,y,.23,state))
            check_row(doc[p],x,y,.23)
        same_centers(circles(doc[p]),expected)
        check_row(doc[p],.4,6.25,.85)
    expected=[]
    for x,state in zip((.6,4.05,7.5),ROOK_EXAMPLE):
        expected.extend(rook_centers(x,1.98,.18,state))
        check_grid(doc[3],x,1.98,.18,4)
        check_grid(doc[3],x+.88,1.98,.18,4)
    same_centers(circles(doc[3]),expected)
    for x in (.85,6.2):
        check_grid(doc[3],x,4.08,.85,4)
    expected=[]
    for i,state in enumerate(ROOKS):
        x,y=.55+3.45*(i%3),1.45+2.45*(i//3)+.38
        expected.extend(rook_centers(x,y,.31,state))
        check_grid(doc[4],x,y,.31,4)
        check_grid(doc[4],x+1.40,y,.31,4)
    same_centers(circles(doc[4]),expected)
    for x in (3.9,5.18):
        check_grid(doc[4],x,6.42,.28,4)
    render=QA/"render"
    render.mkdir(exist_ok=True)
    for n,page in enumerate(doc,1):
        page.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5),alpha=False).save(render/f"page-{n:02d}.png")
    report={"pdf":str(PDF),"pages":5,"page_size_pt":[792,612],
            "all_catalog_and_example_tokens_checked":True,
            "circles_per_page":[len(circles(page)) for page in doc],
            "all_coin_rows": "12 squares, 13 distinct boundaries; labels 1..12 centered",
            "active_coin_cells_in":[.85,.85],"active_coin_strip_in":[10.2,.85],
            "all_rook_grids":"4x4; all 22 grids individually checked",
            "active_rook_cells_in":[.85,.85],"active_rook_boards_in":[3.4,3.4],
            "outside_text":outside,"physical_rehearsal":"untested"}
    (QA/"build").mkdir(exist_ok=True)
    (QA/"build"/"layout-check.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__ == "__main__":
    main()
