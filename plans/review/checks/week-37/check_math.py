"""Independent mathematical check of Week 37 (Mirror twins), base packet and guide.

Reads every tetrahedron drawing from the generated student TeX
(source/week-37/editable/src/*.tex), confirms the letters sit at the same
places in the delivered PDFs, rebuilds each drawing as a 3D regular
tetrahedron (using the dashed edges for depth), and decides every printed
"can they match?" question from the geometry.  The rotation group, the
labelling classes, all merges and the guide's keys are recomputed from
scratch.  Nothing from the packet's own checkers is imported.

Run: python3 check_math.py   (writes check_math.out beside itself)
"""
import itertools
import math
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent


def find_repo():
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand and (cand / 'lowell-math-circle-year-2' / 'week-37').is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):
        if (p / 'lowell-math-circle-year-2' / 'week-37').is_dir():
            return p
    sys.exit('repository not found above ' + str(HERE))


REPO = find_repo()
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-37'
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-37' / 'editable' / 'src'
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def note(msg):
    say('NOTE ' + msg)


# ------------------------------------------------------------------ group
# A regular tetrahedron with integer vertices (all edges sqrt 8), centred at 0.
T = np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)], float)


def perm_parity(p):
    p = list(p)
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


SYM = []  # (perm, matrix, det)
for p in itertools.permutations(range(4)):
    # linear map with M T[i] = T[p[i]] (the vertices are centred, so 3 fix it)
    M = np.linalg.solve(T[:3], T[list(p)][:3]).T
    assert np.allclose(M @ T.T, T[list(p)].T)
    assert np.allclose(M @ M.T, np.eye(3))
    SYM.append((p, M, round(np.linalg.det(M))))
ROT = [s for s in SYM if s[2] == 1]
say('== Rotation group of the regular tetrahedron')
check(len(SYM) == 24, 'all 24 vertex permutations are isometries of the regular tetrahedron')
check(len(ROT) == 12, '12 of them are proper rotations (det +1), identity included')
check(all(perm_parity(p) == 1 for p, _, _ in ROT) and
      all(perm_parity(p) == -1 for p, _, d in SYM if d == -1),
      'proper rotations are exactly the even vertex permutations')
types = {}
for p, M, _ in ROT:
    ang = round(math.degrees(math.acos(max(-1, min(1, (np.trace(M) - 1) / 2)))))
    types[ang] = types.get(ang, 0) + 1
say('     rotation angles (deg: count):', dict(sorted(types.items())))
check(types == {0: 1, 120: 8, 180: 3},
      'types: identity 1, 120/240-degree vertex-axis turns 8, 180-degree edge-axis turns 3')
# vertex-axis turns fix exactly one vertex; half-turns fix none and swap two pairs
ok = True
for p, M, _ in ROT:
    fixed = sum(p[i] == i for i in range(4))
    t = round(np.trace(M))
    if (t == 0 and fixed != 1) or (t == -1 and fixed != 0):
        ok = False
check(ok, '120-degree turns fix one vertex (vertex axis); half-turns fix none (edge-midpoint axis)')
dest = {}
for p, _, _ in ROT:
    dest.setdefault(p[0], []).append(p)
check(all(len(v) == 3 for v in dest.values()) and len(dest) == 4,
      '4 destinations for one vertex x 3 placements of the rest = 12')


def orbit(lab, group=ROT):
    """labellings reachable from lab (tuple indexed by vertex) by the group."""
    out = set()
    for p, _, _ in group:
        new = [None] * 4
        for i in range(4):
            new[p[i]] = lab[i]
        out.add(tuple(new))
    return out


def rot_equiv(a, b):
    return tuple(b) in orbit(tuple(a))


labs4 = list(itertools.permutations('ABCD'))
orbits = []
for l in labs4:
    if not any(l in o for o in orbits):
        orbits.append(orbit(l))
check(len(orbits) == 2 and all(len(o) == 12 for o in orbits),
      '24 four-letter labellings fall into 2 rotation classes of 12 (4-5 P6 answer 2)')
refl = [s for s in SYM if s[2] == -1][0]
check(all(orbit(next(iter(orbits[0])), [refl]).pop() in orbits[1] for _ in [0]),
      'a reflection carries one class to the other')
