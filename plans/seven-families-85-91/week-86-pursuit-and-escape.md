# Week 86: Pursuit and escape on graphs

Planning draft, 11 October 2026. **Unbuilt, unpiloted; board handling and timing untested.** Provisional library identifier 86, checked against the fetched collection before assignment; this is a family for several visits, not a promise to finish seven pages in one hour. This file is a revised planning-stage output. Independent mathematical and operational reviews and their resolved findings are recorded in [REVIEW-RESOLUTION.md](REVIEW-RESOLUTION.md). No existing packet or app changes are proposed.

## Facilitator opening: mathematical destination

Use finite, connected, undirected graphs. The cop chooses a starting dot, the robber chooses a dot after seeing it, and the cop moves first. Turns alternate. A player may stay or move along one road. Both positions remain visible. Sharing a dot is immediate capture, including at placement. A robber victory means a strategy to avoid capture indefinitely; surviving a classroom time limit is an experiment, not that conclusion.

**Trees are cop-win.** The cop moves one edge along the unique path toward the robber. The robber cannot cross the cop. Each uncaptured cop move excludes the cop's old side of the tree and leaves a strictly smaller possible region for the robber, so capture occurs in a finite tree. Branches do not give a way around the cop. On an n-dot path the fastest worst-case cop start is a middle dot and requires floor(n/2) cop moves. This count assumes the robber can stay.

**Bare cycles of length at least four are robber-win.** Before every cop turn, the robber can keep its dot outside the cop's closed one-step neighborhood. After the cop moves, the robber can stay if still safe or move to a neighbor that is outside the new cop neighborhood. Such a neighbor exists on a bare cycle with at least four dots. A triangle is different: any cop start is next to every other dot. A graph containing a cycle can still be cop-win: a square with a diagonal, a triangle with branches, and a wheel with a central hub are examples.

**A fold is a useful optional certificate.** A dot v can fold into an adjacent dot u if every place accessible from v by staying or taking one road is also accessible from u. In adult notation, N[v] is contained in N[u]. Deleting v preserves whether the graph is cop-win. Repeated folds reduce a cop-win graph to one dot; the full finite cop-win/dismantling equivalence is a deeper return-visit theorem, not an assumed explanation supplied by the first games. Sufficiency and the specific square-shadow counterexample are proved below; the necessity argument is an adult continuation.

Children should discover the difference between a tested tactic and a strategy against any response, between a branch and a route around the cop, and between adding roads and helping one particular player. Grades 2–3 readiness usually reaches paths, trees and rings through partner play. Grades 4–5 readiness can build strategy explanations, edit boards and use folds. An adult-assisted K–1 trial can use the first path after checking turn-taking; a full separate K–1 packet is not planned. These are operational predictions, not classroom observations.

## Kernel-only brief for later worksheet workflow

1. On finite trees, the robber's component behind the advancing cop strictly shrinks. Paths make the trap visible before branches are added. On paths with 5 and 7 dots the optimal worst-case capture times are 2 and 3 cop moves.
2. Bare cycles C4, C5 and C6 permit perpetual evasion with the robber outside the cop's closed neighborhood at the beginning of every cop turn. C3 does not. To make C4 cop-win by adding roads between its existing dots needs one diagonal; C5 needs two chords. A five-cycle with one chord retracts onto a four-cycle.
3. Optional encore: dominated-dot folding certifies a cop strategy; two cops can catch on any finite cycle by leaving one stationary and using the other to sweep the remaining path. A general graph's cop number is outside this family's checked scope.

Suggested emphasis: K–1, optional assisted turn-taking and endpoint trap only; 2–3, concrete play on paths, two trees and rings with a referee; 4–5, winning strategies, minimal road edits and justified map construction, followed by folding or two cops when ready.

## Prerequisites and routes

