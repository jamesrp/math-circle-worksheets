# Review: Untangling networks (planarity), draft v1

Reviewer stage. I looked at every page of all three PDFs: K–1 has 5 pages, grades 2–3 has 6 and grades 4–5 has 7. I rendered them at 80 dpi and zoomed key diagrams to 130–200 dpi. I also rebuilt the draft from a scratch copy of `draft/src/`, and the rebuild was clean with no overfull boxes and identical text. I did not edit the draft.

## Overall verdict

The packet is close to usable. The mathematics is right, the format follows the organizer's standard closely, and the choice of networks is thoughtful. Each band has enough work for the hour.

The main problems are about **sequence and pacing**:

- The K–1 packet reaches the houses-and-wells puzzle only after three pages of untangling.
- Grades 4–5 put the hardest proof early and the concrete portal-board work last.
- Grades 2–3 put an abstract explanation ahead of a concrete drawing task.

There are also several **representation gaps**:

- Grades 2–3 and 4–5 never show the houses-and-wells network before they refer to it.
- The portal example has no labels.
- The portal seam marks differ from the Week 41 board that returning children know.

The review lists no must-fix errors. The "should" items below are ordered by how much they matter.

## What I checked independently (and what holds)

- **Pictures match their link lists.** I parsed every `gen/pic_*.tex` and `gen/list_*.tex` and rebuilt each network from the drawn segment endpoints. All 14 pictures match their printed lists exactly. All are connected and have no repeated link. The nearest gap between a dot and a link it does not belong to is 0.78 cm (network 2), so no link appears to pass through a dot.
- **Network types and crossings**, from my own crossing code and networkx planarity:

  | Network | Type | Crossings in picture | Can it be untangled? |
  |---|---|---|---|
  | K–1 P1 | 4-cycle | 1 | yes |
  | K–1 P1 | K4 minus a link | 1 | yes |
  | K–1 P1 | K4 | 1 | yes |
  | K–1 P2 | 5-cycle | 5 | yes |
  | K–1 P2 | fan | 3 | yes |
  | K–1 P3 | 6-cycle | 5 | yes |
  | K–1 P3 | prism | 4 | yes |
  | K–1 P6 | K5 | 5 | no (best is 1 crossing) |
  | 2–3/4–5 networks 1–6 | fan, K5, K5 minus a link, prism, K3,3, octahedron | 2, 3, 3, 4, 5, 4 | yes, **no**, yes, yes, **no**, yes |

  The contrasting pairs in Problem 1 are well chosen: K5 next to K5 minus one link, K3,3 next to the prism (both 6 dots and 9 links), and the octahedron, which has 12 links (more than K5) and can still be untangled. V − E + F = 2 holds for every network that can be untangled: 5−7+4, 5−9+6, 6−9+5 and 6−12+8.
- **Region example:** a rectangle with one diagonal has 4 dots, 5 links and 3 regions. This is correct.
- **Fewest crossings:** K5 needs 1, K3,3 needs 1 and K6 needs 3. These are correct, and "Explain why nobody can do better" for K6 has the intended answer 15 − 12 = 3.
- **The link game:** a plane drawing that admits no new link is a triangulation, so every finished game has exactly 3n − 6 links. That holds whether or not dots may be moved during play. My random simulation (abstract version) agrees for n = 4 to 7: final counts were always 6, 9, 12 and 15. So the winners are fixed: second player with 4 dots, first player with 5 and second player with 6. The questions "which player wins" and "how can you tell before the game starts" are well posed.
- **Portal boards:** with bent links, any dot positions work on the torus. I also checked independently that the printed K6 and K7 positions allow straight links through the portals with no crossings, using the shortest connection for each pair: 0 crossings for each. The portal example's exit and entry points match: the right and left stubs both sit at height 0.68, and the top and bottom stubs both sit at x = 0.675.
- **Format:** the header and footer are consistent. There are no Name or Date fields, no headings other than the Problem labels, no encouragement, no exclamation marks, no hints and no lettered sub-steps. Problems are numbered consecutively: 1–7 for K–1, 1–6 for 2–3 and 1–8 for 4–5. "Extra board" labels follow the repository's own rule for extra workspace.

## Should fix

### 1. K–1: the main idea arrives too late (pages 1–4, Problems 1–5)
The K–1 band shows seven networks that can all be untangled, across Problems 1–3, before any network that stays stuck. The houses-and-wells puzzle, which carries the outline's K–1 idea ("two houses (possible) and then three"), is Problem 4–5 on page 4. Each network has to be built from pipe cleaners link by link and then drawn. At K–1 speed, Problems 1–3 can easily take the whole 35–40 minutes, so many children would never meet the impossible case.

Problems 2 and 3 also have the same wording ("Make each of these networks and move the dots until there are no crossings. Draw what you made.") and differ only in dot count. The 6-cycle (P3) teaches the same lesson as the 5-cycle star (P2): one loop goes round in a ring.

