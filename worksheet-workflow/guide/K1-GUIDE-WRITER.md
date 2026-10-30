# Write the K–1 guide section for Week {WEEK}, "{TOPIC}"

Week {WEEK} has an adult guide for its older tables, with only an adult-led route for K–1. New K–1 student pages are now drafted, reviewed and revised. You are writing the adult guide section for those pages, as a short standalone PDF that will replace the guide's adult-led K–1 route once the organizer approves the pages. Work only inside the run folder `{RUN}`. Write your sources to `{RUN}/draft/src/` and the compiled section to `{RUN}/draft/{OUT}`. Do not edit anything else in the repository.

## Read first

1. `{REPO}/AGENTS.md`, especially "Facilitator mathematical overview", "Launch together", "Make activities usable", "Design and review from classroom evidence" and "Review age fit operationally". The section must meet those rules.
2. The K–1 pages the section serves, which are final and must not change: {PAGES}, and their sources in `{DRAFT}/src/`. Render every page to an image and read it; problem numbers, page numbers and pictures in the section must match the PDF exactly.
3. The outline, `{OUTLINE}`: the mathematical kernels (with proofs and checked instances), sources, emphasis and materials with their physical constraints.
4. The two reviews of the pages, `{DRAFT}/review.md` and `{DRAFT}/review-math.md`. The math review's answer key is a starting point, but the revision changed problems, so re-derive every answer for the final pages.
5. The draft's entry in `{README}` (kit, what is untested, what the revision changed).
6. The week's adult guide, `{BASEGUIDE}`{BASEMAT}, and its older-band pages in `{REPO}/lowell-math-circle-year-2/week-{WEEK}/`. Find the part that describes the adult-led K–1 route: your section replaces it. The K–1 table joins the week's whole-group launch and uses the week's kit; do not contradict the guide, and refer to its overview for the older bands' destination instead of repeating it.
7. A model guide: `{REPO}/lowell-math-circle-year-2/week-98/week-98-facilitator.pdf` (source in `lowell-math-circle-year-2/source/week-98/guide/`). Match its tone and density.

## What the section contains

Header on every page: `Week {WEEK} / {TOPIC} / K–1 adult guide`. Footer: `Bellingham Math Circle / Week {WEEK} / {GUIDEID}` with the page number. US Letter, pdfLaTeX, the same look as the model guide. Aim for 2 to 4 pages.

1. **Mathematical overview, first, before any solution.** Theorem-first and short: the facts these K–1 pages reach, with their assumptions and limits, and the explanation a five- or six-year-old could give with the objects. Say which part of the week's destination the K–1 table reaches, what children are meant to discover, and what counts as an experiment, a conjecture and an explanation at this age.
2. **Preparation, launch and pacing.** Status (unpiloted; name what is physically untested). The K–1 kit per pair with counts and sizes and which week files to print, with a realistic preparation time beyond what the week already needs. Prerequisites (reading, counting, number range) and staffing: the K–1 table needs an adult who reads the pages aloud and records when asked; say what the adult does without operating the investigation or making the children's choices. What the K–1 table does after the whole-group launch: a brief table demonstration on a non-task instance that reveals no answer, with a small worked visual if a recording convention is new. A suggested first route for a one-hour meeting, what to save for a later visit, and readiness-dependent continuations. Finishing every page is not the goal.
3. **Solutions and hints.** Each problem by its printed number: the answer (every answer for "find all" problems, with how to know the list is complete), the reasoning a child might give with objects or drawings, one or two hints to use only when needed (questions, not procedures), and extensions where natural.
4. **Where it goes.** One sentence naming the section and page of `{BASEGUIDE}` that this section replaces once the pages are approved.

## Checks before you finish

- Recompute every answer you print with your own script (`draft/src/check_guide.py` or similar), against the final pages, not the outline. Where a problem has several answers, enumerate them.
- Every problem number, page number, board size and material count you cite matches the final PDF and the week's materials.
- The table demonstration is not a task instance and gives away no answer.
- Compile with no errors or overfull boxes, render every page and look at it. Fix anything that overflows or overlaps.
- Leave a `draft/src/build.sh` that compiles the guide to `../{OUT}` (run from `draft/src/`), cleans up and then runs your checker. The folder will later be copied into `{DRAFT}/guide-src/`, so the checker should look for the student pages first in the folder above the script and fall back to `{DRAFT}`; use no other absolute paths.

Report back in a few sentences: the page count, the overview's main facts, the guide section it replaces, anything on the pages you found wrong or risky (do not change the pages; report it), any object the pages need that no week file prints, and what you could not verify.