| Route | Reading / arithmetic | Reasoning and action | Planned pages |
|---|---|---|---|
| Concrete entry, roughly 2–3 | Adult can read; identify C and R; no arithmetic needed | Retain whose turn it is, move exactly one edge, allow a stay, use visible opponent position | Pages 1–3, then page 5 if game design appeals |
| Strategy route, roughly 4–5 | Short sentences; optional counting to 3, and six roads for page 5 | Respond to a partner, distinguish a repeated plan from a lucky play, consider an opponent choosing the worst reply | Pages 1–5; proof conversations when the child has a conjecture |
| Fold encore | Adult reading allowed; no calculation | Compare two visible sets of nearby dots, keep an original board while removing dots on a second board; shadow argument is substantially harder | Page 6, with adult conversation; neither it nor full classification is a first-visit requirement |
| Two-cop encore | Same rules plus two cop moves before a robber turn | Coordinate a blocker and chaser; extend a path strategy to a ring | Page 7 |

The current group has fixed KK11 / 3333 / 445 tables and three anchored adults. At the upper table rotate the third child as referee. At the middle table each pair uses a turn marker; the anchored adult helps disputes without choosing the moves. The K–1 parent can trial page 1 with two children at a time if they independently retain the legal action; select an established concrete activity for that table if this would consume the parent's whole attention. Routine adult reading, counting or writing a child's strategy is support; adult selection of every move means the route has not become independent.

## Printable materials and preparation

US Letter, single-sided, 100% / Actual Size. Final planned header: `Week 86 / Pursuit and escape / Grades 2–5`; footer `Bellingham Math Circle / Week 86 / W86-S-v1` plus page number. A route cover/guide may state prerequisites; it is not extra student-page prose. Pages 1–7 keep Problems 1–7 consecutively. Additional board copies are labelled `Extra workspace`, never additional numbered problems.

Per pair: two flat counters labelled C and R, 14–18 mm wide; one two-sided turn tile, 35 × 35 mm (`C moves` / `R moves`); one dry-erase sleeve; one fine-tip erasable marker; one wipe. Referee points at the tile and turns it over after a legal move, including a stay. Counter identity must use a label or shape as well as color. For page 7 add a third counter labelled C2 and replace the turn tile with `Both cops move` / `R moves`. Three reusable paper road strips, 4 mm × 110 mm, are optional for page 4; mark their endpoints at the chosen dots. A whiteboard shared by each table holds children’s conjectures and one chosen example, not a concurrent move tally.

Reusable board dimensions: working dots are 22 mm unfilled circles with lowercase labels just outside; counters are at most 18 mm wide. Adjacent dot centers are at least 32 mm apart, apart from the explicit path exception below. Long edges need not have equal length, because a road is one move regardless of ink length. Line width 1.2 pt; labels 13–14 pt; no connections at unlabeled crossings. In this family every supplied graph has a crossing-free drawing. Compact reference diagrams use the same labels and edges.

- Page 1: two horizontal path boards, 132 × 35 mm for five dots and 188 × 35 mm for seven. The production default is 28 mm path spacing with 18 mm counters and 20 mm dots. They can be stacked vertically on one Letter page. Other boards retain 32 mm spacing. This exception must be physically checked before printing.
- Page 2: two working trees, each within 170 × 105 mm, on **two separate reusable apparatus sheets**. The task page shows matching compact locators, about 75 × 50 mm, and keeps its answer space; children play on the full boards. The actual tree grid spans 128 × 64 mm before dot diameters and labels, so an 80 mm height is insufficient. Page 3: two upper working ring boards C4/C5, 85 × 85 mm each, side by side, and one lower C6 board, 110 × 100 mm, on one separate apparatus sheet. Minimum working center separation 32 mm. A polygon need not be regular, but equal x/y scale must preserve any regular polygon the renderer chooses to draw.
- Page 4: blank C4 and C5 within 160 × 85 mm each, stacked; put chord strokes on the sleeve, then erase before trying another choice.
- Page 5: two six-dot blank sets within 160 × 75 mm; enough blank space between dots to draw a crossing-free map, and a 160 × 35 mm drawing/writing strip below.
- Page 6: each map 145 × 100 mm, on its own apparatus sheet, with a second clean copy below it. The task page has only compact 70 × 45 mm matching locators beside the rules/worked example and its explanation space. Movable 22 mm opaque cover disks show deleted dots; erasable road markings show which roads disappear. The original remains visible, avoiding a memory-only comparison. Adult fits two full copies in a 210 mm height and checks labels; otherwise print original and working copy as two apparatus sheets.
- Page 7: C6 and C8 within 165 × 100 mm, each on **a separate apparatus sheet**; compact locators and explanation space stay on the task page. Put one cop counter at each of two selected dots before the robber chooses. No physical scaling determines an answer.

