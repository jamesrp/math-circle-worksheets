#!/usr/bin/env python3
"""Cross-check week-28-materials.pdf against the student pages and this review's oracle.

Reads the kit's printed disks (pages 2-9), recovers their ray angles from the
drawn lines, and checks (1) each disk has the sectors of the student disk it
stands for, in the same clockwise order (pdf_geometry.json, read from the
student PDFs); (2) foldcheck.py, written independently of the kit, finds the
same foldable mountain-valley words the guide states: 8 for the right-angle
disk, none for B, six for C, four for D (VVVM fails); (3) each add-a-ray start
has exactly one whole-degree position for a fourth ray that folds flat, at
360 minus its first angle; (4) the K-1 Problem 6 route words, which the kit's
route cards copy, are exactly the eight foldable words of the right-angle disk
(the package's check_materials.py checks the printed cards themselves).
"""
from fractions import Fraction
from pathlib import Path
import json
import math
import sys

import pymupdf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import foldcheck  # noqa: E402

ROOT = HERE.parents[3]
KIT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'lowell-math-circle-year-2/week-28/week-28-materials.pdf'
GEOM = json.loads((HERE / 'pdf_geometry.json').read_text())
MM = 72 / 25.4
fails = 0


def ok(cond, what):
    global fails
    print(('PASS ' if cond else 'FAIL ') + what)
    fails += not cond


def kit_rays(page):
    disk = [d['rect'] for d in page.get_drawings()
            if d['items'] and d['items'][0][0] == 'c' and abs(d['rect'].width / MM - 180) < .5]
    centres = {(round((r.x0 + r.x1) / 2, 1), round((r.y0 + r.y1) / 2, 1)) for r in disk}
    assert len(centres) == 1, centres            # one disk per page (outline and tint share it)
    cx, cy = centres.pop()
    rays = set()
    for d in page.get_drawings():
        for it in d['items']:
            if it[0] != 'l':
                continue
            for p, q in ((it[1], it[2]), (it[2], it[1])):
                if math.hypot(p.x - cx, p.y - cy) < .5 and math.hypot(q.x - cx, q.y - cy) / MM > 80:
                    rays.add(round(math.degrees(math.atan2(q.x - cx, cy - q.y))) % 360)
    return sorted(rays)


def sectors(rays):
    return [(rays[(i + 1) % len(rays)] - rays[i]) % 360 for i in range(len(rays))]


def student(band, page, name):
    for p in GEOM[band]:
        if p['page'] == page:
            for disc in p['discs']:
                if disc['name'] == name:
                    return [round(x) for x in disc['sectors']]
    raise KeyError((band, page, name))


def same_cycle(a, b):
    return len(a) == len(b) and any(a[k:] + a[:k] == b for k in range(len(a)))


doc = pymupdf.open(KIT)
four = {2: 'A', 3: 'B', 4: 'C', 5: 'D'}
want_words = {
    'A': {'MMMV', 'MMVM', 'MVMM', 'VMMM', 'MVVV', 'VMVV', 'VVMV', 'VVVM'},
    'B': set(),
    'C': {'MMMV', 'MVMM', 'MVVV', 'VMMM', 'VMVV', 'VVVM'},
    'D': {'MVMM', 'MVVV', 'VMMM', 'VMVV'},
}
for pg, name in four.items():
    rays = kit_rays(doc[pg - 1])
    sec = sectors(rays)
    for band, page in (('grades-2-3', 2), ('grades-2-3', 3), ('grades-4-5', 1)):
        ok(same_cycle(sec, student(band, page, name)),
           f'kit p{pg} disk {name} sectors {sec} = {band} p{page} disk {name}')
    words = foldcheck.valid_words([Fraction(s) for s in sec])
    crimp = foldcheck.crimp_words([Fraction(s) for s in sec])
    ok(set(words) == set(crimp) == want_words[name],
       f'kit p{pg} disk {name}: oracle finds {len(set(words))} foldable words, crimp agrees, as the guide states')
ok(student('k-1', 1, None) == [90, 90, 90, 90], 'K-1 disks are right-angle disks, like kit p2')

starts = {6: 'A', 7: 'B', 8: 'C', 9: 'D'}
for pg, name in starts.items():
    rays = kit_rays(doc[pg - 1])
    ok(same_cycle(sectors(rays), student('grades-2-3', 4, name)),
       f'kit p{pg} start {name} {rays} = grades 2-3 P4 start {name}')
    good = []
    for x in range(360):
        if x in rays:
            continue
        r4 = sorted(rays + [x])
        sec = [Fraction(s) for s in sectors(r4)]
        if foldcheck.kawasaki(sec) and foldcheck.valid_words(sec):
            good.append(x)
    ok(good == [360 - rays[1]], f'kit p{pg} start {name}: the only fourth ray that folds flat is at {good}')

k1_p6 = [d['word'] for p in GEOM['k-1'] if p['page'] == 6 for d in p['discs']]
ok(len(k1_p6) == 8 and set(k1_p6) == set(foldcheck.valid_words([90, 90, 90, 90])),
   'K-1 Problem 6 route words A-H are exactly the eight foldable words of the right-angle disk')
print(f'{fails} failures')
sys.exit(1 if fails else 0)
