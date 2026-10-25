# Review of draft/k-1.pdf (Week 57 / Area from dots / K–1, N57-K-v1)

Reviewer stage. I did not edit the draft. My scratch files are in `review-check/` (my own enumeration and vector-measurement scripts) and `review-render/` (page renders). They are not part of the packet.

## Verdict

The draft is close to usable. It covers the brief's development well: printed outlines, then the child's own three-half shapes (always 5), then four halves (the tilted square breaks the pattern), then closing in dots, then fewest outline dots for eight halves. The mathematics is correct, the boards are true 20 mm, and the format follows the standard. Seven problems on six pages give K–1 enough to do. Nothing on the pages needs the organizer's usual deletions.

Fix these before approval:

1. Problem 6's question, "How many different shapes can you find?", has no stated answer until turned copies are settled. Turns give 16 placements on the fixed board, against 6 shapes. (Must fix.)
2. Problem 5, the hardest optimization, comes before Problem 6, the accessible one-dot enumeration it builds on. Swapping them also puts Problem 5's best answer right before Problem 7. (Should fix.)
3. Problem 4's wording ("If they can't, explain why") tells the child the answer. (Should fix.)
4. The answers to Problems 2, 3 and 7 depend on the rule that pieces meet along whole sides. "Pieces touch side to side" may not get that across to a five-year-old who hears it once. (Should fix.)

The other points below are smaller.

## What I checked

- **Every page, rendered.** At 100 dpi for all six pages, 200 dpi for page 1, and 254 dpi for measuring. Nothing overflows or overlaps, and every diagram matches its source.
- **Scale, from the PDF's vector paths** (`mutool trace`, `review-check/vec.py`). Every working board's dot spacing is exactly 20.00 mm in both directions on pp. 2–6. The P1 shapes are also 20 mm, so the kit's pieces fit them. All ink lies between 15.0 and 200.9 mm across the 215.9 mm page, so the side margins are respected. Working-board dots are 2.6 mm across. The launch strip at the top of p. 1 is deliberately drawn at a 12 mm scale.
- **Header, footer and fonts.** The header reads exactly "Week 57 / Area from dots / K–1". The footer reads exactly "Bellingham Math Circle / Week 57 / N57-K-v1", with the page number at the right. Fonts are embedded (TeX Gyre Heros). There are no Name/Date fields.
- **Standard compliance.** No titles beyond the header and problem labels, no encouragement, no exclamation marks and no hints. Every problem is one or two short sentences. Problems are numbered 1–7 in order. There are no letters I or B and no fractions.
- **Mathematics: an independent enumeration** (`review-check/pa_enum.py`, `analyze_r.py`, `pieces_r.py`). I wrote it from scratch, without using the author's `draft/check/` scripts. It models shapes as unions of quarter-triangles of unit cells and reads inside and outline dots from the eight 45° sectors at each dot, so it never assumes Pick's rule. It reproduces the free polyabolo counts 1, 3, 4, 14, 30, 107, 318 and 1116.

| Problem | Answer the page expects | Verified |
|---|---|---|
| P1 | half 1→3; square, triangle, parallelogram 2→4; 1×2 rectangle, trapezoid 4→6 | yes |
| P2 | Three halves make 4 shapes (6 if mirror images count as different), all with 5 outline dots, so the answer is no. All fit the 3×4-dot boards. | yes |
| P3 | Four halves make 14 shapes: 13 have 6 outline dots, and the tilted square has 4 with 1 inside. All 14 fit the 3×4-dot boards. | yes |
| P4 | No. A brute-force search over all placements of three pieces near the dot finds no closure. | yes |
| P5 | Fewest pieces is 6. There are exactly 7 six-piece shapes (up to symmetry) for the horizontal pair, using 8 to 12 halves with 6 to 10 outline dots. One is the 2×3 rectangle; another is the roofed hexagon, which uses 8 halves and has 6 outline dots. All fit the 6×5-dot board. | yes |
| P6 | Exactly 6 shapes (up to turns, and also up to turns and flips), with 4, 5, 6, 6, 7 and 8 halves. Each has as many outline dots as halves. All fit the 3×3-dot boards. | yes |
| P7 | Exactly 2 allowed shapes of eight halves have fewer than 8 outline dots: the tilted domino and the roofed hexagon, both with 6. Both fit 5×5-dot boards. | yes |

