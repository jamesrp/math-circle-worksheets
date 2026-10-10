"""Edge cases for Week 5: hidden cities that no puzzle can single out (4-5 Problem 5) and the
3-by-3 counterpart (2-3 Problem 5); the K-1 Problem 4 hint that points to a Problem 3 card; the
guide's "about ln n towers are seen".

Run after extract_pdf.py (reads pdf_data.json):  python3 -I edge_cases.py > edge_cases.out
"""
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import edge_numbers, latin_squares, rowstr  # noqa: E402

for n in (3, 4):
    sq = latin_squares(n)
    groups = defaultdict(list)
    for s in sq:
        groups[tuple(sorted(edge_numbers(s).items()))].append(s)
    stuck = [s for v in groups.values() if len(v) > 1 for s in v]
    print(f"order {n}: {len(stuck)} of {len(sq)} cities share all {4 * n} numbers with another city,"
          f" so no puzzle at all can make them 'the only one that fits'")
    if n == 4:
        def twin(s):
            return [rowstr(t) for t in groups[tuple(sorted(edge_numbers(s).items()))] if t != s]
        natural = {
            "Problem 4 city A (also Problem 9)": "1234/2143/3412/4321",
            "Problem 4 city D (also Problem 9)": "1234/2413/3142/4321",
            "Problem 4 city B": "1234/2143/3421/4312",
            "Problem 4 city C": "1234/2341/3412/4123",
            "slide left each row": "1234/2341/3412/4123",
            "slide right each row": "1234/4123/3412/2341",
            "rows swap pairs (Klein pattern)": "1234/2143/3412/4321",
            "row 1 reversed in row 4, swaps": "1234/3412/4321/2143",
        }
        for label, r in natural.items():
            s = tuple(tuple(int(c) for c in row) for row in r.split("/"))
            t = twin(s)
            print(f"  {label:38s} {r}: " + (f"NOT fixable; same 16 numbers as {t}" if t else "fixable"))
        # cities with top row 1234: how many are unfixable
        top = [s for s in sq if s[0] == (1, 2, 3, 4)]
        print(f"  with top row 1234 (the guide's P2 hint): {sum(1 for s in top if twin(s))} of {len(top)} not fixable")
        red = [s for s in top if [r[0] for r in s] == [1, 2, 3, 4]]
        print(f"  with top row and left column 1234 (Problem 4's cities): {sum(1 for s in red if twin(s))} of {len(red)} not fixable")

# K-1 Problem 4 hint (2) "Find the card in Problem 3 with these numbers": which numbers a hider can say,
# and which of them have a card on K-1 page 3 (cards read from the PDF by extract_pdf.py).
import json  # noqa: E402
from itertools import permutations  # noqa: E402
from common import views  # noqa: E402
data = json.loads((Path(__file__).resolve().parent / "pdf_data.json").read_text())
cards = {tuple(c) for c in data["student"]["K"]["3"]["cards"]}
sayable = sorted({views(p) for p in permutations((1, 2, 3))})
print("\nK-1 P4: numbers a hider can say:", sayable)
print("        of these, with no card on Problem 3:", [v for v in sayable if v not in cards])

# Guide sec.5: "on average 1 + 1/2 + ... + 1/n ~ ln n towers are seen"
from math import log  # noqa: E402
from fractions import Fraction  # noqa: E402
for n in (3, 4, 5, 10, 100):
    H = sum(Fraction(1, j) for j in range(1, n + 1))
    if n <= 5:
        avg = Fraction(sum(sum(1 for i, h in enumerate(p) if h == max(p[:i + 1])) for p in permutations(range(1, n + 1))),
                       len(list(permutations(range(1, n + 1)))))
        assert avg == H
    print(f"n={n}: average seen H_n = {float(H):.3f}, ln n = {log(n):.3f}, difference {float(H) - log(n):.3f}")
