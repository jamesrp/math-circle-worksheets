"""Recompute every answer printed in the Counting-out circles facilitator guide.

Independent literal simulation of the final pages' rule: counters on spots
1..n of a ring, the count starts at spot 1, standing counters take turns with
a chant of length k ("stand, sit" is k = 2, "stand, stand, sit" is k = 3);
the chant carries on past spot 1 without restarting; the counter that gets the
last word of the chant is flipped (sits); sitting counters are skipped.

Run:  python3 check_guide.py      (exits non-zero if any assertion fails)
"""
import sys


def play(n, k=2):
    """Return (survivor, sitting order, laps) for n counters, chant length k.
    laps[i] lists who sat during the i-th pass of the pointer round the ring."""
    standing = [False] + [True] * n
    word = 0
    order, laps, lap = [], [], []
    left = n
    spot = 1
    while left > 1:
        if standing[spot]:
            word = word % k + 1
            if word == k:
                standing[spot] = False
                order.append(spot)
                lap.append(spot)
                left -= 1
        if spot == n:
            laps.append(lap)
            lap = []
        spot = spot % n + 1
    if lap:
        laps.append(lap)
    survivor = next(i for i in range(1, n + 1) if standing[i])
    return survivor, order, laps


def J(n, k=2):
    return play(n, k)[0]


def restart_misreading(n):
    """Misreading: the chant starts again at 'stand' every time the count
    reaches spot 1. Returns the survivor."""
    standing = [False] + [True] * n
    left, word, spot, guard = n, 0, 1, 0
    while left > 1 and guard < 10 * n * n:
        guard += 1
        if spot == 1:
            word = 0
        if standing[spot]:
            word = word % 2 + 1
            if word == 2:
                standing[spot] = False
                left -= 1
        spot = spot % n + 1
    return next(i for i in range(1, n + 1) if standing[i])


ok = True


def check(label, got, want):
    global ok
    flag = "ok " if got == want else "FAIL"
    if got != want:
        ok = False
    print(f"[{flag}] {label}: {got}" + ("" if got == want else f"   (guide says {want})"))


def two_L_plus_1(n):
    m = n.bit_length() - 1
    return 2 * (n - 2 ** m) + 1


