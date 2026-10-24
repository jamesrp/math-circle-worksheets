"""Generate every diagram for the three packets and check every answer.

Run from this folder:  python3 gen.py   (writes figs/*.tex, prints the answers)
"""
import math, os
from itertools import permutations
from figs import (tournament, square, tri, ngon, lineup_boxes, lineup_row_fig,
                  newcomer, newcomer_boxes, arrowhead, f)
import tourn as T

os.makedirs('figs', exist_ok=True)


def save(name, code):
    with open(f'figs/{name}.tex', 'w') as fh:
        fh.write(code + '\n')


def parse(spec, names):
    """'AB CD' -> [('A','B'),('C','D')]; animal specs use 'cat>dog'."""
    out = []
    for tok in spec.split():
        if '>' in tok:
            a, b = tok.split('>')
        else:
            a, b = tok[0], tok[1]
        out.append((a, b))
    # completeness check
    pairs = {frozenset(e) for e in out}
    assert len(pairs) == len(out), spec
    assert len(out) == len(names) * (len(names) - 1) // 2, spec
    for a, b in out:
        assert a in names and b in names
    return out


def analyse(names, edges):
    idx = {c: i for i, c in enumerate(names)}
    n = len(names)
    beat = frozenset((idx[a], idx[b]) for a, b in edges)
    lus = [' '.join(names[i] for i in p) for p in T.lineups(n, beat)]
    ks = [names[i] for i in T.kings(n, beat)]
    w = {names[i]: x for i, x in enumerate(T.wins(n, beat))}
    return lus, ks, w


def report(title, names, edges, want_lineups=None, want_kings=None, alpha_ok=True):
    lus, ks, w = analyse(names, edges)
    print(f"{title}: wins {w}; {len(lus)} line-up(s): {lus}; kings {ks}")
    if want_lineups is not None:
        assert len(lus) == want_lineups, (title, len(lus))
    if want_kings is not None:
        assert len(ks) == want_kings, (title, ks)
    if not alpha_ok:
        assert ' '.join(sorted(names)) not in lus, f"{title}: alphabetical order is a line-up"
    return lus, ks, w


def places(results, names='ABCDE'):
    """Where X can join the line-up names[0]->...->names[-1]. results[i]=='W' if X beat names[i]."""
    out = []
    n = len(names)
    for i in range(n + 1):
        left_ok = i == 0 or results[i - 1] == 'L'
        right_ok = i == n or results[i] == 'W'
        if left_ok and right_ok:
            out.append(i)
    return out


def place_names(pl, names='ABCDE'):
    out = []
    for i in pl:
        if i == 0:
            out.append(f'front (before {names[0]})')
        elif i == len(names):
            out.append(f'back (after {names[-1]})')
        else:
            out.append(f'{names[i-1]}-{names[i]}')
    return out


# Insertion lemma, checked for every result pattern on 1..7 players.
from itertools import product
for n in range(1, 8):
    for res in product('WL', repeat=n):
        assert places(res, names='ABCDEFG'[:n]), res

ANIMALS = ['cat', 'dog', 'bear', 'rabbit', 'frog', 'pig']

# ---------------------------------------------------------------- K-1
print("\n===== K-1 =====")
# Rules example (three animals, a ranking) and its line-up.
ex_names = ['dog', 'cat', 'bear']
ex_edges = parse('cat>dog dog>bear cat>bear', ex_names)
report('K1 rules example', ex_names, ex_edges, want_lineups=1)
save('k1_rules_tri', tournament(tri(['dog', 'cat', 'bear'], 2.45), ex_edges, r=0.52, kind='face',
                                L=0.34, W=0.29, face_scale=0.49))
save('k1_rules_row', lineup_row_fig(['cat', 'dog', 'bear'], r=0.52, spacing=1.6, L=0.32, W=0.27,
                                    face_scale=0.49))

