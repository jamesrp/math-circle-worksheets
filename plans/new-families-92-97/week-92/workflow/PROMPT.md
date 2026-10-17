Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 92: Fold-and-stretch predictions

Mathematical kernels

1. A deterministic map can amplify uncertainty about its initial state. On a continuous track from 0 to 16, send a point to twice its distance from the nearer end: T(x)=2 min(x,16-x). The point may be between ticks. This is one complete move, repeatedly applied on the same track. On either half, distances between points double, but points on opposite sides can merge: T(x)=T(16-x). Pair separations can shrink or vanish. Whole interval widths never decrease, but strict increase can fail for a symmetric band crossing the midpoint. The image of a whole interval is the complete range of possible outputs, not only the outputs of its endpoints. If it includes the middle 8, its maximum output is 16. Example [7,9] maps to [14,16], then [0,4], [0,8], [0,16]. All endpoints here are included. Each state represents uncertainty about one unchanged deterministic run, not a new random choice at each step. Intervals are not probability distributions.

2. For every n>=1, each dyadic cell [16k/2^n,16(k+1)/2^n], 0<=k<2^n, maps onto the entire track after n moves. A direct fold-and-stretch induction shows T^n is affine and onto on each such cell, with alternating direction. Every nonzero-width interval contains a sufficiently small complete dyadic cell, so its iterates eventually cover the track. Initial intervals may grow or keep their widths for a while; they never shrink. Eventual full coverage is the theorem. Across midpoint8 the image width is twice the larger of the two half-widths, at least their sum. The exact point 0 stays at 0, but [0,16/2^n] fills the track after n steps: limited initial precision limits guaranteed prediction. Whole-number marks on a length-16 track all eventually reach 0, but that is an artifact of this finite dyadic grid, not a theorem about all real starts. The fixed point 32/3 supplies a counterexample; the fractional point is adult continuation unless introduced concretely.

Sources: Gerald Teschl, Ordinary Differential Equations and Dynamical Systems, §§11.3-11.5 (tent maps and distinctions surrounding chaos), https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf . Exact interval-image formulas, dyadic-cell proof, and scaled examples are independently derived. Existing atlas GA-10 student pp.33-36 studies periodic itineraries, inverse affine composition and cycle counts. This is a NEW INVESTIGATION WITHIN THAT EXISTING THEME, not a claim of a new theme. Do not repeat its word-programming and cycle-inventory tasks. Week51 introduces static guaranteed ranges; here ranges evolve under a nonlinear map. Week46's overwrite process loses initial differences; this rule can merge a pair yet expand a whole uncertainty interval. Week20 harmonic averaging/dynamics/energy, Week49 Ducci termination, reserved Week86 pursuit and Week89 discrete calculus are excluded.

Suggested emphasis by level

- K-1: oral optional paired token/folding demonstration only, with an adult; no forced K-1 packet.
- Grades 2-3: concrete tokens, doubling small distances, finding starts that merge or separate, and moving whole shaded intervals using the apparatus; adult reading is normal. No formulas or fractional calculations required.
- Grades 4-5: exact possible ranges, a counterexample to endpoint-only reasoning, constructing long-lived precision, and a dyadic subdivision proof as a readiness-dependent continuation. Understanding every position in a strip, not only numbered marks, is essential.

Materials

Per pair: two 160-mm tracks representing 0-16 with 10-mm unit spacing, two markers, transparent or paper interval strips, ruler, scissors, pencils and whiteboard. Provide an explicit physical rule aid: folding overlay maps both ends toward 0 and the middle toward 8, then a doubled-scale output track turns 0-8 into 0-16. A simpler V-shaped input-to-output map or matched distance strips can serve if mechanically unambiguous. Include a complete small worked visual BEFORE first use: point input, measured nearer-end distance, doubled output. BEFORE the first whole-range task, a non-task interval crossing the midpoint must visibly include the midpoint and show the entire resulting output band; matching labels on every view. Choose a non-task example; the outline examples are mathematical data, not prescribed problems. Give an area to mark possible ranges and enough room for independent experiments, without a long diary table. Launch together after children handle the materials; the apparatus has not been physically rehearsed. Print 100% only if ruler dimensions matter; exact tick coordinates, not paper tolerances, certify answers.


=== Session context ===

The Bellingham Math Circle is an elementary-school math circle that meets weekly for one hour. Its purpose is enjoyment, curiosity, and real mathematical thinking rather than school arithmetic practice.

