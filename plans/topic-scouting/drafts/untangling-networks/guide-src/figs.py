"""Write the guide's TikZ figures into gen/.  Run: python3 figs.py"""
import math
import os

import netdata as N
from tikzgen import SEAM, house, well

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "gen")
os.makedirs(GEN, exist_ok=True)

FONT = r"\sffamily\bfseries\scriptsize"


def mini(pos, links, size=2.3, r=0.17, icons=None, marks=False, ghost=None, arrow=None, lw="0.9pt", extent=None,
         bend=None):
    """A small straight-line drawing scaled (equally in x and y) so its larger side is `size` cm.
    extent: extra points used only for the scale and the bounding box (to match several panels).
    bend: {link: (control1, control2)} draws that link as a cubic Bezier curve instead."""
    xs = [p[0] for p in list(pos.values()) + list(extent or [])]
    ys = [p[1] for p in list(pos.values()) + list(extent or [])]
    k = size / max(max(xs) - min(xs), max(ys) - min(ys))
    P = {v: ((x - min(xs)) * k, (y - min(ys)) * k) for v, (x, y) in pos.items()}
    out = []
    pad = r * 1.25
    out.append(f"\\useasboundingbox ({-pad:.3f},{-pad:.3f}) rectangle "
               f"({(max(xs) - min(xs)) * k + pad:.3f},{(max(ys) - min(ys)) * k + pad:.3f});\n")
    if ghost:
        g = ((ghost[1][0] - min(xs)) * k, (ghost[1][1] - min(ys)) * k)
        out.append(f"\\draw[black!45, dashed, line width=0.7pt] ({P[ghost[2]][0]:.3f},{P[ghost[2]][1]:.3f}) -- ({g[0]:.3f},{g[1]:.3f});\n")
        out.append(f"\\draw[black!45, dashed, line width=0.7pt, fill=white] ({g[0]:.3f},{g[1]:.3f}) circle ({r:.3f});\n")
        if arrow:
            a = P[ghost[0]]
            out.append(f"\\draw[-{{Stealth[length=1.8mm]}}, line width=0.8pt, black!70] ({g[0] + 0.25:.3f},{g[1] + 0.12:.3f}) "
                       f"to[bend right=25] ({a[0] + 0.05:.3f},{a[1] - 0.26:.3f});\n")
    for a, b in links:
        if bend and (a, b) in bend:
            c1, c2 = [((x - min(xs)) * k, (y - min(ys)) * k) for x, y in bend[(a, b)]]
            out.append(f"\\draw[line width={lw}] ({P[a][0]:.3f},{P[a][1]:.3f}) .. controls ({c1[0]:.3f},{c1[1]:.3f}) "
                       f"and ({c2[0]:.3f},{c2[1]:.3f}) .. ({P[b][0]:.3f},{P[b][1]:.3f});\n")
            continue
        out.append(f"\\draw[line width={lw}] ({P[a][0]:.3f},{P[a][1]:.3f}) -- ({P[b][0]:.3f},{P[b][1]:.3f});\n")
    if marks:
        for e, f in N.crossing_pairs(P, links):
            c = N.cross_point(P[e[0]], P[e[1]], P[f[0]], P[f[1]])
            out.append(f"\\draw[line width=0.6pt, black!60] ({c[0]:.3f},{c[1]:.3f}) circle (0.1);\n")
    for v, p in P.items():
        kind = (icons or {}).get(v)
        if kind == "house":
            out.append(house(p, 1.1 * r, v, font=FONT))
        elif kind == "well":
            out.append(well(p, 1.05 * r, v, font=FONT))
        else:
            out.append(f"\\draw[line width=0.7pt, fill=white] ({p[0]:.3f},{p[1]:.3f}) circle ({r:.3f});\n"
                       f"\\node[font={FONT}, inner sep=0pt] at ({p[0]:.3f},{p[1]:.3f}) {{{v}}};\n")
    return "\\begin{tikzpicture}[baseline=(current bounding box.center)]\n" + "".join(out) + "\\end{tikzpicture}%\n"


def portal_marks(size, printed):
    """Week 41 seam marks as on the pages' boards, shrunk with the board (printed side in cm)."""
    k = size / printed
    out = []
    arrow = f"-{{Stealth[length={2.4 * k:.2f}mm,width={2.2 * k:.2f}mm]}},line width=0.9pt"
    a0, a1 = SEAM["arrow_tb"]
    for yy in (0, size):
        out.append(f"\\draw[{arrow}] ({a0 * size:.3f},{yy:.3f}) -- ({a1 * size:.3f},{yy:.3f});\n")
    a0, a1 = SEAM["arrow_lr"]
    for xx in (0, size):
        out.append(f"\\draw[{arrow}] ({xx:.3f},{a0 * size:.3f}) -- ({xx:.3f},{a1 * size:.3f});\n")
    d = 0.18 * k
    xd = SEAM["diamond_x"] * size
    for yy in (0, size):
        out.append(f"\\draw[line width=0.6pt, fill=white] ({xd:.3f},{yy - d:.3f}) -- ({xd + d:.3f},{yy:.3f}) -- "
                   f"({xd:.3f},{yy + d:.3f}) -- ({xd - d:.3f},{yy:.3f}) -- cycle;\n")
    yc = SEAM["circle_y"] * size
    for xx in (0, size):
        out.append(f"\\draw[line width=0.6pt, fill=white] ({xx:.3f},{yc:.3f}) circle ({0.17 * k:.3f});\n")
    return "".join(out)


