"""Row helpers for the Week 63 review: rows by backtracking, home matches,
card->home arrows and cycles, and the two-family deletion/restoration."""


def rows(labels):
    """All rows (card in each home, homes in the given order) by backtracking."""
    out = []

    def rec(prefix, left):
        if not left:
            out.append(''.join(prefix))
            return
        for c in sorted(left):
            rec(prefix + [c], left - {c})
    rec([], set(labels))
    return out


def matches(row, homes):
    return {h for h, c in zip(homes, row) if h == c}


def derangements(labels):
    return [r for r in rows(labels) if not matches(r, labels)]


def arrows(row, homes):
    """card -> home where it sits."""
    return {c: h for h, c in zip(homes, row)}


def cycles(row, homes):
    a = arrows(row, homes)
    seen, cyc = set(), []
    for start in homes:
        if start in seen:
            continue
        c, cur = [], start
        while cur not in seen:
            seen.add(cur)
            c.append(cur)
            cur = a[cur]
        cyc.append(c)
    return cyc


def row_from_arrows(a, homes):
    inv = {h: c for c, h in a.items()}
    return ''.join(inv[h] for h in homes)


def reduce_row(row, homes, z):
    """Two-family deletion for distinguished card z (arrows card->home).
    Returns (family, smaller homes, smaller row)."""
    a = arrows(row, homes)
    h = a[z]
    if a[h] == z:  # reciprocal
        keep = [x for x in homes if x not in (h, z)]
        b = {c: a[c] for c in keep}
        return 'reciprocal', ''.join(keep), row_from_arrows(b, keep)
    x = next(c for c in homes if a[c] == z)
    keep = [y for y in homes if y != z]
    b = {c: a[c] for c in keep}
    b[x] = h
    return 'longer', ''.join(keep), row_from_arrows(b, keep)


def restore(fam, small_homes, small_row, homes, z, h):
    b = arrows(small_row, small_homes)
    if fam == 'reciprocal':
        b[z] = h
        b[h] = z
    else:
        x = next(c for c in small_homes if b[c] == h)
        b[x] = z
        b[z] = h
    return row_from_arrows(b, homes)
