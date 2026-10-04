"""Preliminary checks of outline kernels; not the fresh worksheet math review.

Run from repository root with Python 3. Writes design-24-29-checks.json next to
this script. Does not touch base worksheets, guides, or global indexes.
"""
from itertools import combinations, permutations, product
from pathlib import Path
import json

results = {}
A, B, C = (2, 4, 9), (1, 6, 8), (3, 5, 7)
champions = [0, 0, 0]
for cards in product(A, B, C):
    champions[cards.index(max(cards))] += 1
assert champions == [10, 10, 7]
sum_duels = []
for left, right in ((A, B), (B, C), (C, A)):
    outcomes = [(sum(x) > sum(y), sum(x) == sum(y))
                for x in product(left, repeat=2)
                for y in product(right, repeat=2)]
    wins = sum(x[0] for x in outcomes)
    ties = sum(x[1] for x in outcomes)
    sum_duels.append([wins, 81 - wins - ties, ties])
assert sum_duels == [[37, 44, 0], [39, 38, 4], [39, 38, 4]]
results[24] = {"champions_of_27": champions,
               "two_draw_wins_losses_ties_of_81": sum_duels,
               "mixture_proof": "exact equalizing and mean-score argument in outline"}

perms3 = list(permutations(range(3)))
def diagonal_shadow(p):
    return tuple(sum(c - r == d for r, c in enumerate(p))
                 for d in range(-2, 3))

groups = {}
for p in perms3:
    groups.setdefault(diagonal_shadow(p), []).append(p)
assert sorted(map(len, groups.values())) == [1, 1, 1, 1, 2]
assert diagonal_shadow((0, 2, 1)) == diagonal_shadow((1, 0, 2)) == (0, 1, 1, 1, 0)
def query_depth(candidates):
    if len(candidates) <= 1:
        return 0
    costs = []
    for r, c in product(range(3), repeat=2):
        yes = [p for p in candidates if p[r] == c]
        no = [p for p in candidates if p[r] != c]
        if yes and no:
            costs.append(1 + max(query_depth(yes), query_depth(no)))
    return min(costs)

adaptive = query_depth(perms3)
nonadaptive = next(k for k in range(1, 10)
    if any(len({tuple(p[r] == c for r, c in cells) for p in perms3}) == 6
           for cells in combinations(list(product(range(3), repeat=2)), k)))
assert (adaptive, nonadaptive) == (3, 4)
results[25] = {"diagonal_group_sizes": sorted(map(len, groups.values())),
               "adaptive_queries": adaptive, "fixed_queries": nonadaptive}

cells4 = set(product(range(4), repeat=2))
edges4 = [(p, q) for p in cells4 for q in ((p[0]+1, p[1]), (p[0], p[1]+1)) if q in cells4]
def connected(cells):
    if not cells:
        return False
    seen = {next(iter(cells))}
    queue = list(seen)
    for r, c in queue:
        for p in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
            if p in cells and p not in seen:
                seen.add(p)
                queue.append(p)
    return len(seen) == len(cells)

fence_min = 100
connected_fence_min = 100
for red_tuple in combinations(cells4, 8):
    red = set(red_tuple)
    blue = cells4 - red
    fence = sum((p in red) != (q in red) for p, q in edges4)
    fence_min = min(fence_min, fence)
    if connected(red) and connected(blue):
        connected_fence_min = min(connected_fence_min, fence)
assert fence_min == connected_fence_min == 4
def corner_counts(shape):
    vertices = {(r+dr,c+dc) for r,c in shape for dr,dc in product((0,1), repeat=2)}
    counts = [sum(p in shape for p in ((r-1,c-1),(r-1,c),(r,c-1),(r,c)))
              for r,c in vertices]
    return counts.count(1), counts.count(3)

assert corner_counts({(0,0),(0,1),(1,0)}) == (5,1)
assert corner_counts(set(product(range(3), repeat=2)) - {(1,1)}) == (4,4)
def cube_surface(cubes):
    return sum((x+dx,y+dy,z+dz) not in cubes for x,y,z in cubes
               for dx,dy,dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)))

cube_surfaces = [cube_surface(set(product(range(2),repeat=3))),
                 cube_surface(set(product(range(2),range(4),range(1)))),
                 cube_surface(set(product(range(8),range(1),range(1))))]
assert cube_surfaces == [24,28,34]
turn_shapes = 0
ordered_cells4 = sorted(cells4)
outside_box = set(product(range(-1, 5), repeat=2))
for mask in range(1, 1 << 16):
    shape = {p for i, p in enumerate(ordered_cells4) if mask >> i & 1}
    if not connected(shape):
        continue
    convex = concave = 0
    pinched = False
    for r, c in product(range(5), repeat=2):
        occupied = [p in shape for p in ((r-1,c-1), (r-1,c), (r,c-1), (r,c))]
        k = sum(occupied)
        if k == 2 and ((occupied[0] and occupied[3]) or (occupied[1] and occupied[2])):
            pinched = True
            break
        convex += k == 1
        concave += k == 3
    if pinched:
        continue
    empty = outside_box - shape
    components = 0
    while empty:
        seed = empty.pop()
        queue = [seed]
        components += 1
        for r, c in queue:
            for p in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
                if p in empty:
                    empty.remove(p)
                    queue.append(p)
    holes = components - 1
    assert convex - concave == 4 * (1 - holes)
    turn_shapes += 1
