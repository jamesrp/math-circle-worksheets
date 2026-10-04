You are making targeted corrections to a worksheet packet for an elementary math circle. The draft is already close to what the organizer wants; your job is to fix the specific issues reported, and nothing else.

Files in your working directory /home/claude/genlab/runs/B4-A-r1:
- BRIEF.md: the instructions the packet's author was given (activity outline, session context, the organizer's standard for student pages, and technical notes). Read it first.
- base/: the author's draft as submitted: base/k-1.pdf, base/grades-2-3.pdf, base/grades-4-5.pdf.
- src/: the LaTeX (and any Python) sources that build the draft.

Render the PDFs to PNG (for example `pdftoppm -r 80 -png base/k-1.pdf /home/claude/genlab/runs/B4-A-r1/scratch/k1`) and look at every page with the Read tool; read the sources when you need exact details. Work only inside /home/claude/genlab/runs/B4-A-r1: do not read any file outside it, do not use web search or fetch, and do not use remote-device, computer, or browser tools.
- review.md: a report of issues found in the draft.

Rules:
1. Check each reported issue against the draft yourself. If an issue is mistaken, or its fix would make the page worse for children, skip it.
2. For each issue you accept, make the smallest change that fixes it. Do not reword, restyle, reorder, or reorganize anything an accepted issue does not require.
3. Do not add sentences, hints, encouragement, headings, labels, or explanations, except where an accepted issue requires new content (for example missing recording space, a missing rule, or work to fill an under-filled band). Anything you add follows the organizer's standard in BRIEF.md.
4. If you change a problem, solve it again and make sure the diagrams still match.
5. Edit the sources in src/ and rebuild the three PDFs at exactly these paths:
     /home/claude/genlab/runs/B4-A-r1/final/k-1.pdf
     /home/claude/genlab/runs/B4-A-r1/final/grades-2-3.pdf
     /home/claude/genlab/runs/B4-A-r1/final/grades-4-5.pdf
   Render every page of the rebuilt PDFs to PNG and look at each one with the Read tool before you finish.
6. Write /home/claude/genlab/runs/B4-A-r1/revision-notes.md listing every reported issue as fixed (what you changed) or skipped (why).

Reply with the three PDF paths and their page counts, in under 80 words.
