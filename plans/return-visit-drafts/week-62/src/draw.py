"""TikZ drawing helpers for the Week 62 return-visit network mats.

All coordinates are millimetres.  Full-size working circles are 20 mm across
(r = 10); lines run centre to centre underneath white-filled circles.
"""
import math

R_FULL = 10.0
GAP = 1.4          # gap between circle edge and an allowed-slot label
DIGIT_W = 2.9      # width of one digit at the label font (mm)
SPACE_W = 1.9      # width of the space between digits
LABEL_H = 4.4      # height of a label box (mm)


def parse_edges(s):
    return [tuple(e) for e in s.split()]


def label_text(nums):
    return r"\,\,".join(str(n) for n in nums)


def label_size(nums):
    n = len(nums)
    return n * DIGIT_W + (n - 1) * SPACE_W + 1.0, LABEL_H


def unit(a):
    return math.cos(math.radians(a)), math.sin(math.radians(a))


def border_dist(w, h, a):
    """distance from rectangle centre to its border in direction a"""
    c, s = unit(a)
    tx = (w / 2) / abs(c) if abs(c) > 1e-9 else 1e9
    ty = (h / 2) / abs(s) if abs(s) > 1e-9 else 1e9
    return min(tx, ty)


def seg_point_dist(p, a, b):
    ax, ay = a; bx, by = b; px, py = p
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = 0 if L2 == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L2))
    qx, qy = ax + t * dx, ay + t * dy
    return math.hypot(px - qx, py - qy)


def rect_seg_clear(cx, cy, w, h, a, b, margin):
    """approximate: sample rectangle boundary points and centre"""
    pts = [(cx, cy)]
    for i in range(-2, 3):
        for j in (-1, 1):
            pts.append((cx + i * w / 4, cy + j * h / 2))
            pts.append((cx + j * w / 2, cy + i * h / 4))
    return min(seg_point_dist(p, a, b) for p in pts) - margin


def rects_overlap(r1, r2, margin=1.0):
    (x1, y1, w1, h1), (x2, y2, w2, h2) = r1, r2
    return abs(x1 - x2) < (w1 + w2) / 2 + margin and abs(y1 - y2) < (h1 + h2) / 2 + margin


def choose_label_angles(pos, edges, lists, r=R_FULL, fixed=None, extra_obstacles=(), avoid=None):
    """Pick an angle for each allowed-slot label, clear of lines, circles and labels.

    avoid='x' (or 'y') penalises labels that stick out beyond the circles sideways (or vertically).
    """
    fixed = dict(fixed or {})
    bx0 = min(p[0] for p in pos.values()) - r; bx1 = max(p[0] for p in pos.values()) + r
    by0 = min(p[1] for p in pos.values()) - r; by1 = max(p[1] for p in pos.values()) + r
    cx = sum(p[0] for p in pos.values()) / len(pos)
    cy = sum(p[1] for p in pos.values()) / len(pos)
    placed = {}
    rects = []
    order = sorted(lists, key=lambda v: (v not in fixed, v))
    for v in order:
        nums = lists[v]
        w, h = label_size(nums)
        p = pos[v]
        cands = [fixed[v]] if v in fixed else list(range(0, 360, 5))
        best = None
        for a in cands:
            u = unit(a)
            d = r + GAP + border_dist(w, h, a)
            lx, ly = p[0] + d * u[0], p[1] + d * u[1]
            score = 0.0
            # clearance from every line
            clear = min([rect_seg_clear(lx, ly, w, h, pos[x], pos[y], 0) for x, y in edges] or [99])
            # clearance from other circles
            cclear = min([math.hypot(lx - q[0], ly - q[1]) - border_dist(w, h, math.degrees(math.atan2(q[1] - ly, q[0] - lx))) - r
                          for k, q in pos.items() if k != v] or [99])
            lclear = 99
            for rr in rects:
                if rects_overlap((lx, ly, w, h), rr, 0):
                    lclear = -5
            for ob in extra_obstacles:
                if rects_overlap((lx, ly, w, h), ob, 0):
                    lclear = -5
            outward = math.cos(math.radians(a) - math.atan2(p[1] - cy, p[0] - cx)) if (p[0], p[1]) != (cx, cy) else 0
            pref = {0: 0.3, 90: 0.25, 180: 0.3, 270: 0.25}.get(a % 360, 0)
            ext = 0.0
            if avoid and 'x' in avoid:
                ext += max(0, lx + w / 2 - bx1) + max(0, bx0 - (lx - w / 2))
            if avoid and 'y' in avoid:
                ext += max(0, ly + h / 2 - by1) + max(0, by0 - (ly - h / 2))
            inc = [math.degrees(math.atan2(pos[y][1] - p[1], pos[y][0] - p[0])) for x, y in edges if x == v] + \
                  [math.degrees(math.atan2(pos[x][1] - p[1], pos[x][0] - p[0])) for x, y in edges if y == v]
            angc = min([abs((a - t + 180) % 360 - 180) for t in inc] or [180])
            score = (min(clear, 4) * 3 + min(cclear, 4) * 3 + min(lclear, 0) * 10 + outward * 0.6 + pref
                     - 0.8 * ext + 0.025 * min(angc, 90))
            if best is None or score > best[0]:
                best = (score, a, (lx, ly, w, h), clear, cclear)
        placed[v] = best[1]
        rects.append(best[2])
        if v not in fixed and (best[3] < 0.8 or best[4] < 0.8):
            print(f"  warning: label for {v} tight (line clearance {best[3]:.1f}, circle {best[4]:.1f})")
    return placed


