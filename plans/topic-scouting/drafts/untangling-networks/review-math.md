# Mathematical review: Untangling networks, draft v1

Reviewer: independent math check (CRITIC-MATH stage). The draft was not edited.

## How I checked

- **Sources and PDFs match.** I rebuilt `draft/src` in a scratch copy. The regenerated `gen/` files are byte-identical to the originals, and the text of all three PDFs is identical.
- **Tangled pictures.** I wrote my own parser for the dot centres and link segments in every `gen/pic_*.tex`. For each picture I checked:
  - the link list printed beside it;
  - the number of crossings;
  - whether the network is in one piece and whether it is planar;
  - the closest any link comes to a dot it does not belong to;
  - spacing between crossings, and between crossings and dots.
- **Portal boards.** I parsed the dot positions on each board in `gen/portal_*.tex`. A separate backtracking search of my own looked for a crossing-free drawing on the flat torus. Each link was a straight segment to one of the 9 translates of its far dot, with every contact checked against all translates. As controls, the search correctly fails for K5 inside the square with no portals, and for K8 on the torus.
- **The link-adding game.** I enumerated every connected plane map on 3 to 6 dots: all rotation systems of every connected planar graph with genus 0. A position has no legal move exactly when every region's dots are already pairwise joined. In every such position the number of links is 3n−6, for n = 3, 4, 5 and 6. A position in several pieces always has a legal move, because a link can join two pieces through a region they share. I got the same result for the reading where dots may be moved during play (maximal planar graphs).
- **Fewest crossings.** A random search over straight-line drawings found 1 crossing for K5, 1 for K3,3 and 3 for K6. These match the lower bounds from deleting one link per crossing: 10−9, 9−8 and 15−12.

## Located problems

### 1. Several links may cross at one place, so the fewest crossings for K6 is not 3 (grades 2–3 and 4–5)

- **Where:**
  - The shared opening rules on page 1 of both packets.
  - Grades 2–3, page 4, Problem 3: the box labelled "6 dots, each joined to every other dot".
  - Grades 4–5, page 5, Problem 6.
- **Text:**
  - Opening rules: "A crossing is a place where one link lies across another."
  - Grades 2–3, Problem 3: "Draw each of these networks with as few crossings as you can."
  - Grades 4–5, Problem 6: "Draw the network with 6 dots, each joined to every other dot, with as few crossings as you can. Explain why nobody can do better."
- **Evidence:** The rules count crossings by place and allow any number of links to pass through one place.
  - **The loophole drawing:** pick a point p in the middle and send every link from its first dot to p, then on to its second dot. Bend each link slightly so that links from the same dot meet only at that dot and at p.
  - **What it gives:** every pair of links then meets only at p (or at a shared dot). No link lies across a dot. So K6 is drawn with exactly one crossing place, and with pipe cleaners this is just a pile at one point.
  - **The intended answer:** the minimum is 3 only when each crossing involves exactly two links. The standard argument also needs this: delete one link per crossing, which leaves a crossing-free network on 6 dots with at most 12 links, so 15 − k ≤ 12 and k ≥ 3.
  - **What is unaffected:** the minima for K5 and K3,3 are 1 under either reading. So K–1 Problems 5–6 and the other two boxes in grades 2–3 Problem 3 are fine.
- **Smallest fix:** add one sentence to the shared opening rules in `shared-sort.tex`, after the definition of a crossing: "No more than two links may pass through the same place." Adding the same sentence to the K–1 opening rules is optional, for consistency.

### 2. The region rule fails for networks in more than one piece (grades 2–3 and 4–5)

- **Where:** grades 2–3, page 3, Problem 2, and grades 4–5, page 3, Problem 2. Both come from the shared `shared-sort.tex`.
- **Text:**
  - Opening rules: "A network is dots joined by links."
  - Problem 2: "Find a rule connecting the three numbers that works for every untangled network you can draw."
- **Evidence:** nothing on the page says a network must be in one piece. For an untangled network, dots − links + regions = 1 + the number of pieces. Two counterexamples a child could draw:
  - a triangle plus a lone dot: 4 dots, 3 links, 2 regions, so 4 − 3 + 2 = 3;
  - two separate triangles: 6 dots, 6 links, 3 regions, so 6 − 6 + 3 = 3.

  So no rule giving 2 "works for every untangled network you can draw". All six printed networks and the worked example are in one piece. The four that can be untangled give:

  | Network | Dots | Links | Regions |
  |---|---|---|---|
  | 1 | 5 | 7 | 4 |
  | 3 | 5 | 9 | 6 |
  | 4 | 6 | 9 | 5 |
  | 6 | 6 | 12 | 8 |

  Every row satisfies V − E + F = 2, so the intended discovery works from the page's own examples. Only the universal claim is false.
- **Smallest fix:** change the last sentence of Problem 2 to "Find a rule connecting the three numbers that works for every untangled network in one piece." Alternatively, add "in one piece" to the opening definition of a network. Later problems apply the rule only to K5 and K3,3, which are in one piece, so nothing else needs to change.

