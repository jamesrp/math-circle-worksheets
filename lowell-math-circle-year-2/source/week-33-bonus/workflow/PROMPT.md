Task-specific encore scope (user instruction overrides the generic three-band output paths below):
For Week 33, produce ONE shared selected-band bonus companion, with at least three genuinely distinct investigations matching the outline. Output draft/bonus.pdf, sources draft/src/; reviser outputs final/bonus.pdf, sources final/src/. Ignore references below to three mandatory band PDFs. Select honest grade/readiness coverage; the adult guide will supply the route. Student header: Week 33 / <topic> encore / Grades <appropriate range>. Footer: Bellingham Math Circle / Week 33 / W33-BON-v1. Consecutive Problem N labels. A problem's requested action must be explicit. Printed suitable bands may be stated compactly in problem text if distinct from the overall coverage. Do not force young versions. No base packet, guide, global index or workflow-template edits. No uploads or publication. Material remains unpiloted. Your ONLY stage is the stage named in this file.
Build using /Library/TeX/texbin/pdflatex (portable scripts should find pdflatex on PATH or documented PDFLATEX override). Python with PyMuPDF/ReportLab/Pillow is /Users/jamespfeiffer/math-circle/tmp/encore-18-34-venv/bin/python. Render helper /Users/jamespfeiffer/math-circle/tmp/encore-18-34/tools/render.py supports --out and contact sheets. Portable sources must build without absolute project paths. No physical fit or rehearsal claim is permitted.
Writer: Choose actual investigations yourself, check they differ from base exclusions. Include all student working diagrams and light records. Prefer 3-5 pages per week, enough space over arbitrary compactness; no automatic page target. Record complete draft answers and assumptions separately at draft/answer-notes.md to support the adult guide, not on student pages. Keep PDF/source build and writer notes inside the run.
Critic: review draft/bonus.pdf and write review.md only. Math critic: independently verify every task and represented example in draft/bonus.pdf, write review-math.md plus executable independent-check.py and checks.json in the run; do not edit writer content. Reviser: copy draft/src into final/src, address both reviews, build final/bonus.pdf, render/inspect EVERY final page, and write final/revision-notes.md and final/answer-notes.md with corrected answers and assumptions. Do not write adult guide.

Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 33: Necklaces encore

Mathematical kernels

1. Mirror twins change the equivalence relation. With named counter kinds fixed, rotation-only necklaces may form a reflected pair when flips are allowed. A ring is achiral if its reversed cyclic word is a rotation of itself. Binary rings of lengths at most 5 are all achiral; length 6 first admits a mirror pair. There are 14 binary rotation classes at length 6, but 13 classes allowing rotations and flips, because precisely one reflected pair merges. The base adult guide already gives the six-bead pair AABABB/AABBAB; do not simply print that same demonstration again as the encore. A fresh direction is sorting a small supplied collection under the two equivalence rules, or constructing mirror twins on another genuinely workable size/color set. For three named colors on three beads, there are 11 rotation classes but 10 rotation-and-flip classes; the all-distinct words ABC and ACB merge, whereas every class with a repeated color is achiral. On a binary eight-ring, the three-A gap cycle 1,2,5 and its reversal give a new chiral pair: a rotation preserves the cyclic order of these unequal gaps. Children can match overlays without any group theory.

2. A neighbor constraint changes which necklaces exist. Require different kinds at neighboring bead positions, including the closing pair. With two kinds this is possible exactly for even ring length, and there is one rotation class at every positive even length n≥4: the alternating ring. Odd length needs at least three kinds. For c named colors the number of valid words in n fixed cyclic positions is (c−1)^n+(−1)^n(c−1), n≥3. An elementary recurrence conditions on whether the final color agrees with the first; it is adult context, not a required formula for children. At prime length p, every proper coloring is nonconstant, so its rotation class has p members and the rotation-only count is the fixed-position count divided by p. In particular, a five-ring with three colors has 30 fixed-position proper words and six rotation classes. These are constrained-coloring necklaces, rather than another unconstrained Fermat count. Named colors may not be permuted when deciding equality. Writer chooses concrete parity experiments and a manageable classified collection.

