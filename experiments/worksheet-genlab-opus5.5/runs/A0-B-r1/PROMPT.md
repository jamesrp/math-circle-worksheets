Make an activity PDF for each of three grade levels (K–1, grades 2–3, and grades 4–5) targeting a 1-hour math circle where the kids will get to work with each other and also with professional mathematicians guiding them. High-level activity outline is below.


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


Technical instructions

Your working directory is runs/A0-B-r1. Keep all your files inside it: LaTeX sources in runs/A0-B-r1/src/ and the three finished PDFs at exactly these paths:

  runs/A0-B-r1/final/k-1.pdf
  runs/A0-B-r1/final/grades-2-3.pdf
  runs/A0-B-r1/final/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Tools available: pdflatex, xelatex, lualatex (TeX Live with TikZ and texlive-fonts-extra), python3, pdftoppm, pdftotext. Draw diagrams with TikZ or with Python-generated TikZ. Before you finish, compile each PDF, render its pages to PNG (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page with the Read tool to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Isolation: this is a controlled experiment. Use only the information in these instructions. Do not read any file outside runs/A0-B-r1 (in particular nothing elsewhere under /home/claude/genlab and nothing under /mnt/user-data), do not use web search or web fetch, and do not use any remote-device, computer, or browser tools.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
