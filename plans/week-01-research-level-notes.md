# Research mathematics behind the revised tiling session

Research and independent finite verification, September 19, 2026. These are design notes, not a claim that the cited authors designed these children's activities. The printable lessons should select a small portion; the research connections belong mainly in facilitator material.

## Four substantive questions and their sources

1. **Existence:** what information proves that tiling a region is impossible? William P. Thurston, *Conway's Tiling Groups*, American Mathematical Monthly 97(8), 1990, pp. 757–773, develops the group-valued boundary obstruction and a geometric lifting approach. Section 4, especially printed p. 767, describes lozenge tilings as stepped surfaces in the cubic lattice, with integer vertex heights, and uses compatible boundary heights to construct an extremal tiling. His tileability results here concern simply connected regions. The boundary-group condition alone is generally necessary, not sufficient. [Original paper, university-hosted scan](https://www.ibr.cs.tu-bs.de/users/fekete/oldhp/Sem06/thurston.pdf); [publication record](https://doi.org/10.1080/00029890.1990.11995660).

2. **Reconfiguration and optimization:** can any tiling be changed into any other using a prescribed tiny move, and what is the fewest moves? Saldanha and Tomei, *An overview of domino and lozenge tilings*, Sections 1–3, explain three-rhombus hexagon flips, cube piles, and height functions. For a simply connected finite triangular-grid region, the lozenge flip graph is connected (Theorem 3.1), and minimum flip distance is one third of the sum of absolute vertex-height differences (Theorem 3.2, PDF p. 12). Theorem 1.3 says each orientation's rhombus count is fixed by the region. Holes can obstruct flip connectivity: do not generalize the no-hole claim to arbitrary regions or mixed pattern-block pieces. [Author manuscript](https://arxiv.org/pdf/math/9801111).