Current print budget if both older tables use the family: three pair kits, six labelled playing counters plus three turn tiles, three spare R counters; one selected task-page bundle per pair. First visit adds three apparatus sheets per pair: T1, T2, and rings. Page 6 adds two or four fold sheets per pair; page 7 adds two ring sheets and a third counter per pair, only if selected. Optional K–1 trials need two further pair kits. Parent preparation estimate: 10–15 minutes printing, cutting turn tiles and labelling existing counters; add 10 minutes to fit-check all large boards and rehearse a stay/capture/referee cycle. Estimates are untested. No cutting or constructing specialist equipment is required during a session.

## Shared launch and conventions

After the usual movement time, give children two counters and let them move around a non-task graph for about one minute. Then the adult puts C down first, invites R to choose a different dot, and demonstrates a one-road cop move, a robber stay, and how the turn tile changes. Ask the pair to make a legal attempt to catch or escape. Keep explanation of strategy for later.

Page 1 shared rules, ordinary unnumbered text:

> Put the cop C on a dot, then put the robber R on a dot. C moves first. Take turns: move along one road or stay. Both counters stay visible. If C and R share a dot, C catches R. R tries to avoid capture for as long as possible.

“As long as possible” is the physical game goal; Problems 2–3 introduce the mathematical guarantee and forever question. A classroom timer must never turn the theorem into a claim about surviving a particular number of turns.

The first rules have a small explicit worked visual on a **non-task T-board** with roads x–y, y–z, y–w. Input panel: C at x, R at z, tile `C moves`. Intermediate panel: C at y, R at z, tile `R moves`; caption `C takes one road`. Output panel: C at y, R still at z, tile `C moves`; caption `R stays`. A small pale motion arrow may connect counter positions within the panels; it is a move indication, not an extra road. Match x/y/z/w labels in all three panels. Do not show the next capture or explain the tree theorem here. The actual graph is a T, so no unlabeled crossing is introduced.

## Page-by-page student plan

Each page contains only the standard header/footer, essential shared guidance when a new convention appears, and its numbered problem with boards and space. Facilitation below does not become student copy.

### Page 1 — paths; Problem 1

After the rules and worked visual, print:

> **Problem 1:** Play on both paths and swap jobs. Where should C start to catch R as quickly as possible, even when R chooses the hardest place to start?

Boards: path `a–b–c–d–e` and path `a–b–c–d–e–f–g`. Nothing is preoccupied. Supply one small empty start circle and a 110 × 30 mm answer/drawing area beside or below each board. The large boards are the play space; children need not reproduce moves or count while playing. Adult can put a counter on a whiteboard numeral only when testing a claimed fastest start. This is 8–12 minutes of repeated contrasting games, not a mandatory warm-up tally.

### Page 2 — branches; Problem 2

> **Problem 2:** Make a cop plan that catches R on each map, wherever R starts and however R moves. Challenge your partner to escape from your plan.

