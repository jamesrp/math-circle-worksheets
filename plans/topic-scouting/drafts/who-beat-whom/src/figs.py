"""TikZ drawing helpers for tournament pictures (all lengths in cm)."""
import math

FACES = {'cat', 'dog', 'bear', 'rabbit', 'pig', 'frog'}


def f(x):
    return f"{x:.3f}".rstrip('0').rstrip('.') if abs(x) > 1e-9 else "0"


def square(labels, s, origin=(0, 0)):
    ox, oy = origin
    pts = [(0, s), (s, s), (s, 0), (0, 0)]
    return {l: (ox + x, oy + y) for l, (x, y) in zip(labels, pts)}


def tri(labels, s, origin=(0, 0)):
    ox, oy = origin
    pts = [(s / 2, s * math.sqrt(3) / 2), (0, 0), (s, 0)]
    return {l: (ox + x, oy + y) for l, (x, y) in zip(labels, pts)}


def ngon(labels, R, start=90, origin=(0, 0)):
    ox, oy = origin
    n = len(labels)
    return {l: (ox + R * math.cos(math.radians(start - 360 * k / n)),
                oy + R * math.sin(math.radians(start - 360 * k / n)))
            for k, l in enumerate(labels)}


def seg_intersection(p1, p2, p3, p4):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    d = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if abs(d) < 1e-12:
        return None
    t = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / d
    u = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / d
    if 1e-6 < t < 1 - 1e-6 and 1e-6 < u < 1 - 1e-6:
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    return None


def point_seg_dist(c, a, b):
    ax, ay = a; bx, by = b; cx, cy = c
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = max(0, min(1, ((cx - ax) * dx + (cy - ay) * dy) / L2))
    px, py = ax + t * dx, ay + t * dy
    return math.hypot(cx - px, cy - py)


def arrowhead(c, d, L, W, color='black'):
    cx, cy = c; dx, dy = d
    nx, ny = -dy, dx
    tip = (cx + dx * L / 2, cy + dy * L / 2)
    b1 = (cx - dx * L / 2 + nx * W / 2, cy - dy * L / 2 + ny * W / 2)
    b2 = (cx - dx * L / 2 - nx * W / 2, cy - dy * L / 2 - ny * W / 2)
    notch = (cx - dx * L * 0.22, cy - dy * L * 0.22)
    pts = [tip, b1, notch, b2]
    return (f"\\fill[{color}] " + " -- ".join(f"({f(x)},{f(y)})" for x, y in pts)
            + " -- cycle;")


def place_arrows(segs, crossings_for, L):
    """segs: list of (start, end). Return the centre point chosen for each arrowhead."""
    # Prefer the middle, then the loser's side, so that an arrowhead sits near the
    # player it points at; the winner's side is used only when nothing else fits.
    cands = [0.5, 0.56, 0.62, 0.67, 0.72, 0.76, 0.8, 0.44, 0.38, 0.33, 0.28]
    chosen = []
    order = sorted(range(len(segs)), key=lambda i: len(crossings_for[i]))
    result = [None] * len(segs)
    for i in order:
        s, e = segs[i]
        best, bestscore = None, -1
        for t in cands:
            c = (s[0] + t * (e[0] - s[0]), s[1] + t * (e[1] - s[1]))
            dc = min([math.hypot(c[0] - x[0], c[1] - x[1]) for x in crossings_for[i]] + [99])
            da = min([math.hypot(c[0] - a[0], c[1] - a[1]) for a in chosen] + [99])
            dl = min([point_seg_dist(c, *segs[j]) for j in range(len(segs)) if j != i] + [99])
            ok = dc >= 0.55 + L / 2 and da >= 1.6 * L and dl >= 0.32
            score = min(dc - L / 2, da / 1.6, dl * 2)
            if ok:
                best = c
                break
            if score > bestscore:
                best, bestscore = c, score
        result[i] = best
        chosen.append(best)
    return result


def node_code(label, p, r, kind, face_scale=None, font=r'\Large'):
    x, y = p
    out = [f"\\filldraw[fill=white, line width=0.9pt] ({f(x)},{f(y)}) circle ({f(r)});"]
    if label in FACES and kind == 'face':
        sc = face_scale if face_scale else r * 0.92
        out.append(f"\\pic[scale={f(sc)}] at ({f(x)},{f(y)}) {{{label}}};")
    elif label != '':
        out.append(f"\\node[font=\\sffamily\\bfseries{font}] at ({f(x)},{f(y)}) {{{label}}};")
    return out


