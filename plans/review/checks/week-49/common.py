"""Shared helpers for the Week 49 math check (Four-tower differences).

Written from scratch for this review. Nothing here imports or reads the
packet's own builders or checkers (src/make.py, draw.py, verify*.py,
facilitator-src/verify_math.py, week-49-bonus/student/verify.py).

Geometry and printed data are read from the DELIVERED PDFs with Poppler only:
  * pdftocairo -svg  -> vector paths (lines, arrowheads, circles, squares) in
    PDF points, y measured downward from the top of the page;
  * pdftotext -bbox  -> every printed word with its bounding box.

The mathematical model is the one printed on the student pages:
  base and bonus page 1: new height at a station = |old height - next old height|
                         (next = head of the station's outgoing arrow, or the
                         next letter A-B-C-D-A on the bonus page), all
                         stations updated from one unchanged old ring;
  bonus page 2:          the same rule on 0/1 heights (exclusive or), next =
                         next number, wrapping to 1;
  bonus page 3:          directed rule new = next old - current old.
"""
import math
import os
import re
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
# Committed location: plans/review/checks/week-49/ -> four folders up.
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    # Fallback when run from the scratch run folder (tmp/review-runs/week-49/).
    d = HERE
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
        d = os.path.dirname(d)
    ROOT = d

WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-49')
PDFS = {
    'K-1': os.path.join(WEEK, 'week-49-k-1.pdf'),
    '2-3': os.path.join(WEEK, 'week-49-grades-2-3.pdf'),
    '4-5': os.path.join(WEEK, 'week-49-grades-4-5.pdf'),
    'guide': os.path.join(WEEK, 'week-49-facilitator.pdf'),
    'bonus': os.path.join(WEEK, 'week-49-bonus.pdf'),
    'bonus-guide': os.path.join(WEEK, 'week-49-bonus-facilitator.pdf'),
}
PT_MM = 25.4 / 72.0


# ----------------------------------------------------------------- dynamics
def D(s):
    """Simultaneous cyclic absolute differences: new_i = |s_i - s_{i+1}|."""
    n = len(s)
    return tuple(abs(s[i] - s[(i + 1) % n]) for i in range(n))


def E(s):
    """Directed rule of bonus page 3: new_i = s_{i+1} - s_i."""
    n = len(s)
    return tuple(s[(i + 1) % n] - s[i] for i in range(n))


def run(s, f=D, limit=10000):
    """Trajectory until all-zero or until a whole state repeats.

    Returns (states, outcome, moves) where outcome is 'zero' or
    ('repeat', first_index) and moves counts arrows taken.
    """
    s = tuple(s)
    states = [s]
    seen = {s: 0}
    while any(states[-1]) and len(states) < limit:
        t = f(states[-1])
        states.append(t)
        if not any(t):
            break
        if t in seen:
            return states, ('repeat', seen[t]), len(states) - 1
        seen[t] = len(states) - 1
    return states, 'zero', len(states) - 1


def moves_to_zero(s):
    states, outcome, m = run(s)
    assert outcome == 'zero', (s, outcome)
    return m


def fmt(s):
    return '(' + ','.join(str(x) for x in s) + ')'


# ---------------------------------------------------------------- reporting
class Log:
    def __init__(self, title, name=None):
        self.name = name or os.path.splitext(os.path.basename(
            __import__('__main__').__file__))[0]
        self.lines = []
        self.fails = []
        self.p('# ' + title)

    def p(self, *a):
        s = ' '.join(str(x) for x in a)
        print(s)
        self.lines.append(s)

    def check(self, cond, msg):
        tag = 'OK  ' if cond else 'FAIL'
        self.p(f'[{tag}] {msg}')
        if not cond:
            self.fails.append(msg)
        return cond

    def finish(self):
        self.p('')
        self.p(f'Summary: {len(self.fails)} FAIL line(s).')
        for f in self.fails:
            self.p('  FAIL: ' + f)
        with open(os.path.join(HERE, self.name + '.out'), 'w') as fh:
            fh.write('\n'.join(self.lines) + '\n')


# ------------------------------------------------------------ PDF extraction
def npages(pdf):
    out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    return int(re.search(r'Pages:\s+(\d+)', out).group(1))


def page_text(pdf, layout=False):
    args = ['pdftotext'] + (['-layout'] if layout else []) + [pdf, '-']
    return subprocess.run(args, capture_output=True, text=True).stdout


