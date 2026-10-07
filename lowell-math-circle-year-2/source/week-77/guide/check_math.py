#!/usr/bin/env python3
"""Independent exhaustive checks of the FINAL five-page Week 77 packet.

Only Python standard library. No student sources, comments, previous checkers,
review files, or third-party persistence packages are imported. The boards and
schedules below are transcribed from the final printed questions. All edge-chain
and face-subset tests use direct finite enumeration. General proofs are in the
guide: these finite computations are not claimed to prove the general theorems.
"""
from itertools import combinations, permutations
from math import log2


def edge(label):
    return "".join(sorted(label))


def chain(labels):
    return frozenset(edge(x) for x in labels.split())


def face(label):
    return frozenset(edge(x) for x in combinations(label, 2))


def subsets(items):
    items = tuple(sorted(items))
    for mask in range(1 << len(items)):
        yield frozenset(x for i, x in enumerate(items) if mask & (1 << i))


def boundary(names):
    result = frozenset()
    for name in names:
        result = result ^ face(name)
    return result


def boundaries(filled):
    return {boundary(s) for s in subsets(filled)}


def cycles(edges):
    ans = []
    for c in subsets(edges):
        odd = set()
        for e in c:
            for v in e:
                odd.symmetric_difference_update({v})
        if not odd:
            ans.append(c)
    return ans


def loop(c):
    """Nonempty connected even edge support: a closed no-edge-repeat walk."""
    if not c or c not in cycles(c):
        return False
    seen = {next(iter(c))[0]}
    while True:
        enlarged = seen | {v for e in c if seen.intersection(e) for v in e}
        if enlarged == seen:
            break
        seen = enlarged
    return seen == {v for e in c for v in e}


def beta(edges, filled):
    # Dimension from enumerated cycles / enumerated boundaries, not Euler's rule.
    count = len(cycles(edges)) // len(boundaries(filled))
    b = int(log2(count))
    assert 2 ** b == count
    return b


def film(vertices, edge_times, face_times):
    for e in edge_times:
        assert set(e) <= set(vertices)
    for f, t in face_times.items():
        if not all(e in edge_times and edge_times[e] <= t for e in face(f)):
            raise ValueError("face arrives before its full boundary: " + f)
    frames = {}
    for t in sorted({0} | set(edge_times.values()) | set(face_times.values())):
        edges = frozenset(e for e, s in edge_times.items() if s <= t)
        filled = frozenset(f for f, s in face_times.items() if s <= t)
        # Independent component calculation also checks the planar count formula.
        components = [{v} for v in vertices]
        for a, b in edges:
            group = set().union(*(s for s in components if a in s or b in s))
            components = [s for s in components if not (a in s or b in s)] + [group]
        b1 = beta(edges, filled)
        assert b1 == len(edges) - len(vertices) + len(components) - len(filled)
        frames[t] = (edges, filled, b1)
    return frames


def death(c, frames):
    return next((t for t, (_, f, _) in frames.items() if c in boundaries(f)), None)


def intervals(frames):
    """Recover positive-duration bars from actual inclusion-map ranks.

    Directly enumerate cosets of old cycles modulo later boundaries. This is
    separate from both the hole-count formula and saved-loop death checks.
    """
    times = tuple(frames)
    ranks = {}
    for i in range(len(times)):
        old_cycles = cycles(frames[times[i]][0])
        for j in range(i, len(times)):
            later_boundaries = boundaries(frames[times[j]][1])
            cosets = {min(tuple(sorted(c ^ b)) for b in later_boundaries)
                      for c in old_cycles}
            dimension = int(log2(len(cosets)))
            assert len(cosets) == 2 ** dimension
            ranks[i, j] = dimension
    assert frames[times[-1]][2] == 0
    result = []
    for birth in range(len(times)):
        for die in range(birth + 1, len(times)):
            n = (ranks[birth, die - 1] - ranks.get((birth - 1, die - 1), 0)
                 - ranks[birth, die] + ranks.get((birth - 1, die), 0))
            assert n >= 0
            result.extend([(times[birth], times[die])] * n)
    return sorted(result)


