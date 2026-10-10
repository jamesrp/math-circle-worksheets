"""Small brute-force helpers shared by the diagram checks (no stack rule, no packet code)."""
import itertools


def all_matchings(pts):
    pts = list(pts)
    if not pts:
        yield ()
        return
    a = pts[0]
    for i in range(1, len(pts)):
        for m in all_matchings(pts[1:i] + pts[i + 1:]):
            yield tuple(sorted(((a, pts[i]),) + m))


def noncrossing(m):
    return not any(a < c < b < d or c < a < d < b for (a, b), (c, d) in itertools.combinations(m, 2))


def nc_matchings(N):
    return [] if N % 2 else [m for m in all_matchings(range(1, N + 1)) if noncrossing(m)]


def code(m, N):
    first = {min(e) for e in m}
    return ''.join('U' if i in first else 'D' for i in range(1, N + 1))


def heights(w):
    h = [0]
    for c in w:
        h.append(h[-1] + (1 if c == 'U' else -1))
    return h


def is_dyck(w):
    h = heights(w)
    return min(h) >= 0 and h[-1] == 0


def pairings_with_code(w):
    return [m for m in nc_matchings(len(w)) if code(m, len(w)) == w]


def fmt(m):
    return '|'.join(f'{a}{b}' if b < 10 else f'{a}-{b}' for a, b in sorted(m))
