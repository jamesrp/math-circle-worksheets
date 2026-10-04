"""Town (multigraph) definitions, analysis, geometry checks and TikZ output
for Week 10: Bridges and one-stroke drawings."""

import math
import itertools
from collections import Counter, deque

R = 0.9525        # island radius in cm (3/4 inch diameter)
W = 1.6           # band width in cm
RC = 1.27         # radius of a 1-inch counter, for the room-for-a-counter check
BORDER = 0.06     # band outline thickness in cm
LOOSE = 0.3915    # TikZ default control distance factor for to[bend ...]


class Town:
    def __init__(self, name, labels=True):
        self.name = name
        self.isl = {}          # name -> (x, y)
        self.order = []
        self.br = []           # (u, v, spec) spec: None | ('bend', deg) | ('ctrl', p1, p2)
        self.labels = labels
        self.letters = {}

    # ---------- construction ----------
    def island(self, n, x, y):
        self.isl[n] = (x, y)
        self.order.append(n)
        return self

    def bridge(self, u, v, bend=0, ctrl=None):
        if ctrl is not None:
            self.br.append((u, v, ('ctrl', ctrl[0], ctrl[1])))
        elif bend:
            self.br.append((u, v, ('bend', bend)))
        else:
            self.br.append((u, v, None))
        return self

    def _ctrl(self, u, v, h):
        (x1, y1), (x2, y2) = self.isl[u], self.isl[v]
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy)
        nx, ny = -dy / L, dx / L
        return ((x1 + dx / 3 + nx * h, y1 + dy / 3 + ny * h), (x1 + 2 * dx / 3 + nx * h, y1 + 2 * dy / 3 + ny * h))

    def curved(self, u, v, h):
        """One bridge from u to v bulging 0.75*h to the left of the direction u->v."""
        return self.bridge(u, v, ctrl=self._ctrl(u, v, h))

    def double(self, u, v, h=1.5):
        """Two bridges between u and v, bulging to either side."""
        return self.curved(u, v, h).curved(u, v, -h)

    def copy(self, name):
        t = Town(name, self.labels)
        t.isl = dict(self.isl)
        t.order = list(self.order)
        t.br = list(self.br)
        return t

    # ---------- combinatorics ----------
    def deg(self):
        d = Counter({n: 0 for n in self.isl})
        for u, v, _ in self.br:
            d[u] += 1
            d[v] += 1
        return d

    def odd(self):
        d = self.deg()
        return [n for n in self.order if d[n] % 2]

    def connected(self):
        adj = {n: set() for n in self.isl}
        for u, v, _ in self.br:
            adj[u].add(v)
            adj[v].add(u)
        start = self.order[0]
        seen = {start}
        dq = deque([start])
        while dq:
            x = dq.popleft()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    dq.append(y)
        return len(seen) == len(self.isl)

    def edges(self):
        return [(u, v) for u, v, _ in self.br]

    def trail_from(self, start, edges=None):
        """Return one Euler trail from start (list of islands) or None."""
        E = edges if edges is not None else self.edges()
        m = len(E)
        inc = {n: [] for n in self.isl}
        for i, (u, v) in enumerate(E):
            inc[u].append((i, v))
            inc[v].append((i, u))
        used = [False] * m
        path = [start]

        def dfs(x, k):
            if k == m:
                return True
            for i, y in inc[x]:
                if not used[i]:
                    used[i] = True
                    path.append(y)
                    if dfs(y, k + 1):
                        return True
                    path.pop()
                    used[i] = False
            return False

        return list(path) if dfs(start, 0) else None

    def starts(self, edges=None):
        """dict start -> set of possible end islands (by exhaustive search)."""
        E = edges if edges is not None else self.edges()
        res = {}
        m = len(E)
        inc = {n: [] for n in self.isl}
        for i, (u, v) in enumerate(E):
            inc[u].append((i, v))
            inc[v].append((i, u))
        for s in self.order:
            ends = set()
            used = [False] * m

            def dfs(x, k):
                if k == m:
                    ends.add(x)
                    return
                for i, y in inc[x]:
                    if not used[i]:
                        used[i] = True
                        dfs(y, k + 1)
                        used[i] = False

            if m <= 14:
                dfs(s, 0)
            else:
                # parity theory for big towns, confirmed by one trail
                odd = self.odd_of(E)
                if len(odd) == 0:
                    if self.trail_from(s, E):
                        ends = {s}
                elif len(odd) == 2 and s in odd:
                    if self.trail_from(s, E):
                        ends = {o for o in odd if o != s}
            if ends:
                res[s] = ends
        return res

    def odd_of(self, E):
        d = Counter({n: 0 for n in self.isl})
        for u, v in E:
            d[u] += 1
            d[v] += 1
        return [n for n in self.order if d[n] % 2]

    def greedy_success(self, start, trials=4000, seed=1):
        """Fraction of random walks (choose any available bridge uniformly)
        that pick up every counter."""
        import random
        rng = random.Random(seed)
        E = self.edges()
        ok = 0
        for _ in range(trials):
            used = [False] * len(E)
            x = start
            k = 0
            while True:
                opts = [i for i, (u, v) in enumerate(E) if not used[i] and (u == x or v == x)]
                if not opts:
                    break
                i = rng.choice(opts)
                used[i] = True
                u, v = E[i]
                x = v if u == x else u
                k += 1
            ok += (k == len(E))
        return ok / trials

    def dist(self):
        adj = {n: set() for n in self.isl}
        for u, v, _ in self.br:
            adj[u].add(v)
            adj[v].add(u)
        D = {}
        for s in self.order:
            d = {s: 0}
            dq = deque([s])
            while dq:
                x = dq.popleft()
                for y in adj[x]:
                    if y not in d:
                        d[y] = d[x] + 1
                        dq.append(y)
            D[s] = d
        return D

    def postman(self):
        """(fewest extra crossings for closed route, for open route)."""
        odd = self.odd()
        D = self.dist()

        def best_pairing(nodes):
            if not nodes:
                return 0
            a = nodes[0]
            best = None
            for j in range(1, len(nodes)):
                b = nodes[j]
                rest = nodes[1:j] + nodes[j + 1:]
                c = D[a][b] + best_pairing(rest)
                best = c if best is None else min(best, c)
            return best

        closed = best_pairing(odd)
        if len(odd) <= 2:
            opened = 0
        else:
            opened = min(best_pairing([o for o in odd if o not in (a, b)])
                         for a, b in itertools.combinations(odd, 2))
        return closed, opened

    def double_bridge_works(self):
        """indices of bridges which, when crossed twice, allow a full walk."""
        out = []
        E = self.edges()
        for i in range(len(E)):
            E2 = E + [E[i]]
            odd = self.odd_of(E2)
            if len(odd) in (0, 2):
                s = odd[0] if odd else self.order[0]
                if self.trail_from(s, E2):
                    out.append(i)
        return out

    def single_additions(self):
        """pairs {u,v} such that adding a bridge u-v makes a full walk possible."""
        out = []
        for u, v in itertools.combinations(self.order, 2):
            E2 = self.edges() + [(u, v)]
            if len(self.odd_of(E2)) in (0, 2):
                out.append((u, v))
        return out

    def report(self):
        d = self.deg()
        lines = [f"== {self.name}: {len(self.isl)} islands, {len(self.br)} bridges, "
                 f"connected={self.connected()}"]
        lines.append("   degrees: " + ", ".join(f"{self.letters.get(n, n)}={d[n]}" for n in self.order))
        odd = self.odd()
        lines.append(f"   odd: {[self.letters.get(n, n) for n in odd]}")
        st = self.starts()
        lines.append("   starts->ends: " + "; ".join(
            f"{self.letters.get(s, s)}->{sorted(self.letters.get(e, e) for e in es)}" for s, es in st.items()))
        return "\n".join(lines)

    # ---------- geometry ----------
    def path_points(self, b, n=48):
        u, v, spec = b
        (x1, y1), (x2, y2) = self.isl[u], self.isl[v]
        if spec is None:
            return [(x1 + (x2 - x1) * t / n, y1 + (y2 - y1) * t / n) for t in range(n + 1)]
        if spec[0] == 'bend':
            th = math.radians(spec[1])
            phi = math.atan2(y2 - y1, x2 - x1)
            d = math.hypot(x2 - x1, y2 - y1)
            c = LOOSE * d
            p1 = (x1 + c * math.cos(phi + th), y1 + c * math.sin(phi + th))
            p2 = (x2 + c * math.cos(phi + math.pi - th), y2 + c * math.sin(phi + math.pi - th))
        else:
            p1, p2 = spec[1], spec[2]
        p0, p3 = (x1, y1), (x2, y2)
        pts = []
        for k in range(n + 1):
            t = k / n
            a, b_, c_, d_ = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3
            pts.append((a * p0[0] + b_ * p1[0] + c_ * p2[0] + d_ * p3[0],
                        a * p0[1] + b_ * p1[1] + c_ * p2[1] + d_ * p3[1]))
        return pts

    def bbox(self, pad=0.0):
        xs, ys = [], []
        for n, (x, y) in self.isl.items():
            xs += [x - R, x + R]
            ys += [y - R, y + R]
        for b in self.br:
            for (x, y) in self.path_points(b, 24):
                xs += [x - W / 2, x + W / 2]
                ys += [y - W / 2, y + W / 2]
        return (min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad)

    def geometry_check(self, min_angle=40.0, min_visible=2.4):
        msgs = []
        # angle between bands at each island
        for n in self.order:
            angs = []
            for b in self.br:
                u, v, _ = b
                if n not in (u, v):
                    continue
                pts = self.path_points(b, 200)
                if u == n:
                    seq = pts
                else:
                    seq = pts[::-1]
                # direction at island boundary
                cx, cy = self.isl[n]
                q = next(p for p in seq if math.hypot(p[0] - cx, p[1] - cy) >= R)
                angs.append(math.degrees(math.atan2(q[1] - cy, q[0] - cx)) % 360)
            angs.sort()
            if len(angs) >= 2:
                gaps = [(angs[(i + 1) % len(angs)] - angs[i]) % 360 for i in range(len(angs))]
                if min(gaps) < min_angle:
                    msgs.append(f"angle {min(gaps):.0f} deg at {n}")
        # visible length
        for b in self.br:
            pts = self.path_points(b, 200)
            L = sum(math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(len(pts) - 1))
            vis = L - 2 * R
            if vis < min_visible:
                msgs.append(f"short bridge {b[0]}-{b[1]} visible {vis:.2f}")
        # band vs non-endpoint island
        for b in self.br:
            pts = self.path_points(b, 200)
            for n, (x, y) in self.isl.items():
                if n in (b[0], b[1]):
                    continue
                dmin = min(math.hypot(p[0] - x, p[1] - y) for p in pts)
                if dmin < R + W / 2 + 0.25:
                    msgs.append(f"bridge {b[0]}-{b[1]} near island {n} ({dmin:.2f})")
        # band vs band
        for i, j in itertools.combinations(range(len(self.br)), 2):
            bi, bj = self.br[i], self.br[j]
            shared = {bi[0], bi[1]} & {bj[0], bj[1]}
            pi = self.path_points(bi, 120)
            pj = self.path_points(bj, 120)

            def far(p):
                return all(math.hypot(p[0] - self.isl[s][0], p[1] - self.isl[s][1]) > R + 1.5 for s in shared)

            pi2 = [p for p in pi if far(p)]
            pj2 = [p for p in pj if far(p)]
            if not pi2 or not pj2:
                continue
            dmin = min(math.hypot(p[0] - q[0], p[1] - q[1]) for p in pi2 for q in pj2)
            if dmin < W + (0.1 if shared else 0.4):
                msgs.append(f"bridges {bi[0]}-{bi[1]} and {bj[0]}-{bj[1]} close ({dmin:.2f})")
        return msgs

    def arclen(self, b, n=400):
        pts = self.path_points(b, n)
        return sum(math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(len(pts) - 1))

    def midpoint(self, b, n=400):
        pts = self.path_points(b, n)
        L = [0.0]
        for i in range(len(pts) - 1):
            L.append(L[-1] + math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]))
        half = L[-1] / 2
        k = next(i for i in range(len(L)) if L[i] >= half)
        return pts[k]

    def counter_room(self):
        """For each bridge: room around a counter sitting at the bridge's midpoint.
        Returns list of (bridge, visible length, clearance to the nearest other band edge
        or other island edge)."""
        out = []
        for i, b in enumerate(self.br):
            m = self.midpoint(b)
            vis = self.arclen(b) - 2 * R
            clr = 99.0
            for j, b2 in enumerate(self.br):
                if j == i:
                    continue
                pts = self.path_points(b2, 300)
                d = min(math.hypot(p[0] - m[0], p[1] - m[1]) for p in pts) - W / 2
                clr = min(clr, d)
            for n, (x, y) in self.isl.items():
                if n in (b[0], b[1]):
                    continue
                clr = min(clr, math.hypot(x - m[0], y - m[1]) - R)
            out.append((b, vis, clr))
        return out

    def counter_check(self, min_vis=3.0, rc=RC):
        msgs = []
        for b, vis, clr in self.counter_room():
            if vis < min_vis:
                msgs.append(f"{b[0]}-{b[1]} visible {vis:.2f}")
            if clr < rc:
                msgs.append(f"{b[0]}-{b[1]} clearance {clr:.2f}")
        return msgs

    # ---------- drawing ----------
    def path_tikz(self, b, ox, oy):
        u, v, spec = b
        (x1, y1), (x2, y2) = self.isl[u], self.isl[v]
        a = f"({x1 + ox:.3f},{y1 + oy:.3f})"
        c = f"({x2 + ox:.3f},{y2 + oy:.3f})"
        if spec is None:
            return f"{a} -- {c}"
        if spec[0] == 'bend':
            return f"{a} to[bend left={spec[1]}] {c}"
        p1, p2 = spec[1], spec[2]
        return (f"{a} .. controls ({p1[0] + ox:.3f},{p1[1] + oy:.3f}) and "
                f"({p2[0] + ox:.3f},{p2[1] + oy:.3f}) .. {c}")

    def tikz(self, ox=0.0, oy=0.0, labels=None, extra_bridges=()):
        labels = self.labels if labels is None else labels
        out = []
        for b in self.br:
            out.append(f"\\draw[bandout] {self.path_tikz(b, ox, oy)};")
        for b in self.br:
            out.append(f"\\draw[bandfill] {self.path_tikz(b, ox, oy)};")
        for n in self.order:
            x, y = self.isl[n]
            out.append(f"\\draw[island] ({x + ox:.3f},{y + oy:.3f}) circle ({R});")
            if labels:
                out.append(f"\\node[islandlabel] at ({x + ox:.3f},{y + oy:.3f}) {{{self.letters.get(n, n)}}};")
        return "\n".join(out)


