"""Independent mathematical checks for Weeks 85, 86, 87, 91.
No author code imported. Run with Python 3; results saved beside this file.
"""
from collections import Counter
from itertools import product, combinations
from pathlib import Path
import json, math


def cop_attractor(graph):
    """Full perfect-information reachability game; cop/robber may stay.
    States (cop, robber, turn): turn=0 cop to move, 1 robber to move.
    Cop chooses an attracting successor; all robber successors must attract.
    Capture is immediate whenever positions coincide.
    """
    nodes = tuple(graph)
    states = [(c,r,t) for c in nodes for r in nodes for t in [0,1]]
    win = {(c,c,t):0 for c in nodes for t in [0,1]}
    changed = True
    while changed:
        changed = False
        for c,r,t in states:
            if (c,r,t) in win:
                continue
            successors = [(d,r,1) for d in [c]+graph[c]] if t==0 else [(c,d,0) for d in [r]+graph[r]]
            known = [win[s] for s in successors if s in win]
            if t==0 and known:
                win[c,r,t] = 1+min(known)
                changed = True
            elif t==1 and len(known)==len(successors):
                win[c,r,t] = 1+max(known)
                changed = True
    starts=[c for c in nodes if all((c,r,0) in win for r in nodes)]
    return {"winning_cop_starts": starts,"winning_states":len(win),"state_count":len(states)}


def cop_move_bounds(g):
    """Least worst-case cop-move bound for each occupied state.
    All robber replies may stay. A layer corresponds to one cop move.
    """
    nodes=tuple(g)
    won={(c,c):0 for c in nodes}
    k=0
    while True:
        k+=1
        old=won.copy()
        for c in nodes:
            for r in nodes:
                if (c,r) in old: continue
                for d in [c]+g[c]:
                    if d==r or all((d,e) in old for e in [r]+g[r]):
                        won[c,r]=k
                        break
        if len(won)==len(old): break
    return {c:max(won[c,r] for r in nodes) if all((c,r) in won for r in nodes) else None for c in nodes}


def closed(g,v):
    return set(g[v])|{v}


def fold(g,v,u):
    assert u in g[v] and closed(g,v)<=closed(g,u)
    return {x:[y for y in adj if y!=v] for x,adj in g.items() if x!=v}


def graph(edges):
    out = {}
    for a,b in edges:
        out.setdefault(a,[]).append(b)
        out.setdefault(b,[]).append(a)
    return out


def binary_outputs(bits, count, depth=3):
    bits=list(bits)
    leaves=[]
    for _ in range(count):
        i=0
        path=[]
        for level in range(depth):
            d=bits[i]
            bits[i]^=1
            path.append(d)
            i=2*i+1+d
        leaves.append(''.join('R' if d else 'L' for d in path))
    return leaves,tuple(bits)


def path_outputs(bits, count, start=1):
    """Next-exit arrows 0=L, 1=R; endpoints 0,N absorb."""
    bits=list(bits)
    N=len(bits)+1
    exits=[]
    traces=[]
    for _ in range(count):
        at=start
        trace=[at]
        seen=set()
        while 0<at<N:
            state=(at,tuple(bits))
            assert state not in seen, 'nonabsorbing loop'
            seen.add(state)
            d=bits[at-1]
            bits[at-1]^=1
            at += 2*d-1
            trace.append(at)
        exits.append('L' if at==0 else 'R')
        traces.append(trace)
    return exits,tuple(bits),traces


