"""TikZ snippets for the Week 5 tower-city pages. All lengths in cm."""

CUBE_FILL = "cube"      # colour defined in the preamble
CIRCLE_R = 0.42


def _circle(x, y, r, label=None, font=r"\Large"):
    s = f"\\draw[line width=0.9pt] ({x:.3f},{y:.3f}) circle ({r:.3f});\n"
    if label is not None:
        s += f"\\node at ({x:.3f},{y:.3f}) {{{font} {label}}};\n"
    return s


def eye(x, y, scale=1.0, facing="right"):
    """A simple eye drawn at table level, looking along the row."""
    sx = scale if facing == "right" else -scale
    s = f"\\begin{{scope}}[shift={{({x:.3f},{y:.3f})}}, xscale={sx:.3f}, yscale={scale:.3f}]\n"
    s += r"\draw[line width=0.9pt, fill=white] (-0.55,0) .. controls (-0.2,0.38) and (0.2,0.38) .. (0.55,0) .. controls (0.2,-0.38) and (-0.2,-0.38) .. (-0.55,0);" + "\n"
    s += r"\fill[black!70] (0.12,0) circle (0.2);" + "\n"
    s += r"\fill[white] (0.17,0.06) circle (0.05);" + "\n"
    s += "\\end{scope}\n"
    return s


def side_row(heights, cube=1.0, gap=0.5, circles=True, labels=(None, None),
             r=CIRCLE_R, dashed=False, base_extra=0.0, base_extra_right=None):
    """Side view of a row of towers standing on a table line, with optional
    circles at the two ends (at table level). base_extra lengthens the table
    line on the left (and on the right too, unless base_extra_right is given)."""
    if base_extra_right is None:
        base_extra_right = base_extra
    n = len(heights)
    pitch = cube + gap
    width = n * cube + (n - 1) * gap
    s = ""
    lx = -0.35 - r
    rx = width + 0.35 + r
    style = "dashed, black!55, fill=cube!35" if dashed else "fill=cube, line width=0.7pt"
    for i, h in enumerate(heights):
        x = i * pitch
        for j in range(h):
            s += f"\\draw[{style}] ({x:.3f},{j*cube:.3f}) rectangle ({x+cube:.3f},{(j+1)*cube:.3f});\n"
    left = (lx - r - 0.25 - base_extra) if circles else -0.4 - base_extra
    right = (rx + r + 0.25 + base_extra_right) if circles else width + 0.4 + base_extra_right
    s += f"\\draw[line width=1.2pt] ({left:.3f},0) -- ({right:.3f},0);\n"
    if circles:
        s += _circle(lx, r + 0.04, r, labels[0])
        s += _circle(rx, r + 0.04, r, labels[1])
    return s, (left, right, width)


def chart(n, box=0.8, pitch=1.0, left=None, right=None, show_left=True,
          show_right=True, r=CIRCLE_R):
    """Recording chart: n columns of n empty boxes standing on a table line,
    with circles at the ends. left/right are numbers printed in the circles
    (None = empty circle)."""
    width = (n - 1) * pitch + box
    s = ""
    for i in range(n):
        x = i * pitch
        for j in range(n):
            s += f"\\draw[line width=0.6pt, black!70] ({x:.3f},{j*box:.3f}) rectangle ({x+box:.3f},{(j+1)*box:.3f});\n"
    lx = -0.3 - r
    rx = width + 0.3 + r
    a = (lx - r - 0.15) if show_left else -0.3
    b = (rx + r + 0.15) if show_right else width + 0.3
    s += f"\\draw[line width=1.2pt] ({a:.3f},0) -- ({b:.3f},0);\n"
    if show_left:
        s += _circle(lx, r + 0.04, r, left)
    if show_right:
        s += _circle(rx, r + 0.04, r, right)
    return s, (a, b, n * box)


def card(n, left, right, box=0.8, pitch=1.0):
    """A chart inside a rounded frame, with the two target numbers."""
    body, (a, b, h) = chart(n, box, pitch, left, right)
    s = body
    s += f"\\draw[rounded corners=6pt, line width=0.8pt, black!60] ({a-0.25:.3f},-0.35) rectangle ({b+0.25:.3f},{h+0.35:.3f});\n"
    return s


def row_record(n, sq=1.0, left=None, right=None, r=CIRCLE_R, frame=False):
    """Top view of a row: circle, n squares, circle (for writing heights)."""
    s = ""
    for i in range(n):
        s += f"\\draw[line width=0.8pt] ({i*sq:.3f},0) rectangle ({(i+1)*sq:.3f},{sq:.3f});\n"
    lx = -0.3 - r
    rx = n * sq + 0.3 + r
    s += _circle(lx, sq / 2, r, left)
    s += _circle(rx, sq / 2, r, right)
    if frame:
        s += f"\\draw[rounded corners=6pt, line width=0.8pt, black!60] ({lx-r-0.25:.3f},-0.3) rectangle ({rx+r+0.25:.3f},{sq+0.3:.3f});\n"
    return s