def tikz_styles():
    return (
        "\\tikzset{\n"
        f"  bandout/.style={{line width={W}cm, draw=black!75, line cap=butt}},\n"
        f"  bandfill/.style={{line width={W - 2 * BORDER:.3f}cm, draw=black!9, line cap=butt}},\n"
        "  island/.style={fill=white, draw=black, line width=1.3pt},\n"
        "  islandlabel/.style={font=\\sffamily\\Large},\n"
        "  stroke/.style={line width=1.4pt, draw=black!50, line cap=round, line join=round},\n"
        "}\n")


# ====================================================================
# Shape library.  S is the usual centre-to-centre distance.
# ====================================================================
S = 4.95          # every straight bridge shows at least 3 cm between its islands
H3 = math.sqrt(3) / 2


def triangle(name, s=S):
    t = Town(name)
    t.island('A', 0, 0).island('B', s, 0).island('C', s / 2, s * H3)
    t.bridge('A', 'B').bridge('B', 'C').bridge('C', 'A')
    return t


def diamond(name, s=S):
    # two triangles sharing the bridge P-Q
    t = Town(name)
    t.island('T', 0, s * H3).island('P', -s / 2, 0).island('Q', s / 2, 0).island('B', 0, -s * H3)
    t.bridge('P', 'Q').bridge('P', 'T').bridge('Q', 'T').bridge('P', 'B').bridge('Q', 'B')
    return t


