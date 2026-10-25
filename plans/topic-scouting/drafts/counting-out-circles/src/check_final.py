"""Literal simulation of the counting-out game on a fixed ring of spots:
standing counters take turns with a repeating chant ('stand, sit' or
'stand, stand, sit'); the chant carries on across laps; sitting counters
are skipped. Checks every answer used in the final packets."""

def play(n, k):
    standing = [True] * (n + 1)
    standing[0] = False
    chant = 0          # position in the chant, carried across laps
    left = n
    order = []
    spot = 1
    while left > 1:
        if standing[spot]:
            chant += 1
            if chant % k == 0:
                standing[spot] = False
                order.append(spot)
                left -= 1
        spot = spot % n + 1
    return next(i for i in range(1, n + 1) if standing[i]), order

J2 = lambda n: play(n, 2)[0]
J3 = lambda n: play(n, 3)[0]

# shared facts
assert [J2(n) for n in range(1, 17)] == [1,1,3,1,3,5,7,1,3,5,7,9,11,13,15,1]
assert [J3(n) for n in range(1, 25)] == [1,2,2,1,4,1,4,7,1,4,7,10,13,2,5,8,11,14,17,20,2,5,8,11]
for n in range(1, 1025):
    m = n.bit_length() - 1
    assert J2(n) == 2 * (n - 2**m) + 1
    b = bin(n)[2:]
    assert J2(n) == int(b[1:] + b[0], 2)

# K-1
print("K-1 P1/P2 circles 3..10:", [J2(n) for n in range(3, 11)])
print("K-1 P3 star circles (1 last, among 3..10,16):", [n for n in list(range(3, 11)) + [16] if J2(n) == 1], "J2(16) =", J2(16))
print("K-1 P4 number 3 last in:", [n for n in list(range(3, 11)) + [16] if J2(n) == 3],
      " number 5 last in:", [n for n in list(range(3, 11)) + [16] if J2(n) == 5])
assert all(J2(n) != 2 for n in range(1, 2001))
print("K-1 P6 stand,stand,sit 3..8:", [J3(n) for n in range(3, 9)])
print("K-1 P7 stand,stand,sit circle of 9:", J3(9), play(9, 3)[1])
assert all(J3(n) % 3 != 0 for n in range(1, 2001))
print("number 3 (and every multiple of 3) never last with stand,stand,sit up to 2000: ok")

# grades 2-3
print("2-3 P2:", {n: J2(n) for n in (20, 25, 32)})
print("2-3 P5 number 9 up to 40:", [n for n in range(1, 41) if J2(n) == 9],
      " J(n)=n up to 40:", [n for n in range(1, 41) if J2(n) == n])
print("2-3 P6:", {n: J2(n) for n in (50, 100)})
print("2-3 P8 checks:", {n: J3(n) for n in (14, 20)}, " P9 J3(30) =", J3(30))

# grades 4-5
print("4-5 P3 J=1 up to 100:", [n for n in range(1, 101) if J2(n) == 1])
print("4-5 P4:", {n: J2(n) for n in (100, 1000)})
print("4-5 P5:", {n: J2(n) for n in (26, 52, 53)})
print("4-5 P6 number 23:", [n for n in range(1, 101) if J2(n) == 23],
      " number 22:", [n for n in range(1, 101) if J2(n) == 22])
print("4-5 P8 checks:", {n: J3(n) for n in (14, 21)}, " P9 J3(41) =", J3(41))
print("4-5 P10 example: J(12) =", J2(12), bin(12), bin(J2(12)))
# rival rules ruled out by the n = 12 example
rev = int(bin(12)[2:][::-1], 2)
print("   reversal of 1100 gives", rev, "(not 9)")
# launch sizes
for n in (8, 10, 11):
    print("launch n =", n, "sitting order", play(n, 2)[1], "last", J2(n))