Gap check for P7. The 11 eight-half shapes that pinch off a corner gap all have 9 outline dots when the pinch dot is counted once, so a gap cannot produce a false "fewer than 8". The "no gap" rule is still needed. A child who calls the dots around a pinched gap "inside" could count 7.

## Must fix

### 1. Problem 6: say whether a turned shape counts as new
"How many different shapes can you find?" is the whole question, and its answer depends on a convention the page never gives:

- With the boxed dot fixed and each of the four cells around it holding a square or a half, there are 16 placements.
- Treating turns as the same gives 6.
- Treating turns and flips as the same also gives 6, so flips need no mention.

A child who counts turned copies will fill all nine boards, run out of room and still not have the answer. Add a few words to P6, for example "A turned shape is the same shape." It would also do as a second sentence after the question. Problems 2 and 3 have the same ambiguity, but there it does not change the answer, so P6 is the only place it must be stated. The three spare boards then become ordinary extra space.

## Should fix

### 2. Put Problem 6 before Problem 5
The current order is P4 (can three pieces close in a dot?), P5 (two dots, fewest pieces), P6 (one dot, four pieces, all the ways), P7 (eight halves, fewer outline dots).

- P6 is the concrete foundation: one dot, four pieces, a small board that keeps the work near the dot, and records that show halves equal to outline dots. P5 is a hard optimization whose minimality argument is adult-level. Each of the six cells around the two dots must hold a piece, and the two middle cells must be whole squares.
- The context asks for deeper questions late in the packet, and a K–1 pair who stalls on P5 would never reach the more accessible P6.
- Order P4, P6, P5, P7 also puts P5 directly before P7. One of P5's six-piece answers is the roofed hexagon, which is 8 halves with 6 outline dots: exactly a P7 answer. Children who found it in P5 then have a route into P7.

Layout consequence: P4 and P5 share p. 4 now. After the swap, P4 can stand alone on a page or keep a smaller board, P6 takes a page, P5 takes a page, and P7 takes a page. Seven pages is fine.

### 3. Problem 4: do not give the answer in the question
"Can three pieces make a shape with the boxed dot inside? If they can't, explain why." The second sentence tells the child the answer is no. AGENTS.md asks for open questions. Use a two-sided form, as in the coins exemplar: "If they can, make one. If they can't, explain why." The impossibility explanation is the point of this problem, so keep it; just do not presuppose its outcome.

### 4. Make the whole-side rule unmistakable
The shared rules say "Pieces touch side to side." A five- or six-year-old hearing it once may take it as "put them next to each other". Putting halves tip to tip is exactly what young children do with triangles. That rule decides three answers:

- **P2.** Two halves touching only at a corner have 5 outline dots instead of 4, so three halves with one corner contact can give 6. The child would then find "different numbers", and the intended discovery that every three-half shape has 5 collapses.
- **P3.** The same thing happens with four halves.
- **P7.** It also changes the counts there.

Two fixes, which work together:

- Reword the rule so it is heard correctly, for example "Each piece touches another piece along a whole side."
- Add a small two-picture convention example beside the existing launch strip: two halves sharing a side (yes) and two halves touching only at a corner (no). This is the kind of essential convention example AGENTS.md places with the shared rules, and pictures cost K–1 less than words.

## Smaller points (fix if cheap)

### 5. Counting halves when a shape has squares (P6 records)
P6's record asks for the number of halves, but P6 shapes mix squares and halves. The expected entry for two squares and two halves is 6. A child will probably say 4, or "two squares and two halves". P1 does ground the idea: children cover the printed square with two halves and record 2. The guide's launch also has a child join two halves into a square. So this is moderate. If the reviser adds the yes/no picture from point 4, the same strip could also show two halves becoming one square, which supports P1's and P6's records. Otherwise leave it to the adult and say so in the guide.

### 6. Record icons are not demonstrated
The record icons (a grey half, and a circled dot, each followed by a blank) are never shown in use. An adult can infer what they mean, but AGENTS.md asks for recording conventions to be demonstrated. A cheap fix: under the launch strip's third panel, add its own record, a circled-dot icon with 8. Do not add a halves record there. The launch square has an inside dot (8 halves, 8 outline dots), and showing that first would cut across the P1–P3 pattern that outline dots equal halves plus 2.

