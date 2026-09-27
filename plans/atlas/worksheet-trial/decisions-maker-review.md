# Maker review: four decision/probability worksheet modules

September 25, 2026. The decision/probability author checked the maker previews after the independent design review. This is maker visual QA, not the independent PDF review and not a classroom pilot.

**Files:** `lowell-math-circle-year-2/source/atlas-random-ten/decisions.py` renders exactly **12 student pages** and **12 facilitator pages** for AP-23, AP-21, AP-01 and AP-29. The shared build adds one cover to each selected-family preview, making **13 + 13** preview pages. Preview directory: `tmp/pdfs/atlas-random-ten/decisions-preview/`.

**Checks:** all student and facilitator pages rendered successfully; inspected both contact sheets for each book. Inspected full-size student pages for the dense AP-21 backward certificate, AP-01 ferry arrows, AP-29 sender/receiver page and AP-29 proof page. The shared reports record zero bounds violations and zero suspect glyphs. All four mathematical check groups pass in `decisions-checks.py`; the guide gives every one of the 36 student prompts a complete keyed solution.

**Repairs applied:**

- AP-01 explicitly specifies a fair coin with independent tosses and starts at 1, 2 or 3. “Can any of those starts guarantee a win?” now excludes the trivially winning endpoint, closing the independent review finding.
- AP-23's second-page title is the neutral “What changes when G switches?” so the cost comparison produces the surprise.
- Prose spacing is cleaned throughout student copy and facilitator material; genuine binary strings remain unbroken.
- Student body copy uses 11.5 pt, with shorter captions and diagram labels at readable smaller sizes. No body-font shrinking was needed.
- AP-21 uses only relevant reusable states, not a compulsory full dynamic-programming table. The take/skip comparison panels now record immediate points, battery before day 4, best later score and total without irrelevant duplicate choice rows. Its optional changed-ending question has four full answer lines.
- AP-29 has a receiver-picture row, an enlarged blank code-tree workspace and four proof lines for its optimality explanation. Source formulas and finished code trees remain in the guide, apart from the intentionally supplied baseline code and a separate two-leaf illustration of removing a unary step.
- The shared renderer's orphan-heading fix carries facilitator headings with their following text.

**Candid classroom ranking:** AP-29 is the strongest of these four: it combines a message game, an actual ambiguous transmission, open construction, a complete small optimality proof and a frequency reversal. AP-23 is also strong and needs only small sums, but its payoff depends on children carefully distinguishing the mover's cost from the group's. AP-21 is strong for children who like constrained planning; the five-job problem has to be explored before the backward help cards appear, and the optional changed ending should not crowd out that exploration. AP-01 is the most conditional: moving a counter is easy, but a satisfactory core needs average-of-neighbors reasoning and halves/quarters. Its chance skyline and ferry comparison are substantive, but a coin-tossing-only session would not fulfill the mathematical promise.

**Remaining validation:** an independent reviewer should inspect final combined-book pagination, arrows, fields and answer spaces. All four remain unpiloted; actual student engagement and timing are unknown.
