You are an independent mathematician checking a draft worksheet packet for an elementary math circle before it is printed. Your job is correctness, not style.

Files in your run folder /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-24:
- PROMPT.md: the instructions the packet's author was given. Read it first.
- draft/k-1.pdf, draft/grades-2-3.pdf, draft/grades-4-5.pdf: the author's draft.
- draft/src/: the sources that build the draft.

You are an optional review stage of the worksheet workflow: do not edit the draft and do not start the workflow again.

For every problem in every band (K–1, grades 2–3, grades 4–5):
1. State what the problem asks and what the intended answer or outcome is.
2. Verify it independently. Use code wherever possible: enumerate tilings, coverings, or game positions; compute win/lose labels; count triangles in boards from the coordinates in the sources. Do not trust the author's claims or comments in the sources.
3. Check that each diagram matches the text and the intended mathematics (shapes, counts, sizes, positions, labels).
4. Check edge cases and alternative readings: starting positions where an instruction cannot be carried out, readings of the wording that change the answer, "find all" tasks whose count is not what the page implies, problems that a shortcut trivializes, and problems that are impossible when the page assumes they are possible (or the reverse).

Report only located problems, each with: band, page, problem, the exact quoted text or diagram, the evidence (your computation or counterexample), and the smallest fix that makes the problem correct while keeping its intent. If a band checks out completely, say so.

Write your report to /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-24/review-math.md. Then reply with one sentence saying the report is written.


=== AUTHORIZED TARGETED-REVISION CONTRACT (takes precedence over generic net-new directions) ===
Do only the stage named by this prompt. Work only in /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/week-24. Read current sources/current PDFs before editing. Revise only K–1 Problems 1–3 so children share pair-comparison work and pool a complete nine-outcome result for each deck comparison, instead of requiring each child to transcribe all 27 outcomes. Keep the exact decks, mathematics, all later problems and ALL other grade bands unchanged. A complete pooled comparison remains required, not random trials alone.
Do not change facilitator-src, guide-src, AGENTS.md, README indexes, current release folders, or bonus files. You are producing a draft for independent review, not a release. Keep source generator and generated TeX consistent. Use /Users/jamespfeiffer/math-circle/tmp/example-edit-env/bin/python for package dependencies. PDF rendering uses PyMuPDF if Poppler is absent. Copy changed draft PDF(s) into /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-24/draft and write /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-24/writer-notes.md with exact files, decisions, math checks, and original preserved tasks. Draft source remains in /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/week-24; do not run the top-level builder if it changes adult guides. Do not commit/push/upload. Follow current root AGENTS and student-page conventions.
