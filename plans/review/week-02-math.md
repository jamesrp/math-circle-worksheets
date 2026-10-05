# Week 2 (switches and lamps): math check

Math check for the Week 2 review card, October 5, 2026 (calibration run). I opened no use logs or session records.

**What I checked**
- Compact catalog `week-02-shared-catalog.pdf` (F02-S-CAT-v2, 4 pp., Problems 1–10).
- Upper catalog `week-02-shared-catalog-upper.pdf` (F02-S-CAT-UP-v1, 6 pp., Problems 1–6).
- The upper adult notes, `plans/week-02-catalog-upper.md`.
- For compact Problems 1–10, the archived shared guide `archive-before-deslopping/week-02-shared-facilitator.pdf` (F02-S-FAC-v1): its P2 and P5–P13 sections and the general claims that apply.
- The data in `plans/week-02-shared-data.json` and `plans/week-02-catalog-upper-data.json`, together with the two catalog builders.

**Scripts, in [checks/week-02/](checks/week-02/)**
- `extract.py` reads the vector drawings in both PDFs: lamps, lines, ON dots and arrows.
- `verify_diagrams.py` decodes every printed start→target pair and compares it with the data. It checks lines, ON sets, x/y scale and that the start and target are drawn at the same size.
- `solve.py` does my own BFS over all 2^n states and an enumeration of all edge subsets. It also replays every move list in both guides and checks the general rules on all states.
- `check_json.py` compares my enumeration with the exact edge sets the upper notes cite.
- `edge_cases.py` holds the counterexamples below.
- Saved outputs are `solve.out` and `extracted.json`. The page renders were not kept.

## Results by band

**Compact catalog (Problems 1–10): no wrong answers. Problems 4 and 5 below are minor.**

The diagrams match the data in all 19 printed pairs, with equal x/y scaling. The square, hexagon and grid are regular.

- **Reachable targets:** every "Make each target picture" target in P1, P2, P4, P5, P6 and P7 is reachable.
- **P3:** the six-move tour works.
- **P8:** the trip is impossible. Lamp 1 → lamp 5 crosses islands, and the left island's ON count would have to go from odd to zero.
- **P9:** all 16 possible single bridges between the islands make the trip possible.
- **Guide move lists:** every list in the archived guide for P2 and P5–P12 replays to the stated picture, and it keeps one light where the guide says so.

**Upper catalog (Problems 1–6): the mathematics is correct. Problem 2 below is a reading issue on pp. 3 and 6.**

All 26 printed pairs and the four Problem 5 rings match the data. Every figure has equal scaling, and the rings are regular (angular spread under 0.01°).

My own computations give these answers:

| Problem | My result |
|---|---|
| 1 | Possible, possible, impossible, possible, impossible, possible. On every one of these connected graphs, "reachable iff the ON-count parity matches" holds over all states. |
| 2 | Possible, impossible, possible, possible, impossible, possible. On all four graphs, "even change in every component" holds over all states. |
| 3 | Exactly two complementary sets in each case, with sizes 0/4, 2/3, 3/3 and 2/5. Checked on C3–C8 for all targets. |
| 4 | Minima 2, 4, 3, 5, 4, 4. |
| 5 | Ring records 2, 3, 3, 4, which is ⌊n/2⌋. Checked for n = 3–12. Lamps ⌊n/2⌋ apart attain it. |
| 6 | Solution counts 1, 1, 0, 1. On all four trees, each even target has exactly one set and each odd target has none. |

The edge sets in `week-02-catalog-upper-checks.json` that the notes cite all agree with my enumeration (26/26).

**Guides**
- Every stated answer, minimum, lower-bound argument, proof sketch and extension claim that I checked is true, with correct hypotheses. This covers the parity invariant, the component rule, path-pairing sufficiency, cycle complements, the tree leaf, cut and forest arguments, ⌊n/2⌋, and "complementing works iff every degree is even."
- The exceptions are Problems 1 and 3 below (wording), and Problem 4, where a guarantee no longer applies to the current prompt.

## Located problems (5, all minor; no incorrect answers)

### 1. Upper notes, Problem 6A: "upper" and "lower" branch points are at the same height
- **Where:** `plans/week-02-catalog-upper.md`, §6. The notes say: "A uses the two lines meeting the **upper branch point** on its left/top and the two lines meeting the **lower branch point** on its bottom/right; it omits the middle joining line."
- **Evidence:** in the printed tree (upper p. 6, A), the two branch lamps are at (144.7, 200.6) pt and (198.3, 200.6) pt. They are on the same row: one has a line going up, the other a line going down. The edge set the notes mean is {1-2, 2-3, 4-5, 4-6}, and that is correct; it is the unique solution by enumeration. But "upper" and "lower" don't pick out lamps in the picture.
- **Fix:** "A uses the left and top lines at the left branch point and the bottom and right lines at the right branch point; it omits the line joining the two branch points."

