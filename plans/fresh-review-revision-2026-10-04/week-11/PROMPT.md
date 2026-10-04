Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 11: Chip-firing with a sink (draft library slot, not a scheduled meeting)

Mathematical kernels

1. Many legal choices, one final result. Take a finite connected undirected graph with one distinguished sink. A nonsink vertex holding at least its degree in chips may fire: send exactly one chip along each incident edge, including edges to the sink. The sink keeps chips and never fires; a stable vertex has fewer chips than its degree. Every legal firing sequence continued until no move is available terminates, with the same final configuration and the same firing count at each vertex. For termination, an infinitely firing vertex would force its neighbors, and eventually a neighbor of the sink, to fire infinitely often; finitely many chips cannot supply infinitely many losses. For uniqueness, compare a legal sequence with a completed one and consider the first vertex about to exceed its completed firing count. It has received no more chips, and has fired just as often, as in the completed state, so it cannot be active. Reverse the comparison for equality. On the triangle with vertices A, B, sink, the initial piles (2,2), (4,0), (3,3) stabilize respectively to (1,1), (1,0), (1,1), with firing counts (1,1), (2,1), (2,2). On the four-cycle sink–A–B–C–sink, (0,4,0) stabilizes to (1,0,1) with firing counts (1,3,1). These are checked reference instances, not a required problem sequence. Without an absorbing sink the termination statement is false.

2. Add a batch now or later. Write S(x) for stabilization. For nonnegative chip configurations x and y on the same sink graph, S(S(x)+y)=S(x+y). A legal firing sequence for x remains legal when the extra chips y are already present; complete stabilization and use uniqueness. Consequently the order of adding chips at different vertices, with stabilization between additions, cannot change the final state. The operation x⊕y=S(x+y) on stable configurations is associative and commutative. It need not be reversible. On the triangle above, repeatedly adding one chip at A and stabilizing sends (0,0) to (1,0), then (0,1), then (1,1), then back to (1,0). Thus four stable states include a three-state cycle and a state outside that cycle; do not claim all stable states form a group. This is a concrete entrance to abelian dynamics, rather than a disguised arithmetic-carrying exercise.

Sources: Holroyd, Levine, Mészáros, Peres, Propp, and Wilson, “Chip-Firing and Rotor-Routing on Directed Graphs,” §2, Lemmas 2.2–2.5 and Corollary 2.6, manuscript pp. 3–5, https://arxiv.org/pdf/0801.3306 (definitions, order independence, termination, staged additions); Levine and Propp, “What is a sandpile?”, author manuscript pp. 1–2, https://lionellevine.github.io/what-is-a-sandpile.pdf (finite sink model and the stable-configuration commutative monoid). Small examples and exhaustive finite checks are original to this outline and recorded in plans/corpus-2026-10-03/check-discrete-kernels-results.json.

Suggested emphasis by level:
K–1: legal chip-sharing on tiny boards and comparing final piles after different choices; spoken rules and small counts suffice, with an adult handling notation.
Grades 2–3: order-independent stabilization and the distinction between final piles and how often each place fires; small addition/subtraction and careful move tracking.
Grades 4–5: staged addition, repeated-addition state cycles, and an explanation of why different legal orders agree; no matrix algebra or formal group vocabulary is required.

Materials

Preparation specification for ten children: 24 identical counters per child (240 total), each at most 20 mm wide; use existing counters if they fit, otherwise cut 20 mm paper squares. Provide each child a reusable US Letter board sheet and a separate 60 mm square sink area, plus pencil/eraser and spare paper; existing small whiteboards may replace recording paper. Each working vertex must have a clear region at least 40 mm across, allowing a small pile rather than one marked slot per chip, and edges must remain visible when piles are present. The printed sink is part of the graph, not an ordinary pile children may fire. If the sink is drawn in more than one place for layout, all copies must be explicitly marked as the same collecting sink. No loose sand, random rolls, larger denomination counters, borrowing, or negative chips. Drawn chips on a whiteboard are an exact fallback. All diagrams intended for counter placement must fit single-sided US Letter at 100% scale. The counts and sizes here are a proposed preparation specification; the current stock of counters has not been measured.


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

Your run folder is /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-11. Keep all your files inside it: sources in /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-11/draft/src/ and the three finished PDFs at exactly these paths:

  /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-11/draft/k-1.pdf
  /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-11/draft/grades-2-3.pdf
  /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-11/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.


=== AUTHORIZED TARGETED-REVISION CONTRACT (takes precedence over generic net-new directions) ===
Do only the stage named by this prompt. Work only in /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/week-11. Read current sources/current PDFs before editing. Revise only the recording burden in all three student bands. Preserve every mathematical task and every Grades 4–5 investigation. Record a chronological firing word plus the final piles; derive firing counts afterwards. Provide a small non-task worked convention if necessary. No concurrent count tallies. Keep boards at exactly current physical dimensions.
Do not change facilitator-src, guide-src, AGENTS.md, README indexes, current release folders, or bonus files. You are producing a draft for independent review, not a release. Keep source generator and generated TeX consistent. Use /Users/jamespfeiffer/math-circle/tmp/example-edit-env/bin/python for package dependencies. PDF rendering uses PyMuPDF if Poppler is absent. Copy changed draft PDF(s) into /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-11/draft and write /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-11/writer-notes.md with exact files, decisions, math checks, and original preserved tasks. Draft source remains in /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/week-11; do not run the top-level builder if it changes adult guides. Do not commit/push/upload. Follow current root AGENTS and student-page conventions.
