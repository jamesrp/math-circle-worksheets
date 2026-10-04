You are revising a worksheet packet for an elementary math circle.

Files in your run folder {{RUN_DIR}}:
- PROMPT.md: the instructions the packet's author was given (activity outline, session context, the organizer's standard for student pages, and technical notes). Read it first.
- draft/k-1.pdf, draft/grades-2-3.pdf, draft/grades-4-5.pdf: the author's draft.
- draft/src/: the sources that build the draft.
- review.md: a reviewer's review of the draft. If review-math.md exists, it is a second review focused on correctness.

You are the revision stage of the worksheet workflow: do the revision yourself and do not start the workflow again.

Revise the packet to address the review. Copy draft/src/ to final/src/, edit the copy, and build the three PDFs at exactly these paths:

  {{RUN_DIR}}/final/k-1.pdf
  {{RUN_DIR}}/final/grades-2-3.pdf
  {{RUN_DIR}}/final/grades-4-5.pdf

Before you finish, render every page of the rebuilt PDFs to images and look at each one to check that the diagrams are correct and nothing overflows or overlaps. Reply with the three PDF paths and their page counts, in under 80 words.
