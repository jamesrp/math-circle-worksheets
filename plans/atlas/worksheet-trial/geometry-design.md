# Geometry worksheet trial — design and complete key

Fixed random sample: GA-26, GA-29, GA-25. Four student pages per family. Final printable wording and physical layout are in `lowell-math-circle-year-2/source/atlas-random-ten/geometry.py`; this file preserves the expanded design and complete key. Larger-grid25.15and invented-budget29.11are facilitator back-pocket prompts.

`geometry-data.json` contains verified diagram specifications, expanded prompts, solutions, sources and candid quality assessments. `geometry-checks.py` checks all4096grid subsets,192trees, the minimum4swaproute, braid geometry/coloring, all162valid signed typeIII color assignments, both18typeII assignments, and exact Cantor stages.

Independent review repaired the all-variant knot proof scope, sourceURLspacing, and the copy-your-maze templates. Student copy templates use faint dashed guides with bold kept roads; water crosses only missing-road openings. SourceURLsare exempt from prose cleanup.

## Teaching basis

Re-read *Math Circle by the Bay*, preface printedviii–x/PDF9–11, directly from the local collection: manipulatives, varied pace and recurring explanation. These lessons are independently designed; source teaching advice is not evidence of a classroom pilot. Also inspected the current Week1middle/upper worksheets and redesign notes.

## GA-26 — Can three colors catch a knot?

Promising and substantial, with a real visual-prerequisite risk.

Nearly identical diagrams behave differently; learners invent/check a coloring, a finite count becomes an obstruction, and local moves link hands-on string to a general certificate.

**Risk:** Over/under tracing and coloring an arc rather than each visible stroke are genuinely hard. Page 1 must succeed before continuing. Pages 3–4 may be a second meeting. Do not promise that a seven-year-old’s rainbow picture alone proves the trefoil is knotted.

**Satisfying stop:** Solve A’s coloring and prove B cannot have a nonconstant one by forced propagation. Full knot non-equivalence is a later stop after local checks plus the supplied theorem.

**Boundary:** Coloring is not a complete knot test. No classroom pilot yet.

### Prerequisites and preparation

- **entry:** Track a continuous line through over/under crossings; use three distinct symbols or colors. No arithmetic required.
- **core_explanation:** Apply a local same-or-all-different rule and organize cases; distinguish “cannot find” from an impossibility reason. Spatial tracing is a real prerequisite.
- **extension:** Use five color-equality patterns to check a local move and reason about reversible one-to-one correspondences. The general Reidemeister theorem is an explicitly supplied fact, not proved by coloring.

Materials: three pencils or labels R/B/G; one loose overhand knot with its ends taped together and one plain closed loop of cord per pair, optional but recommended; paper diagrams large enough to trace; a spare open cord for making local moves. Preparation about 15 minutes.

0–10 play with closed cords and trace crossings; 10–15 state coloring rule; 15–35 investigate A and B; 35–40 whole-body over/under trace; 40–55 choose two-move checks OR three-strand extension; 55–60 state exactly what was proved. The complete local-invariance proof may require a second session.

New knot object and invariant. Week 2 has invariants, but no crossing/arc convention or topology. The atlas’s assumed standard trefoil has been replaced by explicit, independently verified geometry.

### Student page 1: Almost the same drawing. The same knot?

Keep the coloring rule and solution off this first page. Page 1 shows two copies of A: a comparison copy and a tracing copy.

**26.1** Each picture is ONE closed cord. At a crossing the solid bridge goes over; the gap goes under. Follow the whole cord in A, then B. What changed?

Expanded layout proposal: A and B large, side by side, with visible gaps and no colors.

**26.2** You may bend, stretch or slide the cord. You may not open an end or pass one strand through another. Which drawing can become a plain circle? Make a prediction. Try the closed cords if you have them.

Expanded layout proposal: 0.9 in prediction/evidence box.

**26.3** For a new way to track A: begin at the marked dot. Follow the cord until it goes UNDER. Start a new section just after that underpass. Keep the same section when you go OVER. How many sections return you to the starting section?

Expanded layout proposal: Second Aat 2.6 in width; mark sections with small labels or pencil traces.

### Student page 2: One color or three. Never exactly two.

