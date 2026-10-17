Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 93: Squaring a rectangle

Mathematical kernels

1. A rectangle with positive sides a<=b has the same area as a square with a side between a and b. Setting m=(a+b)/2 and h=ab/m gives a new equal-area rectangle with a<=h<=sqrt(ab)<=m<=b. Equality of h and m occurs exactly when a=b. The key area identity m^2-ab=((b-a)/2)^2 can be shown by cutting and rearranging a rectangle inside an m-by-m square, leaving one small square uncovered. This is a geometric arithmetic/geometric mean comparison, not a formula to memorize. Repeating the equal-area adjustment gives nested short-side/long-side bounds for one fixed square. The new gap m-h=(b-a)^2/[2(a+b)] is less than half the previous gap for unequal positive sides, hence the brackets shrink to the unique square side. Near equality the gap decreases quadratically. The exact finite bounds are meaningful without claiming finitely many moves reach an irrational side.

2. Merely replacing both sides by their average changes area: the extra area is exactly the small gap-square above. Preserving area is the reason for finding the second new side by division. A concrete exact chain for area12 is (2,6)->(3,4)->(24/7,7/2); its gaps are4,1,1/14. Area36 begins (4,9)->(72/13,13/2), bracketing the known square side6. These are facilitator calibration data, not a mandated problem sequence. Comparing equal-area rectangles with different starting shapes should put the geometric destination before numerical work. Approximate decimals must never silently become exact certificates: check proposed lower/upper sides by squaring, or supply exact fraction cards. Avoid lengthy calculator iteration, bisection, tangent graphs, and generic Newton pathologies already in atlas GA28/AP06.

Sources: Driscoll and Braun, Fundamentals of Numerical Computation, §4.3, https://fncbook.com/newton/ (Newton update and quadratic convergence context). The rectangle construction, area identity, nested enclosure and exact gap proof are independently derived here. This is the square-root specialization of Newton's method, but children need neither derivatives nor that name. Historical claims about who invented it are not part of this activity. Connections: Week48 inside/outside area certificates and Week51 honest ranges become a dynamically improving side-length certificate; Week20 averages do not preserve area, and its harmonic/energy investigation is not repeated. The primary novelty is a nonlinear area-preserving iteration with an explicit error certificate.

Suggested emphasis by level

- K-1: no packet; this family has genuine area and multiplicative prerequisites.
- Grades 2-3: optional concrete entry for children who understand equal-area rectangular arrays and halves: cut/rearrange, compare rectangles, and locate a square side between short and long sides. Adult reading/recording is appropriate, but adults should not operate the investigation for them.
- Grades 3-5: main route requires rectangular area, halves, division and comparing supplied fractions; calculators or exact prepared side cards remove arithmetic load. Distinguish geometric experiments from exact area and bound checks.
- Grades 4-5 ready continuation: explain the uncovered square and why every round improves a guaranteed bracket; general algebraic gap proof stays with adults unless children are ready.

Materials

Per pair: squared paper, at least30 equal square tiles, two copies of paper rectangles for cutting, scissors, ruler, pencil, whiteboard, and optionally a four-function calculator. Printed rectangles used for cutting must have equal horizontal/vertical scale, clearly labeled actual dimensions and manageable cuts; use large physical examples rather than tiny fraction cells. Non-task worked visual before first adjustment: input rectangle with both sides, half-sum side construction as the meaningful intermediate step, output equal-area rectangle with both sides. State why we are reshaping: make the same area closer to a square and trap its unknown side. Any exact fractional cards needed for later iterations must be supplied and their role explained. Do not require children to draw 1/7-mm strips or reconstruct large tables; the mathematics is the area and guarantee, not paper precision. A conceptual diagram can be marked not to scale; cutting diagrams cannot. One short shared demonstration follows handling the tiles. Physical material rehearsal and classroom piloting are untested.


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
This family intentionally has no forced K-1 packet. Deliver one consolidated draft/students.pdf with pages labeled Grades 3-5 or Grades 4-5 as appropriate, and continuous problem numbering. An optional 2-3 area entry may be included without pretending the whole family is accessible there. Aim for 4-6 substantial student pages, not a fixed quota. This overrides the generic three-band output requirement only; do not edit shared workflow templates. Use portable LaTeX/TikZ and build.py in draft/src. Available pdflatex: /Library/TeX/texbin/pdflatex. PDF render/extraction Python: /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Render and view every page. Use deterministic compilation settings. Do only writer stage; no guide, reviews or git push. Do not inspect other worksheets; use the assembled brief. Fraction cards may remove arithmetic load, but do not give away the main comparison or identity as a procedural recipe.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.


Run-specific override: use the consolidated students.pdf, with the honest age/readiness bands in the writer brief. Do only this stage. pdflatex is /Library/TeX/texbin/pdflatex; render Python is /tmp/math-circle-feedback-20261017/tmp/qa-venv/bin/python (pymupdf). Do not edit shared workflow templates or push Git.