### 2. Upper pp. 3 and 6, Problems 3A and 6D: the answer depends on counting "press nothing"
- **Where:** Problem 3 says "Find every set of lines that solves each puzzle. Press each chosen line once. How are the solutions related?" Problem 6 asks the same, ending "…What is the rule for how many solutions a puzzle has on these networks?" 3A (empty ring4 → empty) and 6D (path6, start = target) are solved only with the empty set, or with the empty set plus the full ring.
- **Evidence:** if a child does not count pressing nothing as a set (`edge_cases.py`):
  - 3A has 1 solution instead of 2, which breaks the complementary-pair pattern that Problem 3 is built to show.
  - 6D has 0 solutions, the same as the impossible 6C. That merges the "exactly one when possible" and "none when impossible" cases that Problem 6 asks children to separate.
  - Neither page says pressing no lines counts. The notes say "Choosing no lines is allowed" only in the general "Use at the table" paragraph. The §3 and §6 answers ("do nothing", "just the empty set") give no warning about the other reading.
- **Fix:** in the notes for §3 and §6, add one sentence: "If a child reports one solution for 3A or none for 6D, settle together whether pressing no lines counts before comparing counts." Alternatively, add "Pressing no lines counts." to both prompts.

### 3. Upper notes, Problem 3 hint: "a different first line" can be met by reordering
- **Where:** `plans/week-02-catalog-upper.md`, §3: "If children have one solution, ask whether they can find a solution using a different first line."
- **Evidence:** in 3B, a child who found {1-2, 2-3} can press 2-3 first and then 1-2. That uses a different first line, gives the same set and reaches the target (`edge_cases.py`). This hint leads straight into the reordering confusion the notes warn about elsewhere. On a cycle, only a line *outside* the first set forces the second solution, which is the complement. In 3B, every solution containing 3-4, 4-5 or 5-1 is {3-4, 4-5, 5-1}.
- **Fix:** "…ask whether they can find a solution that uses a line their first solution did not use."

### 4. Compact p. 4, Problem 10, against the archived guide P13–14: invented puzzles can now be impossible
- **Where:** the student prompt is "Make some puzzles for your partner." The guide's corresponding section says: "From all OFF make two moves, then let a partner undo the result. **Reversing the moves always succeeds.**"
- **Evidence:** that guarantee needs the old wording: a connected board, with the puzzle produced by moves from all OFF. The compact prompt drops both conditions, so a child may draw any start and target.
  - On the printed square, all OFF → one lamp ON is unreachable.
  - On the two islands, all OFF → one lamp ON in each island is unreachable, although the total is even.
  
  The guide gives the adult no way to recognise an unsolvable invented puzzle.
- **Fix:** add one guide line for this problem: "A drawn puzzle is solvable exactly when, in each connected piece, an even number of lamps differ between start and target. Ask the maker to solve it first, or make the target by moves from the start." The student prompt can stay as it is.

### 5. Compact p. 1, Problem 3 (also P2 and P4): the one-light rule was dropped, but the wording and guide still assume it
- **Where:** P3 says "Visit every lamp and bring the light home." The source problems said "Keep exactly ONE lamp ON after every move" and "Keep ONE lamp ON". The catalog dropped those sentences. The archived guide still heads these problems "reach a destination with exactly one light" (P5) and "Keep ONE lamp ON" (P7).
- **Evidence:** without the rule, P3 is completed by lighting lamps and then undoing, with no light travelling. From {top}, press 2-3, 4-5, 6-1, 6-1, 4-5, 2-3. The states are {1,2,3}, {1,…,5}, {2,…,6}, {1,…,5}, {1,2,3}, {1}. Every lamp has been ON and the light is home (`edge_cases.py`). "The light" in the prompt presupposes a single light that the page no longer requires. P2 and P4 also become plain reachability tasks, not walks. All their answers stay valid, so nothing printed is wrong.
- **Fix:** add "Keep ONE lamp ON." to Problem 3, and to P2 and P4 if the walking-light contrast with P5 is still intended. Otherwise, drop "exactly one light" from the guide headings.

## Notes (not counted as problems)
- **No theorem-first overview:** neither guide has one. The archived guide opens with logistics and a page finder, and the upper notes go from "Use at the table" straight to per-problem reasoning. There is no overview section to check. The facts such an overview would state (the parity invariant, per-component parity, two complementary solutions on a cycle, the ⌊n/2⌋ ring record, one solution per reachable tree target) are stated inline and are correct.
- **Old problem numbers:** the compact catalog has no adult guide with matching numbers. Its Problems 1–10 are keyed as P2 and P5–P13 in the archived guide. The solutions still apply, apart from problems 4 and 5 above.
- **Problem 9 has no board of its own:** compact P9 relies on drawing the bridge on Problem 8's pictures, and "the trip" refers back to P8. This is a layout point only; any bridge makes the trip possible.
- **Thin lines in low-resolution images:** some grid and ring lines look thinner at 110 dpi. The vector data shows every line at 1.25 pt, and they render evenly at 300 dpi.
