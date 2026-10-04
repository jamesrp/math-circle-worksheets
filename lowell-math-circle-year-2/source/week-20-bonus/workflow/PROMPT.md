Task-specific encore scope (user instruction overrides the generic three-band output paths below):
For Week 20, produce ONE shared selected-band bonus companion, with at least three genuinely distinct investigations matching the outline. Output draft/bonus.pdf, sources draft/src/; reviser outputs final/bonus.pdf, sources final/src/. Ignore references below to three mandatory band PDFs. Select honest grade/readiness coverage; the adult guide will supply the route. Student header: Week 20 / <topic> encore / Grades <appropriate range>. Footer: Bellingham Math Circle / Week 20 / W20-BON-v1. Consecutive Problem N labels. A problem's requested action must be explicit. Printed suitable bands may be stated compactly in problem text if distinct from the overall coverage. Do not force young versions. No base packet, guide, global index or workflow-template edits. No uploads or publication. Material remains unpiloted. Your ONLY stage is the stage named in this file.
Build using /Library/TeX/texbin/pdflatex (portable scripts should find pdflatex on PATH or documented PDFLATEX override). Python with PyMuPDF/ReportLab/Pillow is /Users/jamespfeiffer/math-circle/tmp/encore-18-34-venv/bin/python. Render helper /Users/jamespfeiffer/math-circle/tmp/encore-18-34/tools/render.py supports --out and contact sheets. Portable sources must build without absolute project paths. No physical fit or rehearsal claim is permitted.
Writer: Choose actual investigations yourself, check they differ from base exclusions. Include all student working diagrams and light records. Prefer 3-5 pages per week, enough space over arbitrary compactness; no automatic page target. Record complete draft answers and assumptions separately at draft/answer-notes.md to support the adult guide, not on student pages. Keep PDF/source build and writer notes inside the run.
Critic: review draft/bonus.pdf and write review.md only. Math critic: independently verify every task and represented example in draft/bonus.pdf, write review-math.md plus executable independent-check.py and checks.json in the run; do not edit writer content. Reviser: copy draft/src into final/src, address both reviews, build final/bonus.pdf, render/inspect EVERY final page, and write final/revision-notes.md and final/answer-notes.md with corrected answers and assumptions. Do not write adult guide.

Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 20: Averaging encore

Separate unpiloted bonus companion; leave base Week 20 packets and guides untouched. Preferred output: one selected-band `week-20-bonus.pdf` headed `Week 20 / Averaging encore / Grades 2–5`. The writer chooses the problems. Three mathematical directions reuse graph mats and stacks but ask about wandering, repeated change, and minimum roughness rather than repeating static fillings or the base peak/uniqueness proofs.

Mathematical kernels

1. **A wandering token explains the averaging values.** On a finite undirected connected graph with at least one fixed square, a token at a circle chooses each joined neighbor with equal probability, moves there, and continues until it first reaches a square. It then earns that square's fixed score. The expected score h(v) equals the fixed score at a square and the average of h at neighbors at a circle, by conditioning on the first move. The walk reaches a square with probability one: from every circle there is a path of at most m steps to a square, and finitely many vertices give a positive lower bound δ on following such a path; survival after km steps is at most (1−δ)^k. Thus this expected score is a genuine solution, not a formal recurrence with an unproved stopping assumption. By the base uniqueness theorem it equals the unique averaging filling. On the path of three edges with endpoint scores 0 and 6, the two circle expected scores are 2 and 4; on a three-leaf star with scores 0,3,6 the center expectation is 3. Experiments estimate an expectation but do not prove exact equality: keep the terminal-score record light and distinguish sample mean from exact result. Uniform choice is among joined places, including a zero-valued square; do not choose among nonempty stacks only.

2. **Repeated averaging need not settle when there is no fixed boundary.** This is a different action from satisfying all equations on one unchanged board. At each tick, every circle replaces its value by the average of its neighbors' values from the same BEFORE board; all replacements happen together. On an even cycle, alternating stacks 0,6,0,6 return to themselves after two ticks and alternate forever. In particular there is no convergence despite every individual replacement being an average. If each circle instead averages its own old value with its neighbors' old values, the four-cycle example becomes 4,2,4,2, then 8/3,10/3,8/3,10/3, approaching 3 without reaching it at any finite tick. Fraction cards or drawings are needed after the first tick. The two-circle board 0—6 is a simpler contrast: neighbor-only updates swap forever; averaging each old value with its one neighbor gives 3—3 in one tick. These finite exact examples establish cycling and different effects of retaining one's own value, not a universal convergence theorem. Children can invent and classify cycles without signed differences, eigenvectors, or calculus. Always retain a BEFORE mat so simultaneous updates are checked against one state rather than sequentially moving the same counters.

