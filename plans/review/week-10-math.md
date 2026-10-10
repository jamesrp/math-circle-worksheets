# Week 10 (Bridges and one-stroke drawings): math check

Scope: `lowell-math-circle-year-2/week-10/week-10-k-1.pdf` (F10-K-v4, 12 pp., Problems 1–8), `week-10-grades-2-3.pdf` (F10-M-v4, 12 pp., Problems 1–10), `week-10-grades-4-5.pdf` (F10-U-v4, 12 pp., Problems 1–11) and `week-10-facilitator.pdf` (F10-FAC-v4, 8 pp.). I also checked the return-visit companion in the same folder: `week-10-return-visit.pdf` (F10-RV-v1, 7 pp., Problems 1–3) and `week-10-return-visit-facilitator.pdf` (RV10-FAC-v1, 5 pp.). Archive folders were ignored, and I opened no use logs or session records. I read `source/week-10/src/` and `source/week-10-return-visit/` for data only, and did not run or import the packets' own `check.py`, `check_answers.py`, `verify.py`, `check_math.py` or `independent_check.py`. My scripts and their outputs are in this folder, for `checks/week-10/`. Checked October 10, 2026.

**Result: every student page in all three bands, and every page of the return visit, is mathematically correct. Every town, map and picture matches its text, every "find all" set is what the pages imply, and every claim a page makes ("Nobody can…", "No walk…") is true. Every answer, count, example walk, figure and hint in both adult guides is correct. I found 3 problems, all minor, all in adult-guide prose: a legend sentence that one K–1 answer picture contradicts, and two statements about one-way streets that omit a hypothesis.**

## How it was checked

- `pdfread.py` is my own reader. It uses pdfplumber only to read path operators, line widths, colours and words. It finds islands (white 0.75-inch circles), bridge bands (1.6 cm strokes, straight or Bézier), labels inside islands, check boxes, picture strokes (1.4 pt grey lines and circles) and the return visit's streets, arrowheads, counters and stars. Every band must end at two island centres (within 0.5 pt) and must not pass over a third island.
- `graphs.py` decides everything by exhaustive search over actual walks (memoized over position and used-bridge set), never by the parity rule. It gives every start and end of a walk that uses every bridge once, the closed starts, the walk count, a validity test for island words, the bridge game, and searches over added bridges and extra counters.
- `check_towns.py` (127 checks) reads all 55 towns in the three student PDFs (22, 19 and 14) and solves every town problem. It checks every town answer, example walk and count in the guide, the house bridge game and the Lee count.
- `check_pictures.py` (98 checks) reads every tracing picture (36 drawings, both copies of each). It builds each drawing's graph with corners, line ends, T-junctions, line–line, line–circle and circle–circle crossings as vertices. Then it decides one-stroke by search, gets the fewest strokes as the parity lower bound plus an explicit decomposition, checks for stroke ends that miss by 0.6–4 pt, and checks that the pentagram and triangle pictures are regular.
- `check_koenigsberg.py` (26 checks) reads the land shapes, letters and seven bands from the 4–5 map. It checks that each band runs land, water, land, and answers all three Problem 5 questions by search.
- `check_geometry.py` (161 checks) covers band clearance away from shared islands, visible band length (shortest 3.04 cm), unique consecutive labels, town separation, one check box per K–1 town, equal bridge lengths in the triangular towns, and the guide's busiest-page counter counts.
- `check_guide_figs.py` (52 checks) reads all 22 K–1 answer figures in the guide (black and white nodes, grey, thick and dashed bridges, start dots). It matches each to its student town by layout and edge set, then compares filled islands, dashed new bridges and thick bridges with the search results.
- `check_theory.py` (13 checks) covers all 11,915 connected loopless multigraphs with 2–5 islands and up to 7 bridges. It checks the start and end rule, that the start set is never exactly one island, the handshake fact, the k new bridges for 2k odd islands, fewest strokes = max(1, odd/2) (by search over trail decompositions, up to 6 bridges), and fewest extra counters = minimum matching, open route leaving the best pair (up to 5 bridges). It also checks every 2–3 Problem 8 target and the guide's claims about them.
- `check_rv.py` (173 checks, plus 2 counterexample checks that fail on purpose; see Problems 2 and 3) reads the 8 arrow towns, 4 route-choice towns, stars, launch strip and password examples. It solves all three problems by search, checks every key, word and difference in the return-visit guide, and checks the directed theorem over 6,413 connected digraphs (up to 4 islands, 5 streets).
- `check_sources.py` (32 checks): every problem statement in `source/week-10/src/*.tex` appears in the delivered PDF, and the island counts agree (101, 96, 83), so the PDFs are the current sources.