# ---------------------------------------------------------------- theorems
for n in range(1, 2049):
    assert J(n) == two_L_plus_1(n), n
    b = bin(n)[2:]
    assert J(n) == int(b[1:] + b[0], 2), n            # move the leading 1 to the end
    if n >= 2:
        prev = J(n - 1)
        assert J(n) == (prev + 2 if prev + 2 <= n else 1), n   # step rule, k = 2
    assert (J(n) == 1) == (n & (n - 1) == 0), n                 # powers of two
    assert (J(n) == n) == ((n + 1) & n == 0), n                 # 2^j - 1
    assert J(n) % 2 == 1, n                                     # evens never last
    sat = play(n)[1]
    assert sat[: n // 2] == list(range(2, n + 1, 2)), n         # first lap: the evens, in order
for k in range(1, 1025):
    assert J(2 * k) == 2 * J(k) - 1 and J(2 * k + 1) == 2 * J(k) + 1, k
for n in range(2, 501):
    prev = J(n - 1, 3)
    s = prev + 3
    if s > n:
        s -= n
    assert J(n, 3) == s == (prev + 2) % n + 1, n                # step rule, k = 3
    assert J(n, 3) % 3 != 0, n                                  # multiples of 3 never last
    if n >= 3:
        assert play(n, 3)[1][0] == 3
for k in (2, 3, 4, 5):
    for n in range(2, 301):
        assert J(n, k) == (J(n - 1, k) + k - 1) % n + 1, (n, k)
print("theorems: 2L+1 and binary rotation (n <= 2048), step rules k = 2..5, doubling, first lap: ok")

mis = [restart_misreading(n) for n in range(1, 17)]
check("misreading (restart at 1) survivors n = 1..16", mis, [1] * 16)
check("power-of-two circles never show the misreading (n = 8: same laps)",
      play(8)[2], [[2, 4, 6, 8], [3, 7], [5]])

# ---------------------------------------------------------------- launch
s, order, laps = play(11, 4)
check("launch: 11 people, chant of 4, sitting order", order, [4, 8, 1, 6, 11, 7, 3, 2, 5, 10])
check("launch: 11 people, chant of 4, last one standing", s, 9)
check("launch: first pass sits 4 and 8; first sit after the wrap", (laps[0], order[2]), ([4, 8], 1))
check("launch with 7 people: person 1 is the first to sit after the wrap", play(7, 4)[1][:2], [4, 1])
check("launch: 1..16 sizes where person 1 sits first after the wrap (n = 3 mod 4, n >= 7)",
      [n for n in range(5, 17) if play(n, 4)[2][0] and play(n, 4)[1][len(play(n, 4)[2][0])] == 1], [7, 11, 15])
# the four-word chant is used by no problem; its survivor is not an answer anywhere
print("     chant-of-4 survivors n = 1..12 (adult reference only):", [J(n, 4) for n in range(1, 13)])

sits = lambda ns: sum(n - 1 for n in ns)
# ---------------------------------------------------------------- revision checks (final guide)
def play_on_mat(n, spots, k):
    """Counters on spots 1..n of a ring of `spots` spots; spots n+1..spots are empty.
    Returns the sitting order, simulated spot by spot (empty spots get no word)."""
    occupied = [False] + [i <= n for i in range(1, spots + 1)]
    word, order, left, spot = 0, [], n, 1
    while left > 1:
        if occupied[spot]:
            word = word % k + 1
            if word == k:
                occupied[spot] = False
                order.append(spot)
                left -= 1
        spot = spot % spots + 1
    return order


def words_before_first_sit_after(n, k, who):
    """Return True if, playing n with chant k, the very next word after the pointer
    first passes spot n goes to `who` and is 'sit' (i.e. `who` sits right at the wrap).
    Simulated word by word, independent of any formula."""
    standing = [False] + [True] * n
    word, spot = 0, 1
    for _ in range(n):                     # the first pass: spots 1..n
        if standing[spot]:
            word = word % k + 1
            if word == k:
                standing[spot] = False
        spot = spot % n + 1
    while not standing[spot]:              # next standing person after the wrap
        spot = spot % n + 1
    return spot == who and word % k + 1 == k


check("replay, older tables: 11 counters on the 16-spot mat, chant of 4, first three sits",
      play_on_mat(11, 16, 4)[:3], [4, 8, 1])
check("replay on the mat matches the ring of 11 (empty spots change nothing)",
      play_on_mat(11, 16, 4), play(11, 4)[1])
check("replay, K-1: ring of 7, chant of 4, first two sits", play(7, 4)[1][:2], [4, 1])
check("launch circles where 1 gets 'sit' right at the wrap, sizes 5..19",
      [n for n in range(5, 20) if words_before_first_sit_after(n, 4, 1)], [7, 11, 15, 19])
check("launch: last one standing in circles of 7, 11, 15 (chant of 4)", [J(n, 4) for n in (7, 11, 15)], [2, 9, 13])
check("step-rule proof: first to sit, chant 2 (n >= 2), chant 3 (n = 2; n >= 3)",
      (all(play(n)[1][0] == 2 for n in range(2, 200)), play(2, 3)[1][0],
       all(play(n, 3)[1][0] == 3 for n in range(3, 200))), (True, 1, True))
k1_pages = {1: [3, 4, 5, 6], 2: [7, 8], 3: [9, 10], 4: [16], 6: [3, 4, 5, 6], 7: [7, 8], 8: [9]}
check("K-1 pages with more spots than 16 counters (play one ring at a time)",
      [pg for pg, rs in k1_pages.items() if sum(rs) > 16], [1, 3, 6])
check("K-1 largest single ring fits 16 counters", max(max(rs) for rs in k1_pages.values()), 16)
check("K-1 P4 extension: circles up to 40 leaving 3, leaving 5",
      ([n for n in range(1, 41) if J(n) == 3], [n for n in range(1, 41) if J(n) == 5]),
      ([3, 5, 9, 17, 33], [6, 10, 18, 34]))
check("K-1 first visit flips (P1 + P2 + P3), circle of 16 alone",
      (sits([3, 4, 5, 6]) + sits([7, 8, 9, 10]) + sits([16]), sits([16])), (59, 15))
check("4-5 first visit flips, Problems 1 and 2 (one pair)", sits(range(1, 17)) + sits([20, 25, 32]), 194)
check("2-3 Problem 2 flips per 32-spot circle (20, 25, 32)", [n - 1 for n in (20, 25, 32)], [19, 24, 31])

# ---------------------------------------------------------------- K-1
k1_circles = list(range(3, 11)) + [16]
check("K-1 P1 circles 3,4,5,6", [J(n) for n in (3, 4, 5, 6)], [3, 1, 3, 5])
check("K-1 P2 circles 7,8,9,10", [J(n) for n in (7, 8, 9, 10)], [7, 1, 3, 5])
check("K-1 P3 stars (1 last among 3..10)", [n for n in range(3, 11) if J(n) == 1], [4, 8])
check("K-1 P3 circle of 16", J(16), 1)
check("K-1 P4 number 3 last in", [n for n in k1_circles if J(n) == 3], [3, 5, 9])
check("K-1 P4 number 5 last in", [n for n in k1_circles if J(n) == 5], [6, 10])
check("K-1 P5 number 2 sits first in every circle of 2..100",
      all(play(n)[1][0] == 2 for n in range(2, 101)), True)
check("K-1 P6 stand,stand,sit circles 3..8", [J(n, 3) for n in range(3, 9)], [2, 1, 4, 1, 4, 7])
check("K-1 P7 stand,stand,sit circle of 9", J(9, 3), 1)
check("K-1 P7 sitting order for 9", play(9, 3)[1], [3, 6, 9, 4, 8, 5, 2, 7])
check("K-1 P8 number 3 sits first in every circle of 3..100 (stand,stand,sit)",
      all(play(n, 3)[1][0] == 3 for n in range(3, 101)), True)
check("K-1 sitting order, circle of 3 (1 sits after the wrap)", play(3)[1], [2, 1])
check("K-1 sitting order, circle of 6", play(6)[1], [2, 4, 6, 3, 1])

# ---------------------------------------------------------------- grades 2-3
table16 = [J(n) for n in range(1, 17)]
sits = lambda ns: sum(n - 1 for n in ns)
check("2-3 P1 split: sits for circles 1..11 and 12..16", (sits(range(1, 12)), sits(range(12, 17))), (55, 65))
check("2-3/4-5 P1 circles 1..16", table16, [1, 1, 3, 1, 3, 5, 7, 1, 3, 5, 7, 9, 11, 13, 15, 1])
check("2-3/4-5 P2 circles 20, 25, 32", [J(n) for n in (20, 25, 32)], [9, 19, 1])
check("2-3 P3 even numbers never last (n <= 2048)", all(J(n) % 2 for n in range(1, 2049)), True)
odd_witness = {q: (q - 1) // 2 + 2 ** ((q - 1) // 2).bit_length() for q in range(1, 40, 2)}
check("2-3 P3 every odd q is last in circle (q-1)/2 + next power of two",
      all(J(n) == q for q, n in odd_witness.items()), True)
print("     e.g. witnesses:", {q: odd_witness[q] for q in (1, 3, 5, 7, 9, 17, 21)})
check("2-3 P4 laps for 16", play(16)[2], [[2, 4, 6, 8, 10, 12, 14, 16], [3, 7, 11, 15], [5, 13], [9]])
check("2-3 P4 after the first lap of 32, standing", [i for i in range(1, 33) if i % 2], list(range(1, 33, 2)))
check("2-3 P5 number 9 last, circles up to 40", [n for n in range(1, 41) if J(n) == 9], [12, 20, 36])
check("2-3 P5 last = size, circles up to 40", [n for n in range(1, 41) if J(n) == n], [1, 3, 7, 15, 31])
check("2-3 P6 circles 50, 100", [J(n) for n in (50, 100)], [37, 73])
check("2-3 P6 circle of 50: first 18 to sit, then next counter",
      (play(50)[1][:18], 37), (list(range(2, 37, 2)), 37))
t3 = [J(n, 3) for n in range(1, 25)]
check("2-3/4-5 P7 every third, 1..12", t3[:12], [1, 2, 2, 1, 4, 1, 4, 7, 1, 4, 7, 10])
check("2-3 P8 every third, 13..20", t3[12:20], [13, 2, 5, 8, 11, 14, 17, 20])
check("2-3 P8 check circles 14, 20", (J(14, 3), J(20, 3)), (2, 20))
check("2-3 P9 every third, 21..30", [J(n, 3) for n in range(21, 31)], [2, 5, 8, 11, 14, 17, 20, 23, 26, 29])
check("2-3 P9 circle of 30", J(30, 3), 29)
check("every third, circle of 2: order", play(2, 3)[1], [1])

# ---------------------------------------------------------------- grades 4-5
check("4-5 P3 number 1 last, up to 100", [n for n in range(1, 101) if J(n) == 1], [1, 2, 4, 8, 16, 32, 64])
check("4-5 P4 circles 100, 1000", [J(n) for n in (100, 1000)], [73, 977])
check("4-5 P5 circles 26, 52, 53", [J(n) for n in (26, 52, 53)], [21, 41, 43])
o53 = play(53)[1]
check("4-5 P5 circle of 53: first 27 to sit", o53[:27], list(range(2, 53, 2)) + [1])
check("4-5 P6 number 23 last, up to 100", [n for n in range(1, 101) if J(n) == 23], [27, 43, 75])
check("4-5 P6 number 22 last, up to 100", [n for n in range(1, 101) if J(n) == 22], [])
check("4-5 P8 every third, 13..24", t3[12:24], [13, 2, 5, 8, 11, 14, 17, 20, 2, 5, 8, 11])
check("4-5 P8 check circles 14, 21", (J(14, 3), J(21, 3)), (2, 2))
check("4-5 P9 every third 25..41", [J(n, 3) for n in range(25, 42)],
      [14, 17, 20, 23, 26, 29, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31])
s41, o41, _ = play(41, 3)
check("4-5 P9 circle of 41: last standing, last to sit", (s41, o41[-1]), (31, 16))
check("4-5 P10 example", (J(12), bin(12)[2:], bin(J(12))[2:]), (9, "1100", "1001"))
check("4-5 P10 n = 13 (1101 -> 1011)", (bin(13)[2:], bin(J(13))[2:]), ("1101", "1011"))

# rival rules a child might read off the 12 -> 9 example
def rot(b):  return b[1:] + b[0]
def rev(b):  return b[::-1]
def swap2last(b):
    if len(b) < 3: return b
    return b[0] + b[-1] + b[2:-1] + b[1]
for name, f in (("reverse", rev), ("swap 2nd and last digits", swap2last)):
    fits12 = int(f("1100"), 2) == 9
    agree = [n for n in range(1, 64) if int(f(bin(n)[2:]), 2) == J(n)]
    print(f"     rival rule '{name}': fits 12->9: {fits12}; agrees with J for n = 1..63 at {len(agree)} values;"
          f" first failures {[n for n in range(1, 64) if n not in agree][:6]}")
check("swap rule fits the 12 -> 9 example", int(swap2last("1100"), 2), 9)
check("swap rule fails on every power of two 2..32", all(int(swap2last(bin(2**j)[2:]), 2) != 1 for j in range(1, 6)), True)
check("reverse rule fails on the example", int(rev("1100"), 2), 3)

# ---------------------------------------------------------------- geometry cited in the guide
# Ring radii (cm) and spot radius from the final sources (k-1.tex, common.tex); chord = 2R sin(pi/n).
import math
rings = {"K-1 ring 3": (3, 2.0), "K-1 ring 4": (4, 2.1), "K-1 ring 5": (5, 2.42), "K-1 ring 6": (6, 2.85),
         "K-1 ring 7": (7, 3.40), "K-1 ring 8": (8, 3.85), "K-1 ring 9": (9, 4.1), "K-1 ring 10": (10, 4.55),
         "16-spot mat": (16, 7.2)}
gaps = {k: 2 * R * math.sin(math.pi / n) - 2.6 for k, (n, R) in rings.items()}
print("     edge gap between neighbouring 26 mm spots (cm):", {k: round(v, 2) for k, v in gaps.items()})
check("smallest spot-to-spot gap is about 2 mm", round(min(gaps.values()), 1), 0.2)
check("gap between 25.4 mm counters on the closest ring is about 2.6 mm",
      round(min(2 * R * math.sin(math.pi / n) for n, R in rings.values()) - 2.54, 2), 0.26)
# 32-spot mat (make_mat32.py): centre spacing 3.05 cm at the corners, 3.20 cm on the runs;
# 4.2 cm between spots 5 and 6 across the join of the two pages
check("32-spot mat: smallest edge gap along the loop (cm)", round(3.047 - 2.6, 2), 0.45)
check("32-spot mat: edge gap across the join (cm)", round(2 * 0.8, 1), 1.6)
# printing counts: K-1 4 children x 8 pp; 2-3 4 x 4 + 2 pairs x 3 mats; 4-5 3 x 5 + 1 pair x 3 mats
check("sheets to print (K-1, 2-3, 4-5, total)", (4 * 8, 4 * 4 + 2 * 3, 3 * 5 + 3, 4 * 8 + 22 + 18), (32, 22, 18, 72))
check("counters (two K-1 pairs x 16, three older pairs x 32)", 2 * 16 + 3 * 32, 128)

print()
print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