def words(pdf, page):
    out = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), pdf, '-'],
                         capture_output=True, text=True).stdout
    res = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', out):
        x0, y0, x1, y1 = map(float, m.groups()[:4])
        txt = (m.group(5).replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>'))
        res.append({'t': txt, 'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1,
                    'cx': (x0 + x1) / 2, 'cy': (y0 + y1) / 2, 'h': y1 - y0})
    return res


_NUM = r'-?\d+(?:\.\d+)?(?:e-?\d+)?'


def _parse_d(d):
    toks = re.findall(r'[MLCZmlcz]|' + _NUM, d)
    segs = []   # list of (cmd, [points])
    i = 0
    cmd = None
    while i < len(toks):
        t = toks[i]
        if t in 'MLCZmlcz':
            cmd = t.upper()
            i += 1
            if cmd == 'Z':
                segs.append(('Z', []))
            continue
        k = {'M': 2, 'L': 2, 'C': 6}[cmd]
        vals = [float(v) for v in toks[i:i + k]]
        segs.append((cmd, [(vals[j], vals[j + 1]) for j in range(0, k, 2)]))
        i += k
    return segs


def shapes(pdf, page):
    """Vector paths of one page (outside <defs>) in points, y downward."""
    with tempfile.TemporaryDirectory() as td:
        f = os.path.join(td, 'p.svg')
        subprocess.run(['pdftocairo', '-svg', '-f', str(page), '-l', str(page), pdf, f], check=True)
        svg = open(f).read()
    body = svg.split('</defs>', 1)[1]
    res = []
    for m in re.finditer(r'<path ([^>]*?)/>', body):
        attrs = dict(re.findall(r'([\w:-]+)="([^"]*)"', m.group(1)))
        if 'd' not in attrs:
            continue
        a, b, c, dd, e, f_ = 1, 0, 0, 1, 0, 0
        if 'transform' in attrs:
            mm = re.match(r'matrix\(([^)]*)\)', attrs['transform'])
            a, b, c, dd, e, f_ = [float(v) for v in mm.group(1).split(',')]
        segs = _parse_d(attrs['d'])

        def T(p):
            return (a * p[0] + c * p[1] + e, b * p[0] + dd * p[1] + f_)
        onpts = []
        cmds = []
        for cmd, pts in segs:
            cmds.append(cmd)
            if cmd in 'ML':
                onpts.append(T(pts[0]))
            elif cmd == 'C':
                onpts.append(T(pts[2]))
        if not onpts:
            continue
        xs = [p[0] for p in onpts]
        ys = [p[1] for p in onpts]
        fill = attrs.get('fill', '')
        res.append({
            'cmds': ''.join(cmds), 'pts': onpts, 'fill': fill,
            'stroke': attrs.get('stroke', ''),
            'x0': min(xs), 'x1': max(xs), 'y0': min(ys), 'y1': max(ys),
            'cx': (min(xs) + max(xs)) / 2, 'cy': (min(ys) + max(ys)) / 2,
            'w': max(xs) - min(xs), 'h': max(ys) - min(ys),
        })
    return res


WHITE = 'rgb(100%, 100%, 100%)'


def is_black(fill):
    m = re.match(r'rgb\(([\d.]+)%, ([\d.]+)%, ([\d.]+)%\)', fill)
    return bool(m) and all(float(v) < 25 for v in m.groups())


def classify(shs):
    """Split shapes into stations (white closed shapes), lines, arrowheads."""
    stations, lines, heads = [], [], []
    for s in shs:
        if s['fill'] == WHITE and 'Z' in s['cmds'] and s['w'] > 8 and s['h'] > 8:
            kind = 'circle' if set(s['cmds']) <= set('MCZ') else 'square'
            st = dict(s)
            st['kind'] = kind
            stations.append(st)
        elif s['fill'] == 'none' and s['cmds'] in ('ML',) and len(s['pts']) == 2:
            lines.append(s)
        elif is_black(s['fill']) and 'Z' in s['cmds'] and max(s['w'], s['h']) < 15 and 'C' not in s['cmds']:
            hd = dict(s)
            hd['tip'] = s['pts'][0]
            heads.append(hd)
    return stations, lines, heads


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def inside(w, st, pad=0.0):
    return st['x0'] - pad <= w['cx'] <= st['x1'] + pad and st['y0'] - pad <= w['cy'] <= st['y1'] + pad
