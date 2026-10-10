"""Independent mathematical check of Week 76 (substitution strips, A->AB, B->BA).

Generates the Thue-Morse word itself, reads every printed strip from the
student source (students.tex) and from the delivered student PDF, and checks
each problem and each answer in the adult guide by enumeration.  Nothing from
the packet's own checker scripts is imported.
Run: python3 check_math.py   (writes check_math.out beside itself)
"""
import itertools
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
SRC = os.path.join(REPO, 'lowell-math-circle-year-2', 'source', 'week-76')
PDF = os.path.join(REPO, 'lowell-math-circle-year-2', 'week-76')
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- the word
SUB = {'A': 'AB', 'B': 'BA'}


def mu(w):
    return ''.join(SUB[c] for c in w)


ROWS = ['A']
for _ in range(18):
    ROWS.append(mu(ROWS[-1]))
T = ROWS[-1]                                  # 2^18 letters
for a, b in zip(ROWS, ROWS[1:]):
    assert b.startswith(a)
check(all(T[2 * n] == T[n] and T[2 * n + 1] != T[n] for n in range(len(T) // 2)),
      'T[2n]=T[n], T[2n+1]=complement T[n] on the 2^18 prefix')

FACT = {}


def factors(n, word=T):
    if (n, len(word)) not in FACT:
        FACT[(n, len(word))] = {word[i:i + n] for i in range(len(word) - n + 1)}
    return FACT[(n, len(word))]


def is_factor(w):
    return w in factors(len(w))


# factor sets have stabilised (uniform recurrence): same set in 2^14 and 2^18
for n in range(1, 25):
    assert factors(n, ROWS[14]) == factors(n)
say('factor counts p(n), n=1..12:', [len(factors(n)) for n in range(1, 13)])

BANS = ['AAA', 'BBB', 'ABABA', 'BABAB']
check(not any(b in T for b in BANS), 'no AAA, BBB, ABABA, BABAB in 2^18 prefix')
check(all(T[i] != T[i + 1] for i in range(0, len(T) - 1, 2)),
      'every even-start (true) pair is unequal')
check(all(i % 2 == 1 for i in range(len(T) - 1) if T[i] == T[i + 1]),
      'equal neighbours start only at odd indices')


# ---------------------------------------------------------------- pairings
def pairings(w):
    """All pairings of w into AB/BA using every tile except at most one lone
    tile at each end.  Returns list of (lead_lone, pairs, tail_lone)."""
    res = []
    for lead in (0, 1):
        rest = len(w) - lead
        tail = rest % 2
        body = w[lead:len(w) - tail]
        pairs = [body[i:i + 2] for i in range(0, len(body), 2)]
        if all(p[0] != p[1] for p in pairs):
            res.append((w[:lead], pairs, w[len(w) - tail:] if tail else ''))
    return res


def kept(p):
    return ''.join(x[0] for x in p[1])


def full_parent(p):
    """Parent letters including the lone tiles (a leading lone tile is the
    second half of its pair, so its parent is its complement; a trailing lone
    tile is a first half, so its parent is itself)."""
    lead, pairs, tail = p
    comp = {'A': 'B', 'B': 'A'}
    return (comp[lead] if lead else '') + kept(p) + (tail if tail else '')


def show(p):
    lead, pairs, tail = p
    parts = (['(' + lead + ')'] if lead else []) + pairs + (['(' + tail + ')'] if tail else [])
    return ' | '.join(parts)


def realised_alignments(w):
    """Parities of start positions at which w occurs in T."""
    return sorted({i % 2 for i in range(len(T) - len(w) + 1) if T.startswith(w, i)})


# ---------------------------------------------------------------- printed strips
tex = open(os.path.join(SRC, 'student', 'students.tex')).read()
pages = tex.split('\\newpage')
strips = [[s.replace(',', '') for s in re.findall(r'\\Strip\{[^}]*\}\{[^}]*\}\{([AB,]+)\}', pg)]
          for pg in pages]
say('strips per page (source):', strips)

# same strips in delivered PDF (letters read in reading order, grouped by line)
try:
    import pymupdf as fitz
    doc = fitz.open(os.path.join(PDF, 'week-76-students.pdf'))
    check(doc.page_count == 4, 'student PDF has 4 pages')
    for k, page in enumerate(doc):
        # strip letters are set in \\large (14.4pt); body text is 12pt
        words = []
        for b in page.get_text('dict')['blocks']:
            for ln in b.get('lines', []):
                for sp in ln['spans']:
                    if sp['text'].strip() in ('A', 'B') and sp['size'] > 13:
                        words.append((sp['bbox'][0], sp['bbox'][1], sp['bbox'][2],
                                      sp['bbox'][3], sp['text'].strip()))
        lines = {}
        for w in words:
            lines.setdefault(round((w[1] + w[3]) / 2), []).append(w)
        rows = []
        for y in sorted(lines):
            ws = sorted(lines[y], key=lambda w: w[0])
            cx = [(w[0] + w[2]) / 2 for w in ws]
            cell = min([b - a for a, b in zip(cx, cx[1:])] or [1])
            # split a line where letter spacing exceeds 1.3 cells (separate strips)
            cur = ''
            for i, w in enumerate(ws):
                if i and cx[i] - cx[i - 1] > 1.3 * cell:
                    rows.append(cur)
                    cur = ''
                cur += w[4]
            rows.append(cur)
        want = list(strips[k])
        if k == 2:   # the dashed lone A of the worked example is a node, not a Strip
            want.insert(1, 'A')
        check(rows == want, 'PDF page %d strips match source: %s' % (k + 1, rows))
except ImportError:
    say('pymupdf unavailable; PDF strip comparison skipped')

# ---------------------------------------------------------------- page 1
p1 = strips[0]
check(p1[:3] == ['BA', 'BA', 'AB'] and p1[3] == mu('BA') == 'BAAB',
      'worked example: BA -> BA AB -> BAAB')
r16 = ROWS[4]
say('16-tile row:', r16)
tri16 = sorted({r16[i:i + 3] for i in range(14)})
tri8 = sorted({ROWS[3][i:i + 3] for i in range(6)})
say('P1 distinct triples in 16-row:', tri16, len(tri16), '; in 8-row:', tri8)
check(tri16 == ['AAB', 'ABA', 'ABB', 'BAA', 'BAB', 'BBA'], 'P1 answer = guide list (6)')
check(tri8 == tri16, 'P1 all six already in 8-row (guide)')
check(sorted(factors(3)) == tri16, 'P1 the six are all triples of T')
check(len(r16) - 3 + 1 == 14, 'P1 14 window starts (guide)')
check(all(any(n % 2 == 0 for n in (i, i + 1)) for i in range(100)),
      'P2 each 3-window holds an even-start pair')

# ---------------------------------------------------------------- page 2
p2 = strips[1]
check(p2[:5] == ['BAABBA', 'BA', 'AB', 'BA', 'BAB'] and mu('BAB') == 'BAABBA',
      'P3 worked example BAABBA -> BA AB BA -> BAB')
claims = p2[5:]
say('P3 claims:', claims)


def undo_chain(w):
    chain = [w]
    while len(chain[-1]) > 1:
        x = chain[-1]
        if len(x) % 2:
            return chain, 'odd length'
        prs = [x[i:i + 2] for i in range(0, len(x), 2)]
        bad = [p for p in prs if p[0] == p[1]]
        if bad:
            return chain, 'bad pair ' + bad[0]
        chain.append(''.join(p[0] for p in prs))
    return chain, 'reaches ' + chain[-1]


verdicts = []
for c in claims:
    chain, why = undo_chain(c)
    whole = c in ROWS
    verdicts.append(whole)
    say('  ', c, '->', ' -> '.join(chain[1:]), '|', why, '| whole row:', whole,
        '| factor of T:', is_factor(c))
check(verdicts == [True, False, False, False], 'P3 only claim 1 is a whole row (guide)')
check([len(c) for c in claims] == [8, 8, 8, 16], 'P3 claim lengths all powers of 2 (no length shortcut)')
check([c == ROWS[len(c).bit_length() - 1] for c in claims] == verdicts,
      'P3 SHORTCUT: comparing with the 8/16 rows built in P1 settles every claim')

# ---------------------------------------------------------------- page 3
p3 = strips[2]
check(p3[:4] == ['AABBA', 'AB', 'BA', 'AB'] and re.search(r'draw\[dashed[^\n]*\n\\node[^\n]*\{A\};', pages[2]) is not None,
      'P4 worked example AABBA -> (A, dashed) AB BA -> AB')
we = pairings('AABBA')
check(len(we) == 1 and show(we[0]) == '(A) | AB | BA' and kept(we[0]) == 'AB' and is_factor('AABBA'),
      'P4 worked example has exactly that one pairing and is genuine')
crops = p3[4:]
say('P4 crops:', crops)
guide4 = {'ABA': (['AB | (A)', '(A) | BA'], ['A', 'B']),
          'BAABA': (['BA | AB | (A)'], ['BA']),
          'AABB': (['(A) | AB | (B)'], ['A']),
          'ABBAABBA': (['AB | BA | AB | BA'], ['ABAB'])}
check(crops == list(guide4), 'P4 crop order matches guide table')
for c in crops:
    ps = pairings(c)
    say('  ', c, 'factor:', is_factor(c), 'parities in T:', realised_alignments(c),
        'pairings:', [show(p) for p in ps], 'kept:', [kept(p) for p in ps],
        'kept factors:', [is_factor(kept(p)) for p in ps if kept(p)])
    check(is_factor(c), 'P4 %s genuinely occurs' % c)
    check(sorted(show(p) for p in ps) == sorted(guide4[c][0])
          and sorted(kept(p) for p in ps) == sorted(guide4[c][1]),
          'P4 %s pairings/kept match guide' % c)
    check(len(realised_alignments(c)) == len(ps), 'P4 %s every pairing is realised in T' % c)

# P5: five-tile crops
f5 = sorted(factors(5))
multi = [w for w in f5 if len(pairings(w)) != 1]
say('P5 five-tile factors:', f5)
check(not multi, 'P5 no genuine 5-crop has two pairings (none exists)')
check(all(any(w[i] == w[i + 1] for i in range(4)) for w in f5), 'P5 every 5-crop has equal neighbours')
for n in range(5, 25):
    assert all(len(pairings(w)) == 1 for w in factors(n)), n
check(True, 'guide: every genuine crop of length 5..24 has exactly one pairing')
short2 = {n: sorted(w for w in factors(n) if len(pairings(w)) == 2) for n in range(1, 5)}
say('crops of length 1..4 with two pairings:', short2)
for w in ('ABABA', 'BABAB'):
    ps = pairings(w)
    say('  ', w, 'pairings:', [show(p) for p in ps], 'full parents:', [full_parent(p) for p in ps])
    check(all(full_parent(p) in ('AAA', 'BBB') for p in ps), 'P5 %s forces AAA/BBB parents' % w)

# P5 under a looser reading: one lone tile allowed anywhere (not only at an end)
def loose_pairings(w):
    res = []
    for k in range(0, len(w), 2):            # lone tile at an even index of a 5-tile piece
        prs = [w[i:i + 2] for i in range(0, k, 2)] + [w[i:i + 2] for i in range(k + 1, len(w), 2)]
        if all(len(p) == 2 and p[0] != p[1] for p in prs):
            res.append(' | '.join(prs[:k // 2] + ['(' + w[k] + ')'] + prs[k // 2:]))
    return res


loose = {w: loose_pairings(w) for w in f5 if len(loose_pairings(w)) > 1}
say('P5 if the one lone tile may sit mid-piece, genuine 5-crops with 2+ pairings:', loose)

# ---------------------------------------------------------------- page 4
p4 = strips[3]
check(p4[0] == 'AB' * 8 and p4[1] == 'ABBA' * 4, 'P6 printed strips are (AB)^8 and (ABBA)^4')
for name, per in (('AB', 'AB'), ('ABBA', 'ABBA')):
    S = per * 50
    check(not any(b in S for b in ('AAA', 'BBB')), 'P6 (%s)^inf has no AAA/BBB' % name)
    say('P6 (%s)^inf contains ABABA/BABAB:' % name, [b for b in ('ABABA', 'BABAB') if b in S])
    for n in range(1, 13):
        bad = sorted(w for w in {S[i:i + n] for i in range(len(per))} if not is_factor(w))
        if bad:
            say('   shortest non-factors of (%s)^inf, length %d:' % (name, n), bad)
            break
check('ABABA' not in factors(5), 'P6 ABABA impossible')
check(not is_factor('ABBAABBAAB') and is_factor('ABBAABBA'),
      'P6 ABBAABBAAB impossible; ABBAABBA genuine (guide)')
ps = pairings('ABBAABBAAB')
check(len(ps) == 1 and kept(ps[0]) == 'ABABA', 'P6 ABBAABBAAB forced split decodes to ABABA')

# which windows of the ABBA strip give a contradiction by complete-pair
# decoding only, versus also using the lone end tiles' (determined) parents
S = 'ABBA' * 50
say('P6 ABBA strip, by start offset: first length at which the window is a non-factor;')
say('   first length at which complete pairs alone decode to a non-factor;')
for off in range(4):
    nf = next(n for n in range(1, 30) if not is_factor(S[off:off + n]))
    cp = next(n for n in range(5, 30)
              if all(not is_factor(kept(p)) for p in pairings(S[off:off + n])))
    w = S[off:off + nf]
    say('   offset %d: non-factor at n=%d (%s, pairing %s, full parents %s); complete pairs alone: n=%d (%s)'
        % (off, nf, w, [show(p) for p in pairings(w)], [full_parent(p) for p in pairings(w)],
           cp, [kept(p) for p in pairings(S[off:off + cp])]))
for w in ('BBAABBAA', 'AABBAABB'):
    p = pairings(w)
    check(not is_factor(w) and len(p) == 1 and is_factor(kept(p[0]))
          and full_parent(p[0]) in ('ABABA', 'BABAB'),
          'P6 8-tile %s is impossible, but its complete pairs keep only %s; '
          'lone-tile parents give %s' % (w, kept(p[0]), full_parent(p[0])))

# ---------------------------------------------------------------- P7 sanity
# (not a proof) no period p<=4096 on the second half of the prefix
L = len(T)
N0 = L // 2
ok = all(T[N0 + p:] != T[N0:L - p] for p in range(1, 4097))
check(ok, 'P7 sanity: no p<=4096 is a period of the second half of the 2^18 prefix')
check(all(T[4 * k:4 * k + 4] in ('ABBA', 'BAAB') for k in range(len(T) // 4)),
      'P7 aligned four-blocks are ABBA/BAAB')

# ---------------------------------------------------------------- delivered guide text
import subprocess
g = subprocess.run(['pdftotext', os.path.join(PDF, 'week-76-facilitator.pdf'), '-'],
                   capture_output=True, text=True).stdout
g = re.sub(r'\s+', ' ', g)
for frag in ['AAB, ABA, ABB, BAA, BAB, BBA', '14 possible starting places',
             'ABBABAAB \u2192 ABBA \u2192 AB \u2192 A', 'ABBAABBA \u2192 ABAB \u2192 AA',
             'AB | BA | BB | AB', 'ABBABAABABBABAAB \u2192 ABBAABBA \u2192 ABAB \u2192 AA',
             'BAABA BA | AB | (A) BA', 'AABB (A) | AB | (B) A', 'ABBAABBA AB | BA | AB | BA ABAB',
             'ABBAABBAAB', 'AABBA has (A) | AB | BA, keeping AB']:
    check(frag in g, 'guide PDF contains: ' + frag)

# ---------------------------------------------------------------- guide arithmetic
check(8 + 16 <= 32, 'kit: largest build 8 old + 16 new <= 32 tiles')
check(3 * 36 == 108 and 3 * 4 + 2 == 14 and 4 + 2 == 6, 'kit totals 108 tiles, 14 / 6 dividers')
check((3 + 1) * 4 == 16 and (4 + 1) * 4 == 20, 'print counts 16 and 20 sheets')

say('')
say('FAILURES:', len(FAIL))
for f in FAIL:
    say('  ', f)
text = '\n'.join(OUT) + '\n'
open(os.path.join(HERE, 'check_math.out'), 'w').write(text)
print(text)
