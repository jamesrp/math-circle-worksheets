# Brief: guides for the eleven week-tied drafts

**For Codex, with one stage for Claude.** Written by Claude on October 30, 2026. Work board line: "Facilitator guide drafts for the four return-visit drafts … and K–1 guide sections for the seven K–1 drafts".

## Goal

Give each draft awaiting the organizer's review the adult guide it lacks, so he can judge pages and guide together:

- a return-visit facilitator guide for each of the four [return-visit drafts](../return-visit-drafts/README.md) (Weeks 53, 58, 62, 63);
- a short K–1 guide section for each of the seven [K–1 drafts](../k1-drafts/README.md) (Weeks 57, 66, 81, 87, 91, 97, 98), which will replace that week guide's adult-led K–1 route once the pages are approved.

The twelve new-theme drafts got theirs the same way on October 25; [their README](../topic-scouting/drafts/README.md#facilitator-guides-and-materials) shows the finished shape. Do not change any student page. A problem found on a page goes in the report.

## Steps

Work on a branch, `codex/week-guides`, from fetched `origin/main`. The run folders live on that branch in `plans/guide-runs/` so that Claude can read them; nothing in that folder goes to `main`.

1. **Writer (Codex).** `python3 worksheet-workflow/guide/make_week_runs.py --dir plans/guide-runs` makes eleven run folders, each with `WRITER.md`, `CRITIC.md` and `REVISE.md`. The prompts hold this checkout's absolute paths, so don't commit them. Run each `WRITER.md` in a fresh session (`codex exec "Your instructions are in <run>/WRITER.md. Read it and follow it exactly."`). Commit each run's `draft/` (the PDF and `draft/src/`, without LaTeX intermediates) and the writer's report as `<run>/writer-report.md`. Push the branch, then set the work board line to "writers done; critic next (Claude)".
2. **Critic (Claude).** Claude runs each `CRITIC.md` in its own checkout of the branch and commits `<run>/review-guide.md` for all eleven, then sets the line to "critics done; reviser next (Codex)".
3. **Reviser (Codex).** Run each `REVISE.md` in a fresh session; it writes `<run>/final/`.
4. **Package (Codex).** Follow the October 25 pattern in `plans/topic-scouting/drafts/`:
   - Into each draft folder copy the final guide (`facilitator.pdf` for a return visit, `k1-guide.pdf` for K–1 pages), `review-guide.md`, and `final/src/` as `guide-src/` with a `build.sh` that compiles to `../<guide>.pdf` from inside `guide-src/` and ends by running its checker. The checker finds the student pages in the folder above it.
   - In both drafts READMEs, add the guide to the table and the status paragraph, list what the critic caught, and add the guide to the rebuild instructions.
   - Add `"k1-guide.pdf": "K–1 guide section (draft)"` to `DRAFT_ROLES` in `catalog/build.py` and run `python3 catalog/build.py`.
   - Delete `plans/guide-runs/`, rebase onto `origin/main`, push to `main`, and mark the work board line done with the page counts.

## Checks

- Every guide compiles with no errors or overfull boxes. Every page is rendered and looked at.
- Every problem number, page number and material count matches the final student PDFs.
- Each `guide-src/` rebuilds from a clean copy of the draft folder, outside the repository, to the same text (`pdftotext`), and its checker passes there.
- `python3 catalog/build.py` and `python3 catalog/check_path.py` run clean.

## Report

Per guide: the page count, the critic's must-fix findings and how each was fixed, any finding declined and why, and anything on the student pages the guide had to work around. Say plainly that the guides are untested with children.
