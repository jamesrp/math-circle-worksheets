"""Independent exact review of the delivered Week 92 problems; no writer code imported."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

lines=[]
def record(s):
    lines.append(s)
def T(x):
    x=F(x)
    assert 0 <= x <= 16
    return 2*min(x,16-x)
def image(band):
    a,b=map(F,band)
    assert 0<=a<=b<=16
    # A continuous piecewise-affine function attains its extrema at
    # an endpoint or at its one interior breakpoint.
    candidates=[T(a),T(b)]
    if a<=8<=b: candidates.append(F(16))
    return min(candidates),max(candidates)
def orbit(band,n):
    states=[tuple(map(F,band))]
    for _ in range(n): states.append(image(states[-1]))
    return states
def fmt(band): return '['+', '.join(map(str,band))+']'

assert T(13)==6
assert image((5,10))==(10,16)
record('Worked visuals: 13 -> nearer-end distance 3 -> 6; [5,10] -> [10,16]. Correct.')

pairs=[(a,b) for a,b in combinations(range(17),2) if T(a)==T(b)]
assert pairs==[(a,16-a) for a in range(8)]
growing=[]
for a,b in combinations(range(17),2):
    p,q=F(a),F(b)
    distances=[abs(p-q)]
    for _ in range(3):
        p,q=T(p),T(q)
        distances.append(abs(p-q))
    if all(x<y for x,y in zip(distances,distances[1:])):
        growing.append(((a,b),list(map(int,distances))))
assert ((0,2),[2,4,8,16]) in growing
record(f'P1 asks for all distinct whole-number pairs merging after one move, then a pair separating on each of three moves. All merging pairs: {pairs}. All three-move growth witnesses: {growing}.')

starts=[(1,4),(10,15),(6,11),(2,14)]
expected=[(2,8),(2,12),(10,16),(4,16)]
for b,w in zip(starts,expected): assert image(b)==w
record('P2 asks for exact one-move output bands: '+ '; '.join(f'{fmt(b)} -> {fmt(image(b))}' for b in starts)+'.')
for b in [(1,2),(7,9)]:
    states=orbit(b,4)
    assert states[-1]==(0,16) and all(x!=(0,16) for x in states[:-1])
    record('P3 asks for first full-track coverage. '+ ' -> '.join(map(fmt,states))+'; exactly 4 moves.')

assert image((6,10))==(12,16)
assert image((5,11))==(10,16)
assert image((7,9))==(14,16)
assert T(1)==2 and T(2)==4 and T(F(3,2))==3
record('P4 intended answer: [6,10] -> [12,16]; further crossing examples [5,11] -> [10,16] and [7,9] -> [14,16]. Literal endpoint-only alternative: [1,2] gives endpoint outputs {2,4}, which misses the valid interior output 3 from 3/2, although shading between endpoint outputs is correct. This wording ambiguity is the report finding.')

assert image((1,2))==(2,4)
assert image((7,9))==(14,16)
for a,b in combinations([F(k,8) for k in range(129)],2):
    lo,hi=image((a,b))
    assert hi-lo>=b-a
    assert (hi-lo==b-a)==(a+b==16)
record('P5 asks for width growth, equality, and possibility of narrowing. [1,2] doubles width; [7,9] preserves width. No nonzero band narrows: on either half width doubles; across 8, write [8-u,8+v], then output width = 2 max(u,v) >= u+v. Equality exactly u=v; zero-width bands also preserve width. Exhaustively checked all 8,256 pairs on 1/8 grid.')

for n,limit in [(3,F(1,4)),(4,F(1,8)),(6,F(1,32))]:
    assert limit==F(2,2**n)
    states=orbit((0,limit),n)
    assert states[-1]==(0,2)
    assert all(0<=a<=b<=2 for a,b in states)
    # Any larger b either violates first-move bound or (until violation)
    # doubles without folding. It must therefore violate by move n.
    record(f'P6 widest band for {n} moves: [0,{limit}]; '+ ' -> '.join(map(fmt,states))+'.')
record('P6 maximality: first-move containment requires b<=1, since b>=8 includes output 16 and otherwise output is [0,2b]. At every later permitted step output remains in [0,2], so the next image doubles without folding. Thus 2^n b<=2 is necessary and sufficient. Enlarged diagrams map 0..1 correctly; answers occupy 1/4, 1/8, 1/32 of their 160-mm lines.')
for n in range(1,30):
    assert orbit((0,F(2,2**n)),n)[-1]==(0,2)
record('P7 asks whether a positive-width starting band exists for any named finite move count n. Yes: [0,2/2^n]. n=0 also permits [0,2]. Infinite time would be a different question; there is no positive-width indefinitely confined interval.')

for n in range(1,11):
    for k in range(2**n):
        b=(F(16*k,2**n),F(16*(k+1),2**n))
        assert orbit(b,n)[-1]==(0,16)
record('P8 each of 2 halves after 1 move, 4 quarters after 2 moves, and 8 eighths after 3 moves has image [0,16]. All dyadic cells through depth 10 checked (2,046 cells). Explanation: T^n is affine onto [0,16] on each depth-n cell, alternating direction. Its midpoint maps to 8. Splitting the cell therefore makes each half map under T^n onto [0,8] or [8,16], each mapped by T onto the full track.')

record('P9 asks whether every positive-width real-endpoint band eventually covers the track. Yes. For [a,b], choose dyadic mesh h=16/2^n < (b-a)/2. With k=ceil(a/h), [kh,(k+1)h] is contained in [a,b], because kh<a+h and (k+1)h<a+2h<b (with weak inequality at grid alignment). P8 gives full-track coverage by n. Degenerate singletons are excluded by "some width". An initially full track needs zero moves and stays full. Endpoint inclusion follows the shared rule.')
record('Diagram review: inspected all six independently rendered PDF pages against source coordinates and extracted text. All track tick labels run 0..16 in order at 10-mm spacings; bands match the starts recorded above. P8 divisions are 0,8,16; 0,4,8,12,16; and every even tick. K-1 packet intentionally omitted by override. Physical apparatus rehearsal was not performed; this is a mathematical/PDF review.')
Path(__file__).with_name('independent_check.txt').write_text('\n\n'.join(lines)+'\n')
print('\n\n'.join(lines))