3. Local windows can cover every short code exactly once. On a face-up binary ring, read k consecutive beads clockwise starting at each position, wrapping around the end. There are 2^k possible k-letter windows. A ring containing every one needs at least 2^k beads, since each bead starts one window. That bound is attained for k=2 by 0011, and for k=3 by 00010111: its windows are 000,001,010,101,011,111,110,100. At k=3 there are exactly two eight-bead solutions up to rotation, represented by 00010111 and 00011101; they are mirror twins. This is the binary de Bruijn cycle question. A child can slide a two- or three-position viewer and remove each found code card from the available pile, so the rule lives on the table. Only after concrete work might the adult connect a three-letter code abc to an edge from pair ab to pair bc, and observe that using every code once is an Euler circuit. Do not lead with that representation or require a traversal code. The writer may choose to seek one shortest ring; any request for all solutions requires fresh complete enumeration, not the example alone.

Sources: Base rotation-only and prime-length source notes in `lowell-math-circle-year-2/source/week-33/editable/worksheet-workflow/outlines/week-33-prime-necklaces.md`. New directions are local elementary ring constructions and counting checks, with mathematical contexts of dihedral orbits, proper cycle coloring, and de Bruijn cycles/Euler circuits. The base Oregon instructor worksheet supports the prime-length argument only. The original year-1 handouts were inspected for prior themes; no necklace task was found in their openings, and no claim that these new tasks come from those handouts is made.

Suggested emphasis by level:
K–1: mirror matching with a tracing copy, or making alternating rings and discovering the closing conflict; an adult reads. A two-window ring is suitable only after the child reliably reads each pair and wraps around.
Grades 2–3: constrained necklaces and two-/three-window construction with supplied code cards; matching and reliable clockwise local reading matter more than arithmetic. Mirror sorting is a different return route.
Grades 4–5: classify a small constrained set, defend a parity impossibility, explain the shortest-window-ring bound, and investigate mirror classes. The general coloring formula and Euler interpretation are readiness-dependent adult continuations.

Materials

Per pair: two flat ring mats sized to the writer’s chosen instances, at least eight counters in each of two distinguishable kinds and five in a third kind, removable start arrow, fixed reading-direction arrow, tracing paper/clear overlay, and pencils. For local windows provide four two-letter or eight three-letter cards as a complete supplied set, plus a removable viewer that identifies consecutive positions including across the closing gap. Avoid requiring children to manufacture every word card. A non-task worked visual must show start, clockwise bead window including wraparound, and its matching code card before that representation is used. Keep the original ring still for flip comparison; loose-counter rings are not physically turned over. Flip permission applies only to the mirror investigation, so mark the convention once at that activity’s opening. Equal symbol direction does not encode additional data; keep color names fixed. Working spots must accommodate ≥20 mm counters without overlap. Card/mat fit and viewer procedure remain physically untested.

Base exclusions and drafting boundary

Do not repeat enumerating unconstrained binary three-rings, sorting the eight three-word cards or all 32 five-word cards, finding possible readout counts on four/six beads, the prime-length orbit theorem, or Fermat divisibility. The adult base reflection anecdote is context to move beyond, not a fourth new investigation. Three encore directions are mirror-equivalence classes, neighbor-constrained rings, and universal local-window rings. Multiple lengths/colors are examples within a direction. Prefer one selected-band `week-33-bonus.pdf` with independent readiness routes in the adult companion. Writer chooses the exact substantial tasks and layout. Unpiloted.


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

Your run folder is /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-33-bonus-v1. Keep all your files inside it: sources in /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-33-bonus-v1/draft/src/ and the three finished PDFs at exactly these paths:

  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-33-bonus-v1/draft/k-1.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-33-bonus-v1/draft/grades-2-3.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-33-bonus-v1/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
