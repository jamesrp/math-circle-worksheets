#!/usr/bin/env python3
"""Independent exact checker for the final W58 return-visit guide.

Uses only Python 3 standard library and Poppler pdftotext. Final student PDFs
are hash-bound: the rows were transcribed and compared with every rendered page.
All allocations for each fixed train are examined, not the student checker.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, permutations, combinations
from math import comb
from collections import Counter
import hashlib, subprocess, sys

HERE = Path(__file__).resolve().parent
FILES = {
    'k-1.pdf': ('e2f7b33390031a2dd21d842d3c4536be969a0cf85cdb20c6722377cb0b06b11c', [1,2,3,4,5]),
    'grades-2-3.pdf': ('c355af82ef03fc15a32837b9d4d0cb2bc27214abc7cad0ce27a49d9e81cf7e5e', [1,2,3,4,5,6]),
    'grades-4-5.pdf': ('9a05f73c4fcd48c704f6ebeac740664019e74ff102602a086d1bd3abb7e09a32', [1,2,2,3,4,5,5,6]),
}
K1 = ['RBRB','RRBB','BRRB','BBRR','RBBR','BRBR']
K2 = ['RRRRBB','BRRBRR','RBRBR','RRBBBBRR','RRRRBBBB','RRRBBBBRRR','RRRRRRBBBB']
M2 = ['RRRRBB','RBBRRR','BRRBRRBB','RRRBBBBR','RBRRBRB','RRBRRRBBBR','RBBRRRRBBR']
U1 = ['RRRBBBBR','BRRBRBBR','RRRRBBBB','RBRRRRBRBB','BBRRRRRRBB','RRRRRRBB']


def students():
    candidates = [HERE.parent]
    candidates += [p/'plans'/'return-visit-drafts'/'week-58' for p in HERE.parents]
    for p in candidates:
        if all((p/f).is_file() for f in FILES):
            return p
    raise FileNotFoundError('Put k-1.pdf, grades-2-3.pdf and grades-4-5.pdf beside src/.')


def allocations(row):
    """Assign cards independently to two trays; transitions are required cuts.
    Adjacent pieces assigned to the same tray can be merged, so this gives the
    exact minimum. Fix first card in tray 0 to quotient tray exchange only.
    """
    nr, nb = row.count('R'), row.count('B')
    if nr%2 or nb%2: return None, []
    if not row: return 0, [()]
    best, answers = len(row), set()
    for tail in product((0,1), repeat=len(row)-1):
        mask = (0,) + tail
        if sum(x==1 and c=='R' for x,c in zip(mask,row)) != nr//2: continue
        if sum(x==1 and c=='B' for x,c in zip(mask,row)) != nb//2: continue
        cuts = tuple(i for i in range(1,len(row)) if mask[i]!=mask[i-1])
        if len(cuts)<best: best, answers = len(cuts), {cuts}
        elif len(cuts)==best: answers.add(cuts)
    return best, sorted(answers)


def bar(row, cuts):
    return ''.join(('|' if i in cuts else '')+c for i,c in enumerate(row))


def all_orders(r,b):
    for spots in combinations(range(r+b),r):
        ss=set(spots)
        yield ''.join('R' if i in ss else 'B' for i in range(r+b))


V = {'A':{'X':4,'Y':8,'Z':0}, 'B':{'X':0,'Y':4,'Z':8}, 'C':{'X':8,'Y':0,'Z':4}}

def val(order, who, a, b):
    return sum(F(max(0,min(b,F(50*(j+1)))-max(a,F(50*j))),50)*V[who][c]
               for j,c in enumerate(order))

def mark(order, who, start, target=F(4)):
    if target == 0: return start
    need=target
    for j,c in enumerate(order):
        left=max(start,F(50*j)); right=F(50*(j+1))
        if left>=right: continue
        amount=val(order,who,left,right)
        if amount>=need and amount>0: return left + need/F(V[who][c],50)
        need-=amount
    raise AssertionError('No mark available')

def game(order):
    people=list('ABC'); start=F(0); pieces={}; rounds=[]
    for _ in range(2):
        marks={p:mark(order,p,start) for p in people}
        winner=min(marks,key=marks.get)
        assert list(marks.values()).count(marks[winner])==1
        end=marks[winner]; pieces[winner]=(start,end)
        rounds.append((marks,winner,end)); start=end; people.remove(winner)
    pieces[people[0]]=(start,F(150))
    scores={p:tuple(val(order,p,*pieces[q]) for q in 'ABC') for p in 'ABC'}
    assert all(scores[p]['ABC'.index(p)]>=4 for p in people+list(pieces))
    envy=[p+' to '+q for p in 'ABC' for q in 'ABC' if scores[p]['ABC'.index(q)]>scores[p]['ABC'.index(p)]]
    assert envy
    return rounds, pieces, scores, envy, people[0]


def fmt(v):
    v=F(v)
    if v.denominator==1: return str(v.numerator)
    if v.denominator in (2,4): return str(float(v))
    return str(v)


def tables():
    lines=['% Generated and rechecked by check_guide.py; do not edit by hand.']
    for name, rows in [('ktable',K1),('ksecond',K2),('msecond',M2),('utable',U1)]:
        lines += ['\\newcommand{\\'+name+'}{%', '\\begin{tabular}{@{}rll@{}}', '\\textbf{Row} & \\textbf{Train with minimum cuts} & \\textbf{Fewest}\\\\\\midrule']
        for i,row in enumerate(rows,1):
            n,ans=allocations(row)
            witness=bar(row,ans[0]) if ans else row
            lines.append(f'{i} & \\texttt{{{witness}}} & '+('impossible' if n is None else str(n))+r'\\')
        lines += [r'\end{tabular}}']
    lines += [r'\newcommand{\allfour}{%',r'\begin{tabular}{@{}lll@{}}',r'\textbf{Train} & \textbf{Cuts} & \textbf{Fewest}\\\midrule']
    for row in sorted(all_orders(2,2)):
        n,ans=allocations(row)
        lines.append(r'\texttt{'+row+r'} & \texttt{'+bar(row,ans[0])+'} & '+str(n)+r'\\')
    lines += [r'\end{tabular}}']
    lines += [r'\newcommand{\gametable}{%',r'\begin{tabular}{@{}lllll@{}}',r'\textbf{Order} & \textbf{First marks A B C} & \textbf{First taker} & \textbf{Second marks} & \textbf{Second taker}\\\midrule']
    for order in ['XYZ','XZY','YXZ','YZX','ZXY','ZYX']:
        rd,pcs,sc,en,last=game(order)
        a,w,e=rd[0]; b,w2,e2=rd[1]
        lines.append(' '.join(order)+' & '+', '.join(fmt(a[p]) for p in 'ABC')+' & '+w+' at '+fmt(e)+' & '+', '.join(p+': '+fmt(b[p]) for p in sorted(b))+' & '+w2+' at '+fmt(e2)+r'\\')
    lines += [r'\end{tabular}}', r'\newcommand{\scoretable}{%',r'\begin{tabular}{@{}lllll@{}}',r'\textbf{Order} & \textbf{A sees A B C} & \textbf{B sees A B C} & \textbf{C sees A B C} & \textbf{Envy}\\\midrule']
    for order in ['XYZ','XZY','YXZ','YZX','ZXY','ZYX']:
        rd,pcs,sc,en,last=game(order)
        lines.append(' '.join(order)+' & '+' & '.join(', '.join(fmt(v) for v in sc[p]) for p in 'ABC')+' & '+', '.join(en)+r'\\')
    lines += [r'\end{tabular}}']
    return '\n'.join(lines)+'\n'


def main():
    root=students()
    for f,(digest,pages) in FILES.items():
        assert hashlib.sha256((root/f).read_bytes()).hexdigest()==digest, f+' changed; inspect and rederive'
        txt=subprocess.check_output(['pdftotext','-layout',str(root/f),'-'],text=True)
        pp=txt.split('\f'); pp=[p for p in pp if p.strip()]
        assert len(pp)==max(pages)
        for n,p in enumerate(pages,1): assert f'Problem {n}:' in pp[p-1], (f,n,p)
    assert [allocations(x)[0] for x in K1]==[1,2,1,2,1,1]
    assert [allocations(x)[0] for x in K2]==[2,1,None,1,2,1,2]
    assert [allocations(x)[0] for x in M2]==[2,2,1,2,None,2,1]
    assert allocations('RRBRRRBBBR')[1]==[(2,7),(3,8)]
    assert [allocations(x)[0] for x in U1]==[2,1,2,2,1,2]
    assert all(len(allocations(x)[1])==1 for x in K1+U1)
    assert all(len(allocations(x)[1])==1 for x in M2 if x not in ['RRBRRRBBBR','RBRRBRB'])
    assert [comb(4,r)*comb(4,4-r) for r in [0,1,3,4]]==[1,16,16,1]
    assert comb(4,2)**2==36 and comb(8,4)==70
    assert comb(5,3)==10
    assert 3*8==24 and F(24,3)==8 and 4<F(24,3)
    four=Counter(allocations(x)[0] for x in all_orders(4,4))
    assert four=={1:36,2:34}
    for row in all_orders(4,4):
        assert (allocations(row)[0]==1)==(row[:4].count('R')==2)
    # Every nonempty available K1 train, including odd counts.
    count=Counter()
    for r in range(7):
        for b in range(5):
            if r+b:
                for row in all_orders(r,b): count[allocations(row)[0]]+=1
    assert count=={None:441,1:179,2:170}, count
    # Independent window scan of every binary word at even lengths through 14.
    cases=0
    for n in range(2,15,2):
        for bits in product('RB',repeat=n):
            row=''.join(bits); nr=row.count('R')
            if nr%2: continue
            assert any(row[i:i+n//2].count('R')==nr//2 for i in range(n//2+1))
            cases+=1
    assert cases==10922
    # Exact colour-fraction system: subtract rows to get r=b; sum to get 1/2.
    r=b=F(1,2)
    assert 3*r+b==r+3*b==2
    assert F(80,120)*3==2 and 1+F(40,120)*3==2
    assert F(60,120)*3+F(60,120)==2
    assert F(40,120)*3==1
    # Three-person system, determinant and exact unique solution.
    matrix=[[4,8,0],[0,4,8],[8,0,4]]
    det=4*(4*4)-8*(-8*8)
    assert det==576
    assert all(sum(F(x,2) for x in row)==6 for row in matrix)
    # Half-card point in all 120 labelled orders, not only 10 colour words.
    goods=['R1','R2','R3','B1','B2']; half=F(11,2)
    for order in permutations(goods):
        running=F(0)
        for c in order:
            value=3 if c[0]=='R' else 1
            if running<half<running+value:
                assert c[0]=='R'; break
            assert running!=half
            running+=value
        else: raise AssertionError(order)
    assert F(25)*2+F(25,2)==F(125,2)
    assert F(1)+F(1,2)*3+F(3)==half
    assert F(2,3)*2>1 and F(2,3)*3==2
    assert F(25)*F(2,3)==F(50,3) and 25+F(25,3)==F(100,3)
    # Launch: matching counts in different orders; separate non-task grey panel.
    assert 'RBR'.count('R')=='BRR'.count('R')==2
    assert F(15,30)*6==3 and F(25,50)*8==4 and F(25,100)*8==2
    for order in ['XYZ','XZY','YXZ','YZX','ZXY','ZYX']:
        rd,pcs,sc,en,last=game(order)
        assert sc[rd[0][1]]['ABC'.index(rd[0][1])]==4
        assert sc[rd[1][1]]['ABC'.index(rd[1][1])]==4
        assert sc[last]['ABC'.index(last)]==(11 if order in ['XYZ','YZX','ZXY'] else 8)
    out=tables(); target=HERE/'checked-tables.tex'
    if '--write-tables' in sys.argv: target.write_text(out)
    else: assert target.read_text()==out, 'Regenerate checked-tables.tex'
    print('PASS: final student hashes/pages; every printed train by exhaustive allocations;')
    print('70 four-red/four-blue orders; all 790 available K1 trains; 10,922 even-count trains through 14;')
    print('exact strip/panel algebra; all 6 games including every mark and envy comparison;')
    print('120 labelled five-card orders; card bound and non-task launch; generated tables match.')
    print('Student PDFs:',root)

if __name__=='__main__': main()
