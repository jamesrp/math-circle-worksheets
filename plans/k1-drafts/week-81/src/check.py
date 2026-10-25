"""Exhaustive checks for the Week 81 K-1 pages (one-each refill rule)."""
from functools import lru_cache
from itertools import combinations

def moves(p):
    out = []
    for i in range(len(p)):
        if p[i] == 0:
            continue
        smaller = list(range(i))
        for r in range(len(smaller) + 1):
            for S in combinations(smaller, r):
                q = list(p); q[i] -= 1
                for j in S: q[j] += 1
                out.append((tuple(q), i + 1, S))
    return out

@lru_cache(None)
def first_wins(p):
    return any(not first_wins(q) for q, _, _ in moves(p))

@lru_cache(None)
def length_range(p):
    ms = moves(p)
    if not ms:
        return (0, 0)
    lo = min(length_range(q)[0] for q, _, _ in ms) + 1
    hi = max(length_range(q)[1] for q, _, _ in ms) + 1
    return (lo, hi)

@lru_cache(None)
def all_lengths(p):
    ms = moves(p)
    if not ms:
        return frozenset([0])
    s = set()
    for q, _, _ in ms:
        s |= {x + 1 for x in all_lengths(q)}
    return frozenset(s)

@lru_cache(None)
def board_max(p):
    return max([sum(p)] + [board_max(q) for q, _, _ in moves(p)])

def winning_moves(p):
    return [(q, i, S) for q, i, S in moves(p) if not first_wins(q)]

def W(p): return "first" if first_wins(p) else "second"
if __name__ == "__main__":

    # claim: second player wins iff all even
    for a in range(9):
        for b in range(9):
            assert first_wins((a, b)) == (a % 2 or b % 2), (a, b)
    for a in range(6):
        for b in range(6):
            for c in range(6):
                assert first_wins((a, b, c)) == bool(a % 2 or b % 2 or c % 2)
    print("all-even rule OK")

    print("\nP1 one bucket:")
    for n in [2, 3, 4, 5, 6, 7, 10, 11]:
        print(n, W((n,)))

    print("\nP2 two buckets:")
    for p in [(1,1),(2,0),(0,2),(2,1),(1,2),(2,2)]:
        print(p, W(p))

    print("\nP3 winning first moves:")
    for p in [(1,1),(2,1),(1,2),(3,1),(2,3),(3,3)]:
        print(p, W(p), winning_moves(p))

    print("\nP4 vs adult:")
    for p in [(4,2),(3,4),(2,4),(4,4)]:
        print(p, W(p), winning_moves(p), "lengths", length_range(p))

    print("\nP5 from (2,2): every move and winning replies")
    for q, i, S in moves((2,2)):
        print(" partner ->", q, "took from", i, "refill", S, "| replies:", [r for r,_,_ in winning_moves(q)])

    print("\nP6/P7 second-player starts by total:")
    for t in [4, 5, 6]:
        print(t, [(a, t - a) for a in range(t + 1) if not first_wins((a, t - a))])
        print("   lengths:", {(a, t-a): length_range((a, t-a)) for a in range(t+1)})

    print("\nP8 shortest/longest two buckets:")
    for p in [(1,1),(0,2),(0,3),(2,2),(3,3)]:
        print(p, length_range(p), sorted(all_lengths(p)))

    print("\nP9 three buckets: board max and lengths")
    for p in [(0,0,1),(0,0,2),(0,1,1),(1,1,1),(0,0,3),(1,2,1),(0,1,2),(1,0,2),(0,2,1)]:
        print(p, "board max", board_max(p), "lengths", length_range(p), sorted(all_lengths(p)))

    print("\nP11 three-bucket winning first moves:")
    for p in [(2,0,1),(1,0,1),(0,1,1),(1,1,1),(0,0,1)]:
        print(p, W(p), winning_moves(p), "lengths", length_range(p))

    print("\nDemo move (0,2) -> (1,1) is legal:", any(q == (1,1) for q,_,_ in moves((0,2))))

    print("\nP11 (3,3,3): board max", board_max((3, 3, 3)), "lengths", length_range((3, 3, 3)))

    # revision: new or moved positions
    print("\nRule picture (3,2) bucket-2 results:", sorted({q for q, i, S in moves((3, 2)) if i == 2}))
    print("Rule picture (1,0,2) bucket-3 results:", sorted({q for q, i, S in moves((1, 0, 2)) if i == 3}))
    print("P11 longest games:", {p: length_range(p)[1] for p in [(0, 1, 1), (1, 1, 1), (0, 0, 3)]})
    print("P12 (2,2,2): board max", board_max((2, 2, 2)), "lengths", length_range((2, 2, 2)))
