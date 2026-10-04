"""Independent enumeration and formula checks for the Week 63 outline."""
import itertools
import json
import math
from collections import Counter
from pathlib import Path

data = {}
expected = [1, 0, 1, 2, 9, 44]
for n in range(6):
    rows = list(itertools.permutations(range(1, n+1)))
    fixed = lambda p: sum(v == i for i, v in enumerate(p, 1))
    valid = [p for p in rows if fixed(p) == 0]
    assert len(valid) == expected[n]
    signed_terms = [(-1)**k * math.comb(n, k) * math.factorial(n-k)
                    for k in range(n+1)]
    assert sum(signed_terms) == len(valid)
    if n >= 2:
        assert len(valid) == (n-1) * (expected[n-1] + expected[n-2])
    intersections = {}
    for k in range(n+1):
        for chosen in itertools.combinations(range(1, n+1), k):
            count = sum(all(p[i-1] == i for i in chosen) for p in rows)
            assert count == math.factorial(n-k)
            intersections[",".join(map(str, chosen)) or "empty"] = count
    distinguished = {}
    for target in range(1, n):
        with_target = [p for p in valid if p[n-1] == target]
        reciprocal = sum(p[target-1] == n for p in with_target)
        nonreciprocal = len(with_target) - reciprocal
        assert reciprocal == expected[n-2]
        assert nonreciprocal == expected[n-1]
        distinguished[str(target)] = {"two_cycle": reciprocal,
                                      "longer_cycle": nonreciprocal}
    data[str(n)] = {"all_orders": math.factorial(n), "derangements": len(valid),
                   "fixed_point_histogram": dict(sorted(Counter(map(fixed, rows)).items())),
                   "inclusion_exclusion_signed_terms": signed_terms,
                   "specified_fixed_home_intersection_counts": intersections,
                   "distinguished_card_recurrence_cases": distinguished,
                   "valid_rows": [list(p) for p in valid]}

n = 4
rows = list(itertools.permutations(range(1, n+1)))
for r, count in [(1, 18), (2, 14), (3, 11), (4, 9)]:
    actual = sum(all(p[i-1] != i for i in range(1, r+1)) for p in rows)
    formula = sum((-1)**k * math.comb(r,k) * math.factorial(n-k) for k in range(r+1))
    assert actual == formula == count
data["partial_avoidance_n4"] = {"forbid_first_r_homes": {"1":18,"2":14,"3":11,"4":9},
    "limit": "Other cards may stay home; these are not full derangements unless r=4."}
out = Path(__file__).with_name("small-instances.json")
out.write_text(json.dumps(data, indent=2) + "\n")
print(f"Verified every permutation for n=0 through 5, all fixed-home intersections, and recurrence cases; wrote {out}")
