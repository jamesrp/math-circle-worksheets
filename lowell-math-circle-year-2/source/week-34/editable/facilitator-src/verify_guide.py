"""Independent finite verification for the adult guides. No student builders imported."""
import itertools as it,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def symmetry_keys():
 def maps(n):
  return [tuple((i+k)%n for i in range(n)) for k in range(1,n)]+[tuple((k-i)%n for i in range(n)) for k in range(n)]
 def good(w):return not any(all(w[i]==w[p[i]] for i in range(len(w))) for p in maps(len(w)))
 counts={n:sum(good(w) for w in it.product('AB',repeat=n)) for n in range(3,11)}
 assert list(counts.values())==[0,0,0,12,28,96,252,600]
 for w in ['ABC','ABCC','ABCCC','AABABB','AABABBBB','AABBABBB','ABBC']:assert good(w),w
 assert not good('ABAC')
 w,v='AABABBBB','AABBABBB'
 assert not any(all(w[i]==v[p[i]] for i in range(8)) for p in maps(8)+[tuple(range(8))])
 minority={n:min(min(w.count('A'),w.count('B')) for w in it.product('AB',repeat=n) if good(w)) for n in range(6,11)}
 assert all(x==3 for x in minority.values())
 return {'binary_distinguishing_words':counts,'minimum_minority':minority,'witnesses_and_edits_pass':True}

def border_keys():
 # Polygon vertices in units of 0.05 cm; edge-word isometry condition.
 V=[(-26,-22),(26,-22),(26,-8),(16,-8),(16,-13),(-10,-13),(-10,0),(12,0),(12,9),(-10,9),(-10,22),(-26,22)]
 E=[(V[(i+1)%12][0]-V[i][0])**2+(V[(i+1)%12][1]-V[i][1])**2 for i in range(12)]
 autos=[]
 for s in [1,-1]:
  for k in range(12):
   p=[(s*i+k)%12 for i in range(12)]
   if all(sum((V[i][d]-V[j][d])**2 for d in (0,1))==sum((V[p[i]][d]-V[p[j]][d])**2 for d in (0,1)) for i,j in it.combinations(range(12),2)):autos.append((s,k))
 assert autos==[(1,0)]
 # Anchor positions in half-centimeters; orientations are sign pairs.
 configs={'T':(12,[(0,3,1,1)]),'G':(12,[(0,3,1,1),(6,-3,1,-1)]),'H':(12,[(0,3,1,1),(0,-3,1,-1)]),'R':(12,[(0,3,1,1),(6,-3,-1,-1)]),'E':(12,[(3,3,1,1),(9,3,-1,1),(3,-3,1,-1),(9,-3,-1,-1)])}
 out={}
 for name,(P,pts) in configs.items():
  S=set(pts);result={}
  for a,b in it.product([1,-1],repeat=2):
   # Any symmetry must send a listed anchor to another, determining displacement.
   ds={(u[0]-a*v[0])%P for u in S for v in S}
   good=[]
   for d in sorted(ds):
    if {((a*x+d)%P,b*y,a*ox,b*oy) for x,y,ox,oy in S}==S:good.append(d/2)
   result[str((a,b))]=good
  out[name]=result
 assert out['G']=={'(1, 1)':[0.0],'(1, -1)':[3.0],'(-1, 1)':[],'(-1, -1)':[]}
 assert out['R']['(-1, -1)']==[3.0] and out['R']['(1, -1)']==[] and out['R']['(-1, 1)']==[]
 assert out['H']['(-1, -1)']==[]
 assert out['E']['(-1, 1)']==[0.0] and out['E']['(-1, -1)']==[0.0]
 S={1,12}; P=24
 assert {(x+12)%P for x in S}!=S
 assert min(t for t in range(1,P+1) if {(x+t)%P for x in S}==S)==24
 return {'motif_isometries':autos,'shifts_modulo_period_cm':out,'larger_repeat_edit_primitive_period_cm':12}

def affine_keys():
 V=list(it.product(range(3),repeat=2))
 def triple(q):return all(len({p[d] for p in q}) in [1,3] for d in (0,1))
 lines=[frozenset(q) for q in it.combinations(V,3) if triple(q)]
 def legal(q):return not any(L<=set(q) for L in lines)
 assert len(lines)==12
 for a,b in it.combinations(V,2):
  rest=[c for c in V if c not in (a,b) and triple((a,b,c))]
  assert rest==[tuple((-a[d]-b[d])%3 for d in (0,1))]
 pairs=[((0,0),(0,1)),((0,0),(1,0)),((0,1),(1,2)),((1,1),(2,0))]
 assert [tuple((-a[d]-b[d])%3 for d in (0,1)) for a,b in pairs]==[(0,2),(2,0),(2,0),(0,2)]
 counts={};ext={}
 for k in range(6):
  caps=[frozenset(q) for q in it.combinations(V,k) if legal(q)];counts[k]=len(caps)
  ext[k]=sorted({sum(legal(C|{v}) for v in V if v not in C) for C in caps})
 assert list(counts.values())==[1,9,36,72,54,0]
 assert ext=={0:[9],1:[8],2:[6],3:[3],4:[0],5:[]}
 partitions=[p for p in it.combinations(lines,3) if len(set.union(*(set(q) for q in p)))==9]
 assert len(partitions)==4
 assert {len(a&b) for a,b in it.combinations(lines,2)}=={0,1}
 assert all(sum(v in l for l in lines)==4 for v in V)
 return {'lines':len(lines),'cap_counts':counts,'legal_extensions':ext,'partitions':[[sorted(q) for q in p] for p in partitions],'youngest_readiness_test_performed':False}

def tetra_keys():
 V=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
 def det(u,v,w):return sum(u[i]*(v[(i+1)%3]*w[(i+2)%3]-v[(i+2)%3]*w[(i+1)%3]) for i in range(3))
 def vol(p):return det(*[tuple(V[p[j]][d]-V[p[0]][d] for d in range(3)) for j in range(1,4)])
 base=vol(range(4));perms=list(it.permutations(range(4)));rots=[p for p in perms if vol(p)==base]
 def eq(a,b):return any(all(a[i]==b[p[i]] for i in range(4)) for p in rots)
 def orbit(a):return {''.join(a[p[i]] for i in range(4)) for p in rots}
 assert len(rots)==12
 unseen=set(it.permutations('ABCD'));sizes=[]
 while unseen:
  a=next(iter(unseen));o={tuple(s) for s in orbit(a)};sizes.append(len(o));unseen-=o
 assert sorted(sizes)==[12,12]
 assert not eq('ABCD','ACBD') and eq('ABCD','ADBC') and eq('ABCC','ACBC') and eq('AABC','ABAC')
 merges={a+b:eq('ABCD'.replace(b,a),'ACBD'.replace(b,a)) for a,b in it.combinations('ABCD',2)}
 assert all(merges.values())
 outcomes={}
 for l,r in it.product([0,1],[0,2]):
  a=list('AABC');b=list('ABAC');a[l]='D';b[r]='D';outcomes[f'left_index_{l}_right_index_{r}']=eq(a,b)
 assert list(outcomes.values())==[False,True,True,False]
 return {'proper_vertex_maps':len(rots),'distinct_label_orbits':sizes,'merge_results':merges,'restore_D_results':outcomes,'actual_model_pretest_performed':False}

if __name__=='__main__':
 week=json.loads((ROOT/'config.json').read_text())['week']
 ans={34:symmetry_keys,35:border_keys,36:affine_keys,37:tetra_keys}[week]()
 (ROOT/'verification.json').write_text(json.dumps(ans,indent=2)+'\n')
 print(json.dumps(ans))
