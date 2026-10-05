"""Code wheels and coded messages in the Week 4 grades 2-3 and 4-5 packets.

1. Wheels: reads the 26 letters of each printed wheel (angle, radius), checks equal spacing,
   clockwise A..Z from the top, the wheel diameters, that the outer letters stay outside the inner
   wheel, and simulates "set the wheel to D" by turning the inner wheel's letter angles.
2. Codes: reads the typewriter letters from the pages, groups them into words by spacing, tries all
   26 settings and keeps the settings whose every word is an English word (wordfreq / english-words
   lists), so uniqueness of each crack is tested, not assumed.
3. Tables: Problem 9 (2-3) and Problems 6, 10, 11 (4-5)."""
import math
import os
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import PDFDIR, A, shift

BAD = []


def bad(m):
    BAD.append(m)
    print('  !!', m)


# ---------------------------------------------------------------- word lists
def load_words():
    from wordfreq import top_n_list, zipf_frequency
    from english_words import get_english_words_set
    common = {w.upper() for w in top_n_list('en', 60000) if w.isalpha()}
    web2 = {w.upper() for w in get_english_words_set(['web2'], lower=True, alpha=True)}
    return common, web2, zipf_frequency


COMMON, WEB2, ZIPF = load_words()


def is_word(w, lex):
    return w in lex or (w.endswith('S') and w[:-1] in lex)


# ---------------------------------------------------------------- wheels
def wheel(doc, pno):
    page = doc[pno - 1]
    letters = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                if s['font'].endswith('Bold') and len(s['text'].strip()) == 1 and s['text'].strip() in A:
                    x0, y0, x1, y1 = s['bbox']
                    letters.append((s['text'].strip(), (x0 + x1) / 2, (y0 + y1) / 2, s['bbox']))
    circles = [d for d in page.get_drawings() if ''.join(it[0] for it in d['items']) == 'cccc' and d['rect'].width > 100]
    c = circles[0]['rect']
    cx, cy, R = (c.x0 + c.x1) / 2, (c.y0 + c.y1) / 2, c.width / 2
    out = {}
    for ch, x, y, bb in letters:
        ang = (90 - math.degrees(math.atan2(cy - y, x - cx))) % 360   # clockwise from the top
        # nearest distance from the centre to the glyph box
        nx, ny = min(max(cx, bb[0]), bb[2]), min(max(cy, bb[1]), bb[3])
        out[ch] = dict(ang=ang, r=math.hypot(x - cx, y - cy), rmin=math.hypot(nx - cx, ny - cy))
    return dict(cx=cx, cy=cy, R=R, letters=out, ry=c.height / 2)


def check_wheels(path, outer_p, inner_p, band):
    doc = pymupdf.open(path)
    o, i = wheel(doc, outer_p), wheel(doc, inner_p)
    for name, w in (('outer', o), ('inner', i)):
        L = w['letters']
        ok_set = sorted(L) == list(A)
        steps = [(L[A[(j + 1) % 26]]['ang'] - L[A[j]]['ang']) % 360 for j in range(26)]
        print(f'{band} {name} wheel: diameter {2 * w["R"] / 72:.3f} in (x) / {2 * w["ry"] / 72:.3f} in (y); '
              f'26 letters: {ok_set}; A at {L["A"]["ang"]:.3f} deg from top; clockwise step '
              f'{min(steps):.3f}-{max(steps):.3f} deg (360/26 = {360 / 26:.3f}); letter radius '
              f'{min(v["r"] for v in L.values()):.1f}-{max(v["r"] for v in L.values()):.1f}pt')
        if not ok_set or max(steps) - min(steps) > 0.6 or abs(L['A']['ang']) > 0.5 and abs(L['A']['ang'] - 360) > 0.5:
            bad(f'{band} {name} wheel irregular')
    vis = min(v['rmin'] for v in o['letters'].values())
    print(f'{band}: closest outer-letter glyph box to the centre {vis:.1f}pt; inner wheel radius {i["R"]:.1f}pt '
          f'-> outer letters visible around the inner wheel: {vis > i["R"]}')
    if vis <= i['R']:
        bad(f'{band}: outer letters hidden')
    # set the wheel to D: turn the inner wheel so that inner A is beside outer D
    turn = o['letters']['D']['ang'] - i['letters']['A']['ang']
    mapping = {}
    for ch, v in i['letters'].items():
        a = (v['ang'] + turn) % 360
        mapping[ch] = min(o['letters'], key=lambda c2: min(abs(o['letters'][c2]['ang'] - a), 360 - abs(o['letters'][c2]['ang'] - a)))
    cat = ''.join(mapping[c] for c in 'CAT')
    is_shift3 = all(mapping[c] == shift(c, 3) for c in A)
    print(f'{band}: wheel set to D codes CAT as {cat}; every letter moves 3 along: {is_shift3}')
    if cat != 'FDW' or not is_shift3:
        bad(f'{band}: wheel setting D')
    # decoding rule printed in the guide: find the code letter on the outer wheel, read the inner letter
    inv = {v: k for k, v in mapping.items()}
    print(f'{band}: outer->inner on the wheel decodes VWDU as {"".join(inv[c] for c in "VWDU")}; '
          f'inner->outer (the usual mistake) gives {"".join(mapping[c] for c in "VWDU")}')