stab_ok = all(sum(1 for p, _, _ in ROT if all(l[p[i]] == l[i] for i in range(4))) == 1
              for l in labs4)
check(stab_ok, 'no non-identity rotation fixes a four-distinct-letter labelling (orbit size 12)')
aabc = set(itertools.permutations('AABC'))
check(len(aabc) == 12 and orbit(next(iter(aabc))) == aabc,
      'all 12 A,A,B,C labellings are one rotation class (K-1 P4 / 2-3 P5 answer: no unmatched pair)')
for ms in ['AABB', 'AAAB', 'AAAA']:
    s = set(itertools.permutations(ms))
    check(orbit(next(iter(s))) == s, f'all {ms} labellings form one class too')

# ------------------------------------------------------------------ drawings
say('')
say('== Tetrahedron drawings in the student TeX')


def parse_tex(path):
    """Return list of pages; each page is a list of figures.
    A figure is dict(kind, pts{label_index: (x, y_up)}, labels[], dashed[(i,j)], solid[(i,j)])."""
    txt = path.read_text()
    body = txt.split('\\begin{document}')[1]
    pages = body.split('\\newpage')
    res = []
    num = r'(-?[0-9.]+)'
    for pg in pages:
        figs, lines, badges = [], [], []
        for ln in pg.splitlines():
            m = re.match(r'\\draw\[(dashed[^\]]*|line width=1\.15pt|line width=1pt|gray!55,line width=\.6pt)\] \(' +
                         num + ',' + num + r'\) -- \(' + num + ',' + num + r'\);', ln)
            if m:
                style = m.group(1)
                kind = 'dashed' if style.startswith('dashed') else ('spoke' if 'gray!55' in style else 'solid')
                lines.append((kind, (float(m.group(2)), float(m.group(3))), (float(m.group(4)), float(m.group(5)))))
                continue
            m = re.match(r'\\node\[circle,draw.*\] at \(' + num + ',' + num + r'\) \{(\w?)\};', ln)
            if m:
                badges.append(((float(m.group(1)), float(m.group(2))), m.group(3)))
                if len(badges) == 4:
                    figs.append((lines, badges))
                    lines, badges = [], []
        res.append(figs)
    return res


def close(a, b, tol=1e-6):
    return abs(a[0] - b[0]) < tol and abs(a[1] - b[1]) < tol


def build_fig(lines, badges):
    pts = [b[0] for b in badges]
    labels = [b[1] for b in badges]

    def idx(q):
        for i, p in enumerate(pts):
            if close(p, q):
                return i
        return None
    dashed = sorted(tuple(sorted((idx(a), idx(b)))) for k, a, b in lines if k == 'dashed')
    solid = sorted(tuple(sorted((idx(a), idx(b)))) for k, a, b in lines if k == 'solid')
    spokes = [l for l in lines if l[0] == 'spoke']
    kind = 'tetra' if dashed else ('view' if spokes else 'other')
    return dict(kind=kind, pts=pts, labels=labels, dashed=dashed, solid=solid, nspoke=len(spokes))


def reconstruct(fig):
    """3D screen-frame coordinates (x right, y up, z toward viewer) of the
    drawn vertices, read as an orthographic view of a regular tetrahedron with
    the dashed hub behind.  Returns (X, info)."""
    P = np.array([(x, -y) for x, y in fig['pts']])          # y up
    Pc = P - P.mean(0)
    Tc = T - T.mean(0)
    M = Pc.T @ np.linalg.pinv(Tc.T)                           # 2x3
    resid = np.abs(M @ Tc.T - Pc.T).max()
    G = M @ M.T
    s2 = (G[0, 0] + G[1, 1]) / 2
    ortho = max(abs(G[0, 0] - s2), abs(G[1, 1] - s2), abs(G[0, 1])) / s2
    s = math.sqrt(s2)
    r, u = M[0] / s, M[1] / s
    n = np.cross(r, u)
    z = s * (Tc @ n)
    X = np.column_stack([Pc, z])
    hub = None
    if fig['dashed']:
        cnt = {}
        for e in fig['dashed']:
            for v in e:
                cnt[v] = cnt.get(v, 0) + 1
        hub = max(cnt, key=cnt.get)
        if z[hub] > min(z) + 1e-9:     # wrong depth branch: mirror depth
            X[:, 2] = -X[:, 2]
    return X, dict(resid=resid, ortho=ortho, hub=hub, edge=s * math.sqrt(8))


