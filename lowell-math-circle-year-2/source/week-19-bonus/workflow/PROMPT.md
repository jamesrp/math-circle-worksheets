Task-specific encore scope (user instruction overrides the generic three-band output paths below):
For Week 19, produce ONE shared selected-band bonus companion, with at least three genuinely distinct investigations matching the outline. Output draft/bonus.pdf, sources draft/src/; reviser outputs final/bonus.pdf, sources final/src/. Ignore references below to three mandatory band PDFs. Select honest grade/readiness coverage; the adult guide will supply the route. Student header: Week 19 / <topic> encore / Grades <appropriate range>. Footer: Bellingham Math Circle / Week 19 / W19-BON-v1. Consecutive Problem N labels. A problem's requested action must be explicit. Printed suitable bands may be stated compactly in problem text if distinct from the overall coverage. Do not force young versions. No base packet, guide, global index or workflow-template edits. No uploads or publication. Material remains unpiloted. Your ONLY stage is the stage named in this file.
Build using /Library/TeX/texbin/pdflatex (portable scripts should find pdflatex on PATH or documented PDFLATEX override). Python with PyMuPDF/ReportLab/Pillow is /Users/jamespfeiffer/math-circle/tmp/encore-18-34-venv/bin/python. Render helper /Users/jamespfeiffer/math-circle/tmp/encore-18-34/tools/render.py supports --out and contact sheets. Portable sources must build without absolute project paths. No physical fit or rehearsal claim is permitted.
Writer: Choose actual investigations yourself, check they differ from base exclusions. Include all student working diagrams and light records. Prefer 3-5 pages per week, enough space over arbitrary compactness; no automatic page target. Record complete draft answers and assumptions separately at draft/answer-notes.md to support the adult guide, not on student pages. Keep PDF/source build and writer notes inside the run.
Critic: review draft/bonus.pdf and write review.md only. Math critic: independently verify every task and represented example in draft/bonus.pdf, write review-math.md plus executable independent-check.py and checks.json in the run; do not edit writer content. Reviser: copy draft/src into final/src, address both reviews, build final/bonus.pdf, render/inspect EVERY final page, and write final/revision-notes.md and final/answer-notes.md with corrected answers and assumptions. Do not write adult guide.

Write this week's student pages for a math circle: one PDF for K–1, one for grades 2–3, and one for grades 4–5. The activity outline and the session context are below, followed by the organizer's standard for student pages. Follow that standard closely; the organizer edits every page by hand, and anything that departs from it costs him time.


=== Activity outline ===

Week 19: Subset cards encore

Separate unpiloted bonus companion; do not edit the base Week 19 packets or guides. Preferred output: one selected-band `week-19-bonus.pdf` headed `Week 19 / Subset cards encore / Grades 2–5`, with an adult companion. Use the familiar complete subset deck, but each of the three investigations changes the mathematical question. The writer chooses the problems; the facts and examples below are adult checks.

Mathematical kernels

1. **Sharing a symbol has a complement-pair bound.** A collection is now legal when every two distinct chosen cards share at least one symbol; the empty card is excluded explicitly, including as a singleton collection. This is intersection, unlike the base rule forbidding containment. In the complete n-symbol deck with n≥1, a card and its complement cannot both be chosen. The 2^n cards split into 2^(n−1) complement pairs, so an intersecting family has at most 2^(n−1) cards. All cards containing one chosen symbol attain the bound: 4 for a three-symbol deck and 8 for a four-symbol deck. A largest family need not have one common symbol: in the three-symbol deck `AB, AC, BC, ABC` is intersecting with no symbol on all four cards. Thus pairwise intersection and a common symbol in every card are genuinely different conditions. In a four-symbol deck the family of all cards of size at least three plus three two-symbol cards forming a triangle or a star also has eight cards, giving elementary alternatives. The optimum proof needs only complement pairs, not an advanced extremal-set theorem.

2. **Minimal triggers reconstruct a monotone rule.** A rule marks some subset cards as “works,” with the promise that adding symbols can never turn a working card into a failing one. The working cards form an upward-closed family. Its minimal working cards are an antichain, and every working card contains at least one minimal working card: descend by removing symbols while preserving success until no further removal works. Conversely any antichain of trigger cards defines exactly one monotone family, namely all cards containing at least one trigger; those triggers are precisely its minimal members. Example check: triggers `AB` and `C` on `A,B,C` give working cards `AB, C, AC, BC, ABC`. This is a new creation/reconstruction investigation, not another search for the largest antichain. The rule with no triggers has no working cards; the rule triggered by the empty card makes every card work. A concrete story or testing station can use colored symbol tiles, while a marked whole-deck record externalizes the rule so children do not memorize it. Demonstrate a non-task trigger input → contained trigger check → works/fails output before first use.