## K–1: checks out completely

- **P1 (p. 1):** each of the four towns has a walk. Triangle and bowtie: any island, closed. Diamond (two triangles sharing a bridge): only the two middle islands. House: only the two upper corners of the square.
- **P2 (p. 2):** two squares: only the two middle islands (3 bridges each), the walk ending at the other. Big triangle: all six islands, closed.
- **P3 (pp. 3–4):** three-arm star X; two islands joined by three bridges ✓ (either island, ending at the other); triangle with tail ✓ (the 3-bridge corner or the tip); square with centre island on one diagonal ✓ (the two diagonal corners); arc town X (all four islands have 3). Each of the five towns has its own check box.
- **P4 (pp. 5–6):** closed walks: row of two double bridges ✓, double then single X, square with doubled bottom X, three triangles at a hub ✓, two squares with doubled middle rung ✓. Both X towns still have a walk, ending on the other odd island.
- **P5 (pp. 7–8):** house (2 odd points) yes; square with diamond (0) yes; envelope (4) no; circle with diameter (2) yes; circle with plus (4) no; triangle of triangles (0) yes. Every line end meets its neighbour exactly.
- **P6 (pp. 9–10):** the three towns (three-arm star; square with centre island and both diagonals; square with tails at its top corners) each have four odd islands and no walk, as the page says. Searching all 15 island pairs (parallel bridges allowed), exactly the 6 bridges joining two odd islands work. The walk then starts at one of the two odd islands not joined.
- **P7 (p. 10):** both towns can be built from 4 hexagons (e.g. a row; a three-arm star).
- **P8 (pp. 11–12):** arc town: all 6 bridges work; square with tails at opposite corners: only the 2 tail bridges; square with centre island and both diagonals: only the 4 sides.

## Grades 2–3: checks out completely

- **P1 (p. 1):** house B↔C only; triangle with tail A↔C only; two double bridges any island, closed.
- **P2 (pp. 2–3):** town 1 none (D has 5 bridges; A, C, F have 1); town 2 A↔D; town 3 D↔F; town 4 any island, closed.
- **P3 (pp. 4–5):** big triangle all six; triangle with a double bridge A and C; arc town none; square with three spokes none (B, C, D, E odd).
- **P4 (pp. 6–7):** the star, the square with tails and the 2 × 4 ladder have no walk as printed (odd islands ABCD, BCDE, BCFG). In each, exactly the 6 bridges joining two odd islands work, and the walk then runs between the other two.
- **P5 (pp. 7–8):** fewest new bridges for a closed walk: house 1 (only a second B–C), arc town 2 (3 ways), H town 3 (15 ways, the perfect matchings of its six odd islands).
- **P6–P7 (pp. 8–9):** house yes; window no (4 odd); pentagram in a regular pentagon yes (10 points of degree 4); envelope no; rings yes (8 crossings of degree 4; neighbouring top rings and the two bottom rings are apart); square with diamond yes.
- **P8 (p. 10):** all four targets can be built. Two need a double bridge, which the shared rules allow. For "4 islands, 6 bridges, start on any island" there are 34 labelled solutions and none is without a repeated pair. For "3 islands, 5 bridges, start only on A or B", the only solution with at most two sticks per pair is A–B once, A–C twice and B–C twice.
- **P9 (p. 11):** impossible. Among the 11,915 multigraphs, every start set is all islands, exactly two, or none.
- **P10 (p. 12):** arc town 2 bridges (the three pairs with no island in common); three-arm star 3 (all three, the only way).

## Grades 4–5: checks out completely

- **P1–P2 (pp. 1–3):** the towns read identically to the 2–3 towns, with the same answers.
- **P3 (pp. 4–5):** 2 × 4 ladder none (B, C, F, G have 3); bowtie any island, closed; 3 × 3 grid with diagonal B–D only F↔H.
- **P4, P6, P9:** the rule, "no and no", and both sufficiency statements are true for connected towns, which the shared rules guarantee. The brute-force checks confirm all three.
- **P5 (p. 6):** the map's seven bridges are A–B ×2, A–C ×2, A–D, B–D and C–D, each running land, water, land. That gives degrees 5, 3, 3, 3 and no walk. A new bridge between any two areas works (6 choices); one bridge cannot give a closed walk; two can (3 pairings). There is 2.6 cm of open water west of A for a B–C bridge.
- **P7 (pp. 7–8):** fewest strokes are house 1, window 2, cube 4 (8 corners of degree 3, the 2 front–back crossings of degree 4), 3 × 3 grid 4, rings 1 and pentagram 1. Each has a matching decomposition.
- **P8 (p. 9):** Lee's walk uses the 9 outside bridges. The 9 inside bridges are the triangles B I J, C E J and F H J. 352 circuits from A keep Lee's bridges in order and direction (448 in order with any direction; 8,064 circuits from A in all).
- **P10–P11 (pp. 11–12):** (closed, open) = (2, 1) for the arc town, (3, 1) for the star and (2, 0) for the diagonals town, by search over extra counters. The arc town has no closed route with one extra counter.

