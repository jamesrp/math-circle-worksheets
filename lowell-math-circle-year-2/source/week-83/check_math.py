#!/usr/bin/env python3
"""Independent finite game-tree and birthday check for the Week 83 draft.

Python standard library only. Does not import the writer's check code, use
floating point arithmetic, or assume additivity when computing board values.
Stalks are read from the ground upwards. A cut at index i leaves stalk[:i].
Run from any directory; the reviewed draft is read next to this script.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import os
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
SOURCE = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE / "student/students.tex"


def position(stalks):
    return tuple(sorted(s for s in stalks if s))


def moves(board, color):
    """Yield every legal cut, preserving an opening's location for witnesses."""
    for stalk_index, stalk in enumerate(board):
        for edge_index, edge in enumerate(stalk):
            if edge == color:
                result = position(board[:stalk_index] + (stalk[:edge_index],)
                                  + board[stalk_index + 1:])
                yield (stalk_index, edge_index), result


@lru_cache(None)
def blue_wins(board, turn):
    next_boards = [next_board for _, next_board in moves(board, turn)]
    if turn == "B":
        return any(blue_wins(next_board, "R") for next_board in next_boards)
    # Red has no move -> Red loses; otherwise Red chooses a reply unfavorable
    # to Blue if such a reply exists. Empty all() is deliberately True.
    return all(blue_wins(next_board, "B") for next_board in next_boards)


def winner_class(board):
    a, b = blue_wins(board, "B"), blue_wins(board, "R")
    return {(True, True): "Blue", (False, False): "Red",
            (False, True): "second player", (True, False): "first player"}[(a, b)]


def birthday_catalog(days):
    """Construct births by adjoining each finite old gap's midpoint and ends.

    This enumerates dyadics of these finite birthdays; it is used to compute
    simplest cuts, not imposed on the children's arbitrary bound tasks.
    """
    birth = {Fraction(0): 0}
    for day in range(1, days + 1):
        old = sorted(birth)
        new = {old[0] - 1, old[-1] + 1}
        new.update((a + b) / 2 for a, b in zip(old, old[1:]))
        assert not (new & birth.keys())
        birth.update({q: day for q in new})
    return birth


CATALOG = birthday_catalog(9)


def simplest(left, right, catalog=CATALOG):
    allowed = [q for q in catalog
               if (left is None or left < q) and (right is None or q < right)]
    if not allowed:
        return None
    first_day = min(catalog[q] for q in allowed)
    earliest = [q for q in allowed if catalog[q] == first_day]
    assert len(earliest) == 1, (left, right, earliest)
    return earliest[0]


@lru_cache(None)
def game_value(board):
    left = [game_value(after) for _, after in moves(board, "B")]
    right = [game_value(after) for _, after in moves(board, "R")]
    lo, hi = max(left, default=None), min(right, default=None)
    assert lo is None or hi is None or lo < hi, (board, lo, hi)
    value = simplest(lo, hi)
    assert value is not None
    return value


def parse_stalks(text):
    return [colors.replace(",", "") for colors in re.findall(
        r"\\stalk\{[^}]+\}\{[^}]+\}\{([BR,]+)\}", text)]


def rendered_board_declarations(source):
    pages = source.split(r"\begin{document}", 1)[1].split(r"\newpage")
    assert len(pages) == 7
    # Partition by printed panel/board labels. The source coordinates and
    # diagrams were also checked visually on independently rendered pages.
    p1 = parse_stalks(pages[0].split(r"\textat{98}", 1)[1])
    p2 = parse_stalks(pages[1])
    p3 = parse_stalks(pages[2])
    assert p1 == ["B", "R", "B", "R", "BB", "R"]
    assert p2 == ["BR", "R", "BR", "BR", "R", "BR", "BR", "BR", "R"]
    assert p3 == ["BRR", "RB", "BRR", "BRR", "RB", "BRR", "BRR", "BRR", "RB"]
    return {
        "1A": p1[0:1], "1B": p1[1:2], "1C": p1[2:4], "1D": p1[4:6],
        "2A": p2[0:2], "2B": p2[2:5], "2C": p2[5:9],
        "3A": p3[0:2], "3B": p3[2:5], "3C": p3[5:9],
    }, pages