### 7. P1 repeats a shared rule
"Then circle the dots on its outline" repeats the last sentence of the opening rules. The repetition is defensible on the first problem, so this is optional. Meanwhile P1's record also wants the number of halves, which the text never mentions; the adult writes both counts, so this is acceptable.

### 8. The launch strip is not at actual size
The launch strip uses a 12 mm grid, so a child who sets 20 mm pieces on it will find they do not fit. That is harmless, but a child who tries may be briefly confused. Either leave it, or draw the first panel at 20 mm if space allows. There is about 35 mm spare at the bottom of p. 1, and a 20 mm first panel adds only about 16 mm of height.

### 9. P7's two boards nearly touch
P7's two 5×5 boards are 3.2 mm apart frame to frame, and only 12 mm apart dot to dot, which is less than one 20 mm spacing. The frames separate them, but a 5 to 10 mm larger gap would read more clearly. The boards could also be narrower in total, since both answers fit within three spacings.

### 10. P5 has no record line
P5 has no record line. The pieces sit on the board and can be counted, so this matches "keep bookkeeping light". A piece-count line (a piece icon and a blank) would let a pair keep their best count after the pieces go back in the kit for the next problem. Optional.

## Checked and fine as is

- **Launch.** The pages start from the shared launch and do not make the 2×2 square a task. It appears only as the convention strip on p. 1 and as P7's reference. The strip's sequence (pieces on dots, outline traced with pieces lifted, outline dots circled and inside dot boxed) is the input, step and output visual the brief asks for. It solves the "pieces hide the dots" problem without prose.
- **No overlap with Week 26 or the older bands.** There is no whole-square boundary task repeating Week 26 in dot form. Nothing copies the older packet's problems. The overlap is in answers only: the older P3 asks for a four-sided shape with I = 2 and B = 6, which the tilted domino satisfies, and the tilted domino is also a P7 answer. The brief itself lists that instance for K–1 under kernel 2, the tables do not mix, and the tasks differ.
- **The brief's "whole squares as a familiar entry" is not used.** P1 requires halves. That is a reasonable choice: it avoids repeating Week 26 and makes "a square is two halves" something children do. No change needed.
- **Board sizes suit their use.** The 3×4-dot boards in P2 and P3 force long shapes to be turned upright, because the trapezoid from P1 is three spacings long. Every shape still fits, as verified. The 3×3 boards in P6 confine pieces to the four cells around the dot. That gives the enumeration a clear frame without telling the child the answer.
- **Records stay light.** The adult writes the counts, children circle and box, and nothing asks for running tallies.
- **Amount.** Seven problems is more than a K–1 pair will finish in 35–40 minutes, and stopping anywhere is fine. Each problem supports several minutes of building. P4 alone is the shortest, and it shares its page with P5.

## Physical and operational notes for the guide (not page fixes; untested)

- **Who traces, and how often.** The p. 1 strip shows tracing before lifting. A pair working through P2, P3, P6 and P7 could produce more than 20 shapes to trace, and the table has two pairs. If the parent traces them all, that becomes the bottleneck. The kit's coloured pencils suggest children can trace while their partner holds the pieces. The guide should choose.
- **The 2.6 mm dots are an untested choice.** The working boards use 2.6 mm dots, larger than the older pages' 1 mm. A half's sharp corner leaves about 7/8 of an outline dot visible, a square corner 3/4 and a straight side 1/2. An inside dot, and its printed box, should disappear completely. The box disappearing on P4 to P6 means the dot is inside, which is a nice check by the material itself. Hand-cut pieces may still cover an outline dot or leave an inside dot showing through a crack. Nobody has tried this. Whether pieces stay on the dots in rows of three or four (the P1 trapezoid, P2 and P3) is also untested.
- **What the adult must know.** All of the following must be in the facilitator guide; the pages cannot carry them:
  - a turned shape is the same shape (until point 1 is fixed);
  - a square counts as two halves when recording;
  - pieces must meet along whole sides, and no gap may be left, including a gap that reaches the outside only at a corner (relevant from seven halves, so in P7);
  - P5 and P7 are hard, with answers of 6 pieces and 6 outline dots;
  - the minimality argument for P5.
- **Readiness.** The packet has not been piloted with children, and the kit has not been rehearsed with K–1.