def bowtie(name, s=S):
    t = Town(name)
    a = math.radians(30)
    t.island('L1', -s * math.cos(a), s * math.sin(a)).island('L2', -s * math.cos(a), -s * math.sin(a))
    t.island('O', 0, 0)
    t.island('R1', s * math.cos(a), s * math.sin(a)).island('R2', s * math.cos(a), -s * math.sin(a))
    t.bridge('O', 'L1').bridge('L1', 'L2').bridge('L2', 'O')
    t.bridge('O', 'R1').bridge('R1', 'R2').bridge('R2', 'O')
    return t


def house(name, s=S, roof=None):
    roof = s * H3 if roof is None else roof
    t = Town(name)
    t.island('BL', 0, 0).island('BR', s, 0).island('TR', s, s).island('TL', 0, s).island('AP', s / 2, s + roof)
    t.bridge('BL', 'BR').bridge('BR', 'TR').bridge('TR', 'TL').bridge('TL', 'BL')
    t.bridge('TL', 'AP').bridge('AP', 'TR')
    return t


def ladder(name, cols=3, s=S):
    t = Town(name)
    for i in range(cols):
        t.island(f'b{i}', i * s, 0)
    for i in range(cols):
        t.island(f't{i}', i * s, s)
    for i in range(cols - 1):
        t.bridge(f'b{i}', f'b{i + 1}')
        t.bridge(f't{i}', f't{i + 1}')
    for i in range(cols):
        t.bridge(f'b{i}', f't{i}')
    return t


