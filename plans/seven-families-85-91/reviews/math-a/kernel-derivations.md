# Independent kernel derivations, mathematical review A

Status: preparatory derivations. Draft page sequences have not yet been read; this is not the final review.

## Week 85: pantograph

MoMath's specified construction uses two long rods A and C with midpoint holes and two half-length rods B and D. Let O=A0, U=A60=C0, X=A30, Y=C30, P=C60, T=B–D. The intended uncrossed quadrilateral X–U–Y–T is a parallelogram, hence X+Y=U+T. Since O=2X−U and P=2Y−U, P−O=2(T−O). Thus anchor O, tracer T and pencil P are collinear and OP=2OT on the same ray. Swapping the roles halves lengths. Area scales by four under the ideal enlargement, rather than two. Equal side-length constraints do not by themselves specify the assembly branch; avoid collapsed/crossed closures and fix the intended topology. These algebraic facts do not establish hardware fit, safe friction, pen contact or reachable paper region.

Primary activity source inspected: Glen Whitney, [Math Monday: Linkages – The World “B.X.”](https://momath.org/mathmonday/math-monday-01-03-11/math-monday-linkages-the-world-b-x/), the Pantograph ingredients/directions/use paragraphs. The independent vector proof here is original to the review.

## Week 86: visible pursuit

Use a finite undirected graph, cop places first, robber places after seeing cop, cop moves first, each may stay, and capture occurs immediately whenever their positions agree. On a finite tree, cop moves one edge toward robber along the unique path. Unless capture occurs, robber is confined to the component beyond the new cop vertex; that component is a strict subset of its preceding safe component. Finiteness forces eventual capture. A path is a special case.

On a bare cycle C_n with n≥4, robber starts at distance at least two and maintains that condition before every cop move. If cop stays, robber may stay. If after cop moves the distance is at least two, robber may stay; if it is one, robber chooses the adjacent vertex farther from cop, restoring distance two. This argument concerns the cycle graph itself, not every graph containing a cycle. C_4 with one diagonal is cop-win (a diagonal endpoint is adjacent to every vertex). Staying is a strategic action and may be essential on odd cycles.

Primary course source inspected: Fan Chung Graham, [A Game of COPS & ROBBERS](https://fanchung.ucsd.edu/152/arch/coprob/), Description, Examples, Structural Description/Theorem. It explicitly uses the same timing and stay rules. Source-level dismantlability characterization is accepted under finite reflexive/closed-neighborhood semantics; any activity-board folding proof still requires separate checking.

## Week 87: sincere voting and line preferences

For three equal votes ABC, BCA, CAB, pairwise majority edges are A>B, B>C, C>A, each 2–1. A three-option knockout agenda awards its bye option the final victory: bye A produces B over C then A over B; bye B produces C over A then B over C; bye C produces A over B then C over A. This is true only when each vote follows the supplied sincere ranking in each pair.

For five equally weighted voters with ideal points x1≤x2≤m=x3≤x4≤x5 on a line and preferences strictly decreasing with distance, compare the offered location m with any distinct y. If y<m, the three voters at or to the right of m strictly favor m. If y>m, the three at or to the left strictly favor m. Therefore m obtains at least three strict votes and defeats every distinct offered challenger, even if the other voters are indifferent. Ties between nonmedian alternatives may occur. The median need not be the arithmetic mean; the theorem needs the median location to be among the offered alternatives for the stated winner claim. It is not a theorem about arbitrary preference lists or plurality voting.

Primary sources inspected: James Stodder, [Strategic Voting and Coalitions: Condorcet's Paradox and Ben-Gurion's Tri-lemma](https://www.economicsnetwork.ac.uk/iree/v4n2/stodder.htm), “A classroom Condorcet game,” sincere-agenda paragraphs; Duncan Black, [On the Rationale of Group Decision-making](https://doi.org/10.1086/256633), Section II, journal pp.26–28, [original article scan](https://rohitvaish.in/data/Papers/%5BBlack%5D%20On%20the%20Rationale%20of%20Group%20Decision-Making.pdf). The activity adaptation should omit Stodder's bargaining/payoff apparatus unless separately selected.

## Week 91: next-exit rotor convention

Each two-way junction's arrow denotes the next departure. Follow it, then flip it. Rotors persist between particles. The literature commonly points to the most recently used exit and rotates first; the next-exit convention is equivalent after relabeling, but its worked example and prose must not mix the two conventions.

For a complete directed binary tree of depth three (three alternating junctions on each root-to-leaf route, seven internal junctions, eight absorbing leaves), every eight consecutive particles launched at the root visit each leaf once for every initial rotor configuration. Root divides its eight departures 4+4; each child divides four 2+2; each grandchild divides two 1+1. Every junction makes an even number of departures, so its state returns. Arbitrary initial arrows can change the order, not the eight-leaf multiset. This exact finite balance is not independence or unpredictability.

For an absorbing undirected path with vertices 0,1,...,m, m edges, input s with 1≤s≤m−1, and a next-exit L/R rotor at each internal vertex, every particle terminates: an infinite trajectory would visit one internal vertex infinitely often, force both neighbors infinitely often through alternation, and thereby reach a sink. Let S be the number of internal next-R arrows, and x the moving particle's vertex. Each departure preserves x+S: moving left subtracts one from x and flips L to R, adding one to S; moving right does the reverse. Across n completed particles, m R_count+S_final=n s+S_initial. Since 0≤S≤m−1, the right-exit count differs from n s/m by less than one. For n=m, integrality forces R_count=s and S_final=S_initial. This holds for every block of m successive particles and every initial configuration, with no burn-in or recurrence assumption. Actual bit configurations can have transients even though the block count is exact from the first block; do not infer all bit configurations return after m launches merely because S returns. The output sequence already follows S_next=(S+s) mod m.

Primary papers inspected: Holroyd and Propp, [Rotor Walks and Markov Chains](https://arxiv.org/pdf/0904.4507), §1 definition, pp.2–3 and §1.1 Theorem 1, pp.3–4; Lionel Levine, [The Rotor-Router Model](https://arxiv.org/pdf/math/0409407), §1 and §§2–3. The latter's expanding interval is not the fixed absorbing-path model. Binary and path proofs above are independent elementary special-case derivations, not claims that the papers print these worksheet instances.

## Reproducible finite checks

`independent_checks.py` imports no author code. `independent-results.json` records 128 binary-tree initial states; 1,538 path/start/configuration cases with m=2,...,8, first and second m-blocks, and potential conservation at every prefix; 100,842 median/challenger cases for five ideals in 0,...,6; exact sincere agenda results; explicit cop-attractor reachability games with staying.

Digital checks do not establish physical pantograph readiness or classroom piloting.
