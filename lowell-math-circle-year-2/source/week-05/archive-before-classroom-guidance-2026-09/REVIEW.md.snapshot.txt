# Week 5 authoring and review record

Revised and reviewed September 20, 2026, implementing the fall Weeks 1–10 review. This records the implementing agent's checks, not a fresh independent review of every source or page.

## Changes in this revision

- Delayed bottom-row elimination until the row-3 / row-2 case table supplies the missing constraints.
- Replaced the partial deletion exercise with an optional continuation checking all five printed alternate-city certificates, followed by the left-clue construction 4,3,2. The child's proof that three works stays separate from the computer-certified minimum for the target.
- Added a common six-part hour, including a 35–40-minute movement/reset, and an explicit stopping point and optional proof for each group. Fixed “1 page” in the README.

## Mathematical checks

- Enumerated all 12 order-three and 576 order-four Latin squares.
- Confirmed two solutions for the one-clue middle puzzle and one after adding its second clue; checked the symmetry proof that one visibility clue never suffices.
- Confirmed five-clue uniqueness, deletion counts 2/2/6/12/20, and the listed alternative completions.
- Searched all subsets of the target city's 16 perimeter clues: optimum three, including L1=4,L2=3,L3=2. The facilitator gives a direct uniqueness explanation for this alternative, disproving minimal=minimum.
- Verified all four disjoint extra-page switches remain Latin; four chosen entry clues still admit alternatives. Entry and visibility clue models stay distinct.

Runnable verification: plans/verify-week-05.py. All assertions pass. Facilitator proofs establish the child-facing claims; the global minimum of three for the fixed target remains a separate exhaustive computer result.

Also directly parsed and checked all five certificate cities printed on the revised student page: each is Latin, differs from the target, keeps the four retained clues, and violates the deleted clue. Verified the explicit row-candidate lists for the three-clue proof.

## Print and layout checks

All five sources rebuilt with pdfLaTeX, two passes each. Counts remain K–1 **2**, grades 2–3 **2**, grades 4–5 **3**, extra 6–7 **1**, facilitator **4**: **12 pages**. All are US Letter (612×792 points). No overfull/underfull boxes or LaTeX warnings occurred.

All 12 final pages were rendered with Poppler. Fresh visual inspection covered the changed pages: **upper pages 2–3 and facilitator pages 1 and 3**. Explicit page breaks and unchanged page counts keep the other pages in their original positions; those retain the September 19 full-page review rather than being claimed as freshly inspected. Revised text, tables, writing spaces, mathematical symbols, and footers fit without clipping or overlap. Render files are in `tmp/pdfs/week-05-07-revision-2026-09-20/`.

## Source and teaching boundaries

The implementing agent reread *Math Circle by the Bay*, preface printed pp. viii–x (PDF pp. 9–11): substantive themes, manipulatives, flexible pace, and opportunities to explain. The timetable, per-group stopping points, and specific proof scaffolds are project adaptations, not source prescriptions. Sources and prerequisite details remain in the plan and facilitator guide.

All IDs F05-K-v2/M-v2/U-v2/X-v2 remain **prepared, not taught**. Record which instances were tried, which claims were conjectured or proved, and which were supplied by an adult or computer. Printed proof continuations are optional, with one organizer alternating between the older groups.
