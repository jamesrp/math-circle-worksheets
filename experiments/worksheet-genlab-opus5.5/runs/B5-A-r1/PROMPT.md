Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.

A mathematician has already designed this week's problems. The design is in /home/claude/genlab/runs/B5-A-r1/design.md (with verification scripts in /home/claude/genlab/runs/B5-A-r1/design-checks/). Your job is to write the student pages from that design. Keep the design's mathematics, instances, and sequence. You may change wording, layout, and recording space so the pages meet the organizer's standard, and if you find an error in the design, fix it and re-verify.


=== Activity outline ===

Week 1: Tiling with pattern blocks

Mathematical kernels

1. Coloring obstructions and best possible packings. On the triangular grid every small triangle points up or down, and every blue rhombus covers exactly one up-triangle and one down-triangle. So a region with more up-triangles than down-triangles cannot be tiled by blue rhombi, even when its area is even, and the difference between the two counts is a lower bound on how many triangles must stay uncovered. This is the triangular-grid version of the mutilated-checkerboard argument (dominoes cannot tile a chessboard with two opposite corners removed). A triangle with n small edges on each side has n more up-triangles than down-triangles, so blue rhombi always leave at least n triangles uncovered, and n can be achieved. A piece made of two blue rhombi (the purple chevron) can never do better than blue rhombi alone, because each chevron splits into two blues.

2. Rhombus tilings of a hexagon, and flips. A hexagon on the triangular grid can usually be tiled by blue rhombi in several ways. Any two tilings are connected by flips: wherever three rhombi form a small hexagon, rotate them into the hexagon's other filling. The tilings and flips form a graph worth exploring (shortest flip routes between tilings; whether you can return to a tiling in an odd number of flips). Rhombus tilings correspond to stacks of cubes and to lattice paths: following the chain of rhombi that crosses the hexagon from one side to the opposite side traces a path ("ribbon") of left and right steps. Ribbons can be used to count all tilings and to prove facts about flips; for example each flip swaps an adjacent left/right pair in a ribbon, so every round trip takes an even number of flips. Sources: Thurston, "Conway's tiling groups" (1990); Saldanha and Tomei, "An overview of domino and lozenge tilings"; MIT 18.312 lectures on rhombus tilings and plane partitions.

Suggested emphasis by level: grades 2–3 work with possible and impossible boards and fewest-gap packings (kernel 1); grades 4–5 explore the tilings of a small hexagon, flips between them, and ribbons (kernel 2); K–1 works with the same pieces at an entry point suited to them.

Materials

21st Century Pattern Blocks, plenty for ten children: green triangle (each edge 1 inch), blue rhombus (two triangles), red trapezoid (three triangles), yellow hexagon (six triangles), purple chevron (a concave six-sided piece equal in area to two blue rhombi, and exactly coverable by two blues), plus pink right triangles, teal kites, and gray darts. There are no orange squares or tan thin rhombi. Upscale pattern blocks at 2× and 3× size are also available. Paper, pencils, and small whiteboards.

Any board on which children place physical blocks must be printed at actual size: the small triangle's edge is 1 inch (2.54 cm).


=== Session context ===

The Bellingham Math Circle is an elementary-school math circle that meets weekly for one hour. Its purpose is enjoyment, curiosity, and real mathematical thinking rather than school arithmetic practice.

Children at this session: ten. Two kindergartners and one first grader; four third graders; two fourth graders and one fifth grader. Grade bands (K–1, 2–3, 4–5) are rough entry points, and a child may work from another band's pages.

Adults: three. The organizer (a research mathematician), a second mathematician, and one parent volunteer who is not a mathematician. Each adult stays mainly with one band's group.

Shape of the hour: a few minutes of free handling of the materials; a short whole-group demonstration of the concrete action everyone will use; about forty minutes of work in the three groups, where children work together and talk with their adult; a few minutes of sharing at the end.

Pages are printed single-sided on US Letter paper at 100% scale.


The organizer's standard for student pages

Who uses the page. Children work in small groups at a table with an adult beside them. The adult supplies the warmth, the hints, the explanations, and the encouragement in person, so the page has one job: pose the tasks clearly and give room to work. Kindergartners and first graders mostly cannot read yet. An adult reads each problem aloud to them, so their problems must make sense after one hearing and should lean on pictures and objects.

What a page contains. A one-line header giving the week, topic, and level, for example "Week 1 / Tiling / Grades 2–3". A one-line footer, "Bellingham Math Circle / Week N" and the page number. Between them, numbered problems, each beginning "Problem N:" and continuing in ordinary sentences. Rules that hold for the whole packet may be stated once, briefly, at the top of the first page. Each problem says what to do with the specific objects involved, shows the diagrams the child needs, and leaves space to record. The header and the problem labels are the only headings on the page.

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

Your working directory is /home/claude/genlab/runs/B5-A-r1. Keep all your files inside it: LaTeX sources in /home/claude/genlab/runs/B5-A-r1/src/ and the three finished PDFs at exactly these paths:

  /home/claude/genlab/runs/B5-A-r1/final/k-1.pdf
  /home/claude/genlab/runs/B5-A-r1/final/grades-2-3.pdf
  /home/claude/genlab/runs/B5-A-r1/final/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Tools available: pdflatex, xelatex, lualatex (TeX Live with TikZ and texlive-fonts-extra), python3, pdftoppm, pdftotext. Draw diagrams with TikZ or with Python-generated TikZ. Before you finish, compile each PDF, render its pages to PNG (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page with the Read tool to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Isolation: this is a controlled experiment. Use only the information in these instructions. Do not read any file outside /home/claude/genlab/runs/B5-A-r1 (in particular nothing elsewhere under /home/claude/genlab and nothing under /mnt/user-data), do not use web search or web fetch, and do not use any remote-device, computer, or browser tools.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
