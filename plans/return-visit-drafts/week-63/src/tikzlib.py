"""TikZ drawing helpers for the Week 63 return-visit pages.

All coordinates are in millimetres (tikzpicture uses x=1mm, y=1mm).
Card pictures follow the kit (W63-M-v3): A circle, B triangle, C square,
D diamond, E star.
"""
import math

PICS = "ABCDE"
FILL = "gray!30"


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def pic(L, cx, cy, s, fill=FILL, draw="black", lw="0.5pt"):
    """Picture of card L centred at (cx, cy), about s mm across."""
    st = f"[fill={fill}, draw={draw}, line width={lw}]"
    if L == "A":
        return f"\\path{st} ({f(cx)},{f(cy)}) circle ({f(s*0.45)});\n"
    if L == "B":
        a = s * 0.98
        h = a * math.sqrt(3) / 2
        return (f"\\path{st} ({f(cx)},{f(cy+h/2)}) -- ({f(cx-a/2)},{f(cy-h/2)}) -- "
                f"({f(cx+a/2)},{f(cy-h/2)}) -- cycle;\n")
    if L == "C":
        a = s * 0.78
        return f"\\path{st} ({f(cx-a/2)},{f(cy-a/2)}) rectangle ({f(cx+a/2)},{f(cy+a/2)});\n"
    if L == "D":
        r = s * 0.52
        return (f"\\path{st} ({f(cx)},{f(cy+r)}) -- ({f(cx+r)},{f(cy)}) -- "
                f"({f(cx)},{f(cy-r)}) -- ({f(cx-r)},{f(cy)}) -- cycle;\n")
    if L == "E":
        R = s * 0.52
        r = R * 0.40
        pts = []
        for k in range(10):
            ang = math.radians(90 + 36 * k)
            rad = R if k % 2 == 0 else r
            pts.append(f"({f(cx+rad*math.cos(ang))},{f(cy+rad*math.sin(ang)-R*0.08)})")
        return f"\\path{st} " + " -- ".join(pts) + " -- cycle;\n"
    return ""


def font(pt, bold=True):
    b = "\\bfseries" if bold else ""
    return f"\\fontsize{{{pt}}}{{{pt*1.2:.1f}}}\\selectfont{b}"


def label_pair(L, cx, cy, pt, s, gap=0.8, bold=True):
    """Letter with its picture to the right, centred at (cx, cy)."""
    if L in PICS:
        lw = pt * 0.25  # approx letter width in mm
        tot = lw + gap + s
        lx = cx - tot / 2 + lw / 2
        px = cx + tot / 2 - s / 2
        return (f"\\node[inner sep=0, font={font(pt, bold)}] at ({f(lx)},{f(cy)}) {{{L}}};\n"
                + pic(L, px, cy, s))
    return f"\\node[inner sep=0, font={font(pt, bold)}] at ({f(cx)},{f(cy)}) {{{L}}};\n"


def row(x0, y0, cards, homes=None, w=10, h=10, lab_pt=7, lab_s=2.6, card_pt=11,
        card_s=4.2, blank=False, bold=(), labels=True, lab_gap=3.2):
    """Outcome-card style row: home labels above, cells holding cards.

    (x0, y0) is the lower-left corner of the first cell.
    """
    homes = homes or "ABCDE"[:len(cards)]
    out = ""
    for i, hm in enumerate(homes):
        x = x0 + i * w
        lw = "1.6pt" if i in bold else "0.6pt"
        out += f"\\draw[line width={lw}] ({f(x)},{f(y0)}) rectangle ({f(x+w)},{f(y0+h)});\n"
        if labels:
            out += label_pair(hm, x + w / 2, y0 + h + lab_gap, lab_pt, lab_s, bold=False)
        if not blank:
            out += label_pair(cards[i], x + w / 2, y0 + h / 2, card_pt, card_s)
    return out


def minicard(L, cx, cy, w=9, h=11, cross=True, light=False, pt=8):
    """Small card (letter above picture) centred at (cx, cy), optionally crossed out.

    The cross is drawn under the letter and picture so both stay readable.
    """
    col = "black!62" if light else "black"
    fill = "gray!22" if light else FILL
    out = f"\\draw[line width=0.5pt, draw={col}, fill=white] ({f(cx-w/2)},{f(cy-h/2)}) rectangle ({f(cx+w/2)},{f(cy+h/2)});\n"
    if cross:
        out += (f"\\draw[line width=1.3pt, draw=black!75, line cap=round] ({f(cx-w/2)},{f(cy-h/2)}) -- "
                f"({f(cx+w/2)},{f(cy+h/2)});\n")
        out += (f"\\draw[line width=1.3pt, draw=black!75, line cap=round] ({f(cx-w/2)},{f(cy+h/2)}) -- "
                f"({f(cx+w/2)},{f(cy-h/2)});\n")
    out += (f"\\node[inner sep=0.5pt, fill=white, text={col}, font={font(pt)}] at "
            f"({f(cx)},{f(cy+h*0.22)}) {{{L}}};\n")
    out += pic(L, cx, cy - h * 0.22, min(w, h) * 0.40, fill=fill, draw=col)
    return out


