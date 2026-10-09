#!/usr/bin/env python3
"""Independent Week 82 checks; standard library only, no author imports.

The finite permutation check is exhaustive. Infinite formulas have explicit
inverses, whose general proofs are in review-math.md; finite replays here are
regression checks and do not establish an infinite theorem by themselves.
"""
from itertools import permutations, combinations
from pathlib import Path
import os
import hashlib
import json


def keeps_order(p):
    return all(p[i] < p[j] for i, j in combinations(range(len(p)), 2))


def extra_to_plain(x):
    return 1 if x == "star" else x + 1


def plain_to_extra(n):
    assert n >= 1
    return "star" if n == 1 else n - 1


def blocks_to_plain(x):
    color, n = x
    assert color in ("R", "B") and n >= 1
    return 2 * n - (1 if color == "R" else 0)


def plain_to_blocks(m):
    assert m >= 1
    return ("R", (m + 1) // 2) if m % 2 else ("B", m // 2)


def normal_form(tokens):
    """For finite concatenations of omega rows and stars: omega*k + tail.

    Appending an omega row absorbs any finite trailing block, because an
    order-preserving shift matches that finite block + omega to omega.
    """
    k = tail = 0
    for token in tokens:
        if token == "W":
            k += 1
            tail = 0
        else:
            assert token == "star"
            tail += 1
    return (k, tail)


def main():
    matches = list(permutations((1, 2, 3)))
    ordered = [p for p in matches if keeps_order(p)]
    assert len(matches) == 6
    assert ordered == [(1, 2, 3)]
    # Why checking just one pair would be wrong:
    assert (1, 3, 2)[0] < (1, 3, 2)[1]
    assert not keeps_order((1, 3, 2))

    # Both prepended and appended extra-customer queues admit the same
    # unrestricted bijection. Only the prepended version respects order.
    for n in range(1, 10001):
        assert extra_to_plain(plain_to_extra(n)) == n
        assert plain_to_extra(extra_to_plain(n)) == n
    assert plain_to_extra(extra_to_plain("star")) == "star"
    before = ["star", *range(1, 101)]
    assert all(extra_to_plain(before[i]) < extra_to_plain(before[j])
               for i, j in combinations(range(len(before)), 2))
    # An appended star must follow customer 1, but the bijection puts it first.
    assert extra_to_plain("star") < extra_to_plain(1)

    # D -> E is the identity on the named customers, a bijection with identity
    # inverse, while its ordinal orders differ. E's positional ranks are below.
    for m in range(1, 10001):
        assert blocks_to_plain(plain_to_blocks(m)) == m
    for color in ("R", "B"):
        for n in range(1, 10001):
            assert plain_to_blocks(blocks_to_plain((color, n))) == (color, n)
    # D orders R2 before B1; E orders B1 before R2.
    assert blocks_to_plain(("B", 1)) < blocks_to_plain(("R", 2))

    # The invention task has valid different representations of equal and
    # unequal order types. List all 16 unlabeled block/star arrangements.
    arrangements = set()
    for rows in (1, 2):
        for stars in range(3):
            arrangements.update(permutations(("W",) * rows + ("star",) * stars))
    assert len(arrangements) == 16
    assert {normal_form(a) for a in arrangements} == {
        (k, t) for k in (1, 2) for t in range(3)
    }
    assert normal_form(("star", "W")) == normal_form(("W",))
    assert normal_form(("W", "star")) != normal_form(("W",))
    assert normal_form(("W", "star", "W")) == normal_form(("W", "W"))

    root = Path(__file__).resolve().parent
    sources = [root / "student/students.tex", root / "guide/facilitator.tex"]
    result = {
        "status": "PASS",
        "finite_bijections": [list(p) for p in matches],
        "finite_order_preserving": [list(p) for p in ordered],
        "infinite_inverse_replay_range": "1..10000; general inverse arguments in review-math.md",
        "invention_arrangements": len(arrangements),
        "invention_order_types": 6,
        "visual_review": "See release report; this script does not render PDFs.",
        "limitations": "No physical fit, classroom, or print rehearsal; symbolic order arguments are ordinary mathematics, not proof-assistant checked.",
        "reviewed_inputs": {
            str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sources
        },
    }
    Path(os.environ.get("INFINITY_CHECK_OUT", "math-check-results.json")).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
