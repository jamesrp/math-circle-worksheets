You will simulate the actual session, band by band, to find where these pages will fail in the room. Nothing else about the packet matters to you: only what real children will do with it.

Files in your working directory /home/claude/genlab/runs/crit-sim-B-r2:
- BRIEF.md: the instructions the packet's author was given (activity outline, session context, the organizer's standard for student pages, and technical notes). Read it first.
- base/: the author's draft as submitted: base/k-1.pdf, base/grades-2-3.pdf, base/grades-4-5.pdf.
- src/: the LaTeX (and any Python) sources that build the draft.

Render the PDFs to PNG (for example `pdftoppm -r 80 -png base/k-1.pdf /home/claude/genlab/runs/crit-sim-B-r2/scratch/k1`) and look at every page with the Read tool; read the sources when you need exact details. Work only inside /home/claude/genlab/runs/crit-sim-B-r2: do not read any file outside it, do not use web search or fetch, and do not use remote-device, computer, or browser tools.

Cast the children from the session context and keep them realistic:
- K–1: two kindergartners who cannot read and count reliably to about twenty, and one first grader who reads a few simple words. The adult (a parent volunteer, not a mathematician) reads each problem aloud exactly as printed.
- Grades 2–3: four third graders of mixed strength, one of them quick and impatient.
- Grades 4–5: two fourth graders and one fast fifth grader, with a mathematician nearby.
Children use the physical materials named in the brief. They interpret ambiguous wording literally or in the most natural wrong way, cannot draw small precise figures, lose interest in repetitive copying, race through tasks that are too easy, and give up on tasks whose goal they cannot see. Do not be charitable to the page.

For each band, go problem by problem. In a few lines per problem, narrate what each child actually does: what they think they are being asked, what they try first, where they get stuck or misread, what they ask the adult and whether the adult can answer from the page, whether they can record at the printed sizes, roughly how many minutes they spend, and whether they are engaged or bored. Keep a running clock for the quick child and note when they would run out of work.

Then list the concrete problems the simulation exposed. For each: band, page, problem, the exact quoted text or diagram involved, what went wrong in the simulation, and the smallest fix. Leave out anything that did not cause trouble in the simulation. End with the quick child's minutes of engaged work for each band.

Write everything to /home/claude/genlab/runs/crit-sim-B-r2/review.md. Then reply with one sentence saying the review is written.
