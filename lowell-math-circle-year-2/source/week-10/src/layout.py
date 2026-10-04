"""Simple row-based layout of towns, pictures, boxes and writing lines into
one TikZ picture of a given width."""

from towns import R, W

TEXTW = 19.0    # usable text width in cm (US Letter, 0.5 inch side margins)


class Item:
    w = 0
    h = 0

    def draw(self, ox, oy):
        return ""


class TownItem(Item):
    """A town, optionally with a check box below or beside it, or writing lines beneath it."""

    def __init__(self, town, labels=None, below=None, line_len=None, nlines=1, extra=""):
        self.t = town
        self.labels = labels
        self.below = below
        x0, y0, x1, y1 = town.bbox()
        self.bb = (x0, y0, x1, y1)
        self.tw, self.th = x1 - x0, y1 - y0
        self.line_len = line_len
        self.nlines = nlines
        self.extra = extra
        self.w = self.tw
        self.h = self.th
        if below == 'box':
            self.h += 1.9
        elif below == 'side':
            self.w += 2.3
            self.h = max(self.h, 1.35)
        elif below == 'line':
            self.h += 0.1 + 1.0 * nlines
            if line_len:
                self.w = max(self.w, line_len)

    def draw(self, ox, oy):
        x0, y0, x1, y1 = self.bb
        if self.below == 'side':
            tx = ox - x0
            ty = oy + (self.h - self.th) / 2 - y0
            s = 1.35
            out = [self.t.tikz(tx, ty, labels=self.labels)]
            out.append(f"\\draw[line width=1.2pt] ({ox + self.w - s:.3f},{oy + self.h / 2 - s / 2:.3f}) rectangle ++({s},{s});")
            return "\n".join(out)
        base = oy + (self.h - self.th)
        tx = ox + (self.w - self.tw) / 2 - x0
        ty = base - y0
        out = [self.t.tikz(tx, ty, labels=self.labels)]
        if self.extra:
            out.append(self.extra.format(x=tx, y=ty))
        cx = ox + self.w / 2
        if self.below == 'box':
            s = 1.35
            out.append(f"\\draw[line width=1.2pt] ({cx - s / 2:.3f},{oy:.3f}) rectangle ++({s},{s});")
        elif self.below == 'line':
            L = self.line_len or self.tw
            for k in range(self.nlines):
                out.append(f"\\draw[black!55, line width=0.6pt] ({cx - L / 2:.3f},{oy + 0.05 + k * 1.0:.3f}) -- ++({L},0);")
        return "\n".join(out)


class PicItem(Item):
    def __init__(self, pic, scale):
        self.p = pic
        self.s = scale
        self.w = pic.w * scale
        self.h = pic.h * scale

    def draw(self, ox, oy):
        return self.p.tikz(ox, oy, self.s)


class PicPair(Item):
    """Two copies of a picture side by side, bottom-aligned, with optional writing lines below."""

    def __init__(self, pic, scale, gap=1.2, nlines=0, line_len=None):
        self.p, self.s, self.gap, self.nlines = pic, scale, gap, nlines
        self.pw, self.ph = pic.w * scale, pic.h * scale
        self.w = 2 * self.pw + gap
        self.line_len = line_len or self.w
        self.w = max(self.w, self.line_len)
        self.h = self.ph + (0.5 + 1.0 * nlines if nlines else 0)

    def draw(self, ox, oy):
        y = oy + self.h - self.ph
        x = ox + (self.w - (2 * self.pw + self.gap)) / 2
        out = [self.p.tikz(x, y, self.s), self.p.tikz(x + self.pw + self.gap, y, self.s)]
        for k in range(self.nlines):
            out.append(f"\\draw[black!55, line width=0.6pt] ({ox + (self.w - self.line_len) / 2:.3f},{oy + 0.05 + k * 1.0:.3f}) -- ++({self.line_len:.3f},0);")
        return "\n".join(out)


class BoxItem(Item):
    def __init__(self, w, h, caption=None, caption_h=0.0):
        self.w, self.h0 = w, h
        self.caption = caption
        self.ch = caption_h
        self.h = h + caption_h

    def draw(self, ox, oy):
        out = [f"\\draw[line width=0.9pt, black!70] ({ox:.3f},{oy:.3f}) rectangle ++({self.w},{self.h0});"]
        if self.caption:
            out.append(f"\\node[anchor=north west, inner sep=0pt, text width={self.w:.2f}cm, align=left] "
                       f"at ({ox:.3f},{oy + self.h:.3f}) {{{self.caption}}};")
        return "\n".join(out)


class LinesItem(Item):
    def __init__(self, w, n, gap=1.0):
        self.w = w
        self.n = n
        self.gap = gap
        self.h = n * gap

    def draw(self, ox, oy):
        out = []
        for k in range(self.n):
            y = oy + k * self.gap + 0.05
            out.append(f"\\draw[black!55, line width=0.6pt] ({ox:.3f},{y:.3f}) -- ++({self.w},0);")
        return "\n".join(out)


class Spacer(Item):
    def __init__(self, w, h=0):
        self.w, self.h = w, h


class Stack(Item):
    """Items stacked vertically (top first), centred horizontally."""

    def __init__(self, items, gap=0.4):
        self.items = items
        self.gap = gap
        self.w = max(i.w for i in items)
        self.h = sum(i.h for i in items) + gap * (len(items) - 1)

    def draw(self, ox, oy):
        out = []
        y = oy + self.h
        for it in self.items:
            y -= it.h
            out.append(it.draw(ox + (self.w - it.w) / 2, y))
            y -= self.gap
        return "\n".join(out)


def figure(rows, width=TEXTW, vgap=0.8, align='center', spread=True, min_gap=0.4):
    """rows: list of lists of Items.  Returns (tikz code, height)."""
    out = []
    heights = [max(i.h for i in row) for row in rows]
    total = sum(heights) + vgap * (len(rows) - 1)
    y = total
    for row, rh in zip(rows, heights):
        y -= rh
        ws = sum(i.w for i in row)
        n = len(row)
        if ws + min_gap * (n - 1) > width + 1e-6:
            raise ValueError(f"row too wide: {ws + min_gap * (n - 1):.2f} cm")
        if spread and n > 1:
            g = (width - ws) / (n + 1)
            g = min(g, 2.0)
            if g < 0.9:
                # tight row: put the free space between the items instead of at the margins
                g = min((width - ws) / (n - 1), 1.0)
            x = (width - ws - g * (n - 1)) / 2
        else:
            g = min_gap
            x = (width - ws - g * (n - 1)) / 2
        for it in row:
            if align == 'center':
                oy = y + (rh - it.h) / 2
            elif align == 'top':
                oy = y + rh - it.h
            else:
                oy = y
            out.append(it.draw(x, oy))
            x += it.w + g
        y -= vgap
    code = (f"\\begin{{tikzpicture}}\n\\useasboundingbox (0,0) rectangle ({width},{total:.3f});\n"
            + "\n".join(out) + "\n\\end{tikzpicture}")
    return code, total


class RawItem(Item):
    """Arbitrary TikZ code drawn in a box [0,w]x[0,h], shifted into place."""

    def __init__(self, code, w, h):
        self.code, self.w, self.h = code, w, h

    def draw(self, ox, oy):
        return f"\\begin{{scope}}[shift={{({ox:.3f},{oy:.3f})}}]\n{self.code}\n\\end{{scope}}"
