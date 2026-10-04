# Week 10 return-visit CRITIC-MATH review

No located mathematical errors in `draft/return-visit.pdf`. No student-page correction is needed.

The explicit scope is one shared seven-page collection with Problems 1, 2 and 3 continued across pages. Every actual page was independently rendered and inspected. Page 1 (K–5), pages 2–5 (2–5), and pages 6–7 (4–5) all check out for the mathematics and diagrams they contain.

Independent verification covers the following outcomes:

- **Problem 1, pages 1–3:** Towns 1, 3, 5 and 8 admit a directed walk using every street once. Town 1 works from A, B or C; Towns 3 and 5 work only from A; Town 8 works from every island. Towns 2, 4, 6 and 7 work from no island. Exhaustive edge-by-edge searches check every printed town and every possible start; Town 7 correctly exhibits the separate connectivity obstruction despite balanced arrows.
- **Problem 2, pages 4–5:** From the actual printed stars, the safe first streets are Town 1: AB or AC; Town 2: DA; Town 3: AB, AC or AD; Town 4: AB or AC. Full-route enumeration gives a completion for every reported safe move and none for the other first moves.
- **Problem 3, pages 6–7:** The minimum row length is 10: a length-L row has L−2 triple windows, and `0001011100` contains all eight triples. The minimum circle length is 8: a length-L circle has L triple windows, and `00010111` contains all eight clockwise, including wraparound. Exhaustive enumeration gives 16 shortest linear words and 16 indexed shortest circular words, representing two necklaces under rotation. The page does not claim or require a necklace count.
- **Convention examples:** The rendered walker moves X → Y → Z while unused counters decrease 2 → 1 → 0 and used streets become dashed. The three rendered linear frames select and label `01`, `11`, `10` in `0110`. The rendered circle reads `011` clockwise; its marked join window is `10`, and its printed list is `01`, `11`, `10`. Both password-card sets contain precisely the eight binary triples.
- **Actual PDF geometry:** All 12 towns' printed islands, letter labels, street endpoints, counter midpoints, 34 directed arrow directions, and four starred starts agree with `generate.py` and `towns.json`. The active diagrams retain inch scaling (approximately 72 PDF points per source inch). Full 0.75-inch counter disks clear one another, the 0.30-inch island circles and their strokes, unrelated streets, and every complete rendered arrow polygon and stroke. The smallest arrow-to-counter gap is 0.0431 inch; the smallest arrow-to-island gap is 0.0619 inch. The compact worked example is a reference diagram rather than an active counter board.

The independent checker imports no writer checker. Portable code, bundled town data, complete route enumeration, window enumeration, PDF-vector measurements, and the reviewed PDF hash are preserved in `math-review/independent_check.py`, `math-review/towns.json`, and `math-review/independent-check.json`; commands are documented in `math-review/README.md`. Fresh renders and text extracts of all seven pages are also preserved there.

This is digital verification. Physical rehearsal and classroom piloting remain untested.