Top locator/tree T1: vertices `o,a,b,c,d,e,f`; edges `o–a,a–b,o–c,c–d,o–e,e–f`, a three-armed tree with arms of two roads. Full working coordinates in 32 mm units: o=(0,0), a=(-1,0), b=(-2,0), c=(0,1), d=(0,2), e=(1,0), f=(2,0), translated to its apparatus sheet. Lower locator/tree T2: vertices `a,b,c,d,e,f,g,h`; edges `a–b,b–c,c–d,d–e,c–f,f–g,f–h`. Working coordinates in 32 mm units: a=(-2,0), b=(-1,0), c=(0,0), d=(1,0), e=(2,0), f=(0,-1), g=(-1,-2), h=(1,-2). Orient/translate without stretching x/y independently. A 160 × 35 mm white space on the task page takes a drawn strategy or adult-scribed sentence. There is no full game log table.

### Page 3 — rings; Problem 3

> **Problem 3:** Play on these rings. Can R have a plan that avoids capture forever, even when C changes its moves? Show a plan for each ring.

Show matching compact locators C4, C5 and C6, with labels a onward in cyclic order and no inner roads. Full working boards are on the single rings apparatus sheet specified above; each can be erased and reused. Three tiny result spaces are unnecessary; provide one 165 × 35 mm area for a picture or adult record. Referee can pause between moves so the defender selects a safe dot. A repeated round alone remains evidence for a conjecture; the adult key supplies the invariant.

### Page 4 — road edits; Problem 4

> **Problem 4:** Add as few new roads as possible to each ring so that C can always catch R. Roads join two existing dots. Show a winning cop plan for your changed map.

Use clean C4 `a,b,c,d` and C5 `a,b,c,d,e`, stacked, with marker/chord overlays; a road already present cannot be added again. No new dots, directed roads, crossing junctions or longer cop moves. The two minimum answers differ. Leave 165 × 40 mm for the chosen changed maps or minimality explanation. Readiness gate: children need the page 3 forever distinction. On a first visit the pentagon's “one is not enough” may remain an adult conversation, not a demand to invent graph retractions.

### Page 5 — game design; Problem 5

> **Problem 5:** Draw two connected maps using all six dots and at least six roads on each. Make one map where C can always catch R and one where R can always escape. Challenge your partner on both maps.

Two six-dot sets, labelled a–f, arranged as a shallow hexagon. Each has 165 × 75 mm and a lower blank region for an alternate drawing if a chord crossing would otherwise obscure connectivity. Road endpoints must be printed dots; no two roads have the same endpoints. Distinguish a convincing finite game from a reason the plan keeps working. This deliberately requires a cycle in the cop-win example, refuting “all cyclic maps permit escape.” Counting six lines can be adult-supported.

### Page 6 — fold encore; Problem 6

New unnumbered convention:

> You may fold v into its neighbor u when every place you can reach from v by staying or taking one road can also be reached from u. Remove v and all its roads. Keep the other roads.

Before Problem 6 show a worked non-task four-dot path `w–x–y–z`: input circles around reachable places w,x and x's reachable places w,x,y; intermediate overlay maps w to x; output path x–y–z with w and road w–x removed. Labels remain w/x/y/z, with `from w: w,x`, `from x: w,x,y` beside the actual dots. This is the first use of the closed-neighborhood convention; no N[v] notation on student pages.

> **Problem 6:** Can each map be folded down to one dot? Find a sequence of legal folds, or show where every possible next fold fails. What does your result say about the chasing game?

Map F1: six vertices a–f, edges a–b,b–c,c–a,c–d,d–e,a–f (triangle with a two-road tail and a leaf at a). Map F2: five-cycle a–b–c–d–e–a plus chord a–c. Supply one original and one movable-cover copy of each on separate apparatus sheets, labels matching compact task-page locators exactly, with a single 160 × 35 mm task-page record space for fold arrows such as `e → d`. Worked example teaches this record too. The adult may write the fold arrows children choose. This is an explicit new procedure for comparing graph neighborhoods; do not demand its full correspondence with strategies as a child theorem.

