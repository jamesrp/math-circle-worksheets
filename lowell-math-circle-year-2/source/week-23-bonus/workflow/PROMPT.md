Task-specific encore scope (user instruction overrides the generic three-band output paths below):
For Week 23, produce ONE shared selected-band bonus companion, with at least three genuinely distinct investigations matching the outline. Output draft/bonus.pdf, sources draft/src/; reviser outputs final/bonus.pdf, sources final/src/. Ignore references below to three mandatory band PDFs. Select honest grade/readiness coverage; the adult guide will supply the route. Student header: Week 23 / <topic> encore / Grades <appropriate range>. Footer: Bellingham Math Circle / Week 23 / W23-BON-v1. Consecutive Problem N labels. A problem's requested action must be explicit. Printed suitable bands may be stated compactly in problem text if distinct from the overall coverage. Do not force young versions. No base packet, guide, global index or workflow-template edits. No uploads or publication. Material remains unpiloted. Your ONLY stage is the stage named in this file.
Build using /Library/TeX/texbin/pdflatex (portable scripts should find pdflatex on PATH or documented PDFLATEX override). Python with PyMuPDF/ReportLab/Pillow is /Users/jamespfeiffer/math-circle/tmp/encore-18-34-venv/bin/python. Render helper /Users/jamespfeiffer/math-circle/tmp/encore-18-34/tools/render.py supports --out and contact sheets. Portable sources must build without absolute project paths. No physical fit or rehearsal claim is permitted.
Writer: Choose actual investigations yourself, check they differ from base exclusions. Include all student working diagrams and light records. Prefer 3-5 pages per week, enough space over arbitrary compactness; no automatic page target. Record complete draft answers and assumptions separately at draft/answer-notes.md to support the adult guide, not on student pages. Keep PDF/source build and writer notes inside the run.
Critic: review draft/bonus.pdf and write review.md only. Math critic: independently verify every task and represented example in draft/bonus.pdf, write review-math.md plus executable independent-check.py and checks.json in the run; do not edit writer content. Reviser: copy draft/src into final/src, address both reviews, build final/bonus.pdf, render/inspect EVERY final page, and write final/revision-notes.md and final/answer-notes.md with corrected answers and assumptions. Do not write adult guide.

Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 23: Sorting machines encore

Separate unpiloted bonus companion; leave base Week 23 packets and guides untouched. Preferred output: one selected-band `week-23-bonus.pdf` headed `Week 23 / Sorting machines encore / Grades 2–5`. The writer chooses the problems and networks. Retain genuinely fixed bars and the two-lane compare-exchange action. The three new guarantees concern selection, merging, and equal-card order rather than another complete sorter search.

Mathematical kernels

1. **Selection can require less than full sorting.** A four-lane network that places only the smallest value in lane 1 can use three bars, e.g. (1,2),(1,3),(1,4), without ordering the other lanes. Three are necessary: until a value has lost a comparison it might be the minimum, and one bar can eliminate at most one of four distinct candidates. A different partial goal puts the two smallest values in lanes 1 and 2 in either order and the two largest in lanes 3 and 4 in either order. The four-bar network (1,2),(3,4),(1,4),(2,3) achieves that goal. After the first two bars write a≤b in lanes 1,2 and c≤d in lanes 3,4. Outputs are min(a,d), min(b,c), max(b,c), max(a,d). Each of the first pair is ≤ each of the last pair: the direct pair inequalities hold, and min(a,d)≤a≤b and ≤d gives ≤max(b,c), while min(b,c)≤c≤d and ≤b gives ≤max(a,d). Thus the first pair is precisely the lower half, including ties. It need not itself be sorted: input 3,4,1,2 yields 2,1,4,3. A shortest-bar claim for the lower-half goal needs an independent audit or a separate proof; the writer may make construction and deliberate unsorted outputs the central task without demanding that lower bound. This changes the output specification, not the number labels.