Children at this session (group as of October 3, 2026; update this file when the group changes): eleven, at three fixed tables that do not mix. The K–1 table has two kindergartners and two first graders. The 2–3 table has four third graders. The 4–5 table has two fourth graders and one fifth grader.

Adults: three, one anchored at each table. The parent volunteer, who is not a mathematician, stays with the K–1 table. A second mathematician stays with the 2–3 table. The organizer, a research mathematician, stays with the 4–5 table.

Shape of the hour: the children arrive straight from school with a lot of energy, so the hour starts with about five minutes of running around. Then a short whole-group demonstration of the concrete action everyone will use, about thirty-five to forty minutes of work at the three tables, and a few minutes of sharing at the end.

What the first two sessions showed. A session where children tiled boards with pattern blocks went well: they loved handling the blocks, and the blocks themselves showed whether a move was legal and whether a board was filled. A session on paper lamp puzzles went poorly. Its rule (a move changes both lamps at the ends of a line) existed only on paper, and children kept changing just the lamp they wanted without noticing; many could not tell what they were being asked to do. So activities should be concrete: objects, drawings, movement, or two-player games, with the rules enforced by the materials or by the other player wherever possible. Children usually work in pairs at their table: two pairs at the K–1 and 2–3 tables, and at the 4–5 table a pair with the third child playing the adult or acting as referee, rotating. Deeper and more abstract questions belong late in each packet, where the quickest children will reach them; the first problems should let every child start doing something right away.

Pages are printed single-sided on US Letter paper at 100% scale.


The organizer's standard for student pages

Who uses the page. Children work in small groups at a table with an adult beside them. The adult supplies the warmth, the hints, the explanations, and the encouragement in person, so the page has one job: pose the tasks clearly and give room to work. Kindergartners and first graders mostly cannot read yet. An adult reads each problem aloud to them, so their problems must make sense after one hearing and should lean on pictures and objects.

What a page contains. A one-line header giving the week, topic, and level, for example "Week 1 / Tiling / Grades 2–3". A one-line footer, "Bellingham Math Circle / Week N / <packet id>" (for example F03-K-v1), with the page number. Between them, numbered problems, each beginning "Problem N:" and continuing in ordinary sentences. Rules that hold for the whole packet may be stated once, briefly, at the top of the first page. Each problem says what to do with the specific objects involved, shows the diagrams the child needs, and leaves space to record. The header and the problem labels are the only headings on the page.

Substantial problems. A numbered problem should give a child at least five minutes of real experimenting and thinking without needing another instruction. Several purposeful, contrasting cases can sit under one question, such as four boards to try or three pile sizes to play, rather than many tiny questions. The choice and order of the problems carries the mathematical development: a child meets an idea in concrete cases, and uses it, before being asked to explain or generalize it.

The method belongs to the child. State the goal and the essential rules, then stop. Choosing an approach, noticing a pattern, and organizing the work are the mathematics. Hints, suggested steps, and solution ideas stay with the adults, who give them when a child needs them. Ask for an explanation where explanation is the point (why something is impossible, why a packing is best, why a list is complete, why a strategy always wins), not after every task.

Enough work for the hour. Children have about forty minutes of working time. A quick child in any band should not run out, so write more than most children will finish, in an order where stopping anywhere is fine. That usually means four or more pages per band.

K–1 gets real mathematics. Young children can decide whether something is possible, find every way to do something, look for the fewest pieces, and work out how to win a game, when the task is posed with objects and few words. Give K–1 the same mathematical ideas as the older bands at a smaller scale, and as much to do as the other bands. Keep each K–1 problem to one or two short sentences and let the pictures and objects carry the rest.

Be concrete. Name the exact pieces and the exact starting position, draw every board or position the child needs at a size they can work on, and use specific numbers. A task that says "try other shapes" without giving the shapes leaves a child with nothing to start from.

Plain language. Short sentences and everyday words, the way a teacher talks at the table. Write "explain" rather than "prove". Introduce a new word or notation only after the child has used the idea it names, and only if it helps.


Leave these off the student pages. The organizer deletes them by hand every time they appear.

