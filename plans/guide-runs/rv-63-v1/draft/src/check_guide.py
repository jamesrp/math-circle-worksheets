#!/usr/bin/env python3
"""Independent finite checks for the final Week 63 return-visit guide.

The board coordinates and printed rows below were transcribed from final PDFs,
not imported from the student generator or its verifier. SHA-256 pins that visual
transcription. Standard-library Python plus Poppler pdftotext; no repo imports.
"""
from collections import Counter, deque
from itertools import combinations, permutations
from math import comb, factorial
from pathlib import Path
import hashlib, json, re, subprocess

HERE = Path(__file__).resolve().parent
FILES = ('k-1.pdf', 'grades-2-3.pdf', 'grades-4-5.pdf')

def student_dir():
    if all((HERE.parent/f).is_file() for f in FILES):
        return HERE.parent
    for ancestor in HERE.parents:
        candidate = ancestor/'plans'/'return-visit-drafts'/'week-63'
        if all((candidate/f).is_file() for f in FILES):
            return candidate
    raise SystemExit('Put k-1.pdf, grades-2-3.pdf and grades-4-5.pdf beside src/.')

def text_pages(path):
    text = subprocess.check_output(['pdftotext', '-layout', str(path), '-'], text=True)
    return [p for p in text.split('\f') if p.strip()]

def swap(row, pair):
    s=list(row); a,b=(s.index(x) for x in pair); s[a],s[b]=s[b],s[a]
    return ''.join(s)

def run(row, pairs):
    for pair in pairs.split(): row=swap(row,pair)
    return row

def loops(row):
    letters=sorted(row); dest={x:letters[row.index(x)] for x in letters}
    remaining=set(letters); result=[]
    while remaining:
        x=min(remaining); cycle=[]
        while x in remaining:
            cycle.append(x); remaining.remove(x); x=dest[x]
        result.append(''.join(cycle))
    return result

def bfs(n):
    home='ABCDE'[:n]; dist={home:0}; q=deque([home]); pairs=list(combinations(home,2))
    while q:
        r=q.popleft()
        for pair in pairs:
            t=swap(r,pair)
            if t not in dist: dist[t]=dist[r]+1; q.append(t)
    return dist

def allrows(n): return [''.join(p) for p in permutations('ABCDE'[:n])]
def matches(r): return sum(a==b for a,b in zip(r,sorted(r)))
def forbidden(mapping): return {(c,h) for h,cards in mapping.items() for c in cards}
def strip(n):
    L='ABCDE'[:n]
    return {(L[i],L[i])for i in range(n)}|{(L[i],L[i+1])for i in range(n-1)}
def ring(n): return strip(n)|{('ABCDE'[n-1],'A')}
def obey(n,B):
    return [r for r in allrows(n) if all((c,h) not in B for h,c in zip('ABCDE'[:n],r))]
def rook(n,B):
    B=sorted(B)
    return [sum(len({c for c,h in S})==k==len({h for c,h in S}) for S in combinations(B,k)) for k in range(n+1)]
def alternating(n,R): return sum((-1)**k*r*factorial(n-k) for k,r in enumerate(R))

