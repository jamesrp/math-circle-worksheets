"""Logical grader for tower-city puzzles (outside clues only, optional givens)."""
from itertools import permutations
from towers import view

def lines(n):
    """Each line: (list of cells from the 'first' end, key at first end, key at other end)."""
    L = []
    for r in range(n):
        L.append(([(r, c) for c in range(n)], ('L', r), ('R', r)))
    for c in range(n):
        L.append(([(r, c) for r in range(n)], ('T', c), ('B', c)))
    return L

def grade(n, clues, givens=None, verbose=False):
    givens = givens or {}
    cand = {(r, c): set(range(1, n + 1)) for r in range(n) for c in range(n)}
    for k, v in givens.items():
        cand[k] = {v}
    LN = lines(n)
    level_used = 0
    steps = {1: 0, 2: 0, 3: 0}
    # Rule 1: edge rules from clues (distance rule incl. clue 1 and clue n)
    for cells, k1, k2 in LN:
        for key, seq in ((k1, cells), (k2, cells[::-1])):
            if key in clues:
                c = clues[key]
                for i, cell in enumerate(seq):
                    mx = n - c + 1 + i
                    cand[cell] = {h for h in cand[cell] if h <= mx}
                if c == 1:
                    cand[seq[0]] &= {n}
                if c == n:
                    for i, cell in enumerate(seq):
                        cand[cell] &= {i + 1}
    level_used = 1 if clues else 0
    def singles():
        changed = False
        for cells, _, _ in LN:
            for cell in cells:
                if len(cand[cell]) == 1:
                    v = next(iter(cand[cell]))
                    for o in cells:
                        if o != cell and v in cand[o]:
                            cand[o].discard(v); changed = True
            for v in range(1, n + 1):
                places = [cell for cell in cells if v in cand[cell]]
                if len(places) == 1 and len(cand[places[0]]) > 1:
                    cand[places[0]] = {v}; changed = True
        return changed
    def line_enum():
        changed = False
        for cells, k1, k2 in LN:
            ok = []
            for p in permutations(range(1, n + 1)):
                if all(p[i] in cand[cells[i]] for i in range(n)):
                    if k1 in clues and view(p) != clues[k1]: continue
                    if k2 in clues and view(p[::-1]) != clues[k2]: continue
                    ok.append(p)
            for i, cell in enumerate(cells):
                new = {p[i] for p in ok}
                if new != cand[cell]:
                    cand[cell] = new; changed = True
            if changed:
                return True
        return changed
    while True:
        if any(len(s) == 0 for s in cand.values()):
            return ('contradiction', level_used, steps)
        if all(len(s) == 1 for s in cand.values()):
            sol = tuple(tuple(next(iter(cand[(r, c)])) for c in range(n)) for r in range(n))
            return ('solved', level_used, steps, sol)
        if singles():
            level_used = max(level_used, 2); steps[2] += 1; continue
        if line_enum():
            level_used = max(level_used, 3); steps[3] += 1; continue
        return ('stuck', level_used, steps, {k: sorted(v) for k, v in cand.items()})
