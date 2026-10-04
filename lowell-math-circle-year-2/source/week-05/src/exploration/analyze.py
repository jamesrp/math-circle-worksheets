from towers import *
from collections import Counter, defaultdict
from itertools import combinations
for n in (3,4):
    data = all_with_clues(n)
    sums = Counter(sum(cl.values()) for sq, cl in data)
    print(n, 'clue sums', sorted(sums.items()))
    full = Counter(tuple(sorted(cl.items())) for sq, cl in data)
    print(n, 'full clue sets shared by >1 city:', sum(1 for v in full.values() if v>1), 'max', max(full.values()))
    # minimal clue count for uniqueness
    keys = sorted(data[0][1].keys())
    for k in range(1, 7):
        found = 0; ex=None
        for sq, cl in data:
            for sub in combinations(keys, k):
                cs = {kk: cl[kk] for kk in sub}
                if len(solutions(n, cs)) == 1:
                    found += 1; ex = (sq, cs)
                    break
        print(n, 'k=',k, 'cities with a unique k-clue puzzle:', found)
        if found: print(ex); break
