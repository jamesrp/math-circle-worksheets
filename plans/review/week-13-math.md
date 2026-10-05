# Week 13 (route packing and bottlenecks): math check

Scope: `lowell-math-circle-year-2/week-13/week-13-k-1.pdf` (6 pp., Problems 1–6), `week-13-grades-2-3.pdf` (7 pp., Problems 1–6), `week-13-grades-4-5.pdf` (7 pp., Problems 1–7) and `week-13-facilitator.pdf` (11 pp.). I also checked the return-visit companion in the same folder: `week-13-return-visit.pdf` (3 pp., Problems 1–3) and `week-13-return-visit-facilitator.pdf` (5 pp.). Archive folders were ignored. I opened no use logs or session records. My scripts and outputs are in [checks/week-13/](checks/week-13/). Checked October 5, 2026.

**Result: no errors in any student band of the base packet. The adult guide has 4 minor problems: two incomplete keys, one incomplete argument and one wrong page reference. The return visit has 1 minor problem: its last task repeats the first. No stated answer is wrong.**

## How it was checked

- The delivered PDFs are byte-identical (MD5) to `source/week-13/editable/reference-pdfs/` and `source/week-13-return-visit/reference-pdfs/`.
- `pdfgeom.py` and `extract_graphs.py` read the drawn networks straight out of the PDFs: dots, arrow shafts, arrowheads, thick grey reservation strokes, letters, and the return visit's capacity numbers. Each shaft becomes a directed edge, with the head at the end next to an arrowhead. The script compares all 59 networks with my own transcription in `graphs.py`. The 59 are 42 in the base student pages, 7 in the return visit and 10 figures in the guide. Every edge set, arrow direction, thick-arrow set, letter and capacity matches (`extract_graphs.out`). On lettered boards, the printed letters agree with the dot positions. No two arrows cross away from a dot. There are no regular figures, so equal x/y scaling does not apply.
- `routes.py` and `solve.py` are my own exhaustive search code. They enumerate all simple routes, every edge-disjoint collection, all minimum closures (by subset search), every start-side split, the full closing game tree, every simple change-walk (with toggling and re-decomposition), residual reachability, every one-arrow addition, vertex-disjoint packings, assigned-pair routings and capacity packings (`solve.out`).
- `theorem_check.py` tests the guide's general claims and 4–5 P7 on all 4,096 directed graphs on four dots and on 28,000 random graphs on five and six dots. For *every* edge-disjoint route collection on each graph it checks four things. First, largest collection = fewest blocking arrows = smallest out-count of a split. Second, no change-walk exists exactly when the collection is largest. Third, toggling any change-walk and discarding cycles gives one more edge-disjoint simple route. Fourth, with no change-walk, every arrow leaving the reachable set is reserved, none entering it is, and their number is the route count. All assertions pass (`theorem_check.out`). Collections that are stuck but not largest occur (3,137 cases), and cycles do appear after toggling (167 cases on six dots), as the guide warns.

## K–1: checks out completely

- **P1:** greedy board max 2, with one largest collection only (s-A-t, s-B-t), so "Find another… if you can" has no answer there; bowtie max 2, with exactly 2 collections.
- **P2:** diamond min 2 with 4 closures; funnel min 1 with 2 closures (CD, Dt).
- **P3:** three-to-two board 2 = 2; three-branch board 3 = 3.
- **P4:** exactly 6 single closures keep two routes on the upper board (sA, sB, sC, AD, BD, CD); exactly 1 on the greedy board (AB).
- **P5:** exactly 8 blocking pairs. The page has 8 small recording copies.
- **P6:** diamond is a second-player win; greedy is a first-player win, and AB is the only winning first move.

## Grades 2–3: checks out completely

- **P1:** both boards max 2 = min 2.
- **P2:** 18 routes, 36 unordered maximum collections, max 2. The minimum closures are {DE,DF}, {EG,FG}, {DE,FG} and {DF,EG}.
- **P3:** exactly the 8 pairs.
- **P4:** upper board: exactly 16 new arrows work, any arrow from A, B, C or D to G, H, I or J. The lower board is impossible.
- **P5:** both reserved collections are stuck, and both boards have max 2. Each board has exactly one simple change-walk: s-B-A-t, and s-B-A-C-E-D-t, which cancels AB and DE.
- **P6:** same as K–1 P6.

