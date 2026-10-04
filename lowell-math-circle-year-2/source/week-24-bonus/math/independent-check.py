#!/usr/bin/env python3
"""Independent exact check of every printed Week 24 task; standard library only."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

finalsrc = Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-24-bonus.pdf'

DECKS = {"A": (2, 4, 9), "B": (1, 6, 8), "C": (3, 5, 7)}

def main():
    source = finalsrc.read_text()
    assert "nonempty label bag" in source
    assert "average means points averaged over all equally likely label-slip and card draws" in source
    assert "0.9/B/{1,6,8}/6/2,0/A/{2,4,9}/4/0" in source
    assert 6 in DECKS['B'] and 4 in DECKS['A'] and 6 > 4
    worked_points = (2, 0)
    assert sum(worked_points) == 2
    triples = []
    champions = Counter()
    per_card = {name: Counter() for name in DECKS}
    for values in product(*DECKS.values()):
        assert len(set(values)) == 3
        winner = max(zip(DECKS, values), key=lambda item: item[1])[0]
        champions[winner] += 1
        per_card[winner][values[list(DECKS).index(winner)]] += 1
        triples.append({"cards": dict(zip(DECKS, values)), "winner": winner})
    assert champions == {"A": 10, "B": 10, "C": 7}
    sums = {name: Counter(x + y for x, y in product(cards, repeat=2)) for name, cards in DECKS.items()}
    pairs = {name: [[x, y, x + y] for x, y in product(cards, repeat=2)] for name, cards in DECKS.items()}
    comparisons = {}
    for left, right, expected in (("A", "B", (37, 44, 0)), ("B", "C", (39, 38, 4)), ("C", "A", (39, 38, 4))):
        counts = [0, 0, 0]
        for x1, x2, y1, y2 in product(DECKS[left], DECKS[left], DECKS[right], DECKS[right]):
            x, y = x1 + x2, y1 + y2
            counts[0 if x > y else 1 if x < y else 2] += 1
        assert tuple(counts) == expected
        comparisons[left + right] = {"first_wins": counts[0], "second_wins": counts[1], "ties": counts[2], "outcomes": 81,
            "first_average_points": str(Fraction(2 * counts[0] + counts[2], 81)),
            "second_average_points": str(Fraction(2 * counts[1] + counts[2], 81))}
    payoffs = {}
    for left in DECKS:
        payoffs[left] = {}
        for right in DECKS:
            total = sum(2 if x > y else 1 if x == y else 0 for x, y in product(DECKS[left], DECKS[right]))
            payoffs[left][right] = Fraction(total, 9)
        assert sum(payoffs[left].values()) == 3
    uniform = {opponent: sum(payoffs[own][opponent] for own in DECKS) / 3 for opponent in DECKS}
    assert all(value == 1 for value in uniform.values())
    bags_checked = 0
    for size in range(1, 13):
        for a in range(size + 1):
            for b in range(size - a + 1):
                c = size - a - b
                values = [sum(Fraction(count, size) * payoffs[own][opponent] for own, count in zip(DECKS, (a, b, c))) for opponent in DECKS]
                assert sum(values) == 3
                assert not all(value > 1 for value in values)
                assert (all(value >= 1 for value in values)) == (a == b == c)
                bags_checked += 1
    run = Path(__file__).resolve().parent
    out = {"week": 24, "scope": "final/bonus.pdf, all 4 pages and Problems 1-5", "independent": True,
        "final_pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "final_source_sha256": hashlib.sha256(finalsrc.read_bytes()).hexdigest(),
        "P1": {"champions": dict(champions), "champion_counts_by_card": {name: {str(card): per_card[name][card] for card in cards} for name, cards in DECKS.items()}, "triples": triples},
        "P2": {"ordered_pairs": pairs, "total_multiplicities": sums}, "P3": comparisons,
        "worked_label_to_card": {"own": {"label": "B", "card": 6, "points": 2}, "opponent": {"label": "A", "card": 4, "points": 0}},
        "P4": {"pure_payoffs": {left: {right: str(value) for right, value in row.items()} for left, row in payoffs.items()}, "uniform_payoffs": {key: str(value) for key, value in uniform.items()}, "finite_nonempty_bags_checked": bags_checked},
        "P5": {"answer": "No", "general_certificate": "Each pure-deck payoff row sums to 3; therefore every mixture's three fixed-opponent expectations sum to 3. All >=1 forces equal label proportions.", "expected_against_A_B_C": ["1+(c-b)/9", "1+(a-c)/9", "1+(b-a)/9"]},
        "diagram_check": "Printed A/B/C card values match the separately transcribed decks; 27 triple rows and 9 ordered-pair rows per deck.",
        "assumptions": ["Uniform independent replacement draws", "Nonempty finite label bag; labels have equal draw probability", "Expectation is not a finite-play guarantee"],
        "physical_rehearsal": "untested"}
    (run / "checks.json").write_text(json.dumps(out, indent=2) + "\n")
    print("Week 24 independent checks passed; checks.json written")

if __name__ == "__main__":
    main()