def tikz_network(pos, edges, *, r=R_FULL, lists=None, label_angles=None, arrows=(),
                 counters=None, numbers=None, letters=True, letter_font=r"\Large\bfseries",
                 number_font=r"\bfseries", list_font=r"\large\bfseries", line_w=0.9,
                 letter_out=None, letter_out_font=r"\scriptsize", bold_nodes=(),
                 counter_font=None):
    """Return TikZ commands (no tikzpicture wrapper)."""
    out = []
    lw = f"line width={line_w}pt"
    for u, v in edges:
        out.append(f"\\draw[{lw}] ({pos[u][0]:.2f},{pos[u][1]:.2f}) -- ({pos[v][0]:.2f},{pos[v][1]:.2f});")
    for u, v in arrows:
        out.append(f"\\draw[{lw},midarrow] ({pos[u][0]:.2f},{pos[u][1]:.2f}) -- ({pos[v][0]:.2f},{pos[v][1]:.2f});")
    for k, (x, y) in pos.items():
        w = line_w * (1.9 if k in bold_nodes else 1)
        out.append(f"\\draw[line width={w}pt, fill=white] ({x:.2f},{y:.2f}) circle ({r}mm);")
        if counters and k in counters:
            cf = counter_font or number_font
            out.append(f"\\draw[line width=0.5pt, fill=black!22] ({x:.2f},{y:.2f}) circle ({r*0.75:.2f}mm);")
            out.append(f"\\node[font={cf}] at ({x:.2f},{y:.2f}) {{{counters[k]}}};")
        elif numbers and k in numbers:
            out.append(f"\\node[font={number_font}] at ({x:.2f},{y:.2f}) {{{numbers[k]}}};")
        elif letters:
            out.append(f"\\node[font={letter_font}] at ({x:.2f},{y:.2f}) {{{k}}};")
        if letter_out and k in letter_out:
            a = letter_out[k]
            ux, uy = unit(a)
            out.append(f"\\node[font={letter_out_font}, inner sep=0.4mm, anchor={(a+180)%360}] at ({x+(r+0.5)*ux:.2f},{y+(r+0.5)*uy:.2f}) {{{k}}};")
    if lists:
        for k, nums in lists.items():
            a = label_angles[k]
            ux, uy = unit(a)
            x, y = pos[k]
            d = r + GAP
            out.append(f"\\node[font={list_font}, inner sep=0.5mm, anchor={(a+180)%360}] at ({x+d*ux:.2f},{y+d*uy:.2f}) {{{label_text(sorted(nums))}}};")
    return "\n".join(out)


def bbox(pos, r=R_FULL, pad=0):
    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    return min(xs) - r - pad, min(ys) - r - pad, max(xs) + r + pad, max(ys) + r + pad


def scaled(pos, s, dx=0, dy=0):
    return {k: (x * s + dx, y * s + dy) for k, (x, y) in pos.items()}


def shift(pos, dx, dy):
    return {k: (x + dx, y + dy) for k, (x, y) in pos.items()}


def outward_angles(pos, edges):
    """for compact copies: put the small letter where no line leaves"""
    res = {}
    for v, p in pos.items():
        inc = []
        for a, b in edges:
            if v in (a, b):
                q = pos[b] if a == v else pos[a]
                inc.append(math.degrees(math.atan2(q[1] - p[1], q[0] - p[0])))
        best = None
        for cand in range(0, 360, 15):
            d = min([abs((cand - t + 180) % 360 - 180) for t in inc] or [180])
            pref = {135: 6, 45: 5, 90: 4, 180: 3, 0: 3}.get(cand, 0)
            sc = min(d, 90) * 10 + pref
            if best is None or sc > best[0]:
                best = (sc, cand)
        res[v] = best[1]
    return res