def tournament(pos, edges=None, r=0.9, kind='letter', arrows=True, L=0.42, W=0.36,
               font=r'\Large', face_scale=None, links=None, labels=None, lw='1.1pt',
               extra=None, bbox=None, under=None):
    """Draw players at pos. edges = list of (winner, loser). If arrows is False,
    plain links are drawn for every pair (or for `links`)."""
    names = list(pos)
    if edges is None:
        if links is None:
            links = [(a, b) for i, a in enumerate(names) for b in names[i + 1:]]
        pairs = links
    else:
        pairs = edges
    segs = []
    for a, b in pairs:
        (ax, ay), (bx, by) = pos[a], pos[b]
        dx, dy = bx - ax, by - ay
        D = math.hypot(dx, dy)
        ux, uy = dx / D, dy / D
        segs.append(((ax + ux * r, ay + uy * r), (bx - ux * r, by - uy * r)))
    crossings_for = [[] for _ in segs]
    for i in range(len(segs)):
        for j in range(i + 1, len(segs)):
            x = seg_intersection(*segs[i], *segs[j])
            if x:
                crossings_for[i].append(x)
                crossings_for[j].append(x)
    out = [r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    if bbox:
        (x0, y0), (x1, y1) = bbox
        out.append(f"\\path ({f(x0)},{f(y0)}) rectangle ({f(x1)},{f(y1)});")
    if under:
        out += under
    for (s, e) in segs:
        out.append(f"\\draw[line width={lw}] ({f(s[0])},{f(s[1])}) -- ({f(e[0])},{f(e[1])});")
    if edges is not None and arrows:
        centres = place_arrows(segs, crossings_for, L)
        for (s, e), c in zip(segs, centres):
            dx, dy = e[0] - s[0], e[1] - s[1]
            D = math.hypot(dx, dy)
            out.append(arrowhead(c, (dx / D, dy / D), L, W))
    for name in names:
        lab = labels[name] if labels and name in labels else name
        out += node_code(lab, pos[name], r, kind, face_scale, font)
    if extra:
        out += extra
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def lineup_boxes(n, box=1.2, gap=0.6, L=0.32, W=0.28, faces=None, face_scale=None):
    """A row of n boxes with right-pointing arrowheads between them."""
    out = [r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    x = 0
    for i in range(n):
        out.append(f"\\draw[line width=0.8pt] ({f(x)},0) rectangle ({f(x + box)},{f(box)});")
        if faces and faces[i]:
            sc = face_scale or box * 0.42
            out.append(f"\\pic[scale={f(sc)}] at ({f(x + box / 2)},{f(box / 2)}) {{{faces[i]}}};")
        if i < n - 1:
            a0, a1 = x + box + 0.08, x + box + gap - 0.08
            out.append(f"\\draw[line width=1.0pt] ({f(a0)},{f(box / 2)}) -- ({f(a1 - L * 0.6)},{f(box / 2)});")
            out.append(arrowhead(((a1 - L / 2), box / 2), (1, 0), L, W))
        x += box + gap
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def lineup_row_fig(faces, r=0.75, spacing=2.4, L=0.4, W=0.34, face_scale=None):
    """A line-up drawn as player circles in a row with arrows between neighbours."""
    pos = {}
    for i, a in enumerate(faces):
        pos[a] = (i * spacing, 0)
    edges = [(faces[i], faces[i + 1]) for i in range(len(faces) - 1)]
    kind = 'face' if faces[0] in FACES else 'letter'
    return tournament(pos, edges, r=r, kind=kind, L=L, W=W, face_scale=face_scale)


def newcomer(results, r=0.5, spacing=1.9, depth=2.7, L=0.36, W=0.3, arrows=True,
             names='ABCDE', top_space=1.0, font=r'\large', side=0.25):
    """Line-up A->B->C->D->E in a row; X below. results[i] is 'W' if X beat names[i]."""
    pos = {n: (i * spacing, 0) for i, n in enumerate(names)}
    mid = (len(names) - 1) * spacing / 2
    pos['X'] = (mid, -depth)
    line = [(names[i], names[i + 1]) for i in range(len(names) - 1)]
    xl = [('X', n) if res == 'W' else (n, 'X') for n, res in zip(names, results)]
    x0, x1 = -r - side, (len(names) - 1) * spacing + r + side
    bbox = ((x0, -depth - r - 0.1), (x1, r + top_space))
    if arrows:
        return tournament(pos, line + xl, r=r, L=L, W=W, font=font, bbox=bbox)
    # line-up arrows drawn, links to X plain
    pic = tournament(pos, line, r=r, L=L, W=W, font=font, bbox=bbox,
                     extra=None)
    # add plain links to X
    extra = []
    for n in names:
        (ax, ay), (bx, by) = pos['X'], pos[n]
        dx, dy = bx - ax, by - ay
        D = math.hypot(dx, dy)
        ux, uy = dx / D, dy / D
        extra.append(f"\\draw[line width=1.1pt] ({f(ax + ux * r)},{f(ay + uy * r)}) -- ({f(bx - ux * r)},{f(by - uy * r)});")
    extra += node_code('X', pos['X'], r, 'letter', None, font)
    return pic.replace(r"\end{tikzpicture}", "\n".join(extra) + "\n\\end{tikzpicture}")


def newcomer_boxes(n, face, box=1.0, gap=0.55, depth=2.5, r=0.6, face_scale=0.55,
                   L=0.3, W=0.26):
    """A blank line-up row of n boxes (arrows between them) with a newcomer animal
    below, joined to every box by a plain link, for recording the newcomer's games."""
    out = [r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    step = box + gap
    mid = (n - 1) * step / 2 + box / 2
    X = (mid, -depth)
    for i in range(n):
        x = i * step
        out.append(f"\\draw[line width=0.8pt] ({f(x)},0) rectangle ({f(x + box)},{f(box)});")
        if i < n - 1:
            a0, a1 = x + box + 0.08, x + box + gap - 0.08
            out.append(f"\\draw[line width=1.0pt] ({f(a0)},{f(box / 2)}) -- ({f(a1 - L * 0.6)},{f(box / 2)});")
            out.append(arrowhead(((a1 - L / 2), box / 2), (1, 0), L, W))
        cx = x + box / 2
        dx, dy = cx - X[0], 0 - X[1]
        D = math.hypot(dx, dy)
        out.append(f"\\draw[line width=1.1pt] ({f(X[0] + dx / D * r)},{f(X[1] + dy / D * r)}) -- ({f(cx)},{f(-0.04)});")
    out += node_code(face, X, r, 'face', face_scale)
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)
