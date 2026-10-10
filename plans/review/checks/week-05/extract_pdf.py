"""Read every grid, edge number, card and tower picture from the final Week 5 PDFs.

Vector data only (pdfplumber): grid frames are the thick rectangles, n comes from the
inner lines, edge numbers are the digits beside a grid aligned with a row or column.
Writes pdf_data.json next to this script and prints a readable dump.

Run:  python3 -I extract_pdf.py
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import PDF  # noqa: E402
import pdfplumber  # noqa: E402

OUT = Path(__file__).resolve().parent / "pdf_data.json"
PT_PER_IN = 72.0


def grids_on_page(page, frame_min_lw, small_ok=True):
    """Square frames with inner grid lines.  Returns dicts with bbox, n, cell size."""
    frames = []
    for r in page.rects:
        w, h = r["x1"] - r["x0"], r["bottom"] - r["top"]
        if r["linewidth"] < frame_min_lw or w < 20 or abs(w - h) > 0.5:
            continue
        x0, y0, x1, y1 = r["x0"], r["top"], r["x1"], r["bottom"]
        vx = sorted({round(l["x0"], 1) for l in page.lines
                     if abs(l["x0"] - l["x1"]) < 0.1 and x0 + 1 < l["x0"] < x1 - 1
                     and abs(l["top"] - y0) < 1 and abs(l["bottom"] - y1) < 1})
        hy = sorted({round(l["top"], 1) for l in page.lines
                     if abs(l["top"] - l["bottom"]) < 0.1 and y0 + 1 < l["top"] < y1 - 1
                     and abs(l["x0"] - x0) < 1 and abs(l["x1"] - x1) < 1})
        n = len(vx) + 1
        if n < 2 or len(hy) + 1 != n:
            continue
        cell = w / n
        # equal spacing check
        xs = [x0, *vx, x1]
        ys = [y0, *hy, y1]
        spread = max(abs((xs[i + 1] - xs[i]) - cell) for i in range(n)) + \
            max(abs((ys[i + 1] - ys[i]) - cell) for i in range(n))
        frames.append({"x0": x0, "y0": y0, "x1": x1, "y1": y1, "n": n, "cell": cell,
                       "cell_in": cell / PT_PER_IN, "cell_cm": cell / PT_PER_IN * 2.54,
                       "spacing_err_pt": round(spread, 3)})
    frames.sort(key=lambda g: (round(g["y0"] / 20), g["x0"]))
    return frames


def digit_chars(page, ymin=50, ymax=745):
    out = []
    for c in page.chars:
        if c["text"].isdigit() and ymin < c["top"] < ymax:
            out.append({"t": c["text"], "x": (c["x0"] + c["x1"]) / 2, "y": (c["top"] + c["bottom"]) / 2,
                        "size": round(c["size"], 2), "grey": c.get("non_stroking_color") not in [(0.0,), (0,), [0], None, (0, 0, 0)],
                        "col": c.get("non_stroking_color")})
    return out


def merge_adjacent_digits(chars):
    """Join digits that touch horizontally (multi-digit numbers)."""
    chars = sorted(chars, key=lambda c: (round(c["y"]), c["x"]))
    out = []
    for c in chars:
        if out and abs(out[-1]["y"] - c["y"]) < 1 and 0 < c["x"] - out[-1]["x"] < c["size"] * 0.62:
            out[-1]["t"] += c["t"]
            out[-1]["x"] = (out[-1]["x"] + c["x"]) / 2
        else:
            out.append(dict(c))
    return out


def assign(grids, chars, margin_cells=1.0):
    """Give each digit to a grid as a cell entry or an edge number."""
    for g in grids:
        g["cells"] = [[None] * g["n"] for _ in range(g["n"])]
        g["clues"] = {}
    leftover = []
    for ch in chars:
        best = None
        for gi, g in enumerate(grids):
            x, y, n, cell = ch["x"], ch["y"], g["n"], g["cell"]
            m = max(margin_cells * cell, 14)
            inside_x = g["x0"] < x < g["x1"]
            inside_y = g["y0"] < y < g["y1"]
            if inside_x and inside_y:
                cand = (0, gi, "cell", (int((y - g["y0"]) // cell), int((x - g["x0"]) // cell)))
            elif inside_x and g["y0"] - m < y < g["y0"]:
                cand = (g["y0"] - y, gi, "T", int((x - g["x0"]) // cell) + 1)
            elif inside_x and g["y1"] < y < g["y1"] + m:
                cand = (y - g["y1"], gi, "B", int((x - g["x0"]) // cell) + 1)
            elif inside_y and g["x0"] - m < x < g["x0"]:
                cand = (g["x0"] - x, gi, "L", int((y - g["y0"]) // cell) + 1)
            elif inside_y and g["x1"] < x < g["x1"] + m:
                cand = (x - g["x1"], gi, "R", int((y - g["y0"]) // cell) + 1)
            else:
                continue
            if best is None or cand[0] < best[0]:
                best = cand
        if best is None:
            leftover.append(ch)
            continue
        _, gi, kind, where = best
        g = grids[gi]
        if kind == "cell":
            r, c = where
            g["cells"][r][c] = int(ch["t"])
        else:
            key = f"{kind}{where}"
            if key in g["clues"]:
                raise SystemExit(f"two digits at {key}")
            g["clues"][key] = int(ch["t"])
    return leftover


def clue_boxes(page, g):
    """Small grey squares round a blank grid (answer boxes for edge numbers)."""
    cnt = 0
    for r in page.rects:
        w, h = r["x1"] - r["x0"], r["bottom"] - r["top"]
        if r["linewidth"] < 1 and abs(w - h) < 0.5 and 10 < w < 30:
            cx, cy = (r["x0"] + r["x1"]) / 2, (r["top"] + r["bottom"]) / 2
            near = (g["x0"] - 40 < cx < g["x1"] + 40) and (g["y0"] - 40 < cy < g["y1"] + 40)
            inside = g["x0"] < cx < g["x1"] and g["y0"] < cy < g["y1"]
            if near and not inside:
                cnt += 1
    return cnt


def cards(page, ymin=60, ymax=740):
    """Number pairs on cards: digits grouped by row and by page half, left/right."""
    ds = [d for d in digit_chars(page, ymin, ymax)]
    groups = defaultdict(list)
    for d in ds:
        groups[(round(d["y"] / 6), d["x"] > 306)].append(d)
    out = []
    for key in sorted(groups, key=lambda k: (k[0], k[1])):
        g = sorted(groups[key], key=lambda d: d["x"])
        out.append([int(d["t"]) for d in g])
    return out


def tower_pictures(page):
    """Cube rectangles (filled, light colour) grouped into towers and pictures."""
    cubes = [r for r in page.rects if r.get("fill") and r.get("non_stroking_color")
             and len(r["non_stroking_color"]) == 3 and r["x1"] - r["x0"] > 15]
    by_base = defaultdict(list)
    for r in cubes:
        by_base[round(r["y1"] if "y1" in r else r["bottom"])].append(r)
    pics = []
    # group by the picture's ground line: towers in one picture share a bottom
    bottoms = defaultdict(list)
    for r in cubes:
        bottoms[round(r["bottom"] / 4)].append(r)
    cols = defaultdict(list)
    for r in cubes:
        cols[(round(r["x0"]), )].append(r)
    # assign each cube to the column of its x0; a tower's base is its lowest cube
    towers = []
    for (x0,), rs in cols.items():
        rs.sort(key=lambda r: r["top"])
        # split stacks separated vertically (different pictures)
        stack = [rs[0]]
        for r in rs[1:]:
            if abs(r["top"] - stack[-1]["bottom"]) < 1:
                stack.append(r)
            else:
                towers.append(stack)
                stack = [r]
        towers.append(stack)
    for t in towers:
        pics.append({"x0": round(t[0]["x0"], 1), "base": round(t[-1]["bottom"], 1), "h": len(t),
                     "dashed": bool(t[0].get("dash"))})
    # group towers into pictures by base and proximity
    pics.sort(key=lambda t: (t["base"], t["x0"]))
    grouped = []
    for t in pics:
        if grouped and abs(grouped[-1][-1]["base"] - t["base"]) < 2 and t["x0"] - grouped[-1][-1]["x0"] < 60:
            grouped[-1].append(t)
        else:
            grouped.append([t])
    return [[t["h"] for t in g] for g in grouped]


def blank_frames(page, kind):
    """Count answer frames: 'tower3'/'tower4' = empty tower frames (columns of
    unfilled squares), 'row3'/'row4' = strips of squares, 'grid' handled elsewhere."""
    sq = [r for r in page.rects if not r.get("fill") and abs((r["x1"] - r["x0"]) - (r["bottom"] - r["top"])) < 0.6
          and 15 < r["x1"] - r["x0"] < 40 and r["linewidth"] < 1.0]
    return len(sq)


def main():
    data = {"student": {}, "guide": {}}
    for band in "KMU":
        pdf = pdfplumber.open(PDF[band])
        pages = {}
        for pi, page in enumerate(pdf.pages, 1):
            gr = grids_on_page(page, 1.2)
            chars = merge_adjacent_digits(digit_chars(page, 95, 745))
            left = assign(gr, chars) if gr else chars
            for g in gr:
                g["boxes"] = clue_boxes(page, g)
                g.pop("cells") if all(v is None for row in g["cells"] for v in row) else None
            info = {"grids": gr}
            info["cards"] = cards(page, 95, 745)
            info["towers"] = tower_pictures(page)
            info["open_squares"] = blank_frames(page, None)
            info["text"] = page.extract_text().split("\n")[1][:60] if page.extract_text() else ""
            pages[pi] = info
        data["student"][band] = pages
    pdf = pdfplumber.open(PDF["G"])
    for pi, page in enumerate(pdf.pages, 1):
        gr = grids_on_page(page, 0.9)
        if not gr:
            continue
        chars = merge_adjacent_digits(digit_chars(page, 45, 760))
        assign(gr, chars, margin_cells=0.95)
        data["guide"][pi] = gr
    OUT.write_text(json.dumps(data, indent=1))

    for band, pages in data["student"].items():
        for pi, info in pages.items():
            print(f"== {band} p.{pi}: {info['text']}")
            for g in info["grids"]:
                print(f"   grid n={g['n']} cell={g['cell_in']:.3f} in ({g['cell_cm']:.2f} cm) at ({g['x0']:.0f},{g['y0']:.0f}) "
                      f"spacing err {g['spacing_err_pt']} pt; boxes {g['boxes']}; clues {g['clues']}")
            if info["towers"]:
                print("   tower pictures (heights left to right):", info["towers"])
            print("   digit groups (cards/labels):", info["cards"])
            print("   open squares:", info["open_squares"])
    for pi, gr in data["guide"].items():
        print(f"== guide p.{pi}: {len(gr)} grids")
        for g in gr:
            cells = "/".join("".join(str(v) if v else "." for v in row) for row in g["cells"])
            print(f"   n={g['n']} at ({g['x0']:.0f},{g['y0']:.0f}) cells {cells} clues {g['clues']}")


if __name__ == "__main__":
    main()
