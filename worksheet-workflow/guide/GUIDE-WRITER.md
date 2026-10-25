# Write the facilitator guide for "{TOPIC}"

You are writing the adult facilitator guide for a math circle theme whose student pages are already drafted, reviewed and revised. Work only inside the run folder `{RUN}`. Write your sources to `{RUN}/draft/src/` and the compiled guide to `{RUN}/draft/facilitator.pdf`. Do not edit anything else in the repository.

## Read first

1. `/home/claude/math-circle-worksheets/AGENTS.md`, especially "Facilitator mathematical overview", "Launch together", "Make activities usable", "Design and review from classroom evidence" and "Review age fit operationally". The guide must meet those rules.
2. The student pages the guide serves, which are final and must not change: `{DRAFT}/k-1.pdf`, `{DRAFT}/grades-2-3.pdf`, `{DRAFT}/grades-4-5.pdf`{EXTRA}, and their sources in `{DRAFT}/src/`. Render every page to an image and read it; problem numbers, page numbers and pictures in the guide must match these PDFs exactly.
3. The theme's outline, `{OUTLINE}`: its mathematical kernels (with proofs and checked instances), sources, band emphasis and materials with their physical constraints.
4. The two reviews of the pages, `{DRAFT}/review.md` and `{DRAFT}/review-math.md`. The math review's answer key is a starting point, but it was written about an earlier draft; the revision changed problems, so re-derive every answer for the final pages.
5. The theme's entry in `/home/claude/math-circle-worksheets/plans/topic-scouting/drafts/README.md` (materials, what is untested, what the revision changed).
6. Two approved-style model guides from the library: `/home/claude/math-circle-worksheets/lowell-math-circle-year-2/week-98/week-98-facilitator.pdf` (source in `lowell-math-circle-year-2/source/week-98/guide/`) and `/home/claude/math-circle-worksheets/lowell-math-circle-year-2/week-87/week-87-facilitator.pdf`. Match their structure, tone and density, not their length.

## What the guide contains

Header on every page: `Week NN / {TOPIC} / Facilitator guide`. Footer: `Bellingham Math Circle / Week NN / {GUIDEID}` with the page number. US Letter, pdfLaTeX, the same look as the model guides. "NN" stays until the organizer assigns a week number.

1. **Mathematical overview, first, before any solution.** Theorem-first: state the actual facts, invariants or theorems the pages reach, with their assumptions and limits, and a short proof or proof idea an adult can follow. Say what children are meant to discover, and distinguish experiments, conjectures and explanations. End with a brief map of what each band (K–1, 2–3, 4–5) does. An adult should understand the mathematical destination without reading every solution.
2. **Preparation, launch and pacing.** Status (unpiloted; name what is physically untested). Materials per pair and per table with counts and sizes, what to print (which pages are cut, which are mats, single-sided at 100%), and a realistic preparation time for a parent volunteer with a full-time job. Staffing: which tables need an adult and what the adult does without taking over the mathematical choices. A short whole-group launch that demonstrates the concrete action everyone will use, on a non-task instance that does not reveal the main theorem or any problem's answer; if the procedure is unfamiliar, a small worked visual (input, one meaningful step, output). A suggested first route for a one-hour meeting per band, which problems to save for a return visit, and readiness-dependent continuations. Finishing every page is not the goal.
3. **Solutions and hints by band.** For each band, each problem by its printed number: the answer (every answer for "find all" problems, with how to know the list is complete), the reasoning a child might give with objects or drawings, one or two hints to use only when needed (questions, not procedures), and extensions where natural. Keep the discretionary "How do you know for sure?" follow-ups here, not on the pages.
4. **Sources.** The outline's sources with page or problem references, and which were consulted.

Keep it as short as these allow; the model guides run 5 to 8 pages for three bands.

## Checks before you finish

- Recompute every answer you print with your own script (`draft/src/check_guide.py` or similar), against the final pages, not the outline. Where a problem has several answers, enumerate them.
- Every problem number, page number, board size and material count you cite matches the final PDFs.
- The launch example is not a task instance and gives away no answer.
- Compile with no errors or overfull boxes, render every page and look at it. Fix anything that overflows or overlaps.

Report back in a few sentences: the guide's page count, the overview's main theorems, anything on the pages you found wrong or risky (do not change the pages; report it), and what you could not verify.