# ---------------------------------------------------------------- codes
def code_lines(path, pno):
    page = pymupdf.open(path)[pno - 1]
    chars = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                if 'Inconsolata' in s['font']:
                    x0, y0, x1, y1 = s['bbox']
                    # a span can hold several letters separated by spaces; place each by its advance
                    t = s['text']
                    w = (x1 - x0) / max(1, len(t))
                    for j, ch in enumerate(t):
                        if ch.strip():
                            chars.append((round((y0 + y1) / 2), x0 + w * (j + 0.5), ch))
    rows = {}
    for y, x, ch in chars:
        rows.setdefault(y, []).append((x, ch))
    out = []
    for y in sorted(rows):
        cs = sorted(rows[y])
        pitch = min(cs[j + 1][0] - cs[j][0] for j in range(len(cs) - 1)) if len(cs) > 1 else 23
        words, cur = [], cs[0][1]
        for (xa, _), (xb, ch) in zip(cs, cs[1:]):
            if xb - xa > 1.5 * pitch:
                words.append(cur)
                cur = ch
            else:
                cur += ch
        words.append(cur)
        out.append((y, ' '.join(words)))
    return out


def crack(code, lex):
    return [(A[s], shift(code, -s)) for s in range(26) if all(is_word(w, lex) for w in shift(code, -s).split())]


