Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 24: Three random decks with no strongest deck

Unscheduled library slot, unpiloted. The core is nontransitivity of pairwise random comparison, distinct from optimizing mixed strategies in atlas AP-22. Finite card draws make the complete probability model visible. The writer chooses problems independently; examples and proofs below are answer information.

Mathematical kernels

1. Pairwise advantage can go in a circle. A deck has three equally likely physical cards. Draw one independently from each of two decks, and the larger number wins; return each card before another draw. Use A=(2,4,9), B=(1,6,8), C=(3,5,7). A beats B on five of the nine equally likely ordered card pairs, B beats C on five, and C beats A on five. In every comparison the other deck wins four, with no ties. All three deck totals are 15, so even their equal averages do not predict the advantage relation. The exact nine-pair comparison is a proof; observed frequencies from a few plays are not. The same distributions can be implemented by fair six-sided dice with every value repeated twice: A=(2,2,4,4,9,9), B=(1,1,6,6,8,8), C=(3,3,5,5,7,7). Each directed win count becomes 20 out of 36. Fairness and independence concern physical outcomes, not the number of different printed values.

2. Three faces are enough and, in the no-tie equal-size model, necessary. One-card decks are ordinary numbers and cannot form a strict dominance cycle. For two-card fair decks A=(a1,a2), B=(b1,b2), sorted within each deck, assume no value on one deck equals a value on the other. A wins a majority of the four pairs exactly when a1>b1 AND a2>b2. Necessity: if a1<b1, A's smaller card loses to both of B's cards, so A cannot win three pairs; if a2<b2, both of A's cards lose to B's larger card. Sufficiency: those two inequalities give the three wins a1>b1, a2>b1, a2>b2. This coordinatewise comparison is transitive, so three two-card decks cannot form a cycle. The three-card construction establishes the sharp threshold. This claim is about equally likely draws, no cross-deck ties, and winning more than half of pairs; do not silently extend it to biased coins, unequal deck sizes, or a tie-removal convention.

Sources: Brian Conrey, James Gabbard, Katie Grant, Andrew Liu, and Kent E. Morrison, Intransitive Dice, Mathematics Magazine 89 (2016), 133–143, author version pp. 1–2, https://arxiv.org/pdf/1311.6511 . Read 2026-10-03 for the equal-face model, pairwise comparison, and Efron's four-die cycle. The displayed three-deck example, its equal totals, and the no-tie two-card impossibility proof are independently checked here; no asymptotic conjecture from the paper is needed.

Suggested emphasis by level

- K–1: use adult-read three-card decks to establish a complete nine-pair win comparison and encounter a real three-way cycle; no fraction notation is required.
- Grades 2–3: construct or modify cyclic decks and distinguish a complete comparison from a lucky run of draws; organized case coverage is the principal prerequisite.
- Grades 4–5: design cycles under stated face restrictions and prove why one- and two-card fair no-tie decks cannot do the same thing.

Materials

For each of three tables: three labeled opaque draw bags or three identical-backed card decks, each containing three same-size 4 × 6 cm cards; nine spare blank cards; eighteen small counters in two distinguishable styles; and blank paper. Provide two copies of each numbered card only if deliberately representing six equiprobable faces; do not mix three-card and six-card denominators. Bag cards must be indistinguishable by touch, and each deck must be shuffled separately. Draws are independent and made with replacement between rounds. A full comparison can be made by laying each possible pair side by side, with no random trial equipment required. Use small numeral/dot combinations if helpful; numbers up to nine suffice. Repeated faces remain separate physical cards, and no hidden reroll or tie-discarding rule is permitted. Ordinary dice with stickers are optional and must not be assumed fair if their physical modifications affect rolling.


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

Your run folder is /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-24. Keep all your files inside it: sources in /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-24/draft/src/ and the three finished PDFs at exactly these paths:

  /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-24/draft/k-1.pdf
  /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-24/draft/grades-2-3.pdf
  /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-24/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.


=== AUTHORIZED TARGETED-REVISION CONTRACT (takes precedence over generic net-new directions) ===
Do only the stage named by this prompt. Work only in /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/week-24. Read current sources/current PDFs before editing. Revise only K–1 Problems 1–3 so children share pair-comparison work and pool a complete nine-outcome result for each deck comparison, instead of requiring each child to transcribe all 27 outcomes. Keep the exact decks, mathematics, all later problems and ALL other grade bands unchanged. A complete pooled comparison remains required, not random trials alone.
Do not change facilitator-src, guide-src, AGENTS.md, README indexes, current release folders, or bonus files. You are producing a draft for independent review, not a release. Keep source generator and generated TeX consistent. Use /Users/jamespfeiffer/math-circle/tmp/example-edit-env/bin/python for package dependencies. PDF rendering uses PyMuPDF if Poppler is absent. Copy changed draft PDF(s) into /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-24/draft and write /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/student-stages/week-24/writer-notes.md with exact files, decisions, math checks, and original preserved tasks. Draft source remains in /Users/jamespfeiffer/math-circle/tmp/fresh-review-revision-2026-10-04/week-24; do not run the top-level builder if it changes adult guides. Do not commit/push/upload. Follow current root AGENTS and student-page conventions.
