"""TikZ snippets for networks, link lists, house/well icons and portal boards."""
import math


def dot(name, p, r, label=None, font=r"\sffamily\bfseries", fill="white", lw="1pt"):
    lab = name if label is None else label
    return (
        f"\\draw[line width={lw}, fill={fill}] ({p[0]:.3f},{p[1]:.3f}) circle ({r:.3f});\n"
        f"\\node[font={font}] at ({p[0]:.3f},{p[1]:.3f}) {{{lab}}};\n"
    )


def network(pos, edges, scale, r, font=r"\sffamily\bfseries", link_w="1.4pt", dot_w="1pt", icons=None):
    """Straight-line drawing; pos in grid units, scaled to cm.
    icons: optional {dot: "house" | "well"} to draw lettered house or well icons instead of circles."""
    P = {v: (x * scale, y * scale) for v, (x, y) in pos.items()}
    out = []
    for a, b in edges:
        out.append(f"\\draw[line width={link_w}] ({P[a][0]:.3f},{P[a][1]:.3f}) -- ({P[b][0]:.3f},{P[b][1]:.3f});\n")
    for v, p in P.items():
        kind = (icons or {}).get(v)
        if kind == "house":
            out.append(house(p, 1.12 * r, v, font=font))
        elif kind == "well":
            out.append(well(p, 1.05 * r, v, font=font))
        else:
            out.append(dot(v, p, r, font=font, lw=dot_w))
    return "".join(out)


def link_list(edges, cols=1, font=r"\sffamily"):
    """A small tabular listing the links as A--B."""
    items = [f"{a}\\,--\\,{b}" for a, b in edges]
    rows = math.ceil(len(items) / cols)
    grid = [items[c * rows:(c + 1) * rows] for c in range(cols)]
    lines = []
    for i in range(rows):
        cells = [grid[c][i] if i < len(grid[c]) else "" for c in range(cols)]
        lines.append(" & ".join(cells) + r" \\")
    spec = "@{}" + "@{\\hspace{0.9em}}".join(["l"] * cols) + "@{}"
    return (
        f"{{{font}\\renewcommand{{\\arraystretch}}{{1.15}}\\begin{{tabular}}{{{spec}}}\n"
        + "\n".join(lines)
        + "\n\\end{tabular}}"
    )


def house(p, s, label="", font=r"\sffamily\bfseries\small"):
    """House icon centred at p, width about 2s."""
    x, y = p
    return (
        f"\\draw[line width=1pt, fill=white] ({x - s:.3f},{y - s:.3f}) -- ({x + s:.3f},{y - s:.3f}) -- "
        f"({x + s:.3f},{y + 0.25 * s:.3f}) -- ({x:.3f},{y + 1.05 * s:.3f}) -- ({x - s:.3f},{y + 0.25 * s:.3f}) -- cycle;\n"
        + (f"\\node[font={font}] at ({x:.3f},{y - 0.3 * s:.3f}) {{{label}}};\n" if label else "")
    )


def well(p, s, label="", font=r"\sffamily\bfseries\small"):
    """Well icon centred at p: a circle with a doubled rim."""
    x, y = p
    return (
        f"\\draw[line width=1pt, fill=white] ({x:.3f},{y:.3f}) circle ({s:.3f});\n"
        f"\\draw[line width=0.6pt] ({x:.3f},{y:.3f}) circle ({0.78 * s:.3f});\n"
        + (f"\\node[font={font}] at ({x:.3f},{y:.3f}) {{{label}}};\n" if label else "")
    )


# Week 41 portal-map seam marks, as fractions of the side (y up): a diamond on the top and
# bottom sides near the left corner, a circle on the left and right sides near the top
# corner, and an arrow along each side (rightward on top and bottom, upward on left and right).
SEAM = {"diamond_x": 0.18, "circle_y": 0.82, "arrow_tb": (0.61, 0.77), "arrow_lr": (0.23, 0.39)}


def portal_frame(x0, y0, size, lw="1.2pt"):
    """Square portal board with the Week 41 seam marks sitting on its sides."""
    x1, y1 = x0 + size, y0 + size
    out = [f"\\draw[line width={lw}] ({x0:.3f},{y0:.3f}) rectangle ({x1:.3f},{y1:.3f});\n"]
    arrow = "-{Stealth[length=2.4mm,width=2.2mm]},line width=1.3pt"
    a0, a1 = SEAM["arrow_tb"]
    for yy in (y0, y1):
        out.append(f"\\draw[{arrow}] ({x0 + a0 * size:.3f},{yy:.3f}) -- ({x0 + a1 * size:.3f},{yy:.3f});\n")
    a0, a1 = SEAM["arrow_lr"]
    for xx in (x0, x1):
        out.append(f"\\draw[{arrow}] ({xx:.3f},{y0 + a0 * size:.3f}) -- ({xx:.3f},{y0 + a1 * size:.3f});\n")
    d = 0.18
    xd = x0 + SEAM["diamond_x"] * size
    for yy in (y0, y1):
        out.append(f"\\draw[line width=0.8pt, fill=white] ({xd:.3f},{yy - d:.3f}) -- ({xd + d:.3f},{yy:.3f}) -- "
                   f"({xd:.3f},{yy + d:.3f}) -- ({xd - d:.3f},{yy:.3f}) -- cycle;\n")
    yc = y0 + SEAM["circle_y"] * size
    for xx in (x0, x1):
        out.append(f"\\draw[line width=0.8pt, fill=white] ({xx:.3f},{yc:.3f}) circle (0.17);\n")
    return "".join(out)


def game_board(pts, w, h, r=0.2, frame=True):
    """Unlettered dots for the link game; pts are fractions of the board's width and height."""
    out = ""
    if frame:
        out += f"\\draw[black!45, line width=0.6pt, rounded corners=3pt] (0,0) rectangle ({w:.3f},{h:.3f});\n"
    for x, y in pts:
        out += f"\\draw[line width=1pt, fill=white] ({x * w:.3f},{y * h:.3f}) circle ({r:.3f});\n"
    return out
