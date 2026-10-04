You are the second reader for a draft worksheet packet for an elementary math circle. The organizer will hand your findings to a reviser who changes only what you report, so report precisely, and report only what matters in the room.

Files in your working directory /home/claude/genlab/runs/B2-A-r1:
- BRIEF.md: the instructions the packet's author was given (activity outline, session context, the organizer's standard for student pages, and technical notes). Read it first.
- base/: the author's draft as submitted: base/k-1.pdf, base/grades-2-3.pdf, base/grades-4-5.pdf.
- src/: the LaTeX (and any Python) sources that build the draft.

Render the PDFs to PNG (for example `pdftoppm -r 80 -png base/k-1.pdf /home/claude/genlab/runs/B2-A-r1/scratch/k1`) and look at every page with the Read tool; read the sources when you need exact details. Work only inside /home/claude/genlab/runs/B2-A-r1: do not read any file outside it, do not use web search or fetch, and do not use remote-device, computer, or browser tools.

Go through each band (K–1, grades 2–3, grades 4–5) problem by problem and check:

1. Mathematics. Solve the problem yourself. Is it correct and well posed? Can a child of this band actually do it? Is it trivially answerable by a shortcut the author did not intend, or impossible in a way the author did not intend? Do the diagrams match the text (counts, shapes, positions)? Check edge cases, such as particular starting positions, that break a general instruction. Use code where it helps.
2. Clarity. Read it as the adult reading aloud to a K–1 child, or as the child in grades 2–5. Is it clear what to do and when the task is done? Are references unambiguous (for example "the board" when two boards have been shown)? Are the rules the problem relies on stated where the child needs them?
3. Concreteness and workspace. Is every object, board, and position the child needs drawn? Is the recording space big enough for what a child of this age can actually draw or write?
4. Level and amount. Is each problem pitched right for the band? Would a quick child in this band have about forty minutes of substantial work? Is K–1 doing real mathematics rather than busywork?
5. Giving the thinking away. Does the page print the method or the answer: hints, step-by-step directions that do the planning, or an earlier problem that answers a later one?
6. Words that do no work. Any sentence a strict editor would delete: narration about the activity, encouragement, titles, rules repeated from earlier, prose that restates a diagram.
7. Format. Each page has the one-line header and footer described in the brief, and numbered problems labeled "Problem N:".

For every issue, give: band, page, problem; the exact quoted text or a precise description of the diagram; what will actually go wrong with children; and the smallest fix. Mark each issue MUST (wrong, broken, or will confuse children) or SHOULD (clear improvement). Leave out matters of taste and anything you would not bother to fix if you were the organizer. If a band needs no changes, write "no change needed" for it; that is a good outcome, not a failure.

Write your findings to /home/claude/genlab/runs/B2-A-r1/review.md. Then reply with one sentence saying the review is written.
