# Review: facilitator guide for "Untangling networks", draft v1

I reviewed this as an adversarial reader; I did not write the guide. I read the guide (6 pages) and rendered every page at 80, 110 and 200 dpi. I also rendered and read every page of the final student packets: K–1 has 5 pages, grades 2–3 has 7 and grades 4–5 has 8. Beyond those I read the outline, both page reviews, the drafts README entry, `worksheet-workflow/context.md`, the Week 98 model guide, and Week 41's portal pages for the seam marks.

I did not edit the guide or the student pages.

## Verdict

The mathematics is right. Every answer the guide prints matches my independent recomputation against the final pages, and every problem and page number is right. The overview is a real theorem-first overview. The launch is concrete, uses a network that is on no page, and gives nothing away.

I found **no must-fix items**. The should-fix items are about fitting the plan to the actual group: the hour's time budget, staffing, and how two pairs pool their results. One sentence misdescribes what 2–3 Problem 6 asks. Several statements about how children behave read as observations, although the theme has never been piloted.

## How I checked

My script is `review-guide-check/check.py` and its output is in `review-guide-check/check-output.txt`. It uses my own geometry code, plus networkx for planarity and isomorphism tests. The steps:

- **Student pages.** I rebuilt them from `src/` in a scratch copy. All 20 rendered pages were pixel-identical to the final PDFs, so the parsed sources are the printed pages.
- **Tangled pictures.** For every one of the 13 pictures I parsed the dots and links and compared them with the printed link list. I identified each network's type, counted its crossings, checked that no two crossings fall at one point, and traced the regions of the tangled drawing.
- **Guide figures.** For all of them (`key_*`, `few_*`, `portal_*`, `launch_*`), I checked:
  - that each figure has exactly the right links, using the page's own labels;
  - its crossings, and that the "circled" marks sit on the real crossings;
  - how close links come to dots they do not belong to;
  - for the portal drawings: the exit and entry points, every link's route on the torus, the regions traced on the torus, V − E + F, the number of links that go through a portal, and whether each route is the shortest one, including ties.
- **Game boards.** For all ten boards I did an exhaustive search over every set of straight links that has no crossings and no room for another link. I also counted the outer dots and checked for dots in a straight line. For bent links, I ran random finished games for 3 to 11 dots.
- **The guide's own arguments.** I checked the ring arguments for K5 and K3,3. I checked that K3,3 minus any one link, and K5 minus any one link, can be untangled. I checked the K6 lower bound and the region counts.
- **Rebuild.** I recompiled the guide in scratch. There were no overfull, underfull or warning lines, and the text is identical to `draft/facilitator.pdf`.

### Answers verified (all correct)

| Guide claim | Result |
|---|---|
| K–1 P1: each picture has 1 crossing; moving any one dot fixes it | 1, 1, 1 crossings; every dot (A–D) works, with straight links |
| K–1 P2 (K2,3): yes, one house above the wells and one below | Key drawing: correct links, 0 crossings |
| K–1 P3, network 5 (K3,3): fewest is 1; removing any one link leaves it untangleable | Correct; Figure 2's drawing has the right links (houses A, B, C; wells D, E, F, the same labels as K–1 P3) and its 1 crossing is A–E with B–D |
| K–1 P4: a 5-ring, a fan, a prism; pictures have 5, 3 and 4 crossings | Types and crossing counts correct; key drawings have 0 crossings |
| K–1 P5, network 2 (K5): fewest is 1 | Correct; network 2's drawing is network 3's drawing plus D–E, and D–E crosses only A–C |
| Networks 1, 3, 4, 6 untangle; 2 and 5 stuck; pictures have 2, 3, 3, 4, 5, 4 crossings | Correct (fan, K5, K5 − DE, prism, K3,3, octahedron missing AF, BD, CE) |
| Figure 1 (dots, links, regions): 5,7,4 / 5,9,6 / 6,9,5 / 6,12,8 | Correct, and every key drawing has 0 crossings |
| A tangled picture has links − dots + 2 + crossings regions | Holds in all 13 printed pictures, whose crossings are all at distinct points |
| K6: 3 crossings is the fewest; the bound needs two links per crossing | The drawing has exactly 3 crossings at distinct points; 15 − k ≤ 12 gives k ≥ 3 |
| Game: 4 dots second player, 5 first, 6 second; 7 dots 15 links, first player; 10 dots 24 links (second), 11 dots 27 (first) | On all ten boards, every finished straight-link game has exactly 3n − 6 links; each board has 3 outer dots and no three dots in a line; bent-link games give 3n − 6 for n = 3 to 11 |
| Portal, network 5: A–D, A–E, A–F, B–F and C–F go direct; B–D, B–E and C–E go out the top and in at the bottom; C–D goes out the right and in on the left | Exactly the routes in Figure 3; 0 crossings; 3 regions; V − E + F = 0 |
| Portal, network 2: shortest routes, five links use a portal | Correct (A–D, A–E, B–C, B–E, D–E); no ties; 5 regions |
| Portal, 6 and 7 dots: shortest routes, 8 and 10 portal links, 9 and 14 regions | Correct; no ties; 0 crossings; the 14 regions are all triangles |
| "For network 5 the shortest routes tie" | True for all nine pairs (and A–F in Figure 3 is not a shortest route, which is fine) |
| Ring arguments | 5 chords of the pentagon, at most 2 on each side; around the ring A–D–B–E–C–F, the links A–E, B–F and C–D pairwise interleave |
| Every crossing-free portal drawing gives 3 and 5 regions | True: a connected network that cannot be untangled in the plane fills the torus in patches, so V − E + F = 0 |

