#!/usr/bin/env python3
"""Independent mathematical audit for Week 76 final revision (standard library only).

This file was written independently of the author's check_math.py.  It does not
import or execute that checker.  It can live beside students.tex in a portable
source package, or beside final/src in a review run.  Run:

    python3 independent_check.py [--source /path/to/students.tex]

Independent model and completeness certificate
----------------------------------------------
Write A=0 and B=1.  Define t(n) as the parity of the number of 1 bits of n.
Then t(2n)=t(n), t(2n+1)=1-t(n), and t(0)=0, so these values are precisely the
A-grown rows.  This is a random-access model, not a substitution simulation.

For any requested factor length L, choose a power of two m >= L.  A length-L
factor crosses at most two consecutive aligned m-blocks.  Each block is the
parity prefix of length m, or its complement; its type is its parent's letter.
All four parent digrams AA, AB, BA, BB occur in t[0:8].  Consequently every
length-L factor occurs inside the images of those four digrams.  Conversely
all those images occur in the genuine sequence.  Enumerating those images is
therefore an EXACT factor-language computation, not a long-prefix heuristic.
It also supplies genuine positions and preserves the parity of each position.

General proof audit (these are proofs, not conclusions from finite tests)
------------------------------------------------------------------------
* A replacement doubles length and preserves the old prefix when starting at
  A: mu(A)=AB begins with A, and applying mu preserves a prefix relation.
  Thus the infinite limit is well-defined.
* Every aligned child-pair contains different letters.  Any three consecutive
  positions contain a full aligned pair, so AAA and BBB cannot occur.
* ABABA beginning at an even position forces parent letters AAA, by taking
  the first child of three pairs.  Beginning at an odd position forces BBB,
  by taking their second children.  BABAB gives the complementary argument.
  This uses the forced mates just outside the crop when needed, not an
  assumption that a cut edge is a generation boundary.
* Two valid pair alignments of a length-five crop require every neighboring
  pair to differ.  That means ABABA or BABAB.  Both are impossible, while a
  genuine crop always has its inherited alignment.  Therefore its alignment
  is unique; the same holds for every longer crop.
* The repeated-ABBA strip has neither constant triples nor alternating fives.
  Nevertheless its crop BBAABBAA has the only possible complete pairs
  B | BA | AB | BA | A.  Decoding gives BAB, with the two edge letters forcing
  neighboring parent A's: ABABA, impossible.  The complementary witness is
  AABBAABB.  A longer, simpler witness ABBAABBAAB fully decodes to ABABA.
* No eventual period exists.  Every aligned four-letter block is ABBA or
  BAAB, giving equal neighbors beginning at index 4n+1 arbitrarily far out.
  Equal neighbors cannot start at an even index.  An odd eventual period
  shifts an equal pair to an even start, a contradiction.  If an eventual
  period is 2q after position N, then t(2n)=t(2n+2q) for all 2n>=N; hence
  t(n)=t(n+q), so q is an eventual period.  Repeated halving of a positive
  period reaches an odd one, already excluded.  This proves the tail claim,
  not merely non-repetition of a tested finite prefix.

The finite checks below supplement these arguments.  They cannot, by
running alone, prove an assertion about all possible eventual periods.
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
from pathlib import Path


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def letter(index):
    require(index >= 0, "Negative sequence index")
    return "B" if bin(index).count("1") % 2 else "A"


def prefix(size):
    return "".join(letter(n) for n in range(size))


def complement(word):
    return word.translate(str.maketrans("AB", "BA"))


def substitute(word):
    # Used only to cross-check the independent parity model and worked visuals.
    return "".join(c + complement(c) for c in word)


def words(length):
    return ("".join(x) for x in itertools.product("AB", repeat=length))


def exact_factors(length):
    """Return every legal factor with certified witness positions, all parities.

    Completeness is the two-block proof in the module docstring.  The returned
    positions are genuine positions in the parity sequence, not test offsets.
    """
    require(length >= 1, "Factor length must be positive")
    m = 1
    while m < length:
        m *= 2
    base = prefix(8)
    parent_positions = {w: base.find(w) for w in words(2)}
    require(all(i >= 0 for i in parent_positions.values()), "Missing parent digram")
    blocks = {"A": prefix(m), "B": complement(prefix(m))}
    result = {}
    for parent, j in parent_positions.items():
        image = blocks[parent[0]] + blocks[parent[1]]
        expected_image = "".join(letter(j * m + k) for k in range(2 * m))
        require(image == expected_image, "Two-block certificate failed")
        for offset in range(2 * m - length + 1):
            factor = image[offset:offset + length]
            result.setdefault(factor, set()).add(j * m + offset)
    return result


def alignments(word):
    """All covers by consecutive unlike pairs, with at most one tile per edge."""
    found = []
    for left_count in (0, 1):
        if left_count > len(word):
            continue
        pairs = tuple(word[i:i + 2] for i in range(left_count, len(word) - 1, 2))
        if any(pair not in ("AB", "BA") for pair in pairs):
            continue
        right_start = left_count + 2 * len(pairs)
        found.append({
            "offset": left_count,
            "left": word[:left_count],
            "pairs": list(pairs),
            "right": word[right_start:],
            "parent": "".join(pair[0] for pair in pairs),
        })
    return found


def whole_history(word):
    history = [word]
    while len(word) > 1:
        if len(word) % 2:
            return False, history, "odd length"
        pairs = [word[i:i + 2] for i in range(0, len(word), 2)]
        if any(pair not in ("AB", "BA") for pair in pairs):
            return False, history, "contains a forbidden aligned child-pair"
        word = "".join(pair[0] for pair in pairs)
        history.append(word)
    return word == "A", history, "root " + word


def expected_source_diagrams():
    # All literal Strip calls, in PDF/source reading order, including examples.
    return [
        ["BA", "BA", "AB", "BAAB"],
        ["BAABBA", "BA", "AB", "BA", "BAB", "ABBABAAB", "ABBAABBA",
         "ABBABBAB", "ABBABAABABBABAAB"],
        ["AABBA", "AB", "BA", "AB", "ABA", "BAABA", "AABB", "ABBAABBA"],
        ["AB" * 8, "ABBA" * 4],
    ]


def check_source(path):
    if path is None:
        return "No source supplied; mathematical checks only."
    source = path.read_text(encoding="utf-8")
    pages = source.split(r"\begin{document}", 1)[1].split(r"\newpage")
    require(len(pages) == 4, "Expected four student pages")
    pattern = re.compile(r"\\Strip\{([0-9.]+)\}\{([0-9.]+)\}\{([AB,]+)\}\{([0-9.]+)\}")
    diagram_count = 0
    for page, expected in zip(pages, expected_source_diagrams()):
        entries = pattern.findall(page)
        actual = [entry[2].replace(",", "") for entry in entries]
        require(actual == expected, "A displayed fixed strip differs from reviewed data")
        for x, y, comma_word, size in entries:
            x, y, size = float(x), float(y), float(size)
            require(size > 0, "Nonpositive cell size")
            require(0 <= x <= x + size * len(comma_word.split(",")) <= 183,
                    "Strip exceeds horizontal canvas")
            require(0 <= y <= y + size <= 235, "Strip exceeds vertical canvas")
        diagram_count += len(entries)
    require(r"\Blank{11}{105}{16}{10}" in pages[0], "Problem 1 needs a 16-tile row")
    require(r"\foreach \x in {9,54,99,144}{\Blank{\x}{130}{3}{10}\Blank{\x}{153}{3}{10}}"
            in pages[0], "Expected eight three-tile recording spaces")
    require(r"\node[font=\large,inner sep=0pt] at (68,46) {A};" in pages[2],
            "The crop example's lone tile must be A")
    labels = [int(x) for x in re.findall(r"Problem (\d+):", source)]
    require(labels == list(range(1, 8)), "Problem numbering mismatch")
    return {"fixed_strips": diagram_count, "pages": 4, "geometry": "within canvas"}


def run(source_path=None):
    results = {}
    # Parity recurrence is a general identity; test a substantial finite range
    # as an implementation check, never as the proof of that identity.
    for n in range(4096):
        require(letter(2 * n) == letter(n), "Even-index recurrence")
        require(letter(2 * n + 1) == complement(letter(n)), "Odd-index recurrence")
    for generation in range(12):
        row = prefix(2 ** generation)
        require(substitute(row) == prefix(2 ** (generation + 1)), "Generation mismatch")
    results["source"] = check_source(source_path)
    results["intro_example"] = {"input": "BA", "output": substitute("BA")}
    require(substitute("BA") == "BAAB", "Intro example")

    row16 = prefix(16)
    triples = sorted({row16[i:i + 3] for i in range(14)})
    require(row16 == "ABBABAABBAABABBA", "16-letter row")
    require(triples == ["AAB", "ABA", "ABB", "BAA", "BAB", "BBA"], "Triple set")
    require(set(triples) == set(exact_factors(3)), "The 16-row misses a legal triple")
    results["problem_1"] = {"asks": "Grow 16 tiles and list distinct triples",
                             "row": row16, "triples": triples, "count": len(triples)}
    require("AAA" not in exact_factors(3) and "BBB" not in exact_factors(3), "Constant triple")
    results["problem_2"] = {"asks": "Can constant triples appear?", "answer": "Neither can"}

    require(substitute("BAB") == "BAABBA", "Decoding demonstration")
    candidates = expected_source_diagrams()[1][5:]
    histories = [whole_history(word) for word in candidates]
    require([h[0] for h in histories] == [True, False, False, False], "Whole-row decisions")
    results["problem_3"] = {"asks": "Which claims are whole rows from A?",
        "cases": [{"word": w, "genuine_whole_row": h[0], "history": h[1], "stop": h[2]}
                  for w, h in zip(candidates, histories)]}
    # Exhaustively compare inverse decoding with direct whole-row recognition,
    # including lengths that cannot be generated from a single tile.
    for length in range(1, 17):
        expected_whole = prefix(length) if length & (length - 1) == 0 else None
        for word in words(length):
            require(whole_history(word)[0] == (word == expected_whole), "Decoder classification")

    crop_demo = alignments("AABBA")
    require(crop_demo == [{"offset": 1, "left": "A", "pairs": ["AB", "BA"],
                          "right": "", "parent": "AB"}], "Cut-edge demonstration")
    crops = ["ABA", "BAABA", "AABB", "ABBAABBA"]
    expected_parents = [["A", "B"], ["BA"], ["A"], ["ABAB"]]
    crop_results = []
    for crop, parents in zip(crops, expected_parents):
        alternatives = alignments(crop)
        require([a["parent"] for a in alternatives] == parents, "Crop parent set")
        witnesses = exact_factors(len(crop)).get(crop, set())
        require(witnesses, "A claimed genuine crop is absent")
        for alignment in alternatives:
            require(any(i % 2 == alignment["offset"] for i in witnesses),
                    "A local crop pairing has no genuine global occurrence")
        crop_results.append({"crop": crop, "first_witness": min(witnesses),
                             "alignments": alternatives})
    require(alignments("AABB") == [{"offset": 1, "left": "A", "pairs": ["AB"],
                                  "right": "B", "parent": "A"}],
            "Final crop must use one lone tile at each end")
    require("AABBA" in exact_factors(5), "Worked crop is not genuine")
    results["problem_4"] = {"asks": "Find every crop pairing and decode complete pairs",
                             "cases": crop_results}

    ambiguous_fives = sorted(w for w in words(5) if len(alignments(w)) == 2)
    require(ambiguous_fives == ["ABABA", "BABAB"], "Unexpected ambiguous five")
    legal_fives = exact_factors(5)
    require(all(len(alignments(w)) == 1 for w in legal_fives), "Nonunique genuine five")
    require(not set(ambiguous_fives).intersection(legal_fives), "Alternating five is genuine")
    # This finite suite also verifies all legal crop alignments through length 16.
    for length in range(5, 17):
        require(all(len(alignments(w)) == 1 for w in exact_factors(length)), "Long crop ambiguity")
    results["problem_5"] = {"asks": "Can a genuine five-tile crop have two pairings?",
                             "answer": "No", "legal_fives": sorted(legal_fives)}

    periodic_results = []
    for period, first_bad, expected_bad in [
        ("AB", 5, ["ABABA", "BABAB"]),
        ("ABBA", 8, ["AABBAABB", "BBAABBAA"]),
    ]:
        for length in range(1, first_bad + 1):
            repeated = period * (length + 2)
            factors = {repeated[i:i + length] for i in range(len(period))}
            bad = sorted(factors.difference(exact_factors(length)))
            require(bad == (expected_bad if length == first_bad else []), "Periodic witness")
        periodic_results.append({"period": period, "shortest_forbidden_length": first_bad,
                                 "shortest_witnesses": expected_bad})
    require("ABBAABBAAB" not in exact_factors(10), "Long ABBA witness unexpectedly genuine")
    require(alignments("ABBAABBAAB")[0]["parent"] == "ABABA", "Long witness parent")
    repeat = "ABBA" * 6
    for forbidden in ("AAA", "BBB", "ABABA", "BABAB"):
        require(forbidden not in repeat, "Repeated ABBA should pass the immediate bans")
    results["problem_6"] = {"asks": "Find impossible finite pieces in each periodic strip",
                             "cases": periodic_results, "fully_decodable_witness": "ABBAABBAAB"}
    results["problem_7"] = {"asks": "Could a tail of the infinite limit repeat one block?",
                             "answer": "No", "proof": "See the general period-halving proof in this file"}
    for n in range(1024):
        require(prefix(4 * n + 4)[4 * n:] in ("ABBA", "BAAB"), "Four-block identity")
        require(letter(4 * n + 1) == letter(4 * n + 2), "Equal pair in four-block")
    results["exact_factor_counts_1_through_16"] = [len(exact_factors(n)) for n in range(1, 17)]
    results["status"] = "PASS: all explicit finite examples and exact language checks"
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--source", type=Path, help="students.tex to match against reviewed diagrams")
    args = parser.parse_args()
    source = args.source
    if source is None:
        home = Path(__file__).resolve().parent
        source = next((p for p in (home / "students.tex", home / "final/src/students.tex")
                       if p.is_file()), None)
    print(json.dumps(run(source), indent=2))


if __name__ == "__main__":
    main()
