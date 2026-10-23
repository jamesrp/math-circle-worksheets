"""Week 20 answer checks: solve every board with fixed values exactly.

The old student builder (build_packets.py, archived in
../../archive-before-problem-files-2026-10-23/) solved each board with sympy as it drew it.
figures.py now records those boards in CHECKS while a packet is built; solve() finds the
unique filling with exact fractions (Gaussian elimination) and line() writes it as the
old builder did, so checked-values.txt keeps its format. A board whose circles are not
determined would raise an error here.
"""
from fractions import Fraction


def solve(vals, names, edges):
    """The circle values of one board: each circle is the average of its neighbours."""
    unknown = [n for n in names if n not in vals]
    adj = {n: [b if a == n else a for a, b in edges if n in (a, b)] for n in names}
    rows = []
    for n in unknown:
        row = [Fraction(0)] * len(unknown) + [Fraction(0)]
        row[unknown.index(n)] += len(adj[n])
        for m in adj[n]:
            if m in vals:
                row[-1] += vals[m]
            else:
                row[unknown.index(m)] -= 1
        rows.append(row)
    k = len(unknown)
    for i in range(k):
        j = next(j for j in range(i, k) if rows[j][i])   # StopIteration: the board is not determined
        rows[i], rows[j] = rows[j], rows[i]
        d = rows[i][i]
        rows[i] = [v / d for v in rows[i]]
        for j in range(k):
            if j != i and rows[j][i]:
                f = rows[j][i]
                rows[j] = [a - f * b for a, b in zip(rows[j], rows[i])]
    return {n: rows[i][-1] for i, n in enumerate(unknown)}


def line(check):
    """One line of checked-values.txt: (packet, page, square values, circle values)."""
    file, page, vals, names, edges = check
    sol = solve(vals, names, edges)
    return str((file, page, dict(vals), {n: str(v) for n, v in sol.items()}))
