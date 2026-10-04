"""Independent check: explicit profiles transcribed from final student pages.
Does not import the student builder or its solution/enumeration code.
Run from any directory. Writes portable audit JSON beside this file.
"""
from itertools import permutations, product
from pathlib import Path
from functools import lru_cache
from collections import Counter
import json, hashlib
ROOT=Path(__file__).resolve().parent
PROFILES={
 'mutual':('XY YX','AB BA'),
 'shared':('XY XY','AB AB'),
 'two':('XY YX','BA AB'),
 'cross':('YX XY','BA AB'),
 'one_blocker':('YX YX','AB AB'),
 'unique3':('XYZ XZY YXZ','CBA ACB BAC'),
 'three3':('ZXY YXZ XYZ','BAC ACB CBA'),
 'four4':('WXYZ XWZY YZWX ZYXW','BACD ABDC DCAB CDBA'),
 'older4':('XWZY XYWZ XYZW XYWZ','BCDA DBAC BCAD BDAC'),
 'construct2':('XYZ YXZ ZXY','BAC ABC CAB'),
 'keep_first':('XYZ XYZ ZXY','BAC ABC CAB'),
 'last3':('XYZ YXZ ZXY','BCA ACB ABC'),
}
def parse(raw):
 a,b=map(str.split,raw);n=len(a)
 left='ABCD'[:n];right='XY' if n==2 else ('XYZ' if n==3 else 'WXYZ')
 L=dict(zip(left,a));R=dict(zip(right,b))
 assert all(set(v)==set(right) and len(v)==n for v in L.values())
 assert all(set(v)==set(left) and len(v)==n for v in R.values())
 return L,R

def candidates(L,R):return [dict(zip(L,p)) for p in permutations(R)]
def blocking(L,R,m):
 # Enumerate desired edges with strict mutual improvement, independently using ranks.
 partner={r:l for l,r in m.items()}
 rank={a:{b:i for i,b in enumerate(s)} for a,s in (L|R).items()}
 return [a+b for a in L for b in R if m[a]!=b and rank[a][b]<rank[a][m[a]] and rank[b][a]<rank[b][partner[b]]]
def code(m):return '/'.join(a+b for a,b in sorted(m.items()))
def enum(L,R):return [{'matching':code(m),'blockers':blocking(L,R,m)} for m in candidates(L,R)]
def schedules(L,R,keep_first=False):
 # Explore every free-proposer choice, retaining terminal matching and total count.
 left=tuple(L);right=tuple(R)
 @lru_cache(None)
 def visit(held,used):
  if -1 not in held:return {(tuple(held),sum(used))}
  result=set()
  for p in range(len(left)):
   if p in held:continue
   assert used[p]<len(right),'A free proposer exhausted its list'
   r=right.index(L[left[p]][used[p]]);old=held[r]
   u=list(used);u[p]+=1;h=list(held)
   if old<0 or (not keep_first and R[right[r]].index(left[p])<R[right[r]].index(left[old])):h[r]=p
   result.update(visit(tuple(h),tuple(u)))
  return result
 terms=visit(tuple([-1]*len(left)),tuple([0]*len(left)))
 return [{'matching':code({left[p]:right[r] for r,p in enumerate(h)}),'requests':n} for h,n in sorted(terms)]

