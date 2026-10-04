Task-specific encore scope (user instruction overrides the generic three-band output paths below):
For Week 25, produce ONE shared selected-band bonus companion, with at least three genuinely distinct investigations matching the outline. Output draft/bonus.pdf, sources draft/src/; reviser outputs final/bonus.pdf, sources final/src/. Ignore references below to three mandatory band PDFs. Select honest grade/readiness coverage; the adult guide will supply the route. Student header: Week 25 / <topic> encore / Grades <appropriate range>. Footer: Bellingham Math Circle / Week 25 / W25-BON-v1. Consecutive Problem N labels. A problem's requested action must be explicit. Printed suitable bands may be stated compactly in problem text if distinct from the overall coverage. Do not force young versions. No base packet, guide, global index or workflow-template edits. No uploads or publication. Material remains unpiloted. Your ONLY stage is the stage named in this file.
Build using /Library/TeX/texbin/pdflatex (portable scripts should find pdflatex on PATH or documented PDFLATEX override). Python with PyMuPDF/ReportLab/Pillow is /Users/jamespfeiffer/math-circle/tmp/encore-18-34-venv/bin/python. Render helper /Users/jamespfeiffer/math-circle/tmp/encore-18-34/tools/render.py supports --out and contact sheets. Portable sources must build without absolute project paths. No physical fit or rehearsal claim is permitted.
Writer: Choose actual investigations yourself, check they differ from base exclusions. Include all student working diagrams and light records. Prefer 3-5 pages per week, enough space over arbitrary compactness; no automatic page target. Record complete draft answers and assumptions separately at draft/answer-notes.md to support the adult guide, not on student pages. Keep PDF/source build and writer notes inside the run.
Critic: review draft/bonus.pdf and write review.md only. Math critic: independently verify every task and represented example in draft/bonus.pdf, write review-math.md plus executable independent-check.py and checks.json in the run; do not edit writer content. Reviser: copy draft/src into final/src, address both reviews, build final/bonus.pdf, render/inspect EVERY final page, and write final/revision-notes.md and final/answer-notes.md with corrected answers and assumptions. Do not write adult guide.

Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 25: Row and column shadows encore

Mathematical kernels

1. More shadow directions can help without recovering everything. Binary pictures on a fixed labeled square grid have row and column counts as before; now also give a separate count on every complete northwest-to-southeast diagonal, including length-one diagonals. A 3 × 3 picture with one counter in every row and column has six possibilities. Their diagonal counts, ordered from the bottom-left singleton through the main diagonal to the top-right singleton, distinguish four singleton possibilities and one pair. In row-string notation the pair is `100/001/010` and `010/100/001`; both have diagonal counts (0,1,1,1,0). Thus an extra direction can remove much ambiguity but does not necessarily establish uniqueness. A proof can be the complete six-picture list and checks, with no linear algebra prerequisite. A schematic worked non-task diagram must show which cells belong to a diagonal before children first use this shadow convention.

2. Revealing cells is an information game. Hide a 3 × 3 binary picture known to have one counter in every row and column, and allow a query to one labeled cell; reply occupied or empty. There are six possible pictures. Two yes/no replies have at most four histories, so no adaptive method can always identify the picture with two queries. Three are sufficient: query A1; if occupied, query B2 to settle the two remaining possibilities. If empty, query A2; either reply now fixes row A, and one suitable query in B settles the two remaining pictures. Hence the exact adaptive worst-case cost is three; naming the determined picture is free, not another query. If all queried cells must be chosen before any answer, four are necessary and sufficient. The top-left 2 × 2 cells suffice. To see that three cannot suffice, a separating choice would require distinguishing all six pairs that differ by a 2 × 2 permutation switch; for every pair of rows and every pair of columns at least one of their four intersection cells must be queried. Any three queried cells miss such a rectangle (check row distributions 3+0+0, 2+1+0, or 1+1+1, with the last case requiring the three columns all different and still leaving an unhit rectangle). This optional fixed-vs-adaptive distinction is a genuine deeper continuation, not obligatory scaffolding. Keep candidate pictures physically visible to the guesser.

3. Equal totals are necessary but insufficient for possible shadows. Row counts r_i and column counts c_j of a binary picture obey equal total sums and 0≤r_i≤number of columns, 0≤c_j≤number of rows. For any chosen k rows, their combined counter requirement is at most Σ_j min(k,c_j), since column j has only k cells in those rows and only c_j counters overall. A simple impossible 3 × 3 example has rows (3,3,0), columns (3,3,0): each local count is legal and both totals are six, but the two full rows require six counters while the columns can supply at most 2+2+0=4 in those rows. For a contrasting possible set, rows (3,2,1), columns (2,2,2) are realized by `111/110/001`. The full Gale–Ryser criterion says sorted row counts satisfying every such top-k inequality and the equal total admit a binary matrix; do not ask children to assume or prove this sufficiency. The concrete mathematical destination is a capacity obstruction, with children constructing examples and diagnosing why others cannot fit. Any repair task must specify what a change costs; avoid asserting a “fewest changes” theorem without solving that exact metric.

