#!/usr/bin/env python3
"""Check the statements changed in the October 23, 2026 guide corrections (Week 26).

Standard library only; nothing is imported from the packet or guide builders.
Fixed polyominoes are enumerated by Redelmeier's method and checked directly.
Run from anywhere: python3 review/verify_card_fixes_2026_10_23.py [max_tiles]
(default 12; 10 runs in seconds).
"""
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 12
SIDE = ((1, 0), (-1, 0), (0, 1), (0, -1))
EIGHT = SIDE + ((1, 1), (1, -1), (-1, 1), (-1, -1))


def rows(*lines):
    return frozenset((x, y) for y, s in enumerate(lines) for x, c in enumerate(s) if c == '#')


def shared(s):
    return sum((x + dx, y + dy) in s for x, y in s for dx, dy in SIDE) // 2


def perimeter(s):
    return sum((x + dx, y + dy) not in s for x, y in s for dx, dy in SIDE)


def has_hole(s, steps):
    """True if some empty cell cannot reach the outside moving by `steps`.
    SIDE steps: two tiles meeting at a corner close a gap.
    EIGHT steps: a corner gap lets the inside out."""
    x0 = min(x for x, y in s) - 1; x1 = max(x for x, y in s) + 1
    y0 = min(y for x, y in s) - 1; y1 = max(y for x, y in s) + 1
    space = {(x, y) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1)} - s
    seen = {(x0, y0)}; todo = [(x0, y0)]
    while todo:
        x, y = todo.pop()
        for dx, dy in steps:
            p = (x + dx, y + dy)
            if p in space and p not in seen:
                seen.add(p); todo.append(p)
    return len(seen) < len(space)


def redelmeier(n_max, visit):
    """Visit every fixed polyomino with at most n_max cells exactly once."""
    def ok(c):
        x, y = c
        return y > 0 or (y == 0 and x >= 0)

    def rec(poly, untried, neighbours):
        while untried:
            cell = untried.pop()
            new = poly | {cell}
            visit(new)
            if len(new) < n_max:
                fresh = []
                for dx, dy in SIDE:
                    nb = (cell[0] + dx, cell[1] + dy)
                    if ok(nb) and nb not in neighbours and nb not in new:
                        fresh.append(nb)
                rec(new, list(untried) + fresh, neighbours | set(fresh))

    rec(frozenset(), [(0, 0)], {(0, 0)})


counts = [0] * (N + 1)
trees = [0] * (N + 1)
tree_side_holes = [0] * (N + 1)
tree_eight_holes = [0] * (N + 1)
max_p_without_tree = [0] * (N + 1)


def visit(s):
    s = frozenset(s)
    n = len(s)
    counts[n] += 1
    e = shared(s)
    assert perimeter(s) == 4 * n - 2 * e
    if e == n - 1:
        trees[n] += 1
        if has_hole(s, SIDE):
            tree_side_holes[n] += 1
        if has_hole(s, EIGHT):
            tree_eight_holes[n] += 1
    else:
        # every hole closed by full sides needs a cycle; the shape is not a tree
        max_p_without_tree[n] = max(max_p_without_tree[n], perimeter(s))


redelmeier(N, visit)
KNOWN = [0, 1, 2, 6, 19, 63, 216, 760, 2725, 9910, 36446, 135268, 505861]
assert counts[1:] == KNOWN[1:N + 1], counts
checks = [f'fixed polyomino counts 1..{N} match the known sequence ({sum(counts)} shapes); P = 4n - 2e on every one']
assert all(tree_eight_holes[n] == 0 for n in range(1, N + 1))
checks.append(f'no tree (e = n - 1) with up to {N} tiles has a hole if a corner gap lets the inside out')
assert tree_side_holes[N] > 0 if N >= 8 else True
checks.append(f'trees with a hole if a corner contact closes a gap: ' +
              ', '.join(f'n={n}: {tree_side_holes[n]}' for n in range(1, N + 1) if tree_side_holes[n]))
assert all(max_p_without_tree[n] <= 2 * n for n in range(2, N + 1))
checks.append('every non-tree has P <= 2n, below the maximum 2n + 2')

# The guide's third Grades 4-5 P2 drawing.
fig = rows('.##.....', '#.#.....', '########')
assert len(fig) == 12 and shared(fig) == 11 and perimeter(fig) == 26
assert has_hole(fig, SIDE) and not has_hole(fig, EIGHT)
checks.append('guide figure: 12 tiles, 11 shared sides, P = 26; a hole if the corner contact closes it, none if the corner gap leaks')

# "No hole" is not the tree test under either reading: the 2-by-2 block.
block = rows('##', '##')
assert not has_hole(block, SIDE) and not has_hole(block, EIGHT) and shared(block) == 4
checks.append('the 2-by-2 block has no hole under either reading and is not a tree')

# K-1 P1 extension: which tetrominoes take a fifth tile with no boundary change?
tetro = {'straight': rows('####'), 'square': rows('##', '##'), 'L': rows('###', '#..'),
         'T': rows('###', '.#.'), 'zigzag': rows('##.', '.##')}
zero = {}
for name, s in tetro.items():
    cand = {(x + dx, y + dy) for x, y in s for dx, dy in SIDE} - s
    changes = {perimeter(s | {c}) - perimeter(s) for c in cand}
    zero[name] = 0 in changes
    assert changes <= {2, 0}
assert zero == {'straight': False, 'square': False, 'L': True, 'T': True, 'zigzag': True}
checks.append('a fifth tile can keep the boundary at 10 for the L, T and zigzag (touching two old tiles); never for the square or the straight')

for c in checks:
    print('PASS', c)
print(f'PASS: {len(checks)} Week 26 correction checks')
