# Week 6 authoring and review record

Revised and reviewed September 20, 2026, implementing the fall Weeks 1–10 review. This records the implementing agent's checks, not a fresh independent review of every source or page.

## Changes in this revision

- Promoted coordinatewise color renaming to numbered middle task 6, with the concrete BRB-to-RRR example; the all-first-query optimality claim now depends explicitly on that step.
- Made redundant middle table entries optional after the score structure is explained. Added distinct hints for the upper three-candidate and four-candidate obstructions.
- Added a common six-part hour, including a 35–40-minute movement/reset, and an explicit stopping point and optional proof for each group; older proof discussions take turns with the organizer. Fixed “1 page” in the README.

## Mathematical checks

- Exhaustive memoized decision-tree search covers every possible query at every candidate set: exact worst-case identification costs 2,3,4 for two,three,four binary places.
- Verified baseline-plus-single-flips signatures for every secret and checked the explicit middle score table.
- Facilitator supplies structural adversary proofs for three/four places; the lower bound does not rely on a naive logarithmic answer count.
- Verified all 32 signatures of five-bit probes 00000,00011,00101,01001 are distinct; scores 2,2,2,0 give 10110. Elementary pair-sum proof included.
- Clearly distinguishes identifying a secret from submitting a winning guess, and the binary exact-position rules from commercial Mastermind.

Runnable verification: plans/verify-week-06.py. All assertions pass. Facilitator proofs explain why results hold independently of the finite program.

Also exhaustively checked coordinatewise color renaming for every secret/query pair at lengths three and four, and that every query gives at most two scores on the printed middle and upper triples.

## Print and layout checks

All five sources rebuilt with pdfLaTeX, two passes each. Counts remain K–1 **2**, grades 2–3 **2**, grades 4–5 **3**, extra 6–7 **1**, facilitator **4**: **12 pages**. All are US Letter (612×792 points). No overfull/underfull boxes occurred. K–1 and middle builds retain existing Computer Modern typewriter size-substitution warnings at the large code labels; inspection of the revised middle page found no visible defect. This revision does not claim warning-free logs.

All 12 final pages were rendered with Poppler. Fresh visual inspection covered the changed pages: **middle page 2, upper page 2, and facilitator pages 1–3**. Explicit page breaks and unchanged page counts keep the other pages in their original positions; those retain the September 19 full-page review rather than being claimed as freshly inspected. Revised text, tables, writing spaces, mathematical symbols, and footers fit without clipping or overlap. Render files are in `tmp/pdfs/week-05-07-revision-2026-09-20/`.

## Source and teaching boundaries

The implementing agent reread *Math Circle by the Bay*, preface printed pp. viii–x (PDF pp. 9–11): substantive themes, manipulatives, flexible pace, and opportunities to explain. The timetable, per-group stopping points, and specific proof scaffolds are project adaptations, not source prescriptions. Sources and prerequisite details remain in the plan and facilitator guide.

All IDs F06-K-v2/M-v2/U-v2/X-v2 remain **prepared, not taught**. Record which instances were tried, which claims were conjectured or proved, and which were supplied by an adult or computer. Printed proof continuations are optional, with one organizer alternating between the older groups.
