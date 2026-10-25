# Review: Week 62 return visit draft (W62-RV-K-v1, W62-RV-M-v1, W62-RV-U-v1)

Reviewer stage. I rendered every page of all three PDFs at 80 and 200 dpi and looked at each one (K–1 6 pages, grades 2–3 10 pages, grades 4–5 9 pages). I read `draft/src/` (gen.py, draw.py, nets.py, instances.py, mathlib.py and the .tex files). I recompiled the .tex copies in a scratch folder: they compile cleanly with no overfull or underfull boxes and the same page counts. I also checked every printed instance with my own brute-force script, which does not use the author's `mathlib.py`. I did not edit the draft.

## Verdict

The packet is mathematically sound and mostly close to the organizer's standard. The headers and footers are right, there are no Name or Date fields, titles, encouragement or hints, problems are numbered consecutively, and a non-task worked visual comes before each of the three new conventions. The bands cover the outline's kernels in a sensible order, and the 4–5 pairing of "six cards can fail" with "five cards and trees never fail" is excellent.

Four problems should be fixed before the organizer sees the packet:

1. Three move boards are impossible but are worded as commands.
2. No page connects the printed numerals to the coloured counters.
3. In the 4–5 move section, the subtle obstruction comes before the simple one.
4. Grades 2–3 Problem 4 is very likely a dead end.

There are also several medium layout and wording issues, listed below.

## 1. Mathematical verification (all correct)

I checked each claim independently. Every printed instance matches its intended answer, and every rendered diagram matches its source: I checked every edge, every allowed-slot label and every arrow direction against `instances.py` on the rendered pages.

- **K–1 Problems 1–3:**
  - P1: all four puzzles have one solution each (A2 B3 C1; A2 B1 C3; A3 B1 C2 D1; A1 B2 C1 D3).
  - P2: the triangle with all {1,2} and the path A{1} B{1,2} C{2} are impossible. The square with all {1,2} has 2 solutions; the four-card path has 1.
  - P3: the six-ring has the single solution A1 B2 C3 D1 E2 F3. The A/B–C, D, E network is impossible because A's three neighbours are forced to 1, 2 and 3.
- **Grades 2–3 Problems 1–3:**
  - The tree has the single solution A4 B3 C1 D1 E4 F3 G2 H2.
  - The six-ring with leaves is impossible: the forced chain from G and H collides at F and A.
  - Rings: the five-ring with all {1,2} fails; with C{1,3} it works (2 solutions); the six-ring with all {1,2} works; the five-ring with all {2,3} and leaf F{1,3} fails.
  - Six cards: A12 B34 C13 D14 E23 F24 fails. With F34 it works (2 solutions).