The failure in Bmust come from a forced contradiction, not a collection of unsuccessful attempts.

**26.4** Color every section between underpasses. At each crossing, inspect the overpass and the two underpass ends. Their colors must be ALL THE SAME or ALL DIFFERENT. The overpass keeps its color. Use R, B, Gletters if you prefer.

Expanded layout proposal: Three small crossing examples: valid RRR, valid RBG, invalid RRB.

**26.5** Can you color A with more than one color? Can you do the same for B? Follow every section, including the joins around the outside.

Expanded layout proposal: One large uncolored A and one B; do not prelabel A’s arcs with color names.

**26.6** If you get stuck on B, try two different colors at its top ends and follow the forced colors down. What happens when they must join around the outside?

Expanded layout proposal: 0.75 in evidence box; hint after a genuine attempt.

**26.7** How many legal colorings does each FIXED drawing have? Color names matter:RBG and BRG count differently. Include the all-one-color choices. Find a counting method that cannot miss a coloring.

Expanded layout proposal: Table A/B/plaincircle with total and more-than-one-color columns.

### Student page 3: Can the colors survive a real move?

Two local checks are worthwhile but are not yet a proof for all possible knot deformations.

**26.8** Curl or uncurl. Start with red at the left end. Complete the coloring of the curl. What color reaches the right end? Could any other completion work?

Expanded layout proposal: Large R1 before/after diagram and 0.65 in response.

**26.9** Slide two crossings away. Start red on the left and blue on the right. Fill every section before the move. Compare the bottom colors with the two straight strands. Then try equal starting colors.

Expanded layout proposal: R2 before/after; a two-row input/output table.

**26.10** Why do those two trials cover EVERY choice of starting colors, if colors may be renamed? Is the completion unique?

Expanded layout proposal: 0.8 in explanation box.

**26.11** Return to B. Can its first two crossings slide away? What remains? Why is switching a single overpass to an underpass different from sliding these two crossings away?

Expanded layout proposal: 0.9 in sketch/reason box.

### Student page 4: The last move, and a certificate

Optional proof page. Checking the local rules does not prove the supplied theorem about all deformations.

Gate: Organized cases and reversible correspondences.

**26.12** Slide a strand past a crossing. Start with the SAME three top colors in both pictures. Complete both diagrams. Compare the bottom colors, left to right.

Expanded layout proposal: R3 pair large; five-row table inputs RRR, RRB, RBR, BRR, RBG; blank left/right outputs.

**26.13** Why do these five rows cover every possible pattern of three starting colors, after renaming colors? Is every completion forced?

Expanded layout proposal: 0.8 in explanation box.

**26.14** FACTS TO USE: every deformation of a closed cord without cutting or passing through itself can be represented by these three kinds of local move and ordinary redrawing. Every version of a local move pairs each coloring before with exactly one afterward; our checks illustrate this fact. Explain why a drawing with 9 colorings cannot become a circle with 3.

Expanded layout proposal: 0.95 in proof box.

**26.15** Does our argument prove that matching coloring counts mean two drawings represent the same knot? Explain what this argument leaves unresolved.

Expanded layout proposal: 0.55 in final boundary box.

### Delayed hints

- 26.5: Try different colors on the two top strands, then each crossing forces the next color.
- 26.7: There are three choices for the left top color and three for the right. Which choices close consistently?
- 26.9: The same strand passes over at both crossings. Track it all the way.
- 26.13: Three colors can be all equal, all different, or have just one unequal position.

### Complete solutions


**26.1** Only the MIDDLE crossing changes which strand is on top. Both diagrams have the same planar shadow and exactly 3 crossings. Following either diagram traverses both braid strands and both outer closures before returning, so each has one component. A is the closure of σ₁³, a trefoil; B is the closure of σ₁σ₁⁻¹σ₁.

**26.2** A cannot become a circle; the later coloring certificate proves it. B can: cancel its first two opposite crossings by a type II move, leaving a one-crossing closed braid, then remove its curl by type I. Physical difficulty or matching coloring counts alone would not prove this.

**26.3** A has 3 arcs/sections between successive underpasses. Each arc can contain an overpass. Starting at the left closure, its top-left portion is arc A; top-right portion arc B; the left strand just below first crossing arc C. Because the marked dot may lie inside a section, returning to that section is not a fourth arc.

