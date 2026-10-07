#!/usr/bin/env python3
"""Independent verification of the five-page final Week 77 prototype.

The sibling baseline_check.py verifies Problems 1--5. It is an unchanged copy
of the original independent review, distinct from this entrypoint. Usage:
  python3 portable_check.py --source-dir ../student --verify-only
No PDF, TeX, Poppler, external package, network, or original workspace is needed.
An optional --pdf FILE performs an additional text audit using pdftotext; visual
inspection of the original final PDF is documented separately. --results FILE
writes the complete JSON result in addition to the concise terminal summary.
Problem 6 uses a new integer edge-mask calculation, direct trail enumeration,
and every fill order. Neither writer/reviser check_math.py was read or imported.

For the fan, each triangular face has a unique outer edge. Therefore the map
from face subsets to their mod-2 boundaries is injective. A saved loop with
unique support S disappears precisely when every face in S is filled; its death
in a one-face-at-a-time schedule is max(position(f) for f in S). This proves the
order claims and the completeness of the finite boundary tests below.
"""
from pathlib import Path
import argparse
import contextlib
import hashlib
import io
import itertools
import json
import re
import runpy
import subprocess
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-dir', type=Path, required=True,
                    help='Directory containing packaged students.tex and README.md')
parser.add_argument('--verify-only', action='store_true',
                    help='Verify source consistency and mathematics without building or reading a PDF (the default).')
parser.add_argument('--pdf', type=Path,
                    help='Optional existing PDF to text-audit; requires pdftotext only when supplied.')
parser.add_argument('--results', type=Path, help='Optional destination for complete JSON results.')
args = parser.parse_args()
if not __debug__:
    parser.error('Run without Python -O: this independent verifier uses assertions.')
source_dir = args.source_dir.resolve()
for name in ('students.tex', 'README.md'):
    if not (source_dir/name).is_file():
        parser.error(f'--source-dir must contain {name}')
HERE = Path(__file__).resolve().parent
original_path = HERE / 'baseline_check.py'
if original_path.resolve() == Path(__file__).resolve():
    parser.error('The entrypoint must be separate from baseline_check.py.')
if not original_path.is_file():
    parser.error('Place baseline_check.py beside this entrypoint.')
original_hash = hashlib.sha256(original_path.read_bytes()).hexdigest()
with contextlib.redirect_stdout(io.StringIO()) as prior_output:
    prior = runpy.run_path(str(original_path))
previous = json.loads(prior_output.getvalue())
assert previous['result'] == 'PASS'
assert hashlib.sha256(original_path.read_bytes()).hexdigest() == original_hash

# Source consistency is independent of PDF extraction. These mathematical
# inputs were read from the reviewed final source and its five rendered pages.
# We check per-page task statements, stage lists, coordinate maps, edge paths,
# and the material conventions. No immutable source hash is assumed: packaging
# additions to README and non-mathematical whitespace changes are permitted.
source = (source_dir/'students.tex').read_text(encoding='utf-8')
readme = (source_dir/'README.md').read_text(encoding='utf-8')
pages = source.split(r'\newpage')
assert len(pages) == 5, 'Expected five source pages.'
normalize = lambda text: ' '.join(text.split())
compact = lambda text: ''.join(text.split())
assert [re.findall(r'\\textbf\{Problem (\d+):\}', p) for p in pages] == [
    ['1'], ['2'], ['3'], ['4','5'], ['6']]

def require(page, *fragments):
    text = normalize(pages[page-1])
    for fragment in fragments:
        assert normalize(fragment) in text, (page, fragment)

require(1,
    'Use only the printed edge places. During a build, add pieces and keep them.',
    'all three edges are in place when a triangle is filled',
    'Dashed lines are places for edges; solid lines are already present.',
    'AB and BA name the same edge.',
    'A loop follows edges back to its starting dot without repeating an edge.',
    'To test it, copy those tokens, add the edge tokens of any filled triangles you choose, and remove matching pairs.',
    'The loop is gone if a choice leaves no tokens. Only the test tokens change.',
    'For example, using filled triangle XYZ on the tokens XY and YZ:',
    'Start with the dots only. Build a loop that can disappear after just one triangle is filled.',
    'Start again and build a loop that survives either choice of a single filled triangle.',
    'Test the two choices in separate builds.')
