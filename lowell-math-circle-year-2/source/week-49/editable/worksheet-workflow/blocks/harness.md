Technical instructions

You are the writer stage of the worksheet workflow. Write the pages yourself from this brief; do not start the workflow again or hand the work to other agents.

Your run folder is {{RUN_DIR}}. Keep all your files inside it: sources in {{RUN_DIR}}/draft/src/ and the three finished PDFs at exactly these paths:

  {{RUN_DIR}}/draft/k-1.pdf
  {{RUN_DIR}}/draft/grades-2-3.pdf
  {{RUN_DIR}}/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
