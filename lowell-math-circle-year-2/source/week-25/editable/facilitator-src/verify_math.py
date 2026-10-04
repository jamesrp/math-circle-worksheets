#!/usr/bin/env python3
"""Independent finite checks. No imports from the student builder or answer files.
Run with Python 3.9+: python verify_math.py [--output verification.json]
Rows are tuples of 0/1 entries. Labels remain fixed; no symmetry quotient.
"""
from itertools import combinations, product
from collections import defaultdict, deque
from pathlib import Path
import argparse, hashlib, json
from math import comb

def picture(s): return tuple(tuple(map(int, row)) for row in s.split('/'))
def code(a): return '/'.join(''.join(map(str,row)) for row in a)
def margins(a): return (tuple(map(sum,a)),tuple(map(sum,zip(*a))))
def solutions(rows, cols):
    options=[]
    for n in rows:
        opts=[]
        for inds in combinations(range(len(cols)),n):
            occupied=set(inds);opts.append(tuple(int(i in occupied) for i in range(len(cols))))
        options.append(opts)
    return sorted(a for a in product(*options) if margins(a)[1]==tuple(cols))
def switches(a):
    r,c=len(a),len(a[0]);out=[]
    for i,j in combinations(range(r),2):
        for k,l in combinations(range(c),2):
            if a[i][k]==a[j][l] and a[i][l]==a[j][k] and a[i][k]!=a[i][l]:
                b=[list(row) for row in a]
                for x,y in [(i,k),(i,l),(j,k),(j,l)]:b[x][y]=1-b[x][y]
                b=tuple(map(tuple,b)); assert margins(b)==margins(a)
                out.append(((i,j,k,l),b))
    return out

def distances(a):
    d={a:0};q=deque([a])
    while q:
        x=q.popleft()
        for _,y in switches(x):
            if y not in d:d[y]=d[x]+1;q.append(y)
    return d

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='verification.json');args=ap.parse_args()
    cases=[('K1 P1 top',[1,1],[1,1],2),('K1 P1 middle',[1,1],[1,0,1],2),
      ('K1 P1 bottom; K1 P2 right; 23 P1 top',[2,1],[1,1,1],3),('K1 P2 left',[1,2],[1,1,1],3),
      ('K1 P3',[1,1,1],[1,1,1],6),('K1 P4 first; 23 P1 middle',[3,1],[2,1,1],1),
      ('K1 P4 second; 23 P3 top left',[2,1,0],[2,1,0],1),('K1 P4 last; 23 P2',[2,1,1],[2,1,1],5),
      ('23 P1 bottom',[2,2],[2,1,1],2),('23 P3 nonadjacent',[1,0,1],[1,0,1],2),
      ('23 P4; 45 P1 and P2',[2,2],[1,1,1,1],6),('45 P3',[3,3],[1,1,1,1,1,1],20),
      ('45 P4',[3,3],[2,1,0,1,1,1],6)]
    result={'method':'Independent row-subset reconstruction and breadth-first search. No student answer file or student builder imported.','fixed_cases':[]}
    for label,rows,cols,n in cases:
        ss=solutions(rows,cols);assert len(ss)==n
        result['fixed_cases'].append(dict(label=label,rows=rows,columns=cols,count=n,pictures=[code(a) for a in ss]))
    printed=['110/100/000','100/000/001','110/001/100','111/110/100']
    result['23_P3_switches']=[]
    for s,n in zip(printed,[0,1,3,0]):
        sw=switches(picture(s));assert len(sw)==n
        result['23_P3_switches'].append(dict(start=s,count=n,moves=[dict(rows=[chr(65+x[0]),chr(65+x[1])],columns=[x[2]+1,x[3]+1],result=code(b)) for x,b in sw]))
    paths=[['1100/0011','0110/1001','0011/1100'],
           ['111000/000111','011100/100011','001110/110001','000111/111000'],
           ['110100/100011','100110/110001','100011/110100']]
    result['shortest_routes']=[]
    for route in paths:
        aa=list(map(picture,route));assert len(route)-1==distances(aa[0])[aa[-1]]
        for a,b in zip(aa,aa[1:]):assert b in [t for _,t in switches(a)]
        result['shortest_routes'].append(dict(route=route,distance=len(route)-1))
    one=distances(picture('1100/0011'));assert sorted(one.values())==[0,1,1,1,1,2]
    result['23_P4_distance_distribution']={str(i):list(one.values()).count(i) for i in range(3)}
    result['construction_examples']=[]
    for s,n in [('111/100',1),('110/101',2),('111/100/000',1),('110/001/100',5)]:
        a=picture(s);rr,cc=margins(a);ss=solutions(rr,cc);assert len(ss)==n and sum(rr)==4
        result['construction_examples'].append(dict(picture=s,rows=rr,columns=cc,count=n))
    result['all_four_counter_constructions']={}
    for r,c in [(2,3),(3,3)]:
        groups=defaultdict(list)
        for ones in combinations(range(r*c),4):
            cells=set(ones);a=tuple(tuple(int(i*c+j in cells) for j in range(c)) for i in range(r));groups[margins(a)].append(a)
        unique=sum(len(v)==1 for v in groups.values());ambiguous=sum(len(v)>1 for v in groups.values())
        assert (unique,ambiguous)==((9,3) if r==2 else (45,27))
        result['all_four_counter_constructions'][f'{r}x{c}']=dict(pictures=sum(map(len,groups.values())),unique_margin_sets=unique,ambiguous_margin_sets=ambiguous)
    # Verify uniqueness criterion for every binary board of the listed sizes;
    # verify all-pairs two-row distance via BFS, independently of the formula.
    result['exhaustive_checks']=[]
    for r,c in [(2,4),(2,6),(3,3)]:
        groups=defaultdict(list)
        for n in range(1<<(r*c)):
            a=tuple(tuple((n>>(i*c+j))&1 for j in range(c)) for i in range(r));groups[margins(a)].append(a)
        comparisons=0
        for aa in groups.values():
            for a in aa:
                assert (not switches(a))==(len(aa)==1)
                if r==2:
                    dd=distances(a);assert len(dd)==len(aa)
                    rr,cc=margins(a);s=cc.count(1);k=rr[0]-cc.count(2)
                    assert len(aa)==comb(s,k)
                    assert max(dd.values())==min(k,s-k)
                    for b in aa:
                        exact=sum(x==1 and y==0 for x,y in zip(a[0],b[0]));assert dd[b]==exact;comparisons+=1
        result['exhaustive_checks'].append(dict(shape=f'{r}x{c}',boards=1<<(r*c),margin_sets=len(groups),uniqueness_criterion=True,two_row_ordered_pairs_checked=comparisons))
    for rows,cols in [([2,2],[1,1,1,1]),([3,3],[2,1,0,1,1,1])]:
        aa=solutions(rows,cols);assert max(max(distances(a).values()) for a in aa)==2
    # Small three-row caution: equal top rows need not make distance zero.
    a=picture('100/010/001');b=picture('100/001/010');assert a[0]==b[0] and distances(a)[b]==1
    root=Path(__file__).resolve().parent.parent
    result['student_pdf_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (root/'reference-pdfs').glob('*.pdf') if p.name!='facilitator-guide.pdf'}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: 13 fixed reconstruction cases; all printed switches; shortest routes; four-counter constructions; 4864 binary boards; all two-row pairs.')
if __name__=='__main__':main()
