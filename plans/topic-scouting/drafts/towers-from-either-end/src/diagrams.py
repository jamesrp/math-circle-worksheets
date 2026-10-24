"""TikZ helpers for 'Towers from either end' student pages."""

RED = "slotred"
BLUE = "slotblue"
CUBE = "black!14"


def slot_fill(i, tint):
    if not tint:
        return "white"
    return RED if i % 2 == 0 else BLUE


def towers(h, tint=False, s=10.0, b=5.5, q=5.0, numsize=r"\footnotesize",
           maxh=None):
    """Side view: a base rectangle per slot (slot number inside), a stack of
    q x q cubes standing on it.  maxh reserves vertical room so rows line up."""
    out = [r"\begin{tikzpicture}[x=1mm,y=1mm,line join=round]"]
    top = (maxh if maxh is not None else max(h)) * q + b
    # invisible box to fix the height
    out.append(rf"\path (0,0) rectangle ({len(h) * s},{top + 0.5});")
    for i, hh in enumerate(h):
        x0 = i * s
        out.append(rf"\draw[thick, fill={slot_fill(i, tint)}] ({x0},0) "
                   rf"rectangle ({x0 + s},{b});")
        out.append(rf"\node[font={numsize}] at ({x0 + s / 2},{b / 2}) {{{i + 1}}};")
        cx = x0 + (s - q) / 2
        for k in range(hh):
            y = b + k * q
            out.append(rf"\draw[fill={CUBE}] ({cx},{y}) rectangle ({cx + q},{y + q});")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def blank_towers(n, maxh=6, tint=False, s=13.0, b=7.0, q=6.5,
                 numsize=r"\small"):
    """Empty strip with a dashed column of maxh cube outlines above each slot."""
    out = [r"\begin{tikzpicture}[x=1mm,y=1mm,line join=round]"]
    for i in range(n):
        x0 = i * s
        out.append(rf"\draw[thick, fill={slot_fill(i, tint)}] ({x0},0) "
                   rf"rectangle ({x0 + s},{b});")
        out.append(rf"\node[font={numsize}] at ({x0 + s / 2},{b / 2}) {{{i + 1}}};")
        cx = x0 + (s - q) / 2
        for k in range(maxh):
            y = b + k * q
            out.append(rf"\draw[black!45, densely dashed] ({cx},{y}) "
                       rf"rectangle ({cx + q},{y + q});")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def numstrip(h, tint=False, s=9.0, numsize=r"\large", slotsize=r"\scriptsize"):
    """Squares with the tower height written inside; slot number below.
    Entries of h may be None for a blank square to write in."""
    out = [r"\begin{tikzpicture}[x=1mm,y=1mm]"]
    for i, hh in enumerate(h):
        x0 = i * s
        out.append(rf"\draw[thick, fill={slot_fill(i, tint)}] ({x0},0) "
                   rf"rectangle ({x0 + s},{s});")
        if hh is not None:
            out.append(rf"\node[font={numsize}] at ({x0 + s / 2},{s / 2}) {{{hh}}};")
        out.append(rf"\node[font={slotsize}, black!70] at ({x0 + s / 2},-2.3) "
                   rf"{{{i + 1}}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def ring_choices(words, gap=6.0, font=r"\normalsize"):
    """Words spaced out for ringing one of them."""
    sep = r"\hspace{%smm}" % gap
    return "{" + font + " " + sep.join(words) + "}"


def k1_game_marks(n=2, words=("went first", "went second", "tie"),
                  gap="8mm", vstep=13):
    """n rounded boxes stacked, each holding the words to ring one of."""
    out = [r"\begin{tikzpicture}[x=1mm,y=1mm]"]
    body = (r"\hspace{%s}" % gap).join(words)
    for k in range(n):
        out.append(rf"\node[draw=black!60, rounded corners=2mm, inner xsep=4mm, "
                   rf"minimum height=10mm, anchor=west, font=\normalsize] at (0,{-k * vstep}) "
                   rf"{{{body}}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def k1_choice():
    out = [r"\begin{tikzpicture}[x=1mm,y=1mm]"]
    out.append(r"\draw[rounded corners=2mm, black!60] (0,0) rectangle (36,10);")
    out.append(r"\node[font=\large] at (10,5) {1st};")
    out.append(r"\node[font=\large] at (26,5) {2nd};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def two_game_table(w=17):
    """Small table: two games, totals of the player who went first / second."""
    return (r"{\small\renewcommand{\arraystretch}{1.9}"
            r"\begin{tabular}{l|p{%dmm}|p{%dmm}|}" % (w, w) +
            r"\multicolumn{1}{l}{} & \multicolumn{1}{c}{went first} & "
            r"\multicolumn{1}{c}{went second}\\ \cline{2-3}"
            r"game 1 & & \\ \cline{2-3}"
            r"game 2 & & \\ \cline{2-3}"
            r"\end{tabular}}")


def totals_blank(first="first player", second="second player", w=14):
    return (r"{\small %s \rule{%dmm}{0.4pt}\quad %s \rule{%dmm}{0.4pt}}"
            % (first, w, second, w))


def ruled(n, gap_mm=9):
    """Ruled writing lines across the text width (uses \\rulefill macro)."""
    return r"\ruledlines{%d}{%s}" % (n, gap_mm)


def cell_grid(rows, cols, s=9.0):
    out = [r"\begin{tikzpicture}[x=1mm,y=1mm]"]
    for r in range(rows):
        y = -r * (s + 2.5)
        for c in range(cols):
            out.append(rf"\draw[black!70] ({c * s},{y}) rectangle ({(c + 1) * s},{y + s});")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def triangle(h, w=27.5, bh=15.0, gap=1.6, vgap=2.4, labelsize=r"\footnotesize"):
    """Boxes for every run of consecutive towers, short runs at the bottom."""
    n = len(h)
    out = [r"\begin{tikzpicture}[x=1mm,y=1mm]"]
    for k in range(1, n + 1):          # run length
        count = n - k + 1
        y = (k - 1) * (bh + vgap)
        total = count * w + (count - 1) * gap
        full = n * w + (n - 1) * gap
        x_start = (full - total) / 2
        for i in range(count):
            x = x_start + i * (w + gap)
            label = r",\,".join(str(v) for v in h[i:i + k])
            out.append(rf"\draw[black!75] ({x},{y}) rectangle ({x + w},{y + bh});")
            out.append(rf"\node[font={labelsize}, anchor=north] at ({x + w / 2},{y + bh - 0.6}) "
                       rf"{{{label}}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def order_example(h=(3, 1, 4, 2), seq=(4, 3, 1, 2), s=9.0, b=5.0, q=4.5,
                  cell=7.5, frame=True):
    """A finished game on a plain row: ordinal tags above the towers show the
    order they were taken; the record lists the slot numbers in that order,
    under the same ordinal tags."""
    ords = ["1st", "2nd", "3rd", "4th", "5th", "6th"]
    when = {slot: k for k, slot in enumerate(seq)}
    out = [r"\begin{tikzpicture}[x=1mm,y=1mm,line join=round]"]
    tagy = b + max(h) * q + 3.2
    for i, hh in enumerate(h):
        x0 = i * s
        out.append(rf"\draw[thick, fill=white] ({x0},0) rectangle ({x0 + s},{b});")
        out.append(rf"\node[font=\scriptsize] at ({x0 + s / 2},{b / 2}) {{{i + 1}}};")
        cx = x0 + (s - q) / 2
        for k in range(hh):
            y = b + k * q
            out.append(rf"\draw[fill=black!14] ({cx},{y}) rectangle ({cx + q},{y + q});")
        out.append(rf"\node[font=\scriptsize] at ({x0 + s / 2},{tagy}) "
                   rf"{{{ords[when[i + 1]]}}};")
    # arrow
    ax = len(h) * s + 5
    out.append(rf"\draw[-latex, black!60, thick] ({ax},{b + 6}) -- ({ax + 9},{b + 6});")
    # record cells
    x1 = ax + 14
    cy = b + 6 - cell / 2
    for k, slot in enumerate(seq):
        x0 = x1 + k * cell
        out.append(rf"\draw[black!70] ({x0},{cy}) rectangle ({x0 + cell},{cy + cell});")
        out.append(rf"\node[font=\normalsize] at ({x0 + cell / 2},{cy + cell / 2}) {{{slot}}};")
        out.append(rf"\node[font=\scriptsize] at ({x0 + cell / 2},{cy + cell + 2.6}) "
                   rf"{{{ords[k]}}};")
    if frame:
        right = x1 + len(seq) * cell
        out.append(rf"\draw[black!30, rounded corners=2mm] (-4,-4) rectangle "
                   rf"({right + 4},{tagy + 4});")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def towers_to_numbers(h=(3, 1, 4, 2)):
    """Bridge picture: a row of towers, an arrow, the same row as numbers."""
    return (towers(h, s=9, b=5, q=4.5, numsize=r"\scriptsize")
            + r"\hspace{6mm}\raisebox{6mm}{\tikz[x=1mm,y=1mm]"
              r"\draw[-latex, black!60, thick] (0,0) -- (9,0);}\hspace{6mm}"
            + r"\raisebox{3mm}{" + numstrip(h, s=9) + "}")
