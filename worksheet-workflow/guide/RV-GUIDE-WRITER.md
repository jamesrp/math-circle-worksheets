# Write the return-visit facilitator guide for Week {WEEK}, "{TOPIC}"

You are writing the adult guide for a return visit: new student pages for children who already met Week {WEEK} once. The pages are drafted, reviewed and revised. Work only inside the run folder `{RUN}`. Write your sources to `{RUN}/draft/src/` and the compiled guide to `{RUN}/draft/{OUT}`. Do not edit anything else in the repository.

## Read first

1. `{REPO}/AGENTS.md`, especially "Facilitator mathematical overview", "Launch together", "Make activities usable", "Design and review from classroom evidence", "Build encore investigations" and "Review age fit operationally". The guide must meet those rules.
2. The student pages the guide serves, which are final and must not change: {PAGES}, and their sources in `{DRAFT}/src/`. Render every page to an image and read it; problem numbers, page numbers and pictures in the guide must match these PDFs exactly.
3. The outline, `{OUTLINE}`: the mathematical kernels (with proofs and checked instances), sources, band emphasis and materials with their physical constraints.
4. The two reviews of the pages, `{DRAFT}/review.md` and `{DRAFT}/review-math.md`. The math review's answer key is a starting point, but it was written about an earlier draft; the revision changed problems, so re-derive every answer for the final pages.
5. The draft's entry in `{README}` (kit, what is untested, what the revision changed).
6. The base week's adult guide, `{BASEGUIDE}`{BASEMAT}. The return visit uses its kit and builds on what children met there; do not contradict it, and do not re-explain its first-visit mathematics beyond the one or two facts the new pages lean on.
7. Model guides: `{REPO}/lowell-math-circle-year-2/week-08/week-08-return-visit-facilitator.pdf` (an approved-style return-visit guide) and `{REPO}/lowell-math-circle-year-2/week-98/week-98-facilitator.pdf` (source in `lowell-math-circle-year-2/source/week-98/guide/`). Match their structure, tone and density, not their length.

## What the guide contains

Header on every page: `Week {WEEK} / {TOPIC} / Adult return-visit guide`. Footer: `Bellingham Math Circle / Week {WEEK} / {GUIDEID}` with the page number. US Letter, pdfLaTeX, the same look as the model guides.

1. **Mathematical overview, first, before any solution.** Theorem-first: state the actual facts, invariants or theorems the new pages reach, with their assumptions and limits, and a short proof or proof idea an adult can follow. Say how they extend the first visit, what children are meant to discover, and distinguish experiments, conjectures and explanations. End with a brief map of what each band (K–1, 2–3, 4–5) does. An adult should understand the mathematical destination without reading every solution.
2. **Preparation, launch and pacing.** Status (unpiloted; name what is physically untested). Materials per pair and per table with counts and sizes, which base-week files to print and which pages are cut or used as mats, and a realistic preparation time for a parent volunteer with a full-time job. Staffing: which tables need an adult and what the adult does without taking over the mathematical choices. A short whole-group launch that reminds children of the kit and demonstrates any new action, on a non-task instance that reveals no theorem or answer; if a procedure or recording convention is new, a small worked visual (input, one meaningful step, output). A suggested first route for a one-hour meeting per band, what to save for a later visit, and readiness-dependent continuations. Finishing every page is not the goal.
3. **Solutions and hints by band.** For each band, each problem by its printed number: the answer (every answer for "find all" problems, with how to know the list is complete), the reasoning a child might give with objects or drawings, one or two hints to use only when needed (questions, not procedures), and extensions where natural. Keep discretionary "How do you know for sure?" follow-ups here, not on the pages.
4. **Sources.** The outline's sources with page or problem references, and which were consulted.

Keep it as short as these allow; three-band guides in the library run 5 to 8 pages.

## Checks before you finish

- Recompute every answer you print with your own script (`draft/src/check_guide.py` or similar), against the final pages, not the outline. Where a problem has several answers, enumerate them.
- Every problem number, page number, board size and material count you cite matches the final PDFs and the base week's materials.
- The launch example is not a task instance and gives away no answer.
- Compile with no errors or overfull boxes, render every page and look at it. Fix anything that overflows or overlaps.
- Leave a `draft/src/build.sh` that compiles the guide to `../{OUT}` (run from `draft/src/`), cleans up and then runs your checker. The folder will later be copied into `{DRAFT}/guide-src/`, so the checker should look for the student pages first in the folder above the script and fall back to `{DRAFT}`; use no other absolute paths.

Report back in a few sentences: the guide's page count, the overview's main theorems, anything on the pages you found wrong or risky (do not change the pages; report it), any object the pages need that no base-week file prints, and what you could not verify.