**Fix:** move the two houses-and-wells problems (now P4 and P5) to come right after Problem 1. Then put the 5- and 6-dot untangles, the K5 problem and the game after them. Consider dropping the 6-cycle and merging the remaining 5- and 6-dot networks (star, fan, prism) into one problem across one or two pages. The packet would still have five pages of work.

### 2. K–1 Problem 5 gives away that it is impossible (page 4)
Problem 4 says "so that there are no crossings". Problem 5 switches to "with as few crossings as you can". When the problems are read aloud one after the other, that change tells the children and the adult that zero cannot be done. The standard says K–1 children "can decide whether something is possible".

**Fix:** pose the possibility question directly and keep an exit. For example: "Join each of these 3 houses to each of the 3 wells. Can you do it with no crossings? Draw what you made."

### 3. K–1 Problem 7 is too long to follow after one hearing (page 5)
It has four sentences and three rules: "Play with a partner. Put 4 dots on the table and take turns adding one link, with no crossings and never two links joining the same two dots. The player who cannot add a link loses. Play again with 5 dots, and mark who wins each game." K–1 problems should be one or two short sentences.

**Fix:** tighten it, for example: "Take turns adding one link to 4 dots, with no crossings and never two links between the same dots. Whoever cannot add a link loses. Then play with 5 dots." The table already shows what to mark, so "mark who wins each game" can go.

### 4. Grades 2–3 and 4–5: houses and wells appear only as a phrase
Network 5 in Problem 1 (pages 1–2) is K3,3, but it is drawn with plain lettered dots A–F. Later problems talk about houses and wells without ever connecting them to network 5:

- grades 2–3, Problem 3: the caption "3 houses, each joined to all 3 wells" under a blank box
- grades 4–5, Problem 5: "Three houses each need a link to each of three wells"
- the portal page in both bands: unlabeled house and well icons

A child has no way to tell that "3 houses and 3 wells" is the network they already found stuck.

**Fix (smallest):** draw network 5 in the shared Problem 1 with house icons for A, B, C and well icons for D, E, F, keeping the letters. Every later mention then points back to a picture the children have built. Also consider putting letters on the K3,3 portal board's houses and wells, as K–1 does, so drawings can be checked and discussed.

The 2–3 Problem 3 captions could also refer to "network 2" and "network 5". If so, keep the descriptive words for the K6 box, since K6 is new.

### 5. Portal example: no labels, and the seam marks don't match Week 41 (2–3 p. 6, 4–5 pp. 6–7)
The example board has three blank circles and four short stubs at the edges. Nothing shows which stub continues which, so a child sees four loose ends. The repository guidance asks that an unfamiliar convention get a small worked visual "with matching labels".

The board is also marked with single chevrons on the top and bottom and double chevrons on the left and right. Their meaning is never stated, and they differ from Week 41's portal map: that map has a diamond at the top and bottom midpoints, a circle at the left and right midpoints, and arrows along the sides. The outline calls this board "Week 41's portal board". Returning children (Week 41 had all three bands) will recognize it only if it looks the same.

**Fix:**
- Letter the three example dots.
- Put a small matching mark (the same number or tick) where each link leaves and where it comes back in.
- Use Week 41's seam marks on every portal board in this packet. Otherwise remove the chevrons, since the sentence already states the rule.

The text "comes back in at the same place on the opposite side" is fine as written.

### 6. Grades 4–5: hardest proof early, concrete portal work last (pages 4–7)
After the shared Problems 1–2 come P3 (game plus "Explain how you can tell which player will win before the game starts"), P4 (explain K5), P5 (explain K3,3) and P6 (K6 plus "Explain why nobody can do better"). That is four written explanations in a row.

P3's explanation is the hardest proof in the packet. It needs two steps: a finished game has only triangular regions, and then V − E + F = 2 with 2E = 3F gives E = 3V − 6. It comes *before* the easier K5 proof that would give the children the tool.

The portal board is part of the outline's 4–5 emphasis ("draw K3,3 on the portal board") and is the most hands-on task. It is P7 on page 6, after the shared Problem 1, which alone takes a long time. A fourth grader who stalls on P3 or P4 never reaches it.

**Fix:**
- Keep the game where it is, but ask only which player wins (as in 2–3), and record it.
- Move "Explain how you can tell which player will win before the game starts" to a later problem, after the K5/K3,3 proofs. With E ≤ 3V − 6 in hand it becomes reachable, and it is a fine final challenge.
- Consider placing the K3,3/K5 portal problem directly after the K3,3 proof (P5), as "the way out", and before the K6 crossing proof.

Optional: add a "links at the end" column to the 2–3 and 4–5 game tables. Every finished game on 5 dots has 9 links while K5 needs 10, which is concrete evidence for the K5 proof. It is light bookkeeping that serves the central idea. Leave it out if it feels directive.

### 7. Grades 2–3: abstract explanation comes before the concrete portal task (pages 5–6)
Problem 5, "Explain why the network with 5 dots ... can never be untangled", comes before Problem 6, drawing on the portal board. The standard puts deeper and more abstract questions last. The outline's 2–3 emphasis does not include a proof, so this belongs at the very end for the quickest child.