- Titles or headings other than the page header and the "Problem N:" labels: no activity names, section names, or labels such as Warm-up, Challenge, Bonus, Think about it, Fun fact, or Did you know.
- Encouragement, praise, or manufactured excitement: no "Great job", "You've got this", "Have fun", and no exclamation marks.
- Talk about the activity itself: "In this activity you will…", "Today we explore…", "Let's…".
- Cute framing that does not carry the mathematics: mascots, characters, themed names for ordinary things, emoji.
- Writing tics: "not X but Y" or "it's not just X, it's Y" contrasts, lists of three for rhythm, dashes used for asides.
- Hints, method suggestions, worked answers, or "remember…" reminders.
- Automatic follow-ups after each task ("Explain your thinking", "What do you notice?", "Compare with a partner") when they are not the point of the problem.
- Small lettered sub-steps that do the planning for the child.
- A K–1 packet that is easier or shorter than the mathematics allows, or that ends after a few quick tasks.
- Vague tasks without the specific objects, numbers, or diagrams a child needs to start.
- Sentences that describe a diagram or say what the blank spaces are for ("Here are seven rules.", "The small boards are for recording."). The picture and the task already say it.


Examples of the register the organizer wants

These problems come from math circles the organizer admires; the theater problem and the walking problem are from his own handouts. Their topics are unrelated to this week. Use them for voice, length, and concreteness, not content. Notice what they leave out: no titles, no encouragement, no hints, and a clear statement of what the child should produce.

From a grades 1–4 circle (often read aloud to the youngest):
  Place three chairs in a square room, so that there is a chair by each wall.
  Place four chairs in a square room, so that there are two chairs by each wall.

From the organizer's handouts, with a picture of four numbered seats:
  Problem 2.1: Horse, Cow, Dog, and Cat went to a theater and sat in a row of four seats. Here is what I heard afterwards:
  • Cow and Cat took the seats on the ends.
  • Dog's seat number and Cow's seat number were bigger than Horse's seat number.
  Write the name of each animal above the chair it sat in.

From a grades 1–3 circle:
  Yesterday Mister Jameson made 7 cuts and got 14 pieces of sausage. How many whole sausages did Mister Jameson cut yesterday?
  Last week Mister Jameson made 7 cuts but he got 10 pieces. How many whole sausages did Mister Jameson cut last week?

From a grades 1–3 circle:
  I have a few marbles in my pocket, at least one but no more than eight. I can answer questions with "yes" or "no". Can you guess the number of marbles in my pocket by asking me just three questions?

From a grades 1–5 circle, with a picture of a cone holding two scoops side by side:
  Ann can put two scoops of ice cream in her cone side by side. She must select two different flavors out of vanilla, chocolate, pistachio, and strawberry. How many different ice cream cones can she make?

From the organizer's handouts, with a street grid and sixteen small blank copies of it:
  Problem 4.6: Mary is walking from her house to her school. Her house (the red square) is three blocks south and three blocks west of her school (the red star). She has to walk six blocks total, but there are lots of options for how she could walk. For instance, she could go three blocks east and then three blocks north (EEENNN). Or she could go two blocks east, three blocks north, one block east (EENNNE). How many ways can you find for Mary to walk to school? If you run out of space below, you can draw more grids on the back.

From a family math puzzle series:
  You have five big bags of coins. Each bag has only one kind of coin. The bags have coins worth 1, 3, 5, 7, and 9. If you can, find ten coins that add up to 43. If you can't, explain why it is impossible.


Technical instructions

You are the writer stage of the worksheet workflow. Write the pages yourself from this brief; do not start the workflow again or hand the work to other agents.

Your run folder is <RUN>. Keep all your files inside it: sources in <RUN>/draft/src/ and the three finished PDFs at exactly these paths:

  <RUN>/draft/students.pdf
  <RUN>/draft/students.pdf
  <RUN>/draft/students.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.


=== Authorized run-specific output override ===
This family intentionally has no forced K-1 packet. Deliver one consolidated draft/students.pdf with pages labeled Grades 2-3 or Grades 4-5 as appropriate, and continuous problem numbering. Aim for 4-6 substantial student pages, not a fixed quota. This overrides the generic three-band output requirement only; do not edit shared workflow templates. Use a portable LaTeX/TikZ source and build.py in draft/src. Available pdflatex: /Library/TeX/texbin/pdflatex. PDF render/extraction Python: /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf available). Render with pymupdf and view every page using tools.view_image. Keep deterministic compilation (set SOURCE_DATE_EPOCH, FORCE_SOURCE_DATE, and PDF metadata as needed). Do only the writer stage; no guide, no reviewer stage, no git push. Do not inspect other existing worksheets; use the assembled brief.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.
