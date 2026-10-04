"""Independent exact finite-policy audit; run from any working directory."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

values = (0, 4, 6)
v = {1: Fraction(sum(values), len(values))}
for m in (2, 3):
    v[m] = sum(max(Fraction(x), v[m - 1]) for x in values) / len(values)

def score(word, policy):
    for j, x in enumerate(word):
        if j == len(word) - 1 or policy(word[:j + 1]):
            return x
    raise AssertionError('final choice is mandatory')

audits = {}
for horizon in (2, 3):
    histories = [h for j in range(1, horizon) for h in product(values, repeat=j)]
    words = list(product(values, repeat=horizon))
    best = Fraction(-1)
    best_count = 0
    for bits in product((False, True), repeat=len(histories)):
        policy = dict(zip(histories, bits))
        mean = Fraction(sum(score(w, lambda h: policy[h]) for w in words), len(words))
        if mean > best:
            best, best_count = mean, 1
        elif mean == best:
            best_count += 1
    assert best == v[horizon]
    optimal = lambda h: h[-1] >= v[horizon - len(h)]
    scores = [score(w, optimal) for w in words]
    audits[str(horizon)] = {
        'full_words': len(words), 'deterministic_history_policies': 2 ** len(histories),
        'best_mean': str(best), 'best_policy_count_including_unreachable_choices': best_count,
        'optimal_score_counts': {str(x): scores.count(x) for x in values},
        'optimal_score_total': sum(scores),
    }
words3 = list(product(values, repeat=3))
myopic = Fraction(sum(score(w, lambda h: h[-1] >= v[1]) for w in words3), len(words3))
recall = Fraction(sum(max(w) for w in words3), len(words3))
assert myopic == Fraction(130, 27)
assert recall == Fraction(142, 27)
result = {'model': 'iid replacement tickets 0,4,6; no recall; mandatory final choice',
          'values_before_draw': {str(m): str(x) for m, x in v.items()},
          'policy_audits': audits, 'myopic_three_draw_mean': str(myopic),
          'recall_three_draw_mean_different_model': str(recall),
          'verified': True, 'physical_pretest': 'unperformed', 'pilot': 'unperformed'}
Path(__file__).with_name('math-checks.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
