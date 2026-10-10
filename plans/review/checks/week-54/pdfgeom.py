#!/usr/bin/env python3
"""Standard-library reader for the pdfTeX/TikZ PDFs of Week 54.

It reads every page's content stream and returns, in PDF points (origin at the
bottom-left of the page):
  rects : rectangles drawn with `re`, with the paint operator and fill gray
  texts : text runs (font size, position, decoded string)
  lines : stroked straight segments (m/l pairs)
Only the operators this packet uses are interpreted (q/Q, cm, re, m, l, g/G,
w, f/B/S/n, BT/ET, Tf, Td, TJ/Tj).
"""
import re
import zlib
from pathlib import Path


def find_repo():
    """Walk up from this file to the folder that holds the packet."""
    here = Path(__file__).resolve().parent
    for p in [here, *here.parents]:
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    raise SystemExit("repository not found above " + str(here))


def _objects(data):
    objs = {}
    for n, body in re.findall(rb"(\d+) 0 obj(.*?)endobj", data, re.S):
        objs[int(n)] = body
    # unpack object streams
    for n, body in list(objs.items()):
        if b"/ObjStm" in body:
            first = int(re.search(rb"/First (\d+)", body).group(1))
            raw = _stream(body)
            header = raw[:first].split()
            for i in range(0, len(header), 2):
                on, off = int(header[i]), int(header[i + 1])
                nxt = int(header[i + 3]) if i + 3 < len(header) else len(raw) - first
                objs.setdefault(on, raw[first + off:first + nxt])
    return objs


def _stream(body):
    m = re.search(rb"stream\r?\n(.*?)\r?\nendstream", body, re.S)
    return zlib.decompress(m.group(1))


def page_streams(path):
    data = Path(path).read_bytes()
    objs = _objects(data)
    root = int(re.search(rb"/Root (\d+) 0 R", data).group(1))
    pages = int(re.search(rb"/Pages (\d+) 0 R", objs[root]).group(1))

    def walk(n):
        body = objs[n]
        if re.search(rb"/Type\s*/Pages", body):
            kids = re.search(rb"/Kids\s*\[(.*?)\]", body, re.S).group(1)
            out = []
            for k in re.findall(rb"(\d+) 0 R", kids):
                out += walk(int(k))
            return out
        c = re.search(rb"/Contents (\d+) 0 R", body)
        return [_stream(objs[int(c.group(1))]).decode("latin1")]
    return walk(pages)


_tok = re.compile(r"\[(?:[^\]\\]|\\.)*\]|\((?:[^)\\]|\\.)*\)|/[^\s/\[\]()]+|[^\s\[\]()/]+")


def _mul(a, b):
    # matrices as (a,b,c,d,e,f) in PDF convention: x' = a x + c y + e
    a1, b1, c1, d1, e1, f1 = a
    a2, b2, c2, d2, e2, f2 = b
    return (a1 * a2 + b1 * c2, a1 * b2 + b1 * d2,
            c1 * a2 + d1 * c2, c1 * b2 + d1 * d2,
            e1 * a2 + f1 * c2 + e2, e1 * b2 + f1 * d2 + f2)


def _apply(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


def _decode_tj(arr):
    s = ""
    for part in re.findall(r"\((?:[^)\\]|\\.)*\)|-?[\d.]+", arr):
        if part.startswith("("):
            t = part[1:-1]
            t = re.sub(r"\\(\d{3})", lambda m: chr(int(m.group(1), 8)), t)
            t = t.replace("\\(", "(").replace("\\)", ")").replace("\\\\", "\\")
            s += t
        else:
            if float(part) < -200:
                s += " "
    return s


def interpret(stream):
    ctm = (1, 0, 0, 1, 0, 0)
    fill = 0.0
    stack = []
    subpaths = []      # list of point lists for the current path
    rects, texts, lines, polys = [], [], [], []
    args = []
    tm = None
    fsize = None
    for tok in _tok.findall(stream):
        if tok[0] in "[(/" or re.fullmatch(r"-?[\d.]+", tok):
            args.append(tok)
            continue
        op = tok
        if op == "q":
            stack.append((ctm, fill))
        elif op == "Q":
            ctm, fill = stack.pop()
        elif op == "cm":
            m = tuple(float(v) for v in args[-6:])
            ctm = _mul(m, ctm)
        elif op == "g":
            fill = float(args[-1])
        elif op == "re":
            x, y, w, h = (float(v) for v in args[-4:])
            pts = [_apply(ctm, x, y), _apply(ctm, x + w, y), _apply(ctm, x + w, y + h),
                   _apply(ctm, x, y + h)]
            subpaths.append(pts + [pts[0]])
        elif op == "m":
            subpaths.append([_apply(ctm, float(args[-2]), float(args[-1]))])
        elif op == "l":
            subpaths[-1].append(_apply(ctm, float(args[-2]), float(args[-1])))
        elif op == "h":
            if subpaths and subpaths[-1]:
                subpaths[-1].append(subpaths[-1][0])
        elif op in ("f", "f*", "B", "B*", "S", "s", "b", "n"):
            for sp in subpaths:
                if len(sp) < 2:
                    continue
                polys.append({"pts": sp, "op": op, "fill": fill})
                xs = sorted(set(round(x, 2) for x, _ in sp))
                ys = sorted(set(round(y, 2) for _, y in sp))
                if len(sp) == 5 and len(xs) == 2 and len(ys) == 2:
                    rects.append({"x": xs[0], "y": ys[0], "w": xs[1] - xs[0],
                                  "h": ys[1] - ys[0], "op": op, "fill": fill})
                elif op in ("S", "s", "B", "b"):
                    for a, b in zip(sp, sp[1:]):
                        if a != b:
                            lines.append((a, b))
            subpaths = []
        elif op == "BT":
            tm = (1, 0, 0, 1, 0, 0)
        elif op == "Tf":
            fsize = float(args[-1])
        elif op == "Td":
            tm = _mul((1, 0, 0, 1, float(args[-2]), float(args[-1])), tm)
        elif op in ("TJ", "Tj"):
            s = _decode_tj(args[-1]) if op == "TJ" else _decode_tj("[" + args[-1] + "]")
            pos = _apply(_mul(tm, ctm), 0, 0)
            texts.append({"x": pos[0], "y": pos[1], "size": fsize, "s": s})
        args = []
    return rects, texts, lines


def read_pdf(path):
    return [interpret(s) for s in page_streams(path)]


if __name__ == "__main__":
    repo = find_repo()
    pages = read_pdf(repo / "lowell-math-circle-year-2/week-54/week-54-students.pdf")
    for i, (r, t, l) in enumerate(pages, 1):
        print(i, len(r), "rects", len(t), "texts", len(l), "segments")