require(2,
    'Save the first loop when it closes.',
    'Find every schedule in which that saved loop first disappears at stage 8.',
    'Count each enclosed, unfilled region as one hole.',
    'Every allowed schedule has 0, 1, 2, 1, 0 holes after stages 0, 2, 4, 5, 8.')
require(3,
    'Start with the four solid edges. Add one dashed edge at stage 2 and the other at stage 4.',
    'Fill one triangle at stage 5 and the other at stage 8.',
    'Make one build where the first loop is gone at 5, and another where it first disappears at 8.',
    "Save the first loop's edges each time",
    'Both builds have 0, 1, 2, 1, 0 holes after stages 0, 2, 4, 5, 8.',
    'Can those counts alone tell you when the first loop disappears?')
require(4,
    'Stage 4 is one step: place its edge, then its tile, and check only after both are in place.',
    'Does it ever have two holes at a finished stage?',
    'Move exactly one of those two additions to stage 3 or 5 so that it does.',
    'Find every legal change. Keep all other additions at their original stages.',
    'Could a saved loop be gone at one stage and survive again at a later stage, if no edge or filled triangle is removed?',
    'Explain why your answer works for every legal growing board.')
require(5,
    'Start with all eight edges and filled triangles ABO and BCO.',
    'Save two loops with different sets of edges.',
    'Both must survive now and first disappear at the last filling, whichever of the two unfilled triangles your partner fills first.',
    'Can you choose your pair so that either loop can disappear first on a fresh board with all eight edges and no filled triangles?',
    'Keep the two saved edge lists unchanged. Fill all four triangles, one at a time.',
    'Show a filling order for each outcome, or explain why it is impossible.')

def stage_list(page):
    return [(int(t), normalize(description)) for t, description in
            re.findall(r'Stage (\d+): ([^}]+)\}', pages[page-1])]

assert stage_list(2) == [(0,'AB, BC, CD'), (2,'one of DA and AC'),
                        (4,'the other edge'), (5,'fill ABC or ACD'),
                        (8,'fill the other triangle')]
assert stage_list(4) == [(0,'AB, BC, CD'), (2,'DA'),
                        (4,'AC and filled ABC'), (8,'filled ACD')]

def coordinates(text):
    return {v: (float(x),float(y)) for v,x,y in
            re.findall(r'\\coordinate\s*\((\w+)\)\s*at\s*\(([-\d.]+),\s*([-\d.]+)\)', text)}

# Macro geometry for repeated square boards, plus both explicit new diagrams.
macro = source.split(r'\newcommand{\squareboard}',1)[1].split(r'\newcommand{\pagebegin}',1)[0]
assert coordinates(macro) == {'A':(0,0),'B':(6.2,0),'C':(6.2,6.2),'D':(0,6.2)}
assert '(A)--(B)--(C)--(D)--cycle(A)--(C);' in compact(macro)
assert r'\ifnum#3=1\draw[linewidth=1.5pt](A)--(B)--(C)--(D);\fi' in compact(macro)
assert r'\squareboard{.65}{12.1}{0}' in compact(pages[0])
assert r'\squareboard{10.6}{6.3}{1}' in compact(pages[1])
assert r'\squareboard{10.6}{5.3}{1}' in compact(pages[3])
assert coordinates(pages[2]) == {'A':(0,0),'B':(0,5.8),'C':(5.8,2.9),'D':(11.6,0),'E':(11.6,5.8)}
assert '(A)--(C)--(B)(D)--(C)--(E);' in compact(pages[2])
assert '(A)--(B)(D)--(E);' in compact(pages[2])
assert coordinates(pages[4]) == {'A':(0,0),'B':(8,0),'C':(8,8),'D':(0,8),'O':(4,4)}
assert '(A)--(B)--(C)--(D)--cycle(A)--(O)--(C)(B)--(O)--(D);' in compact(pages[4])
assert r'\fill(O)circle(2.2pt);' in compact(pages[4])
assert 'x=1cm,y=-1cm' in compact(source)
# Input, intermediate pair cancellation, and output of the launch diagram.
for token in (r'\token{3.4}{6.25}{XY}{inxy}',r'\token{4.35}{6.25}{YZ}{inyz}',
              r'\token{6.95}{6.25}{XY}{a}',r'\token{7.95}{6.25}{YZ}{b}',
              r'\token{8.95}{6.25}{XY}{c}',r'\token{9.95}{6.25}{YZ}{d}',
              r'\token{10.95}{6.25}{XZ}{e}',r'\token{14.2}{6.25}{XZ}{out}'):
    assert token in compact(pages[0]), token
