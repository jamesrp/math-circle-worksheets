"""Independent single-vertex flat-folding oracle (written for this review).

Two separate methods:

1. brute force over layer orders.  A flat-folded single vertex is modelled
   by its angular image: ray 1 goes to direction 0, and each sector is swept
   alternately forward/backward (reflection at every crease).  When the
   alternating sums agree the image closes up and spans at most 180 degrees,
   so it is a 1-D problem on a line.  A global bottom-to-top order of the
   sectors is enough (interval graphs are chordal, so any consistent local
   layering extends to a total order).  An order is legal when
     (a) no sector whose open interval contains a crease position lies
         strictly between the two sectors joined there (taco-tortilla);
     (b) two creases at one position on the same side do not interleave
         (taco-taco);
     (c) two creases at one position on opposite sides have disjoint height
         ranges (the outer fold would have to wrap through the other).
   The mountain/valley word is read off the order: odd sectors face up,
   even sectors face down; a crease is V when the face-down sector is above
   the face-up one (front faces toward each other).

2. the crimp reduction (Bern-Hayes / Hull): repeatedly crimp a sector that
   is no larger than its neighbours and whose two creases differ; finish
   with a straight fold (two equal labels).  This is a separate theorem
   used only as a cross-check of method 1.

Angles are integers (degrees) or Fractions.  Words list rays 1..n in
clockwise order; ray k lies between sector k-1 and sector k (ray 1 between
the last sector and sector 1).
"""
from itertools import permutations, product


def kawasaki(angles):
    n = len(angles)
    if n % 2:
        return False
    odd = sum(angles[0::2])
    even = sum(angles[1::2])
    return odd == even


def folded_image(angles):
    """Crease positions, sector intervals and facing (+1 up, -1 down)."""
    n = len(angles)
    theta = [0]
    s = [1 if k % 2 == 0 else -1 for k in range(n)]
    for k in range(n):
        theta.append(theta[-1] + s[k] * angles[k])
    if theta[-1] != 0:
        return None
    theta = theta[:n]
    iv = []
    for k in range(n):
        a, b = theta[k], theta[(k + 1) % n]
        iv.append((min(a, b), max(a, b)))
    return theta, iv, s


def word_from_heights(h, s):
    n = len(h)
    w = []
    for k in range(n):
        i, j = (k - 1) % n, k          # sectors joined at ray k
        up, down = (i, j) if s[i] == 1 else (j, i)
        w.append('V' if h[down] > h[up] else 'M')
    return ''.join(w)


def legal(h, theta, iv, s):
    n = len(h)
    creases = []
    for k in range(n):
        i, j = (k - 1) % n, k
        x = theta[k]
        side = s[k]  # both sectors extend from x in direction s[k]
        lo, hi = sorted((h[i], h[j]))
        # (a) taco-tortilla
        for m in range(n):
            if m in (i, j):
                continue
            a, b = iv[m]
            if a < x < b and lo < h[m] < hi:
                return False
        creases.append((x, side, lo, hi))
    for p in range(n):
        for q in range(p + 1, n):
            x1, s1, l1, h1 = creases[p]
            x2, s2, l2, h2 = creases[q]
            if x1 != x2:
                continue
            if s1 == s2:
                # (b) no interleaving
                inside = (l1 < l2 < h1) + (l1 < h2 < h1)
                if inside == 1:
                    return False
            else:
                # (c) opposite sides: height ranges must be disjoint
                if not (h1 < l2 or h2 < l1):
                    return False
    return True


def legal_orders(angles):
    """All (bottom-to-top order, word) pairs.  Order lists sector numbers 1..n."""
    img = folded_image(angles)
    if img is None:
        return []
    theta, iv, s = img
    n = len(angles)
    out = []
    for perm in permutations(range(n)):      # perm[pos] = sector at height pos
        h = [0] * n
        for pos, sec in enumerate(perm):
            h[sec] = pos
        if legal(h, theta, iv, s):
            out.append((''.join(str(x + 1) for x in perm), word_from_heights(h, s)))
    return out


def valid_words(angles):
    return sorted({w for _, w in legal_orders(angles)})


def order_word(angles, order):
    """Word of a given bottom-to-top order string such as '3412'; None if illegal."""
    theta, iv, s = folded_image(angles)
    n = len(angles)
    h = [0] * n
    for pos, ch in enumerate(order):
        h[int(ch) - 1] = pos
    if not legal(h, theta, iv, s):
        return None
    return word_from_heights(h, s)


def crimp_foldable(angles, word):
    a = list(angles)
    w = list(word)
    if len(a) % 2 or not kawasaki(a):
        return False
    while len(a) > 2:
        n = len(a)
        for i in range(n):
            if a[i] <= a[i - 1] and a[i] <= a[(i + 1) % n] and w[i] != w[(i + 1) % n]:
                r = (i - 1) % n
                a2 = a[r:] + a[:r]
                w2 = w[r:] + w[:r]
                a = [a2[0] - a2[1] + a2[2]] + a2[3:]
                w = [w2[0]] + w2[3:]
                break
        else:
            return False
    return w[0] == w[1]


def crimp_words(angles):
    n = len(angles)
    return sorted(''.join(t) for t in product('MV', repeat=n) if crimp_foldable(angles, ''.join(t)))


def maekawa(word):
    return abs(word.count('M') - word.count('V')) == 2