def orient(X, order):
    a, b, c, d = (X[i] for i in order)
    return np.sign(np.linalg.det(np.array([b - a, c - a, d - a])))


def match(f1, f2):
    """Can drawing f2's labelled model be reached from f1's by a proper rigid motion?"""
    X1, _ = reconstruct(f1)
    X2, _ = reconstruct(f2)
    o1 = orient(X1, range(4))
    for p in itertools.permutations(range(4)):       # vertex i of f1 -> p[i] of f2
        if all(f1['labels'][i] == f2['labels'][p[i]] for i in range(4)):
            if orient(X2, p) == o1:
                return True
    return False


def describe(fig):
    """labels in the order [apex, lower left, lower right, far vertex]."""
    P = [(x, -y) for x, y in fig['pts']]
    X, info = reconstruct(fig)
    far = info['hub']
    rest = [i for i in range(4) if i != far]
    apex = max(rest, key=lambda i: P[i][1])
    low = sorted([i for i in rest if i != apex], key=lambda i: P[i][0])
    return ''.join(fig['labels'][i] or '_' for i in [apex, low[0], low[1], far])


BANDS = ['k-1', 'grades-2-3', 'grades-4-5']
FIGS = {}
for b in BANDS:
    pages = parse_tex(SRC / f'{b}.tex')
    FIGS[b] = [[build_fig(l, bd) for l, bd in pg] for pg in pages]
    for pn, pg in enumerate(FIGS[b], 1):
        for fn, f in enumerate(pg):
            if f['kind'] == 'tetra':
                X, info = reconstruct(f)
                P = np.array([(x, -y) for x, y in f['pts']])
                hub = info['hub']
                others = [i for i in range(4) if i != hub]
                exp_d = sorted(tuple(sorted((hub, o))) for o in others)
                exp_s = sorted(tuple(sorted(e)) for e in itertools.combinations(others, 2))
                # hub strictly inside the front triangle?
                a, bb, c = (P[i] for i in others)

                def cr(o, p, q):
                    return (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])
                h = P[hub]
                signs = [np.sign(cr(a, bb, h)), np.sign(cr(bb, c, h)), np.sign(cr(c, a, h))]
                inside = len(set(signs)) == 1 and 0 not in signs
                good = (info['resid'] < 1e-9 and info['ortho'] < 1e-9 and f['dashed'] == exp_d and
                        f['solid'] == exp_s and inside)
                check(good, f'{b} p{pn} fig{fn + 1} {describe(f)}: exact orthographic regular tetrahedron'
                      f' (ortho err {info["ortho"]:.1e}), dashed = 3 edges to far vertex, far vertex inside front face')
            elif f['kind'] == 'view':
                say(f'     {b} p{pn} fig{fn + 1}: view-from-A diagram, labels {f["labels"]}')

# all four-distinct-letter drawings: chirality class by [apex,LL,LR,far] reading
say('')
say('== Every drawn model, read as [apex, lower-left, lower-right, far]')
ref = None
for b in BANDS:
    for pn, pg in enumerate(FIGS[b], 1):
        for fn, f in enumerate(pg):
            if f['kind'] == 'tetra' and all(f['labels']):
                d = describe(f)
                say(f'     {b} p{pn} fig{fn + 1}: {d}')


def fig(b, pn, fn):
    return FIGS[b][pn - 1][fn - 1]


say('')
say('== Problem-by-problem decisions from the drawn geometry')
for b in BANDS:
    demo0, demo1 = fig(b, 1, 1), fig(b, 1, 2)
    check(describe(demo0) == 'ABCD' and describe(demo1) == 'ADBC',
          f'{b} p1 turn demo reads ABCD -> ADBC')
    check(match(demo0, demo1), f'{b} p1 "after the turn" is a proper rotation of "before the turn"')
    # it fixes A's position and is a 120-degree turn
    X0, _ = reconstruct(demo0)
    X1, _ = reconstruct(demo1)
    i0 = {l: i for i, l in enumerate(demo0['labels'])}
    i1 = {l: i for i, l in enumerate(demo1['labels'])}
    A0 = np.array([X0[i0[l]] for l in 'ABCD'])
    A1 = np.array([X1[i1[l]] for l in 'ABCD'])
    A0 /= np.linalg.norm(A0[0] - A0[1])
    A1 /= np.linalg.norm(A1[0] - A1[1])
    R = np.linalg.lstsq(A0 - A0.mean(0), A1 - A1.mean(0), rcond=None)[0].T
    ang = math.degrees(math.acos(max(-1, min(1, (np.trace(R) - 1) / 2))))
    check(abs(ang - 120) < 1e-6 and describe(demo0)[0] == describe(demo1)[0] == 'A',
          f'{b} p1 demo: the turn is {ang:.1f} degrees and keeps A at the apex ("turn around A")')
    c0, c1 = fig(b, 1, 3), fig(b, 1, 4)
    check(describe(c0) == describe(c1) == 'ABCD', f'{b} P1 copies are both ABCD (true copies)')