def voting_checks():
    rankings=['ABC','BCA','CAB']
    def beats(a,b):
        return sum(r.index(a)<r.index(b) for r in rankings)>len(rankings)/2
    edges = [a+'>'+b for a,b in [('A','B'),('B','C'),('C','A')] if beats(a,b)]
    agendas={}
    for bye in 'ABC':
        a,b=[x for x in 'ABC' if x!=bye]
        first=a if beats(a,b) else b
        winner=bye if beats(bye,first) else first
        agendas[bye]={"first_pair":a+b,"first_winner":first,"final_winner":winner}
        assert winner==bye
    # Repeated favorite locations allowed; compare any distinct integer y.
    checked=0
    for ideals in product(range(7),repeat=5):
        m=sorted(ideals)[2]
        for y in range(7):
            if y==m: continue
            votes=sum(abs(x-m)<abs(x-y) for x in ideals)
            assert votes>=3
            checked+=1
    def counts(ideals,a,b):
        left=sum(abs(p-a)<abs(p-b) for p in ideals)
        right=sum(abs(p-b)<abs(p-a) for p in ideals)
        return (left,right,len(ideals)-left-right)
    concrete={q:counts([0,2,4,7,10],4,q) for q in range(11) if q!=4}
    assert concrete[1]==(3,2,0) and concrete[2]==(3,2,0)
    even=[x for x in range(11) if all(counts([1,3,7,9],x,y)[0]>=counts([1,3,7,9],x,y)[1] for y in range(11) if y!=x)]
    assert even==[3,4,5,6,7]
    strict=[x for x in range(11) if all(counts([1,3,7,9],x,y)[0]>counts([1,3,7,9],x,y)[1] for y in range(11) if y!=x)]
    assert strict==[]
    all_line_duels={str(x)+':'+str(y):counts([1,3,7,9],x,y) for x,y in combinations(range(11),2)}
    def profile(profile):
        def winner(a,b):
            return a if sum(r.index(a)<r.index(b) for r in profile)>=2 else b
        return {bye:winner(bye,winner(*[x for x in 'ABC' if x!=bye])) for bye in 'ABC'}
    fixed=profile(['ABC','ACB','BAC'])
    reversed_cycle=profile(['ACB','CBA','BAC'])
    assert fixed=={'A':'A','B':'A','C':'A'}
    assert reversed_cycle=={'A':'A','B':'B','C':'C'}
    demo=['DFE','FED','EDF']
    assert sum(r.index('E')<r.index('D') for r in demo)==2
    assert sum(r.index('F')<r.index('E') for r in demo)==2
    return {"pairwise_cycle":edges,"bye_agendas":agendas,"median_checks":checked,"W87_P4_counts_for_favorites_0_2_4_7_10":concrete,"W87_P3_fixed_profile_agendas":fixed,"W87_P3_reversed_cycle_agendas":reversed_cycle,"W87_P6_weak_winners":even,"W87_P6_strict_winners":strict,"W87_P6_all_duels":all_line_duels,"W87_convention_examples":"E over D 2–1; F over E 2–1; distances2vs3 and tie2vs2 correct"}


def linkage_checks():
    # Two independent vectors u,v, both length 30. Convex rhombus:
    # O=0, S=u, U=2u, V=2u+v, T=u+v, P=2u+2v.
    tests=[]
    for alpha in [0,math.pi/5,math.pi/2]:
        for theta in [math.pi/6,math.pi/3,math.pi/2,2*math.pi/3]:
            u=(30*math.cos(alpha),30*math.sin(alpha))
            v=(30*math.cos(alpha+theta),30*math.sin(alpha+theta))
            O=(0,0); S=u; U=tuple(2*x for x in u)
            T=tuple(u[i]+v[i] for i in range(2))
            V=tuple(2*u[i]+v[i] for i in range(2))
            P=tuple(2*u[i]+2*v[i] for i in range(2))
            lengths=[math.dist(S,U),math.dist(U,V),math.dist(V,T),math.dist(T,S)]
            assert all(abs(d-30)<1e-9 for d in lengths)
            assert all(abs(P[i]-2*T[i])<1e-9 for i in range(2))
            tests.append({"theta_degrees":round(theta*180/math.pi),"T":T,"P":P})
    # Degenerate alternate closure T=U satisfies equal 30 side constraints,
    # but violates the required homothety for nonparallel u,v.
    # Original Week 85 support proposal: half-bars 80, O=(40,140), T=(110,140).
    q_dy=2*math.sqrt(80**2-35**2)
    clearance={"nominal_T":[110,140],"anchor":[40,140],"possible_Q_centers":[[110,140-q_dy],[110,140+q_dy]],"joined_mat_height":279,"original_proposed_board_height":280}
    assert 140-q_dy<0 and 140+q_dy>280
    max_q_offset=max(abs(y+sign*x*math.sqrt(160**2/(x*x+y*y)-1)) for x in range(70,121) for y in range(-25,26) for sign in [-1,1])
    assert max_q_offset+math.sqrt(11**2+9**2)<179.5
    clearance['max_Q_vertical_offset_on_integer_safe_zone_grid']=max_q_offset
    # Continuous conservative bounds for the final 450 x 400 support.
    # Q=t +/- rot90(t)*sqrt(160^2/|t|^2-1), |Q|=160.
    # In the nominal rectangle, 70<=x<=120, |y|<=25, so |t|>=70.
    margin=math.hypot(11,9)
    multiplier=math.sqrt(160**2/70**2-1)
    qx_min=70-25*multiplier
    qx_max=120+25*multiplier
    # O, X=Q/2, T, Y=Q/2+T, and P=2T bound all bar endpoints.
    endpoint_x_min=min(0,qx_min,qx_min/2,70,qx_min/2+70,140)
    endpoint_x_max=max(0,qx_max,qx_max/2,120,qx_max/2+120,240)
    # Q supplies the widest vertical range; Y is bounded by 80+25.
    bounds=[49+endpoint_x_min-margin,49+endpoint_x_max+margin,
            200.5-160-margin,200.5+160+margin]
    assert 0<bounds[0]<bounds[1]<450
    assert 0<bounds[2]<bounds[3]<400
    clearance['final_support_size_mm']=[450,400]
    clearance['final_anchor_support_coordinates_mm']=[49,200.5]
    clearance['conservative_continuous_strip_bounds_mm']={
        'x_min':bounds[0],'x_max':bounds[1],'y_min':bounds[2],'y_max':bounds[3]}
    clearance['status']='Ideal continuous bar geometry fits the final support. Physical hardware and hand-clearance rehearsal remain required.'
    return {"valid_configurations":len(tests),"examples":tests[:4],"W85_board_clearance":clearance,
            "warning":"Equal side lengths alone do not select the parallelogram closure; the legal assembly branch is essential."}