def triforce(name, s=S):
    t = Town(name)
    t.island('A', 0, 0).island('D', s, 0).island('B', 2 * s, 0)
    t.island('F', s / 2, s * H3).island('E', 1.5 * s, s * H3).island('C', s, 2 * s * H3)
    for u, v in [('A', 'D'), ('D', 'B'), ('B', 'E'), ('E', 'C'), ('C', 'F'), ('F', 'A'),
                 ('D', 'E'), ('E', 'F'), ('F', 'D')]:
        t.bridge(u, v)
    return t


def claw(name, s=S):
    t = Town(name)
    t.island('O', 0, 0)
    for k, a in enumerate([90, 210, 330]):
        t.island(f'L{k}', s * math.cos(math.radians(a)), s * math.sin(math.radians(a)))
        t.bridge('O', f'L{k}')
    return t


def long_claw(name, s=S):
    t = Town(name)
    t.island('O', 0, 0)
    for k, a in enumerate([90, 210, 330]):
        c, sn = math.cos(math.radians(a)), math.sin(math.radians(a))
        t.island(f'M{k}', s * c, s * sn)
        t.island(f'E{k}', 2 * s * c, 2 * s * sn)
        t.bridge('O', f'M{k}').bridge(f'M{k}', f'E{k}')
    return t


