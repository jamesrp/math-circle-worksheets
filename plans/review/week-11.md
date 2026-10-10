# Week 11: Chip firing with a sink

**Verdict: keep.** There is no must. Every answer checks, every band reaches the abelian property by experiment, and 4–5 can prove it. The fixes are wording, tables and a partner routine.

Reviewed October 10, 2026 by Claude, with the math check in [week-11-math.md](week-11-math.md). Packets: week-11-k-1.pdf (F11-K-v3, 6 pp.), week-11-grades-2-3.pdf (F11-23-v3, 6 pp.), week-11-grades-4-5.pdf (F11-45-v3, 6 pp.). Adult guide: week-11-facilitator.pdf (12 pp.). Companions noticed but not reviewed: week-11-return-visit.pdf (F11-RV-v1, 3 pp.) and its guide. Status: unpiloted (guide footers, source README); revised October 4.

## The mathematics

A circle holding one chip per line sends one along each; the sink only receives. With a sink every run stops, and every complete run from a start ends with the same piles and the same share counts. Children test this on three boards (every band's P1, K–1 P3, 2–3 P2 and P4, 4–5 P4), find stable placements and their capacity (K–1 P4), work backwards from a finish (K–1 P2, 2–3 P3), and see one-chip additions cycle through three states while the empty board never returns and two states merge (K–1 P6, 2–3 P6, 4–5 P3). 4–5 proves termination with a score (P5) and order independence (P6). A mathematician would enjoy it: this is the abelian sandpile.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A real theorem with its hypothesis (the sink), two proofs within reach, capacity and a transient state. |
| Problems | strong | Many runs per problem (11 starts in K–1 P2, 24 additions in 2–3 P6). 4–5 tests order on two boards (P1, P4) before proving it (P6). 2–3 spends P1, P2 and P4 on one question (fix 10). |
| Student pages | adequate | Right headers and footers, one problem per page, no slop. Two K–1 tables have one row per start under an order question (fix 1); K–1 P4's rows give a count away (fix 2); 2–3 P4 and P5 lack a question or trial labels (fixes 4, 5). |
| Concreteness | adequate | Chips carry the state. Guide p. 4 launches on (2, 2) and gives every child one move. Only the child checks "one chip along each line"; the mover-recorder routine is a 2–3 hint (p. 8). Counter fit on 44 mm circles is unrehearsed (p. 4). |
| Correctness | strong | math.md: 259 checks of pages and guides, no mismatch, three wordings (fixes 2, 3, 7). |
| Adult guide | strong | Theorem-first overview with assumptions and limits (pp. 1–3), launch and menu (p. 4), all 18 keys with hints, the score and quota arguments (p. 11). |
| Age fit, K–1 | adequate | Starts are drawn as dots, every K–1 circle has two lines, and the adult reads and scribes. Scribing and checking moves for two pairs is a load (a prediction); P5's "sharing whenever you choose" is abstract. |
| Age fit, grades 2–3 | strong | Totals to 12, a running letter word, and one explanation (P3, where completeness is the point). |
| Age fit, grades 4–5 | strong | P1–P4 are experiments; P5–P6 are real proofs, late, with the organizer and the guide's routes. |

## Keep

- One running sharing word plus final piles, letters counted afterwards (all bands).
- Duplicated start rows in 2–3 and 4–5, and "if possible" where (4, 0) has only AAB.
- 4–5 P1's "For the same start, can the final piles agree while the sharing counts differ?"
- K–1 P4's "Can any of these ways use 4 chips?": an impossibility a kindergartner can explain.
- K–1 P2 and 2–3 P3 (fixed totals, the inverse), and 4–5 P3 (return and merging).
- The three boards, and guide pp. 1–4.

## Fix

1. **should**, K–1 P1 and P3 (pp. 1, 3): one row per start under "Can choosing a different order leave different piles?" P1's four starts finish at three different piles, so a child who runs each once can answer yes about order. Print each start twice, as in 2–3 P1.
2. **should**, K–1 P4 (p. 4): eight answer rows give the count away, and the eighth is the empty board, which "put chips on" may exclude (math.md item 1, agreed; the giveaway is mine). Print ten rows; add to the guide hint "If a child stops at seven, ask whether a board with no chips counts."
3. **should**, K–1 P6 (p. 6): "Can you ever get empty circles again?" One circle is empty in eight of eleven rows, so "an empty circle" gives yes (math.md item 2, agreed). Not a must: "again" points back to the start's two empty circles, and the key fits that reading. Write "Can both circles ever be empty again?"
4. **should**, 2–3 P4 (p. 4): "Finish each start. Find another order wherever a choice is possible. After stopping, compare the final piles and count each letter in the sharing words." No question. End with 4–5 P4's "Does the extra line change your conclusion about order?"
5. **should**, 2–3 P5 (p. 5): three identical rows "2 | 4" for three timings joined by "or"; a child may add both batches together three times. Add 4–5 P2's Timing column.
6. **should**, guide p. 4 launch: make the 2–3 P1 hint the routine at every table: one child moves, the partner touches each line from the sharing circle and says its letter, swap each start. Nothing else catches a single chip sent (a prediction, from the Week 2 lamp session).
7. **could**, guide p. 8, 2–3 P3 invariant: add "A start with chips never finishes empty, because the last share leaves a chip on the other circle." (math.md item 3.)
8. **could**, 5.4–6 mm rows in 2–3 P4 and P6 and 4–5 P1 are cramped for words; take 7 mm from the board margins.
9. **could**, p. 1 of each band: swap "A → AB → ABA" for the return visit's Before / A fires / After panel.
10. **could**, 2–3 P4 asks about order a third time; the extra-line capacity question (guide p. 12: at most 5 chips) would add an idea.
11. **could**, "End A" (2–3 P2, P4; 4–5 P4) against "Finish A" elsewhere.
12. **could**, the return visit says "fire" where the base pages say "share".

## Overlaps

Week 39 (road detours) and Week 27's Extension A reach a finish independent of order on other objects; cross-reference them. Week 20 uses anchored graphs for the maximum principle; Weeks 3 and 49 iterate a map until it cycles. No merge.

## App fit

Fit A, confirmed: shipped as 12 puzzles and a playground. Only ready circles glow and illegal taps are refused, closing the concreteness gap above. The inverse puzzles (5, 9, from 2–3 P3), the biggest avalanche (7), the most firings with W = 3A + 4B + 3C as certificate (10, from 4–5 P5) and the loop (12) are click-to-solve and checkable.

Against the worksheet:

- The add-one cycle (K–1 P6, 2–3 P6, 4–5 P3), the theme's sandpile-group content, is no puzzle. Ask for every still board that returns when you keep adding at A, or two that merge: (0, 0) and (1, 1) both go to (1, 0).
- Capacity (K–1 P4) is no puzzle. Place the most chips with nothing glowing on the square with a diagonal (5); certificate: each circle holds at most one fewer than its lines. That board is otherwise only in the playground.
- Five of twelve puzzles enumerate firing orders, one idea. Batch timing (K–1 P5) is a prediction; leave it to the playground.
- Every "find every" puzzle shows one empty slot per answer, giving the count away, as Track C says. Let the child claim "done" and the app check.
- Puzzle 4's grown-up note says "three chips reach the sink"; from 2, 1, 2 only A and C reach it, once each: two (scripts/build-chips.mjs, line 98).
- The themes.md row says children find "every stable state"; no puzzle asks for it.

**Decision, October 10, 2026.** In the app as Chip firing (PR #1). The wrong grown-up note for puzzle 4 is fixed on `main` (a880df6). Two puzzles join the family in Wave 9's touch-ups of in-app families: the add-one cycle (every still board that returns as chips are added at A, and two that merge) and capacity (the most chips with nothing glowing on the square with a diagonal). In the same pass the "find every" puzzles lose their answer slots and end in a "done" claim the app checks. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. The worksheets are unpiloted, and no child has played the app family (docs/chips/README.md).
