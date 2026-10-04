Task-specific encore scope (user instruction overrides the generic three-band output paths below):
For Week 29, produce ONE shared selected-band bonus companion, with at least three genuinely distinct investigations matching the outline. Output draft/bonus.pdf, sources draft/src/; reviser outputs final/bonus.pdf, sources final/src/. Ignore references below to three mandatory band PDFs. Select honest grade/readiness coverage; the adult guide will supply the route. Student header: Week 29 / <topic> encore / Grades <appropriate range>. Footer: Bellingham Math Circle / Week 29 / W29-BON-v1. Consecutive Problem N labels. A problem's requested action must be explicit. Printed suitable bands may be stated compactly in problem text if distinct from the overall coverage. Do not force young versions. No base packet, guide, global index or workflow-template edits. No uploads or publication. Material remains unpiloted. Your ONLY stage is the stage named in this file.
Build using /Library/TeX/texbin/pdflatex (portable scripts should find pdflatex on PATH or documented PDFLATEX override). Python with PyMuPDF/ReportLab/Pillow is /Users/jamespfeiffer/math-circle/tmp/encore-18-34-venv/bin/python. Render helper /Users/jamespfeiffer/math-circle/tmp/encore-18-34/tools/render.py supports --out and contact sheets. Portable sources must build without absolute project paths. No physical fit or rehearsal claim is permitted.
Writer: Choose actual investigations yourself, check they differ from base exclusions. Include all student working diagrams and light records. Prefer 3-5 pages per week, enough space over arbitrary compactness; no automatic page target. Record complete draft answers and assumptions separately at draft/answer-notes.md to support the adult guide, not on student pages. Keep PDF/source build and writer notes inside the run.
Critic: review draft/bonus.pdf and write review.md only. Math critic: independently verify every task and represented example in draft/bonus.pdf, write review-math.md plus executable independent-check.py and checks.json in the run; do not edit writer content. Reviser: copy draft/src into final/src, address both reviews, build final/bonus.pdf, render/inspect EVERY final page, and write final/revision-notes.md and final/answer-notes.md with corrected answers and assumptions. Do not write adult guide.

Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 29: Two-length builders encore

Mathematical kernels

1. Recording rod order creates a new counting object. With whole 3-rods and 4-rods, a build word records their order from the fixed left endpoint. Rods of the same length remain indistinguishable, but 3,4 and 4,3 are now different words. Let f(n) be the number of words reaching n, with f(0)=1 for the empty word and f(n)=0 for negative n. The last rod is either 3 or 4, giving f(n)=f(n−3)+f(n−4); the two cases cannot overlap. Examples: f(7)=2, f(10)=3, f(12)=2, f(15)=5 and f(18)=11. Alternatively, for a fixed combination x three-rods and y four-rods, the number of orders is C(x+y,x); summing over 3x+4y=n gives the same f(n). The recurrence and choose-positions count can be explained with actual rows, without formal notation. This counting is different from the base's unordered build catalog: an explicit non-task build→word example must introduce the changed equivalence convention before first use.

2. A finite box has complement symmetry rather than eventual coverage. Supply exactly X rods of length a and Y of length b, with total T=aX+bY; a target is possible if some subset of this finite stock makes it. The unused rods make T−n, so n is possible if and only if T−n is possible. This gives a mirror correspondence on reachable targets and gaps within 0,…,T. For X=4 three-rods and Y=3 four-rods, T=24 and the gaps are exactly 1,2,5,19,22,23; every target from 6 through 18 is possible. The small gaps pair with the large ones by 24−n. Reaching a target above T is impossible, so the unlimited-stock base certificate cannot be applied. Equal two-way use of all pieces is possible exactly when T/2 is an available subset target (and T is even); here 12 can use all four threes while its complement uses all three fours. Children can lay used and unused rods in two visible lanes, with one recoverable record instead of a moving tally. Do not add stock during this investigation, even if more rods are available elsewhere on the table.

