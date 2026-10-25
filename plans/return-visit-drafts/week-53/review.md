# Week 53 return visit, draft v1: critic review

## What I checked

- I rendered all 20 pages (K–1 6, grades 2–3 5, grades 4–5 9) at 90 dpi and cropped the maps at 150–200 dpi.
- I read `PROMPT.md` and all of `draft/src/`. I reran `verify.py`, and every assertion passes.
- I rebuilt the packets from `src/` in a scratch folder. The `.tex` files, the extracted text and the page counts match the draft, and pdflatex reports no overfull boxes.
- I wrote my own checks for two things `verify.py` does not test:
  - how far each price label is from its own link and from the nearest other link;
  - whether the 4–5 "any map" questions still hold when places in squares are allowed.

## Verdict

This is a strong draft:

- The register is right: no titles, encouragement, hints, Name/Date fields or dash asides.
- Each new convention has a start / step / result example: buying, opening links by price, trips, places in squares.
- Changed prices are printed on separate copies of the same layout.
- K–1 prices are shown as a numeral plus dots.
- Every numerical answer checks out (listed at the end).

Three problems should be fixed before the organizer sees the packet:

1. In 4–5, several general questions have the wrong intended answer under the packet's own definition of a network. The packet's own maps are counterexamples.
2. On the star maps and the six-place map, some price labels sit nearer a neighbouring link than their own. The brief singles out exactly this kind of misplaced label.
3. Children record only what a network costs, not which links it uses. So the kernel-2 observation ("the network stayed the same") is never captured.

---

## Must fix

### 1. Grades 4–5: the "any map" questions fail once places in squares are allowed (P2, P3, P4 Lee, P6)

The shared rules on 4–5 page 1 say "A network may pass through places in squares or leave them out." They apply to the whole packet. Four questions then generalize to "any map" or "one map" without excluding squares, and each intended answer holds only when every place is circled.

- **P2** asks: "Now take any two places on any map. Is the route between them along a cheapest network always a route whose most expensive link is as cheap as possible?" (intended answer: yes)
  - The packet's own **P8 right-hand map** (star with SA = SB = 2, SC = 4) is a counterexample. AB, BC is a cheapest way (8), and its A–B route has most expensive link 4. The route ASB has most expensive link 2.
  - The underlying reason: with two circled places, a cheapest network is a cheapest trip, and that minimizes the sum of prices, not the largest price.
- **P3** asks: "Can two cheapest networks of one map use different prices?" (intended answer: no)
  - The same P8 map has cheapest ways AB, BC (prices 4, 4) and AS, BS, CS (prices 2, 2, 4). They use different prices and even different numbers of links.
  - The group-count cost formula also fails there.
- **P4 Lee** says a loop-free network meeting the lowest-dearest-route condition "for every two places" must be cheapest (intended answer: Lee is right).
  - The **P8 left-hand map** (S-links 3, sides 4) is a counterexample. SA, SB, SC has no loop and meets the condition for every pair of places, S included. It costs 9, and the cheapest costs 8.
- **P6** asks: "Which ways of changing every price can change the cheapest networks of a map?" (intended answer: adding a constant cannot)
  - On the **P7 star map**, adding 2 to every price changes the set of cheapest networks: AS, BS, CS ties at 12 with the three pairs of triangle links. Adding 3 makes only the triangle pairs cheapest (14 against 15).
  - The reason: with squares, networks can have different numbers of links, so they behave like trips.

All of these were confirmed by enumeration (scratch scripts /tmp/claude-0/-home-claude/d1d23a10-bfbf-5b59-a13a-5f6afdbf2b0f/scratchpad/critsrc/crit_checks.py and /tmp/claude-0/-home-claude/d1d23a10-bfbf-5b59-a13a-5f6afdbf2b0f/scratchpad/critsrc/crit_checks2.py).

A quick child who gets to P8 and looks back will find the packet contradicting itself. The organizer would have to rescope four problems by hand.

**Fix.** Keep the square rule in the shared rules, as the brief requires. Scope each general question to maps on which every place is circled. For example:
- P2: "…take any two places on any map where every place is circled…"
- Apply the same scoping to P3, to Lee's statement and to P6's question about networks.

The way the theorems fail with squares is good extension material for the facilitator guide ("Does this still hold when some places are squares?"). It should not appear on the page as the intended answer.

### 2. Price labels nearer the wrong link (every band)

The brief asks that each price label sit on its own link, clear of other links, and it notes that the base week's first print misplaced two labels on the six-place map. The build's clearance check only requires about 2.6 mm from other links. It never checks that a label is nearer its own link. I measured each label's edge distance to its own link and to the nearest other link (working size):

