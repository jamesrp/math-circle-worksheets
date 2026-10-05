# Week 13: Route packing and bottlenecks

**Verdict: keep.** No must. Every band reaches max-flow/min-cut through drawn routes and closure markers, the pages are clean, and the math check found no student-page error. The fixes are two sentences that give away the point, thin practice with the change-walk, and guide repairs.

Reviewed October 5, 2026 by Claude, with the math check in [week-13-math.md](week-13-math.md); I agree with all five of its findings. Packets: `week-13-k-1.pdf` (F13-K-v2, 6 pp., Problems 1–6), `week-13-grades-2-3.pdf` (F13-23-v2, 7 pp., Problems 1–6), `week-13-grades-4-5.pdf` (F13-45-v2, 7 pp., Problems 1–7). Adult guide: `week-13-facilitator.pdf` (11 pp.). Companions noticed but not reviewed: `week-13-return-visit.pdf` (W13-RV-v1, 3 pp.) and its guide; the math check found its Problem 2 last map repeats map 1. Status: unpiloted (October 4 revision; the organizer approved its scope, not classroom use).

## The mathematics

Routes follow arrows from Start to Finish and may share dots but not arrows; a marker closes an arrow. The most routes equals the fewest closures, and k routes with k closures that stop everything prove both at once. Every band meets "stuck is not largest" on the greedy board. Grades 2–3 add an interior bottleneck, a complete closure list and rerouting; grades 4–5 reach cuts with backward arrows, a route crossing a smallest cut twice, change-walks, the reachable-set cut and the general theorem (P7). A mathematician would enjoy it: a real duality theorem with a certificate on each side.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Max-flow/min-cut with both certificates; 4–5 P3–P7 build the augmenting-path proof. |
| Problems | strong | Nearly every problem has two contrasting boards and a find-every, fewest, possible-or-not or game goal. Gaps: K–1 P3 states the equality; the change-walk gets one board (fixes 1, 3). |
| Student pages | strong | Header, footer and Problem labels only; short tasks; large boards with room. Two sentences carry the point (fixes 1, 2). |
| Concreteness | adequate | Markers close arrows physically; the game and the guide's "sneak a route" check put a partner on the rules; one launch shows tracing, closing and dot-sharing. The no-shared-arrow rule lives in pencil, and colored routes cannot be erased on the trap boards (fix 4). |
| Correctness | strong | The math check confirms every answer on the 42 student boards. |
| Adult guide | adequate | Theorem-first overview, launch, menu, keys, hints, full proof. Two keys incomplete, the token proof muddled (fixes 5–7). |
| Age fit, K–1 | adequate | The same ideas at small scale: one-sentence tasks, a game, find-every tasks, counting to three. The opening rules are four sentences, with "collection", for one hearing; P4 needs adult recording. |
| Age fit, grades 2–3 | strong | Lettered dots allow written lists; P3's completeness and P4's impossible board are real explanations at small size; P5's two-cancellation board comes late. |
| Age fit, grades 4–5 | strong | P1–P4 start concretely. The change-walk definition and P7 are heavy but late, at the organizer's table. |

## Keep

- The two-sided certificate in every band; the greedy board, stuck but not largest (K–1 P1, P4, P6; 2–3 P1, P5; 4–5 P1).
- The interior bottleneck board (2–3 P2, P4; 4–5 P2, P6): three arrows leave Start, two leave D.
- The eight-pair closure list (2–3 P3, K–1 P5 with recording copies); 2–3 P4 and its impossible board; the double-trap board needing two cancellations (2–3 P5, 4–5 P1).
- 4–5 P3 (backward arrows into the Start side), P4 ("at least one" cut arrow, not "exactly one"), P5 (staircase), P6 (reachable set), P7.
- The closing game: diamond a second-player win, greedy a first-player win only by closing AB.
- Unlettered K–1 boards, lettered older boards, no crossings; the guide's p. 1 overview, p. 4 certificate argument and p. 10 existence proof.

