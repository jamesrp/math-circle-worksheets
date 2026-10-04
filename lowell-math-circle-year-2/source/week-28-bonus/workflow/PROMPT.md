Task-specific encore scope (user instruction overrides the generic three-band output paths below):
For Week 28, produce ONE shared selected-band bonus companion, with at least three genuinely distinct investigations matching the outline. Output draft/bonus.pdf, sources draft/src/; reviser outputs final/bonus.pdf, sources final/src/. Ignore references below to three mandatory band PDFs. Select honest grade/readiness coverage; the adult guide will supply the route. Student header: Week 28 / <topic> encore / Grades <appropriate range>. Footer: Bellingham Math Circle / Week 28 / W28-BON-v1. Consecutive Problem N labels. A problem's requested action must be explicit. Printed suitable bands may be stated compactly in problem text if distinct from the overall coverage. Do not force young versions. No base packet, guide, global index or workflow-template edits. No uploads or publication. Material remains unpiloted. Your ONLY stage is the stage named in this file.
Build using /Library/TeX/texbin/pdflatex (portable scripts should find pdflatex on PATH or documented PDFLATEX override). Python with PyMuPDF/ReportLab/Pillow is /Users/jamespfeiffer/math-circle/tmp/encore-18-34-venv/bin/python. Render helper /Users/jamespfeiffer/math-circle/tmp/encore-18-34/tools/render.py supports --out and contact sheets. Portable sources must build without absolute project paths. No physical fit or rehearsal claim is permitted.
Writer: Choose actual investigations yourself, check they differ from base exclusions. Include all student working diagrams and light records. Prefer 3-5 pages per week, enough space over arbitrary compactness; no automatic page target. Record complete draft answers and assumptions separately at draft/answer-notes.md to support the adult guide, not on student pages. Keep PDF/source build and writer notes inside the run.
Critic: review draft/bonus.pdf and write review.md only. Math critic: independently verify every task and represented example in draft/bonus.pdf, write review-math.md plus executable independent-check.py and checks.json in the run; do not edit writer content. Reviser: copy draft/src into final/src, address both reviews, build final/bonus.pdf, render/inspect EVERY final page, and write final/revision-notes.md and final/answer-notes.md with corrected answers and assumptions. Do not write adult guide.

Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 28: Flat folds encore

Mathematical kernels

1. A fold taking one point to another is constrained by geometry. For two distinct marked points P,Q, the only possible straight crease that reflects P onto Q is their perpendicular bisector: each crease point must be equally far from P and Q, and reflection exchanges the two equal perpendicular offsets. To align two distinct point-pairs with one fold, their perpendicular bisectors must be the same line. Thus several pairwise possible alignments can be simultaneously impossible. A point required to stay fixed must lie on the crease. These are exact statements about a single reflection of an ideal flat sheet, not a measurement tolerance rule. Children have a concrete entry by bringing two visible marks together, creasing, reopening, and testing a second pair; adults can introduce distance language after the action. Fixed-point and multiple-pair constraints give depth without asking for formal coordinate proofs. Base Weeks 15 and 21 use reflection for nearest-site or shortest-bounce-route questions; this is a new inverse alignment question, not a repetition of those tasks.

2. Crease directions do not necessarily fix the layer order. Fold a strip of three equal square panels A,B,C completely flat at both joins, reading mountain/valley from the original marked front. With both outer panels folded toward the front of middle B (two valleys), B is the bottom panel but A,C can stack in either order, depending on which is folded first. All six top-to-bottom permutations of three panels are possible in the ideal static model: the two equal-type assignments allow two orders each, and the two mixed-type assignments one each. At four panels, the pairs of joins AB and CD occur at the same end of the flat stack, while BC occurs at the other. Their connecting bends must not interleave in a side-view layer order: patterns A,C,B,D and the seven analogous interleavings would force paper to cross. Of the 24 permutations, eight interleave (two choices of first pair and two orientations of each pair), leaving exactly sixteen noncrossing ideal stack orders. Noncrossing endpoint bends supply a static embedding for each survivor. This is a layer-order theorem under ideal zero-thickness/static assumptions; it neither supplies a rigid folding motion nor certifies easy sequential folding with real paper. The boundary creases of a strip do not form the base's one interior vertex, so Maekawa's ray count must not be applied here. Start with actual three-panel folded strips; four-panel completeness is a readiness-dependent return visit.