3. **Enumeration and large-scale shape:** how many tilings exist, and what does a typical one look like? Cohn, Larsen, and Propp, *The Shape of a Typical Boxed Plane Partition*, NYJM 4 (1998), pp. 137–165, identify hexagonal lozenge tilings with cube piles in a box and study the limiting shape of a uniformly selected large pile/tiling. Their questions are the large version of counting all six small-board configurations. We are not teaching their asymptotic result, and a tiny board does not exhibit its limiting phenomenon. [Original paper and abstract](https://nyjm.albany.edu/j/1998/4-10.html).

4. **Random dynamics:** if we make random local changes, which tilings are visited, and how long until the process becomes nearly random? David B. Wilson's *Mixing times of lozenge tiling and card shuffling Markov chains* treats those two topics in the same paper. Section 5.2 (especially PDF p. 13) defines the local move chain and explains why symmetry yields uniform stationarity for that rule; §5.6 treats local-chain mixing. This is a direct mathematical bridge to the user's cup-swapping example. It does not justify saying every random-flip rule is uniform. [Original paper](https://arxiv.org/pdf/math/0102193).

## Proposed grades 4–5 investigation: one board, six states

Use **only eight blue 60-degree rhombi**, on a triangular-grid hexagon with consecutive side lengths 1,2,2,1,2,2. Do not permit the other pattern-block pieces in this investigation. The board has area sixteen small equilateral triangles. Keep a marked side or corner fixed; rotated or reflected arrangements occupying different internal positions count separately. Identical blue pieces are indistinguishable.

The legal move is to locate three blue rhombi that fill one small regular hexagon, lift precisely those three, and refill that same hexagon in its other way. This is the actual lozenge flip of the research sources. Merely moving one piece or rearranging a larger area is not one legal move.

### Suggested sequence

- Let children first build the board and handle the blocks. Demonstrate one flip on a separate three-rhombus hexagon.
- Challenge them to turn tiling A into tiling F by flips, and record a route. Ask whether fewer moves could work.
- Collect all states reached, give each one a card, and connect two cards exactly when one flip joins them. Ask whether the picture is complete and how one could check.
- Have them find two shortest A-to-F routes; invent a pair of equally distant states; ask whether a return in exactly three or five flips is possible.
- Offer a larger regular side-2 hexagon only after the first graph is understood. It requires twelve rhombi and has twenty tilings. Ask which parts of the method still work when drawing every state becomes inconvenient.

These are proposals, not adaptations of a published elementary lesson. Counting all states, proving optimality, and detecting a parity obstruction are the mathematical products, not decorative vocabulary.

### Checked answer key

The file [week-01-lozenge-research.json](week-01-lozenge-research.json) supplies actual tile polygons for every state, boundary and unit triangles, all legal flips and their centers, vertex heights, and all pairwise graph distances. [The standard-library Python enumerator](week-01-lozenge-research.py) independently searches every perfect matching of adjacent unit triangles, checks consistency of the heights, constructs the flip graph, and verifies the distance formula against breadth-first search. It also checks the twenty-state count for the larger board.

In the generated labels:

| State | Neighbors | Rank | Equivalent path code |
|---|---|---:|---|
| A | B | 0 | 0011 |
| B | A, C, D | 1 | 0101 |
| C | B, E | 2 | 1001 |
| D | B, E | 2 | 0110 |
| E | C, D, F | 3 | 1010 |
| F | E | 4 | 1100 |

Thus the graph is A—B, with a diamond B—C—E—D—B, followed by E—F. It has six vertices and six edges. The shortest A-to-F routes are A-B-C-E-F and A-B-D-E-F, each four moves. C-to-D takes two moves and has two shortest routes. The diameter is four. Every step changes rank by exactly one, so returns have even length. The two rank-parity classes contain four and two states; equal class sizes are not required for a graph to be bipartite.

**A child-accessible optimality certificate:** after the graph has been established, put levels 0,1,2,2,3,4 on the state cards. One move changes the level by only one. Going from level zero to level four therefore needs at least four moves; exhibiting a four-move route proves it is best. This is a finite proof, provided completeness of the six-card graph has actually been checked. It is not a proof that arbitrary mixed-block swaps enjoy these properties.

### Actual height / cube structure behind the level numbers

Axial lattice coordinates (u,v) in the JSON mean ordinary coordinates (u+v/2, sqrt(3)v/2). Its hexagon vertices are (0,0), (1,0), (1,2), (-1,4), (-2,4), (-2,2). Fix height zero at (0,0). Direct each unit edge with the upward-pointing triangle on its left. Along a directed edge add 1 if it is a tile edge and subtract 2 if it is the diagonal covered by a rhombus. Heights are consistent around every tile.

Only four interior vertices change with the tiling. Normalizing each by subtracting its height in A and dividing by three gives four zero/one coordinates. Name their positions p=(0,2), q=(0,1), r=(-1,3), s=(-1,2). Their occupied sets are:

- A: empty;
- B: {p};
- C: {p,q};
- D: {p,r};
- E: {p,q,r};
- F: {p,q,r,s}.

The dependencies are p before q and r, and both q and r before s. These are exactly the order ideals of a 2-by-2 grid, or the possible cube piles in a 2-by-2-by-1 box. Rank counts occupied positions/cubes; a flip adds or removes one. This explains the level certificate geometrically and proves why two middle moves may occur in either order. Do not require elementary children to calculate negative height values; use the actual tilings, graph, and optional four-cube model.

### An elementary complete count and rank statistic, directly on the pictures

The JSON also constructs a real path through each tiling (`path_midpoints` and `path_tile_indices`), not just an abstract correspondence. Start at the midpoint of the marked bottom horizontal boundary edge. Cross its rhombus to the midpoint of the opposite horizontal edge. Continue in this way upward through successive rhombi until the top horizontal boundary edge. Each crossing goes northeast (R) or northwest (L). There are exactly two R and two L crossings because the vertical rise is four rows and the endpoints are vertically aligned in ordinary coordinates.

Every rhombus with horizontal sides lies on this one ribbon: follow a supposed second ribbon downward; it cannot cycle because every step strictly decreases its vertical coordinate, and it would have to reach another horizontal bottom boundary edge, which does not exist. All remaining rhombi have the third orientation. Each triangle has at most one partner in that orientation, so the remaining placements are forced once the ribbon is known.

There are only six four-letter orders containing two R and two L: RRLL, RLRL, RLLR, LRRL, LRLR, LLRR. The six displayed tilings realize them all, so there cannot be a hidden seventh state or disconnected component. This is an elementary completeness proof independent of both the program and the general connectivity theorem. Use colored string laid along the path, or draw its segments on copied cards, to keep the representation concrete. Codes in the table write R=0 and L=1.

On this ribbon a flip exchanges two neighboring unlike letters, RL and LR. Count every pair in which an L occurs earlier than an R. In RRLL there are zero; in LLRR there are four. Swapping adjacent unlike letters changes this count by exactly one: their mutual order changes, while their order with every other letter is unchanged. Consequently at least four flips are necessary. The two four-flip routes attain this bound. Counting crossed pairs is suitable as an optional grade-5 explanation after exploring the graph; no formal height notation or probability is needed.

### Independent cell-by-cell completeness proof

For a facilitator who prefers covering decisions, number the small triangles 1–16 using `id+1` from the JSON (the file itself uses zero-based IDs). A blue rhombus joins two side-adjacent triangles. At every branch below the specified triangle has exactly the two stated available partners. A forced pair means a still-empty triangle has only one available partner.

| Decisions | Forced continuation | Result |
|---|---|---|
| 1+7 | 2+3, 4+5, 6+12, 11+10, 9+8, 13+14, 15+16 | F |
| 1+2; 3+9 | 4+5, 11+10, 16+15; now branch on 6 | next two rows |
| previous row; 6+7 | 8+14, 12+13 | D |
| previous row; 6+12 | 7+8, 13+14 | E |
| 1+2; 3+4 | 5+11; now branch on 6 | next three rows |
| previous row; 6+12 | 7+8, 9+10, 13+14, 15+16 | C |
| 1+2; 3+4; 6+7; 8+9 | 5+11, 12+13, 10+16, 14+15 | A |
| 1+2; 3+4; 6+7; 8+14 | 5+11, 12+13, 9+10, 15+16 | B |

At the root, triangle 1 can only pair with 2 or 7. After 1+2, triangle 3 can only pair with 4 or 9. The table covers both options each time, proving exhaustion. The path argument is shorter and has a richer connection to the minimum-move question; this table is a backup check on the physical geometry.

## Optional probability follow-up, kept out of the core hour

There are two different experiments worth contrasting.

**Choose uniformly among currently legal flips.** On the six-state graph the degrees are 1,3,2,2,3,1. Long-run occupancy is proportional to degree, so A through F have weights (1,3,2,2,3,1)/12. The expected first positive return times are respectively 12,4,6,6,4,12 steps. In particular, starting at A gives mean return twelve, despite there being six states. These values can be checked directly by first-step equations or by the finite Markov-chain return theorem. This walk has period two; its one-time distribution oscillates between parity classes, although occupation frequencies have the stated limits.

**Choose uniformly among the four marked interior vertices; flip there if possible, otherwise count a turn and stay put.** Each possible transition has probability 1/4 in both directions, so the uniform distribution on six states is stationary. Self-loops remove periodicity, and mean first positive return is six turns at every state. Here a stay-put turn can already count as a return at time one. If you discard those turns from the count, you have changed the experiment back toward the first rule.

The cup puzzle's random transpositions form a regular six-vertex graph, so its mean return is six. Its natural generalization has n! states and uniform stationarity, giving mean n! for n at least two; periodicity does not invalidate the finite irreducible chain return formula. This is a useful facilitator connection, not a prerequisite or a promised discovery for a fourth grader in Week 1.

## Why this meets the user's requested standard

The children encounter a genuine instance of a research object: a flip graph of lozenge tilings. Its small size allows experimentation and complete proofs. The same questions survive enlargement: classify possible states, count them, decide reachability, optimize a route, find invariants, and study random motion. The research names can disappear from the student page without weakening the mathematical direction.