k = 'k-1'
check(describe(fig(k, 2, 1)) == 'ABCD' and describe(fig(k, 2, 2)) == 'ACBD' and not match(fig(k, 2, 1), fig(k, 2, 2)),
      'K-1 P2: ABCD | ACBD mirror pair cannot match (answer no)')
check(describe(fig(k, 3, 1)) == 'ABCC' and describe(fig(k, 3, 2)) == 'ACBC' and match(fig(k, 3, 1), fig(k, 3, 2)),
      'K-1 P3: ABCC | ACBC match (answer yes); drawn letters are D->C on the P2 pair')
check(describe(fig(k, 4, 1)) == 'AABC' and describe(fig(k, 4, 2)) == 'ABAC' and match(fig(k, 4, 1), fig(k, 4, 2)),
      'K-1 P4: printed AABC | ABAC pair matches; no A,A,B,C pair fails (one class)')
g = 'grades-2-3'
check(describe(fig(g, 2, 1)) == 'ABCD' and describe(fig(g, 2, 2)) == 'ACBD' and not match(fig(g, 2, 1), fig(g, 2, 2)),
      '2-3 P2: mirror pair cannot match')
check(describe(fig(g, 3, 1)) == 'ABCC' and describe(fig(g, 3, 2)) == 'ACBC' and match(fig(g, 3, 1), fig(g, 3, 2)),
      '2-3 P4: printed D->C pair matches')
check(describe(fig(g, 4, 1)) == 'AABC' and describe(fig(g, 4, 2)) == 'ABAC' and match(fig(g, 4, 1), fig(g, 4, 2)),
      '2-3 P5: printed AABC | ABAC pair matches')
f = 'grades-4-5'
check(describe(fig(f, 2, 1)) == 'ABCD' and describe(fig(f, 2, 2)) == 'ACBD' and not match(fig(f, 2, 1), fig(f, 2, 2)),
      '4-5 P2: mirror pair cannot match')
check(describe(fig(f, 4, 1)) == 'ABCC' and describe(fig(f, 4, 2)) == 'ACBC' and match(fig(f, 4, 1), fig(f, 4, 2)),
      '4-5 P4: printed D->C pair matches')
check(fig(f, 5, 1)['kind'] == 'tetra' and not any(fig(f, 5, 1)['labels']),
      '4-5 P5: bare frame drawn with four blank vertex circles')


def relabel(fig_, mapping):
    g_ = dict(fig_)
    g_['labels'] = [mapping.get(l, l) for l in fig_['labels']]
    return g_


say('')
say('== Exhaustive testing as a proof (guide p1 "A finite list of unsuccessful turns alone is not an impossibility proof")')
# With both models posed alike and A at the same corner, a matching motion must keep that corner,
# so it is one of the rotations fixing a vertex: list them and test each on the mirror pair.
mirror_l, mirror_r = ('A', 'B', 'C', 'D'), ('A', 'C', 'B', 'D')    # vertex 0 holds A in both
fixA = [p for p, _, _ in ROT if p[0] == 0]
tested = []
for p in fixA:
    new = [None] * 4
    for i in range(4):
        new[p[i]] = mirror_l[i]
    tested.append(tuple(new) == mirror_r)
check(len(fixA) == 3 and not any(tested),
      'once A is aligned only 3 rotations remain (identity and the two turns about A); all 3 fail on the '
      'mirror pair, so trying those three turns is a complete impossibility proof')
check(not any(rot_equiv(mirror_l, q) for q in [mirror_r]) and len(ROT) == 12,
      'equivalently, all 12 rotations fail: an exhaustive finite list does prove impossibility')