results[26] = {"all_balanced_4x4_partitions": 12870,
               "minimum_interface": fence_min,
               "minimum_connected_interface": connected_fence_min,
               "connected_no_pinch_4x4_corner_formula_shapes": turn_shapes,
               "corner_examples_L_and_ring": [[5,1],[4,4]],
               "cube_surface_examples": cube_surfaces}

left = [(1,2,0), (1,0,2), (0,1,2)]
right = [(1,0,2), (0,2,1), (1,0,2)]
def stable_complete(m):
    inv = {v:k for k,v in enumerate(m)}
    return not any(left[i].index(j) < left[i].index(m[i])
                   and right[j].index(i) < right[j].index(inv[j])
                   for i,j in product(range(3), repeat=2) if j != m[i])
def ranks_total(m):
    return sum(left[i].index(m[i]) + right[m[i]].index(i) + 2 for i in range(3))

best_score = min(map(ranks_total, perms3))
best = [m for m in perms3 if ranks_total(m) == best_score]
stable = [m for m in perms3 if stable_complete(m)]
assert best == [(1,2,0)] and best_score == 10
assert stable == [(1,0,2)] and ranks_total(stable[0]) == 11
roommate_preferences = [(1,2,3), (2,0,3), (0,1,3), (0,1,2)]
roommate_matchings = [(1,0,3,2), (2,3,0,1), (3,2,1,0)]
blockers = []
for m in roommate_matchings:
    blockers.append([(i,j) for i,j in combinations(range(4), 2)
        if m[i] != j and roommate_preferences[i].index(j) < roommate_preferences[i].index(m[i])
        and roommate_preferences[j].index(i) < roommate_preferences[j].index(m[j])])
assert all(blockers)
partial_lists = [(), (0,), (1,), (0,1), (1,0)]
partial_matchings = [(-1,-1), (0,-1), (1,-1), (-1,0), (-1,1), (0,1), (1,0)]
partial_profiles_checked = 0
for lp0,lp1,rp0,rp1 in product(partial_lists, repeat=4):
    lp, rp = [lp0,lp1], [rp0,rp1]
    stable_sets = set()
    for m in partial_matchings:
        inv = {v:k for k,v in enumerate(m) if v != -1}
        allowed = lambda i,j: j in lp[i] and i in rp[j]
        if any(j != -1 and not allowed(i,j) for i,j in enumerate(m)):
            continue
        def prefers_l(i,j):
            return m[i] == -1 or lp[i].index(j) < lp[i].index(m[i])
        def prefers_r(j,i):
            return j not in inv or rp[j].index(i) < rp[j].index(inv[j])
        if any(allowed(i,j) and j != m[i] and prefers_l(i,j) and prefers_r(j,i)
               for i,j in product(range(2), repeat=2)):
            continue
        stable_sets.add((tuple(i for i,j in enumerate(m) if j != -1), tuple(sorted(inv))))
    assert len(stable_sets) == 1
    partial_profiles_checked += 1
results[27] = {"rank_minimum": best_score, "stable_rank_total": 11,
               "roommate_blockers": blockers,
               "incomplete_2x2_profiles_with_invariant_matched_sets": partial_profiles_checked}

stack_counts = {}
for n in (3,4):
    valid = []
    for stack in permutations(range(n)):
        positions = {panel:i for i,panel in enumerate(stack)}
        crossing = False
        for i,j in combinations(range(n-1), 2):
            if i % 2 != j % 2:
                continue
            a,b = sorted((positions[i],positions[i+1]))
            c,d = sorted((positions[j],positions[j+1]))
            crossing |= a<c<b<d or c<a<d<b
        if not crossing:
            valid.append(stack)
    stack_counts[n] = len(valid)
assert stack_counts == {3:6, 4:16}
orbit4 = {(x,y) for x in (-2,2) for y in (-1,1)}
orbit8 = orbit4 | {(y,x) for x,y in orbit4}
assert len(orbit4) == 4 and len(orbit8) == 8
results[28] = {"ideal_noncrossing_strip_stack_counts": stack_counts,
               "off_axis_punch_orbit_counts": [len(orbit4),len(orbit8)],
               "physical_folds_and_punching": "untested"}

f = [0] * 21
f[0] = 1
for n in range(1,21):
    f[n] = sum(f[n-k] for k in (3,4) if n >= k)
assert [f[n] for n in (7,10,12,15,18)] == [2,3,2,5,11]
finite = {3*x + 4*y for x in range(5) for y in range(4)}
gaps = [n for n in range(25) if n not in finite]
assert gaps == [1,2,5,19,22,23]
assert all((n in finite) == (24-n in finite) for n in range(25))
def reachable(lengths, cap=100):
    values = {0}
    for n in range(1,cap+1):
        if any(n-k in values for k in lengths):
            values.add(n)
    return values

original = reachable((3,5))
assert reachable((3,5,8)) == original
assert max(set(range(101)) - reachable((3,5,7))) == 4
assert max(set(range(101)) - reachable((3,4,5))) == 2
results[29] = {"ordered_3_4_counts_0_to_20": f, "finite_4threes_3fours_gaps": gaps,
               "third_rod_gaps_for_7_and_4": [4,2]}

target = Path(__file__).with_name('design-24-29-checks.json')
target.write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
