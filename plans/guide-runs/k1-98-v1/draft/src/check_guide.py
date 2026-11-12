#!/usr/bin/env python3
"""Independent Week 98 guide checks, using only Python stdlib and Poppler.

Seed coordinates were transcribed from the FINAL nine-page student PDF and
visually checked, not imported from the student generator or its checker.
The exact input fingerprint binds those transcriptions to the inspected PDF.
"""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
from math import ceil, comb
import hashlib
import subprocess
import re

HERE = Path(__file__).resolve().parent
EXPECTED_SHA = '804470c9ad7a0b88c393dda83e8e510796e0da749db79bab402328f50565f86a'


def student_pdf():
    beside = HERE.parent / 'k-1.pdf'
    if beside.is_file():
        return beside
    for root in HERE.parents:
        candidate = root / 'plans/k1-drafts/week-98/k-1.pdf'
        if candidate.is_file():
            return candidate
    raise FileNotFoundError('Place k-1.pdf beside src/ (or guide-src/) before checking.')


def engine(rows, cols):
    full = (1 << (rows * cols)) - 1
    neighbors = []
    for i in range(rows * cols):
        r, c = divmod(i, cols)
        neighbors.append(sum(1 << (rr*cols+cc) for rr,cc in
                             [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
                             if 0 <= rr < rows and 0 <= cc < cols))
    def legal(mask):
        return [i for i,n in enumerate(neighbors)
                if not mask >> i & 1 and (mask & n).bit_count() >= 2]
    def closure(mask):
        while True:
            additions = legal(mask)
            if not additions:
                return mask
            mask |= sum(1 << i for i in additions)
    def encode(cells):
        return sum(1 << ((r-1)*cols+c-1) for r,c in cells)
    def coords(mask):
        return tuple((i//cols+1,i%cols+1) for i in range(rows*cols) if mask >> i & 1)
    return full, legal, closure, encode, coords, neighbors


def minimum_fillers(rows, cols):
    full, legal, closure, encode, coords, neighbors = engine(rows, cols)
    for size in range(rows*cols+1):
        answers = []
        for cells in combinations(range(rows*cols), size):
            mask = sum(1 << i for i in cells)
            if closure(mask) == full:
                answers.append(mask)
        if answers:
            return size, answers


def main():
    src = student_pdf()
    assert hashlib.sha256(src.read_bytes()).hexdigest() == EXPECTED_SHA, 'Student PDF differs from the visually inspected final input.'
    txt = subprocess.check_output(['pdftotext', '-layout', str(src), '-'], text=True)
    pages = txt.split('\f')
    if not pages[-1].strip(): pages.pop()
    assert len(pages) == 9
    for i,p in enumerate(pages,1):
        assert re.findall(r'Problem\s+(\d+):',p) == [str(i)], (i,'number mismatch')
    assert 'two or more' in pages[0]
    assert 'Put each seed back before you try the next one' in pages[7]
    assert 'Can you end with a different number of seeds?' in pages[8]
    print('PASS: exact final student PDF, 9 pages, Problems 1-9, revised rules.')

    f, legal, cl, enc, coords, nbs = engine(2,2)
    pairs = [enc(c) for c in combinations([(1,1),(1,2),(2,1),(2,2)],2)]
    winners = {enc([(1,1),(2,2)]),enc([(1,2),(2,1)])}
    assert len(pairs) == 6 and {m for m in pairs if cl(m)==f} == winners
    assert all(cl(m)==m for m in pairs if m not in winners)
    assert all(cl(1 << i) == (1 << i) for i in range(4))
    assert 3+2+1 == 6
    print('P1: six placements, two diagonal fillers, four adjacent pairs stuck; one seed never grows.')

    f, legal, cl, enc, coords, nbs = engine(3,3)
    starts = [((1,1),(1,2),(2,1)), ((2,1),(2,2),(2,3)),
              ((1,1),(1,3),(2,1)), ((1,1),(2,1),(3,1),(1,3))]
    assert [cl(enc(s)).bit_count() for s in starts] == [4,3,6,9]
    assert [bool(legal(enc(s))) for s in starts] == [True,False,True,True]
    assert coords(cl(enc(starts[0]))) == ((1,1),(1,2),(2,1),(2,2))
    assert coords(cl(enc(starts[2]))) == tuple((r,c) for r in [1,2] for c in [1,2,3])
    print('P2: top-left/top-right/bottom-left/bottom-right finishes 4,3,6,9.')

    # Complete searches, including every smaller cardinality; no old checker imported.
    for n, expected in [(3,14),(4,130),(5,1615)]:
        size, ways = minimum_fillers(n,n)
        f,l,c,e,co,nb = engine(n,n)
        assert size == n and len(ways) == expected
        assert c(e([(i,i) for i in range(1,n+1)])) == f
        assert c(e([(i,n+1-i) for i in range(1,n+1)])) == f
        print(f'P{n}: {n}x{n} minimum {size}, {len(ways)}/{comb(n*n,n)} starts at that size fill; all smaller starts checked.')

    strip_answers = {3:[(1,3)], 4:[(1,2,4),(1,3,4)], 5:[(1,3,5)],
                     6:[(1,2,4,6),(1,3,4,6),(1,3,5,6)]}
    for length, answers in strip_answers.items():
        size, ways = minimum_fillers(1,length)
        f,l,c,e,co,nb = engine(1,length)
        assert {co(m) for m in ways} == {tuple((1,x) for x in a) for a in answers}
        assert size == {3:2,4:3,5:3,6:4}[length]
        # Enumerate every start to check the structural explanation, not just witnesses.
        for mask in range(f+1):
            bits = [bool(mask >> i & 1) for i in range(length)]
            criterion = bits[0] and bits[-1] and all(bits[i] or bits[i+1] for i in range(length-1))
            assert (c(mask)==f) == criterion
        print(f'P6: 1x{length} minimum {size}, ALL optimal starts {answers}.')

    witnesses = {3:[(1,1),(2,2),(3,1)],4:[(1,1),(2,2),(4,1)],
                 5:[(1,1),(2,2),(4,1),(5,2)]}
    for rows, expected in [(3,10),(4,8),(5,48)]:
        size, ways = minimum_fillers(rows,2)
        f,l,c,e,co,nb = engine(rows,2)
        assert size == ceil((rows+2)/2) and len(ways) == expected
        assert c(e(witnesses[rows])) == f
        print(f'P7: {rows}x2 minimum {size}, {len(ways)} optimal starts, printed witness checked.')

    take_one = [(2,2,[(1,1),(1,2),(2,1)],[(1,1)]),
                (3,3,[(1,1),(1,3),(3,1),(3,3)],[(1,1),(1,3),(3,1),(3,3)]),
                (3,3,[(1,1),(1,3),(2,2),(3,1)],[(1,1),(2,2)]),
                (3,3,[(1,2),(2,1),(2,3),(3,2)],[])]
    for rows,cols,seeds,removable in take_one:
        f,l,c,e,co,nb = engine(rows,cols)
        start=e(seeds)
        assert c(start)==f
        assert [s for s in seeds if c(start ^ e([s]))==f] == removable
        if not removable:
            assert [c(start ^ e([s])).bit_count() for s in seeds] == [6,6,6,6]
        print('P8:', seeds, 'removable singly:',removable,'all deletion sizes:',[c(start ^ e([s])).bit_count() for s in seeds])

    f,l,c,e,co,nb = engine(3,3)
    start=e([(1,1),(1,2),(1,3),(2,1),(3,1)])
    @lru_cache(None)
    def routes(mask):
        removable = [i for i in range(9) if mask>>i&1 and c(mask^(1<<i))==f]
        if not removable: return (((),mask),)
        return tuple(((i,)+word,end) for i in removable for word,end in routes(mask^(1<<i)))
    allroutes=routes(start)
    endings={end for word,end in allroutes}
    assert endings=={e([(1,2),(1,3),(2,1),(3,1)]),e([(1,1),(1,3),(3,1)])}
    assert len(allroutes)==3
    assert {co(1<<word[0])[0] for word,end in allroutes}=={(1,1),(1,2),(2,1)}
    assert sorted(len(word) for word,end in allroutes)==[1,2,2]
    for word,end in allroutes:
        print('P9 removal route:',[co(1<<i)[0] for i in word],'; ending:',co(end))

    # Exhaustively all legal orders for every 3x3 start (memoized terminal sets).
    @lru_cache(None)
    def terminals(mask):
        moves=l(mask)
        if not moves: return frozenset([mask])
        return frozenset(t for i in moves for t in terminals(mask|(1<<i)))
    for mask in range(512): assert terminals(mask)==frozenset([c(mask)])
    print('PASS: every legal completed order for every 3x3 start has one finish.')

    # Perimeter change checked for every legal addition on every 3x3 state.
    def perimeter(mask):
        return sum(4-(mask & nb[i]).bit_count() for i in range(9) if mask>>i&1)
    for mask in range(512):
        for i in l(mask):
            k=(mask & nb[i]).bit_count()
            assert perimeter(mask|(1<<i))-perimeter(mask)==4-2*k <= 0
    assert [4-2*k for k in [2,3,4]] == [0,-2,-4]
    for r,cc in [(2,2),(3,3),(4,4),(5,5),(3,2),(4,2),(5,2)]:
        assert ceil(2*(r+cc)/4) == ceil((r+cc)/2)

    # Shared launch is the non-task 2x3 nonminimum start, not a P7 answer.
    f,l,c,e,co,nb=engine(2,3)
    demo=e([(1,1),(2,1),(2,2)])
    assert l(demo)==[1] and co(c(demo))==((1,1),(1,2),(2,1),(2,2))
    assert c(demo)!=f
    # Student page 1 pictures: target has THREE or ONE filled side-neighbors.
    f,l,c,e,co,nb=engine(3,3)
    assert (e([(1,2),(2,1),(2,3)]) & nb[4]).bit_count()==3
    assert (e([(1,2),(3,3)]) & nb[4]).bit_count()==1
    assert 5+20==25 and 6+20==26 and 2*6==12 and 2*20==40
    assert 4*5==20 and 10+2+10+15+15+8==60
    assert all(n*30==m for n,m in [(2,60),(3,90),(4,120),(5,150),(6,180)])
    print('PASS: demo, final rule pictures, perimeter changes, sizes and kit counts.')
    guide=HERE.parent/'k1-guide.pdf'
    if guide.is_file():
        gt=subprocess.check_output(['pdftotext','-layout',str(guide),'-'],text=True)
        gp=[p for p in gt.split('\f') if p.strip()]
        assert len(gp)==4
        assert all('W98-K-FAC-v1' in p for p in gp)
        assert all('K–1 adult guide' in p or 'K-1 adult guide' in p for p in gp)
        print('PASS: four guide pages; required repeated header/footer.')
    print('All independent guide checks passed.')

if __name__=='__main__': main()