## Grades 4–5: checks out completely

- **P1:** same as 2–3 P5.
- **P2:** same as 2–3 P2. The out-arrows of {s,A,B,C,D} are exactly DE and DF.
- **P3:** exactly 3 splits qualify: {s,A}, {s,A,B} and {s,A,B,D}, so "two different splits" is possible.
- **P4:** the minimum closures are {sA,sB}, {sB,AC}, {AC,BD}, {AC,Dt} and {Ct,Dt}. Only the middle three have a route using two of their arrows. Every such route belongs only to collections of size 1, so the answer is always no. (See guide problem 2.)
- **P5:** no route fits beside the reserved routes, and the unique simple change-walk is s-A-D-B-E-C-F-t, giving s-A-D-t, s-B-E-t and s-C-F-t.
- **P6:** the reachable set is {s,A,B,C,D}. Its only out-arrows are DE and DF, both reserved, and no arrow enters it.
- **P7:** yes (the theorem; also `theorem_check.py`).

## Adult guide

The overview's facts (unit-capacity max-flow/min-cut, the split formulation, routes crossing a cut more than once, stuck ≠ largest, augment-then-remove-cycles, the reachable-set cut, and the limits to one endpoint pair and edge-disjoint routes) are true with the stated hypotheses. So are the P7 proof, the existence argument and its cycle-removal step. Every count, list, route, game claim and certificate in the keys matches my computations: "uniquely", "exactly two collections", the 4 and 2 closures, "exactly six", "exactly eight", "only winning opening", 18/36, 9 routes and 2 collections, the unique change-walks, the three splits, and the reachable set. All ten guide figures match the student boards. The problems below change no answer.

### 1. Grades 2–3 Problem 4: the key gives one of 16 answers as if it were the answer (guide p. 6)

- **Quoted text:** "Upper board: add D to G. Three routes are s-A-D-E-G-H-t, s-B-D-G-I-t, and s-C-D-F-G-J-t."
- **Evidence:** every arrow from {A,B,C,D} to {G,H,I,J} gives three routes: 16 in all (`solve.out`). For example, A to H gives s-A-H-t, s-B-D-E-G-I-t and s-C-D-F-G-J-t. A new arrow helps exactly when it goes from the start side of all four two-arrow closures ({s,A,B,C,D}) to the finish side of all four ({G,H,I,J,t}). An adult holding only "add D to G" may doubt a child's correct A→H, which is a natural bypass along the top.
- **Smallest fix:** "Upper board: any new arrow from A, B, C or D to G, H, I or J works (16 choices); it must jump past both two-arrow bottlenecks. With D to G, three routes are…"

### 2. Grades 4–5 Problem 4: the key does not warn that two of the five smallest closures cannot work (guide p. 8)

- **Quoted text:** "Close AC and BD. This is a minimum two-arrow set… The route s-A-C-B-D-t uses both AC and BD."
- **Evidence:** the board has five minimum closures. A route uses two arrows of {sB,AC} (s-B-A-C-t), of {AC,BD} (s-A-C-B-D-t) and of {AC,Dt} (s-A-C-D-t). No route uses both arrows of {sA,sB} or of {Ct,Dt}, because a route leaves Start and enters Finish only once. {sA,sB} is the closure a child is most likely to find first, and the guide itself uses "two Start arrows" as the certificate on other boards. A child who starts there cannot complete the task, and the key gives the adult no way to see why.
- **Smallest fix:** add: "There are five smallest sets: {sA,sB}, {sB,AC}, {AC,BD}, {AC,Dt}, {Ct,Dt}. Only the middle three are used twice by one route (s-B-A-C-t, s-A-C-B-D-t, s-A-C-D-t). If a child chose the two Start or the two Finish arrows, ask for a different smallest set. The answer to the question is always no."