### Page 7 — two-cop encore; Problem 7

New shared rule: `Put down both cops before R chooses a dot. On a cop turn, each cop may stay or take one road, then R gets one turn. Capture happens as soon as a cop shares R's dot. Cops may share a dot.` Demonstrate this turn using an ordinary board and the new turn tile before distributing the page; no unfamiliar symbolic representation needs another printed example.

> **Problem 7:** Use two cops to catch R on both rings. Find a plan that works however R moves. Will your plan work on every ring?

Clean C6 and C8 locators, with full working boards on their separate apparatus sheets, not already marked with earlier strategies. Three labelled counters. One 165 × 40 mm task-page explanation space. The strategic difference is coordinating a blocker and a chaser, not a longer ring record. A second adult is not required: the player controlling cops uses both counters, the other controls R, and upper-table referee rotates.

## Keyed facilitator solutions, held hints and proof scope

**Problem 1.** Five-dot path: start c, worst-case 2 cop moves. Seven-dot path: start d, worst-case 3. The robber can choose a farthest endpoint and stay, forcing at least that many cop moves because a move crosses at most one road. From a middle start the cop walks toward the visible robber; the robber remains on that side, cannot cross the cop, and cannot retreat beyond its endpoint, so the respective upper bounds hold. Other starts have larger maximum endpoint distance. Delay hint: physically block the dot occupied by C and ask R whether it can pass to the other side. Optional shortest-game count belongs on the adult whiteboard after the children have a plan, not in a concurrent tally.

**Problem 2.** Both are trees. Choose any starting dot; moving along the unique path to the current R wins. Let S be the component containing R after deleting C. The next cop move enters S, and the new robber component is a proper subset of S, unless capture occurs. R's legal reply cannot leave that component without moving onto C. Thus this set strictly shrinks on every uncaptured cop move; at most n−1 such advances are possible. R may switch arms ahead of C, so “the distance goes down every turn” is not the proof: it may stay the same after R replies. The shrinking region is the invariant. Optional hint: place cover disks over the region C has made unreachable, without covering playable routes ahead. T1 starting o catches in at most 2 cop moves; T2 starting c catches in at most 2. These times are supplementary, not requested on the page.

**Problem 3.** Before C's first move, R chooses a dot that is not C and not adjacent to C; C4–C6 all have such a dot. Maintain that condition at the beginning of each cop turn. C cannot capture on its next move, because it moves at most one edge. After that move, if R is still at distance at least two, R can stay. If C is now a neighbor of R, move away along the other ring edge: on Cn for n≥4 that other neighbor of R is neither C nor adjacent to C. Hence R reestablishes the condition. For C4 an opposite robber simply switches to the opposite dot after C moves one road, or stays after C stays. For C5/C6, keeping “opposite” is not a uniform convention; the safe-neighbor invariant works. An adult asks a partner to choose each possible cop response to test the local argument. “Ten rounds survived” never proves indefinitely.

**Problem 4.** C4: no addition fails by Problem 3; either diagonal makes one endpoint adjacent to all other dots, so starting there captures on the first move. Minimum one. C5: two chords sharing an endpoint, such as a–c and a–d, make a adjacent to all dots, so two suffice. Zero fails. Any single chord is equivalent by relabelling to a–c. Fold b to a; the resulting map on a,c,d,e is a bare square. More explicitly project the cop's position by f(b)=a and f(x)=x otherwise, while keeping R on the square. Each cop move projects to a legal square move or a stay. The square robber strategy stays outside the projected cop's closed neighborhood; actual capture would imply projected capture, which cannot occur. Hence one chord fails. This proof uses a graph map and is a held upper-route/adult explanation. The finite checker verifies every one-chord position, but those calculations do not replace the reason. Additional child solutions using two other chords are acceptable if an actual guaranteed strategy is given; the task asks a minimum, not a catalog of every minimum completion.

