"""Map of Königsberg: four land areas A (island), B (north bank), C (south bank),
D (east land), and seven bridges: A-B twice, A-C twice, A-D, B-D, C-D."""

from towns import Town

MAP_W, MAP_H = 17.0, 12.0

# bridges as (from point, to point, land areas joined)
BRIDGES = [
    ((4.2, 6.0), (4.2, 10.4), 'A', 'B'),
    ((7.0, 6.0), (7.0, 10.4), 'A', 'B'),
    ((4.2, 6.0), (4.2, 1.6), 'A', 'C'),
    ((7.0, 6.0), (7.0, 1.6), 'A', 'C'),
    ((7.6, 6.0), (12.2, 6.0), 'A', 'D'),
    ((14.4, 6.0), (14.4, 10.4), 'D', 'B'),
    ((14.4, 6.0), (14.4, 1.6), 'D', 'C'),
]


def as_town():
    t = Town('koenigsberg')
    for n, (x, y) in {'A': (5.6, 6.0), 'B': (8.5, 11), 'C': (8.5, 1), 'D': (14.5, 6.0)}.items():
        t.island(n, x, y)
    for _, _, u, v in BRIDGES:
        t.bridge(u, v)
    return t


def tikz():
    out = [f"\\fill[black!28] (0,0) rectangle ({MAP_W},{MAP_H});"]
    for (x1, y1), (x2, y2), _, _ in BRIDGES:
        out.append(f"\\draw[bandout] ({x1},{y1}) -- ({x2},{y2});")
    for (x1, y1), (x2, y2), _, _ in BRIDGES:
        out.append(f"\\draw[bandfill] ({x1},{y1}) -- ({x2},{y2});")
    land = "fill=white, draw=black, line width=1.1pt"
    # north bank
    out.append(f"\\filldraw[{land}] (-0.02,{MAP_H}) -- (-0.02,10.0) .. controls (4,9.75) and (7,10.25) .. "
               f"(10,10.0) .. controls (13,9.8) and (15,10.15) .. ({MAP_W + 0.02},9.95) -- ({MAP_W + 0.02},{MAP_H}) -- cycle;")
    # south bank
    out.append(f"\\filldraw[{land}] (-0.02,0) -- (-0.02,2.0) .. controls (4,2.25) and (7,1.75) .. "
               f"(10,2.0) .. controls (13,2.2) and (15,1.85) .. ({MAP_W + 0.02},2.05) -- ({MAP_W + 0.02},0) -- cycle;")
    # island A
    out.append(f"\\filldraw[{land}] (5.6,6.0) ellipse (3.0 and 1.3);")
    # east land D
    out.append(f"\\filldraw[{land}] ({MAP_W + 0.02},4.6) -- (12.9,4.6) .. controls (11.0,4.6) and (11.0,7.4) .. "
               f"(12.9,7.4) -- ({MAP_W + 0.02},7.4) -- cycle;")
    # frame on top so the land edges at the border are clean
    out.append(f"\\draw[line width=1.1pt] (0,0) rectangle ({MAP_W},{MAP_H});")
    for n, (x, y) in {'A': (5.6, 6.0), 'B': (2.0, 11.0), 'C': (2.0, 1.0), 'D': (15.6, 6.0)}.items():
        out.append(f"\\node[font=\\sffamily\\LARGE] at ({x},{y}) {{{n}}};")
    return "\n".join(out)
