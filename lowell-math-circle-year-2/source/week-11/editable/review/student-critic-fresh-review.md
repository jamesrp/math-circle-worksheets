# Week 11 targeted revision: independent adversarial review

**Disposition: pass; no blocking defects found.** Reviewed the authorized recording revision, rather than proposing a new packet. The reviewer did not write or edit the student sources or facilitator guide.

Read `PROMPT.md`, `CRITIC.md`, the current student PDF text and copied baseline sources, the revised generator and generated TeX, and the writer's notes. Independently rendered all three draft PDFs and inspected every page individually, as well as the three six-page overviews.

## Scope and preservation

All three packets retain six pages, Problems 1–6, every starting case, the original repetitions, and the original mathematical questions. All six K–1 problem descriptions are verbatim. Grades 2–3 Problems 3, 5 and 6 and Grades 4–5 Problems 2, 3, 5 and 6 are verbatim. The other five older-band descriptions change only how the existing sharing counts are recorded and when they are counted.

| Band | Pages with substantive recording changes | Pages retaining their mathematical content and original record format |
|---|---|---|
| K–1 | 1, 3, 5 | 2, 4, 6 |
| Grades 2–3 | 1, 2, 4 | 3, 5, 6 |
| Grades 4–5 | 1, 4 | 2, 3, 5, 6 |

Every page has the revised version footer. This table distinguishes substantive student edits from version-label changes. All 18 delivered pages were nevertheless rendered and inspected.

No task is narrowed to a prescribed firing order. Repeated rows allow comparisons of different orders. The paired `(4,0)` start has only one complete legal order, and both older packets retain “if possible” for that task. All three starts in Grades 2–3 Problem 2 admit different orders, so its unqualified request is correct. The larger final questions about termination, irreversible addition and order independence remain intact.

## Recording and convention

The shared rule now asks for the chronological sharing letters followed by final piles. The older-band prompts explicitly say to count letters **after stopping**. Their tables contain one wide word field and final-state fields; none retains a separate per-vertex concurrent tally column. K–1 gets the same single recoverable word field in its repeated trials, without a new firing-count demand.

The first page of each packet supplies an explicit spoken input “A, then B, then A,” the intermediate records `A → AB`, and the output `ABA`. This is a recording convention, not a claimed solution to an assigned start. Its older-band letter-count explanation is correct. An independent non-task legal witness is `(3,1) → (1,2) → (2,0) → (0,1)` under `ABA`; this witness is evidence only and need not be added to the worksheet.

One word preserves the complete firing order. Counts can be recovered from it later and checked against the independent results. The staged-addition problems ask about final piles, so they do not require a second simultaneous addition ledger. Their existing totals and final-state records remain sufficient for their stated question.

## Visual and physical-scale check

Inspected all 18 pages for clipped or overlapping text, missing or unclear edges, circle and sink labels, start numbers/dots, table headers, record space, footers, and numbered tasks. No such defect found. The convention examples occupy spare space beside the triangle sink without crossing edges or occupying a chip circle.

Every board command in the revised generated TeX matches the corresponding baseline command exactly. The actual PDF drawing bounding boxes also match the current release on every page: 44 mm circles, a 60 mm square sink, unchanged positions and counts. The diagrams remain on single-sided US Letter pages, at the original scale. The wider word fields accommodate the longest specified histories in their relevant trials; the shorter rows in the upper packet contain at most eight letters in Problem 1.

## Optional facilitator support, not a student defect

A mover/recorder or mover/referee partnership can keep one adult from writing several simultaneous K–1 histories. A child may dictate letters while another person writes them, and partners can swap roles. This is a practical guide option, not a reason to remove material or add another printed student procedure. The guide owner should ensure any former per-circle tally instructions now say to count the completed word after stopping.

## Evidence and limits

Independent code and full numerical results: `../../week-11/critic-qa/independent_checks.py` and `../../week-11/critic-qa/independent-checks.json`. Task-by-task mathematical coverage: `../../week-11/critic-qa/independent-verification.md`. Critic renders: `../../week-11/critic-qa/<band>-<page>.png`.

The critic did not perform a physical rehearsal, classroom pilot, source-ZIP rebuild or release synchronization. The packet is digitally checked and unpiloted; packaging and adult-guide checks remain on the parent release path.