## Not errors, but worth knowing

- **The game result depends on every legal link being physically possible.** This is a hypothesis about the materials, not a computed result. Every finished game has 3n−6 links (verified above), but only if players can always add any legal link. In a finished position some links must go round the outside or round other dots. With 30 cm pipe cleaners and 5 cm dots spread out on a table, such a link may be too short. A game could then stop early and the tally would show inconsistent winners. Both opening rules allow moving dots, which avoids this if players use it. The pipe-cleaner version of the game has not been rehearsed.
- **The winner rule needs at least 3 dots.** In grades 4–5 Problem 3, "odd number of dots: first player wins" holds only from 3 dots up. With 2 dots there is 1 link, so the first player wins with an even count; with 1 dot the second player wins. The page asks only about 4, 5 and 6 dots, so nothing on the page is wrong.

## Problem-by-problem verification

### K–1 (5 pages): correct

| Problem | Intended outcome | Check |
|---|---|---|
| 1 (p. 1) | Untangle a 4-cycle (1 crossing drawn), K4 minus one link (1 crossing) and K4 drawn as a square with diagonals (1 crossing) | All planar. Link lists match the drawings. No link comes within 2.9 dot radii of a dot it does not belong to. |
| 2 (p. 2) | Untangle a 5-cycle drawn as a pentagram (5 crossings), and a fan: E joined to A, B, C, D, plus the path A–B–C–D (3 crossings) | Planar; lists match |
| 3 (p. 3) | Untangle a 6-cycle (5 crossings) and a triangular prism (4 crossings) | Planar; lists match |
| 4 (p. 4) | Two houses and three wells (K2,3) can be joined with no crossings | K2,3 is planar |
| 5 (p. 4) | Three houses and three wells: fewest crossings is 1 | Correct |
| 6 (p. 5) | All five of five dots (K5): fewest crossings is 1 | Correct; the picture and list are K5 |
| 7 (p. 5) | Link-adding game | The winner is fixed whatever the play: second player with 4 dots (6 moves), first player with 5 dots (9 moves). Verified by enumeration. |

### Grades 2–3 (6 pages): correct apart from items 1 and 2

| Problem | Intended outcome | Check |
|---|---|---|
| 1 (pp. 1–2) | Networks 2 and 5 stay stuck | 1: planar, V = 5, E = 7, F = 4. 2: K5. 3: K5 minus D–E, planar (5, 9, 6). 4: prism, planar (6, 9, 5). 5: K3,3 with parts ABC and DEF. 6: octahedron, K6 minus A–F, B–D, C–E, planar (6, 12, 8). Lists match. Clearance checked: links stay at least 2.4 dot radii from dots they do not belong to, and crossings at least 0.5 cm from one another. |
| 2 (p. 3) | V − E + F = 2 | The example is right: 4 dots, 5 links, 3 regions, and labels 1, 2, 3 sit in the two triangles and outside. See item 2. |
| 3 (p. 4) | Fewest crossings 1, 1, 3 | Correct with pairwise counting. See item 1 for the 6-dot box. |
| 4 (p. 5) | Second player wins with 4 dots, first with 5, second with 6 | Verified by enumeration |
| 5 (p. 5) | Explain why K5 cannot be untangled | True. Untangled, it would have 10 − 5 + 2 = 7 regions, needing at least 21 link-sides, but there are only 20. |
| 6 (p. 6) | K3,3 and K5 on the portal board with no crossings | Possible at the printed positions. My search found straight-link drawings using 4 and 6 portal crossings. The arrow marks give an untwisted torus. In the example, the exit and entry points match: 0.680 and 0.680 on the sides, 0.675 and 0.675 on the top and bottom. |

### Grades 4–5 (7 pages): correct apart from items 1 and 2

| Problem | Intended outcome | Check |
|---|---|---|
| 1–2 (pp. 1–3) | Same as grades 2–3 Problems 1–2 | Same shared pages; same findings. Item 2 applies. |
| 3 (p. 4) | Every finished game has 3n−6 links, so the parity of the number of dots decides the winner | Verified by enumeration for 4, 5 and 6 dots |
| 4 (p. 4) | Explain why K5 cannot be untangled | True (argument as above) |
| 5 (p. 5) | Explain why K3,3 cannot be untangled | True. It has no triangles, so each of the F = 9 − 6 + 2 = 5 regions needs at least 4 link-sides: at least 20, but there are only 18. |
| 6 (p. 5) | Fewest crossings for K6 is 3, with an explanation | A drawing with 3 crossings exists, and the bound 15 − 12 = 3 holds, but only with pairwise counting. See item 1. |
| 7 (p. 6) | K3,3 and K5 on the portal board | Possible at the printed positions (as in grades 2–3 Problem 6) |
| 8 (p. 7) | K6 and K7 on the portal board with no crossings | Possible at the printed positions. My search found straight-link drawings using 8 and 11 portal crossings. The K7 dots are the standard 7-point lattice, whose drawing fills the torus with triangles. The K6 board is the same lattice without G. |