| Map (where used) | Label | Own link | Nearest other link |
|---|---|---|---|
| Star, S-links 3 (K–1 P5 left) | BS "3" | 3.5 mm | **AB 2.5 mm** |
| Star, S-links 3 (K–1 P5 left) | AS "3" | 3.5 mm | **AC 2.6 mm** |
| Star (K–1 P4, P7 boxes; 4–5 P7) | CS "2" | 3.5 mm | **BC 2.7–3.0 mm** |
| Star (K–1 P4, P7 boxes; 4–5 P7) | AS "2", BS "2" | 3.5 mm | AC / AB 3.0–3.3 mm |
| Star 2-2-4 (K–1 P5 right; 4–5 P8 right) | AS, BS | 3.5 mm | AC / AB 2.8–3.0 mm |
| Six-place map, all copies (2–3 P5 ×3; 4–5 P6 ×4) | EF | 3.5 mm | **DE 2.6 mm** |
| K–1 map (K–1 P2, P3) | CD "3 dots" | 3.5 mm | **BC 2.9 mm** |
| New six-place map (2–3 P1–P3; 4–5 P1–P3) | EF "1" | 3.5 mm | DE 4.0 mm |
| Diamond (K–1 P5 bottom) | X-links "2" | 3.5 mm | sides 4.0–4.6 mm |

These labels matter most on K–1 P5's left map:
- If BS's "3" is read as belonging to AB, AB looks like it has two prices (the "4" outside and the "3" inside).
- The square's links are the whole point of that map.

On the six-place map, EF's "2" (printed copy) shares triangle DEF with DE's "1". Visually it sits about equally near both links.

There is also a physical problem. A 5 mm marker strip centred on a link reaches 2.5 mm to each side, so these labels touch it or come within about 0.5 mm. A marker laid slightly off-centre on BC, DE or AB will cover a neighbouring link's price. This has not been rehearsed.

**Fix.**
- Make every working-map label clearly nearer its own link. A workable rule is own link at about 3.5 mm, every other link at least about 6 mm.
- On the star and diamond maps, move each square-link label toward the square end of its link (about t = 0.3 from S or X). The triangle sides are far away there.
- On the grid maps, slide EF's label toward F, or put it outside the map to the right. Slide CD's label toward D. Near the far end of a vertical link, the diagonal is far from it.
  - If 4–5 P6 then becomes too wide, use a unit of about 38 mm or widen the 5 mm gap between maps.
