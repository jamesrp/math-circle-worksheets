"""TikZ helpers for the Week 8 pages: boards with a star in the bottom-left
corner, token dots, move arrows, piles of counters and answer boxes.

Coordinates on a board: square (a, b) is a columns right of the star's column
and b rows above the star's row, so the star is (0, 0)."""


def board(n, s, dots=(), arrows=(), line="0.9pt", star=True):
    """n-by-n board with squares of side s inches.  The star is drawn as an
    outline so that its square can still be coloured."""
    w = n * s
    out = [r"\begin{tikzpicture}[x=1in,y=1in]"]
    out.append(rf"\draw[line width={line}] (0,0) grid[step={s}] ({w:.4f},{w:.4f});")
    out.append(rf"\draw[line width=1.4pt] (0,0) rectangle ({w:.4f},{w:.4f});")
    if star:
        c = s / 2
        size = 0.62 * s
        lw = 1.3 if s >= 0.6 else (1.0 if s >= 0.35 else 0.8)
        out.append(
            rf"\node[star, star points=5, star point ratio=2.3, draw=black, "
            rf"line width={lw}pt, inner sep=0pt, outer sep=0pt, minimum size={size:.3f}in] "
            rf"at ({c:.4f},{c:.4f}) {{}};"
        )
    for (a, b) in dots:
        x, y = (a + 0.5) * s, (b + 0.5) * s
        out.append(
            rf"\filldraw[fill=black!35, draw=black, line width=0.9pt] "
            rf"({x:.4f},{y:.4f}) circle ({0.3 * s:.4f});"
        )
    for (p, q) in arrows:
        x1, y1 = (p[0] + 0.5) * s, (p[1] + 0.5) * s
        x2, y2 = (q[0] + 0.5) * s, (q[1] + 0.5) * s
        # start the arrow at the edge of the dot
        dx, dy = x2 - x1, y2 - y1
        L = (dx * dx + dy * dy) ** 0.5
        sx, sy = x1 + dx / L * 0.33 * s, y1 + dy / L * 0.33 * s
        out.append(
            rf"\draw[-{{Stealth[length=7pt,width=6pt]}}, line width=1.6pt] "
            rf"({sx:.4f},{sy:.4f}) -- ({x2:.4f},{y2:.4f});"
        )
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def piles(sizes, r=0.12, gap=0.5, vgap=0.035, maxk=None):
    """Piles of counters drawn as towers of circles, side by side, each tower
    on its own short base line.  maxk reserves room for a tower of that
    height, so pictures in one row line up."""
    out = [r"\begin{tikzpicture}[x=1in,y=1in]"]
    if maxk:
        top = 2 * r * maxk + vgap * (maxk - 1)
        out.append(rf"\path (0,-0.03) -- (0,{top:.4f});")
    for i, k in enumerate(sizes):
        x = i * gap
        for j in range(k):
            y = r + j * (2 * r + vgap)
            out.append(
                rf"\draw[line width=0.9pt, fill=white] ({x:.4f},{y:.4f}) circle ({r:.4f});"
            )
        out.append(
            rf"\draw[line width=1.2pt, black!60] ({x - r - 0.05:.4f},-0.03) -- ({x + r + 0.05:.4f},-0.03);"
        )
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def choice(w=0.95, h=0.42, gap=0.3, vertical=False):
    """Two boxes reading 1st and 2nd, for circling."""
    if vertical:
        x2, y2 = 0, -(h + gap)
    else:
        x2, y2 = w + gap, 0
    return (
        r"\begin{tikzpicture}[x=1in,y=1in]"
        rf"\draw[rounded corners=4pt, line width=0.9pt] (0,0) rectangle ({w},{h});"
        rf"\node at ({w / 2},{h / 2}) {{\large 1st}};"
        rf"\draw[rounded corners=4pt, line width=0.9pt] ({x2},{y2}) rectangle ({x2 + w},{y2 + h});"
        rf"\node at ({x2 + w / 2},{y2 + h / 2}) {{\large 2nd}};"
        r"\end{tikzpicture}"
    )


def answer_line(w=2.0):
    return (
        r"\begin{tikzpicture}[x=1in,y=1in]"
        rf"\draw[line width=0.6pt] (0,0) -- ({w},0);"
        r"\end{tikzpicture}"
    )
