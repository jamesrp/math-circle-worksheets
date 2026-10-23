# Week 89 review-card fixes, October 23, 2026

From [plans/review/week-89.md](../../../../../plans/review/week-89.md) (verdict keep, no must). Made in the problem files after the conversion, then in the guide.

## Changed

| Card item | Where | Change |
|---|---|---|
| should 1 | student p. 11, P19 | Both pictures draw cube (1,0,0) after the corner cube or column, so the stair layer reads correctly. |
| should 2 | student p. 10, P18; guide p. 7 | The worked turn is (3,3,3) → (4,3,3) → (4,7,3) → (4,7,10), off the six-turn path; the guide says so and that copying old totals would give (4,6,6). |
| should 3 | student p. 1; guide p. 2 | The opening example grows a 2 × 2 square into a 2 × 3 rectangle by one shaded column; the launch does the same. |
| should 4 | student p. 1, P2; guide p. 3 | P2 asks for the tiles removed peeling the side-5 square layer by layer (9, 7, 5, 3, 1, adding to 25). |
| should 5 | student p. 11, P20; guide p. 7 | "without building it or running the trays for ten turns". |
| should 6 | guide pp. 1, 2, 8 | A K–1 return route with adult reading: P7 and P10 with counters, P16 to side 3, P19 steps 2–3, and a plain-words key. That K–1 sustains it is a prediction. |
| could 7 | student pp. 4, 6 | The one-tray and two-tray rules and worked turns now come before Problems 7 and 11 (setup files). |
| could 8 | student p. 6 | "same input already added" no longer touches its box or the next line. |
| could 10 | student p. 10, P18 | The table has a row for each turn 1–6. |
| could 11, 12 | guide p. 2 | One-inch tiles do not fit the 20 mm cells, 2 cm cubes do; the board is 140 × 120 mm, as on the materials page. |

Deferred: could 9 (P16 "shell" wording), since P17 relies on the word. No page moved: Problems 1–20 keep their pages, so the guide's page references and the band-view index stand. Student pages 2, 3, 5, 7, 8, 9 and guide pages 4–6 are pixel-identical to the conversion's build; the materials packet is unchanged.

## Checks

- `verify_card_fixes_2026_10_23.py`: the mathematics of every changed task and key; the Problem 19 cubes against their intended coordinates and a ray test that every visible point is painted by the nearest cube (0.0 mm² wrong, against 24.1 mm² before); the page 1 example read from the PDF; the Problem 11 label clearances; wording, tables and the guide's page references. 0 failures.
- `check_math.py` (run by the build) passes.
- Every changed page was rendered at 80 dpi and inspected.

Unpiloted; tile fit, copying totals, zero turns, shells and piles remain physically unrehearsed.
