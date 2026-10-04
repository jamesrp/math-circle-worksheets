"""Answer check for the final Week 4 packets (prints the answers; asserts the ones the pages rely on)."""
from math import gcd
import os

A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PICS = ['sun', 'moon', 'heart', 'tree', 'fish', 'house']  # clockwise from the top


def enc(s, k):
    return ''.join(A[(A.index(c) + k) % 26] if c in A else c for c in s)


def pieces(n, k):
    seen, out = set(), []
    for s in range(n):
        if s in seen:
            continue
        cyc, j = [s], (s + k) % n
        seen.add(s)
        while j != s:
            cyc.append(j)
            seen.add(j)
            j = (j + k) % n
        out.append(cyc)
    return out


def chords(n, k):
    return {frozenset((i, (i + k) % n)) for i in range(n)}


def reach(n, k):  # dots reached from the black dot before getting back
    return len(pieces(n, k)[0])


# ---------------------------------------------------------------- K-1
for n in (4, 5, 6):
    print(f"K1 P1-P3 ring {n}: lands on every dot:", [k for k in (1, 2, 3) if reach(n, k) == n])
print("K1 P4 starts:", [(n, k, len(pieces(n, k))) for n, k in [(6, 2), (6, 3), (8, 2), (8, 3)]])
assert [len(pieces(n, k)) for n, k in [(6, 2), (6, 3), (8, 2), (8, 3)]] == [2, 3, 2, 1]
for name, n, k in [('pentagon', 5, 1), ('5-star', 5, 2), ('hexagon', 6, 1), ('6-star', 6, 2), ('3 lines', 6, 3)]:
    print("K1 P5", name, [h for h in range(1, 6) if h % n and chords(n, h) == chords(n, k)])
print("K1 P6-P7 ring 7: lands on every dot:", [k for k in range(1, 7) if reach(7, k) == 7])
rows, r = [], ['sun', 'tree', 'fish']
for _ in range(3):
    r = [PICS[(PICS.index(x) + 2) % 6] for x in r]
    rows.append(r)
print("K1 P8 rows:", rows)
assert rows[-1] == ['sun', 'tree', 'fish']
print("K1 P9 hop back:", [(6 - k) % 6 for k in (1, 2, 3, 4)])
secret = [k for k in range(6) if PICS[k] == 'tree'][0]
print("K1 P10 secret hop", secret, [(x, PICS[(PICS.index(x) + secret) % 6]) for x in ['moon', 'heart', 'fish', 'house']])

# ---------------------------------------------------------------- 2-3
print("23 P1 starts:", [len(pieces(8, k)) for k in (1, 2, 3, 4)])
print("23 P2 starts:", [len(pieces(10, k)) for k in (2, 3, 4, 5)])
print("23 P3 starts:", [len(pieces(12, k)) for k in range(2, 7)])
print("23 P4:", [enc(w, 3) for w in ["STAR", "FOX", "WHEEL", "PENCIL", "I CAN DRAW A STAR"]], enc("CAT", 3))
assert enc("CAT", 3) == "FDW"
print("23 P6 starts:", [(n, k, len(pieces(n, k))) for n, k in [(9, 2), (15, 5), (16, 6), (12, 8)]])
for n in (9, 16, 18, 15):
    print("23 P7 hops > 3 with 3 starts on", n, [k for k in range(4, n) if len(pieces(n, k)) == 3])
print("23 P8 codes:", enc("A STAR CAN HAVE TEN POINTS", 7), "|", enc("MEET ME BY THE BIG TREE", 16))
print("23 P9:", [(s, A[(26 - A.index(s)) % 26]) for s in "DHNW"])

# ---------------------------------------------------------------- 4-5
print("45 P1 pieces:", [len(pieces(12, k)) for k in range(1, 7)])
print("45 P2 pieces:", [len(pieces(n, k)) for n, k in [(10, 4), (9, 6), (15, 10), (16, 12), (18, 8), (24, 9)]])
print("45 P3 pieces:", [(n, k, gcd(n, k)) for n, k in [(20, 8), (24, 10), (30, 12), (36, 27), (17, 5), (100, 35), (60, 45)]])
print("45 P4:", enc("I DREW A STAR WITH TWELVE POINTS", 9), "|", enc("WE MEET AT NOON BY THE BIG TREE", 18),
      "|", enc("BALLOON", 23), "|", enc("CHEER", 10), enc("JOLLY", 3))
print("45 P6:", [(a, b, A[(A.index(a) + b_) % 26]) for a, b in ["HK", "DF", "TM", "PL"] for b_ in [A.index(b)]],
      "H then", A[(26 - 7) % 26])
print("45 P8:", [n for n in range(4, 21) if all(gcd(n, k) == 1 for k in range(1, n))])
for n, k in [(15, 6), (20, 5), (14, 6), (21, 6)]:
    g = gcd(n, k)
    print("45 P9", n, "dots: hops", [h for h in range(1, n) if chords(n, h) == chords(n, k)],
          f"= {g} pieces of {{{n // g}/{min(k // g, n // g - k // g)}}}")
print("45 P11:", [A[k] for k in range(1, 26) if gcd(26, k) == 1], "setting C cycle length", 26 // gcd(26, 2))
print("45 P12 x2 fixed dots:", [m for m in range(24) if 2 * m % 24 == m], "x3 fixed dots:",
      [m for m in range(24) if 3 * m % 24 == m], "13 ->", 2 * 13 % 24)

# ---------------------------------------------------------------- crack checks against a word list
DIC = '/usr/share/hunspell/en_US.dic'
if os.path.exists(DIC):
    words = set()
    for line in open(DIC, encoding='latin-1').read().splitlines()[1:]:
        w = line.split('/')[0]
        if w.isalpha() and (w.islower() or len(w) == 1):
            words.add(w.upper())
    words |= {'A', 'I'}
    for msg, k in [("A STAR CAN HAVE TEN POINTS", 7), ("MEET ME BY THE BIG TREE", 16),
                   ("I DREW A STAR WITH TWELVE POINTS", 9), ("WE MEET AT NOON BY THE BIG TREE", 18),
                   ("BALLOON", 23), ("CHEER", 10)]:
        code = enc(msg, k)
        ok = lambda w: w in words or (w.endswith('S') and w[:-1] in words)  # allow plurals of listed stems
        hits = [(A[s], enc(code, -s)) for s in range(26) if all(ok(w) for w in enc(code, -s).split())]
        print("crack", code, "->", hits)