3. **A legal landscape minimizes the total squared gap.** On a finite graph with fixed square values, define roughness as the sum over edges of (difference between the joined values)^2, counting every edge once. A harmonic filling minimizes this score among all real fillings with the same fixed values. If each component reaches a square, it is the unique minimizer. For an adult proof write a competitor as h+g, with g=0 at squares. Expanding the edge squares gives E(h+g)=E(h)+E(g)+2Σ_edges(h_u−h_v)(g_u−g_v); the cross term is Σ_circle g_u Σ_neighbor(h_u−h_v)=0 because h averages. E(g)≥0, with equality only when g is constant on each component and thus zero. Small checked instances: 0—x—6 has minimum 18 at x=3; 0—x—y—6 has minimum 12 at x=2,y=4. A child can discover equal gaps by making and comparing square areas instead of multiplying. Restricting guesses to integer values can change the optimum and may leave several minimizers; use an instance whose harmonic answer is integral if integers are the only available values. Demonstrate a non-task scored path, with gap squares as visual areas and one total, before asking for a minimum. This is an optimization investigation, not a demand to solve every static equation again.

Sources: Current Week 20 PDFs, editable outline `source/week-20/editable/outlines/week-20-averaging-maximum-principle.md`, and facilitator guide pp. 1,3–4,22–25 supply the harmonic rule, uniqueness, and explicit limits on iteration. The base source is Doyle and Snell, Random Walks and Electric Networks, §§1.1–1.2. The first-step/stopping argument, exact dynamic examples, and finite energy expansion above were independently derived here; no newly verified outside source body is claimed. The base adult guide already suggests pointwise averaging of two solutions, so mere superposition is excluded as a new investigation.

Suggested emphasis by level

- K–1: optional oral wandering-token action on a two-choice board, or copy-and-swap the two-circle dynamics; adults keep records. The fractional dynamics and roughness score are not forced into a young-child version.
- Grades 2–3: run fair walks and compare terminal scores with stack values; repeat small whole-number synchronous updates; compare roughness using square drawings with adult reading.
- Grades 4–5: explain first-step averaging, expose a genuine two-cycle, and certify a least-rough landscape. Fractions and comparing square areas are readiness gates; the full algebraic energy proof stays with adults.

Materials

For each pair: 60 snap cubes or counters, two copies of each small graph mat (BEFORE and AFTER) with nodes at least 30 mm wide, one wandering token, numbered choice slips or a spinner that gives each current neighbor equal chances, 30 small number/fraction cards, a ruler, squared paper, pencils and a terminal-score strip. Number the incident neighbors locally so a degree-three choice is as fair as a degree-two choice; use repeated draws from identical opaque slips if necessary. Boundary values stay fixed during walks and roughness tasks; the cycling boards deliberately have no fixed shapes. Supply spare cubes for copying—values are not one conserved pile to redistribute. Fractions may be represented as cut fraction cards rather than split physical cubes. Working mats must support two recoverable states at once. Prepare only a few boards per visit; these directions need not fit one hour. Fair-draw handling and simultaneous-state operation remain physically untested.

Base exclusions and novelty

- Base packets already fill simultaneous mean boards, prohibit hidden peaks, compare equality at extremes, prove uniqueness, enumerate boundary-free constant assignments, and study integer/fraction feasibility.
- The base guide's integer path divisibility, translations, scaling, and pointwise averaging extensions are not new bonus counts.
- New investigations are (1) a stopping walk giving harmonic values, (2) an update process and its cycles, (3) an optimization score minimized by the same values. The update process must be labeled explicitly so it is not mistaken for the base simultaneous consistency puzzle.


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

Your run folder is /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-20-bonus-v1. Keep all your files inside it: sources in /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-20-bonus-v1/draft/src/ and the three finished PDFs at exactly these paths:

  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-20-bonus-v1/draft/k-1.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-20-bonus-v1/draft/grades-2-3.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-20-bonus-v1/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