assert r'\foreach\nin{a,b,c,d}' in compact(pages[0])
for fragment in ('6.2 cm', '11.6 cm wide and 5.8 cm high', '8 cm sides',
                 'ABC/ACD', 'ABC/CDE', 'ABO/BCO/CDO/ADO',
                 'three tokens each for AB, BC, CD, AD, AC, CE, DE, AO, BO, CO, DO',
                 'two XY tokens, two YZ tokens, and one XZ token',
                 'one saved loop at a time', 'remove them only when resetting'):
    assert fragment in normalize(readme), fragment

pdf_audit = None
if args.pdf is not None:
    if not args.pdf.is_file():
        parser.error('--pdf must name an existing PDF')
    pdf_text = subprocess.check_output(['pdftotext', '-layout', str(args.pdf), '-'], text=True)
    assert pdf_text.count('\f') == 5
    flat = normalize(pdf_text)
    for n in range(1,7):
        assert flat.count(f'Problem {n}:') == 1
    for text in ('all three edges are in place when a triangle is filled',
                 'Stage 4 is one step: place its edge, then its tile, and check only after both are in place',
                 'Stage 2: one of DA and AC', 'Stage 5: fill ABC or ACD',
                 'Start with all eight edges and filled triangles ABO and BCO',
                 'Keep the two saved edge lists unchanged',
                 'Fill all four triangles, one at a time'):
        assert text in flat, text
    pdf_audit = {'result':'PASS', 'sha256':hashlib.sha256(args.pdf.read_bytes()).hexdigest()}

# These lists are transcribed from the final diagram, not from its checker.
vertices = 'ABCDO'
edges = ('AB', 'BC', 'CD', 'AD', 'AO', 'BO', 'CO', 'DO')
faces = ('ABO', 'BCO', 'CDO', 'ADO')
face_edges = {'ABO': ('AB', 'AO', 'BO'),
              'BCO': ('BC', 'BO', 'CO'),
              'CDO': ('CD', 'CO', 'DO'),
              'ADO': ('AD', 'AO', 'DO')}
edge_index = {e: 1 << i for i, e in enumerate(edges)}
face_masks = {f: sum(edge_index[e] for e in es) for f, es in face_edges.items()}


def selected_faces(mask):
    return [f for i, f in enumerate(faces) if mask & (1 << i)]


def selected_edges(mask):
    return sorted(e for i, e in enumerate(edges) if mask & (1 << i))


def boundary(face_set):
    result = 0
    for f in face_set:
        result ^= face_masks[f]
    return result


def boundaries(filled):
    filled = tuple(filled)
    return {boundary(f for i, f in enumerate(filled) if s & (1 << i))
            for s in range(1 << len(filled))}


# Enumerate every parity-valid edge chain independently of all face subsets.
cycles = {mask for mask in range(1 << len(edges))
          if all(sum(bool(mask & edge_index[e]) for e in edges if v in e) % 2 == 0
                 for v in vertices)}
assert len(cycles) == 16
support = {boundary(selected_faces(s)): frozenset(selected_faces(s)) for s in range(16)}
assert len(support) == 16
assert set(support) == cycles
# Each selected triangle can be read off from its unique outer edge.
for mask, fs in support.items():
    for f, outer in zip(faces, ('AB', 'BC', 'CD', 'AD')):
        assert bool(mask & edge_index[outer]) == (f in fs)

# Check the printed definition literally: closed walks with no edge repeated.
# Returning to the starting vertex is recorded but does not forbid continuation.
# This includes the two allowed figure-eight trails through the center.
trails = {}

