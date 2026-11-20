# Week 106 (Coloring maps) draft review

Reviewer stage. I read PROMPT.md and both `.tex` sources, rendered every page of `draft/k-1.pdf` (8 pages) and `draft/grades-2-5.pdf` (12 pages) at 80 dpi, and zoomed to 150–200 dpi where a detail mattered. I rebuilt both PDFs from `draft/src/` in a scratch copy. The rebuild compiled with only four 1.3 pt overfull boxes in K–1, which are harmless, and its text matches the draft PDFs. I reran `game.py`, `figs.py check` and `check_torus7.py`.

## What is right (verified)

- **Headers and footers.** Every page has the header "Week 106 / Coloring maps / K–1" or "… / Grades 2–5" and the footer "Bellingham Math Circle / Week 106 / W106-k-1-v1" or "W106-grades-2-5-v1", with page numbers. The pages are US Letter. Problems are numbered consecutively.
- **Register.** The pages use American spelling throughout and have no exclamation marks, extra headings, encouragement or em-dash asides. Nothing relies on color printing: the K–1 rule pictures use hatch patterns.
- **Every printed map has the expected minimum number of colors.** I checked this by rasterizing each map:
  - K–1:
    - Scribble maps need 2.
    - T needs 3, plus 2, Y 3, line-and-loop 2.
    - Ponds with 4/5/6/7 countries need 2/3/2/3.
    - Flowers with 3/4/5/6 petals need 4/3/4/3.
  - Grades 2–5:
    - The four P1 maps need 2.
    - P3 needs T 3, six-spoke star 2, Y 3, dangling line 2, ladder 3, five-spoke star 3. Including the six-spoke star (lines stop at the center, but it is still 2-colorable) and the dangling line is a good choice.
    - Rings of 4/5/6/7 need 2/3/2/3, and wheels need 3/4/3/4.
    - The labeled wheel-5 is in ring order A–E around F.
- **Game claims.** I reran the computer check.
  - K–1 strip of 4 with 2 colors and the Painter first: the Spoiler wins.
  - K–1 pond of 4 with 2 colors and the Spoiler first: the Painter wins.
  - Tic-tac-toe board with 3 colors: the Spoiler wins whoever starts.
  - With 4 colors: the Painter wins whoever starts. A child can explain why: the middle square is the only one with four neighbors, so it is the only square that can ever get stuck.
- **Donut maps.**
  - The torus answers are stripes 4 → 2, stripes 3 → 3, 4×4 → 2 and 3×3 → 3.
  - On the seven-country board, all 21 pairs share a border. The shortest shared border is 0.24 of the board side.
  - Each country is connected on the torus, and every edge-cut piece is numbered.
- **Coverage of the outline.** Every kernel appears, in a sensible order, and the donut material is late in the grades 2–5 packet.
  - The grades 2–5 packet in particular varies what children do: color, draw and try to break, generalize, play, and a strange world.

## Serious problems (fix before printing)

1. **P11 and P12 (grades 2–5) use the donut board's frame line in two opposite ways.**
   - In P11 the frame line is a border: the leftmost and rightmost stripes are different countries that touch across the edge.
   - In P12 the frame line is not a border: pieces of country 4 continue across it.
   - The P11 text makes this worse: "a country that runs off the right edge comes back on the left edge". A child can reasonably read the leftmost and rightmost stripes in P11 as one country, which turns 4 stripes into a ring of 3 and gives the answer 3 instead of 2. On the same reading the 3×3 grid needs 2 colors, not 3.
   - Fix: number the countries in the P11 maps as P12 does (different numbers on the two sides of an edge mean different countries), and state the convention once in P11. P13's blank boards need the same convention.

2. **No rule says a country must be one piece.**
   - The four color theorem, P6 ("5 countries that all touch") and P8 ("a map that needs five colors") all depend on connected countries.
   - A child who draws a country in two separate parts can genuinely make five mutually touching "countries" and a map that needs 5 or more colors. Children often draw maps like this.
   - The rule P12 states ("Pieces with the same number belong to the same country") positively invites disconnected countries on the flat page.
   - Fix: add one clause to the grades 2–5 opening rules: "Each country is one piece." Mention in P11 that on the donut board, pieces join across the edges.

3. **P13 (grades 2–5) comes after the answer has been shown.**
   - P12 has just shown 7 countries that all touch. P13 ("as many countries as you can") then becomes either copying P12 or trying for 8, which is impossible and has no foothold.
   - The natural donut question mirrors P6: on a flat page 5 is impossible, so can you draw 5 (then 6) all-touching countries on the donut? That task is constructive, uses the wrap, and makes P12's 7 a payoff rather than a given.
   - Fix: move a "draw 5 countries that all touch on a donut board" task before P12. If P13 stays, rephrase it so its target is clear.

