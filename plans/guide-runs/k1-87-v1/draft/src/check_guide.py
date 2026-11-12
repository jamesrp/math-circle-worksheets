#!/usr/bin/env python3
"""Independent final-PDF anchored checks for the Week 87 K-1 adult guide.

Requires Python 3 and Poppler's pdftotext/pdfinfo, no third-party Python package.
The student PDF is read, not rebuilt. The exact approved-draft hash binds the
checked diagrams/layout to the version personally inspected by this writer.
The mathematical model below does not import the student checker.
"""
from hashlib import sha256
from itertools import combinations, permutations, product
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
STUDENT_SHA = "02d7aed95f9d5fb4af5126e710494e54aee9a7f5bd217b551709920e1523ca47"


def find_student():
    # Portable package: k-1.pdf sits beside src/ (or guide-src/).
    direct = HERE.parent / "k-1.pdf"
    if direct.is_file():
        return direct
    # Writer run: discover this repository without embedding a machine path.
    for parent in HERE.parents:
        candidate = parent / "plans/k1-drafts/week-87/k-1.pdf"
        if candidate.is_file():
            return candidate
    raise FileNotFoundError("Put the final student k-1.pdf beside src/ or guide-src/.")


def text(pdf, raw=False):
    return subprocess.check_output(
        ["pdftotext", "-raw" if raw else "-layout", str(pdf), "-"], text=True
    )


def pages(pdf):
    return int(re.search(r"^Pages:\s+(\d+)", subprocess.check_output(
        ["pdfinfo", str(pdf)], text=True), re.M).group(1))


student = find_student()
assert sha256(student.read_bytes()).hexdigest() == STUDENT_SHA, "Student version changed; re-review final pages."
assert pages(student) == 6
raw = text(student, True).split("\f")[:6]
for i, nums in enumerate(((1,), (2,), (3,), (4,), (5, 6), (7, 8))):
    assert tuple(map(int, re.findall(r"Problem (\d+):", raw[i]))) == nums
assert "so that C wins" in raw[4]
assert "Make B win" in raw[4]
assert "with B 1st on just one card" in raw[5]
assert "with B never 1st" in raw[5]


def printed_cards(chunk, ranked=True):
    middle = r"1st\s+2nd\s+3rd\s+" if ranked else ""
    matches = re.findall(r"V([123])\s+" + middle + r"([A-F])\s+([A-F])\s+([A-F])", chunk)
    assert [x[0] for x in matches] == ["1", "2", "3"]
    return tuple("".join(x[1:]) for x in matches)


fixed = printed_cards(raw[0].split("Problem 1:")[1])
p3 = printed_cards(raw[2])
p4 = printed_cards(raw[3])
p5 = printed_cards(raw[4].split("Problem 6:")[0])
demo = printed_cards(raw[0].split("Problem 1:")[0], False)
assert fixed == p5 == ("ABC", "BCA", "CAB")
assert p3 == ("CBA", "BAC", "CBA")
assert p4 == ("ABC", "BAC", "CAB")
assert demo == printed_cards(raw[1].split("Run each knockout")[0], False) == ("DFE", "EFD", "FED")
starts = re.findall(r"First pair Waiting\s+([ABC]) ([ABC]) ([ABC]) A B C", raw[1])
assert starts == [("B", "C", "A"), ("C", "A", "B"), ("A", "B", "C")]


def ballot(card, a, b):
    # Scan top to bottom; the first offered letter is the ballot.
    return next(letter for letter in card if letter in (a, b))


def vote(profile, a, b):
    ballots = tuple(ballot(card, a, b) for card in profile)
    count = {letter: ballots.count(letter) for letter in (a, b)}
    assert count[a] != count[b]
    winner = max(count, key=count.get)
    return winner, count[winner], 3 - count[winner], ballots


def run(profile, waiting):
    pair = [letter for letter in profile[0] if letter != waiting]
    first = vote(profile, *pair)[0]
    return first, vote(profile, first, waiting)[0]


def finals(profile):
    return {run(profile, wait)[1] for wait in profile[0]}


def beats_both(profile, letter):
    return all(vote(profile, letter, rival)[0] == letter for rival in profile[0] if rival != letter)


assert vote(demo, "D", "E") == ("E", 2, 1, ("D", "E", "E"))
assert vote(demo, "E", "F") == ("F", 2, 1, ("F", "E", "F"))
assert finals(demo) == {"F"}
expected = [("A", ("A", "B", "A")), ("B", ("B", "B", "C")), ("C", ("A", "C", "C"))]
for pair, (winner, ballots) in zip(("AB", "BC", "CA"), expected):
    assert vote(fixed, *pair) == (winner, 2, 1, ballots)