**Fix:** swap them, so the portal board is P5 and the explanation is P6. Third graders will mostly explain with drawings, so give the explanation a blank drawing area, or a box above fewer lines, instead of 12 ruled lines alone.

### 8. Region rule: the claim fails for networks in two pieces (2–3 and 4–5, Problem 2, page 3)
The text asks for "a rule connecting the three numbers that works for every untangled network you can draw". The opening definition, "A network is dots joined by links", does not require one piece. A child who draws two separate triangles gets 6 − 6 + 3 = 3, and V − E + F = 2 is no longer true; the general value is 1 plus the number of pieces.

**Fix:** "...that works for every untangled network in one piece." Alternatively, add "in one piece" to the opening definition. The other option is to leave it and let the table adults treat the counterexample as a discovery, but they have no guide this week.

### 9. The link game depends on recognizing the true end (all bands)
The fixed winner shows up only if players stop when no link really fits. In practice, the last links usually have to go round the outside of everything, and K–1 and 2–3 children will often declare the game over too soon. A 30 cm pipe cleaner may also be too short to reach round a spread-out set of 5 cm dots, and the kit's 15 pipe cleaners leave little room to join two together for the 12-link game on 6 dots. If games end early, the winner will look random and the discovery fails.

In 2–3 and 4–5 the page does not say what to play with ("Two players take turns adding one link to a set of dots"), and there is no paper space for playing with pencil.

**Fix on the page:** in 2–3 and 4–5, say what to play with. Pencil on paper removes the length limit; if so, add a blank playing area or point to the back of the page. Dots and pipe cleaners are the other option.

**Fix off the page** (for the facilitator guide and catalog): note that 4 dots always end with all 6 links and 5 dots with 9. Also rehearse the pipe-cleaner game physically; it is untested.

## Could fix

10. **K–1 drawing load (pages 1–5).** Every untangled network, ten in all, must also be drawn, some with 6 lettered dots and 9 links. For kindergartners, copying can take as long as the mathematics. Consider asking K–1 to draw only the key results: the 4-dot K4, both houses-and-wells problems and the best K5. Leave the other built networks undrawn, or give them smaller boxes. This also helps pacing (item 1).
11. **Pacing of the shared Problem 1 (2–3 and 4–5, pages 1–2).** Building six networks link by link, up to 12 links each, can fill most of the hour before Problem 2's rule-finding. For 4–5 especially, "Make or draw each network" would let quick children untangle on paper once they have the idea. Splitting the six networks between the two pairs and pooling the results is a facilitator option.
12. **Answer place for "Which networks stay stuck?"** (shared P1). An empty box can mean "stuck" or "not tried yet". A few words such as "Write *stuck* in its box" would make the record readable for Problem 2's table. This is optional.
13. **Continuation page** (2–3 and 4–5, page 2). Networks 4–6 start the page with no label. The organizer has accepted continuation labels before ("Problem 1, continued").
14. **K7 board size** (4–5, page 7). K7 has 21 links, and 11 of them go through a portal, all on a 7.6 cm board. The page has about 5 cm unused at the bottom, so give K7 a larger board or a page of its own. Separately, on the K6 and K7 boards the dots B, C, D and E lie exactly on one straight line, (1/14, 11/14) stepping by (4/14, −2/14). A straight B–D or B–E inside the board would run through a dot. Bending is allowed, so this is legal but may surprise children. Keep the positions unless they are changed and re-checked; they are what makes the straight-link solution work.
15. **Box alignment** (K–1 pp. 2–3; 2–3 and 4–5 p. 2). The two or three answer boxes on each of these pages have different widths and left edges, because the link-list column changes width. Fix the column width per page so the boxes line up.
16. **Packet IDs.** The year-2 pattern is `F##-K-v#`, `F##-23-v#` and `F##-45-v#` (for example F41-23-v3). The draft uses `NN-K-v1`, `NN-23-v1` and `NN-45-v1`. Use `FNN-K-v1` and so on until the week number is assigned.
17. **Explanation space in 4–5** (P4: 6 lines; P3: 5 lines). This is fine for the organizer's table but tight if a child explains with a drawing. A small blank area would help.

## Band-by-band notes for the reviser (things to keep)

- **K–1:** the 4-dot entry networks (one crossing each) give everyone an immediate success. The K5 "as few crossings as you can" with the pentagon-and-star picture is a real K–1 problem. In the game, 4 dots always ending with every pair joined, and 5 dots always ending one link short, connect to K5. Keep the large pictures and the link lists.
- **Grades 2–3:** the six-network sort, the region example with numbered regions, the open "find a rule" and the K5/K3,3/K6 fewest-crossings page are all strong. Keep the K6 box large.
- **Grades 4–5:** P4 → P5 → P6 (K5, then K3,3 with no triangles, then a lower bound for K6) is a good proof progression once item 6 is fixed. The portal page for K6 and K7, with the same letters plus G, is a good final extension.