**26.4** Given overcolor and one undercolor, the other undercolor is uniquely forced: same if they agree, otherwise the third color. Thus valid examples are RRR and RBG; RRB is invalid. The gap is an underpass of a single cord, not a cut end; color is permitted to change there because diagram arcs terminate at undercrossings.

**26.5** A: start top colors R, B. From top to bottom the color pairs are(R, B),(G, R),(B, G),(R, B). Both outer joins agree, and every crossing contains all 3 colors. B with the same start gives(R, B),(G, R),(R, B),(G, R), which fails the outer joins. Any two different top colors behave by renaming in the same way; equal colors stay equal. Hence B has no nonconstant coloring.

**26.6** For Bthe bottom pair differs from the top pair when the two top colors are different. Since each bottom endpoint joins the SAME-side top endpoint, the drawing cannot be colored consistently. The local rule forces every intermediate color; there is no alternative hidden choice.

**26.7** A has 9 total colorings: 3 equal top pairs give constant colorings, and 6 unequal ordered top pairs give nonconstant ones. B has 3 total, all constant. A plain circle has one arc and therefore 3 constant colorings. Global fixed drawing/colors are counted; color permutations are distinct here. On later move-check pages, renaming is only a way to reduce proof cases.

**26.8** The curl must remain entirely red. Its overpass and the entering undersection are already the same color, so the outgoing undersection is forced red. This proves a unique extension for any single starting color; reversing the move forgets no choice.

**26.9** For input(R, B), the pair between crossings is(G, R) and after both crossings returns to(R, B). For(R, R), every section is R. The corresponding straight strands keep their input colors. Both operations are uniquely reversible. Do not accidentally draw two crossings of the SAME sign; those are not removable by this move.

**26.10** A pair of colors is either equal or different. Any equal pair is a renaming of RR and any unequal ordered pair is a renaming of RB. The rule depends only on equality/difference, so those two trials cover all 9 assignments. Each crossing uniquely determines the new undercolor.

**26.11** Yes: B’s first two crossings are positive then negative, with the same physical strand passing over both; they cancel. The remaining one-crossing closure is a curl of the unknot. Changing one crossing would require a strand to pass through another and is not one of the legal deformations.

**26.12** Both diagrams send the following top colors to the same bottom colors, left to right: RRR→RRR; RRB→BRR; RBR→BGR; RBG→RGR; BRR→GGB. Exact 27-case check confirms all. These are ENDPOINT colors, not three arc names. The intermediate colors may differ between drawings; the endpoint correspondence is identical.

**26.13** The patterns are: all same; left=middle only; left=right only; middle=right only; all different. Every triple belongs to exactly one type. Color renaming transfers the checked example to every member of its type. Uniqueness follows crossing-by-crossing; reverse moves recover the original.

**26.14** Each local move gives a bijection between the entire diagrams’ legal colorings because outside colors stay fixed and inside completion is unique in both directions. Therefore a finite sequence preserves the number. Ordinary redrawing also preserves it. The supplied Reidemeister theorem turns any possible unknotting into such a sequence. A has 9 but the circle has 3, impossible. The theorem is necessary; checking a handful of moves without it would not cover arbitrary 3 Ddeformations. The five student cases cover the displayed type III representative. The complete facilitator variant check covers every consistent strand-height order; it must be supplied if the children have not proved those variants. See invariance_variants and the 162-case exact check.

**26.15** No. Equal invariant values do not establish equivalence; an invariant may fail to distinguish different knots. For B we additionally gave an explicit sequence to a circle. Do not offer an unsourced nontrivial zero-test knot as if checked in this packet.

### All local-move variants

The displayed braid slide is one representative. A complete local check must include all allowed height orders, not just three positive crossings. For signs (a, b, c), compare braid words (σ₁^a, σ₂^b, σ₁^c) with (σ₂^c, σ₁^b, σ₂^a). Six sign triples are legal; exclude (+, −, +) and (−, +, −), which would require a cyclic above/below order of the three strands. The exact script verifies all 6×27=162 color assignments. It also checks both orders of opposite-sign type II crossings (18 assignments), and type I forces one color. Turning a strand around does not change the rule: the two undercolors are symmetric. The operation a*b = 2b − a modulo 3 is idempotent, involutory and self-distributive, giving the same argument for all unoriented local variants. These extra checks belong to the facilitator; students may use their invariance conclusion as a supplied fact after investigating the pictured examples.