STUB_OFF = 0.28  # cm outside the side for an exit/entry number


def stub_label_points(name, size):
    """Printed positions (cm) of the exit/entry numbers: [(number, (x, y)), ...], two per number."""
    pos, links, printed = N.PORTAL[name]
    out = []
    for n, a, b, e in N.portal_stubs(pos, N.portal_offsets(name)):
        for pt in (a, b):
            sd = N.side_of(pt)
            x, y = pt[0] * size, pt[1] * size
            x += {"L": -STUB_OFF, "R": STUB_OFF}.get(sd, 0)
            y += {"B": -STUB_OFF, "T": STUB_OFF}.get(sd, 0)
            out.append((n, (x, y)))
    return out


def portal_solution(name, size=6.2, r=0.17):
    pos, links, printed = N.PORTAL[name]
    offs = N.portal_offsets(name)
    out = [f"\\draw[line width=0.9pt] (0,0) rectangle ({size:.3f},{size:.3f});\n"]
    for e, off in offs.items():
        p, q = N.cover_segment(pos, e, off)
        for a, b in N.clip_to_square(p, q):
            out.append(f"\\draw[line width=0.7pt] ({a[0] * size:.3f},{a[1] * size:.3f}) -- ({b[0] * size:.3f},{b[1] * size:.3f});\n")
    out.append(portal_marks(size, printed))
    for n, (x, y) in stub_label_points(name, size):
        out.append(f"\\node[font=\\sffamily\\bfseries\\scriptsize, inner sep=0pt] at ({x:.3f},{y:.3f}) {{{n}}};\n")
    font = r"\sffamily\bfseries\scriptsize"
    for v, (x, y) in pos.items():
        p = (x * size, y * size)
        if name == "k33":
            out.append(house(p, 0.22, v, font=font) if v in "ABC" else well(p, 0.21, v, font=font))
        else:
            out.append(f"\\draw[line width=0.6pt, fill=white] ({p[0]:.3f},{p[1]:.3f}) circle ({r:.3f});\n"
                       f"\\node[font={font}, inner sep=0pt] at ({p[0]:.3f},{p[1]:.3f}) {{{v}}};\n")
    return "\\begin{tikzpicture}[baseline=(current bounding box.center)]\n" + "".join(out) + "\\end{tikzpicture}%\n"


def save(name, body):
    with open(os.path.join(GEN, name + ".tex"), "w") as f:
        f.write(body)


HW23 = {"A": "house", "B": "house", "C": "well", "D": "well", "E": "well"}
HW33 = {"A": "house", "B": "house", "C": "house", "D": "well", "E": "well", "F": "well"}

if __name__ == "__main__":
    # launch: input, one move, output (same scale in all three panels)
    ext = list(N.LAUNCH_IN.values()) + [N.LAUNCH_OUT["D"]]
    save("launch_in", mini(N.LAUNCH_IN, N.LAUNCH_LINKS, size=2.2, marks=True, extent=ext))
    save("launch_step", mini(N.LAUNCH_OUT, N.LAUNCH_LINKS, size=2.2, ghost=("D", N.LAUNCH_IN["D"], "C"),
                             arrow=True, extent=ext))
    save("launch_out", mini(N.LAUNCH_OUT, N.LAUNCH_LINKS, size=2.2, extent=ext))
    save("launch_bend", mini(N.LAUNCH_IN, N.LAUNCH_LINKS, size=2.2, extent=ext, bend=N.LAUNCH_BEND))

    for nm in ("k_bowtie", "k_kite", "k_k4", "k_star", "k_fan", "k_prism"):
        save("key_" + nm, mini(N.UNTANGLED[nm], N.PAGE_NETS[nm][0], size=1.9))
    save("key_k_hw23", mini(N.UNTANGLED["k_hw23"], N.PAGE_NETS["k_hw23"][0], size=1.9, r=0.21, icons=HW23))
    # K-1 Problems 3 and 5: the same fewest-crossing drawings as Figure 2, at the K-1 key's size
    save("key_k_hw33", mini(N.FEWEST["K33"][0], N.FEWEST["K33"][1], size=2.1, marks=True, r=0.21, icons=HW33))
    save("key_k_k5", mini(N.FEWEST["K5"][0], N.FEWEST["K5"][1], size=1.9, marks=True))
    for nm in ("n1", "n3", "n4", "n6"):
        save("key_" + nm, mini(N.UNTANGLED[nm], N.PAGE_NETS[nm][0], size=2.4))
    for nm, (pos, links, c) in N.FEWEST.items():
        save("few_" + nm, mini(pos, links, size=2.8, marks=True, r=0.21 if nm == "K33" else 0.17,
                                icons=HW33 if nm == "K33" else None))
    for nm in N.PORTAL:
        save("portal_" + nm, portal_solution(nm))
    print("figures written to", GEN)