4. **The K–1 game rule never says a move must obey the coloring rule.**
   - P7 says "Take turns coloring one square" and "A square that touches both colors is stuck", but does not say you may not color a square to match its neighbor.
   - The grades 2–5 version states this ("keeping the coloring rule"). For five-year-olds playing Spoiler, a matching color is the obvious way to "spoil", and it breaks the game.
   - Fix: add a short clause, for example "Color a square so it does not match the square next to it."
   - Also give K–1 a tiny picture of a stuck square: a hatched square, then an empty one, then a differently hatched one. Per AGENTS.md, an unfamiliar procedure needs a worked visual at first use, and "stuck" is the whole game.

## Significant concerns

5. **The K–1 coloring load may use up the hour before the game.**
   - P1–P3 are six frames of about 17 × 8 cm, every region to be filled with thick pencils. P2's Venn map alone has an outside region of about 100 cm².
   - At a kindergartner's coloring speed, P1–P2 could take most of the 35–40 minutes. The games (P7–P8), which the context says engage children most because the other player enforces the rules, would then never be reached.
   - This is a hypothesis, not observed. Consider some of these:
     - Smaller frames for P1–P2, or one map each.
     - Letting the K–1 page say "Put a color in every country" so that quick scribbles count.
     - Moving a game earlier.

6. **The K–1 game pair changes two things at once.**
   - P7 is the strip with the Painter first, where the Spoiler wins. P8 is the pond with the Spoiler first, where the Painter wins.
   - Children cannot tell whether the map or the starting player caused the reversal. On both maps the second player wins.
   - Fix: have P8 replay the strip with the Spoiler first, then the pond both ways. Alternatively, play the pond with the Painter first and then with the Spoiler first.
   - Either way the cleaner discovery is that going first is bad here.

7. **K–1 P7 is too long to make sense after one hearing.**
   - It has eight sentences, against the standard of one or two short sentences per K–1 problem.
   - "One of you is the Painter and one is the Spoiler" and "Swap jobs after each game" can be cut to the essentials. The launch demonstration carries the rest.
   - "If all 4 squares get colored" carries over awkwardly to P8's pond countries. "If every square gets colored" or "every country" would work for both.

8. **Grades 2–5 P2 asks for the hardest proof in the packet second.**
   - P2 ends with "If you think every map like this can be colored with two colors, explain why." This is the parity argument.
   - A second grader who stalls here never reaches P3–P5, which are more accessible.
   - The explanation also comes more easily after P3, where children see that only a line that stops partway breaks two colors.
   - Fix: keep P2 as the drawing challenge, and move the "explain why it always works" question to after P3, either as its own problem or folded into P3's explanation.

9. **P8 (five-color challenge) does not say where the map is drawn and colored.**
   - "Give it to your partner, who tries to color it with four colors" works on paper, but there are only two boxes and colored maps cannot be erased.
   - On the whiteboards it may not work, because the markers come in only 3 or 4 colors, so a 4-color attempt may be impossible there.
   - Fix: say "On your whiteboard…" and allow writing 1–4 in each country, or say "on paper" and add more boxes.
   - Partners will often fail to 4-color a complicated map they could have, so the adult has to check any claimed five-color map. That belongs in facilitator notes, which this workflow does not produce. Flag it for the guide stage.

## Minor issues

10. **Two figures are nearly tangent.**
    - Grades 2–5 P1, Venn-plus-line map: the curve passes only about 1.6 mm below the bottom circle, so it looks tangent at print size. Children will ask whether it touches, or whether there is a sliver country there. Make it clearly cross the circle or clearly miss it.
    - K–1 P2 Venn: the bottom circle sits about 0.5 mm from the frame's bottom edge and looks tangent. Raise it.

11. **K–1 country sizes are borderline.**
    - The K–1 Venn's smallest regions are about 2.6 cm² (about 1.6 cm across).
    - The small top-right triangle in P1's first map is about 3.4 cm².
    - These are borderline for "K–1 countries much larger" with thick pencils. Enlarging the circles would help.

12. **Some sentences describe a diagram or narrate.**
    - "The arrows mark the edges that are joined." and "So countries can share a border across an edge of the board." (P11)
    - "This is a donut map of 7 countries." (P12)
    - "Now" opening P5.
    - The arrows do need a gloss, but the single and double arrow types are never explained. Matching letters on paired edges might be more transparent for children than arrow conventions.

13. **The K–1 packet varies little in what children do.**
    - Six of the eight K–1 problems are "color these maps" (P4–P6 at least ask for the fewest pencils).
    - This is the organizer's stated worry. A K–1 making task would vary the experience at no reading cost, for example "Draw a map that needs 3 pencils" or "Draw a flower that needs 4 pencils".

14. **The grades 2–5 packet carries a heavy writing load.**
    - "Explain" with ruled lines appears in 8 of 13 problems.
    - Each explanation is defensible as the point of its problem. Together they are heavy for third graders. Some could be oral, without lines, which the organizer may prefer.

15. **P7 (grades 2–5) gives away P5's answer.**
    - It states "This map needs four colors" about the same wheel-5 map that P5 asked children to work out. This is harmless, since P5 comes first.
    - P7 could instead ask why the map needs four colors when no four countries all touch, which is the real surprise.