## Fix

1. **should**, K–1 p. 3, P3: "Then stop all travel with the same number of markers." It states the equality the packet builds toward, and K–1 has nowhere else to notice it (P1 and P2 use different boards). Write "Then stop all travel with as few markers as you can." and have the guide ask children to compare the numbers.
2. **should**, 4–5 p. 3, P2: "…and why the two answers show that your collection is largest" states the certificate. Use 2–3 P2's "Explain how you know your collection cannot be larger."
3. **should**, 4–5 p. 6, P5: the change-walk is tried on one board, then P6 and P7 depend on it. Add "on this board and on both boards of Problem 1"; guide p. 7 already solves those (s-B-A-t; s-B-A-C-E-D-t with two cancellations).
4. **should**, guide pp. 2–3, materials and launch: the repair tasks (K–1 P1 upper; 2–3 P5; 4–5 P1, P5) need a route undone, colored pencil does not erase, and nothing stops two routes on one arrow. Say to draw routes there in pencil patterns or wipe-off marker on a sheet protector; in the launch, show two routes on one arrow as illegal. Prediction; unpiloted.
5. **should**, guide p. 6, 2–3 P4 key: "Upper board: add D to G." is one of 16 answers; any arrow from A, B, C or D to G, H, I or J works, and an adult may doubt a child's A→H. Use math check item 1's wording.
6. **should**, guide p. 8, 4–5 P4 key: it omits that no route uses both arrows of {sA,sB} or {Ct,Dt}, the likeliest first finds. Add math check item 2's list of the five smallest sets.
7. **should**, guide p. 10, drawing proof: "Only the k departures from Start and the outward boundary crossings survive" merges two counts and never shows that k equals the outward count. Use math check item 3's two-way token count.
8. **could**, K–1 p. 5, P5: eight copies for eight answers tell children when they are done; print ten.
9. **could**, 2–3 p. 6 and 4–5 p. 2: the unlabeled clean copies can look like a missing problem; the adult says what they are.
10. **could**, K–1 p. 1 rules: drop "without visiting a dot twice" (no K–1 board has a cycle) and "in a collection".
11. **could**, 4–5 p. 6 worked visual: C and D are also P5 dots, with no C→D arrow there; use other letters.
12. **could**, guide p. 5, K–1 P5: "The final page has a large working board" means page 5.
13. **could**, K–1 P6 and 2–3 P6: add K–1 P3's three-branch board, a second-player win because closing a dead arrow is a spare move (my game-tree check).
14. **could**, guide p. 3 menu: match context.md's hour (run, launch, tables, share), not free tracing and a 25–28 standing break.

## Overlaps

Week 19 (antichains) shares the two-sided certificate and "maximal is not maximum" on another object; Week 53 shares the improve-then-certify arc and, in the app, the graph board with 39, 52 and 62. No other theme has max-flow/min-cut; no merge.

## App fit

Fit B, as the row says. The child taps arrows from Start to draw routes (the app refuses a used arrow or revisited dot, which paper cannot) and taps arrows to place roadblocks. The solve is k routes and k roadblocks leaving no open route; that pair certifies "best", so the app never shows k. A leak shows the open route. For "add one arrow so three routes fit" (2–3 P4), the impossible board's certificate is the two Start arrows the move cannot touch.

Pitfalls:

- No slot per answer in find-every tasks (K–1 P4, P5; 2–3 P3); the child declares done and the app checks.
- Erasing a route takes one tap, because the greedy trap is about undoing.
- Don't require change-walk notation; pre-reserved stuck boards make the child reroute without it.
- Play the closing game against perfect play rather than asking who wins.

Draw on K–1 P1–P6, 2–3 P2, P4, P5 and 4–5 P4, P5. The app's Routes and roadblocks family (`dist/families/flow/`) takes this shape.

## Classroom evidence

None reported. Unpiloted; marker fit on the shortest edge (26 mm centre to centre) and timing are untested.