### Agreement with the pages (all correct)

- **Problem-to-page maps.** These match the printed PDFs:
  - K–1: P1 p1, P2–3 p2, P4 p3, P5 p4, P6 p5.
  - Grades 2–3: P1 pp1–2, P2 p3, P3 p4, P4 p5, P5 p6, P6 p7.
  - Grades 4–5: P1 pp1–2, P2 p3, P3 p4, P4–5 p5, P6 p6, P7–8 p7, P9 p8.
- **Pages cited in the Print paragraph.** Packet lengths, game-board pages and portal-board pages match.
- **Kit.** It needs at most 6 dots and 12 links (network 6). K5 needs 10. The 15 pipe cleaners cover the 2–3 six-dot drawing if a child builds it.
- **Figure 3.** Its dot positions equal the printed board positions.
- **Seam marks.** They match Week 41's portal map: a diamond near the top-left, circles near the upper sides, arrows right and up.

## Must fix

None.

## Should fix

1. **Statements about children's behavior read as observations, but nothing has been piloted (pp. 2–6).** The AGENTS rules ask the guide to distinguish observations from hypotheses. The statements are:
   - p. 2: "the outside is the usual miss";
   - p. 3, K–1 P3: "Children usually get down to one crossing and stop";
   - p. 3, K–1 P5: "children often reach two or three first";
   - p. 4, 2–3 P2: "Usual slips: forgetting the outside, …";
   - p. 6, 4–5 P8: "Children often first see 6, 9, 12".

   *Fix:* reword each one as an expectation, for example "Expect many children to stop at one crossing" or "Likely slips: …". The Status paragraph already says that nothing has been tried.

2. **The first-hour routes overrun the group's table time (p. 3).** `context.md` gives about 35–40 minutes of table work and a few minutes of sharing after the run-around and the launch. The guide's routes add up as follows:
   - K–1: 35–45 minutes;
   - Grades 2–3: 20–25 + 10–15 + 10 = 40–50 minutes;
   - Grades 4–5: 35–40 minutes before "then Problem 4 with an adult".

   They also leave no time for the closing comparison the guide asks for.

   *Fix:* budget each route to 35–40 minutes and give the close about 3 minutes. For example:
   - Grades 2–3: Problem 1 in 20 minutes, Problem 2 in 10–15, and the game only if time allows.
   - Grades 4–5: make Problem 4 an "if time" step.
   - K–1: the game at 10 minutes.

3. **Staffing does not match the actual group (p. 2; also p. 3, "pairs can split").** The guide says "One adult can serve the 2–3 and 4–5 tables". The group in `context.md` is different:
   - It has three adults, one anchored at each table: the parent volunteer, who is not a mathematician, at K–1; a second mathematician at 2–3; and the organizer at 4–5.
   - The 4–5 table has three children, a pair plus a rotating referee. So "pairs can split the networks" at 4–5 does not apply.

   *Fix:* write the staffing paragraph for this roster. Say what the 2–3 adult does: check region counts, read the portal rule, and run the game demonstration at that table. Give the third 4–5 child a real role: referee the game ("Is there a pair not joined that still can be?") and check each untangled drawing against its link list. Keep the useful one-adult fallback as a single clause.

4. **The 2–3 split leaves Problem 2 short of data (p. 3).** The guide says "one pair builds networks 1–3, the other 4–6". Each pair then has only two untangled networks in its own boxes (1 and 3, or 4 and 6), and Problem 2's table asks for "each network you untangled". Two rows plus the example are thin evidence for a rule.

   *Fix:* add one sentence. Before Problem 2, the pairs read their dots, links and regions to each other, so that every child's table has all four rows. The other option is to drop the split.

5. **"Problem 6 asks why" is stated for both stuck networks, but 2–3 Problem 6 asks only about network 2 (p. 4).** The Problem 1 note says "At this point 'stuck' is a conjecture; Problem 6 asks why." The Problem 3 note says "That 1 is the best for networks 2 and 5 is Problem 6's question." The 2–3 page 7 reads "Explain why network 2 can never be untangled."

   *Fix:*
   - Problem 1 note: "Problem 6 asks why for network 2; network 5 stays a conjecture in this packet (a ready child can try the ring argument in the 4–5 Problem 5 note)."
   - Problem 3 note: "That 1 is the best for network 2 is Problem 6's question."

