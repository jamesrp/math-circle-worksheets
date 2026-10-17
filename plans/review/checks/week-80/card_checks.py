"""Card-stage checks for Week 80 (Midnight laboratory).

1. The proposed design problem: a card rule on the same marks that settles,
   and a counter rule on the same marks that does not approach one place.
2. The two-direction counter (halfway toward END when the card turns ON,
   halfway toward START when it turns OFF): its positions hover near 1/3 and 2/3.
3. The app variant with a choice (each move halfway toward START or END):
   which places are reachable, by how many sequences, and how the solve goes.
4. Sizes read from students.tex: the p. 3 MIDNIGHT box against the p. 5 card.
"""
from fractions import Fraction as F
from itertools import product

L = 180  # mm between the end ticks on every strip

def marks(n):
    t, out = F(0), []
    for _ in range(n):
        t = (t + 1) / 2
        out.append(t)
    return out

print("Switch marks (mm from 11:00):", [float(m * L) for m in marks(4)])

# 1. A card that flips only at the first two marks settles; one that flips at every mark does not.
def card_states(flip_at, n):
    s, out = 0, []
    for k in range(1, n + 1):
        if flip_at(k):
            s ^= 1
        out.append(s)
    return out
print("Card flipping at marks 1-2 only (1=ON):", card_states(lambda k: k <= 2, 12))
print("Card flipping at every mark:            ", card_states(lambda k: True, 12))
print("Card flipping at even marks only:       ", card_states(lambda k: k % 2 == 0, 12))

# Counter jumping to the other end at each mark: 1, 0, 1, 0, ... never approaches one place.
p, jumps = F(0), []
for _ in range(8):
    p = 1 - p
    jumps.append(p)
print("Counter jumping end to end:", [str(x) for x in jumps])

# 2. Two-direction counter.
p, pos = F(0), []
for k in range(1, 41):
    p = (p + 1) / 2 if k % 2 == 1 else p / 2
    pos.append(p)
print("Two-direction counter, first 6 (mm):", [float(x * L) for x in pos[:6]])
odd, even = pos[0::2], pos[1::2]
print("  odd-move positions -> 2/3? gap after 20:", float(abs(odd[-1] - F(2, 3))))
print("  even-move positions -> 1/3? gap after 20:", float(abs(even[-1] - F(1, 3))))
assert abs(odd[-1] - F(2, 3)) < F(1, 10**10) and abs(even[-1] - F(1, 3)) < F(1, 10**10)
assert all(abs(pos[k + 1] - pos[k]) >= F(1, 4) for k in range(len(pos) - 1))  # every move is at least a quarter of the strip

# 3. Choice variant: from START (0), each move goes halfway toward START (p/2) or END ((p+1)/2).
for n in range(1, 11):
    reach = {}
    for seq in product("SE", repeat=n):
        q = F(0)
        for m in seq:
            q = q / 2 if m == "S" else (q + 1) / 2
        reach.setdefault(q, []).append("".join(seq))
    assert set(reach) == {F(k, 2**n) for k in range(2**n)}, n
    assert all(len(v) == 1 for v in reach.values()), n
    # The unique sequence is the target's binary digits read last to first (E = 1, S = 0).
    for q, (seq,) in reach.items():
        k = q * 2**n
        bits = format(int(k), f"0{n}b")
        assert seq == "".join("E" if b == "1" else "S" for b in reversed(bits)), (q, seq)
print("Choice variant: after n moves (n <= 10) the places are exactly k/2^n, 0 <= k < 2^n,"
      " each by exactly one sequence: the binary digits of k read backwards.")
# Working backwards is the doubling map: if the target is at least 1/2 the last move was toward END.
q, back = F(13, 32), []
while q != 0:
    if q >= F(1, 2):
        back.append("E"); q = 2 * q - 1
    else:
        back.append("S"); q = 2 * q
print("Example 13/32 of the way (73.125 mm): moves", "".join(reversed(back)))

# 4. Sizes from students.tex.
box = (125 - 59, 65 - 12)
card = (88 - 12, 54 - 0)
print("p. 3 MIDNIGHT box (mm):", box, " p. 5 ON/OFF panel (mm):", card)
assert box[0] < card[0]
print("All checks passed.")