**Problem 5.** Cop-win example: triangle a–b–c–a with tail c–d–e–f, six roads. Start at c. If R starts a or b, catch on the first move. Otherwise follow R along the tail as on a path; R cannot pass C to enter the triangle. Robber-win example: bare C6, six roads, using Problem 3's invariant. Both maps are connected and use six dots and at least six roads. More examples may be accepted by their explicit strategy rather than diagram resemblance. Hint only if stuck: invite children to attach a branch to a board they already understood, without stating that it must be the cop example.

**Problem 6.** F1: e→d, then d→c, then f→a leaves triangle a,b,c. Fold a→b, then b→c to end at c (other legal choices also work). At each step check neighborhoods in the **current** remaining graph. The original stays beside it only as a reference, not the neighborhood test after deletions. F2: the only initially foldable dot is b, which can fold into a or c. After either deletion, the remaining a,c,d,e form C4, where each closed neighborhood has three dots and differs from every neighbor's, so no legal fold remains. F1 is cop-win; F2 is robber-win, as also proved in Problem 4.

Adult fold sufficiency: given N[v]⊆N[u], define f(v)=u and fix every other vertex. A real robber move maps to a legal move or stay on G−v. The cop can follow a winning strategy there against this shadow. When it catches the shadow, either it has caught R or C=u and R=v. After a robber reply from v, its new dot lies in N[v]⊆N[u], so the cop captures on its next move. Induct through a recorded fold sequence to produce a strategy. The difficult part is holding the real and shadow games simultaneously; allow children to stop at a physical fold certificate.

Adult necessity continuation, optional: in a finite connected graph with more than one vertex and no dominated dot, R starts outside N[C]; such a dot exists since a universal C would dominate every other vertex. After a safe cop move, if R∈N[C], non-domination supplies a point in N[R] outside N[C] for R's reply; otherwise R stays. This perpetually avoids capture. Repeated legal folds terminate. If the remaining graph has more than one vertex, compose the fold maps into a retraction onto it; its robber strategy lifts to an evasion strategy for the original graph by keeping R in the remainder and projecting C. If one vertex remains, sufficiency gives the cop strategy. This proves the finite equivalence, with connectedness and closed neighborhoods essential. It is a guide destination, not a seven-year-old's prerequisite.

**Problem 7.** Put one cop at a as a stationary blocker and the other at b. R chooses some remaining dot. Deleting a turns the cycle's other vertices into a path. The second cop follows the unique path to R; R cannot pass the stationary cop to use the missing connection. The path proof catches R. If R initially chooses either occupied dot it is captured immediately. This works for every finite cycle, including C3; it does not assert two cops suffice on every graph. Held hint: ask whether one cop can make an edge of the ring permanently unusable. Cop motion remains one road each, not a pooled budget of two moves for one cop.

## Visits, adult questions and use records

First visit after movement: 3-minute launch, 8–12 minutes page 1, 12–15 minutes page 2, 10–15 minutes page 3, brief sharing. Forty minutes of table time is a target; page 2 can take the rest of the visit. An upper pair that already reasons about tree traps may choose page 4 after initial ring play. Do not accelerate children past repeated physical cases in order to reach a formal statement.

Next visit choices: page 5 map design challenges the “cycle means escape” guess and supplies reusable authored games; page 4 investigates how added roads alter strategies; page 6 studies graph reduction and certificates; page 7 adds cooperation and a blocking invariant. These are different investigations, not only larger numbers. Choose one encore destination per visit, retaining unfinished worthwhile work.

Adult questions after a child has played: “What can the other player do if it knows your plan?”, “Which places has C made impossible for R to reach?”, “Does that same response still work when C stays?” Hints, arbitrary finite round limits and proof prompting stay with the guide. Record the actual boards and Problems used, independent retention of stay/turn rules, a child's strategy in their words, and whether an adult chose moves. Record observed disputes separately from predictions about why they arose. Every route remains unpiloted until actual use is logged.

