#!/usr/bin/env python3
"""Independent capped-game solver and direct final-PDF diagram check.
Requires Python 3 and PyMuPDF (fitz). No student sources or old checkers used.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
import argparse, hashlib
import fitz

HERE = Path(__file__).resolve().parent
PIN = 'a6a6e52ed4a391ccd6e10f7cd7444c779f612e73be21e58d97ac27d46d264738'
PAGE = {1:1,2:2,3:2,4:3,5:3,6:4,7:4,8:5,9:5,10:6,11:7,12:7}
STARTS = {
 1:[(n,) for n in [2,5,3,6,4,7,11,10]],
 2:[(1,1),(2,0),(0,2),(2,1),(1,2),(2,2)],
 3:[(1,1),(2,1),(1,2),(3,1),(2,3),(3,3)],
 4:[(4,2),(3,4)],5:[(2,2)],
 8:[(0,1),(0,2),(0,3),(1,1),(2,2),(3,3)],
 9:[(0,0,1),(0,0,2),(0,0,3)],
 10:[(2,0,1),(1,0,1),(0,1,1),(1,1,1)],
 11:[(0,1,1),(1,1,1),(0,0,3)],12:[(2,2,2)]}

def student_file():
    nearby = HERE.parent / 'k-1.pdf'
    if nearby.exists(): return nearby
    for parent in HERE.parents:
        p = parent / 'plans/k1-drafts/week-81/k-1.pdf'
        if p.exists(): return p
    raise FileNotFoundError('Place the final k-1.pdf beside src (one folder above this script).')

def vector_counts(page, lo, hi):
    """Count filled circular paths inside rounded rectangular buckets in PDF order."""
    ds = page.get_drawings()
    circles = [d['rect'] for d in ds if d['type']=='f' and
               [v[0] for v in d['items']]==['c']*4 and
               5 < d['rect'].width < 11 and abs(d['rect'].width-d['rect'].height)<.1]
    boxes = [d['rect'] for d in ds if d['type']=='s' and
             [v[0] for v in d['items']]==['l','c']*4 and
             29<d['rect'].width<53 and 40<d['rect'].height<72 and
             lo<d['rect'].y0<hi]
    return [sum(r.contains((c.tl+c.br)/2) for c in circles) for r in boxes]

def flatten(rows): return [x for row in rows for x in row]

def verify_student(p):
    assert hashlib.sha256(p.read_bytes()).hexdigest()==PIN, 'Student PDF differs from inspected final version'
    pdf=fitz.open(p); assert len(pdf)==7
    actual={}
    for n, pn in PAGE.items():
        page=pdf[pn-1]; loc=page.search_for(f'Problem {n}:'); assert len(loc)==1
        later=[page.search_for(f'Problem {m}:')[0].y0 for m in PAGE if PAGE[m]==pn and m>n]
        counts=vector_counts(page,loc[0].y1,min(later,default=740))
        if n in [3,10]:
            k=len(STARTS[n][0]); actual[n]=[tuple(counts[i:i+k]) for i in range(0,len(counts),2*k)]
            assert all(counts[i+j]==0 for i in range(k,len(counts),2*k) for j in range(k))
        elif n==5:
            actual[n]=[tuple(counts[:2])]; assert len(counts)==14 and counts[2:]==[0]*12
        elif n in [6,7]:
            assert counts==[0]*(20 if n==6 else 2); continue
        else:
            k=len(STARTS[n][0]); actual[n]=[tuple(counts[i:i+k]) for i in range(0,len(counts),k)]
        assert actual[n]==STARTS[n], (n,actual[n],STARTS[n])
    rule=vector_counts(pdf[0],50,pdf[0].search_for('Problem 1:')[0].y0)
    assert rule==flatten([(3,2),(3,1),(4,1),(1,0,2),(1,0,1),(2,0,1),(1,1,1),(2,1,1)])
    txt=' '.join(pdf[0].get_text().split())
    assert 'Start each game with Removed empty.' in txt
    assert 'into bucket 1, into bucket 2, or into both.' in txt
    print('Final student PDF: all 12 numbered problems, page map, 21 rule buckets and all task dots checked.')

@lru_cache(None)
def moves(s):
    out=[]
    for j,n in enumerate(s):
        if n:
            for bits in product((0,1),repeat=j):
                q=list(s); q[j]-=1
                for i,b in enumerate(bits): q[i]+=b
                q=tuple(q)
                assert weight(q)<weight(s)
                out.append((q,j,bits))
    return tuple(out)

def weight(s): return sum((1<<i)*x for i,x in enumerate(s))
@lru_cache(None)
def win(s): return any(not win(q) for q,_,_ in moves(s))
@lru_cache(None)
def lengths(s):
    return frozenset(1+n for q,_,_ in moves(s) for n in lengths(q)) if any(s) else frozenset([0])
@lru_cache(None)
def peak(s): return max([sum(s)]+[peak(q) for q,_,_ in moves(s)])
def winners(s): return [q for q,_,_ in moves(s) if not win(q)]
def fmt(s): return '('+','.join(map(str,s))+')'
def macro(name,s): return '\\newcommand{\\'+name+'}{'+s+'}\n'
def winnerword(s): return '1st' if win(s) else '2nd'

def check_math():
    # Exhaust every legal descendant, not only one suggested strategy.
    for k, bound in [(1,12),(2,8),(3,5)]:
        for s in product(range(bound+1),repeat=k):
            assert win(s)==any(x%2 for x in s)
            assert lengths(s)==frozenset(range(sum(s),weight(s)+1))
            if any(x%2 for x in s): assert len(winners(s))==1
            else:
                for q,j,bits in moves(s):
                    r=list(q);r[j]-=1
                    for i,b in enumerate(bits): r[i]+=b
                    assert all(x>=0 and x%2==0 for x in r)
                    assert any(t==tuple(r) for t,_,_ in moves(q))
    assert [winnerword(s) for s in STARTS[1]]==['2nd','1st','1st','2nd','2nd','1st','1st','2nd']
    assert [winnerword(s) for s in STARTS[2]]==['1st','2nd','2nd','1st','1st','2nd']
    assert [winnerword(s) for s in STARTS[4]]==['2nd','1st']
    assert winners((3,4))==[(2,4)]
    assert sum([5,5,3,10,15,15,7])==60
    assert [winners(s) for s in STARTS[3]]==[[(2,0)],[(2,0)],[(0,2)],[(4,0)],[(2,2)],[(4,2)]]
    assert [winners(s) for s in STARTS[10]]==[[(2,0,0)],[(2,0,0)],[(0,2,0)],[(2,2,0)]]
    assert [(min(lengths(s)),max(lengths(s))) for s in STARTS[8]]==[(1,2),(2,4),(3,6),(2,3),(4,6),(6,9)]
    assert [peak(s) for s in STARTS[9]]==[2,4,6]
    for n in (1,2,3):
        s=(0,0,n)
        for _ in range(n):
            s=next(q for q,j,b in moves(s) if j==2 and b==(1,1))
        assert s==(n,n,0) and sum(s)==2*n
    assert [max(lengths(s)) for s in STARTS[11]]==[6,7,12]
    assert (min(lengths((2,2,2))),max(lengths((2,2,2))),peak((2,2,2)))==(6,14,8)
    # All split lists, including impossibility, not a parity-only assumed answer.
    splits={t:[(a,t-a) for a in range(t+1) if not win((a,t-a))] for t in (4,5,6)}
    assert splits=={4:[(0,4),(2,2),(4,0)],5:[],6:[(0,6),(2,4),(4,2),(6,0)]}
    # Launch uses a non-task input; neither bucket-2 option is its winning move.
    assert (3,2) not in sum(STARTS.values(),[])
    assert [q for q,j,b in moves((3,2)) if j==1]==[(3,1),(4,1)]
    assert all(win(q) for q,j,b in moves((3,2)) if j==1)
    assert [q for q,j,b in moves((1,0,2)) if j==2]==[(1,0,1),(1,1,1),(2,0,1),(2,1,1)]
    # Physical pool: counters in Removed + buckets never exceed eventual longest length.
    starts=[s for rows in STARTS.values() for s in rows]+[(a,t-a) for t in (4,5,6) for a in range(t+1)]
    assert max(max(lengths(s)) for s in starts)==14
    print(f'Math PASS: exhaustive outcomes, all lengths, unique winning moves and copy replies; {win.cache_info().currsize} states visited.')
    print('P5 complete replies:',[(q,winners(q)) for q,_,_ in moves((2,2))])
    print('All second-player splits:',splits)
    # Generate tables exclusively from recomputed outputs. Assertions above fix expected results.
    out='% Generated by independent check_guide.py; do not edit.\n'
    out+=macro('OneBucketRow',' & '.join(str(s[0]) for s in STARTS[1])+r' \\ '+ '\n'+' & '.join(winnerword(s) for s in STARTS[1])+r' \\')
    out+=macro('TwoBucketRow',' & '.join('$'+fmt(s)+'$' for s in STARTS[2])+r' \\ '+'\n'+' & '.join(winnerword(s) for s in STARTS[2])+r' \\')
    for name,n in [('FirstMoves',3),('ThreeMoves',10)]:
        out+=macro(name,'\n'.join('$'+fmt(s)+'$ & $'+fmt(winners(s)[0])+'$'+r' \\' for s in STARTS[n]))
    for name,n in [('FirstMovesWide',3),('ThreeMovesWide',10)]:
        out+=macro(name,'Start & '+' & '.join('$'+fmt(s)+'$' for s in STARTS[n])+r' \\ '+'\n'+'After & '+' & '.join('$'+fmt(winners(s)[0])+'$' for s in STARTS[n])+r' \\')
    out+=macro('LengthsWide','Start & '+' & '.join('$'+fmt(s)+'$' for s in STARTS[8])+r' \\ '+'\n'+'Shortest & '+' & '.join(str(min(lengths(s))) for s in STARTS[8])+r' \\ '+'\n'+'Longest & '+' & '.join(str(max(lengths(s))) for s in STARTS[8])+r' \\')
    out+=macro('CopyReplies','\n'.join('$'+fmt(q)+'$ & $'+fmt(winners(q)[0])+'$'+r' \\' for q,_,_ in moves((2,2))))
    out+=macro('LengthRows','\n'.join('$'+fmt(s)+'$ & '+str(min(lengths(s)))+' & '+str(max(lengths(s)))+r' \\' for s in STARTS[8]))
    return '\n'.join(line.rstrip() for line in out.splitlines())+'\n'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write-data',action='store_true');a=ap.parse_args()
    verify_student(student_file()); data=check_math(); target=HERE/'verified-data.tex'
    if a.write_data: target.write_text(data)
    else:
        assert target.read_text()==data, 'Regenerate verified-data.tex with --write-data'
        pdf=fitz.open(HERE.parent/'k1-guide.pdf');assert len(pdf)==4
        assert vector_counts(pdf[1],0,740)==[3,2,3,1,4,1], 'Guide demonstration dots differ'
        for i,p in enumerate(pdf,1):
            text=p.get_text();assert 'W81-K-FAC-v1' in text and 'K–1 adult guide' in text
            assert 'Week 81 / Buckets of Fish' in text
        full=' '.join(' '.join(p.get_text().split()) for p in pdf)
        for n in range(1,13): assert f'Problem {n} ' in full
        print('Guide PASS: four pages, all 12 solution headings, correct running identifiers, verified generated answer tables.')
if __name__=='__main__': main()
