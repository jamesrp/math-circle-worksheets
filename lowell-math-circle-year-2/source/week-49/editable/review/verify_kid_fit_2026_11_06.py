#!/usr/bin/env python3
"""Check the November 6, 2026 kid-fit revision (v4 packets) in the Week 49 PDFs.

Usage: python3 review/verify_kid_fit_2026_11_06.py [folder]
(default: reference-pdfs/). Needs pypdf only. Reads k-1.pdf, grades-2-3.pdf,
grades-4-5.pdf and facilitator-guide.pdf from the folder: page counts, footer ids,
the order of the numbered problems in each band, the K-1 cup rule, and the guide's
renumbered keys and materials. The mathematics behind the keys is checked by
src/check.py; the mat sizes by facilitator-src/verify_pdfs.py. The October 23 card
fixes' own check, review/verify_card_fixes_2026_10_23.py, describes the v3 PDFs,
which are archived in the project.
"""
from pathlib import Path
import re
import sys

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent


def pages(path):
    return [' '.join(p.extract_text().split()) for p in PdfReader(path).pages]


# (pages, footer tag, [(problem number, opening words, page)])
BANDS = {
    'k-1': (7, 'F49-K-v4', [
        (1, 'Build these starts', 2), (2, 'Put 0, 1, 2, and 4', 3), (3, 'Choose heights from 0 to 4', 4),
        (4, 'Find different starts that become all zeros in one move', 5),
        (5, 'Find starts that take exactly two moves', 5), (6, 'Try both starts', 6)]),
    'grades-2-3': (8, 'F49-23-v4', [
        (1, 'Run each start', 2), (2, 'Try different orders of 0, 1, 2, and 4', 3),
        (3, 'Choose starting heights from 0 to 5', 4), (4, 'Could each ring be the result', 5),
        (5, 'Use the gap rule on both rings', 6), (6, 'Can a new tower be taller', 8)]),
    'grades-4-5': (8, 'F49-45-v4', [
        (1, 'Run each start until all four heights are 0. Which lasts longer?', 2),
        (2, 'Choose starting heights from 0 to 5', 3), (3, 'Could each ring be the result', 4),
        (4, 'Use the gap rule on both rings', 5), (5, 'Replace even heights by E', 7),
        (6, 'Compare these two starts', 8), (7, 'Could any new height exceed', 8),
        (8, 'Do four nonnegative whole-number heights', 8)]),
}


def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'reference-pdfs'
    for name, (count, tag, problems) in BANDS.items():
        text = pages(folder / f'{name}.pdf')
        assert len(text) == count, (name, len(text))
        for i, t in enumerate(text, 1):
            assert t.startswith('Week 49 / Four towers and differences /'), (name, i)
            assert f'Bellingham Math Circle / Week 49 / {tag} {i}' in t, (name, i)
        found = [(int(m.group(1)), i) for i, t in enumerate(text, 1) for m in re.finditer(r'Problem (\d+):', t)]
        assert [n for n, _ in found] == list(range(1, len(problems) + 1)), (name, found)
        for n, words, page in problems:
            assert f'Problem {n}: {words}' in text[page - 1], (name, n, words, page)
    assert 'drop a counter in the cup' in pages(folder / 'k-1.pdf')[0]
    print('PASS packets: K-1 7 pages, Grades 2-3 8 and Grades 4-5 8, footers F49-K-v4, F49-23-v4 and F49-45-v4; '
          'the v4 problem order in every band; the K-1 page-1 rules end with the cup.')

    g = ' '.join(pages(folder / 'facilitator-guide.pdf'))
    for need in ('Facilitator guide v4 | Student packets v4', 'Revised 6 November 2026 (kid-fit)',
                 'each K-1 pair also needs a cup and 10 counters', 'takes 36 of the 40 cubes, so that table needs all 40',
                 'drop one counter in the cup after each move', 'Grades 4-5 run only the first and last',
                 'Longest run: K-1 and Grades 2-3 Problem 3, Grades 4-5 Problem 2', 'K-1 Problem 4. Exactly the positive',
                 'K-1 Problem 5. Examples (0,1,0,1)', 'what ring turns into 1,1,1,1?',
                 'Grades 2-3 Problem 4; Grades 4-5 Problem 3', 'K-1 Problem 6; Grades 2-3 Problem 5; Grades 4-5 Problem 4',
                 'K-1 and Grades 2-3 Problem 2. Both printed orders last 4 moves', 'Grades 2-3 Problem 6; Grades 4-5 Problem 7',
                 'two columns of letter boxes', 'Grades 4-5 Problem 6. The first printed start',
                 'First routes: K-1 P1 and P2'):
        assert need in g, need
    for gone in ('Older Problem', 'older Problem', 'Problem 2, all bands', 'four columns of letter boxes',
                 'K-1 Problem 6; Grades 2-3 Problem 5.', 'Final student packets v3'):
        assert gone not in g, gone
    print('PASS guide: v4 subtitle, cup and 10 counters for K-1, 36 of the 40 cubes for the 4-5 doubled start, and every '
          'key and route reference renumbered to the v4 packets.')


if __name__ == '__main__':
    main()
