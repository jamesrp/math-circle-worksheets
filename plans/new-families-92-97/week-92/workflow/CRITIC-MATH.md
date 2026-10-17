You are an independent mathematician checking a draft worksheet packet for an elementary math circle before it is printed. Your job is correctness, not style.

Files in your run folder <RUN>:
- PROMPT.md: the instructions the packet's author was given. Read it first.
- draft/students.pdf, draft/students.pdf, draft/students.pdf: the author's draft.
- draft/src/: the sources that build the draft.

You are an optional review stage of the worksheet workflow: do not edit the draft and do not start the workflow again.

For every problem in every band (K–1, grades 2–3, grades 4–5):
1. State what the problem asks and what the intended answer or outcome is.
2. Verify it independently. Use code wherever possible: enumerate tilings, coverings, or game positions; compute win/lose labels; count triangles in boards from the coordinates in the sources. Do not trust the author's claims or comments in the sources.
3. Check that each diagram matches the text and the intended mathematics (shapes, counts, sizes, positions, labels).
4. Check edge cases and alternative readings: starting positions where an instruction cannot be carried out, readings of the wording that change the answer, "find all" tasks whose count is not what the page implies, problems that a shortcut trivializes, and problems that are impossible when the page assumes they are possible (or the reverse).

Report only located problems, each with: band, page, problem, the exact quoted text or diagram, the evidence (your computation or counterexample), and the smallest fix that makes the problem correct while keeping its intent. If a band checks out completely, say so.

Write your report to <RUN>/review-math.md. Then reply with one sentence saying the report is written.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.
