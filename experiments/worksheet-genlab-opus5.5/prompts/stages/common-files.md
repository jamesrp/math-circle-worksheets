Files in your working directory {{RUN_DIR}}:
- BRIEF.md: the instructions the packet's author was given (activity outline, session context, the organizer's standard for student pages, and technical notes). Read it first.
- base/: the author's draft as submitted: base/k-1.pdf, base/grades-2-3.pdf, base/grades-4-5.pdf.
- src/: the LaTeX (and any Python) sources that build the draft.

Render the PDFs to PNG (for example `pdftoppm -r 80 -png base/k-1.pdf {{RUN_DIR}}/scratch/k1`) and look at every page with the Read tool; read the sources when you need exact details. Work only inside {{RUN_DIR}}: do not read any file outside it, do not use web search or fetch, and do not use remote-device, computer, or browser tools.
