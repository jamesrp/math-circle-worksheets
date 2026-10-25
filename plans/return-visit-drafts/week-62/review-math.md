# Week 62 return visit: mathematical review of the draft

Reviewer: independent math check (CRITIC-MATH stage). Draft: `draft/k-1.pdf` (6 pp.), `draft/grades-2-3.pdf` (10 pp.), `draft/grades-4-5.pdf` (9 pp.).

## How I checked

I wrote my own parser for the generated TikZ in `draft/src/*.tex`. It reads circles, centre-to-centre lines, mid-line arrows, allowed-slot labels (each tied to its circle by the anchor geometry), the numbers in the compact Start/Goal copies (K–1 copies have no letters, so I matched them to the full-size network by shape) and the "Counters" keys. I did not import the author's `mathlib.py` or `instances.py`. From that data I solved every printed task with separate brute-force code:

- every allowed-slot puzzle, by backtracking over all solutions;
- every move task, by breadth-first search over legal placements with 2, 3 and 4 counters;
- every arrow board, by trying all header assignments for the fewest headers, plus the longest arrow path;
- the "can you make it fail" boards, over every assignment of two numbers from 1–4: 7,776 for A, B joined to C, D, E; 46,656 for tree AB BC AD BE CF; 1,679,616 for tree HA HB BC HD DE DF FG;
- stuck placements and move families on rings of 3–8;
- the two-number ring rule on rings of 3–7;
- all orientations of the five-ring with leaf (64) and the six-ring with two leaves (256).

I also checked label placement: every allowed-slot label sits 0.4–1.4 mm from its own circle, at least 7 mm from any other circle and at least 5.7 mm from every line. Every diagram matches its intended network, lists, states and arrow directions. All printed Start and Goal placements are legal, and no board needs more than 8 counters of one number.

Every intended answer is correct. The four problems below come from wording: each is a reading under which the page asks for something impossible without saying so, or a reading that a shortcut trivializes.

## Located problems

### 1. K–1, page 4, Problem 4 (left board): impossible task worded as if possible

- **Text:** "Problem 4: Match Start, then change it into Goal one move at a time, using only the counters shown." The left board is A–B with Start A1 B2, Goal A2 B1 and the key "Counters 1 2".
- **Evidence:** With only counters 1 and 2, the Start placement has no legal move. A cannot become 2 because B is 2, and B cannot become 1 because A is 1. My search finds no route. The right board (counters 1–3) takes 3 moves: A3 B1 A2.
- **Why it matters:** The contrast with the right board is the point of the problem. But the sentence is an instruction that assumes success, and children and a non-mathematician adult get no signal that one board cannot be done. Problems 2 and 3 in the same packet do give that signal ("Some of these can't be done", "If one can't be done").
- **Smallest fix:** Add "If it can't be done, show why." to Problem 4.

### 2. K–1, page 6, Problem 8 (top board): same issue

- **Text:** "Problem 8: Match Start, then change it into Goal one move at a time, using only the counters shown." The top board is the triangle with Start A1 B2 C3, Goal A2 B3 C1 and the key "Counters 1 2 3".
- **Evidence:** With three counters on a triangle, all 6 legal placements are stuck, so the Goal cannot be reached. With counters 1–4 (bottom board) it takes 4 moves: A4 C1 B3 A2.
- **Smallest fix:** Add "If it can't be done, show why." to Problem 8.

### 3. Grades 2–3, page 7, Problem 7 (top board): "as few moves as you can" when no route exists

- **Text:** "Problem 7: Using only the counters shown, change Start into Goal in as few moves as you can. Write your moves." The top board is the triangle with A1 B2 C3 → A2 B3 C1 and "Counters 1 2 3".
- **Evidence:** Same as finding 2: every three-counter triangle placement is stuck, so there is no route. The bottom board (1–4) takes 4 moves (A4 C1 B3 A2), and 4 is the minimum.
- **Smallest fix:** "Using only the counters shown, change Start into Goal in as few moves as you can, or explain why it can't be done. Write your moves."

### 4. Grades 2–3, page 8, Problem 8, and grades 4–5, page 5, Problem 6 (also page 6, Problem 7, second question): illegal placements trivialize "no counter can move"