def k4(name, s=S):
    # diamond of two triangles plus an outer arc from left to right over the top
    t = Town(name)
    t.island('A', 0, s / 2).island('C', 0, -s / 2)
    t.island('B', -s * H3, 0).island('D', s * H3, 0)
    t.bridge('A', 'C').bridge('A', 'B').bridge('A', 'D').bridge('C', 'B').bridge('C', 'D')
    bx = -s * H3
    t.bridge('B', 'D', ctrl=((bx - 0.6, s * 1.45), (-bx + 0.6, s * 1.45)))
    return t


def flower(name, s=S):
    t = Town(name)
    t.island('O', 0, 0)
    for k in range(3):
        a1 = math.radians(90 + 120 * k - 30)
        a2 = math.radians(90 + 120 * k + 30)
        t.island(f'P{k}', s * math.cos(a1), s * math.sin(a1))
        t.island(f'Q{k}', s * math.cos(a2), s * math.sin(a2))
        t.bridge('O', f'P{k}').bridge(f'P{k}', f'Q{k}').bridge(f'Q{k}', 'O')
    return t


def grid(name, rows, cols, s=S):
    t = Town(name)
    for r in range(rows):
        for c in range(cols):
            t.island(f'{r}{c}', c * s, -r * s)
    for r in range(rows):
        for c in range(cols):
            if c + 1 < cols:
                t.bridge(f'{r}{c}', f'{r}{c + 1}')
            if r + 1 < rows:
                t.bridge(f'{r}{c}', f'{r + 1}{c}')
    return t


def tri_lattice(name, n=3, s=S):
    t = Town(name)
    pts = {}
    for j in range(n + 1):           # row from bottom
        for i in range(n + 1 - j):
            x = (i + j / 2) * s
            y = j * s * H3
            nm = f'{i}_{j}'
            pts[(i, j)] = nm
            t.island(nm, x, y)
    for (i, j), nm in pts.items():
        for di, dj in [(1, 0), (0, 1), (-1, 1)]:
            q = (i + di, j + dj)
            if q in pts:
                t.bridge(nm, pts[q])
    return t


def relabel(t, mapping):
    """Give islands display letters, in the order of mapping."""
    t.letters = dict(mapping)
    return t
