You are revising a worksheet packet for an elementary math circle.

Files in your run folder <RUN>:
- PROMPT.md: the instructions the packet's author was given (activity outline, session context, the organizer's standard for student pages, and technical notes). Read it first.
- draft/students.pdf, draft/students.pdf, draft/students.pdf: the author's draft.
- draft/src/: the sources that build the draft.
- review.md: a reviewer's review of the draft. If review-math.md exists, it is a second review focused on correctness.

You are the revision stage of the worksheet workflow: do the revision yourself and do not start the workflow again.

Revise the packet to address the review. Copy draft/src/ to final/src/, edit the copy, and build the three PDFs at exactly these paths:

  <RUN>/final/students.pdf
  <RUN>/final/students.pdf
  <RUN>/final/students.pdf

Before you finish, render every page of the rebuilt PDFs to images and look at each one to check that the diagrams are correct and nothing overflows or overlaps. Reply with the three PDF paths and their page counts, in under 80 words.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.

Coordinator execution notes: Address the critic and preserve all seven substantial problems. The complete fixed-input reshaping example must show both new side lengths. Clarify that Problem 3's tightest bracket is among the four old/new side lengths. Provide exact-quotient support before the first nonterminating division; calculators must not turn rounded values into guaranteed endpoints. Problem 4 needs usable movable cards; if the design uses a second copy of a page, record the exact preparation in revision.md. Do not edit the separate facilitator guide. Write revision.md with changes and remaining physical rehearsal limits.
