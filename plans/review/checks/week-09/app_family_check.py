"""Independent check of the shipped Mirror Couriers instances (app dist/puzzles.json).

Simulates the reflected ray with exact fractions, wall event by wall event
(no lcm formula), and recomputes every accepted setting for the design modes.
Also checks the K-1 guide's walking rule against the true reflection on the
3 by 5 floor grid. Usage: python3 -I app_family_check.py <path to puzzles.json>
"""
import json, sys
from fractions import Fraction as F

def simulate(w, h, rise, run, limit=10000):
    # position and velocity; velocity (run, rise) scaled
    x, y = F(0), F(0)
    vx, vy = F(run), F(rise)
    bounces = 0
    for _ in range(limit):
        tx = ((w - x) / vx) if vx > 0 else (x / -vx)
        ty = ((h - y) / vy) if vy > 0 else (y / -vy)
        t = min(tx, ty)
        x, y = x + vx * t, y + vy * t
        hitx, hity = tx == t, ty == t
        if hitx and hity:
            corner = ('top' if y == h else 'bottom') + '-' + ('right' if x == w else 'left')
            return corner, bounces
        bounces += 1
        if hitx: vx = -vx
        else: vy = -vy
    raise RuntimeError('no corner')

d = json.load(open(sys.argv[1]))
ok = bad = 0
for p in d['puzzles']:
    if p.get('mechanic') != 'billiard':
        continue
    q, sol = p['parameters'], p['solution']
    if q['mode'] == 'predict':
        c, b = simulate(q['width'], q['height'], q['rise'], q['run'])
        good = (c, b) == (sol['corner'], sol['bounces'])
        print(p['id'], 'predict', q['width'], 'x', q['height'], f"slope {q['rise']}/{q['run']}", '->', c, b, 'OK' if good else 'MISMATCH')
    elif q['mode'] == 'choose_width':
        valid = [w for w in range(q['width_min'], q['width_max'] + 1)
                 if simulate(w, q['height'], q['rise'], q['run']) == (q['target_corner'], q['target_bounces'])]
        good = valid == sol['all_valid_widths']
        print(p['id'], 'choose_width h=%d' % q['height'], q['target_corner'], q['target_bounces'], 'valid widths', valid, 'OK' if good else 'MISMATCH', '(of %d options)' % (q['width_max'] - q['width_min'] + 1))
    else:
        rng = range(q['component_min'], q['component_max'] + 1)
        valid = [[r, u] for r in rng for u in rng
                 if simulate(q['width'], q['height'], r, u) == (q['target_corner'], q['target_bounces'])]
        good = sorted(valid) == sorted(sol['all_valid_directions'])
        print(p['id'], 'choose_direction %dx%d' % (q['width'], q['height']), q['target_corner'], q['target_bounces'], 'valid', valid, 'OK' if good else 'MISMATCH', '(of %d options)' % (len(rng) ** 2))
    ok += good; bad += not good
print('instances OK:', ok, 'mismatches:', bad)

# Does any shipped instance ask for an impossible target, a 'never home' claim,
# or a 'find every one' list? (Read off the modes and targets above.)
print('modes:', sorted({p['parameters']['mode'] for p in d['puzzles'] if p.get('mechanic') == 'billiard'}))

# K-1 guide walking rule vs true reflection on the 3 by 5 floor grid.
def walk(w, h, start_right=False, rule=False):
    x, y = (w, 0) if start_right else (0, 0)
    dx, dy = (-1 if start_right else 1), 1
    log = []
    for _ in range(100):
        nx, ny = x + dx, y + dy
        x, y = nx, ny
        if x in (0, w) and y in (0, h):
            log.append(('stop', (x, y)))
            return log
        side, end = x in (0, w), y in (0, h)
        if side or end:
            going = 'up' if dy > 0 else 'down'
            true_d = (-dx if side else dx, -dy if end else dy)
            if side:
                guide_d = (-dx, 1)          # "keep going up the grid but slant the other way"
            else:
                guide_d = (dx, -1)          # far end: "keep slanting the same way but come back down"
            wall = 'side' if side else ('far end' if y == h else 'near end')
            log.append((wall, (x, y), going, 'guide agrees' if guide_d == true_d else 'GUIDE WRONG' if wall != 'near end' else 'guide silent'))
            dx, dy = true_d
    return log
for s in (False, True):
    print('floor walk from', 'right' if s else 'left', 'dot:')
    for e in walk(3, 5, s):
        print('   ', e)