## Adult guide (F10-FAC-v4)

The overview and section 5 are true with the hypotheses they state: connected multigraphs, parallel bridges allowed. That covers the parity rule, the start sets, the handshake fact, k new edges for 2k odd vertices, Listing's k strokes, the postman matching, and the three-arm star where the "half the odd count" bound fails. All 22 K–1 answer figures match their towns, and every filled island, dashed bridge, thick bridge and start dot matches the search. Every table key, example walk, count (6 per town, 15 ways, 352), hint and materials count (20, 22 + 4, 18) is correct. So are the bridge-game claim (from B or C the second player wins; from A, D or E the first) and Euler's 9 > 8 count.

### 1. K–1 answer-picture legend: "every island filled" is said to mean a closed walk, but one figure has both islands filled and an open walk (guide p. 3)

- **Quoted text:** "In the answer pictures, filled islands are where a walk that picks up every counter can start. The walk then ends on the other filled island. When every island is filled, it ends where it started." The Problem 3 figure for the two islands joined by three bridges has both islands filled, captioned "✓ any island".
- **Evidence:** each of those two islands has 3 bridges. Search finds walks only from either island to the other, never back to the start (`check_towns.out`: "i1->i2; i2->i1"). Every island is filled, so the legend's last sentence tells the adult the walk ends where it started, which it cannot.
- **Smallest fix:** "When every island has an even number of bridges, every island is filled and the walk ends where it started." Or caption the figure "✓ either island; ends on the other".

### 2. "Where it goes next": the directed Euler-circuit criterion omits connectivity (guide p. 7)

- **Quoted text:** "Directed graphs: an Euler circuit exists if and only if in-degree equals out-degree everywhere".
- **Evidence:** return-visit Town 7 (two one-way triangles) has in-degree equal to out-degree at all six islands and no walk at all (`check_rv.out`). The undirected theorem two paragraphs earlier states "connected", and the return-visit guide relies on the distinction.
- **Smallest fix:** "Directed graphs: a connected directed graph has an Euler circuit if and only if in-degree equals out-degree everywhere".

## Return visit

The student pages check out completely.

- **P1 (pp. 1–3):** every street has one arrowhead and one counter at its middle. Town 1 closed; 2 none; 3 A→D only; 4 none; 5 A→C only; 6 none; 7 none (two balanced but separate triangles); 8 closed. In the launch strip the ring sits on X, then Y, then Z, with used streets dashed.
- **P2 (pp. 4–5):** the safe first streets from the star are: Town 1 (A) AB and AC, with AD stranding; Town 2 (D) DA; Town 3 (A) all three; Town 4 (A) AB and AC, with AD stranding.
- **P3 (pp. 6–7):** exhaustive search gives a shortest row of 10 and a shortest circle of 8. The example frames read 01, 11, 10 as captioned. The circle reads 011 clockwise, with the join between the bottom-left 1 and the 0.

In the guide (RV10-FAC-v1), the opening theorem is right: the search over 6,413 digraphs agrees with it. So does every town key, word and difference (+2/−2; +1, −2, +2, −1; +1, +2, −3), every safe and unsafe first street and completion word, the reachability argument, the bridge-free claim for all-even towns, 0001011100, the necklace 00010111, the two necklaces up to rotation, the 12 + 12 slips and the overlap circuit.

### 3. Return-visit guide "Open walks": the hypothesis leaves out "every other island balances" (guide p. 3)

- **Quoted text:** "If exactly one start has outgoing-minus-incoming equal to 1 and exactly one end has incoming-minus-outgoing equal to 1, temporarily add a street from end to start. The augmented town balances and has a closed all-street walk."
- **Evidence:** take the connected streets A→B, B→C, C→B, C→D, C→D. Outgoing minus incoming is +1 at A, −1 at B, +2 at C and −2 at D. Exactly one island is at +1 and exactly one at −1, but adding B→A leaves C at +2 and D at −2. The augmented town does not balance, and search finds no walk (`check_rv.out`). The page 1 overview states the condition correctly ("and all others balance").
- **Smallest fix:** "If exactly one start has outgoing-minus-incoming equal to 1, exactly one end has incoming-minus-outgoing equal to 1, and every other island balances, temporarily add a street from end to start."