def board(x0, y0, homes, refused, W=35, H=45, actual=True, mc_w=10, mc_h=12.5,
          lab_pt=12, lab_s=3.6, menu=False, mc_pt=10, gap=1.8):
    """Row of homes with crossed-out cards above each home.

    actual=True draws 35 x 45 mm homes; the home label sits in the top 5 mm band.
    refused: dict home -> string of refused cards.
    menu=True draws all cards lightly above each home (for children to cross).
    """
    out = ""
    for i, hm in enumerate(homes):
        x = x0 + i * W
        out += f"\\draw[line width=0.7pt] ({f(x)},{f(y0)}) rectangle ({f(x+W)},{f(y0+H)});\n"
        ly = y0 + H - 2.5 if actual else y0 + H / 2
        out += label_pair(hm, x + W / 2, ly, lab_pt, lab_s, bold=True)
        cards = homes if menu else refused.get(hm, "")
        n = len(cards)
        if n:
            tot = n * mc_w + (n - 1) * gap
            for k, c in enumerate(cards):
                cx = x + W / 2 - tot / 2 + mc_w / 2 + k * (mc_w + gap)
                out += minicard(c, cx, y0 + H + 2.2 + mc_h / 2, mc_w, mc_h,
                                cross=not menu, light=menu, pt=mc_pt)
    return out


def pentagon(cx, cy, letters, r=10, arrows=(), loops=(), node_mm=6, pt=9, name="p",
             lw="0.9pt"):
    out = ""
    pos = {}
    for i, L in enumerate(letters):
        ang = 90 - 72 * i
        x = cx + r * math.cos(math.radians(ang))
        y = cy + r * math.sin(math.radians(ang))
        pos[L] = (x, y, ang)
        out += (f"\\node[circle, draw, line width=0.6pt, minimum size={node_mm}mm, inner sep=0, "
                f"font={font(pt)}] ({name}{L}) at ({f(x)},{f(y)}) {{{L}}};\n")
    pairs = set(arrows)
    for a, b in arrows:
        if (b, a) in pairs:
            out += f"\\draw[-{{Stealth[length=2mm]}}, line width={lw}] ({name}{a}) to[bend left=22] ({name}{b});\n"
        else:
            out += f"\\draw[-{{Stealth[length=2mm]}}, line width={lw}] ({name}{a}) -- ({name}{b});\n"
    for L in loops:
        ang = pos[L][2]
        out += (f"\\draw[-{{Stealth[length=1.8mm]}}, line width={lw}] ({name}{L}.{f(ang+40)}) "
                f"to[out={f(ang+40)}, in={f(ang-40)}, looseness=5] ({name}{L}.{f(ang-40)});\n")
    return out


def grid(x0, y0, letters, shaded=(), dots=(), cell=6, pt=8, captions=True):
    """Card-by-home grid. Lines (rows of the grid) are cards, columns are homes.

    (x0, y0) is the top-left corner of the grid squares.
    """
    n = len(letters)
    out = ""
    for (c, hm) in shaded:
        i = letters.index(c)
        j = letters.index(hm)
        out += (f"\\fill[gray!45] ({f(x0+j*cell)},{f(y0-(i+1)*cell)}) rectangle "
                f"({f(x0+(j+1)*cell)},{f(y0-i*cell)});\n")
    for k in range(n + 1):
        out += f"\\draw[line width=0.5pt] ({f(x0)},{f(y0-k*cell)}) -- ({f(x0+n*cell)},{f(y0-k*cell)});\n"
        out += f"\\draw[line width=0.5pt] ({f(x0+k*cell)},{f(y0)}) -- ({f(x0+k*cell)},{f(y0-n*cell)});\n"
    for k, L in enumerate(letters):
        out += f"\\node[font={font(pt)}] at ({f(x0+(k+.5)*cell)},{f(y0+2.6)}) {{{L}}};\n"
        out += f"\\node[font={font(pt)}] at ({f(x0-2.8)},{f(y0-(k+.5)*cell)}) {{{L}}};\n"
    for (c, hm) in dots:
        i = letters.index(c)
        j = letters.index(hm)
        out += f"\\fill ({f(x0+(j+.5)*cell)},{f(y0-(i+.5)*cell)}) circle (1.5);\n"
    if captions:
        out += f"\\node[font={font(7, False)}] at ({f(x0+n*cell/2)},{f(y0+6.6)}) {{homes}};\n"
        out += (f"\\node[font={font(7, False)}, rotate=90] at ({f(x0-7.4)},{f(y0-n*cell/2)}) "
                f"{{cards}};\n")
    return out


def swapline(x, y, length, label="swaps", pt=9):
    return (f"\\node[anchor=base west, inner sep=0, font={font(pt, False)}] at ({f(x)},{f(y)}) {{{label}}};\n"
            f"\\draw[line width=0.4pt] ({f(x+len(label)*pt*0.19+1.5)},{f(y-0.8)}) -- ({f(x+len(label)*pt*0.19+1.5+length)},{f(y-0.8)});\n")


def box(x, y, label, w=12, h=8, pt=9, label_left=True):
    """Answer box; (x, y) is the left end of the label baseline region centre."""
    out = ""
    if label:
        out += f"\\node[anchor=east, inner sep=0, font={font(pt, False)}] at ({f(x)},{f(y+h/2)}) {{{label}}};\n"
    out += f"\\draw[line width=0.6pt] ({f(x+1.5)},{f(y)}) rectangle ({f(x+1.5+w)},{f(y+h)});\n"
    return out


def tikz(body, extra=""):
    return f"\\begin{{tikzpicture}}[x=1mm, y=1mm{extra}]\n{body}\\end{{tikzpicture}}"