- **"Can you make it fail" boards** (2–3 P4, 4–5 P2–P3): no two-number assignment from 1–4 fails:
  - A/B–C, D, E: 0 of 7,776 fail.
  - Tree AB BC AD BE CF: 0 of 46,656.
  - Tree HA HB BC HD DE DF FG: 0 of 1,679,616 (the author's count; I did not rerun this one).
  - For contrast, the six-card network has exactly 144 failing assignments of 46,656.
- **4–5 Problem 4:** the five-ring with all {1,2} fails. The other three boards work (6, 2 and 2 solutions).
- **Fewest moves:**
  - A–B with 2 counters is unreachable; with 3 counters it takes 3.
  - A–B–C takes 4; A–B–C–D takes 6.
  - The star takes 7; the square 1212 to 2121 with 3 counters takes 6.
  - The triangle with 3 counters is unreachable; with 4 it takes 4 (A4 C1 B3 A2).
  - Five-ring with 3 counters: Goal 1 takes 5 (E3 D2 C1 B3 A2). Goal 2 is unreachable: the start has 4 ups and Goal 2 has 1 up.
  - Five-ring with 4 counters: Goal 2 takes 4 (B4 C2 B3 E3).
- **Stuck rings with 3 counters:** rings of 3 and 6 have 6 stuck placements each; rings of 4, 5, 7 and 8 have none. With 4 counters, every ring from 3 to 8 is one connected family.
- **Arrows:**
  - The Problem 9 (2–3) and Problem 8 (4–5) instance needs 4 headers: longest path A, B, C, D; earliest placement A E F G | B H | C | D.
  - The circle A→B→C→A has no schedule.
  - The chain of five needs 5.
  - The layered network needs 4; adding E→D makes it need 5.
  - 4–5 Problem 9: the first network needs 4; adding E→C makes it need 5 (path G, D, E, C, F).
  - Pointing every line: the five-ring with leaf needs at least 3; the six-ring with two leaves can get down to 2.

No mathematical fixes are needed. Problems that ask for an explanation have honest, age-reachable explanations:

- six cards: four joint choices for A and B, each blocked by one of C–F;
- the five-card network: if A and B share a slot, use it; otherwise only 3 of the 4 joint choices can be blocked;
- trees: work outward from any card;
- the ring rule: start between two neighbours with different lists;
- stuck rings: the colours must repeat 1, 2, 3 around the ring;
- 4 counters free any ring: fix cards one at a time, and the unfixed neighbour has a spare number;
- the longest arrow path.

## 2. High-priority issues

### 2a. Impossible move tasks are worded as commands (K–1 P4 and P8, 2–3 P7)

- K–1 Problem 4, first board (A–B, counters 1 and 2), and Problem 8, first board (triangle, counters 1, 2 and 3): "Match Start, then change it into Goal one move at a time, using only the counters shown."
- Grades 2–3 Problem 7, first board (triangle, counters 1, 2 and 3): "Using only the counters shown, change Start into Goal in as few moves as you can. Write your moves."

On each of these boards, no counter can move at all, so the instruction cannot be carried out. The page gives no permission to answer "it can't be done", and on 2–3 Problem 7 a "Moves:" line asks for a move word that does not exist.

This matters most at the K–1 table, where the adult is a parent volunteer, not a mathematician. Children told to do something impossible are likely to conclude they are doing it wrong, which is the failure mode of the lamp session. The contrast between the two boards ("a spare counter is a parking place") is the point of these problems, so the wording should present impossibility as a legitimate finding. K–1 Problem 2 already does this well ("Some of these can't be done.").

Suggested wording:
- K–1 P4 and P8: "Set up Start. Can you change it into Goal one move at a time, using only the counters shown?"
- 2–3 P7: "Using only the counters shown, can you change Start into Goal? Write your moves."

4–5 Problem 5 already gets this right ("Which goals can you reach? … For a goal you can't reach, explain why.").

### 2b. No page connects numbers to counter colours (all bands; most serious for K–1)

The kit's counters are coloured and carry no numerals. A number is linked to a colour only by the key counter in each header's dashed circle, and the outline lists "matching numerals 1–4 to the headers' key counters" as a K–1 prerequisite.

The draft draws counters as grey discs with numerals: in the list demo, in the "Counters ①②③" rows, and as numbers in the Start/Goal copies. The headers do not appear until the arrow rules (2–3 page 9, 4–5 page 7), and never appear in the K–1 packet. So the opening rules ("Put one counter on each circle. Two circles joined by a line must not have the same number. The numbers next to a circle show which counters it may have.") refer to counter numbers that the child cannot read off a counter. The outline requires the K–1 packet to work on its own after a normal launch, and without a key it depends on the launch and on the adult remembering to lay out the headers.

Fix: add one short clause to the opening rules of each packet, without naming colours, for example "The headers show which colour goes with each number." Also draw the four header cards, each with its dashed key circle and numeral, as the first panel of the list demo. The arrow demo already contains a header drawing that can be reused. The move rules ("A move changes one counter to a different number") depend on the same key.

### 2c. 4–5 move section: trapped comes before stuck, with no concrete entry (4–5 P5 and P6)

The first move problem in the 4–5 packet (Problem 5) asks children to reach one goal and explain why another is unreachable on the five-ring. The only explanation is the up-count invariant, the hardest idea in the packet. The simple obstruction, a placement where no counter can move (Problem 6, stuck rings), comes after it.

The outline's logic, and the guidance to give each idea concrete work before introducing a second obstruction, run the other way:
1. Meet stuck placements (rings of 3 and 6).
2. Learn that the five-ring has no stuck placement at all.
3. Then meet a five-ring goal that is unreachable even though some counter can always move.

Problem 6's answer for the five-ring is exactly what makes Problem 5 surprising. These children have also never made a single move before this page: the first visit had no moves.

Fix: swap Problems 5 and 6. Consider opening the move section with a quick concrete pair such as the triangle with counters 1–3 against 1–4, as in 2–3 Problem 7, so the 4–5 children handle the move rule before the invariant question. This adds at most half a page.

### 2d. Grades 2–3 Problem 4 has no reachable success and no defined end

"For each network, can you write two of the numbers 1, 2, 3, 4 next to every circle so that it can't be done?" Both networks (the A/B–C, D, E network and the tree AB BC AD BE CF) have zero failing assignments, so the answer is "no" for both. The problem does not ask for a reason, which is reasonable for grades 2–3, but that leaves no way to finish except "we tried and couldn't".

Problem 3 has just handed the children the failing six-card lists, so they never build a failure themselves. The outline's 2–3 emphasis, "the familiar five cards that never fail against the six that can", works better when the children produce the contrast.

Options, from smallest change to largest:
- Make the first board of Problem 4 a blank six-card network and the second the five-card network, keeping the same question. On the six-card network the child must rebuild the structure (A and B with no number in common, and C–F carrying the four mixed pairs), for example with A {3, 4}. The five-card network then fails to fail, by contrast.
- Move Problem 4 before Problem 3, so Problem 3's ready-made failing lists arrive as an answer.
- Drop the tree from the 2–3 packet. It adds a second futile hunt and its explanation, working outward, is a 4–5 idea. The 4–5 packet already has the trees.

## 3. Medium-priority issues

### 3a. 4–5 Problem 10's last question repeats a first-visit question

"Choose the arrows so that as few headers as possible are needed. On which network can two headers be enough? Explain." The children already know from the first visit that the five-ring with leaf needs 3 slots, the six-ring with leaves needs 2, and that two slots work exactly when there is no odd ring. The outline lists that rule among the base packet's questions to avoid repeating. As worded, a child can answer from memory ("the odd ring") without using arrows, and the new idea goes unasked: on every arrow choice, the number of headers equals the longest arrow path, and one good arrow choice reaches the conflict minimum.

Suggested rephrase, keeping both boards:

> Draw an arrowhead on every line so that the longest path along the arrows passes through as few cards as you can, then put the cards under headers to follow your arrows. On the first network, can you draw arrows so that no path along the arrows passes through three cards? Explain.

### 3b. K–1 Problem 4: Start/Goal copies sit next to the wrong network (K–1 page 4)

The two A–B boards are in one row. Board 1's Start/Goal copies are about 12 mm to the right of their own network but only about 5–6 mm from board 2's circle A. (From gen.py: `bx = x1 + 12`, and `row()` spreads two boards of about 89 mm each across 189 mm, so the gaps are about 3.7 mm plus padding.) When you look at the page, it reads as Start/Goal, then a network, then Start/Goal. The two boards use different counter rows, so the pairing matters to a K–1 child.

Fix: stack the two boards vertically as on K–1 page 6, or put both Start/Goal pairs to the right of their networks with a clear gap between boards.

### 3c. "Move" invites sliding counters between circles (all bands; unpiloted hypothesis)

"A move changes one counter to a different number." With physical counters, "move" naturally means picking a counter up and putting it on another circle, which would make swapping two circles' counters look like one move. Nothing in the materials enforces the one-card rule; only the partner does. That is the same weakness that sank the lamp session.

A wording that describes the physical action would help: "A move takes one counter off a circle and puts a counter with a different number there." The outline's own phrasing is "one move swaps one counter". This is a reviewer hypothesis, not observed behaviour.

### 3d. K–1 "Match Start" is unclear when read aloud

K–1 Problems 4–8 all begin "Match Start". Grades 2–3 Problem 5 says "Set up Start", which is clearer. Use "Set up Start" or "Make your network look like Start" in the K–1 packet as well.

### 3e. K–1 "Moves" box has no defined use (K–1 P5–P7)

K–1 children cannot write a move word, so the box could only hold a tally or a number. Either way it forces them to keep a running count while moving counters, which is the concurrent bookkeeping the project guidance asks us to avoid. Either drop the box and let the adult count, or keep it and leave its use to the adult; the second option needs no page text. Problems 4 and 8 have no box, which is fine.

## 4. Low-priority wording and standards points

- **4–5 Problem 4:** "A ring of any size has two numbers next to every circle." reads as a statement of fact. Suggest "Suppose every circle of a ring, of any size, has two numbers next to it. When can it not be done? Explain."
- **4–5 Problem 4, evidence:** only one of the four boards fails. A child testing the conjecture "odd and all the same" has nowhere to try new lists except by rewriting the printed ones. One blank five-ring or seven-ring, labelled as extra workspace, would help; this is optional.
- **4–5 Problem 7:** "every placement of counters on a ring" should be "on a ring of any size", to parallel Problem 4 and make the scope clear.
- **4–5, "Explain" on all ten problems:** most are warranted (impossibility, completeness, invariants). Problem 9's explanation repeats Problem 8's (a path through five cards), so its "Explain" could go. The standard asks for explanations only where they are the point, and the organizer may trim this.
- **K–1 Problems 1–3:** each begins "Put a counter on every circle.", restating the opening rule. That is tolerable for read-aloud, but Problem 2 runs to three sentences; the K–1 limit is one or two. Possible fix: "Some of these can't be done. Find them and show why."
- **Mid-packet rule paragraphs:** the move rules (K–1 page 4, 2–3 page 5, 4–5 page 4) and arrow rules (2–3 page 9, 4–5 page 7) are unnumbered rule blocks in the middle of the packet. The organizer's standard says rules go once at the top of the first page. These rules are not packet-wide, though, and the outline requires a worked visual before first use, so this placement is defensible. Flag it for the organizer rather than change it.
- **Move rules (2–3 and 4–5):** "Write a move as the card's letter and its new number" should say "circle's letter". Move tasks use counters on the mat, and cards are optional.
- **2–3 Problem 10:** "Which of these can be put under the four headers?" is vaguer than 4–5 Problem 9's "Can the cards of each network be put under the four headers?". Use the clearer wording.
- **Arrow rules:** children both put cards under headers and put a counter on each circle. That doubles the placement work, but it is the base kit's checking method: the partner reads each arrow's two counters. Keep it; the facilitator guide should say why.
- **K–1 move demo:** the changed circle D is marked only by a thicker outline. That is easy for a five-year-old to miss, but the adult will point to it. Optional: a small mark or shading on D.

## 5. Coverage against the outline (nothing missing)

- **K–1:** forced chains (P1); impossibility with "show why" (P2, and P3's three-line obstruction); fewest moves on A–B, the three-card path and the star, plus the square (P5–P7); the spare counter as a parking place (P4 and P8). Six pages and 17 boards is adequate for 35–40 minutes at a K–1 pace.
- **Grades 2–3:** forced chains (P1); lists changed on an odd ring (P2); six cards against five (P3–P4, see 2d); fewest-move swaps (P5–P7); stuck rings (P8); arrows as a continuation (P9–P10).
- **Grades 4–5:**
  - why the six cards fail (P1);
  - why the five cards and trees never fail (P2–P3);
  - the ring rule (P4);
  - the trapped five-ring (P5);
  - stuck rings (P6);
  - 4 counters free any ring (P7);
  - earliest placement against the longest path (P8–P9);
  - arrows on conflict networks (P10, see 3a).
- **Physical constraints:**
  - working circles are 20 mm (R_FULL = 10 mm, no scaling) with lines centre to centre;
  - slot labels sit just outside circles and clear of lines (checked at 200 dpi on every board);
  - arrowheads are mid-line;
  - every network uses at most eight cards, A–H, each letter once;
  - lists come from 1–4, and moves use at most 4 counters;
  - five-card arrow paths are used as the impossibility;
  - slots are given as numbers, never colour names;
  - regular polygons are drawn at equal scale.
- **Base week:** no question repeats the base packet except the end of 4–5 P10 (3a).

## 6. Keep these when revising

- All the instances: each is verified and well chosen. Examples are the K–1 P3 obstruction (A's three single-number neighbours), the 2–3 P1 forced loop that collides at F and A, the 4–5 P5 Goal 2 that looks only three cards away from Start, and the 4–5 P9 pair that differ by a single arrow.
- The three non-task demos: the A–B list demo, the paw network move demo with the move word D1, and the A→B, A→C arrow demo bridging from cards under headers to counters on the circles.
- The 4–5 opening sequence: six cards fail, then five cards and the tree never fail, with explanations.
- The light record: a single move word on one "Moves:" line.

Physical handling is unrehearsed, as in the base week. That covers counter fit inside sleeves, children sharing two sleeves per kit, and whether a partner checks each move. Mark it as untested when the packet is moved into the year-2 folder.