# Problem 1: the board.
def board(names, d=7.4, sq=4.0, lane=2.3, face_scale=1.62):
    # Centres 14.8 cm apart and 4 cm animal squares: side lanes 10.8 cm, diagonal lanes 15.3 cm,
    # both 2.3 cm wide, so a 2 x 10 cm arrow card fits inside every lane.
    pos = square(names, 2 * d, origin=(-d, -d))
    out = [r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    pairs = [(a, b) for i, a in enumerate(names) for b in names[i + 1:]]
    h = sq / 2
    for a, b in pairs:
        (ax, ay), (bx, by) = pos[a], pos[b]
        dx, dy = bx - ax, by - ay
        D = math.hypot(dx, dy)
        ux, uy = dx / D, dy / D
        # distance from a square's centre to its edge along (ux,uy)
        e = h / max(abs(ux), abs(uy))
        L = D - 2 * e
        ang = math.degrees(math.atan2(dy, dx))
        cx, cy = (ax + bx) / 2, (ay + by) / 2
        out.append(f"\\draw[gray!70, dashed, line width=0.9pt, rotate around={{{f(ang)}:({f(cx)},{f(cy)})}}] "
                   f"({f(cx - L / 2)},{f(cy - lane / 2)}) rectangle ({f(cx + L / 2)},{f(cy + lane / 2)});")
    for a in names:
        x, y = pos[a]
        out.append(f"\\filldraw[fill=white, line width=1.2pt, rounded corners=3pt] ({f(x - h)},{f(y - h)}) rectangle ({f(x + h)},{f(y + h)});")
        out.append(f"\\pic[scale={f(face_scale)}] at ({f(x)},{f(y)}) {{{a}}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)

save('k1_board', board(['cat', 'dog', 'bear', 'rabbit']))


def join_mat(n, face, spot=1.3, gap=0.75, depth=4.0, lane=0.3, newcard=1.75, spread=0.38,
             L=0.3, W=0.26):
    """Picture of the joining layout: a blank line-up of n cards, the newcomer's card
    below, and a dashed arrow-card lane from the newcomer to every card."""
    out = [r"\begin{tikzpicture}[x=1cm,y=1cm]"]
    step = spot + gap
    h = spot / 2
    cents = [(i * step + h, h) for i in range(n)]
    mid = ((n - 1) * step + spot) / 2
    X = (mid, -depth)
    hn = newcard / 2
    for i, (cx, cy) in enumerate(cents):
        p0 = (cx, 0)                                            # bottom of the line-up card
        p1 = (mid + (i - (n - 1) / 2) * spread, X[1] + hn)      # top edge of the newcomer card
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        D = math.hypot(dx, dy)
        Ln = D - 0.3
        ang = math.degrees(math.atan2(dy, dx))
        mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
        out.append(f"\\draw[gray!70, dashed, line width=0.8pt, rotate around={{{f(ang)}:({f(mx)},{f(my)})}}] "
                   f"({f(mx - Ln / 2)},{f(my - lane / 2)}) rectangle ({f(mx + Ln / 2)},{f(my + lane / 2)});")
    for i, (cx, cy) in enumerate(cents):
        out.append(f"\\draw[line width=1.0pt, rounded corners=2pt] ({f(cx - h)},{f(cy - h)}) rectangle ({f(cx + h)},{f(cy + h)});")
        if i < n - 1:
            a0, a1 = cx + h + 0.1, cx + h + gap - 0.1
            out.append(f"\\draw[line width=1.0pt] ({f(a0)},{f(cy)}) -- ({f(a1 - L * 0.6)},{f(cy)});")
            out.append(arrowhead(((a1 - L / 2), cy), (1, 0), L, W))
    out.append(f"\\draw[line width=1.0pt, rounded corners=2pt] ({f(X[0] - hn)},{f(X[1] - hn)}) rectangle ({f(X[0] + hn)},{f(X[1] + hn)});")
    out.append(f"\\pic[scale={f(newcard * 0.4)}] at ({f(X[0])},{f(X[1])}) {{{face}}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


save('k1_join4', join_mat(4, 'frog'))
save('k1_join5', join_mat(5, 'pig'))
# Recording rows for found line-ups (initials or small marks).
save('boxes3k', lineup_boxes(3, box=1.0, gap=0.5, L=0.28, W=0.25))
save('boxes4k', lineup_boxes(4, box=1.0, gap=0.5, L=0.28, W=0.25))

# Problem 2: three animals, how many line-ups.
p2a_names = ['rabbit', 'pig', 'frog']
p2a = parse('frog>rabbit frog>pig pig>rabbit', p2a_names)
report('K1 P2 left (ranking)', p2a_names, p2a, want_lineups=1)
p2b_names = ['bear', 'cat', 'dog']
p2b = parse('dog>cat cat>bear bear>dog', p2b_names)
report('K1 P2 right (circle)', p2b_names, p2b, want_lineups=3)
for nm, names, edges in [('k1_p2a', p2a_names, p2a), ('k1_p2b', p2b_names, p2b)]:
    save(nm, tournament(tri(names, 4.2), edges, r=1.0, kind='face', L=0.5, W=0.42, face_scale=0.93,
                        lw='1.4pt'))

# Problem 3: four printed tournaments, line up each.
k1p3 = [
    ('k1_p3a', ['dog', 'frog', 'pig', 'cat'], 'pig>cat pig>dog pig>frog cat>dog cat>frog dog>frog', 1),
    ('k1_p3b', ['frog', 'rabbit', 'cat', 'bear'], 'rabbit>bear rabbit>frog rabbit>cat bear>frog frog>cat cat>bear', 3),
    ('k1_p3c', ['pig', 'dog', 'rabbit', 'cat'], 'pig>dog cat>dog rabbit>dog pig>cat cat>rabbit rabbit>pig', 3),
    ('k1_p3d', ['dog', 'rabbit', 'bear', 'frog'], 'bear>dog dog>frog frog>rabbit rabbit>bear bear>frog dog>rabbit', 5),
]
for nm, names, spec, want in k1p3:
    e = parse(spec, names)
    report(f'K1 P3 {nm}', names, e, want_lineups=want)
    save(nm, tournament(square(names, 4.6), e, r=1.0, kind='face', L=0.5, W=0.42, face_scale=0.93,
                        lw='1.4pt'))

# Problems 4 and 5: blank copies of the board animals for recording.
save('k1_blank', tournament(square(['cat', 'dog', 'bear', 'rabbit'], 5.0), None, r=0.95, kind='face',
                            arrows=False, face_scale=0.88, lw='1.4pt'))
# Equal wins: the cat, dog and bear alone, and all four animals.
save('k1_eq3', tournament(tri(['cat', 'dog', 'bear'], 4.4), None, r=0.9, kind='face',
                          arrows=False, face_scale=0.83, lw='1.4pt'))
save('k1_eq4', tournament(square(['cat', 'dog', 'bear', 'rabbit'], 4.4), None, r=0.9, kind='face',
                          arrows=False, face_scale=0.83, lw='1.4pt'))
# answers for P4-P7 (all tournaments on four players)
counts = {}
for t in T.all_tournaments(4):
    counts.setdefault(len(T.lineups(4, t)), 0)
    counts[len(T.lineups(4, t))] += 1
print('K1 P4/P5/P6: line-up counts over all 64 four-animal boards:', counts)
eq3 = [t for t in T.all_tournaments(3) if len(set(T.wins(3, t))) == 1]
eq4 = [t for t in T.all_tournaments(4) if len(set(T.wins(4, t))) == 1]
two_unbeaten = [t for t in T.all_tournaments(4) if T.wins(4, t).count(3) >= 2]
print(f'K1 P7: equal wins with three animals: {len(eq3)} ways; with four: {len(eq4)}; two unbeaten: {len(two_unbeaten)}')
assert eq3 and not eq4 and not two_unbeaten
# Problem 8: which animals can be first in a line-up?
k1p8 = [
    ('k1_p8a', ['cat', 'rabbit', 'frog', 'dog'], 'dog>cat dog>rabbit dog>frog cat>rabbit rabbit>frog frog>cat', 1),
    ('k1_p8b', ['pig', 'bear', 'cat', 'rabbit'], 'pig>bear rabbit>bear cat>bear pig>rabbit rabbit>cat cat>pig', 3),
    ('k1_p8c', ['frog', 'pig', 'dog', 'bear'], 'frog>pig pig>dog dog>bear bear>frog frog>dog pig>bear', 4),
]
for nm, names, spec, want_first in k1p8:
    e = parse(spec, names)
    lus, ks, w = report(f'K1 P8 {nm}', names, e)
    firsts = sorted({l.split()[0] for l in lus})
    print(f'   animals that can be first: {firsts}')
    assert len(firsts) == want_first
    save(nm, tournament(square(names, 3.55), e, r=0.92, kind='face', L=0.46, W=0.4, face_scale=0.85,
                        lw='1.3pt'))

# ---------------------------------------------------------------- Grades 2-3
print("\n===== Grades 2-3 =====")
up_ex_names = ['A', 'B', 'C']
up_ex = parse('BA AC BC', up_ex_names)
report('Upper rules example', up_ex_names, up_ex, want_lineups=1)
save('up_rules_tri', tournament(tri(['A', 'B', 'C'], 2.5), up_ex, r=0.52, L=0.38, W=0.32, font=r'\large'))
save('up_rules_row', lineup_row_fig(['B', 'A', 'C'], r=0.52, spacing=1.7, L=0.36, W=0.3))

# Problem 1: three blank recording pictures with the four animals, plus a line-up row.
save('g23_rec4', tournament(square(['cat', 'dog', 'bear', 'rabbit'], 4.0), None, r=0.78, kind='face',
                            arrows=False, face_scale=0.72, lw='1.1pt'))
save('boxes4', lineup_boxes(4, box=1.15, gap=0.62, L=0.34, W=0.3))
save('boxes5', lineup_boxes(5, box=1.15, gap=0.62, L=0.34, W=0.3))
save('boxes6', lineup_boxes(6, box=1.15, gap=0.62, L=0.34, W=0.3))
save('boxes4s', lineup_boxes(4, box=1.0, gap=0.55, L=0.3, W=0.26))
save('boxes5s', lineup_boxes(5, box=1.0, gap=0.55, L=0.3, W=0.26))
save('boxes6s', lineup_boxes(6, box=1.0, gap=0.55, L=0.3, W=0.26))
# Problem 3: copy the line-up above the newcomer and draw the newcomer's games.
save('g23_p3_frog', newcomer_boxes(4, 'frog'))
save('g23_p3_pig', newcomer_boxes(5, 'pig'))

# Problem 2: find a line-up; which have only one?
g23p2 = [
    ('g23_p2a', 'ABCD', 'AC CB BD DA AB CD', 5),
    ('g23_p2b', 'ABCD', 'DB DA DC BA BC AC', 1),
    ('g23_p2c', 'ABCDE', ' '.join(a + b for i, a in enumerate('CEADB') for b in 'CEADB'[i + 1:]), 1),
    ('g23_p2d', 'ABCDE', 'BA BC BD BE EA EC ED CD DA AC', 3),
]
for nm, names, spec, want in g23p2:
    e = parse(spec, list(names))
    report(f'2-3 P2 {nm}', list(names), e, want_lineups=want, alpha_ok=False)
    pos = square(list(names), 4.4) if len(names) == 4 else ngon(list(names), 2.8)
    save(nm, tournament(pos, e, r=0.75, font=r'\Large'))

# Problem 4: newcomer X.
g23p4 = ['LLLWW', 'LLLLL', 'LWLLL', 'WLLWL']
for k, res in enumerate(g23p4):
    pl = places(res)
    print(f'2-3 P4 case {k+1} X results vs A-E {res}: X fits at {place_names(pl)}')
    save(f'g23_p4_{k}', newcomer(res, r=0.48, spacing=1.6, depth=2.6, side=0.9))
save('g23_p5_blank', newcomer('LLLLL', r=0.48, spacing=1.6, depth=2.6, arrows=False, top_space=0.3,
                              side=0.9))
save('hex_blank', tournament(ngon(list('ABCDEF'), 2.85), None, r=0.52, arrows=False, font=r'\large'))

# Problem 7: kings. A small example of the definition: P->Q->R->P, the path P->Q->R shaded.
kex_names = ['P', 'Q', 'R']
kex = parse('PQ QR RP', kex_names)
report('King example (not a task)', kex_names, kex, want_kings=3)
kpos = tri(['P', 'R', 'Q'], 2.5)
def _trim(a, b, r):
    (ax, ay), (bx, by) = kpos[a], kpos[b]
    dx, dy = bx - ax, by - ay
    D = math.hypot(dx, dy)
    return (ax + dx / D * r, ay + dy / D * r), (bx - dx / D * r, by - dy / D * r)
under = []
for a, b in [('P', 'Q'), ('Q', 'R')]:
    (sx, sy), (ex2, ey2) = _trim(a, b, 0.46)
    under.append(f"\\draw[gray!35, line width=7pt, line cap=round] ({f(sx)},{f(sy)}) -- ({f(ex2)},{f(ey2)});")
save('king_example', tournament(kpos, kex, r=0.46, L=0.36, W=0.3, font=r'\large', under=under))

g23p7 = [
    ('g23_p7a', 'ABCD', 'CB AB DB CA AD DC', 3),
    ('g23_p7b', 'ABCD', 'CA CB CD AB BD DA', 1),
    ('g23_p7c', 'ABCDE', 'DA DE DB AE AC EB EC BA CD CB', 4),
    ('g23_p7d', 'ABCDE', 'AC AE CE CB EB ED BD BA DA DC', 5),
]
for nm, names, spec, want in g23p7:
    e = parse(spec, list(names))
    report(f'2-3 P7 {nm}', list(names), e, want_kings=want)
    pos = square(list(names), 5.0) if len(names) == 4 else ngon(list(names), 3.2)
    save(nm, tournament(pos, e, r=0.75, font=r'\Large'))
kc4 = sorted({len(T.kings(4, t)) for t in T.all_tournaments(4)})
kc5 = sorted({len(T.kings(5, t)) for t in T.all_tournaments(5)})
print('2-3 P8 / 4-5 P7: king counts possible with 4 players', kc4, 'with 5 players', kc5)
save('sq_blank', tournament(square(list('ABCD'), 3.0), None, r=0.5, arrows=False, font=r'\large'))
save('sq_blank_s', tournament(square(list('ABCD'), 2.7), None, r=0.45, arrows=False, font=r'\normalsize'))
save('pent_blank_s', tournament(ngon(list('ABCDE'), 1.75), None, r=0.45, arrows=False, font=r'\normalsize'))
# 4-5 Problem 7: larger blank pictures, more of them than there are answers.
save('sq_blank_m', tournament(square(list('ABCD'), 3.0), None, r=0.5, arrows=False, font=r'\large'))
save('pent_blank_m', tournament(ngon(list('ABCDE'), 2.25), None, r=0.5, arrows=False, font=r'\large'))
# 4-5 Problem 11: blank dots, for building a tournament and writing each player's win count in its dot.
save('sq_dots', tournament(square(list('ABCD'), 2.6), None, r=0.42, arrows=False,
                           labels={c: '' for c in 'ABCD'}))
save('pent_dots', tournament(ngon(list('ABCDE'), 1.9), None, r=0.42, arrows=False,
                             labels={c: '' for c in 'ABCDE'}))

# ---------------------------------------------------------------- Grades 4-5
print("\n===== Grades 4-5 =====")
save('g45_rec6', tournament(ngon(['cat', 'dog', 'bear', 'rabbit', 'frog', 'pig'], 3.05), None, r=0.74,
                            kind='face', arrows=False, face_scale=0.69, lw='1.1pt'))
g45p2 = [
    ('g45_p2a', 'ABCD', 'BA AD DC CB BD AC', 5),
    ('g45_p2b', 'ABCD', 'BA CA DA BD DC CB', 3),
    ('g45_p2c', 'ABCD', 'CA CD CB AD AB DB', 1),
    ('g45_p2d', 'ABCD', 'DA DB DC AC CB BA', 3),
]
for nm, names, spec, want in g45p2:
    e = parse(spec, list(names))
    report(f'4-5 P2 {nm}', list(names), e, want_lineups=want, alpha_ok=False)
    save(nm, tournament(square(list(names), 3.15), e, r=0.6, L=0.4, W=0.34, font=r'\Large'))
g45p3 = ['LLWLW', 'LLLLW', 'WWLLL']
for k, res in enumerate(g45p3):
    pl = places(res)
    print(f'4-5 P3 case {k+1} X results vs A-E {res}: X fits at {place_names(pl)}')
    save(f'g45_p3_{k}', newcomer(res, r=0.48, spacing=1.6, depth=2.6, side=0.9))
g45p5 = [
    ('g45_p5a', 'ABCDE', 'CA AD DC AE CE DE AB CB DB EB', 3),
    ('g45_p5b', 'ABCDE', 'CE CB CA EB ED BA BD AE DC DA', 4),
    ('g45_p5c', 'ABCDEF', 'AB AC AD BC BD BE CD CF DE DF EA EC EF FA FB', 6),
    ('g45_p5d', 'ABCDEF', 'DA DB DC DE AB AC AE AF BC BE BF CE CF EF FD', 3),
]
for nm, names, spec, want in g45p5:
    e = parse(spec, list(names))
    lus, ks, w = report(f'4-5 P5 {nm}', list(names), e, want_kings=want)
    pos = ngon(list(names), 2.75 if len(names) == 5 else 3.0)
    save(nm, tournament(pos, e, r=0.72, font=r'\Large'))

# Problems 9 and 10: win counts written in the dots.
def build(scores):
    n = len(scores)
    for t in T.all_tournaments(n):
        if T.wins(n, t) == list(scores):
            return t
    return None

g45p9 = [(1, 3, 1, 4, 1), (0, 3, 4, 0, 3), (2, 2, 2, 2, 2), (4, 1, 0, 4, 1), (3, 0, 3, 1, 3)]
g45p10 = [(4, 1, 4, 1, 4, 1), (0, 4, 1, 5, 1, 4), (2, 3, 2, 3, 2, 3), (5, 0, 2, 4, 2, 2)]
for tag, lists in [('4-5 P9', g45p9), ('4-5 P10', g45p10)]:
    for k, sc in enumerate(lists):
        n = len(sc)
        ok = T.landau_ok(sc)
        t = build(sc)
        assert (t is not None) == ok
        names = 'ABCDEF'[:n]
        ex = ' '.join(names[a] + names[b] for a, b in sorted(t)) if t else '-'
        s = sorted(sc)
        fail = [kk for kk in range(1, n + 1) if sum(s[:kk]) < kk * (kk - 1) // 2]
        print(f"{tag} list {k+1} {sc}: {'possible, e.g. ' + ex if ok else 'impossible; fails at k=' + str(fail)}")
        labels = {nm: str(x) for nm, x in zip(names, sc)}
        pos = ngon(list(names), 2.25 if n == 5 else 2.45)
        save(f"{'g45_p9' if n == 5 else 'g45_p10'}_{k}",
             tournament(pos, None, r=0.55, arrows=False, labels=labels, font=r'\Large'))

for n in (4, 5, 6):
    from itertools import combinations_with_replacement as cwr
    ok = [c for c in cwr(range(n), n) if T.landau_ok(c)]
    print(f'4-5 P11: {len(ok)} possible sorted win lists for {n} players: {ok if n < 6 else "..."}')
print('4-5 P13: line-up counts possible with 4 players:', sorted(counts))
