# Check every number used on the K-1 pages (revised packet) by repeated take-away.
def leftover(total, m):
    groups = 0
    while total >= m:
        total -= m
        groups += 1
    return total, groups


def square_page(m, sides):
    row = [leftover(n * n, m) for n in sides]
    occur = sorted(set((n * n) % m for n in range(0, 2001)))
    print(f" groups of {m}, sides {list(sides)}: leftovers {[r[0] for r in row]}, "
          f"fills {[r[1] for r in row]}; leftovers for sides 0-2000: {occur}")


def secret(m, sides):
    d = {}
    for n in sides:
        d.setdefault(leftover(n * n, m)[0], []).append(n)
    fills = max(leftover(n * n, m)[1] for n in sides)
    print(f" groups of {m}, cards {list(sides)}: {dict(sorted(d.items()))}, "
          f"most fills in a round {fills}")


print("P1 squares, groups of 4 (prefilled side 3 -> 1)")
square_page(4, range(1, 7))
assert leftover(9, 4)[0] == 1
print("Worked strip: 3x3 in groups of 4:", leftover(9, 4))
print("P2 secret square")
secret(4, range(1, 6))
print("P3 rectangles in groups of 4 (4x3 first)")
for a, b in [(4, 3), (3, 2), (5, 2), (5, 3)]:
    print(f" {a}x{b}={a*b}: leftover, fills {leftover(a*b, 4)}")
print("P4 squares, groups of 3")
square_page(3, range(1, 7))
print("P5 squares, groups of 6")
square_page(6, range(1, 7))
print("P6 secret square")
secret(6, range(1, 7))
print("P7 squares, groups of 2")
square_page(2, range(1, 6))
print("P8 big squares in groups of 4 (kit has 64 tiles)")
for n in (9, 10):
    print(f" {n}x{n}={n*n}: {leftover(n*n, 4)}")
print("P9/P10 rings and groups of 8")
for n in (1, 3, 5, 7):
    k = (n - 1) // 2
    ring = n * n - (n - 2) ** 2 if n > 1 else 1
    print(f" {n}x{n}={n*n}: leftover {leftover(n*n, 8)}, outer ring {ring} = 8*{k}")
print("P11 secret square")
secret(8, range(1, 7))