def run():
    graphs={
        'path5':graph([(0,1),(1,2),(2,3),(3,4)]),
        'path7':graph([(i,i+1) for i in range(6)]),
        'C6':graph([(i,(i+1)%6) for i in range(6)]),
        'C8':graph([(i,(i+1)%8) for i in range(8)]),
        'triangle_tail6':graph([('a','b'),('b','c'),('c','a'),('c','d'),('d','e'),('e','f')]),
        'wheel5':graph([(0,1),(1,2),(2,3),(3,0),(4,0),(4,1),(4,2),(4,3)]),
        'star4':graph([(0,1),(0,2),(0,3)]),
        'tree7':graph([(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]),
        'W86_T1':graph([('o','a'),('a','b'),('o','c'),('c','d'),('o','e'),('e','f')]),
        'W86_T2':graph([('a','b'),('b','c'),('c','d'),('d','e'),('c','f'),('f','g'),('f','h')]),
        'W86_F1':graph([('a','b'),('b','c'),('c','a'),('c','d'),('d','e'),('a','f')]),
        'W86_F2':graph([('a','b'),('b','c'),('c','d'),('d','e'),('e','a'),('a','c')]),
        'triangle':graph([(0,1),(1,2),(2,0)]),
        'C4':graph([(0,1),(1,2),(2,3),(3,0)]),
        'C5':graph([(0,1),(1,2),(2,3),(3,4),(4,0)]),
        'C4_plus_diagonal':graph([(0,1),(1,2),(2,3),(3,0),(0,2)]),
    }
    cop_results={k:cop_attractor(v) for k,v in graphs.items()}
    for k in ['path5','star4','tree7','triangle','C4_plus_diagonal','W86_T1','W86_T2','W86_F1','path7','triangle_tail6','wheel5']:
        assert cop_results[k]['winning_cop_starts']
    for k in ['C4','C5','C6','C8','W86_F2']:
        assert not cop_results[k]['winning_cop_starts']
    bounds={k:cop_move_bounds(v) for k,v in graphs.items()}
    assert bounds['path5'][2]==2 and bounds['path7'][3]==3
    assert bounds['W86_T1']['o']==2
    assert bounds['W86_T2']['c']==2
    assert bounds['W86_T2']['f']==3
    f1=graphs['W86_F1']
    for v,u in [('e','d'),('d','c'),('f','a'),('a','b'),('b','c')]:
        f1=fold(f1,v,u)
    assert tuple(f1)==('c',)
    f2folds=[(v,u) for v in graphs['W86_F2'] for u in graphs['W86_F2'][v] if closed(graphs['W86_F2'],v)<=closed(graphs['W86_F2'],u)]
    assert f2folds==[('b','a'),('b','c')]
    cycle5_edges=[(0,1),(1,2),(2,3),(3,4),(4,0)]
    chords=[(0,2),(0,3),(1,3),(1,4),(2,4)]
    chord_results={}
    for n in range(3):
        chord_results[n]=[{'chords':extra,'cop_win':bool(cop_attractor(graph(cycle5_edges+list(extra)))['winning_cop_starts'])} for extra in combinations(chords,n)]
    assert not any(x['cop_win'] for x in chord_results[1])
    assert sum(x['cop_win'] for x in chord_results[2])==5
    tree_checked=0
    for bits in product([0,1],repeat=7):
        leaves,final=binary_outputs(bits,16)
        assert Counter(leaves[:8])==Counter({x:1 for x in ['LLL','LLR','LRL','LRR','RLL','RLR','RRL','RRR']})
        assert leaves[:8]==leaves[8:]
        assert final==bits
        tree_checked+=1
    prog2=[bits for bits in product([0,1],repeat=3) if binary_outputs(bits,3,2)[0]==['LL','RL','LR']]
    assert prog2==[(0,0,0)]
    assert not any(binary_outputs(bits,3,2)[0]==['LL','LR','RL'] for bits in product([0,1],repeat=3))
    prog3=[bits for bits in product([0,1],repeat=7) if binary_outputs(bits,4)[0]==['LLL','RLL','LRL','RRL']]
    assert prog3==[(0,)*7]
    assert not any(binary_outputs(bits,2)[0]==['LLL','LLR'] for bits in product([0,1],repeat=7))
    path_checked=0
    for N in range(2,9):
        for bits in product([0,1],repeat=N-1):
            for start in range(1,N):
                exits,final,traces=path_outputs(bits,2*N,start)
                assert exits[:N].count('R')==start
                assert exits[N:].count('R')==start
                for n in range(1,2*N+1):
                    # Conservation: N*right_count = n*start + S_initial - S_after.
                    e,f,t=path_outputs(bits,n,start)
                    assert N*e.count('R')==n*start+sum(bits)-sum(f)
                    assert abs(e.count('R')-n*start/N)<1
                path_checked+=1
    worked_e,worked_f,worked_t=path_outputs((1,0),1,2)
    assert worked_t==[[2,1,2,3]] and worked_f==(0,0)
    encore_e,encore_f,encore_t=path_outputs((0,0,0),8,2)
    assert ''.join(encore_e)=='LRLRLRLR'
    assert encore_t[:2]==[[2,1,0],[2,3,2,1,2,3,4]]
    all_left_m5={str(k):''.join(path_outputs((0,0,0,0),5,k)[0]) for k in range(1,5)}
    assert all_left_m5=={'1':'LLLLR','2':'LLRLR','3':'LRLRR','4':'LRRRR'}
    all_left,final,traces=path_outputs((0,0,0),8,1)
    # Same S can yield identical exits but different initial bit states.
    # A full m-launch block need not restore an arbitrary bit configuration.
    transient_examples=[]
    for bits in product([0,1],repeat=3):
        e,f,t=path_outputs(bits,4,1)
        if f!=bits:
            transient_examples.append({'initial_bits':bits,'after_four':f,'exits':''.join(e)})
    output={"linkage":linkage_checks(),"pursuit":cop_results,"cop_move_bounds":bounds,"folds":{"F1_verified_sequence":["e>d","d>c","f>a","a>b","b>c"],"F2_initial_legal_folds":f2folds},"C5_chord_edits":chord_results,"voting":voting_checks(),
            "binary_tree":{"configurations_checked":tree_checked,"P2_ACB_initial_states":prog2,"P3_AECG_initial_states":prog3,"P2_ABC_and_P3_AB":"impossible; exhaustively checked all initial states", "all_left_first_eight":binary_outputs((0,)*7,8)[0]},
            "absorbing_paths":{"cases_checked":path_checked,"W91_convention_example":{"trace":worked_t,"final_arrows":worked_f},"W91_encore_P1":{"outputs":"".join(encore_e),"first_two_traces":encore_t[:2]},"W91_encore_P2_all_left_words":all_left_m5,"all_left_0_to_4_start1":''.join(all_left),"first_four_traces":traces[:4],"rotor_state_transient_examples":transient_examples,"all_initial_exact_block_theorem":"On path 0..N, N consecutive particles started at k produce exactly k right exits for every initial next-exit configuration."}}
    (Path(__file__).parent/'independent-results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__=='__main__':
    run()
