"""Single source of the targets printed in the K-1 packet (writer notation:
places -3..3, home 0). Each target is (lit places, walker place)."""

P1 = [((0,), 0), ((), -2), ((2,), 2), ((-3,), -3)]
P2 = [((2,), 3), ((2,), 1), ((2,), 0), ((2,), -1)]
P3 = [((1, 2), 2), ((-1, 2), 2), ((-3, 1), -3), ((-2, 3), 3)]
P4 = [((-2, 1), 1), ((-2, 1), 0), ((-2, 1), -1), ((-2, 1), -2)]
P5 = [((0, 1), 0), ((0, 1, 2), 0)]
# kernel 2: (top, [(move, neighbour)])
P6_TOP = ((-2, -1), -1)
P7_TOP = ((-1, 0, 2), 0)
# kernel 3: (target, towers)
P8 = [(((0,), 0), (1, 2, 3, 4)), (((), 0), (1, 2, 3, 4)), (((1,), -1), (4, 5, 6, 7))]

def step(target, m):
    lit, w = set(target[0]), target[1]
    if m == 'L':
        w -= 1
    elif m == 'R':
        w += 1
    else:
        lit ^= {w}
    return (tuple(sorted(lit)), w)

def neighbours(top):
    return [(m, step(top, m)) for m in 'LRF']

P6 = neighbours(P6_TOP)
P7 = neighbours(P7_TOP)