def main():
    root=student_dir(); manifest=json.loads((HERE/'student-manifest.json').read_text())
    page_problems={
      'k-1.pdf':[[1],[2,3],[4],[5,6],[7,8]],
      'grades-2-3.pdf':[[1],[2,3],[4,5],[6,7],[8],[9]],
      'grades-4-5.pdf':[[1],[2],[3],[4,5],[6,7],[8,9],[10],[11],[12],[13]]}
    for f in FILES:
        assert hashlib.sha256((root/f).read_bytes()).hexdigest()==manifest[f], f+' changed; re-inspect diagrams'
        pp=text_pages(root/f)
        assert [list(map(int,re.findall(r'Problem (\d+):',p))) for p in pp]==page_problems[f]
    assert run('VUWX','VX')=='XUWV'
    assert loops('WUVXY')==['UVW','X','Y']
    assert {(c,h) for h,c in zip('UVWX','VXUW')}=={('V','U'),('X','V'),('U','W'),('W','X')}
    assert not ({(c,h) for h,c in zip('UVWX','VXUW')}&{('U','V'),('W','W'),('X','U')})
    d={n:bfs(n) for n in (2,3,4,5)}
    for n,dist in d.items():
        assert len(dist)==factorial(n)
        assert all(v==n-len(loops(r)) for r,v in dist.items())
        # Independently exhaust exact-length paths, including deliberate detours.
        reachable={'ABCDE'[:n]}
        for m in range(8):
            assert reachable=={r for r,v in dist.items() if v<=m and (m-v)%2==0}
            reachable={swap(r,p) for r in reachable for p in combinations('ABCDE'[:n],2)}
    assert [min(v for r,v in d[n].items() if matches(r)==0)for n in (3,4,5)]==[2,2,3]
    assert sorted(r for r,v in d[3].items() if matches(r)==0 and v==2)==['BCA','CAB']
    assert sorted(r for r,v in d[4].items() if matches(r)==0 and v==2)==['BADC','CDAB','DCBA']
    assert run('ABCDE','AB CD AE')=='BEDCA'
    assert run('ABC','AB AC')=='BCA'
    assert sum([5,5,20,2,18,5,5])==60
    expected_rows={'CBA':1,'BCA':2,'BADC':2,'BCDA':3,'CBAD':1,'BCAD':2,'DCBA':2,'ACDB':2,'CDBA':3,
                   'EBCDA':1,'BCADE':2,'BADEC':3,'BCAED':3,'BCDEA':4,'DEABC':4}
    for r,v in expected_rows.items(): assert d[len(r)][r]==v
    witnesses={'CBA':'AC','BCA':'AB BC','BADC':'AB CD','BCDA':'AB BC CD',
      'CBAD':'AC','BCAD':'AB BC','DCBA':'AD BC','ACDB':'BC CD','CDBA':'AC BD CD',
      'EBCDA':'AE','BCADE':'AB BC','BADEC':'AB CD DE','BCAED':'AB BC DE',
      'BCDEA':'AB BC CD DE','DEABC':'AD BE CD DE'}
    for r,moves in witnesses.items():
        assert run(r,moves)==''.join(sorted(r)),(r,moves,run(r,moves))
        assert len(moves.split())==d[len(r)][r]
    hardest4=['BCDA','BDAC','CADB','CDBA','DABC','DCAB']
    # Catalog is compared with independently generated graph distances below.
    actual5=sorted(r for r,v in d[5].items() if v==4)
    assert sorted(r for r,v in d[4].items() if v==3)==hardest4
    # Stored catalog generated in writer-data.json and printed verbatim in guide.
    data=json.loads((HERE/'writer-data.json').read_text())
    assert actual5==data['hardest5'] and len(actual5)==24
    assert sum(matches(r)==0 and v==3 for r,v in d[5].items())==20
    reciprocal=[]
    for r in ['BCDA','CDAB','BCAD','DBCA','DACB']:
        reciprocal.append([''.join(p)for p in combinations('ABCD',2) if matches(swap(r,p))-matches(r)==2])
    assert reciprocal==[[],['AC','BD'],[],['AD'],[]]
    assert loops('EBCDA')==['AE','B','C','D']
    assert loops('BCADE')==['ACB','D','E']
    assert loops('BADEC')==['AB','CED']
    assert loops('BCAED')==['ACB','DE']
    assert loops('BCDEA')==['AEDCB']
    assert loops('DEABC')==['ACEBD']
    for n, totals, per, pairs, piles in [(3,6,2,3,[2,3,0,1]),(4,24,6,12,[9,8,6,0,1]),(5,120,24,60,[44,45,20,10,0,1])]:
        rr=allrows(n); freq=Counter(matches(r)for r in rr)
        assert [freq[k]for k in range(n+1)]==piles
        assert sum(matches(r)for r in rr)==totals
        assert all(sum(r[i]=='ABCDE'[i]for r in rr)==per for i in range(n))
        assert sum(comb(matches(r),2)for r in rr)==pairs
        for k in range(n+1):
            small=sum(all(p[i]!=i for i in range(n-k))for p in permutations(range(n-k)))
            assert freq[k]==comb(n,k)*small
        assert piles[0]-piles[1]==(-1)**n
    assert [matches(r)for r in ['ABC','ACB','BAC','BCA','CAB','CBA']]==[3,1,1,0,0,1]
    assert obey(3,strip(3))==['BCA']
    assert obey(4,strip(4))==['BCDA','CDAB','DCAB']
    assert obey(4,forbidden({'A':'AB','B':'ABC','C':'BCD','D':'CD'}))==['CDAB']
    middle=[{'A':'A','B':'B','C':'C','D':'D'},{'A':'A','B':'AB','C':'C'},
            {'A':'AB','B':'AB'},{'A':'A','B':'A','C':'A','D':'A'}]
    assert [len(obey(4,forbidden(B)))for B in middle]==[9,7,4,0]
    assert obey(4,forbidden(middle[2]))==['CDAB','CDBA','DCAB','DCBA']
    assert len(obey(4,{('A','A'),('B','B'),('D','C'),('D','D')}))==8
    assert len(obey(4,{('A','A'),('B','B'),('D','A'),('D','B')}))==6
    sizes=Counter(); coeffs=set()
    for B in combinations([(c,h)for c in 'ABCD'for h in 'ABCD'],4):
        answer=len(obey(4,set(B))); sizes[answer]+=1
        assert (answer==9)==(len({c for c,h in B})==len({h for c,h in B})==4)
        R=rook(4,B); assert alternating(4,R)==answer; coeffs.add(tuple(R[2:]))
    assert dict(sorted(sizes.items()))=={0:8,4:324,6:384,7:576,8:504,9:24}
    assert coeffs=={(0,0,0),(2,0,0),(3,0,0),(4,0,0),(4,1,0),(5,2,0),(6,4,1)}
    assert sum(sizes.values())==comb(16,4)==1820
    for n,B,R,count,key in [(4,strip(4),[1,7,15,10,1],3,'strip4'),
      (4,ring(4),[1,8,20,16,2],2,'ring4'),(5,strip(5),[1,9,28,35,15,1],16,'strip5'),
      (5,ring(5),[1,10,35,50,25,2],13,'ring5')]:
        assert rook(n,B)==R and alternating(n,R)==count
        def chain(L,k):
            if k==0: return 1
            if k<0 or L<=0: return 0
            if L==1: return int(k==1)
            return chain(L-1,k)+chain(L-2,k-1)
        by_chain=[chain(2*n-1,k) for k in range(n+1)] if 'strip' in key else [1]+[chain(2*n-1,k)+chain(2*n-3,k-1) for k in range(1,n+1)]
        assert by_chain==R
        assert obey(n,B)==data[key] and len(data[key])==count
    assert sorted(set(data['strip5'])-set(data['ring5']))==['ECDAB','ECDBA','EDABC']
    assert [sum(r[0]==c for r in data['strip5'])for c in 'ABCDE']==[0,4,5,4,3]
    guide=HERE.parent/'facilitator.pdf'
    if guide.exists():
        pp=text_pages(guide); assert len(pp)==8, len(pp)
        assert all('W63-RV-FAC-v1' in p and 'Adult return-visit guide' in p for p in pp)
        # Confirm the complete catalogs are actually present in the delivered PDF.
        section=pp[4].split('Problem 4, student page 4')[1].split('Problem 5, student page 4')[0]
        assert re.findall(r'\b[A-E]{5}\b',section)==data['hardest5']
        section=pp[6].split('Problem 10, student page 7')[1].split('Problem 11, student page 8')[0]
        assert re.findall(r'\b[A-E]{5}\b',section)==data['strip5']
        section=pp[6].split('Problem 11, student page 8')[1].split('Problem 12, student page 9')[0]
        assert re.findall(r'\b[A-E]{5}\b',section)==['ECDAB','ECDBA','EDABC']+data['ring5']
    print('PASS: final student PDF hashes and all 21 page/problem mappings; all 152 permutation states; exact lengths 0..7; every displayed row, swap, loop, tally, pile, complete catalog and rook sum; all 1820 four-spot boards.')
    print('Student directory:',root)
    print('Four-spot distribution:',dict(sorted(sizes.items())))
    print('Five-card hardest rows:', ' '.join(actual5))
    print('Guide pages:',len(text_pages(guide)) if guide.exists() else 'not yet built')

if __name__=='__main__': main()
