"""Independent check of the app's Mirror Couriers instances (dist/puzzles.json).

Simulates the reflected ray with exact fractions, wall by wall (no lcm
formula), and checks every instance's stated corner, bounce count, and the
complete list of valid settings for the design modes. Also lists which
targets in the worksheet's inverse problems are impossible.

Usage: python3 -I app_check.py /path/to/small-math-adventure/dist/puzzles.json
"""
import json
import sys
from fractions import Fraction as F


def simulate(w, h, rise, run):
    """Ball from (0,0) with velocity (run, rise) in [0,w]x[0,h]. Returns (corner, bounces)."""
    x, y = F(0), F(0)
    vx, vy = F(run), F(rise)
    bounces = 0
    for _ in range(100000):
        tx = (F(w) - x) / vx if vx > 0 else (x / -vx)
        ty = (F(h) - y) / vy if vy > 0 else (y / -vy)
        t = min(tx, ty)
        x, y = x + vx * t, y + vy * t
        hitx, hity = tx == t, ty == t
        if hitx and hity:
            corner = ('top' if y == h else 'bottom') + '-' + ('right' if x == w else 'left')
            return corner, bounces
        bounces += 1
        if hitx:
            vx = -vx
        else:
            vy = -vy
    raise RuntimeError('no corner')


def main(path):
    data = json.load(open(path))
    ps = [p for p in data['puzzles'] if p.get('mechanic') == 'billiard']
    bad = 0
    for p in ps:
        q, s = p['parameters'], p['solution']
        mode = q['mode']
        if mode == 'predict':
            got = simulate(q['width'], q['height'], q['rise'], q['run'])
            ok = got == (s['corner'], s['bounces'])
            print(p['id'], mode, (q['width'], q['height'], q['rise'], q['run']), got, 'OK' if ok else 'MISMATCH')
        elif mode == 'choose_width':
            valid = [w for w in range(q['width_min'], q['width_max'] + 1)
                     if simulate(w, q['height'], q['rise'], q['run']) == (q['target_corner'], q['target_bounces'])]
            ok = valid == s['all_valid_widths']
            print(p['id'], mode, 'height', q['height'], 'target', q['target_corner'], q['target_bounces'], 'valid widths', valid, 'OK' if ok else 'MISMATCH')
        else:
            valid = [[r, u] for r in range(q['component_min'], q['component_max'] + 1)
                     for u in range(q['component_min'], q['component_max'] + 1)
                     if simulate(q['width'], q['height'], r, u) == (q['target_corner'], q['target_bounces'])]
            ok = sorted(valid) == sorted(s['all_valid_directions'])
            print(p['id'], mode, (q['width'], q['height']), 'target', q['target_corner'], q['target_bounces'], 'valid [rise,run]', valid, 'OK' if ok else 'MISMATCH')
        bad += not ok
    modes = {}
    for p in ps:
        modes.setdefault(p['parameters']['mode'], []).append(p['id'])
    print('modes:', modes)
    print('instances:', len(ps), 'mismatches:', bad)
    # Does any instance pose an impossible target (a "can't" puzzle)?
    impossible = [p['id'] for p in ps if p['parameters']['mode'] != 'predict' and not (
        p['solution'].get('all_valid_widths') or p['solution'].get('all_valid_directions'))]
    print('instances with no valid setting (a can\'t answer):', impossible or 'none')
    # Worksheet inverse targets at 45 degrees, tables up to 14 by 14.
    for corner, n in [('top-right', 3), ('bottom-right', 10), ('top-right', 4), ('top-left', 13), ('bottom-right', 1)]:
        tables = [(w, h) for w in range(1, 15) for h in range(1, 15) if simulate(w, h, 1, 1) == (corner, n)]
        print('45-degree tables up to 14x14 with', corner, n, ':', tables if tables else 'none')
    home = [(w, h) for w in range(1, 41) for h in range(1, 41) if simulate(w, h, 1, 1)[0] == 'bottom-left']
    print('45-degree tables up to 40x40 returning to the start:', home or 'none')


if __name__ == '__main__':
    main(sys.argv[1])
