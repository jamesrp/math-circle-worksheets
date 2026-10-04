Task-specific encore scope (user instruction overrides the generic three-band output paths below):
For Week 31, produce ONE shared selected-band bonus companion, with at least three genuinely distinct investigations matching the outline. Output draft/bonus.pdf, sources draft/src/; reviser outputs final/bonus.pdf, sources final/src/. Ignore references below to three mandatory band PDFs. Select honest grade/readiness coverage; the adult guide will supply the route. Student header: Week 31 / <topic> encore / Grades <appropriate range>. Footer: Bellingham Math Circle / Week 31 / W31-BON-v1. Consecutive Problem N labels. A problem's requested action must be explicit. Printed suitable bands may be stated compactly in problem text if distinct from the overall coverage. Do not force young versions. No base packet, guide, global index or workflow-template edits. No uploads or publication. Material remains unpiloted. Your ONLY stage is the stage named in this file.
Build using /Library/TeX/texbin/pdflatex (portable scripts should find pdflatex on PATH or documented PDFLATEX override). Python with PyMuPDF/ReportLab/Pillow is /Users/jamespfeiffer/math-circle/tmp/encore-18-34-venv/bin/python. Render helper /Users/jamespfeiffer/math-circle/tmp/encore-18-34/tools/render.py supports --out and contact sheets. Portable sources must build without absolute project paths. No physical fit or rehearsal claim is permitted.
Writer: Choose actual investigations yourself, check they differ from base exclusions. Include all student working diagrams and light records. Prefer 3-5 pages per week, enough space over arbitrary compactness; no automatic page target. Record complete draft answers and assumptions separately at draft/answer-notes.md to support the adult guide, not on student pages. Keep PDF/source build and writer notes inside the run.
Critic: review draft/bonus.pdf and write review.md only. Math critic: independently verify every task and represented example in draft/bonus.pdf, write review-math.md plus executable independent-check.py and checks.json in the run; do not edit writer content. Reviser: copy draft/src into final/src, address both reviews, build final/bonus.pdf, render/inspect EVERY final page, and write final/revision-notes.md and final/answer-notes.md with corrected answers and assumptions. Do not write adult guide.

Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 31: Hidden orchard encore

Mathematical kernels

1. Two lookouts change visibility into a covering problem. From a lattice lookout L=(c,d), a different lattice target T=(a,b) is visible exactly when gcd(|a−c|,|b−d|)=1; only dots strictly between L and T are blockers. For adjacent lookouts (0,0) and (1,0), a target (a,b), b>0, is hidden from both exactly when gcd(a,b)>1 and gcd(a−1,b)>1. A row of height b equal to a prime power can contain no doubly hidden target: the same prime would have to divide consecutive integers a and a−1. The height-6 row does have doubly hidden targets; modulo 6 these occur exactly at a≡3 or 4. Thus adding a nearby lookout helps but does not guarantee all targets are visible. Concrete core: keep two separate, fixed lookouts and test the same target against both; classify visible from both, exactly one, neither. The prime-power conclusion is a readiness-dependent explanation, not a required entry fact.

2. Empty orchard triangles connect visible sides to area. A lattice triangle with vertices O,P,Q has boundary lattice-point count B=gcd(|P_x|,|P_y|)+gcd(|Q_x|,|Q_y|)+gcd(|P_x−Q_x|,|P_y−Q_y|). Pick’s theorem says area=I+B/2−1, where I counts strictly interior lattice points. Hence a nondegenerate lattice triangle with no lattice dots other than its three vertices has area 1/2. Conversely area 1/2 forces I=0 and B=3. Having all three sides visible is insufficient to make a triangle empty: O=(0,0), P=(1,2), Q=(3,1) have primitive sides, area 5/2, and interior points (1,1),(2,1). The child entry is stretching three sides, checking boundary versus inside, and comparing area by enclosing rectangles/copies; the adult may use Pick’s theorem for the complete key. Do not present a small census as a proof of Pick’s theorem, and do not require determinants from children.