def extend(start, current, mask, word):
    if current == start and mask:
        trails.setdefault(mask, ''.join(word))
    for e in edges:
        if current in e and not mask & edge_index[e]:
            nxt = e[1] if current == e[0] else e[0]
            extend(start, nxt, mask | edge_index[e], word + [nxt])

for start in vertices:
    extend(start, start, 0, [start])
assert set(trails) == cycles - {0}

initial = frozenset({'ABO', 'BCO'})
remaining = ('CDO', 'ADO')
allowed = []
for mask in sorted(trails):
    if mask in boundaries(initial):
        continue
    works = all(mask not in boundaries(initial | {first}) and
                mask in boundaries(faces) for first in remaining)
    if works:
        allowed.append(mask)
expected_supports = {frozenset({'CDO', 'ADO'}) | frozenset(extra)
                     for extra in ((), ('ABO',), ('BCO',), ('ABO', 'BCO'))}
assert {support[m] for m in allowed} == expected_supports
assert len(allowed) == 4

# Universal relation: ALL acceptable loops are equal and nonzero modulo the
# already filled faces; it does not follow that distinct edge lists are
# independent persistent features. Check all pairs and both later stages.
for first, second in itertools.combinations(allowed, 2):
    assert first != second
    assert first ^ second in boundaries(initial)
    for new_face in remaining:
        assert first ^ second in boundaries(initial | {new_face})
        assert first not in boundaries(initial | {new_face})
        assert second not in boundaries(initial | {new_face})

# All 24 four-face orders and all 15 nonempty saved edge cycles. The max-support
# law is checked against exact boundary membership at every completed stage.
orders = list(itertools.permutations(faces))
order_rows = []
deaths_by_order = {}
for order in orders:
    deaths = {}
    for mask in trails:
        at = next(n for n in range(5) if mask in boundaries(order[:n]))
        expected = max(order.index(f)+1 for f in support[mask])
        assert at == expected
        deaths[mask] = at
        for n in range(5):
            assert (mask in boundaries(order[:n])) == (at <= n)
    deaths_by_order[order] = deaths
    order_rows.append({'order': list(order),
                       'candidate_deaths': {trails[m]: deaths[m] for m in allowed}})

# Ordered outcome checks for EVERY unordered candidate pair, including ties.
pairs = []
reversible_pairs = []
for a, b in itertools.combinations(allowed, 2):
    before = [o for o in orders if deaths_by_order[o][a] < deaths_by_order[o][b]]
    after = [o for o in orders if deaths_by_order[o][b] < deaths_by_order[o][a]]
    tied = [o for o in orders if deaths_by_order[o][a] == deaths_by_order[o][b]]
    assert len(before) + len(after) + len(tied) == 24
    incomparable = not (support[a] <= support[b] or support[b] <= support[a])
    assert bool(before and after) == incomparable
    if before and after:
        reversible_pairs.append((a,b))
        assert (len(before), len(after), len(tied)) == (6,6,12)
    pairs.append({'first_edges': selected_edges(a), 'second_edges': selected_edges(b),
                  'first_strictly_before_count': len(before),
                  'second_strictly_before_count': len(after), 'tie_count': len(tied),
                  'first_before_example': list(before[0]) if before else None,
                  'second_before_example': list(after[0]) if after else None})
assert len(reversible_pairs) == 1
want = {frozenset({'ABO','CDO','ADO'}), frozenset({'BCO','CDO','ADO'})}
assert {support[m] for m in reversible_pairs[0]} == want

# Human-readable exact witnesses for the unique flexible pair.
def edge_list(word):
    return {''.join(sorted(pair)) for pair in zip(word, word[1:])}

word_a = 'ABOCDA'
word_b = 'AOBCDA'
a = sum(edge_index[e] for e in edge_list(word_a))
b = sum(edge_index[e] for e in edge_list(word_b))
assert {a,b} == set(reversible_pairs[0])
example_ab = ('CDO','ADO','ABO','BCO')
example_ba = ('CDO','ADO','BCO','ABO')
assert (deaths_by_order[example_ab][a], deaths_by_order[example_ab][b]) == (3,4)
assert (deaths_by_order[example_ba][a], deaths_by_order[example_ba][b]) == (4,3)
assert a ^ b == face_masks['ABO'] ^ face_masks['BCO']