- **Text:** "Use counters 1, 2 and 3. On which of these rings can you place counters so that no counter can move?" The 4–5 version adds "Explain." The boards are rings of 4, 5, 6 and 7.
- **Intended answer (correct):** If placements must follow the rules, only the six-ring has a stuck placement (6 of them, for example A1 B2 C3 D1 E2 F3). Rings of 4, 5 and 7 have none. I confirmed this for rings of 3–8: stuck placements exist only for lengths 3 and 6.
- **Evidence for the other reading:** These problems never say the placement must have different numbers at the two ends of every line. The moves rule on page 5 of the 2–3 packet and page 4 of the 4–5 packet says only "After every move, no line may have the same number at both ends." Placing a 1 on every circle freezes any ring: one move fixes at most the two lines at one circle, so no single move ends legal. My count of such frozen illegal placements with counters 1–3 is 15 on the four-ring, 93 on the five-ring, 375 on the six-ring and 1,389 on the seven-ring. Under this reading the answer becomes "all four rings", and the multiple-of-3 idea disappears.
- **The same gap in 4–5 Problem 7:** The second question, "With counters 1, 2, 3, 4, can every placement of counters on a ring be changed into every other one?", is true only for legal placements. I confirmed one family on rings of 3–8 with four counters. An all-1 placement still cannot move.
- **Smallest fix:** In 2–3 Problem 8 and 4–5 Problem 6, write "place counters, with different numbers at the two ends of every line, so that no counter can move". Alternatively, put that condition into the shared moves rule once: "Start from a placement with different numbers at the two ends of every line. After every move, that must still be true." Either version also covers 4–5 Problem 7.

## Checked and correct (no change needed)

- **K–1**
  - P1: all four boards have exactly one solution (A2 B3 C1; A2 B1 C3; A3 B1 C2 D1; A1 B2 C1 D3).
  - P2: the triangle with every list {1, 2} and the path A{1} B{1, 2} C{2} are impossible. The square with every list {1, 2} has 2 solutions, and path A–D has exactly one (A1 B2 C3 D1).
  - P3: the six-ring has exactly one solution (A1 B2 C3 D1 E2 F3). The second board is impossible because A touches 1, 2 and 3.
  - P5–P7: fewest moves are 4, 7 and 6. These answers are the same whether or not counter 4 is used, so leaving "using only the counters shown" out of these problems changes nothing.
- **Grades 2–3**
  - P1: the tree has exactly one, fully forced solution (A4 B3 C1 D1 E4 F3 G2 H2). The six-ring with leaves is impossible: G and H force A1 B2 C3 D2, which leaves F no number.
  - P2: the five-ring with every list {1, 2} is impossible; with C {1, 3} it can be done. The six-ring with every list {1, 2} can be done. The five-ring with leaf is impossible because its odd ring has every list {2, 3}.
  - P3: the first lists cannot be done; the second can (A2 B4 C1 or C3, D1, E3, F3). Of all 46,656 two-number lists, 144 fail.
  - P4: the answer is no for both networks, since 0 assignments fail on each.
  - P5 and P6: fewest moves are 3, 4, 6 and 7.
  - P9: 4 headers, needed because of the path A, B, C, D.
  - P10: only the third board fits four headers. The others are a circle, a path through 5 cards and a path B, E, D, F, G through 5 cards.
- **Grades 4–5**
  - P1: matches 2–3 P3.
  - P2 and P3: the answer is no for both networks, since 0 assignments fail on each.
  - P4: impossible / possible (6 solutions) / possible / possible. The stated ring rule is right: on rings of 3–7, the failing two-number lists are exactly the 6 in which an odd ring has the same pair everywhere.
  - P5: Goal 1 is reachable in 5 moves (E3 D2 C1 B3 A2). Goal 2 cannot be reached. Using the up-count, Start and Goal 1 have 4 ups and Goal 2 has 1; the 30 five-ring placements split into two families of 15, and every placement has a movable counter.
  - P7: 4 moves (B4 C2 B3 E3), and 4 is the minimum.
  - P8: 4 headers.
  - P9: the first network fits (its longest path has 4 cards); the second does not (G, D, E, C, F has 5).
  - P10: the five-ring with leaf needs at least 3. Its 64 orientations give longest paths of 3 (16), 4 (20), 5 (20) and 6 (4), and 4 contain a circle. The six-ring with two leaves can be done with 2, in 2 of its 256 orientations.