- Apply the same placement to the blank answer boxes on K–1 P7 (BS's box is 2.6 mm from AB) and to the record copies.

### 3. Record which links the network uses, not only its cost (2–3 P4, P5; 4–5 P5, P6)

Kernel 2's claim is that the same network stays cheapest while the cheapest trip changes. But the record lines read "Network costs ___" (2–3 P4, 4–5 P5, 4–5 P6) and "Cheapest network costs ___" (2–3 P5). Those costs change from map to map (3 / 6 / 9; 8 / 18 / 16 / 14), so a child's record suggests that both the network and the trip changed. Meanwhile:
- 2–3 P7 asks whether adding to every price can change which networks are cheapest;
- 4–5 P6 asks which changes can change the cheapest networks.

Both depend on having noticed that the links stayed the same, and that observation lives only in markers that have since been lifted off.

**Fix.** Make the network line parallel to the trip line, for example "Network ______ costs ___", recorded as link names (AB BC CD). That gives a single, easy-to-check record (AGENTS.md: "prefer one recoverable record").

---

## Should fix

### 4. The opening-by-price problems start by telling children to act on the example (K–1 P2, 2–3 P3, 4–5 P3)

Each starts with an instruction ("Lay a marker on every link with 1 dot … Then add markers on the 2-dot links and ring the groups again"). The only map nearby is the small worked example, which already shows it done. The real task follows separately ("Do the same on this map…").

A child following the text acts on the example first, or does not know which map the first instruction means. The example should support a single instruction aimed at the real map.

K–1 P2 is also four sentences long, and the standard limits a K–1 problem to one or two short sentences that make sense after one hearing. A possible shape: "On this map, open the 1-dot links, then the 2-dot, 3-dot and 4-dot links, as in the pictures, and ring the groups each time. When can the pawn first walk from A to F?"

### 5. Grades 4–5 ordering: hard explanations come before the concrete work

- **P2** puts the main kernel-1 proof ("any map") on page 2, before the group-opening picture in P3 that makes the explanation reachable.
- **P4** prints the converse (Lee) mid-packet. The brief lists the converse as an extension, and Lee's statement is the hardest sentence in the packet to read.
- A trio stuck on either one never reaches trips (P5–P6) or squares (P7–P9), although the brief names the trip and stuck-purchase explanations as core.
- **P7** (explain why the star purchase is stuck) comes before **P8**, the plain "does the square help?" cases. The standard says children should meet an idea in concrete cases before explaining it.

**Fix.**
- Move the "any map" generalization after P3, or fold it into P3's explanation questions.
- Move Lee to the last page, or leave it to the facilitator.
- Put P8's maps before the stuck-purchase problem, and move the square convention example with them.

### 6. K–1 P7 wording

P4 and P5 say "once without the square and once using it". P7 says "costs the same **with** the square as without it". Heard as "when you may use the square", any prices at which the square does not help (for example 4, 4, 4) satisfy the task, and the intended reverse problem disappears. That problem is: S-link prices with the cheapest network through S costing exactly 8, such as 2, 2, 4; 1, 3, 4; or 2, 3, 3.

Use "using the square", matching P4 and P5.

### 7. Grades 4–5 P2 and P3 send children back to page 1

Both say "on the map of Problem 1". Children laying markers and drawing rings need the working map in front of them while they record on pages 2 and 3. The 2–3 packet already repeats the working map for P3.

There is room to do the same in 4–5: about 60% of page 2 and the lower third of page 3 are blank.

### 8. Counters for comparing two totals side by side

The brief adds a scrap-paper second payment area so that two totals can lie side by side. On the six-place map, the network and trip totals together exceed the kit's 30 counters:
- 18 + 15 = 33 after adding 2;
- 16 + 16 = 32 when doubled.

This affects 2–3 P5 and 4–5 P6. Each single payment is within the limit, but the side-by-side comparison the materials are designed for runs out of counters.

Either the facilitator note says to write the first total before paying the second, or the kit needs more counters. Flag this to the organizer; it is unrehearsed.

### 9. Grades 4–5 kernel 1 rests on a single map

The price-list and group-count conjectures in P3, and the lowest-dearest-route claim in P2, are all drawn from the one new six-place map. AGENTS.md asks for several purposeful, contrasting examples before generalizing, and the brief offers familiar maps for this:
- the five-place tie map: three cheapest networks of different shapes, all 1, 1, 2, 2;
- the trap map: group counts 4, 3, 2, 2, 1, so cost 7.

A second map in P3 would let the "same price list" observation come from more than one case.

---

## Smaller points

- **Vocabulary drift in 4–5.** The packet uses "network" in P1–P6, "purchase" in P7 and "way to join" in P8–P9. "Purchase" is the base week's word, but this packet defined "network" and should keep using it (it is defined to cover squares).
- **Stopping point for the opening-by-price problems** (2–3 P3, 4–5 P3). The text says to continue "until there is one group", which happens at price 4, but a fifth record copy, "priced up to 5", is printed. The example caption says "Links priced 1 or 2" while the record copies say "priced up to 2"; pick one wording.
- **4–5 P3, "use different prices".** This can be read as "contain a link with a different price". "Have different lists of prices" (or equivalent) is unambiguous.
- **Header.** "Networks return visit" describes the session rather than naming a topic. Other return-visit packets use the topic alone (for example "Week 7 / Take-away games / Grades 2–5"). The base week's topic is "Connecting networks". The packet ids (W53R-…) differ from the F07-RV-v1 pattern, which is the organizer's choice.
- **Short problems.** 2–3 P2 (three pairs), 4–5 P1 (four pairs) and 4–5 P5 (three square maps whose trips are obvious to 4–5) will likely take under five minutes. For 4–5, P5's maps could join P6. For 2–3 P2 and 4–5 P1, a contrasting pair would help, such as one whose direct link is cheaper than its lowest-dearest route's top price.
- **Two layouts in 4–5.** The new six-place map (P1–P3) and the base week's six-place map (P6, P8) use the identical A C E / B D F layout with different prices. A child told "the map of Problem 1" can read prices from the wrong one.
  - The base week drew its six-place map as a bowtie, so returning children will not recognize it either.
  - Consider distinct layouts, or keep the base week's layout for the familiar map.
- **Drawn length.** On the 2-2-2 star (K–1 P4, P7; 4–5 P7) and the diamond, the cheap links are exactly the short ones, so "use the short links" works without reading prices. P5's other two stars break this pattern. Varying the geometry on one of the main maps would help.
- **2–3 P5.** Two answer lines for "every cheapest trip" match the count on the printed and doubled maps, which mildly signals the answer.
- **4–5 P8.** There are no record copies for the six cheapest ways on the right-hand star. Link names on blank space will work, but small record copies would be easier to check.
- **Map captions.**
  - "Prices as printed" is odd when every copy is printed; "Original prices" is clearer.
  - "Every price squared" may be an unfamiliar word for some fourth graders. The prices are printed, so the word is not needed to do the task.
- **Grades 2–3 length.** Seven problems for about 40 minutes, with nothing on squares, so a quick third grader could run out. A star-map problem at the end would give overflow without disturbing the emphasis.

---

## Checked and correct

All of these were confirmed by `verify.py` or my scripts. Answers are per problem.

**K–1**
- P1: 4 counters, three networks (AB BC CD; AB AC CD; AC BC CD).
- P2: the groups go {A,B}{C}{D}{E,F}, then {A,B,C}{D,E,F}, then one group. A to F first joins when the 3-dot links open.
- P3: 9 counters, two networks. No network avoids every 3- and 4-dot link.
- P4: 8 without the square, 6 using it (SA SB SC).
- P5: 8 / 9 (the square costs more); 8 / 8 (a tie, with six cheapest overall); 12 / 8 (the square saves 4).
- P6: 6 (AS BS ST TC TD). It is 10 with no squares and 9 with one square.
- P7: S-link prices x ≤ y ≤ z with min(x+y+z, x+y+4) = 8 (for example 2, 2, 4; 1, 3, 4; 2, 3, 3).
- Prices are at most 4, totals at most 12, and every price is a numeral with matching dots.

**Grades 2–3**
- P1: cost 9, six cheapest networks (eight record copies, so the count is not given away).
- P2: B–D 2 (BCD), D–F 4, A–F 4.
- P3: group counts 6, 3, 2, 2, 1. B and D first share a ring at price 2, D and F at 4, A and F at 4. These match P2.
- P4 (A–D):
  - as printed: network 3, trip ABCD 3;
  - +1: network 6, trip AD 5;
  - +2: network 9, trip AD 6.
- P5 (A–F):
  - as printed: network 8, trips ABCDEF and ACDEF at 8;
  - +2: network 18, trip ACDF at 15 only;
  - doubled: network 16, trips ABCDEF and ACDEF at 16.
- P6: with whole numbers, AB + BC = AC − 1.
- P7: no, and no.

**Grades 4–5**
- P1: A–D 2, B–D 2, D–F 4, A–F 4.
- P2: six cheapest networks. Yes on maps with every place circled.
- P3: group counts 6, 3, 2, 2, 1, so the cost is 5 + 2 + 1 + 1 = 9. All six networks have prices 1, 1, 1, 2, 4.
- P4: Sam is wrong (BC CD DA costs 9 against 7). Lee is right on maps with every place circled.
- P5: same answers as 2–3 P4.
- P6: network AB BC CD DE EF on all four maps (8, 18, 16, 14). Trips:
  - as printed: ABCDEF and ACDEF at 8;
  - +2: ACDF at 15;
  - doubled: ABCDEF and ACDEF at 16;
  - squared: ABCDEF at 14.
- P7: cheapest is 6 (SA SB SC). The answer is no: from any two triangle links, every legal change costs at least 10 or gives another 8. With a cap of 8 or of 9, only three purchases are reachable; a cap of 10 reaches 6.
- P8: S-links 3: 8, three ways, S unused. 2-2-4 star: 8, six ways. A and F only: 8, the two cheapest A–F trips.
- P9: 6, a single way. A square never has just one bought link. At most 2 squares have three or more links, and this map has exactly 2.

**Format and brief compliance**
- Headers and footers are consistent, with page numbers. Problems are numbered consecutively in each band.
- Scans found no exclamation marks, em dashes, banned phrases or Name/Date fields.
- Squares are defined once in the shared rules (K–1 and 4–5).
- Each working map has at most 9 links, 10 mm place circles and about 40 mm or more between centres. The smallest is the diamond's centre to corner, at 39.6 mm.
- The largest single payment is 18 counters, and no links cross.
- Each convention example comes before the convention's first use.
- Opening by price is never presented as a method for finding a cheapest network.
- The Week 100 inequality stays off the page.

## Not established

- Physical fit and classroom use are untested, as they are for the base week: whether markers clear the labels (see item 2), whether 30 counters cover side-by-side totals (item 8), and how K–1 children manage drawing group rings on the small record copies.
