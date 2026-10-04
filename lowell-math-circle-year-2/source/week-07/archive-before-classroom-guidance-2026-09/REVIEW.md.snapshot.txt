# Week 7 authoring and review record

Revised and reviewed September 20, 2026, implementing the fall Weeks 1–10 review. This records the implementing agent's checks, not a fresh independent review of every source or page.

## Changes in this revision

- Added a movable paper frame and straight label strip to make the four-label recurrence concrete, with matching facilitator directions and preparation notes.
- Added a common six-part hour, including a 35–40-minute movement/reset, and an explicit stopping point and optional proof for each group. Further table entries are optional after the structure is clear. Fixed “1 page” in the README.

## Mathematical checks

- Checked the 1/2, 1/3/4, 1/3/5 recurrences through pile size 1000.
- Confirmed the 1/3/4 Grundy block 0,1,0,1,2,3,2, the losing remainders 0/2 modulo 7, and all stated winning moves.
- Independently solved every two-pile game with each pile at most 30 and compared it to equality of mex labels.
- Facilitator proves all unbounded claims: both losing-position obligations, finite-memory eventual periodicity, and the two-pile mex equality theorem.
- The extra contrasts (1,1) with (1,4); individual W labels alone do not determine a sum. Prior Lowell erroneous label 5 is corrected, and 1/3/4 is attributed to JRMF.

Runnable verification: plans/verify-week-07.py. All assertions pass. Facilitator proofs explain why results hold independently of the finite program.

Checked the paper-frame indexing: for a four-cell window ordered left to right, the next 1/3/4 label uses the rightmost, second-from-left, and leftmost entries.

## Print and layout checks

All five sources rebuilt with pdfLaTeX, two passes each. Counts remain K–1 **2**, grades 2–3 **2**, grades 4–5 **3**, extra 6–7 **1**, facilitator **4**: **12 pages**. All are US Letter (612×792 points). No overfull/underfull boxes or LaTeX warnings occurred.

All 12 final pages were rendered with Poppler. Fresh visual inspection covered the changed pages: **upper page 3 and facilitator pages 1 and 3**. Explicit page breaks and unchanged page counts keep the other pages in their original positions; those retain the September 19 full-page review rather than being claimed as freshly inspected. Revised text, tables, writing spaces, mathematical symbols, and footers fit without clipping or overlap. Render files are in `tmp/pdfs/week-05-07-revision-2026-09-20/`.

## Source and teaching boundaries

The implementing agent reread *Math Circle by the Bay*, preface printed pp. viii–x (PDF pp. 9–11): substantive themes, manipulatives, flexible pace, and opportunities to explain. The timetable, per-group stopping points, and specific proof scaffolds are project adaptations, not source prescriptions. Sources and prerequisite details remain in the plan and facilitator guide.

All IDs F07-K-v2/M-v2/U-v2/X-v2 remain **prepared, not taught**. Record which instances were tried, which claims were conjectured or proved, and which were supplied by an adult or computer. Printed proof continuations are optional, with one organizer alternating between the older groups.