### 3. Problem 7 drawing proof: the token count skips the step that proves it (guide p. 10)

- **Quoted text:** "give each reserved arrow one token at its tail and one matching token at its head. Cancel pairs at internal dots. Only the k departures from Start and the outward boundary crossings survive."
- **Evidence:** the argument needs one total counted two ways. Counted dot by dot over S, only Start's k departures survive. Counted arrow by arrow, only arrows crossing the boundary leave an unmatched token in S. The paragraph merges the two counts into one sentence, and the "survivors" it names are not what either count leaves. As written, it does not show that k equals the number of outward arrows. (The algebraic paragraph above it is correct.)
- **Smallest fix:** "Put a + token at the tail and a − token at the head of each reserved arrow, and total the tokens on the dots of S. Dot by dot: each internal dot has as many + as −, and Start has k +, so the total is k. Arrow by arrow: an arrow inside S gives + and −; an arrow leaving S gives one +; an arrow entering S would give one −, but none is reserved. So k is the number of arrows leaving S, all of them reserved."

### 4. K–1 Problem 5: wrong page reference (guide p. 5)

- **Quoted text:** "The final page has a large working board and eight small recording copies."
- **Evidence:** the large bowtie and the eight copies are on K–1 page 5. The final page, page 6, is the closing game (Problem 6).
- **Smallest fix:** "K–1 page 5 has a large working board and eight small recording copies."

## Return visit

**Problems 1 and 3 and the companion guide check out.**

- **P1:** hub board: 2 edge-disjoint routes, 1 internally vertex-disjoint route (every route passes through H). With A→C added: 2 and 2. The guide's three-branch hub extension needs 3 arrows to block but only 1 dot.
- **P3:** route types S-A-T, S-A-C-T and S-B-C-T. With C→T = 3 the maximum is 4, reached by the multiplicities (2,1,1) and (1,1,2). The unique minimum cut is {C→T, A→T} = 4. With C→T = 4 the maximum is 5, reached only by one S-A-T, two S-A-C-T and two S-B-C-T. Five cuts have value 5.
- **Guide:** "P-A-X and Q-B-Y", "P→Y and Q→X both require the single arrow C→D", and "A→Y suffices… B→X works symmetrically" are correct (22 one-arrow additions work in all).

### 5. Return visit Problem 2: the last map's task has only one answer, the pairing already done on the first map (p. 2)

- **Quoted text:** "On the last map, choose two different finishes for P and Q so that both routes fit."
- **Evidence:** with finishes X and Y, the only assignments are P→X, Q→Y (map 1, fits) and P→Y, Q→X (map 2, impossible). The third map's only answer copies map 1. If "finishes" may be any dot, 18 ordered choices fit, most of them trivial (P→A, Q→B). Either way the task adds nothing. The guide's intended point, "If the endpoints can be reassigned, two routes fit again", is already shown by map 1.
- **Smallest fix:** replace the sentence with the guide's extension: "On the last map, draw one new arrow so that P→Y and Q→X both fit." In the guide, note that many arrows work (A→Y, B→X, A→D, C→Y, …).

## Notes (not counted)

- Guide p. 11: "K-1 can find every preserving closure (P4-5)". P5 asks for closures that *stop* every route, not ones that preserve two routes.
- Guide p. 6, 2–3 P2: "close DE and DF (or EG and FG)" omits the mixed minimum closures {DE,FG} and {DF,EG}. It is offered as an example, so nothing is wrong.
- The guide figures are rescaled (the diamond is 6.1 × 0.6 in, against 5.5 × 1.7 in on the student page), so letters sit at the same relative positions, not "exactly the same positions". The graphs are identical.
- In 70–80 dpi renders, C→D on the 4–5 P3/P4 board looks thicker. The vector width is 0.95 pt like every other arrow, and the board renders evenly at 300 dpi.
- Physical marker fit was not checked. The shortest full-size edge is 26 mm centre to centre on the bottleneck board, which leaves about 22 mm of visible shaft for a 15–20 mm marker.