# Exact chain quotient and inclusion ranks across the partly filled start,
# either next face, and both final faces. All candidates track one common class.
for first in remaining:
    sequence = [initial, initial|{first}, frozenset(faces)]
    dimensions = [4 - len(fs) for fs in sequence]
    assert dimensions == [2,1,0]
    for i, earlier in enumerate(sequence):
        earlier_classes = {min(c ^ x for x in boundaries(earlier)) for c in cycles}
        assert len(earlier_classes) == 2 ** dimensions[i]
        for j in range(i, len(sequence)):
            late_b = boundaries(sequence[j])
            images = {min(c ^ x for x in late_b) for c in cycles}
            # No new edges in this sequence: each inclusion is surjective.
            assert len(images) == 2 ** dimensions[j]

# Diagram: center is a real marked vertex; no two edge interiors cross. 8 cm
# square with four 16 cm^2 triangles partitions exactly 64 cm^2.
coords = {'A': (0,0), 'B': (8,0), 'C': (8,8), 'D': (0,8), 'O': (4,4)}
for e, f in itertools.combinations(edges, 2):
    if not set(e) & set(f):
        assert not prior['intersects'](coords[e[0]], coords[e[1]], coords[f[0]], coords[f[1]])
for f in faces:
    assert abs(prior['orient'](*(coords[v] for v in f))) == 32
assert sum(abs(prior['orient'](*(coords[v] for v in f))) for f in faces) == 128
assert set(face_masks.values()) <= cycles
# Each spoke lies in two faces, each outer edge in one. Three tokens of each
# edge suffice for a one-loop test, including all four filled triangles.
assert max(1 + sum(e in face_edges[f] for f in faces) for e in edges) == 3
# README was read from the user-selected portable source directory above.
for label in ('AO', 'BO', 'CO', 'DO', 'ABO/BCO/CDO/ADO', 'one saved loop at a time'):
    assert label in readme
assert 'center vertex' in readme and 'remove them only when resetting' in readme

results = {
    'result': 'PASS',
    'reviewed_files_sha256': {name: hashlib.sha256((source_dir/name).read_bytes()).hexdigest()
                            for name in ('students.tex', 'README.md')},
    'source_consistency': 'PASS: five pages, six tasks, stage lists, coordinates, paths, launch tokens, and materials',
    'optional_pdf_audit': pdf_audit,
    'preserved_original_checker_sha256': original_hash,
    'problems1to5': previous,
    'problem6': {
        'nonempty_closed_trail_edge_sets': len(trails),
        'eligible_loops': [{'edges': selected_edges(m), 'one_closed_walk': trails[m],
                            'unique_triangle_support': sorted(support[m])} for m in allowed],
        'universal_relation': 'All four eligible edge loops differ by boundaries of ABO and/or BCO; all represent the same nonzero class initially and after either single remaining fill.',
        'all_four_face_orders': order_rows,
        'all_six_unordered_candidate_pairs': pairs,
        'unique_reversible_pair': [word_a, word_b],
        'first_before_second_example': list(example_ab),
        'second_before_first_example': list(example_ba),
        'general_order_proof': 'The unique triangle support must be entirely filled; death is its maximum filling position. Both strict orders are possible exactly for incomparable supports.',
        'physical_readiness': 'Not tested.'}}
if args.results is not None:
    args.results.write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
print('PASS: source consistency, five pages and Problems 1-6.')
print('PASS: Problems 1-5 baseline, exact boundary witnesses and inclusion ranks.')
print('PASS: Problem 6, 15 loops, 4 qualifying loops, 6 pairs, 24 filling orders, 1 reversible pair.')
print('PASS: diagram coordinates, tied stages, token supplies, and no-resurrection argument.')
print('PDF audit: ' + ('PASS (text only; prior visual review is separate).' if pdf_audit else 'not requested; no PDF or pdftotext used.'))