def selected_path(stalks, first_turn, cuts):
    """Check one tangible response path; index pairs refer to sorted stalks."""
    board = position(stalks)
    turn = first_turn
    result = []
    for desired_before, desired_after in cuts:
        assert board == position(desired_before), (board, desired_before)
        desired = position(desired_after)
        legal = [(cut, after) for cut, after in moves(board, turn) if after == desired]
        assert legal, (board, turn, desired)
        result.append({"turn": turn, "before": list(board), "after": list(desired),
                       "legal_cut": legal[0][0]})
        board, turn = desired, "R" if turn == "B" else "B"
    assert not list(moves(board, turn)), (board, turn)
    return result


def main():
    source = SOURCE.read_text()
    declared, pages = rendered_board_declarations(source)
    expected = {
        "1A": ("Blue", Fraction(1)), "1B": ("Red", Fraction(-1)),
        "1C": ("second player", Fraction(0)), "1D": ("Blue", Fraction(1)),
        "2A": ("Red", Fraction(-1, 2)), "2B": ("second player", Fraction(0)),
        "2C": ("Blue", Fraction(1, 2)), "3A": ("Red", Fraction(-1, 4)),
        "3B": ("second player", Fraction(0)), "3C": ("Blue", Fraction(1, 4)),
    }
    results = {}
    for label, stalks in declared.items():
        board = position(stalks)
        actual = winner_class(board), game_value(board)
        assert actual == expected[label], (label, board, actual, expected[label])
        results[label] = {"stalks": stalks, "value": str(actual[1]), "winner": actual[0],
                          "Blue_starts_Blue_wins": blue_wins(board, "B"),
                          "Red_starts_Blue_wins": blue_wins(board, "R"),
                          "legal_openings": {color: [
                              {"cut": cut, "after": list(after),
                               "Blue_wins_after": blue_wins(after, "R" if color == "B" else "B")}
                              for cut, after in moves(board, color)] for color in "BR"}}

    # The unfamiliar worked cut BRB --Red cuts middle--> B, before Problem 1.
    assert any(after == ("B",) for _, after in moves(("BRB",), "R"))
    assert "#2+22*(\\i-1)" in source and "#2+22*\\i" in source

    # Satisfiable invention task with at least one two-segment stalk per board.
    inventions = [("BR", "RB"), ("BB", "RR")]
    for stalks in inventions:
        board = position(stalks)
        assert max(map(len, board)) >= 2 and winner_class(board) == "second player"
        assert game_value(board) == 0

    # Read the printed cut declarations directly instead of trusting a list of
    # alleged answers from the author. The order is left-bound, right-bound.
    cut_declarations = re.findall(r"\\cutmat\{0\}\{[^}]+\}\{([^}]+)\}\{([^}]+)\}", pages[4])
    assert cut_declarations == [("0", "3"), ("-1", "1"), ("0", "1"), (r"\frac12", "1")]
    cut_bounds = [(Fraction(0), Fraction(3)), (Fraction(-1), Fraction(1)),
                  (Fraction(0), Fraction(1)), (Fraction(1, 2), Fraction(1))]
    chosen = [simplest(lo, hi) for lo, hi in cut_bounds]
    assert chosen == [Fraction(1), Fraction(0), Fraction(1, 2), Fraction(3, 4)]
    assert simplest(Fraction(-2), Fraction(2)) == 0  # non-task worked visual

    # Verify the complete supplied day-0--3 card catalog, including first births.
    supplied = {Fraction(0): 0, Fraction(-1): 1, Fraction(1): 1,
                Fraction(-2): 2, Fraction(-1, 2): 2, Fraction(1, 2): 2, Fraction(2): 2,
                Fraction(-3): 3, Fraction(-3, 2): 3, Fraction(-3, 4): 3,
                Fraction(-1, 4): 3, Fraction(1, 4): 3, Fraction(3, 4): 3,
                Fraction(3, 2): 3, Fraction(3): 3}
    assert supplied == birthday_catalog(3)
    enum_match = re.search(r"\\foreach \\num/\\day/\\col/\\row in \{(.*?)\}\{", pages[5], re.S)
    assert enum_match
    raw_cards = enum_match.group(1).split(",")
    printed_cards = {}
    for raw in raw_cards:
        value_text, day, col, row = raw.split("/")
        if r"\frac" in value_text:
            sign = -1 if value_text.startswith("-") else 1
            a, b = value_text.replace("-", "").replace(r"\frac", "")
            value = sign * Fraction(int(a), int(b))
        else:
            value = Fraction(int(value_text))
        assert value not in printed_cards
        printed_cards[value] = int(day)
    assert printed_cards == supplied

    # Enumerate all distinct ordered lower/upper pairs of supplied cards.
    # There are 105 pairs; adjacent day-3 catalog gaps have no supplied answer.
    fits, absent, newer = [], [], []
    for lo, hi in combinations(sorted(supplied), 2):
        q = simplest(lo, hi, supplied)
        row = {"lower": str(lo), "upper": str(hi), "chosen": None if q is None else str(q)}
        if q is None:
            absent.append(row)
        else:
            fits.append(row)
            if supplied[q] > max(supplied[lo], supplied[hi]):
                newer.append(row)
    assert len(fits) == 91 and len(absent) == 14 and newer
    # Problem 6 concrete witnesses: two distinct pairs both choose old zero;
    # (0,1) chooses 1/2, newer than both bounds.
    assert simplest(Fraction(-1), Fraction(1), supplied) == 0
    assert simplest(Fraction(-2), Fraction(2), supplied) == 0
    assert simplest(Fraction(0), Fraction(1), supplied) == Fraction(1, 2)
    assert supplied[Fraction(1, 2)] > max(supplied[0], supplied[1])

    # Cover every type of first cut in BR+BR+R, with concrete winning replies.
    paths = {
        "Blue_cuts_BR_base": selected_path(("BR", "BR", "R"), "B", [
            (("BR", "BR", "R"), ("BR", "R")),
            (("BR", "R"), ("B", "R")),
            (("B", "R"), ("R",)), (("R",), ())]),
        "Red_cuts_lone_R": selected_path(("BR", "BR", "R"), "R", [
            (("BR", "BR", "R"), ("BR", "BR")),
            (("BR", "BR"), ("BR",)), (("BR",), ("B",)), (("B",), ())]),
        "Red_cuts_stalk_top": selected_path(("BR", "BR", "R"), "R", [
            (("BR", "BR", "R"), ("B", "BR", "R")),
            (("B", "BR", "R"), ("B", "R")),
            (("B", "R"), ("B",)), (("B",), ())]),
    }
    # Both Blue openings are equivalent base cuts. Red's openings consist of
    # two top cuts and the separate red cut. Therefore these cases are complete.
    initial = position(("BR", "BR", "R"))
    assert len(list(moves(initial, "B"))) == 2
    assert len(list(moves(initial, "R"))) == 3
    assert {after for _, after in moves(initial, "B")} == {position(("BR", "R"))}
    assert {after for _, after in moves(initial, "R")} == {
        position(("BR", "BR")), position(("B", "BR", "R"))}

    # A green edge, if mentioned only as adult encore, is first-player win,
    # since either player can take its sole move. This is distinct from zero.
    # All-context equality is a known theorem, not inferred by this finite code.
    report = {"source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              "diagram_page_count": 7, "segment_height_mm": 22,
              "printed_boards": results,
              "problem_4_balance_witnesses": [list(x) for x in inventions],
              "problem_5_answers": [str(x) for x in chosen],
              "catalog": {str(q): day for q, day in sorted(supplied.items())},
              "problem_6": {"pairs_with_answer": len(fits), "no_catalog_answer": len(absent),
                             "newer_than_both_count": len(newer),
                             "newer_witnesses": newer},
              "complete_balance_reply_paths": paths,
              "game_tree_states_checked": blue_wins.cache_info().currsize,
              "numeric_cut_states_checked": game_value.cache_info().currsize,
              "limits": ["No physical fit or classroom rehearsal",
                         "Finite game-tree tests do not prove all-context equality",
                         "No transfinite arithmetic computation or Lean certification"]}
    Path(os.environ.get("INFINITY_CHECK_OUT", "math-check-results.json")).write_text(json.dumps(report, indent=2) + "\n")
    print("PASS: 10 printed boards, both starters, all legal game-tree replies")
    print("PASS: exact values, worked cut, 2 invention boards, 4 printed cuts")
    print("PASS: all 15 birthday cards, 105 bound pairs, complete 2BR+R response cases")
    print("Independent game and birthday checks passed.")


if __name__ == "__main__":
    main()