3. One punch can generate an orbit of reflected positions. Start with a square centered at the intersection of its horizontal and vertical midlines. Fold along both midlines to a quarter-square. A punch strictly away from every fold and outside edge unfolds to the four positions (±p,±q), making the corners of a centered rectangle. Reversing the two fold orders gives the same position set. If the quarter-square is additionally folded along its diagonal, an off-axis punch unfolds to eight positions: (±p,±q) and (±q,±p), with p,q>0 and p≠q. The position set is invariant under both midline reflections and the diagonal reflection; an arbitrary pattern with four or eight holes need not be obtainable from one punch. Inverse pattern design therefore asks about the relations among positions, not the count alone. The statements count distinct point-centers; finite circular holes must be far enough from folds and each other to remain separate. Do not extend the four/eight claim to punches on fold lines, intersecting cuts, a freely chosen crease, or partly folded layers. Coordinates are adult shorthand; children can mark corresponding locations on unfolded copies and compare patterns.

Sources: Current Week 28 PDFs and overview supply the distinction between ideal states and physical witnesses and the base interior-vertex assumptions. All new fold-image and layer-order claims were independently derived above; the four-panel sixteen-count should be enumerated independently in CRITIC-MATH. Natalia Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 12, “One mirror”, “Two mirrors”, “Symmetry”, and “At the lesson” (`OEBPS/part0022.xhtml` in the downloaded EPUB), was read during design. It supplies related reflection/symmetry precedents and explicitly reports that imagined two-mirror tasks were difficult without actual mirrors, while a later workshop gave every child mirrors. It also reports using physical figures matched to their copy-machine shadows to expose invariance. These are source observations; our choice to use folded strips and actual unfolded punches is an inference/adaptation. Do not claim the book contains these specific alignment, sixteen-stack, or four/eight-hole questions.

Suggested emphasis by level

- K–1: Supported entry through aligning visible marks and trying three-panel layer orders; no degree arithmetic, long codes, or theorem names. Fold-and-punch work can be adult-assisted, with the child's choices of position and pattern retained.
- Grades 2–3: Investigate simultaneous alignments, compare actual folded stacks, and design/check four-image hole patterns.
- Grades 4–5: Explain one-fold constraints, certify the complete noncrossing stack count, and solve inverse four/eight-image pattern questions; no need to finish all branches in one visit.

Materials

Per table: twelve thin square sheets about 15 cm on a side, two sheets of tracing paper, six three-panel strips 5 × 15 cm, six four-panel strips 5 × 20 cm, removable labels A–D visible on both sides, pencils, ruler, and one ordinary hole punch shared with the adult. Prepare parallel joins accurately at 5 cm intervals. All panels must remain connected; no tearing or extra crease may substitute for a requested layer order. For the reflection/punch directions extra folds are permitted only when the chosen task expressly supplies them; these are different models from the original all-listed-rays/no-extra-crease disk tasks. Keep the original front marked for M/V; do not require M/V transcription as well as layer-order transcription unless that comparison is the actual investigation. Show a non-task two-panel strip with a side-view stack before first using top-to-bottom letter records. Keep punch centers at least 10 mm from folds and sheet edges and far enough apart after unfolding that circles do not merge. Actual eight-layer punch capacity, crease accuracy and each proposed fold witness must be tested by an adult before use; no physical pretest has been completed in this design pass. Drawing reflection positions on unfolded paper can substitute if the punch is unready, but should be labeled a model rather than a punched witness.

Scope and exclusions

Create shared `week-28/week-28-bonus.pdf`, header `Week 28 / Flat folds encore / Grades K–5`, plus `week-28-bonus-facilitator.pdf`, sources in `source/week-28-bonus/`. Writer chooses exact tasks and matched visual examples. Three distinct new investigations are inverse fold alignment, layer orders on strips, and reflected punch patterns. Do not repeat half-turn wedge assembly, missing-ray Kawasaki completion, even-ray/alternating-angle obstruction, four-right-angle M/V classification or constrained completion, six-angle order enumeration, or tours of the eight M/V assignments. Evidence read: K–1 P1–6, 2–3 P1–6, 4–5 P1–6 and mathematical overview; Week 15/21 task text checked for the related but different reflection use. Preserve Week 1 encore entirely; no tiling, giant pattern-block copies or cube-flip questions are reused. All proposed material is unpiloted.


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

Your run folder is /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-28-bonus-v1. Keep all your files inside it: sources in /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-28-bonus-v1/draft/src/ and the three finished PDFs at exactly these paths:

  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-28-bonus-v1/draft/k-1.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-28-bonus-v1/draft/grades-2-3.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-28-bonus-v1/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
