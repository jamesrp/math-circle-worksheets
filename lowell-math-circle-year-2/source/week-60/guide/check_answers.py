#!/usr/bin/env python3
"""Independent Week 60 adult-guide audit; standard-library mathematics.

Optional --students audits the actual supplied student PDF's full-word cards.
No student-builder/reviewer code or results are imported.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def words(bag, n):
    return list(product(bag, repeat=n))


def evaluate(word, decision):
    for i, x in enumerate(word):
        prefix = word[:i + 1]
        if i == len(word) - 1 or decision(prefix):
            return x
    raise AssertionError('mandatory final offer was not scored')


def full_history_audit(bag, n):
    """Every binary action at every possible nonfinal observed prefix."""
    nodes = [p for k in range(1, n) for p in product(bag, repeat=k)]
    lookup = {p: i for i, p in enumerate(nodes)}
    cases = words(bag, n)
    best, masks = None, []
    for mask in range(1 << len(nodes)):
        total = sum(evaluate(w, lambda p: bool(mask & (1 << lookup[p])))
                    for w in cases)
        if best is None or total > best:
            best, masks = total, [mask]
        elif total == best:
            masks.append(mask)
    return {'total': best, 'mean': str(F(best, len(cases))),
            'policies_checked': 1 << len(nodes), 'optimal_masks': masks}


def values(bag, horizon):
    out = [None, F(sum(bag), len(bag))]
    for n in range(2, horizon + 1):
        out.append(sum(max(F(x), out[-1]) for x in bag) / len(bag))
    return out


def threshold_scores(bag, n):
    val = values(bag, n)
    return [evaluate(w, lambda p: p[-1] >= val[n - len(p)])
            for w in words(bag, n)]


def actual_cards(pdf):
    import pymupdf
    doc = pymupdf.open(pdf)
    assert len(doc) == 7
    result = {}
    for index, length, expected in [(1, 2, words((0, 4, 6), 2)),
                                    (2, 3, words((0, 4, 6), 3)),
                                    (5, 2, words((0, 3, 6), 2) + words((0, 5, 6), 2))]:
        lines = [s.strip() for s in doc[index].get_text().splitlines()]
        cards = []
        for i, s in enumerate(lines):
            if s == 'score':
                prev = lines[i - length:i]
                assert all(x.isdigit() for x in prev), (index, prev)
                cards.append(tuple(map(int, prev)))
        assert cards == expected, (index + 1, cards, expected)
        result[str(index + 1)] = [list(c) for c in cards]
    # Independently check the printed position convention and circular counter count.
    text = doc[3].get_text()
    assert '2 offers left, including this one' in text
    assert '3 offers left, including this one' in text
    circles = [d['rect'] for d in doc[3].get_drawings()
               if abs(d['rect'].width - 17.28) < 0.1
               and abs(d['rect'].height - 17.28) < 0.1]
    assert len(circles) == 5
    rules = doc[0].get_text()
    assert rules.index('With one counter left') < rules.index('after deciding on each offer')
    result['position_counter_count'] = 5
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--students', type=Path)
    ap.add_argument('--out', type=Path)
    args = ap.parse_args()
    evidence = {}
    original = (0, 4, 6)
    # Independently recompute the operational counts printed in the guide.
    table_cards = 3**2 + 3**3 + 3**2 + 3**2
    assert table_cards == 54 and 2 * table_cards == 108
    assert 7 + 1 == 8 and 3 * (3 + 1) == 12
    assert 2 * 3 == 6 and 2 * (4 + 1) == 10
    k1_spare_kits = 4 + 1
    assert [k1_spare_kits * n for n in (6, 12, 3, 2, 2)] == [30, 60, 15, 10, 10]
    evidence['preparation_counts'] = {'older_kits': 3, 'bags': 3, 'original_tickets': 9,
                                     'counters': 12, 'new_bag_tickets': 18,
                                     'cards_per_table': table_cards, 'cut_cards': 108,
                                     'uncut_spare_cards': 54, 'older_paper_sheets': 32,
                                     'cardstock_sheets': 9, 'prior_K1_sheets': 10,
                                     'prior_K1_blocks_with_spare_kit': [30, 60, 15, 10, 10]}
    # Both practice conversions, including input, intermediate, output.
    assert evaluate((2, 1), lambda p: False) == 1
    assert evaluate((3, 1), lambda p: p[-1] in (3, 5)) == 3
    assert F(1 + 3 + 5, 3) == 3
    evidence['practice'] = {'2_then_1_forced_score': 1, '3_then_unseen_1_score': 3,
                            'non_target_mean_1_3_5': 3}

    # P1/P2: same fixed rules in both matches; fully recoverable unseen tails.
    # The constant-word construction in fact works for every legal history policy.
    samples = []
    for two_x, three_x in [(6, 0), (0, 6)]:
        two, three = [(two_x,) * 2] * 6, [(three_x,) * 3] * 6
        for n, batch in [(2, two), (3, three)]:
            nodes = [p for k in range(1, n) for p in product(original, repeat=k)]
            lookup = {p: i for i, p in enumerate(nodes)}
            for mask in range(1 << len(nodes)):
                got = sum(evaluate(w, lambda p: bool(mask & (1 << lookup[p]))) for w in batch)
                assert got == 6 * batch[0][0]
        samples.append({'two_offer_words': two, 'three_offer_words': three,
                        'two_total': 6 * two_x, 'three_total': 6 * three_x,
                        'full_sample_probability': str(F(1, 3**30))})
    evidence['opposite_six_round_matches'] = samples

    for bag, two_total in [(original, 40), ((0, 3, 6), 36), ((0, 5, 6), 44)]:
        key = ','.join(map(str, bag))
        v = values(bag, 4)
        audit = {str(n): full_history_audit(bag, n) for n in (2, 3)}
        assert audit['2']['total'] == two_total
        assert all(F(audit[str(n)]['mean']) == v[n] for n in (2, 3))
        choices = []
        for take in product((False, True), repeat=3):
            scores = [evaluate(w, lambda p: take[bag.index(p[-1])]) for w in words(bag, 2)]
            choices.append({'choices': ''.join('T' if b else 'P' for b in take),
                            'scores': scores, 'total': sum(scores)})
        evidence[key] = {'values': [str(x) for x in v[1:]],
                         'history_audit': audit, 'two_offer_rules': choices}

    assert evidence['0,4,6']['values'][:3] == ['10/3', '40/9', '134/27']
    assert evidence['0,5,6']['values'] == ['11/3', '44/9', '143/27', '448/81']
    assert [r['choices'] for r in evidence['0,3,6']['two_offer_rules'] if r['total'] == 36] == ['PPT', 'PTT']

    plan_a = lambda p: p[-1] in (4, 6)
    plan_b = lambda p: p[-1] == 6 if len(p) == 1 else p[-1] in (4, 6)
    cards = words(original, 3)
    a = [evaluate(w, plan_a) for w in cards]
    b = [evaluate(w, plan_b) for w in cards]
    assert (sum(a), sum(b)) == (130, 134)
    assert Counter(a) == {0: 1, 4: 13, 6: 13}
    assert Counter(b) == {0: 2, 4: 8, 6: 17}
    evidence['P4_every_card'] = [{'word': w, 'A': x, 'B': y} for w, x, y in zip(cards, a, b)]
    evidence['P4_totals'] = [sum(a), sum(b)]
    evidence['P5'] = {'two_take': '4', 'two_pass': '10/3',
                       'three_take': '4', 'three_pass': '40/9'}
    assert F(10, 3) < 4 < F(40, 9)
    assert Counter(threshold_scores(original, 2)) == {0: 1, 4: 4, 6: 4}

    # P8: exhaustive only within current-score/turn policies at horizon 4.
    bag = (0, 5, 6)
    n = 4
    keys = [(i, x) for i in range(1, n) for x in bag]
    lookup = {k: j for j, k in enumerate(keys)}
    best = max(sum(evaluate(w, lambda p: bool(mask & (1 << lookup[len(p), p[-1]])))
                   for w in words(bag, n)) for mask in range(1 << len(keys)))
    assert best == 448
    three_scores, four_scores = threshold_scores(bag, 3), threshold_scores(bag, 4)
    assert Counter(three_scores) == {0: 1, 5: 13, 6: 13}
    assert Counter(four_scores) == {0: 2, 5: 26, 6: 53}
    assert F(44, 9) < 5 < F(143, 27)
    evidence['P8'] = {'three_counts': dict(Counter(three_scores)),
                       'four_counts': dict(Counter(four_scores)),
                       'four_total': best, 'current_turn_policies_checked': 512,
                       'not_a_full_history_policy_enumeration': True}

    # P9 finite examples include negatives and duplicate score tickets.
    checked = 0
    for bag in product(range(-2, 3), repeat=3):
        v = values(bag, 6)
        for k in range(1, 6):
            assert v[k + 1] >= v[k]
            assert (v[k + 1] == v[k]) == (min(bag) == max(bag))
        checked += 1
    evidence['P9_bags_checked'] = checked
    evidence['P9_general_proof'] = 'Guide induction and all-minimum-word bound; finite checks support it.'
    if args.students:
        evidence['actual_student_pdf'] = actual_cards(args.students)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(evidence, indent=2) + '\n')
    print('PASS: all guide task answers, examples, full cards and scoped policy audits')


if __name__ == '__main__':
    main()