assert [run(fixed, w) for w in "ABC"] == [("B", "A"), ("C", "B"), ("A", "C")]
for profile, winner, counts, traces in [
    (p3, "C", [("BA", 3), ("CA", 2), ("CB", 2)], [("C", "C"), ("C", "C"), ("B", "C")]),
    (p4, "A", [("AB", 2), ("AC", 2), ("BC", 2)], [("B", "A"), ("A", "A"), ("A", "A")]),
]:
    assert finals(profile) == {winner}
    for pair, count in counts:
        assert vote(profile, *pair)[:3] == (pair[0], count, 3-count)
    assert [run(profile, w) for w in "ABC"] == traces
print("Final PDF: six pages, Problems 1-8, all actual printed card profiles and agenda starts verified.")
print("Demo and Problems 1-4: every printed vote count, supporter and knockout trace PASS.")

swaps = []
all_swaps = []
for voter in range(3):
    for i, j in combinations(range(3), 2):
        changed = list(fixed[voter])
        changed[i], changed[j] = changed[j], changed[i]
        profile = list(fixed)
        profile[voter] = "".join(changed)
        all_swaps.append((voter+1, fixed[voter], profile[voter], finals(profile)))
        if finals(profile) == {"C"}:
            ca = 3 if voter == 0 and profile[voter] == "CBA" else 2
            assert vote(profile, "C", "A")[:3] == ("C", ca, 3-ca)
            assert vote(profile, "C", "B")[:3] == ("C", 2, 1)
            swaps.append((voter+1, fixed[voter], profile[voter]))
assert swaps == [(1, "ABC", "CBA"), (1, "ABC", "ACB"), (2, "BCA", "CBA")]
print("Problem 5: all nine single swaps:", all_swaps)

cards = tuple("".join(p) for p in permutations("ABC"))
profiles = tuple(product(cards, repeat=3))
good = [p for p in profiles if finals(p) == {"B"}]
good_sets = sorted({tuple(sorted(p)) for p in good})
assert len(profiles) == 216 and len(good) == 68 and len(good_sets) == 18
example = ("BAC", "BCA", "ABC")
assert example in good
assert vote(example, "B", "A")[:3] == ("B", 2, 1)
assert vote(example, "B", "C")[:3] == ("B", 3, 0)
one_first = sorted({tuple(sorted(p)) for p in good if sum(c[0] == "B" for c in p) == 1})
assert one_first == [("ABC", "BAC", "CBA"), ("ABC", "BCA", "CBA")]
assert all(vote(p, "B", rival)[:3] == ("B", 2, 1) for p in one_first for rival in "AC")
assert not any(p in good for p in profiles if all(c[0] != "B" for c in p))
assert all(p in good for p in profiles if sum(c[0] == "B" for c in p) >= 2)
for profile in profiles:
    for letter in "ABC":
        assert (finals(profile) == {letter}) == beats_both(profile, letter)
    for a, b in combinations("ABC", 2):
        assert vote(profile, a, b)[0] == vote(profile, b, a)[0]
    # Complete constructive characterization of every B-winning build.
    tops = sum(card[0] == "B" for card in profile)
    characterized = tops >= 2 or (tops == 1 and tuple(sorted(profile)) in one_first)
    assert (profile in good) == characterized
    # P8's disjoint-support claim is checked card by card.
    if tops == 0:
        ab = {i for i, c in enumerate(profile) if ballot(c, "B", "A") == "B"}
        cb = {i for i, c in enumerate(profile) if ballot(c, "B", "C") == "B"}
        assert ab.isdisjoint(cb) and len(ab) + len(cb) <= 3
print("Problem 6: 68 ordered / 18 unordered winning profiles; complete unordered catalog:", good_sets)
print("Problem 7: exact two unordered sets:", one_first)
print("Problem 8: zero solutions among all 64 ordered no-B-first profiles.")
print("All 216 profiles: no ties, iff theorem, pair-order invariance and build characterization PASS.")

guide = HERE.parent / "k1-guide.pdf"
assert guide.is_file()
assert pages(guide) == 4
guide_text = text(guide)
for number, page in [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 5), (7, 6), (8, 6)]:
    assert f"Problem {number}, page {page}" in guide_text
assert "W87-K-FAC-v1" in guide_text
tex = (HERE / "k1-guide.tex").read_text()
for answer in ["V1 ABC to ACB", "V1 ABC to CBA", "V2 BCA to CBA", "BAC, BCA, ABC",
               r"\{ABC,\ BAC,\ CBA\}", r"\{ABC,\ BCA,\ CBA\}"]:
    assert answer in tex, answer
assert "physically unrehearsed" in guide_text and "Unpiloted" in guide_text
print("Guide: four US Letter pages, all student page references and printed constructions PASS.")
print("CHECK PASSED (digital only; no physical rehearsal or classroom pilot).")