def check_codes():
    M = os.path.join(PDFDIR, 'week-04-grades-2-3.pdf')
    U = os.path.join(PDFDIR, 'week-04-grades-4-5.pdf')
    print('\n== 2-3 Problem 4 (setting D)')
    lines4 = [t for y, t in code_lines(M, 4)]
    print('codes read:', lines4)
    dec = [shift(t, -3) for t in lines4]
    print('decoded with D:', dec)
    if dec != ['STAR', 'FOX', 'WHEEL', 'PENCIL', 'I CAN DRAW A STAR']:
        bad('2-3 P4 decode')

    print('\n== 2-3 Problem 8 (unknown settings); codes that wrap are joined')
    l8 = [t for y, t in code_lines(M, 7)]
    print('lines read:', l8)
    msgs = [l8[0] + ' ' + l8[1], l8[2] + ' ' + l8[3]]
    for m, (want_s, want) in zip(msgs, [('H', 'A STAR CAN HAVE TEN POINTS'), ('Q', 'MEET ME BY THE BIG TREE')]):
        c1, c2 = crack(m, COMMON), crack(m, WEB2)
        print(f'{m}: all-word settings (60k common words) {c1}; (web2, 235k words) {c2}')
        if (want_s, want) not in c1 or len(c1) != 1:
            bad(f'2-3 P8 crack {m}')

    print('\n== 4-5 Problem 4 (unknown settings)')
    l4 = [t for y, t in code_lines(U, 4)]
    print('lines read:', l4)
    msgs = [l4[0] + ' ' + l4[1], l4[2] + ' ' + l4[3], l4[4], l4[5]]
    want = [('J', 'I DREW A STAR WITH TWELVE POINTS'), ('S', 'WE MEET AT NOON BY THE BIG TREE'), ('X', 'BALLOON')]
    for m, w in zip(msgs[:3], want):
        c1, c2 = crack(m, COMMON), crack(m, WEB2)
        print(f'{m}: all-word settings (common) {c1}; (web2) {c2}')
        if w not in c1 or len(c1) != 1:
            bad(f'4-5 P4 crack {m}')
    last = msgs[3]
    print(f'last code {last}: every setting')
    for s in range(26):
        d = shift(last, -s)
        print(f'   {A[s]} {d}  zipf={ZIPF(d.lower(), "en"):.2f} common={d in COMMON} web2={d in WEB2}')
    words_last = [(A[s], shift(last, -s)) for s in range(26) if shift(last, -s) in COMMON or shift(last, -s) in WEB2]
    print('   settings giving a listed word:', words_last)

    # the hint: a seven-letter word with two pairs of doubles, as a shift of YXIILLK
    seven = sorted(w for w in WEB2 | COMMON if len(w) == 7 and w[2] == w[3] and w[4] == w[5]
                   and len({w[0], w[1], w[2], w[4], w[6]}) == 5)
    shifts_of = [w for w in seven if all((A.index(a) - A.index(b)) % 26 == (A.index('Y') - A.index(w[0])) % 26
                                         for a, b in zip('YXIILLK', w))]
    print(f'\nseven-letter words shaped like BALLOON (ab cc dd e): {len(seven)}, e.g. {seven[:12]}; '
          f'shifts of YXIILLK among them: {shifts_of}')


def check_tables():
    print('\n== 2-3 Problem 9: second setting that gives the word back')
    for s in 'DHNW':
        back = [A[t] for t in range(26) if all(shift(shift(c, A.index(s)), t) == c for c in A)]
        print(f'   first {s}: second {back}')
    print('== 4-5 Problem 6: two settings in a row')
    for a, b in ['HK', 'DF', 'TM', 'PL']:
        single = [A[t] for t in range(26) if all(shift(shift(c, A.index(a)), A.index(b)) == shift(c, t) for c in A)]
        print(f'   {a} then {b} = {single}')
    miss = [A[t] for t in range(26) if all(shift(shift(c, A.index('H')), t) == c for c in A)]
    print(f'   H then ? = A: {miss}')
    print('== 4-5 Problem 10: is every double coding a single setting?')
    ok = all(any(all(shift(shift(c, s), t) == shift(c, u) for c in A) for u in range(26))
             for s in range(26) for t in range(26))
    ident = [(A[s], A[t]) for s in range(1, 26) for t in range(1, 26) if (s + t) % 26 == 0]
    print(f'   every pair is one setting: {ok}; pairs of non-A settings that leave the message uncoded: {len(ident)} '
          f'(e.g. {ident[6]})')
    print('== 4-5 Problem 11: repeating a setting from A')
    for s in range(26):
        seq, x = ['A'], 'A'
        while True:
            x = shift(x, s)
            if x == 'A':
                break
            seq.append(x)
        if s in (2, 13, 0) or len(seq) == 26:
            pass
    full = [A[s] for s in range(26) if len({shift('A', s * j) for j in range(26)}) == 26]
    seqC, x = ['A'], 'A'
    while True:
        x = shift(x, 2)
        if x == 'A':
            break
        seqC.append(x)
    print(f'   setting C from A: {"".join(seqC)} ({len(seqC)} letters); settings through all 26: {full} ({len(full)})')


if __name__ == '__main__':
    print('== Wheels')
    check_wheels(os.path.join(PDFDIR, 'week-04-grades-2-3.pdf'), 8, 9, '2-3')
    check_wheels(os.path.join(PDFDIR, 'week-04-grades-4-5.pdf'), 10, 11, '4-5')
    check_codes()
    check_tables()
    print('\nSUMMARY:', 'all checks agree' if not BAD else BAD)