def run():
 out={'method':'Independent explicit transcription and exhaustive candidate/blocking-edge enumeration.'}
 for key,raw in PROFILES.items():
  L,R=parse(raw);rows=enum(L,R)
  out[key]={'left':L,'right':R,'candidates':rows,'stable':[r['matching'] for r in rows if not r['blockers']]}
 expected={'mutual':['AX/BY'],'shared':['AX/BY'],'two':['AX/BY','AY/BX'],'cross':['AY/BX'],'one_blocker':['AY/BX'],'unique3':['AY/BZ/CX'],'three3':['AY/BX/CZ','AZ/BX/CY','AZ/BY/CX'],'four4':['AW/BX/CY/DZ','AW/BX/CZ/DY','AX/BW/CY/DZ','AX/BW/CZ/DY'],'older4':['AW/BY/CZ/DX','AZ/BY/CW/DX'],'construct2':['AX/BY/CZ','AY/BX/CZ']}
 for key,want in expected.items():assert out[key]['stable']==want,(key,out[key]['stable'])
 for key in ['one_blocker','cross']:
  L,R=parse(PROFILES[key]);tests={}
  for who in L|R:
   l=L.copy();r=R.copy();target=l if who in l else r;target[who]=target[who][::-1]
   tests[who]=blocking(l,r,{'A':'X','B':'Y'})
  out[key]['single_strip_tests']=tests
 assert [k for k,v in out['one_blocker']['single_strip_tests'].items() if not v]==['A','Y']
 assert all(out['cross']['single_strip_tests'].values())
 # K-1 Problem 4: test each possible blank Y strip without changing other strips.
 out['blank_Y_tests']={}
 for name,raw in [('top',('XY YX','BA AB')),('bottom',('XY XY','BA AB'))]:
  L,R=parse(raw); tests={}
  for y in ['AB','BA']:
   R['Y']=y; tests[y]=[q['matching'] for q in enum(L,R) if not q['blockers']]
  out['blank_Y_tests'][name]=tests
 assert out['blank_Y_tests']['top']['AB']==['AX/BY','AY/BX']
 assert len(out['blank_Y_tests']['top']['BA'])==1
 assert all(v!=['AX/BY','AY/BX'] for v in out['blank_Y_tests']['bottom'].values())
 two_profiles=[]
 for v in product(('XY','YX'),('XY','YX'),('AB','BA'),('AB','BA')):
  L,R=parse((' '.join(v[:2]),' '.join(v[2:])));stable=[q['matching'] for q in enum(L,R) if not q['blockers']]
  two_profiles.append({'A':v[0],'B':v[1],'X':v[2],'Y':v[3],'stable':stable})
 out['all_16_two_pair_profiles']=two_profiles
 assert sum(t['stable']==['AX/BY'] for t in two_profiles)==7
 assert sum(len(t['stable'])==2 for t in two_profiles)==2
 L,R=parse(PROFILES['older4']);out['older4']['left_schedules']=schedules(L,R);out['older4']['right_schedules']=schedules(R,L)
 assert out['older4']['left_schedules']==[{'matching':'AW/BY/CZ/DX','requests':8}]
 assert out['older4']['right_schedules']==[{'matching':'WC/XD/YB/ZA','requests':7}]
 def trace(L,R,requests,keep_first=False):
  held={};used={a:[] for a in L};log=[]
  for a,r in requests:
   assert a not in held.values(),(a,'not free')
   assert r==L[a][len(used[a])],(a,r,'not highest untried')
   used[a].append(r);old=held.get(r)
   if old is None or (not keep_first and R[r].index(a)<R[r].index(old)):held[r]=a
   log.append({'request':a+r,'kept':held[r],'released':old if held[r]==a else a})
  assert len(held)==len(L)
  return {'matching':code({a:r for r,a in held.items()}),'log':log}
 L,R=parse(PROFILES['older4'])
 out['older4']['left_sample_trace']=trace(L,R,['AX','BX','AW','CX','CY','DX','BY','CZ'])
 out['older4']['right_sample_trace']=trace(R,L,['WB','XD','YB','WC','ZB','ZD','ZA'])
 assert out['older4']['left_sample_trace']['matching']=='AW/BY/CZ/DX'
 assert out['older4']['right_sample_trace']['matching']=='WC/XD/YB/ZA'
 L,R=parse(PROFILES['keep_first']);out['keep_first']['sample_trace']=trace(L,R,['AX','BX','BY','CZ'],True)
 assert out['keep_first']['sample_trace']['matching']=='AX/BY/CZ'
 L,R=parse(PROFILES['keep_first']);bad={'A':'X','B':'Y','C':'Z'}
 assert blocking(L,R,bad)==['BX']
 out['keep_first']['chosen_bad_result']={'matching':code(bad),'blockers':blocking(L,R,bad)}
 L,R=parse(PROFILES['last3']);m={'A':'X','B':'Y','C':'Z'}
 assert not blocking(L,R,m)
 def last_count(L,R,m):
  inv={r:a for a,r in m.items()}
  return sum(L[a][-1]==m[a] for a in L)+sum(R[r][-1]==inv[r] for r in R)
 assert last_count(L,R,m)==3
 # Independent full 46,656-profile, 279,936-candidate check, no fixed-matching reduction.
 maxlast=0;hist=Counter();stable_count=0
 lp=list(permutations('XYZ'));rp=list(permutations('ABC'))
 for ls in product(lp,repeat=3):
  L=dict(zip('ABC',ls))
  for rs in product(rp,repeat=3):
   R=dict(zip('XYZ',rs));cnt=0
   for m in candidates(L,R):
    if not blocking(L,R,m):
     cnt+=1;stable_count+=1;maxlast=max(maxlast,last_count(L,R,m))
   assert cnt>0
   hist[cnt]+=1
 assert maxlast==3
 out['full_three_pair_audit']={'profiles':46656,'candidate_matchings_tested':279936,'stable_matchings_total':stable_count,'histogram_stable_count':dict(sorted(hist.items())),'maximum_last_choices':maxlast}
 out['student_pdf_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT.parent/'reference-pdfs').glob('*.pdf') if p.name!='facilitator-guide.pdf'}
 (ROOT/'math-checks.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'stable_counts':{k:len(out[k]['stable']) for k in PROFILES},'single_strip':{k:out[k]['single_strip_tests'] for k in ['one_blocker','cross']},'three_pair_audit':out['full_three_pair_audit']},indent=2))
if __name__=='__main__':run()
