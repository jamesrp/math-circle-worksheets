You are the mathematical designer for this week's math-circle pages. You will not write the pages; a separate writer will turn your design into student pages, following the organizer's standard (included below so you know what the pages must be like). Your job is to choose and sequence the problems so that the pages can be excellent.

=== Activity outline ===

Week 7: Take-away games

Mathematical kernels

1. Backward induction. In a take-away game there is a pile of counters; two players alternate removing counters, and each move must remove an allowed number (for example 1 or 2). Whoever takes the last counter wins. Every pile size is either a win for the player about to move or a loss: a pile is losing when every allowed move leads to a winning pile, and winning when at least one move leads to a losing pile. Working up from an empty pile classifies every size. A winning strategy means always moving to a losing pile, and it must answer every possible reply of the opponent, not just the replies you expect.

2. Repeating patterns. With moves {1, 2} the losing piles are the multiples of 3. With moves {1, 3, 4} the losing piles are those leaving remainder 0 or 2 when divided by 7. With moves {1, 3, 5} the game is decided by whether the pile is even or odd. For any finite set of allowed moves the win/lose pattern eventually repeats: each label depends only on a fixed number of earlier labels, and there are only finitely many possible windows of labels (pigeonhole). Changing the rule changes the pattern, and the obvious greedy move (take as many as you can) is often wrong.

3. Beyond win and lose. Sprague–Grundy values (the smallest number not among the values of the positions you can move to) let you play sums of games, such as two piles where each turn you move in one pile. Two piles of the same game with equal values are a loss for the player to move. Research continues on when such patterns repeat; for example, whether every finite octal game is eventually periodic (Guy's conjecture) is still open. Sources: Berlekamp, Conway, and Guy, Winning Ways; Siegel, Combinatorial Game Theory.

Suggested emphasis by level: K–1 plays small games with moves of 1 or 2 and looks for traps; grades 2–3 classify piles under a rule such as {1, 3, 4} and test claimed strategies against every reply; grades 4–5 find and explain repeating patterns and compare what happens when the rule changes.

Materials

Counters (plenty), paper, pencils, and small whiteboards. Children play in pairs or threes.


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

=== What to produce ===

Write a design document to /home/claude/genlab/runs/B5-B-r1/design.md. For each band (K–1, grades 2–3, grades 4–5):

1. The mathematical thread for this band: what the children should come to see, and how it connects to the kernels in the outline.
2. The sequence of numbered problems. For each problem give the exact task in plain words, the exact instances (boards described precisely enough to draw, for example by listing their small triangles or their outline vertices on the triangular grid; pile sizes; move rules; starting positions), what the child does with the materials, what the child records and roughly how much space that needs, the intended answer or outcome, and what an adult might watch for. Do not write hints into the tasks.
3. A time budget: minutes for a quick child and for a typical child, problem by problem. The quick child in every band must have at least forty minutes of substantial work, with later problems that reward a child who gets far.
4. Why the level is right: what makes the entry easy and where the real challenge is. K–1 must get real mathematics (possible or impossible, all the ways, fewest pieces, how to win), posed with objects and few words, with as much to do as the other bands.

Verify every answer, count, and claim with code (enumerate tilings, coverings, or game positions). Put your verification scripts in /home/claude/genlab/runs/B5-B-r1/design-checks/ and state in design.md what each one confirmed. Make sure no problem can be carried out in a way that breaks it (for example a starting position from which the instruction is impossible) unless that is the point.

Work only inside /home/claude/genlab/runs/B5-B-r1: do not read any file outside it, do not use web search or fetch, and do not use remote-device, computer, or browser tools.

Reply with one sentence when design.md is written.