def city(n, sq, clues=None, boxes=False, heights=None, font=r"\Large",
         off=None, box=None):
    """An n-by-n grid. clues: dict with keys ('T',c), ('B',c), ('L',r), ('R',r)
    (rows counted from the top, columns from the left). boxes=True draws an
    empty light square at every clue position."""
    clues = clues or {}
    box = box if box is not None else min(0.75, 0.55 * sq)
    if off is None:
        off = box / 2 + 0.28 if boxes else 0.52
    N = n * sq
    s = ""
    for i in range(1, n):
        s += f"\\draw[line width=0.7pt] ({i*sq:.3f},0) -- ({i*sq:.3f},{N:.3f});\n"
        s += f"\\draw[line width=0.7pt] (0,{i*sq:.3f}) -- ({N:.3f},{i*sq:.3f});\n"
    s += f"\\draw[line width=1.6pt] (0,0) rectangle ({N:.3f},{N:.3f});\n"

    def pos(key):
        side, k = key
        if side == 'T':
            return ((k + 0.5) * sq, N + off)
        if side == 'B':
            return ((k + 0.5) * sq, -off)
        if side == 'L':
            return (-off, N - (k + 0.5) * sq)
        return (N + off, N - (k + 0.5) * sq)

    allkeys = [(sd, k) for sd in 'TBLR' for k in range(n)]
    if boxes:
        for key in allkeys:
            if key in clues:
                continue
            x, y = pos(key)
            hb = box / 2
            s += f"\\draw[black!45, line width=0.6pt] ({x-hb:.3f},{y-hb:.3f}) rectangle ({x+hb:.3f},{y+hb:.3f});\n"
    for key, v in clues.items():
        x, y = pos(key)
        s += f"\\node at ({x:.3f},{y:.3f}) {{{font} {v}}};\n"
    if heights:
        for r in range(n):
            for c in range(n):
                if heights[r][c]:
                    s += f"\\node at ({(c+0.5)*sq:.3f},{N-(r+0.5)*sq:.3f}) {{{font} {heights[r][c]}}};\n"
    return s


def folder_scene(heights=(2, 3, 1), cube=0.9, gap=0.45):
    """A row of towers hidden behind a standing file folder."""
    body, (a, b, w) = side_row(heights, cube=cube, gap=gap, circles=False,
                               dashed=True, base_extra=0.6)
    s = body
    top = max(heights) * cube + 0.7
    s += f"\\draw[line width=0.9pt, fill=folder, fill opacity=0.88] ({-0.55:.3f},0) -- ({-0.55:.3f},{top:.3f}) -- ({w*0.35:.3f},{top:.3f}) -- ({w*0.35+0.3:.3f},{top+0.3:.3f}) -- ({w*0.75:.3f},{top+0.3:.3f}) -- ({w*0.75+0.3:.3f},{top:.3f}) -- ({w+0.55:.3f},{top:.3f}) -- ({w+0.55:.3f},0) -- cycle;\n"
    for i, h in enumerate(heights):
        x = i * (cube + gap)
        s += f"\\draw[dashed, black!55, line width=0.7pt] ({x:.3f},0) rectangle ({x+cube:.3f},{h*cube:.3f});\n"
    return s


def table(n, cell=1.3):
    """Counting table: rows = number seen from the left, columns = number seen
    from the right."""
    s = ""
    N = n * cell
    for i in range(n + 1):
        s += f"\\draw[line width=0.7pt] ({i*cell:.3f},0) -- ({i*cell:.3f},{-N:.3f});\n"
        s += f"\\draw[line width=0.7pt] (0,{-i*cell:.3f}) -- ({N:.3f},{-i*cell:.3f});\n"
    s += f"\\draw[line width=1.4pt] (0,0) rectangle ({N:.3f},{-N:.3f});\n"
    for i in range(n):
        s += f"\\node at ({(i+0.5)*cell:.3f},0.45) {{\\large {i+1}}};\n"
        s += f"\\node at (-0.45,{-(i+0.5)*cell:.3f}) {{\\large {i+1}}};\n"
    s += f"\\node[anchor=south] at ({N/2:.3f},0.95) {{seen from the right end}};\n"
    s += f"\\node[anchor=south, rotate=90] at (-0.95,{-N/2:.3f}) {{seen from the left end}};\n"
    return s