2. **Two already sorted pairs need only three merging bars.** Inputs satisfy lane1≤lane2 and lane3≤lane4 before entering; a machine must still be fixed for every such input. The network (1,3),(2,4),(2,3) fully sorts them. The first bar settles the global minimum in lane 1 because each initial pair minimum is known; the second settles the global maximum in lane 4; the final bar orders the two middle values. For four distinct ranks there are six inputs obeying the pair precondition: choose which two ranks belong to the first pair and put each pair in order. At least three bars are necessary, because two bars have at most four swap/no-swap records, each record can sort at most one distinct input. Three attain the bound. The argument includes repeated values for correctness although the lower bound uses distinct inputs. Removing the precondition makes this three-bar merger fail, so physically preserve two sorted trains as the starting input and make the legal-input change explicit. The base full sorter uses two preliminary pair comparisons plus this merge; turning the precondition into the investigation is the new mathematics.

3. **A sorted output can still change equal-card order.** Give equal-valued cards distinct corner identifiers. A stable sorter keeps the input relative order of any two equal-valued cards in its sorted output; identifiers do not participate in comparisons, and ties do not swap. Any neighbor-only compare-exchange network is stable: two cards reverse relative order only by crossing each other, which would require directly swapping them when adjacent; equal cards never do. A nonneighbor comparator can jump one equal card over another without comparing the pair. Concrete counterexample: network (1,3),(1,2),(2,3), input 2A,2B,1C, produces 1C,2B,2A, reversing the equal 2s despite ties staying put. Neighbor network (1,2),(2,3),(1,2) produces 1C,2A,2B and sorts every three-card input stably. A worked non-task comparator example should distinguish values from identifiers and show what “same relative order” means before the first stability task. Children can design and attack machines with tagged tokens; no formal algorithmic-complexity language is needed.

Sources: Current Week 23 PDFs, editable outline `source/week-23/editable/outlines/week-23-sorting-networks.md`, and facilitator guide pp. 3,11–12 supply fixed comparator conventions, full-sorter certificates and record bounds. University of Liverpool COMP308 Lecture 17 pp. 1–2 is the base verified network source. The selection construction, merging proof and stability argument above are independently derived for this outline. No newly verified outside source-body claim is made.

Suggested emphasis by level

- K–1: optional oral smallest-card tournament or tagged equal-length-strip stability experiment; keeping a machine fixed and using identifiers only to watch order are prerequisite gates. Do not force a separate reading-heavy packet.
- Grades 2–3: construct partial selectors and three-bar mergers with physical ranked cards, then distinguish value order from the order of equal tagged cards.
- Grades 4–5: prove selection/merge guarantees, justify the merging lower bound, and explain why adjacency ensures stability while jumping bars can fail it. Formal decision trees are optional adult explanation.

Materials

For each pair: a reusable four-lane mat at least 24×30 cm, eight removable comparator strips with exactly two endpoint dots, four distinct-rank cards, six repeated-value cards bearing small distinct identifiers, four different-length strips for an oral alternative, pencils and blank paper. Cards should be at least 30×30 mm, with corner identifiers visually secondary to the compared dot count/value. Every bar sends the smaller value to the lower-numbered lane; ties keep their current positions. Children move all cards together from bar to bar. A long bar crossing an intermediate lane does not compare that lane. For merging, provide two physical two-card trays or brackets that indicate the sorted-pair precondition before the network starts. Supply spare bars rather than a frame with exactly the target number. Manual swaps, input-adaptive bars or comparing the tags alter the mathematics. Tangible compare-exchange and tagged-tie handling remain untested physical procedures.

Base exclusions and novelty

- Base packets already build/repair full three- and four-lane sorters, test binary inputs, prove zero–one certification, record swap histories, and establish full/neighbor-only comparison minima.
- Base adult extensions already optimize parallel stages, generalize adjacent inversion counts, and relabel values monotonically. These are excluded as encore directions.
- New investigations are (1) partial selection with explicitly unordered outputs allowed, (2) merging under a structural input promise, (3) preserving identities within equal values. Reusing a known three-bar network under a genuinely different guarantee is intentional; do not present it as another complete sorter construction.


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

Your run folder is /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-23-bonus-v1. Keep all your files inside it: sources in /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-23-bonus-v1/draft/src/ and the three finished PDFs at exactly these paths:

  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-23-bonus-v1/draft/k-1.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-23-bonus-v1/draft/grades-2-3.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-23-bonus-v1/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