say('')
say('== Merges of two letters on the drawn mirror pair (2-3 P4, 4-5 P4, guide p1/p4/p5)')
L0, R0 = fig(g, 2, 1), fig(g, 2, 2)
allm = True
for x, y in itertools.combinations('ABCD', 2):
    for keep, drop in [(x, y), (y, x)]:
        m = match(relabel(L0, {drop: keep}), relabel(R0, {drop: keep}))
        say(f'     merge {x}{y} keeping {keep}: {"match" if m else "NO match"}')
        allm &= m
check(allm, 'all 6 pairwise merges (either retained name) let the mirror pair match')
# the guide's reflection argument: a reflection swapping the two merged vertices is a symmetry
ok = True
for i, j in itertools.combinations(range(4), 2):
    p = list(range(4))
    p[i], p[j] = j, i
    M = [s for s in SYM if list(s[0]) == p][0]
    ok &= (M[2] == -1)
    # its fixed plane contains the other two vertices and the midpoint of ij
    Mm = M[1]
    mid = (T[i] + T[j]) / 2
    others = [v for v in range(4) if v not in (i, j)]
    ok &= all(np.allclose(Mm @ T[v], T[v]) for v in others) and np.allclose(Mm @ mid, mid)
check(ok, 'guide p5: for each vertex pair a reflection swaps them, fixing the other two and the pair midpoint')

say('')
say('== 2-3 P6 (change one A on each AABC model to D) and the guide key')
L5, R5 = fig(g, 4, 1), fig(g, 4, 2)
L5d, R5d = describe(L5), describe(R5)
say('     printed P5 pair:', L5d, R5d)


def change_at(fig_, pos_name):
    """pos_name in apex/LL/LR; change the A at that drawn position to D."""
    P = [(x, -y) for x, y in fig_['pts']]
    _, info = reconstruct(fig_)
    far = info['hub']
    rest = [i for i in range(4) if i != far]
    apex = max(rest, key=lambda i: P[i][1])
    low = sorted([i for i in rest if i != apex], key=lambda i: P[i][0])
    idx = {'top': apex, 'left': low[0], 'right': low[1]}[pos_name]
    assert fig_['labels'][idx] == 'A', (pos_name, fig_['labels'])
    g_ = dict(fig_)
    g_['labels'] = list(fig_['labels'])
    g_['labels'][idx] = 'D'
    return g_


cases = {('top', 'top'): False, ('top', 'right'): True, ('left', 'right'): False, ('left', 'top'): True}
for (a, bpos), claim in cases.items():
    m = match(change_at(L5, a), change_at(R5, bpos))
    check(m == claim, f'2-3 P6: first model {a} A->D, second {bpos} A->D: '
                      f'{"match" if m else "no match"} (guide says {"match" if claim else "no match"})')
check(len({match(change_at(L5, a), change_at(R5, bp)) for a in ['top', 'left'] for bp in ['top', 'right']}) == 2,
      '2-3 P6: both outcomes are reachable (answer yes and yes)')
# any A,A,B,C pair, not only the printed one
ok = True
for l1 in aabc:
    for l2 in aabc:
        outs = set()
        for i in [k_ for k_ in range(4) if l1[k_] == 'A']:
            for j in [k_ for k_ in range(4) if l2[k_] == 'A']:
                a1 = list(l1); a1[i] = 'D'
                a2 = list(l2); a2[j] = 'D'
                outs.add(rot_equiv(a1, a2))
        ok &= outs == {True, False}
check(ok, '2-3 P6: for every A,A,B,C pair a partner might have built, both outcomes are reachable')

say('')
say('== Guide keys on rotations about the A axis')
# K-1 P3 / pretest step 4: one-third turn about the A axis, B front-left -> front-right
Lc, Rc = fig(k, 3, 1), fig(k, 3, 2)
XL, _ = reconstruct(Lc)
XR, _ = reconstruct(Rc)
iA = Lc['labels'].index('A')
axis = XL[iA] - np.mean([XL[i] for i in range(4) if i != iA], 0)
axis /= np.linalg.norm(axis)
found = []
for th in (120, 240):
    t = math.radians(th)
    K = np.array([[0, -axis[2], axis[1]], [axis[2], 0, -axis[0]], [-axis[1], axis[0], 0]])
    Rm = np.eye(3) + math.sin(t) * K + (1 - math.cos(t)) * K @ K
    c = XL.mean(0)
    Y = (Rm @ (XL - c).T).T + c
    # labels at the rotated positions vs the right model at the same places (same pose)
    newlab = {}
    for i in range(4):
        j = min(range(4), key=lambda j: np.linalg.norm(Y[i] - (XR[j] - XR.mean(0) + c)))
        newlab[j] = Lc['labels'][i]
    if all(newlab[j] == Rc['labels'][j] for j in range(4)):
        found.append(th)
