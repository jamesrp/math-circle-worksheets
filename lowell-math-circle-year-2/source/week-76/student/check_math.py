#!/usr/bin/env python3
"""Finite checks for every fixed string printed in students.tex (standard library)."""
from itertools import product
from pathlib import Path
import re

RULE = {"A": "AB", "B": "BA"}
INVERSE = {v: k for k, v in RULE.items()}


def grow(word):
    return "".join(RULE[c] for c in word)


def generation(n):
    word = "A"
    for _ in range(n):
        word = grow(word)
    return word


def decode(word):
    if len(word) % 2:
        return None
    pairs = [word[i:i+2] for i in range(0, len(word), 2)]
    return "".join(INVERSE[p] for p in pairs) if all(p in INVERSE for p in pairs) else None


def whole_history(word):
    rows = [word]
    while len(word) > 1:
        word = decode(word)
        if word is None:
            return rows, False
        rows.append(word)
    return rows, word == "A"


def pairings(word):
    """All immediate complete-pair placements with at most one lone tile per end.

    A returned placement is locally pairable. It does not certify that this
    placement has an ancestry in a row generated from A.
    """
    result = []
    for offset in (0, 1):
        stop = len(word) - ((len(word) - offset) % 2)
        pairs = [word[i:i+2] for i in range(offset, stop, 2)]
        if pairs and all(p in INVERSE for p in pairs):
            result.append((offset, len(word) - stop, "".join(INVERSE[p] for p in pairs)))
    return result


def factor_language(length):
    """Exact factor set, from a substitution-invariant collection of blocks.

    The four two-letter factors all occur in generation 3. Substitute each
    complete two-letter factor until each expanded letter has length >= n.
    Any n-letter factor meets at most two such expanded letters, so it is in
    one of these blocks. Conversely each such block occurs in the fixed word.
    Thus this is an exact finite computation, not an assumed sampling cutoff.
    """
    parents = ("AA", "AB", "BA", "BB")
    assert all(p in generation(3) for p in parents)
    expansions = list(parents)
    letter_length = 1
    while letter_length < length:
        expansions = [grow(w) for w in expansions]
        letter_length *= 2
    return {w[i:i+length] for w in expansions for i in range(len(w)-length+1)}


def main():
    assert generation(0) == "A"
    assert generation(1) == "AB"
    assert generation(2) == "ABBA"
    assert generation(3) == "ABBABAAB"
    assert generation(4) == "ABBABAABBAABABBA"
    # Convention visuals are examples independent of the task rows.
    assert grow("BA") == "BAAB"
    assert decode("BAABBA") == "BAB"
    assert pairings("AABBA") == [(1, 0, "AB")]
    # Problem 1: all three-tile factors are already present in the 16-tile row.
    triples = {generation(4)[i:i+3] for i in range(14)}
    assert triples == {"AAB", "ABA", "ABB", "BAA", "BAB", "BBA"}
    assert triples == factor_language(3)
    # Problem 2: exact factor language excludes both three-of-a-kind words.
    assert not {"AAA", "BBB"} & factor_language(3)
    # Problem 3: whole-row claims. The false claims are not all false crops.
    whole_cases = {
        "ABBABAAB": (["ABBABAAB", "ABBA", "AB", "A"], True),
        "ABBAABBA": (["ABBAABBA", "ABAB", "AA"], False),
        "ABBABBAB": (["ABBABBAB"], False),
        "ABBABAABABBABAAB": (["ABBABAABABBABAAB", "ABBAABBA", "ABAB", "AA"], False),
    }
    for row, expected in whole_cases.items():
        assert whole_history(row) == expected, (row, whole_history(row))
    # Problem 4: all supplied crops are genuine. Report only complete parents.
    crops = {
        "ABA": [(0, 1, "A"), (1, 0, "B")],
        "BAABA": [(0, 1, "BA")],
        "AABB": [(1, 1, "A")],
        "ABBAABBA": [(0, 0, "ABAB")],
    }
    for row, expected in crops.items():
        assert row in factor_language(len(row)), row
        assert pairings(row) == expected, (row, pairings(row))
    # Both alignments of ABA really do occur in A-grown rows, not just locally.
    word = generation(6)
    assert {i % 2 for i in range(len(word)-2) if word[i:i+3] == "ABA"} == {0, 1}
    # Problem 5: every genuine length-five crop has precisely one alignment.
    five = factor_language(5)
    assert "ABABA" not in five and "BABAB" not in five
    assert all(len(pairings(w)) == 1 for w in five)
    both = {"".join(w) for w in product("AB", repeat=5) if len(pairings("".join(w))) == 2}
    assert both == {"ABABA", "BABAB"}
    # Problem 6: explicit repeating rows and short witnesses of impossibility.
    repeat_ab = "AB" * 8
    repeat_abba = "ABBA" * 4
    assert repeat_ab == "ABABABABABABABAB"
    assert repeat_abba == "ABBAABBAABBAABBA"
    assert "ABABA" in repeat_ab and "ABABA" not in factor_language(5)
    assert "ABBAABBAA" in repeat_abba
    assert "ABBAABBAA" not in factor_language(9)
    # ABBA repetition passes the immediate three/five-letter forbidden checks.
    periodic_sample = "ABBA" * 32
    assert all(w not in periodic_sample for w in ("AAA", "BBB", "ABABA", "BABAB"))
    # Every fixed row in the diagram source must belong to this audited set.
    source = Path(__file__).with_name("students.tex").read_text()
    printed = {s.replace(",", "") for s in re.findall(r"\\Strip\{[^}]*\}\{[^}]*\}\{([AB,]+)\}", source)}
    audited = {"A", "B", "AB", "BA", "BAAB", "BAABBA", "BAB", "AABBA"} | set(whole_cases) | set(crops) | {repeat_ab, repeat_abba}
    assert printed <= audited, (printed - audited)
    print("PASS: convention diagrams; all whole-row claims; all cut examples; exact factors; repeating-strip witnesses.")
    print("Finite checks do not constitute the infinite nonperiodicity argument or a classroom trial.")


if __name__ == "__main__":
    main()