## Novelty and consulted corpus

- Read the actual [Week 67 student source](../../lowell-math-circle-year-2/source/week-67/student/students.tex), [mathematical note](../../lowell-math-circle-year-2/source/week-67/MATHEMATICS.md), [review](../review/week-67.md), and rendered student PDF pages 1 and 3. Its colored shortest-road checks keep one reference state fixed. Here each move changes the game state and visibility matters. Reuse the clear labelled-road convention; do not reuse its meeting-point tasks. Its tree and square are related prerequisites, not prior pursuit play.
- Read actual Week 24 grades 2–3 student source/page 1 and its review for partner-enforced game rules and recoverable comparisons. Pursuit has adversarial perfect information, not random draws or a probability table. Board design does not depend on prior nontransitivity work.
- Read the [Week 1 encore README](../../lowell-math-circle-year-2/source/week-01-encore/README.md): material reuse supports a new invariant or representation. The folds and two-cop visits follow that pattern.
- Read retained organizer Fall 2025 DOCX text: Handouts 2, Problem 2.3, gives the take-away game and asks children to play to work out a strategy; Handouts 3, Problems 3.1–3.3, revisit it at different pile/rule sizes. This supports play followed by a return visit as a format; no pursuit task was identified in those consulted passages. No copied incorrect historical arithmetic is imported.

## Primary source attribution and source boundary

- Mostafa Azizi / Fan Chung Graham, [A Game of COPS & ROBBERS](https://fanchung.ucsd.edu/152/arch/coprob/), revision spring 2002: inspected `Description of the Game`, the path/cycle/tree claims, and `Structural Description` with its fold theorem. These fix the rule convention and supply the fold lead. Board choices, prompts, material dimensions and child routes are new adaptations, with self-contained proofs above.
- Richard Nowakowski and Peter Winkler, [Vertex-to-vertex pursuit in a graph](https://www.sciencedirect.com/science/article/pii/0012365X83901607), *Discrete Mathematics* 43 (1983), 235–239, DOI 10.1016/0012-365X(83)90160-7: inspected publisher abstract to verify visible alternating play, cop placement/move first and allowed stays. Full article was not opened; do not imply a page-by-page audit of its classification proof. The optional theorem is attributed to this original research and checked here by the supplied argument.

No wholesale downloaded article belongs in Git. Pedagogical choices and preparation estimates are our hypotheses, not findings reported by either mathematical source.

## Review and production gates

- Verify all supplied edge sets; an extra road or unlabeled junction can reverse a game. The rule tile must allow a stay, and capture must stop the game immediately. Physical rehearsal should include a robber stay next to C and a cop stay on C4.
- Mathematical risk: a greedy chase-distance argument is insufficient on trees; use the shrinking-region proof. Square “opposite” is not the sole strategy on longer odd rings. Adding edges may help the cop. A finite successful simulation does not prove an infinite evasion claim.
- Operational age-fit risk: the children may retain “move” but omit “stay”, or count ink length rather than a road. Those are predictions requiring launch/rehearsal evidence. Two counters and a turn tile externalize the core state; folding and shadow games are separate gates.
- Checker: `checks/check_games_voting.py` (planning examples only) uses a finite game-state attractor to classify the actual paths, trees, cycles, road edits and folds; general proofs remain written above. The separate independent review checks these same examples without importing author code.
- Before PDF production, extract the kernel-only brief into the unchanged worksheet workflow, check the then-current roster, use fresh writer → critic (+independent enumeration math) → reviser agents, and separately author/review the facilitator guide. Render every selected board/page, check counter fit and labels, and rehearse the physical turn procedure. No claim is made that a current PDF, source ZIP, combined set or cloud copy has changed.