3. A new length may add a tool without adding a reachable target. In the unlimited-stock model let S be the lengths reachable with a,b. Adding a third length c changes no reachable targets exactly when c∈S. If c=ax+by, replace every c-rod by that same construction to show that every new build was already possible. Conversely, if c∉S, c itself becomes a newly reachable target. For 3/5, adding an 8-rod adds no targets since 8=3+5; adding a 7-rod fills a genuine gap, and the final gap becomes 4 (5,6,7 are a consecutive certificate, while 4 still fails). Adding a 4-rod makes every target at least 3 possible since 3,4,5 give a certificate. The question is tool redundancy and useful new generators, not another search for the two-length last-gap formula. If an extra rod merely shortens some build, that may change minimum piece counts even though reachability is unchanged: make this a readiness-dependent distinction rather than call the rod useless. The theorem assumes unlimited copies; it need not hold in the finite-box model above because replacement may consume unavailable stock.

Sources: Current Week 29 packets and guide establish whole-rod reachability with order ignored and unlimited stock. Chapel Hill Math Circle, “The Frobenius Coin Problem”, Beginners’ Group, 18 January 2025, pp. 1–4, is the base activity precedent as recorded in that guide. The new ordered-word recurrence, complement theorem and redundancy criterion were independently derived here. The displayed values were computed by dynamic programming or finite subset enumeration, and must be independently recomputed by CRITIC-MATH; no claim that the source contains these bonus tasks. Related combinatorial build words can revisit earlier counting/code ideas, but keep the concrete same-theme rods and the changed mathematical equivalence explicit.

Suggested emphasis by level

- K–1: Real concrete entry through different left-to-right orders and through using/unused finite rods; adult can write a word or target number. A complete recurrence proof is not required to participate.
- Grades 2–3: Organize build words and compare finite-box complementary targets; test whether a third length changes what can be built.
- Grades 4–5: Prove the last-rod recurrence/completeness, the complement correspondence, and the exact redundancy criterion; compare unlimited reachability with finite-stock or minimum-piece questions on later visits.

Materials

Per working pair/trio: ten 3-unit rods and ten 4-unit rods, six 5-unit rods, three 7-unit and three 8-unit rods, two distinct “used”/“unused” trays or lanes, and a separate sealed finite-box kit containing exactly four 3-rods and three 4-rods. Rods share a physical unit of 1 cm and should be 1 cm wide with visible divisions and labels; keep unused lengths away from each task. Five pair/trio kits serve the current eleven children at fixed tables. Reuse rods between cases; for larger word catalogs small cards or drawn rods are records, not additional stock. A working 0–24 ruler needs landscape Letter or a separate 24 cm strip; print at 100% and measure the unit. Compact diagrams must say through their layout that construction occurs beside the page rather than falsely invite physical alignment. The finite-box kit cannot borrow rods from the unlimited kit. Demonstrate one build word with matching order labels and one used/unused split on a non-task target before the respective unfamiliar conventions.

Scope and exclusions

Create shared `week-29/week-29-bonus.pdf`, header `Week 29 / Two-length builders encore / Grades K–5`, and `week-29-bonus-facilitator.pdf`; sources in `source/week-29-bonus/`. The writer chooses exact tasks and substantive contrasts. Count ordered words, finite-stock complements, and third-length redundancy as three investigations; do not count extra target numbers as further ones. Do not repeat unordered all-ways builds for 12/15/16/24, 3/4 or 3/5 gap catalogs, consecutive certificates as the main question, gcd gap classification, exchanges between unordered builds, 4/7 or 5/7 last-gap searches, or the general ab−a−b conjecture/proof. Evidence read: all K–1 P1–6, 2–3 P1–6, 4–5 P1–8 and mathematical overview. Certificates may support a new third-generator conclusion, but must not become a copy of a base problem. All bonus materials remain unpiloted; rod dimensions and finite-kit procedure remain physically untested.


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

Your run folder is /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-29-bonus-v1. Keep all your files inside it: sources in /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-29-bonus-v1/draft/src/ and the three finished PDFs at exactly these paths:

  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-29-bonus-v1/draft/k-1.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-29-bonus-v1/draft/grades-2-3.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-29-bonus-v1/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