### Sources


- [Louis H. Kauffman, Knots](https://homepages.math.uic.edu/~kauffman/Tots/Knots), §II and §III; “Three Coloring a Knot,” Figures 12–14. Local Fox coloring rule, Reidemeister-move invariance and the theorem bridge. Exact braid drawings and finite tables independently checked.

- [Jonny Evans, 6.03 Braids: the Wirtinger presentation](https://www.jde27.uk/tg/braids03.html), example identifying closure of σ₁³ as the trefoil. Confirms the explicit closed-braid diagram chosen here is a trefoil, rather than relying on a familiar icon.

## GA-29 — More pieces. Less path.

Good finite worksheet; the ambitious title of the original atlas card needs an honest advanced gate.

Addressing adds a second representation and completeness argument; endpoint traps and simultaneous count/length optimization give finite discoveries beyond repeatedly shading thirds.

**Risk:** The full uncountability result is not a satisfying low-prerequisite endpoint for every learner. The finite first 3 pages are the core. Infinite page 4 is optional and likely another meeting; do not equate enjoying the picture with proving the theorem.

**Satisfying stop:** Explain all 16 addresses and solve the round 6 double challenge, while identifying permanently safe endpoints.

**Boundary:** No finite diagram exhibits zero retained length; every finite stage has positive length. No classroom pilot yet.

### Prerequisites and preparation

- **entry:** Locate labeled whole numbers and split a segment into three equal parts; count and double.
- **core_explanation:** Fractions with denominators 3 and 9 for budget page; follow finite L/R addresses; distinguish endpoints from interiors.
- **extension:** Infinite sequences, a nested-interval existence fact and “for every proposed list” reasoning. No calculus, but genuine proof maturity. Do not describe the infinite page as elementary merely because the arithmetic is small.

Materials: paper number-line strips; pencils in two colors; ruler optional; address slips L/R; scissors optional only for separate play strips; use shading on proof sheets to preserve endpoints. Preparation about 8 minutes.

0–8 fold/play with thirds; 8–13 state remove-open-middle rule; 13–30 finite cutting and addresses; 30–35 movement: walk L/R branches; 35–50 choose budget or infinity extension; 50–60 explain one certificate. Page 4 often deserves a later meeting.

No documented matching worksheet. Binary branching resembles several earlier tree representations, but here the addresses code nested intervals rather than queries or moves. GA-03 has a related countable zero-length example; this extension tests the false converse.

### Student page 1: Which places escape the eraser?

Do not hand out the completed stage picture yet.

**29.1** Start with the whole path from 0 to 81. In each round, erase the middle third of EVERY piece that remains. Keep the two boundary dots of each erased gap. Do two rounds on the blank copies.

Expanded layout proposal: Three 6.3 in number lines labeled start/round 1/round 2; blank cut annotations.

**29.2** Predict: which of these places will ever be erased? 9, 15, 18, 27, 40, 54. Mark a safe place with a dot. If a place is erased, write its first round.

Expanded layout proposal: Six-row table: place / safe or round / reason.

**29.3** Choose a surviving piece and do one more round inside it. Find a place that survives two rounds but is erased in the third.

Expanded layout proposal: Zoom drawing box 1.0 in.

### Student page 2: Give every piece an address

A completed stage 4 strip is a supplied search space, not a proof of completeness.

**29.4** At every split, call the left piece L and the right piece R. Start from the whole 0-to 81 path. Four letters name a piece after four rounds. Find LLRR and RLRL. Write each piece’s two endpoints.

Expanded layout proposal: Stage 4 strip plus two address/endpoints lines.

**29.5** The piece from 20 to 21 is still there. Find its four-letter address. Then choose another piece and make an address puzzle for a partner.

Expanded layout proposal: Two blank address/endpoint pairs.

**29.6** List EVERY four-letter address beginning LR. How do you know none is missing?

Expanded layout proposal: Four address boxes, initially unnumbered; allow a branch drawing.

**29.7** How many pieces are there after four rounds? Explain without counting the picture one tiny piece at a time. Could two different four-letter addresses lead to the same piece?

Expanded layout proposal: 1.15 in explanation space.

### Student page 3: Win two challenges at once

This is a complete finite investigation. The infinite page is optional.

Gate: Fractions, or a partner comfortable with them.

**29.8** Fill the table. “Total length” means add the lengths of all surviving pieces. Do not count the erased gaps.

Expanded layout proposal: Table rounds 0–6; columns number of pieces / length of one piece / total length. Only round 0 given: 1, 81, 81.

**29.9** Can you keep MORE THAN 50 pieces while their total length is LESS THAN10? Find the first round that wins both challenges. Explain why no earlier round works.

Expanded layout proposal: 1.0 in certificate box.

**29.10** Choose five exact places you are sure will NEVER be erased. Explain what protects them, even after a million rounds.

Expanded layout proposal: Five number blanks plus 0.8 in explanation.

**29.11** Invent a new challenge: keep more than ___ pieces with total length less than ___. Find a round that wins, or explain why yours cannot be won.

Expanded layout proposal: 0.9 in chosen-challenge workspace.

### Student page 4: Could a list name every survivor?

Optional infinity investigation. The nested-interval fact is supplied, not proved by cutting paper.

Gate: Infinite sequences and quantified reasoning; no derivatives needed.

**29.12** Now imagine an endless L/R address. Keep following its nested pieces. FACT TO USE: because these closed pieces shrink to length 0, exactly one point lies in all of them. Explain why two different endless addresses give different points.

Expanded layout proposal: 0.9 in explanation box.

**29.13** Here is the start of someone’s list. Make a new address whose first letter differs from row 1’s first letter, whose second differs from row 2’s second, and so on. Fill the first six letters.

Expanded layout proposal: Six-by-six address table plus six blank boxes.

**29.14** Your six letters beat the first six rows. That alone does not beat an endless list! Describe a rule for EVERY later letter so your new address differs from row n, whatever n is. Why does the new address still name a surviving point?

Expanded layout proposal: 1.0 in explanation box.

**29.15** How could the surviving set fit inside pieces with total length below ANY positive budget, yet fail to fit in any list? Give one reason about length and a separate reason about lists.

Expanded layout proposal: Two short separate boxes: length certificate / list certificate.

### Delayed hints

- 29.2: An endpoint stays an endpoint of one surviving piece at every later round.
- 29.7: At each step, how many choices does an address have? Look at the first letter where two addresses differ.
- 29.9: Every round doubles the pieces, but each is a third as long. Keep those two changes separate.
- 29.14: Choose the nth new letter by inspecting the nth letter of row n.
- 29.15: Two rounds multiply total length by 4/9, which is less than 1/2.

### Complete solutions


**29.1** Round 1 keeps[0, 27] and [54, 81]. Round 2 keeps[0, 9],[18, 27],[54, 63],[72, 81]. Gaps are open: 27 and 54 remain, as do 9, 18, 63, 72. Distinguish a mathematical endpoint from the finite width of ink.

**29.2** 9, 18, 27, 54 are safe forever because they become endpoints and stay endpoints of surviving intervals.15 is first removed in round 2, from the gap(9, 18).40 is removed in round 1, from(27, 54). “Not erased yet” alone is not a forever proof.

**29.3** In[0, 9], round 3 removes(3, 6); for example 5 survives two rounds then is erased. Other examples: 21 is an endpoint of the gap(21, 24) and is NOT erased, so choose 22 instead. The other new open gaps are(21, 24),(57, 60),(75, 78).

**29.4** LLRR=[8, 9]; RLRL=[60, 61]. Four choices contribute offsets 0 or 54, 0 or 18, 0 or 6, 0 or 2, leaving length 1. Each address is a recursive interval choice, not a base-two coordinate value.

**29.5** [20, 21] has address LRLR: left[0, 27], right[18, 27], left[18, 21], right[20, 21]. Partner puzzles may use any of the 16 intervals in the checked address table.

**29.6** LRLL, LRLR, LRRL, LRRR. After fixed prefix LR, the two remaining positions each have two choices, exhausted by LL, LR, RL, RR. A small binary tree is a completeness certificate.

**29.7** There are 2×2×2×2=16 pieces. The first differing letter sends two addresses into left and right thirds of one parent interval, separated by a positive gap, so the final pieces cannot coincide. This finite address bijection proves the count.

**29.8** For rounds 0–6: piece counts 1, 2, 4, 8, 16, 32, 64; individual lengths 81, 27, 9, 3, 1, 1/3, 1/9; totals 81, 54, 36, 24, 16, 32/3, 64/9. Powers notation is optional.

**29.9** First win is round 6: 64>50 and 64/9<10. Before round 6 there are at most 32 pieces, already failing the first demand; round 5 also has 32/3>10. Fraction comparisons can be made by multiplying both sides by 9 or 3.

**29.10** Many answers: 0, 81, 27, 54, 9, 18, 63, 72. Each is an endpoint at some finite stage; after each subsequent split it is the outer endpoint of one retained third. Induction in pictures proves permanence. Do not assert that only finite-stage endpoints survive.

**29.11** For any finite positive piece target K and positive length budgetb, both can be met by sufficiently many rounds: 2^n grows and 81(2/3)^n shrinks. An accessible example “more than 20 pieces, less than 12 length” first succeeds at 5. Targets with budget 0 ornegative cannot succeed at a finite round, because total length remains strictly positive. Accept a chosen numeric example without requiring the general infinite-growth theorem.

**29.12** At their first different letter, two addresses enter disjoint left/right thirds of a common positive-length parent, with a positive middle gap. Their final points cannot be equal. Existence and uniqueness for one infinite address use the supplied nested-interval fact. This avoids the ambiguity of ordinary terminating positional expansions.

**29.13** The visible diagonal is LRLLLR, so the opposite letters are RLRRRL. There are many completions after those six letters. Do not claim this six-letter calculation alone defeats row 7 orany later row.

**29.14** Given any proposed infinite list of infinite addresses, choose new letter n opposite to row n’s letter n. The new address differs from every row at its own numbered position; it is still a valid infinite L/Rsequence and therefore names a survivor. If a point list was supplied, use each point’s unique address. Hence no countable list exhausts all survivors.

**29.15** Length: at roundn, all never-erased points lie within 2^nclosed intervals whose lengths total 81(2/3)^n. Every two rounds multiply by 4/9<1/2, so a sufficiently large even number of rounds puts that total below any positive budget. Formal outer-measure definitions using open intervals can enlarge the finitely many intervals by an arbitrarily small total allowance. List: the independent diagonal construction defeats any proposed enumeration. Small total covering length does not mean empty, finite or listable.

### Sources


- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/MIRA.pdf), §2D, construction 2.74 and 2.75; results 2.76–2.79, printed 56–59 (PDF 70–73). Adult limiting construction and distinction between measure and cardinality. The 81-unit finite tasks, exact addresses and budget instance were independently constructed and checked.

## GA-25 — Make a maze. Then turn it inside out.

Strong candidate for the Week 1 richness standard.

Manipulable choices, a misleading right-count counterexample, a general invariant proof, optimal local reconfiguration, and a second representation with a genuine duality surprise.

**Risk:** Four pages are too much for many one-hour groups; use 1–2 plus either 3 or 4. The courtyard page needs physical tracing; do not force a general topology proof.

**Satisfying stop:** One valid maze and a reason all valid mazes remove 4 roads, OR a shortest 4 swaproute with a lower bound.

**Boundary:** No classroom pilot yet; no claim that every random atlas card would support this expansion.

### Prerequisites and preparation

- **entry:** Trace a route; count to 12; distinguish a loop from going along one road and back. Oral directions suffice.
- **core_explanation:** Choose routes and check all rooms; explain a leaf-removal certificate or a shortest sequence of swaps. No algebra required.
- **extension:** Track the outside as one region; compare two planar networks. A complete theorem for arbitrary planar graphs is optional, not claimed from four examples.

Materials: 12 toothpicks or removable road strips per pair; 9 counters on the room dots; pencil and eraser; optional transparent sheet/highlighter for courtyard flood. Preparation about 10 minutes.

0–8 free road designs; 8–13 demonstrate a loop and a disconnected room; 13–28 maze challenge and a proof; 28–33 walk a human tree; 33–50 choose swaps OR courtyard view; 50–60 share a certificate. Four pages are a menu for one or two meetings, not a required pace.

Week 10 asks Euler/postman traversal; this uses spanning trees and planar complementarity. The swap lower bound resembles Week 1 intentionally, but the maze objects and dual representation are new. Atlas square+diagonal instance has been enlarged and replaced.

### Student page 1: Can you keep every room and lose every loop?

Give this page before the proof and courtyard pages.

**25.1** Put a counter on every room. Use the twelve roads shown. Remove roads until every room can still reach every other, but there is no loop. A loop comes back to its start without reusing a road or visiting any other room twice. Just going out and back is not a loop.

Expanded layout proposal: Two large blank grid copies, 2.6 in each. Space to circle removed roads.

**25.2** Find a second successful maze. It must keep a different set of roads. How many roads did you remove each time?

Expanded layout proposal: Two count blanks.

**25.3** Can you succeed by removing fewer? Give a partner something to check, not only “I tried.”

Expanded layout proposal: 1.1 in explanation box.

### Student page 2: A certificate for every maze

Offer after genuine attempts; leaf clue is intentionally delayed.

**25.4** This design keeps eight roads. Does it satisfy BOTH rules? Mark what goes wrong.

Expanded layout proposal: Perimeter diagram at 2.1 in; brief response beside it.

**25.5** Draw your kept roads over the faint guides; leave missing roads faint. Cross out a one-road room and its road. Repeat until one room remains. Record the room order.

Expanded layout proposal: Fresh blank grid at 2.4 in plus 8 letter slots.

**25.6** What does each removal do to the room count and the road count? Use your record to explain how many roads every nine-room maze must keep.

Expanded layout proposal: 1.2 in explanation box.

**25.7** Why can you always find a one-road room before the last room? Try following a route as far as it can go without revisiting a room.

Expanded layout proposal: 0.8 in explanation box; optional proof prompt.

### Student page 3: Repair the maze one swap at a time

No supplied intermediate states: the sequence belongs to the children.

**25.8** Change Maze A into Maze B. One swap means: restore one missing road, then remove a different road. After each whole swap, every room must still be reachable and no loop may remain. Keep all nine rooms.

Expanded layout proposal: Maze A/Maze B side by side at 2.5 in; full road labels by endpoints.

**25.9** Make a shortest swap plan. Check each step with road strips.

Expanded layout proposal: Table: swap / restore / remove; six blank rows.

**25.10** Why can no plan use fewer swaps?

Expanded layout proposal: 0.9 in explanation box.

**25.11** After restoring a missing road, how many loops appear? Which road may you remove to make the repair legal?

Expanded layout proposal: 0.8 in explanation box; generalization.

### Student page 4: The roads become walls

Optional representation change. OUTSIDE wraps around all four sides; corners of walls are not passageways.

Gate: Planar region reasoning, not just counting.

**25.12** Draw your kept roads as bold WALLS over the faint guides. Missing roads stay faint: they are OPENINGS. Water crosses openings, never bold walls or wall corners. Color where water from OUTSIDE can flow. Can it reach all four courtyards?

Expanded layout proposal: Large labeled courtyard grid, 3 in; room for flood coloring.

**25.13** Try a different successful maze. Can you trap a courtyard, or must every courtyard open to the outside? Explain your prediction with a picture.

Expanded layout proposal: 0.9 in answer area.

**25.14** Make a new map: one dot for each courtyard and one for OUTSIDE. Each removed road gives a link between its two neighboring regions. Draw those links. What kind of network did your four removed roads make?

Expanded layout proposal: Five-region node template, 2.3 in.

**25.15** Go further: draw a larger rectangular road grid. Guess how many roads a maze must remove. Test whether its removed roads still make a tree of regions.

Expanded layout proposal: Small blank drawing box; reserve challenge.

### Delayed hints

- 25.3: Can a road on a loop be removed without blocking any room?
- 25.6: Pair each disappearing road with one disappearing room. Which room has no partner?
- 25.10: Count roads that Maze B needs and Maze A is missing.
- 25.13: If some courtyards stay dry, trace the outside boundary of that dry patch.

### Complete solutions


**25.1** Many answers. Maze A keeps AB, BC, DE, EF, GH, HI, AD, DG, removing BE, EH, CF, FI. It connects all nine rooms and has no cycle. There are 192 successful kept edge sets in this fixed grid. Do not require students to enumerate them.

**25.2** Maze B keeps AB, BC, AD, DG, BE, EH, CF, FI, removing DE, EF, GH, HI. Both remove 4 roads. Any other distinct verified tree works.

**25.3** Deleting one road of a loop preserves all possible reachability: the rest of that loop gives a detour. Continue until no loops remain. Every resulting connected acyclic graph on 9 vertices has 8 edges (proved onpage 2), so 12−8=4 removals are necessary and sufficient. Before the formal count, accept a correct paired room/road certificate explained with counters.

**25.4** The perimeter uses 8 roads, but it leaves E isolated and also retains the outer 8-edge loop. Having the right edge count alone is not enough.

**25.5** For Maze A one valid leaf sequence is C, B, F, E, I, H, G, D, leaving A. Students may start from any current leaf; checks must use the graph after previous removals. For Maze B one sequence is G, D, H, E, I, F, C, B, leaving A.

**25.6** Each leaf deletion removes exactly 1 room and 1 road, preserves connectivity among remaining rooms, and cannot create a loop. Eight room deletions leave one room with no roads, so every successful maze had 8 roads. The starting 12 roads therefore lose 4.

**25.7** Take a longest simple path in the finite tree. An endpoint cannot have a neighbor off the path, since that extends it; it cannot have another neighbor already on the path, since that makes a loop. Thus the endpoint has degree 1 whenever more than one vertex remains. This is a picture proof, not a demand for the formal word “induction.”

**25.8** Use only the 12 original grid edges. Do not slide rooms, invent diagonal roads, or regard rotated drawings as an allowed swap. A valid solution is supplied under 25.9.

**25.9** Four swaps: restore BE/remove DE; restore CF/remove EF; restore EH/remove GH; restore FI/remove HI. Every intermediate graph is a tree; exact check script verifies it. Other shortest sequences are valid.

**25.10** The target has four roads BE, EH, CF, FI that the start lacks. One swap restores at most one of them, so at least 4 swaps are necessary; the displayed plan meets that bound.

**25.11** A tree has exactly one simple route between any two rooms. Adding one road creates exactly one loop: that road plus the old route between its endpoints. Remove any other edge on that loop, and the graph is a tree again. Removing an edge outside that loop disconnects the graph. If the new road is itself removed, the state is unchanged; the task excludes that empty move.

**25.12** Yes for every successful maze. For Maze A the removed edges are BE, EH, CF, FI; the region links are NW–NE, SW–SE, NE–OUT, SE–OUT. All 5 region dots are connected by 4 links with no loop. Water cannot slip through a retained wall vertex: regions cross only through a removed edge.

**25.13** Yes. If a collection of courtyards cannot reach OUT, its outer boundary consists of kept roads and contains a loop; a successful maze has no such loop. The picture is sufficient for this rectangular grid. The stronger dual-tree theorem also needs the primal connected condition, ensuring the removed-region links have no dual cycle.

**25.14** The complementary network is another tree: 5 region dots and 4 links. For Maze B its links are NW–SW, NE–SE, SW–OUT, SE–OUT. All 4096 edge subsets were checked: primal kept roads form a tree exactly when complementary dual region links form a tree. Parallel outside links are distinct roads, so do not merge them in a broader example.

**25.15** For an m-by-n array of square courtyards there are (m+1)(n+1) rooms and m(n+1)+n(m+1) roads. The required number removed is mn, matching one less than the mn+1 regions including outside. A 3 by 2 courtyard example has 12 rooms, 17 roads, needs 6 removals. Keep all horizontal rows and one vertical boundary to construct a maze. Its complement is a dual tree. The general statement is planar graph duality, not a claim about arbitrary crossing networks.

### Sources


- [Allen Hatcher, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), Chapter 0; §1.A, Proposition 1A.2, printed 84–85 (PDF 92–93). Adult graph/fundamental-group connection. This specific 3×3 maze, swaps and dual worksheet are independently designed/verified.