check(len(found) == 1, f'K-1 P3 key / pretest step 4: exactly one of the two one-third turns about the A axis '
                       f'turns ABCC into ACBC (found {found}); both C vertices then match')

say('')
say('== 4-5 P3 view from A')
model = fig(f, 3, 1)
view = fig(f, 3, 2)
blank1, blank2 = fig(f, 3, 3), fig(f, 3, 4)
check(describe(model) == 'ABCD', '4-5 P3 model drawing is ABCD')
X, _ = reconstruct(model)
lab = model['labels']
iA = lab.index('A')
cen = np.mean([X[i] for i in range(4) if i != iA], 0)
u = X[iA] - cen
u /= np.linalg.norm(u)                # points toward the eye (A nearest)


def view_orient(X, labels):
    q = {labels[i]: X[i] - np.dot(X[i], u) * u for i in range(4) if labels[i] != 'A'}
    return np.sign(np.dot(np.cross(q['C'] - q['B'], q['D'] - q['B']), u))   # +1 = B,C,D anticlockwise


o_model = view_orient(X, lab)
Xm = X * np.array([-1, 1, 1])                       # mirror in a vertical plane, labels kept
o_mirror = view_orient(Xm, lab)
Pv = {l: (x, -y) for (x, y), l in zip(view['pts'], view['labels'])}
cr = (Pv['C'][0] - Pv['B'][0]) * (Pv['D'][1] - Pv['B'][1]) - (Pv['C'][1] - Pv['B'][1]) * (Pv['D'][0] - Pv['B'][0])
o_print = np.sign(cr)
say(f'     looking from A: model B,C,D {"anticlockwise" if o_model > 0 else "clockwise"};'
    f' mirror {"anticlockwise" if o_mirror > 0 else "clockwise"}; printed view {"anticlockwise" if o_print > 0 else "clockwise"}')
check(o_model == o_print and o_mirror == -o_model,
      '4-5 P3: printed view from A (B lower left, C lower right, D top) has the true handedness;'
      ' the mirror reverses it (guide: "B, D, C counterclockwise")')
# the printed view's placement also agrees: D away from the viewer appears at the top
# when the eye rises above A, B nearer-left, C nearer-right
check(Pv['B'][1] < Pv['D'][1] and Pv['C'][1] < Pv['D'][1] and Pv['B'][0] < Pv['C'][0],
      '4-5 P3 view: D top, B lower-left, C lower-right as the README states')
vs = [np.array(Pv[l]) for l in 'BCD']
sides = sorted(np.linalg.norm(vs[i] - vs[(i + 1) % 3]) for i in range(3))
cent = np.mean(vs, 0)
check(sides[2] / sides[0] < 1.02 and np.allclose(cent, Pv['A'], atol=1e-9),
      f'4-5 P3 view triangle sides {", ".join(f"{s:.3f}" for s in sides)} cm: equilateral within '
      f'{100 * (sides[2] / sides[0] - 1):.1f}% and A at its centre')
check(blank1['labels'] == ['', '', '', 'A'] and blank2['labels'] == ['', '', '', 'A'],
      '4-5 P3: two blank view diagrams with only A filled')

# ------------------------------------------------------------------ materials
say('')
say('== Markers needed for the merges (guide p2: "category markers A, B, C, D with duplicate As and Cs")')
dups = set('AC')
for x, y in itertools.combinations('ABCD', 2):
    ways = [keep for keep in (x, y) if keep in dups]
    say(f'     merge {x}{y}: extra marker needed of {x} or {y}; available with duplicate As/Cs: '
        f'{"yes (" + "/".join(ways) + ")" if ways else "NO"}')
