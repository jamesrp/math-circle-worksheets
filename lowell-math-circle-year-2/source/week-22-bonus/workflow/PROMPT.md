Task-specific encore scope (user instruction overrides the generic three-band output paths below):
For Week 22, produce ONE shared selected-band bonus companion, with at least three genuinely distinct investigations matching the outline. Output draft/bonus.pdf, sources draft/src/; reviser outputs final/bonus.pdf, sources final/src/. Ignore references below to three mandatory band PDFs. Select honest grade/readiness coverage; the adult guide will supply the route. Student header: Week 22 / <topic> encore / Grades <appropriate range>. Footer: Bellingham Math Circle / Week 22 / W22-BON-v1. Consecutive Problem N labels. A problem's requested action must be explicit. Printed suitable bands may be stated compactly in problem text if distinct from the overall coverage. Do not force young versions. No base packet, guide, global index or workflow-template edits. No uploads or publication. Material remains unpiloted. Your ONLY stage is the stage named in this file.
Build using /Library/TeX/texbin/pdflatex (portable scripts should find pdflatex on PATH or documented PDFLATEX override). Python with PyMuPDF/ReportLab/Pillow is /Users/jamespfeiffer/math-circle/tmp/encore-18-34-venv/bin/python. Render helper /Users/jamespfeiffer/math-circle/tmp/encore-18-34/tools/render.py supports --out and contact sheets. Portable sources must build without absolute project paths. No physical fit or rehearsal claim is permitted.
Writer: Choose actual investigations yourself, check they differ from base exclusions. Include all student working diagrams and light records. Prefer 3-5 pages per week, enough space over arbitrary compactness; no automatic page target. Record complete draft answers and assumptions separately at draft/answer-notes.md to support the adult guide, not on student pages. Keep PDF/source build and writer notes inside the run.
Critic: review draft/bonus.pdf and write review.md only. Math critic: independently verify every task and represented example in draft/bonus.pdf, write review-math.md plus executable independent-check.py and checks.json in the run; do not edit writer content. Reviser: copy draft/src into final/src, address both reviews, build final/bonus.pdf, render/inspect EVERY final page, and write final/revision-notes.md and final/answer-notes.md with corrected answers and assumptions. Do not write adult guide.

Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 22: Meeting regions encore

Separate unpiloted bonus companion; leave base Week 22 packets and guides untouched. Preferred output: one selected-band `week-22-bonus.pdf` headed `Week 22 / Meeting regions encore / Grades 2–5`. The writer chooses the configurations and substantial tasks. Reuse filled stretched-band regions, including points and segments, but change the target to small witnesses, separation, or three simultaneous groups.

Mathematical kernels

1. **A point inside a many-dot region needs at most three supporting dots.** For any finite nonempty planar dot set S, every point P in its convex hull belongs to the convex hull of at most three members of S. If the hull is a point or segment, one or two extreme dots suffice. Otherwise triangulate its convex boundary polygon by drawing diagonals from one boundary vertex; the triangles cover the filled polygon, so one containing P provides at most three original dots. The bound three is sharp: a point strictly inside a nondegenerate triangle and not on any of its edges is not in a hull of one or two of its three vertices. This is the elementary planar Carathéodory theorem. It asks for a small certificate for one target, unlike Radon’s partition of every label. Children can remove unneeded dots while keeping a marked target inside the stretched-band region, and can encounter cases where one, two, or three are needed. “Try deleting dots until stuck” suggests a candidate; a triangulation explains why three always suffice. Targets on edges count, and the goal does not require every original label to be used.

2. **Two disjoint filled regions can be separated by one line.** For two finite nonempty labeled dot groups, their closed convex hulls are disjoint exactly when a straight line can put the entire first group strictly on one side and the entire second strictly on the other, with no dot on the line. The forward construction uses a shortest segment P–Q between the two compact hulls; its perpendicular bisector separates them strictly. For the adult justification, minimality gives (X−P)·(Q−P)≤0 for every X in the first hull and (Y−Q)·(Q−P)≥0 for every Y in the second, by considering a small move from P toward X or Q toward Y. Hence the two hulls lie on opposite sides of the bisector with a positive gap. Conversely a convex hull stays in the open half-plane containing its defining dots, so a strict separator prevents intersection. The child entry is a ruler-line challenge with preassigned groups and a visible proof when a shared point defeats all lines; closest-point algebra stays with adults. Alternating colors around a quadrilateral have intersecting diagonal regions, whereas two adjacent-color pairs are separable. Do not confuse a thick drawn line gap with mathematical separation, or claim a unique separator.

