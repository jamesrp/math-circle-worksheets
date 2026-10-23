#!/usr/bin/env python3
"""Independent checks of the displayed final Week 76 instances.

Data below were transcribed from final/students.pdf, not its answer checker.
The factor-language closure is exact for bounded length: a child factor of
length <= m has a parent cover of length <= ceil((m+1)/2) <= m for m >= 2.
Closure from A therefore contains all and only factors of generated rows.
This finite check does not replace the guide's infinite nonperiodicity proof.
"""
from itertools import product

RULE = {"A": "AB", "B": "BA"}
INVERSE = {v: k for k, v in RULE.items()}


def grow(word):
    return "".join(RULE[c] for c in word)


def factors(word, length):
    return {word[i:i + length] for i in range(len(word) - length + 1)}


def whole_decode(word):
    if len(word) % 2:
        return None
    pairs = [word[i:i + 2] for i in range(0, len(word), 2)]
    if any(pair not in INVERSE for pair in pairs):
        return None
    return "".join(INVERSE[pair] for pair in pairs)


def history(word):
    result = [word]
    while len(word) > 1:
        word = whole_decode(word)
        result.append(word)
        if word is None:
            break
    return result


def crop_pairings(word):
    """Enumerate every permitted left/right lone-tile choice, not greedy pairing."""
    result = []
    for left, right in product((0, 1), repeat=2):
        stop = len(word) - right
        middle = word[left:stop]
        if len(middle) % 2:
            continue
        parent = whole_decode(middle)
        if parent is not None:
            result.append((word[:left], tuple(middle[i:i + 2] for i in range(0, len(middle), 2)), word[stop:], parent))
    return result


def exact_bounded_language(limit):
    current = {"A"}
    while True:
        expanded = set(current)
        for word in current:
            image = grow(word)
            for size in range(1, min(len(image), limit) + 1):
                expanded.update(factors(image, size))
        if expanded == current:
            return current
        current = expanded


def main():
    rows = ["A"]
    for _ in range(5):
        rows.append(grow(rows[-1]))
    assert rows[:5] == ["A", "AB", "ABBA", "ABBABAAB", "ABBABAABBAABABBA"]
    assert rows[5] == "ABBABAABBAABABBABAABABBAABBABAAB"
    assert factors(rows[4], 3) == {"AAB", "ABA", "ABB", "BAA", "BAB", "BBA"}
    assert factors(rows[3], 3) == factors(rows[4], 3)
    assert len(rows[4]) - 3 + 1 == 14
    assert 16 * 15 < 30 * 10  # 16 tiles of 15 mm fit within 30 cm
    assert 8 + 16 <= 32  # simultaneous old/new rows fit the kit
    assert grow("BA") == "BAAB"  # page 1 and launch visual
    assert whole_decode("BAABBA") == "BAB"  # page 2 visual
    assert crop_pairings("AABBA") == [("A", ("AB", "BA"), "", "AB")]

    claims = ["ABBABAAB", "ABBAABBA", "ABBABBAB", "ABBABAABABBABAAB"]
    expected = [
        ["ABBABAAB", "ABBA", "AB", "A"],
        ["ABBAABBA", "ABAB", "AA", None],
        ["ABBABBAB", None],
        ["ABBABAABABBABAAB", "ABBAABBA", "ABAB", "AA", None],
    ]
    assert [history(word) for word in claims] == expected
    crops = ["ABA", "BAABA", "AABB", "ABBAABBA"]
    expected_pairings = {
        "ABA": [("", ("AB",), "A", "A"), ("A", ("BA",), "", "B")],
        "BAABA": [("", ("BA", "AB"), "A", "BA")],
        "AABB": [("A", ("AB",), "B", "A")],
        "ABBAABBA": [("", ("AB", "BA", "AB", "BA"), "", "ABAB")],
    }
    assert {w: crop_pairings(w) for w in crops} == expected_pairings
    language = exact_bounded_language(10)
    assert all(w in language for w in crops)
    assert "ABBAABBA" in language and history("ABBAABBA")[-1] is None
    assert all(w not in language for w in ("AAA", "BBB", "ABABA", "BABAB", "ABBAABBAAB"))
    five = sorted(w for w in language if len(w) == 5)
    assert all(len(crop_pairings(w)) == 1 for w in five)
    assert len(five) == 12
    assert crop_pairings("ABBAABBAAB") == [("", ("AB", "BA", "AB", "BA", "AB"), "", "ABABA")]
    # Proposed forbidden pieces are actually pieces of the specified forgeries.
    assert "ABABA" in "AB" * 8
    assert "ABBAABBAAB" in "ABBA" * 4
    # Four starts modulo the period exhaust every local test on (ABBA)^infinity.
    periodic = "ABBA" * 4
    for banned in ("AAA", "BBB", "ABABA", "BABAB"):
        assert all(periodic[i:i + len(banned)] != banned for i in range(4))
    # In the fallback game, any one flipped tile invalidates the whole row.
    for row in (rows[2], rows[3]):
        for i, tile in enumerate(row):
            changed = row[:i] + ("B" if tile == "A" else "A") + row[i + 1:]
            assert changed != row
            assert history(changed)[-1] != "A"
    # Local exhaustive checks of the two all-scale lemmas.
    images = [grow("".join(chars)) for chars in product("AB", repeat=3)]
    assert all("AAA" not in s and "BBB" not in s for s in images)
    assert grow(grow("A")) == "ABBA" and grow(grow("B")) == "BAAB"
    # Material/printing counts appearing in the guide.
    assert (32 + 4, 3 * (32 + 4), 4 + 2, 3 * 4 + 2) == (36, 108, 6, 14)
    assert (4 * 4, 5 * 4, 4 * 4 + 5 * 4) == (16, 20, 36)
    print("PASS: final examples, complete pairing cases, exact bounded factor closure and preparation counts.")
    print("P1:", rows[4], "; triples:", ", ".join(sorted(factors(rows[4], 3))))
    for i, chain in enumerate(expected, 1):
        print("P3 row", i, ":", " -> ".join("FAIL" if w is None else w for w in chain))
    for word, pairings in expected_pairings.items():
        print("P4", word, ":", pairings)
    print("P5: all", len(five), "genuine five-letter factors have one pairing.")
    print("P6: ABABA and ABBAABBAAB are forbidden; the latter decodes to ABABA.")
    print("P7: analytic proof in guide; finite computation is not its proof.")


if __name__ == "__main__":
    main()