3. An orchard can grow from visible neighbor directions. Begin with the two axis directions (1,0),(0,1). Between neighboring directions u=(a,b) and v=(c,d), insert u+v=(a+c,b+d), replacing that neighbor pair by u,u+v and u+v,v. If ad−bc=±1, then u+v is primitive: any common divisor of its coordinates divides a(b+d)−b(a+c)=ad−bc. Both new neighbor determinants remain ±1. Repeated insertion generates every positive primitive point once (the Stern–Brocot construction in vector form). For a complete converse, express a target inside the current neighbor cone as T=A u+B v; the determinant-one inverse gives positive integer coefficients. When A>B, the target lies between u and u+v, with new coefficients A−B,B; when B>A it lies between u+v and v, with coefficients A,B−A. Coefficient subtraction terminates at A=B=1, because primitiveness prevents a common factor; then T=u+v. These forced interval choices also give uniqueness. This is not the rule of directly subtracting coordinates to find a parent in this tree, and not arbitrary addition of visible points: (1,1)+(1,3)=(2,4) is hidden because those directions are not determinant-one neighbors. Concrete work should grow a physical ordered row/fan of direction cards with pair boundaries retained; do not ask children to remember a traversal code. A small non-target input → componentwise addition → plotted new dot visual is essential before first use. Generating and checking a few new directions is the entry; completeness and uniqueness are deeper return work.

Sources: Current Week 31 base visibility criterion and source notes in `lowell-math-circle-year-2/source/week-31/editable/worksheet-workflow/outlines/week-31-visible-lattice.md`. New directions are local derivations from the translated gcd criterion, Pick’s lattice-area formula, and the Stern–Brocot/Farey neighbor construction. Source context is elementary number theory and lattice geometry; the supplied current visibility sources do not establish classroom use of these encore tasks. All represented small examples need fresh finite checks in the math stage.

Suggested emphasis by level:
K–1: two fixed lookout threads with adult reading, targets chosen on a small grid; distinguishing exact-on-thread blockers remains the task. Empty triangles can be explored by touching dots, but area proofs and direction-card addition are not forced.
Grades 2–3: two-lookout comparison and empty triangles; direction growth after understanding across/up coordinates and two-component addition. Arithmetic to 6 and distinguishing boundary from interior suffice for concrete entries.
Grades 4–5: explain row behavior through common factors; test visible-sided versus empty triangles; grow and defend the neighbor rule, with the general uniqueness proof optional after concrete construction. No calculus or formal linear algebra is a student prerequisite.

Materials

Per pair: one square-spaced dot grid covering at least coordinates 0–6 across/up, at least 20 mm spacing; two differently styled fixed lookout markers and thin nonstretch threads; a ruler, removable dot markers, pencils, and spare dot grids. For triangles use rubber bands on a pegboard or pencil/ruler segments rather than three crossing loose threads. Dot centers alone count as trees: outlines and thread thickness must not make near-collinear blockers. Keep two lookout references fixed during a comparison; do not sequentially replace one state with the other. For direction growth provide movable two-number cards for the two axis boundaries and generated directions, with room for an ordered strip or fan. A pair keeps one recoverable construction rather than copying every intermediate ray into a second log. Grid scale may change uniformly; diagrams require equal horizontal/vertical scale for area comparisons. Adult preparation should avoid threading dozens of targets or making a large census compulsory.

Base exclusions and drafting boundary

Do not repeat finding all visible dots from the origin, collecting targets by first blocker, counting d−1 blockers, deriving gcd visibility, finding an all-visible row, or asking for a target with 99 blockers. Translation of the visibility rule is only support for a genuinely new two-station question. The three investigations are two-lookout coverage, empty triangles, and neighbor-direction growth. More grid instances do not create more investigations. Prefer one shared selected-band `week-31-bonus.pdf`, with guide routes allowing a K–1 concrete entry only where it works. Writer chooses exact problems and their sequence. Unpiloted; physical thread accuracy and pegboard fit have not been rehearsed.


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

Your run folder is /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-31-bonus-v1. Keep all your files inside it: sources in /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-31-bonus-v1/draft/src/ and the three finished PDFs at exactly these paths:

  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-31-bonus-v1/draft/k-1.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-31-bonus-v1/draft/grades-2-3.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-31-bonus-v1/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.

Verified local source addendum: Math Circle by the Bay, printedpp132–134 (PDF145–147), Problems5.31–5.34, gives Pick formula, its simple lattice-polygon assumptions and explicit distinction between observed examples and proof. Root read source body. Empty lattice triangle work may use that adult context; do not claim children prove Pick from finite experiments.