no_way = [x + y for x, y in itertools.combinations('ABCD', 2) if x not in dups and y not in dups]
check(no_way == ['BD'], f'only the B-D merge cannot be built from duplicate As and Cs (found {no_way})')
note('the B-D merge (listed in the guide key for 2-3 P4 and required by "every choice" in 4-5 P4) '
     'needs a duplicate B or D, or removing both markers so the two corners are equally blank')

say('')
say('== 4-5 P6 if "four different letters" may be any letters')
for n in (4, 5, 26):
    say(f'     letters chosen from {n}: {2 * math.comb(n, 4)} classes')
note('the intended answer 2 assumes the four letters are A, B, C, D (the kit letters)')

# ------------------------------------------------------------------ PDFs
say('')
say('== Delivered PDFs: letters at the TeX positions, problem text, numbering')
CM = 72 / 2.54


def words(pdf):
    xml = subprocess.run(['pdftotext', '-bbox', str(pdf), '-'], capture_output=True, text=True).stdout
    pages = xml.split('<page ')[1:]
    out = []
    for pg in pages:
        ws = []
        for m in re.finditer(r'xMin="([0-9.]+)" yMin="([0-9.]+)" xMax="([0-9.]+)" yMax="([0-9.]+)">([^<]*)<', pg):
            ws.append(((float(m.group(1)) + float(m.group(3))) / 2, (float(m.group(2)) + float(m.group(4))) / 2,
                       m.group(5)))
        out.append(ws)
    return out


for b in BANDS:
    pdf = WEEK / f'week-37-{b}.pdf'
    W = words(pdf)
    check(len(W) == len(FIGS[b]), f'{b}: PDF has {len(W)} pages, TeX {len(FIGS[b])}')
    bad = 0
    total = 0
    for pn, (pg, ws) in enumerate(zip(FIGS[b], W), 1):
        for fg in pg:
            for (x, y), l in zip(fg['pts'], fg['labels']):
                if not l:
                    continue
                total += 1
                px, py = (x + 1.5) * CM, (y + 1.5) * CM
                near = [w for w in ws if abs(w[0] - px) < 6 and abs(w[1] - py) < 6]
                if not near or near[0][2] != l:
                    bad += 1
    check(bad == 0, f'{b}: all {total} printed vertex letters sit at their TeX coordinates in the PDF')
    txt = subprocess.run(['pdftotext', str(pdf), '-'], capture_output=True, text=True).stdout
    nums = [int(n) for n in re.findall(r'Problem (\d+):', txt)]
    check(nums == list(range(1, len(nums) + 1)), f'{b}: problems numbered 1..{len(nums)} consecutively')
    flat = ' '.join(txt.split())
    tex = (SRC / f'{b}.tex').read_text()
    probs = re.findall(r'\\textbf\{Problem (\d+):\} (.*?)\};', tex)
    for n, t in probs:
        t = t.replace('--', '–')
        check(' '.join(t.split()) in flat.replace('- ', '-'), f'{b} P{n}: TeX text appears verbatim in the PDF')

gtxt = ' '.join(subprocess.run(['pdftotext', str(WEEK / 'week-37-facilitator.pdf'), '-'],
                               capture_output=True, text=True).stdout.split())
for phrase in ['exactly 12 proper rotational symmetries', 'eight 120°/240° vertex-axis rotations',
               'three 180° opposite-edge-axis rotations', 'two rotational classes of 12',
               'all assignments of the multiset A, A, B, C are rotationally equivalent',
               'AB, AC, AD, BC, BD and CD', 'The mirror reads B, D, C counterclockwise',
               '1 + 8 + 3 = 12', '4 × 3 = 12', 'duplicate As and Cs', '5 / 6 / 6 problems',
               'Change the top A on both to D: the new pair does not match',
               'Change the top A on the first and the front-right A on the second: it matches']:
    check(phrase in gtxt, f'guide text contains: "{phrase}"')
counts = {b: len(re.findall(r'Problem \d+:', subprocess.run(['pdftotext', str(WEEK / f'week-37-{b}.pdf'), '-'],
                                                             capture_output=True, text=True).stdout)) for b in BANDS}
check([counts[b] for b in BANDS] == [5, 6, 6], f'problem counts {counts} match the guide status line 5 / 6 / 6')

say('')
say(f'{len(FAIL)} failure(s)')
(HERE / 'check_math.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