## Minor

6. **The bands map omits K3,3 on the portal board for 4–5 (p. 2).** It reads "draw 5, 6 and 7 all-joined dots on the portal board". 4–5 Problem 6 is network 5 (houses and wells) and network 2. *Fix:* "draw networks 5 and 2, then six and seven all-joined dots, on the portal board".

7. **Some references cross bands or point forward (pp. 3, 5).** The K–1 notes cite "Figure 2, middle" and "Figure 2, left", but Figure 2 is on p. 4 in the 2–3 section. 2–3 Problem 6 cites "(Problem 5 of K–1)". The K–1 parent should not have to search another band's section. *Fix:* write "Figure 2, page 4", or add the two one-crossing drawings to the K–1 key row. In the 2–3 note, give the reason directly ("6 = 3·4 − 6, so every region is a triangle").

8. **One hint is a procedure, not a question (p. 4, 2–3 P2).** "Try the smallest networks: one link, then two." *Fix:* "What happens with just one link? With two?"

9. **"network 6 has 12 links, the most possible on 6 dots" (p. 1)** can be misread, since six dots all joined have 15 links. *Fix:* "the most any untangled network on 6 dots can have".

10. **The model paragraph (p. 1)** says the two-link rule "makes crossings countable". The real role of that rule is the K6 lower bound, and the K–1 rules do not include it. *Fix:* "…which the six-dot lower bound needs (see Fewest crossings); K–1 needs no such rule."

11. **The launch shows only an illegal link (p. 2).** It shows what is not allowed: a link across a dot. The pages say "bend the links however you like", and houses-and-wells attempts depend on bending. *Fix:* show one legal bent link next to the illegal one, for example C–D curving round A instead of moving D, as a second legal way to remove the crossing. Keep the launch at 5 minutes. A table demonstration with 5 cm dots also needs children standing round it. Saying so, or using the floor, costs nothing.

12. **The Figure 3 portal drawings are hard for an adult to follow (p. 5).** The boards are 3.9 cm wide with no exit or entry marks; the 7-dot drawing has 12 side crossings. *Fix:* number matching stubs as the page's example does, or print two boards per row at about 6 cm.

13. **The game demonstration (p. 2) is listed under whole-group items, but tables reach the game at different times.** *Fix:* "At each table, when it reaches the game, the table adult…".

14. **Preparation (p. 2).** It assumes 30 hand-cut 5 cm card circles in about 20 minutes, which is the outline's estimate. *Fix:* suggest 5 cm round stickers on card, or a printed sheet of circles, and keep the "not measured" caveat. Also count a demonstration set: five kits are all in use once the tables start.

15. **Brevity (pp. 1, 4–6).** The K5 impossibility argument appears in full three times: in the overview, in 2–3 Problem 6, and in 4–5 Problem 4. The overview's "In children's terms" sentence repeats 4–5 Problem 4 word for word. The 4–5 note already cross-references 2–3 Problem 6, which is good. *Fix:* remove the "In children's terms" sentence from the overview, or the duplicate count from 4–5 Problem 4. This saves about four lines and loses nothing. Otherwise the guide is tight, with no encouragement, padding or page narration. At 6 pages it is within the 5–8 page range of the models.

## What works and should be kept

- **The overview meets the standard.**
  - It states the theorems with their assumptions: Euler's rule with the "one piece" limit and 1 + k for k pieces; E ≤ 3V − 6, and E ≤ 2V − 4 without triangles.
  - It gives proofs an adult can follow, including two formula-free ring proofs and the four-dot proof.
  - It states the limits: counting proves impossibility, never possibility; the prism and network 6 are counterexamples to reading 9 or 12 links as "stuck"; Kuratowski is stated, not proved.
  - It explains why the six-dot bound needs two links per crossing.
  - It covers straight and bent games (3n − 3 − h against 3n − 6, and why the printed boards agree).
  - It gives the torus count, limited to regions that are one patch.
  - It has an explicit experiment, conjecture and explanation paragraph, and a bands map.
- **The launch.** The triangle with a tail is on no page, the three-panel input, step and output figure uses matching labels, the list of what not to do is explicit, and children handle the materials first.
- **Practical judgments.** Letters-only dots (because C changes role between K–1 Problems 2 and 3). "If the adult is choosing moves, go back to a smaller network." "No adult says it is impossible" before houses and wells. Adults may attach links for K5. The fallback for a crowded clip.
- **The game advice.** The question "Is there a pair not joined that still can be?", and rotating who plays first so that the winning seat shows up in the tally.
- **The portal notes.** The word description of network 5's routes, the "shortest routes tie" caveat, and the honest note that the region count on the torus is an extension.
- **Sources.** Honest about what was and was not consulted, including the Dudeney loophole closed by "never lies across a dot".
