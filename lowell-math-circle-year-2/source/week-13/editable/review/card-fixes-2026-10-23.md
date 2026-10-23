# Week 13: student-page and guide fixes from the review card, October 23, 2026

The review card is `plans/review/week-13.md` in the project (verdict keep, no must), with its math check `plans/review/week-13-math.md` and checks in `plans/review/checks/week-13/`.

The student pages first became problem files with no wording change (`../../README.md`). The fixes below were then made in the problem files and the guide source, with the footer ids raised to F13-K-v3, F13-23-v3 and F13-45-v3.

## What changed

- **K–1 Problem 3 (should 1).** "Then stop all travel with the same number of markers." now reads "Then stop all travel with as few markers as you can." Guide p. 5: "The page asks for as few markers as possible; ask children to compare that number with the number of routes."
- **Grades 4–5 Problem 2 (should 2).** "…and why the two answers show that your collection is largest" now reads "…and how you know your collection cannot be larger", as in grades 2–3 Problem 2.
- **Grades 4–5 Problem 5 (should 3).** The change-walk is asked "on this board and on both boards of Problem 1", with "Draw each resulting route collection." Guide p. 9 points to the two walks, s-B-A-t and s-B-A-C-E-D-t, solved on p. 7.
- **Guide pp. 2–3, supplies and launch (should 4).** The supplies paragraph says the repair tasks (K–1 Problem 1 upper board, grades 2–3 Problem 5, grades 4–5 Problems 1 and 5) need a route undone, so routes there are drawn in pencil with different line patterns or in wipe-off marker on a sheet protector, marked as a prediction and untested. The launch ends by starting a second route along an arrow the first already uses and asking a partner whether that is allowed.
- **Guide p. 6, grades 2–3 Problem 4 key (should 5).** "Upper board: any new arrow from A, B, C or D to G, H, I or J works (16 choices); it must jump past both two-arrow bottlenecks." The D-to-G routes follow as an example.
- **Guide p. 8, grades 4–5 Problem 4 key (should 6).** The five smallest sets, {sA,sB}, {sB,AC}, {AC,BD}, {AC,Dt}, {Ct,Dt}, with the three that one route uses twice (s-B-A-C-t, s-A-C-B-D-t, s-A-C-D-t), and a note for the child who chose the two Start or two Finish arrows.
- **Guide p. 10, drawing proof (should 7).** A + token at the tail and a − token at the head of each reserved arrow, totalled over the dots of the Start side S two ways: dot by dot (each internal dot balances and Start has k +, so the total is k) and arrow by arrow (an arrow inside S gives + and −, an arrow leaving S one +, and no arrow entering S is reserved). So exactly k arrows leave S, all reserved.
- **K–1 Problem 5 (could 8).** Ten small recording copies instead of eight, so the copies do not give the eight answers away; guide p. 5 says so.
- **Clean copies (could 9).** Grades 2–3 p. 6 and grades 4–5 p. 2 now say "Extra workspace for Problem 5." and "Extra workspace for Problem 1."; the guide's opening note says they are labelled.
- **K–1 opening rules (could 10).** "without visiting a dot twice" and "in a collection" are dropped (no K–1 board has a directed cycle). The older bands keep the full rule.
- **Grades 4–5 p. 6 worked visual (could 11).** The cancellation example's dots are X and Y ("walk Y to X", "X to Y is now unused"), letters on no grades 4–5 board.
- **Guide p. 5 (could 12).** "The final page has a large working board" now reads "K–1 page 5 has a large working board and ten small recording copies".
- **Guide p. 3 menu (could 14).** 0–5 run around (the children arrive from school), 5–9 launch and handling the markers, 9–28 and 28–50 table work, 50–60 share, matching `worksheet-workflow/context.md`; the free-tracing opening and the standing break are gone.
- **Route note (guide p. 11).** K–1's return choices read "every preserving closure (P4) or every stopping pair (P5)" instead of grouping both as "every preserving closure (P4-5)".

Every page of the three packets changed (the footer id); in content, K–1 pages 1, 3 and 5, grades 2–3 page 6 and grades 4–5 pages 2, 3 and 6. Guide pages 2, 3, 5, 6, 8, 9, 10 and 11 changed; the guide keeps 11 pages and every heading stays on its page, so its page references (pp. 4, 6, 7) still hold.

## Not done

- **Could 13** (add K–1 Problem 3's three-branch board to the closing game in K–1 and grades 2–3 Problem 6): a third game board changes the game's substance and the page's length. The card's game-tree claim (a second-player win, because closing a dead arrow is a spare move) is noted for the organizer.
- **The return visit's Problem 2** (the math check: its last map repeats map 1): the return visit is a separate package (`week-13-return-visit.pdf`) that the card noticed but did not review; it is unchanged.

## Verification

- `src/student_checks.py` keeps the old builder's exhaustive checks and adds checks that read the boards and copy counts from the problem files' `figures.py`: the six K–1 boards have no directed cycle and the grades 4–5 backward board has one; on K–1 Problem 3's boards the most routes equal the fewest closures (2 and 3); the bowtie has 8 closure pairs, fewer than the 10 copies; every change-walk on the greedy, double-trap and staircase boards adds one route and reaches the maximum; the worked visual's letters are X and Y and on no grades 4–5 board. Changing a copy count, a letter or a board makes it fail.
- `facilitator-src/check_math.py` adds the guide's new claims: exactly the 16 arrows from A–D to G–J make three routes fit on the bottleneck board; the five smallest sets of the backward board, three of them used twice by one route, and in each such case no second route fits beside it; the greedy change-walk is s-B-A-t. `review/math_checks.json` is unchanged.
- `check_guide_copy.py` confirms that every key and hint sentence in the problem files appears in the regenerated guide.
- The review's own extractor, `plans/review/checks/week-13/extract_graphs.py`, run on the new print PDFs with K–1 page 5 expecting 11 bowties (outputs kept outside the project): all 61 boards in the packets, guide and return visit are the intended graphs with the intended reservations and no crossing without a dot.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` and the strict `verify_rebuild.py` on all four PDFs (31 pages), and the problem-file tools give the same student LaTeX. Every changed student page and guide pages 2, 3, 8 and 10 were rendered and inspected.
- The references are now built with TeX Live 2023 (pdfTeX 1.40.25), so the audited pixel alternates for unchanged pages are no longer needed.
- These are digital checks. Marker fit on the 26 mm shortest edge, erasable route drawing and the launch are unrehearsed, and the theme remains unpiloted.
