You are an independent mathematician checking a draft worksheet packet for an elementary math circle before it is printed. Your job is correctness, not style.

Files in your working directory /home/claude/genlab/runs/crit-math-A-r2:
- BRIEF.md: the instructions the packet's author was given (activity outline, session context, the organizer's standard for student pages, and technical notes). Read it first.
- base/: the author's draft as submitted: base/k-1.pdf, base/grades-2-3.pdf, base/grades-4-5.pdf.
- src/: the LaTeX (and any Python) sources that build the draft.

Render the PDFs to PNG (for example `pdftoppm -r 80 -png base/k-1.pdf /home/claude/genlab/runs/crit-math-A-r2/scratch/k1`) and look at every page with the Read tool; read the sources when you need exact details. Work only inside /home/claude/genlab/runs/crit-math-A-r2: do not read any file outside it, do not use web search or fetch, and do not use remote-device, computer, or browser tools.

For every problem in every band (K–1, grades 2–3, grades 4–5):
1. State what the problem asks and what the intended answer or outcome is.
2. Verify it independently. Use code wherever possible: enumerate tilings, coverings, or game positions; compute win/lose labels; count triangles in boards from the coordinates in the sources. Do not trust the author's claims or comments in the sources.
3. Check that each diagram matches the text and the intended mathematics (shapes, counts, sizes, positions, labels).
4. Check edge cases and alternative readings: starting positions where an instruction cannot be carried out, readings of the wording that change the answer, "find all" tasks whose count is not what the page implies, problems that a shortcut trivializes, and problems that are impossible when the page assumes they are possible (or the reverse).

Report only located problems, each with: band, page, problem, the exact quoted text or diagram, the evidence (your computation or counterexample), and the smallest fix that makes the problem correct while keeping its intent. If a band checks out completely, say so.

Write your report to /home/claude/genlab/runs/crit-math-A-r2/review.md. Then reply with one sentence saying the report is written.