3. **Allowing a pair but forbidding a nested triple changes the extremal problem.** A new collection may contain one card inside another, but may not contain three distinct chosen cards X⊂Y⊂Z. A covering partition into chains now supplies at most two chosen cards per chain, or fewer if a chain has fewer than two cards. For the three-symbol deck, the familiar chain lengths 4,2,2 give upper bound 6, attained by all one-symbol and two-symbol cards. For the four-symbol deck, a complete chain partition with lengths 5,3,3,1,3,1 gives upper bound 2+2+2+1+2+1=10, attained by all two-symbol and three-symbol cards (6+4), or all one-symbol and two-symbol cards (4+6). One independently checked partition is `empty/A/AB/ABC/ABCD`; `D/AD/ABD`; `C/AC/ACD`; `CD`; `B/BC/BCD`; `BD`. Each card appears exactly once. The new obstruction is a triple, not a forbidden pair; children may first build large legal families and then look for a certificate. Do not give exactly six preprinted chains or announce ten in the student task. These two small proofs do not establish the general k-Sperner theorem.

Sources: Current Week 19 student PDFs, editable outline `source/week-19/editable/outlines/week-19-subset-antichains.md`, and facilitator guide pp. 3–4 and 11. They supply verified small chain partitions, complement reversal, and limits of the base theorem. The three encore claims above are independently derived; Stanley’s MIT 18.318 notes §4 “The Sperner property” (base source, pp. 17–25) provide adult set-order context, but this outline claims no newly read external theorem. Minimal triggers are a standard finite-order/upward-closure construction and need no Boolean-algebra prerequisites.

Suggested emphasis by level

- K–1: optional orally launched pairwise-sharing search or concrete trigger test; children must distinguish “every pair shares” from “all share one,” with adult reading. No separate young-child worksheet is forced.
- Grades 2–3: use physical cards to make and challenge intersecting collections, create a monotone rule from visible triggers, and build a family without a nested triple; counting through sixteen and symbol matching suffice.
- Grades 4–5: certify the complement bound, prove the minimal-trigger correspondence, and adapt chain capacity from one chosen card to two; the representation is the same deck with a different mathematical goal.

Materials

For each pair: two complete 16-card decks on symbols A,B,C,D, each card at least 45×45 mm with symbols in consistent positions; 20 selection counters; sixteen two-sided works/fails markers; symbol tiles or four small picture tokens; pencils and blank paper. Each deck has one card per subset, including a plainly identifiable empty card, and a different back/corner mark to prevent duplicates from mixed decks. Obtain a three-symbol deck by retaining cards avoiding the fourth symbol. A whole-deck marked record is recoverable; do not require simultaneous transcription. Adults cut cards beforehand. Supply an unconstrained stock of blank chain strips rather than a target number of lanes.

Base exclusions and novelty

- Base packets already maximize antichains for two, three and four symbols, enumerate maximum collections, keep prescribed starting cards, minimize nested-row counts, and distinguish maximal from maximum. The base guide additionally complements families and studies one/two removed cards. Avoid repeating any of these as an encore question.
- New investigation 1 changes containment prohibition to pairwise intersection; investigation 2 uses antichains as minimal generators for rules; investigation 3 allows nested pairs and forbids only triples, giving a new capacity theorem. No new theme is counted merely because the same deck receives another rule.


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

Your run folder is /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-19-bonus-v1. Keep all your files inside it: sources in /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-19-bonus-v1/draft/src/ and the three finished PDFs at exactly these paths:

  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-19-bonus-v1/draft/k-1.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-19-bonus-v1/draft/grades-2-3.pdf
  /Users/jamespfeiffer/math-circle/tmp/worksheet-runs/week-19-bonus-v1/draft/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Use LaTeX with TikZ (or Python-generated TikZ) for the pages and diagrams. Check answers with code where that helps. Before you finish, compile each PDF, render its pages to images (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Work from this brief. Do not base the pages on existing worksheets elsewhere in the repository.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