Sources: Current Week 25 packets and guide establish binary labeled pictures and ordinary shadows. The new diagonal examples and query bounds were independently derived and exhaustively checked for the six permutation pictures; the writer must not copy this answer list into student instructions. The capacity inequality follows directly from counting available cells in each column. Gale–Ryser is background only, not a source-dependent student prerequisite. The base outline cites Ryser (1957), §3, for switch connectivity; no claim that it supplies these query or diagonal tasks. Related existing Week 6 query games share the information idea but use score responses to whole binary words, whereas this encore exposes individual cells of a constrained picture.

Suggested emphasis by level

- K–1: Concrete entry to extra diagonal shadows through a demonstrated line count and counter placement; supported cell-reveal play with a visible six-picture catalog is also viable, without a worst-case proof requirement.
- Grades 2–3: Make and compare extra-shadow pictures, play cell-reveal games, and explain a small impossible count set using physical capacity.
- Grades 4–5: Certify residual ambiguity, prove the optimal three-query bound and optionally compare nonadaptive queries, then develop the selected-row capacity obstruction.

Materials

For each table: two reusable 3 × 3 grids with fixed A–C rows and 1–3 columns, twelve counters at most 18 mm wide, nine opaque square cover cards, row/column/diagonal count cards 0–3, pencils, six small reusable candidate-picture cards and blank paper. Work cells at least 22 mm square; a hidden board must have one cover per cell, and queries lift only the requested cover. Diagonal line labels must stay anchored at the correct border; use one consistent northwest-to-southeast direction and count every full diagonal, not just the main one. On the page supply sufficiently large working grids or explicitly use separate table mats. Use two unchanged reference boards when comparing shadow matches. Do not require concurrent shadow tables and move logs. Adult can read the rules and record counts; children should choose their queries and constructions.

Scope and exclusions

Create a separate shared `week-25/week-25-bonus.pdf` (header `Week 25 / Row and column shadows encore / Grades K–5`) and `week-25-bonus-facilitator.pdf`, sources in `source/week-25-bonus/`. Writer chooses exact substantial tasks, with three investigation directions and guide readiness routes; supported younger entry does not require a separate packet. Base exclusions: matching ordinary margins, enumerating ordinary-margin catalogs, finding/using rectangle switches, nested-row uniqueness, two-row shortest switches and diameter. Read base evidence: K–1 P1–6; 2–3 P1–5; 4–5 P1–5 in all current extracted student PDFs, plus the mathematical overview. None supplies diagonal shadows, cell-query limits, or impossible legal/equal-total margins. All encore material is unpiloted; cover-card procedure and printed working-cell fit are untested physically.


=== Session context ===

The Bellingham Math Circle is an elementary-school math circle that meets weekly for one hour. Its purpose is enjoyment, curiosity, and real mathematical thinking rather than school arithmetic practice.

Children at this session (group as of October 3, 2026; update this file when the group changes): eleven, at three fixed tables that do not mix. The K–1 table has two kindergartners and two first graders. The 2–3 table has four third graders. The 4–5 table has two fourth graders and one fifth grader.

Adults: three, one anchored at each table. The parent volunteer, who is not a mathematician, stays with the K–1 table. A second mathematician stays with the 2–3 table. The organizer, a research mathematician, stays with the 4–5 table.

Shape of the hour: the children arrive straight from school with a lot of energy, so the hour starts with about five minutes of running around. Then a short whole-group demonstration of the concrete action everyone will use, about thirty-five to forty minutes of work at the three tables, and a few minutes of sharing at the end.

What the first two sessions showed. A session where children tiled boards with pattern blocks went well: they loved handling the blocks, and the blocks themselves showed whether a move was legal and whether a board was filled. A session on paper lamp puzzles went poorly. Its rule (a move changes both lamps at the ends of a line) existed only on paper, and children kept changing just the lamp they wanted without noticing; many could not tell what they were being asked to do. So activities should be concrete: objects, drawings, movement, or two-player games, with the rules enforced by the materials or by the other player wherever possible. Children usually work in pairs at their table: two pairs at the K–1 and 2–3 tables, and at the 4–5 table a pair with the third child playing the adult or acting as referee, rotating. Deeper and more abstract questions belong late in each packet, where the quickest children will reach them; the first problems should let every child start doing something right away.

Pages are printed single-sided on US Letter paper at 100% scale.

Encore scope: these are optional return visits to a familiar theme. There is no requirement to finish them in one meeting. Choose entry by prerequisites. The requested output is a shared selected-band companion, with three distinct substantial investigations, rather than three redundant age variants. Grade labels are approximate; a K-1 version is not required when the mathematics has no honest K-1 entry.


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

Your run folder is /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-25-bonus-v1. Keep all your files inside it: sources in /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-25-bonus-v1/draft/src/ and the three finished PDFs at exactly these paths:

  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-25-bonus-v1/draft/k-1.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-25-bonus-v1/draft/grades-2-3.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-25-bonus-v1/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