def check():
    square_edges = chain("AB BC CD DA AC")
    square_faces = frozenset({"ABC", "ACD"})
    P, Q, O = face("ABC"), face("ACD"), chain("AB BC CD DA")
    assert P ^ Q == O
    assert chain("XY YZ") ^ face("XYZ") == chain("XZ")
    all_square_loops = {c for c in cycles(square_edges) if loop(c)}
    assert all_square_loops == {P, Q, O}
    one_fill = {c for c in all_square_loops if any(c in boundaries({f}) for f in square_faces)}
    survive_either = {c for c in all_square_loops if all(c not in boundaries({f}) for f in square_faces)}
    assert one_fill == {P, Q} and survive_either == {O}
    print("P1: ABC or ACD rim dies with its tile; outer rim survives either single tile.")

    p2 = []
    for first_edge in ("AD", "AC"):
        second_edge = ({"AD", "AC"} - {first_edge}).pop()
        for first_face in sorted(square_faces):
            last_face = next(iter(square_faces - {first_face}))
            frames = film("ABCD", {"AB": 0, "BC": 0, "CD": 0, first_edge: 2, second_edge: 4},
                          {first_face: 5, last_face: 8})
            assert [frames[t][2] for t in (0, 2, 4, 5, 8)] == [0, 1, 2, 1, 0]
            saved = [c for c in cycles(frames[2][0]) if c]
            assert len(saved) == 1
            saved_death = death(saved[0], frames)
            p2.append((first_edge, second_edge, first_face, last_face, saved_death))
            assert intervals(frames) == ([(2, 5), (4, 8)] if saved_death == 5
                                          else [(2, 8), (4, 5)])
    assert p2 == [("AD", "AC", "ABC", "ACD", 8), ("AD", "AC", "ACD", "ABC", 8),
                  ("AC", "AD", "ABC", "ACD", 5), ("AC", "AD", "ACD", "ABC", 8)]
    print("P2 all schedules (stage 2 edge, stage 4 edge, stage 5 face, stage 8 face, death):")
    for row in p2:
        print(" ", row)

    p3 = []
    for first_edge in ("AB", "DE"):
        second_edge = ({"AB", "DE"} - {first_edge}).pop()
        for first_face in ("ABC", "CDE"):
            last_face = ({"ABC", "CDE"} - {first_face}).pop()
            frames = film("ABCDE", {"AC": 0, "BC": 0, "CD": 0, "CE": 0, first_edge: 2, second_edge: 4},
                          {first_face: 5, last_face: 8})
            assert [frames[t][2] for t in (0, 2, 4, 5, 8)] == [0, 1, 2, 1, 0]
            saved = [c for c in cycles(frames[2][0]) if c]
            assert len(saved) == 1
            saved_death = death(saved[0], frames)
            p3.append((first_edge, second_edge, first_face, last_face, saved_death))
            assert intervals(frames) == ([(2, 5), (4, 8)] if saved_death == 5
                                          else [(2, 8), (4, 5)])
    assert p3 == [("AB", "DE", "ABC", "CDE", 5), ("AB", "DE", "CDE", "ABC", 8),
                  ("DE", "AB", "ABC", "CDE", 8), ("DE", "AB", "CDE", "ABC", 5)]
    print("P3 all schedules:")
    for row in p3:
        print(" ", row)

    base_edges = {"AB": 0, "BC": 0, "CD": 0, "AD": 2, "AC": 4}
    base_faces = {"ABC": 4, "ACD": 8}
    base = film("ABCD", base_edges, base_faces)
    assert [base[t][2] for t in (0, 2, 4, 8)] == [0, 1, 1, 0]
    assert intervals(base) == [(2, 8)]
    p4 = []
    for item in ("AC", "ABC"):
        for new_stage in (3, 5):
            et, ft = dict(base_edges), dict(base_faces)
            (et if item == "AC" else ft)[item] = new_stage
            try:
                frames = film("ABCD", et, ft)
            except ValueError:
                p4.append((item, new_stage, "illegal"))
            else:
                two_hole_times = [t for t, (_, _, b) in frames.items() if b == 2]
                assert two_hole_times
                p4.append((item, new_stage, two_hole_times))
                assert death(O, frames) == 8
                assert intervals(frames) == ([(2, 8), (3, 4)] if item == "AC"
                                              else [(2, 8), (4, 5)])
    assert p4 == [("AC", 3, [3]), ("AC", 5, "illegal"), ("ABC", 3, "illegal"), ("ABC", 5, [4])]
    print("P4:", p4)
    print("P2/P3/P4 interval answers verified by inclusion-map ranks, including stage ties.")
    square_schedule_count = 0
    for b in range(1, 4):
        for s in range(b + 1, 5):
            for u in range(s, 7):
                for v in range(s, 7):
                    frames = film("ABCD", {"AB": 0, "BC": 0, "CD": 0, "AD": b, "AC": s},
                                  {"ABC": u, "ACD": v})
                    expected = sorted([(b, max(u, v))] +
                                      ([(s, min(u, v))] if s < min(u, v) else []))
                    assert intervals(frames) == expected
                    square_schedule_count += 1
    print("Square interval formula: finite cross-check of", square_schedule_count,
          "schedules, including ties; proof remains the guide's algebra.")

    fan_edges = chain("AB BC CD DA AO BO CO DO")
    fan_faces = frozenset({"ABO", "BCO", "CDO", "DAO"})
    # Injectivity on all 16 face selections is verified independently here.
    assert len(boundaries(fan_faces)) == 16
    fan_cycles = cycles(fan_edges)
    assert len(fan_cycles) == 16
    for small in subsets(fan_faces):
        for big in subsets(fan_faces):
            if small <= big:
                assert boundaries(small) <= boundaries(big)
    print("P5: finite checks of boundary monotonicity pass; universal proof is in guide.")

    start = frozenset({"ABO", "BCO"})
    remaining = fan_faces - start
    eligible = []
    for c in fan_cycles:
        if not loop(c) or c in boundaries(start):
            continue
        if all(c not in boundaries(start | {f}) for f in remaining):
            assert c in boundaries(fan_faces)
            eligible.append(c)
    support = {boundary(s): s for s in subsets(fan_faces)}
    expected = {chain("AO CO CD DA"), chain("AB BO CO CD DA"), chain("AO BO BC CD DA"), O}
    assert set(eligible) == expected
    print("P6 complete eligible loop list (edge set; required tiles):")
    for c in sorted(eligible, key=lambda c: (len(support[c]), sorted(c))):
        print(" ", " ".join(sorted(c)), ";", " ".join(sorted(support[c])))
    reversible_pairs = []
    for c, d in combinations(eligible, 2):
        signs = set()
        for order in permutations(fan_faces):
            dc = next(i for i in range(1, 5) if c in boundaries(order[:i]))
            dd = next(i for i in range(1, 5) if d in boundaries(order[:i]))
            signs.add((dc > dd) - (dc < dd))
        if {-1, 1} <= signs:
            reversible_pairs.append(frozenset({c, d}))
    L1, L2 = chain("AB BO CO CD DA"), chain("AO BO BC CD DA")
    assert reversible_pairs == [frozenset({L1, L2})]
    for order, expected_deaths in [(('CDO', 'DAO', 'ABO', 'BCO'), (3, 4)),
                                   (('CDO', 'DAO', 'BCO', 'ABO'), (4, 3))]:
        actual = tuple(next(i for i in range(1, 5) if c in boundaries(order[:i])) for c in (L1, L2))
        assert actual == expected_deaths
        print("  filling order", order, "gives L1/L2 deaths", actual)
    # Confirm all first-condition loops are the same nonzero current class.
    for c, d in combinations(eligible, 2):
        assert c ^ d in boundaries(start)
    print("P6: exactly one reversible unordered pair; all 6 pairs and all 24 filling orders checked.")
    print("PASS: every finite answer in the guide independently recomputed.")


if __name__ == "__main__":
    check()