3. **Three regions must share one point, not only meet pairwise.** Partition every label into three nonempty groups and seek one point in all three closed hulls. On a line, five labels always suffice: write their positions x1≤x2≤x3≤x4≤x5 and use groups {x1,x5}, {x2,x4}, {x3}; all contain x3. Repeated locations are allowed. Four distinct collinear positions cannot guarantee success: a three-group split of four labels has two singleton groups, whose distinct points cannot meet. Thus five is the sharp one-dimensional threshold for three groups. In the plane the behavior differs: six equally spaced dots on a regular hexagon succeed with three opposite pairs, while a generic convex hexagon can fail. Adult checked failing convex hexagon, in cyclic order: A=(0,0), B=(4,0), C=(7,2), D=(6,6), E=(2,7), F=(−1,3). Any group with a singleton fails because that extreme dot is outside the hull of the other vertices; hence three groups would have to be pairs. For three pairs to share an interior point in a convex hexagon they must be AD, BE, CF. AD and BE meet at (28/9,28/9), which is not on CF, so no split works. Pairwise intersection is weaker: the three sides of a triangle meet pairwise but have no common point. The new question is common concurrency, not the base two-region Radon split with larger numbers. These checks establish the line threshold and particular planar examples; they do not prove or require the seven-point planar Tverberg theorem.

Sources: Current Week 22 PDFs, editable outline `source/week-22/editable/outlines/week-22-four-point-convex-partitions.md`, and facilitator guide pp. 3–4 and 20 supply the hull conventions and exclusions. Gallier and Quaintance, Aspects of Convex Geometry, §3.5, is the base verified Radon source. The triangulation witness proof, compact-hull separator proof, line three-group threshold, and finite hexagon checks above are independently derived for this outline. No newly consulted outside source body or general higher-dimensional theorem is claimed.

Suggested emphasis by level

- K–1: optional oral entry to preserving one marked target while removing dots, or finding a separating ruler line; routine adult reading is appropriate, but a separate multi-group packet is not required.
- Grades 2–3: act on filled regions with movable dot markers, find small witnesses and line separators, then use five collinear labels for a three-group common-point challenge.
- Grades 4–5: certify the at-most-three witness, explain separator impossibility, and distinguish pairwise meetings from one common point. The general-plane three-group proof is not an expected task.

Materials

For each pair: twelve movable labeled dot markers, one distinct target marker, three pencils with different hatch styles as well as colors, six tracing-paper sheets, a straightedge, blank paper, removable tape and erasers. Use working regions at least 13×13 cm; keep equal x/y scaling for regular hexagons. Dot centers are ideal points; marker thickness and colored strokes cannot create a false intersection. Show filled hulls, not only outlines. A one-dot hull is a point and two-dot hull a closed segment. Every label is used exactly once only in the partition investigations; the small-witness investigation intentionally keeps a subset. For a separator, all of each group must lie strictly on its own side and no dot lies on the separating line. Three-group recording should be one marked shared point on one recoverable diagram, not three independent pairwise marks. Physical overlay alignment and young-child rule retention remain untested.

Base exclusions and novelty

- Base packets already enumerate successful two-group partitions of four labels, classify coincidences/collinearity, create shared segments, prove the four-point guarantee and sharpness against three, and prescribe arrangements with exact success counts.
- Base adult extensions already discuss five/six-label positive-area overlap, the one-dimensional threshold for two groups, and the absence of a universal fixed split. Do not repeat these.
- New investigations are (1) at most three dots witnessing one target in a hull, (2) a line certificate for disjoint fixed groups, (3) one point common to three groups with a sharp line theorem and contrasting planar configurations. Multiple example shapes do not inflate the investigation count.


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

Your run folder is /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-22-bonus-v1. Keep all your files inside it: sources in /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-22-bonus-v1/draft/src/ and the three finished PDFs at exactly these paths:

  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-22-bonus-v1/draft/k-1.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-22-bonus-v1/draft/grades-2-3.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-22-bonus-v1/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
