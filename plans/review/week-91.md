# Week 91: Rotor-router machines

**Verdict: keep.** No must in the base packet: every answer, diagram and material checks, the boards and cards are printed, and the guide opens with the theorems. The return packet's wrong key word is a companion finding (Weeks 17, 22, 30, 38). The missing K–1 route is a should, because the design leaves K–1 out (Weeks 60, 76, 87).

Reviewed October 23, 2026 by Claude, with math.md. I agree with its four findings, each a should. Packets: week-91-students.pdf (students-v1, 6 pp.: Grades 2–3 P1–P3 on pp. 1–3, Grades 4–5 P4–P6 on pp. 4–5, Grades 2–5 P7 on p. 6); week-91-materials.pdf (materials-v1, 7 pp.); band views for 2–3 (pp. 1–3, 6) and 4–5 (pp. 1, 4–6). Adult guide: week-91-facilitator.pdf (F91-FAC-v1, 6 pp.). Companions noticed: week-91-return-visit.pdf (return-visit-v1, 4 pp., Grades 4–5 roads), reviewed only for fix 6. Status: unpiloted. The kit and timing are unrehearsed (guide p. 2).

## The mathematics

A card shows the next exit and flips after each departure. So at one switch, any run of consecutive visits splits within one. A complete depth-d tree sends every block of 2^d counters once to each leaf, from any start, and its cards then return. A tree can make exactly the orders that alternate at every switch: 2^(2^d−1) of them, one per start. The all-left order AECGBFDH is the bit-reversal order. In the return packet, position plus right-pointing cards is conserved, which gives exactly s right exits in every m launches, with no burn-in. A mathematician would enjoy it. P2–P4 and P6 carry the trees, P7 the contrast with a coin, and return P3 and P5 the score.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | The Propp machine: balance, order constraints, an invariant. |
| Problems | strong | The sequence runs operate (P1), invert (P2), possible and impossible targets (P3, P4), theorem (P6). The impossible targets fail at counters 1–2 (ABCD), at 2–3 (DABC) and below the root (AEBFCGDH). P5 is thin (fix 4). |
| Student pages | adequate | Headers, footers and numbering are right; no neg.md items. Faults: P4's labels (fix 3) and the band label on pp. 1–3 (fix 2). |
| Concreteness | strong | Two-faced cards hold the state, and a partner checks each move. The launch shows one move, then a child makes the next (guide p. 2). |
| Correctness | strong | The math check confirms every student answer, diagram and material. The guide errors are wording (fix 5) and the companion key (fix 6). |
| Adult guide | strong | Theorem-first p. 1 states assumptions, limits, a band map and evidence levels. Full keys; hints that withhold cards. |
| Age fit, K–1 | weak | No route: "only an optional adult-supported one-switch station" (p. 1), or "a familiar pattern-block activity" (p. 2). |
| Age fit, grades 2–3 | strong | Adults read; children count to 12, follow arrows and track three cards with a partner. P3's reason needs only that A and B are both on the left. |
| Age fit, grades 4–5 | strong | Seven cards with rotating roles; P6's bundle proof; the return packet's score. |

## Keep

- The p. 1 rules and the Input / Move to X / Flip pictures.
- P1's two trials and four strings.
- P2's D-first inverse problem, with its free left card and exactly two answers.
- P3's four targets, and P4's all-L, all-R and AEBFCGDH targets.
- P6 with the guide's bundle argument, and P7's XX.
- Cards whose sideways flip turns ↙ into ↘, and the 24 mm board circles.
- The return packet's short-road example, its LLR start and its score table.

## Fix

1. **should**, K–1, guide pp. 1–2. A station with no tasks, though moving counters and flipping cards needs no reading. Add a route on p. 2:
   - the launch;
   - P1 with the parent reading, plus "Can X come twice in a row?";
   - on the four-exit tree, "Send four counters. Does every exit get one?" and "Make the first counter land on D";
   - a plain-words key.

   That K–1 sustains this is a prediction.
2. **should**, headers of pp. 1–3, band views. Guide p. 2 sends both older tables through P1–3 first ("print students pp1–3 per older pair"). But pp. 1–3 say "Grades 2–3", so the 4–5 slice and menu (pp. 1, 4–6) skip the four-exit tree. Head pp. 1–3 "Grades 2–5", update the page index and rebuild the views. Reconcile "continue to P4–6 on another visit" with "Add students pp4–5 … for ready groups".
3. **should**, p. 4, P4. "H D F B G C E A" and "A E B F C G D H" sit 1.9 mm under the tree above and far left of their own roots, so each reads as the wrong tree's caption (math check 4). Move each down about 10 mm, level with its root.
4. **should**, p. 5, P5. It is thin after P4: ABCDEFGH with P3's root reason answers it, as do 40,192 of the 40,320 orders. Replace it with "How many different arrival orders can the eight-exit tree make? Explain why." The answer is 128, one per start. The guide's P4 key has the reason.
5. **should**, guide p. 3: "DABC is impossible for a deeper reason." It is the same root rule one step later, since A and B arrive together, both on the left (math check 3). "Deeper" hides the single rule the share should reach. Use the math check's wording.
6. **should** (companion; a must in the return packet's own pass), guide p. 5, return P4: "The first two output blocks are both 0004." They are 0040, as the guide's own P1 trace and my hand trace give. Add math check 2's sentence that cards change only during the first block.
7. **could**, p. 2, P2: one board under "Find every arrival order" tells the child there is exactly one more. Add a second, marked extra workspace.
8. **could**, guide p. 2: give a preparation time and a source for 48 counters no wider than 12 mm.
9. **could**, footers: use F91-S-v1, F91-RV-v1 and F91-M-v1, to match F91-FAC-v1.
10. **could**, guide pp. 1–2 and 6: cut production notes such as "no multi-level coverage is implied".
11. **could**, guide p. 4: name AECGBFDH as the bit-reversal order.

October 23, 2026: fixes 1–6 and 9–11 made in the problem files and the guide; coulds 7 and 8 deferred; see `source/week-91/editable/review/card-fixes-2026-10-23.md`.

October 23, 2026, later the same day: coulds 7 and 8 made. Problem 2's second question has two boards side by side, the second marked "Extra workspace: arrival order" (F91-S-v2; the other pages changed only in their footers). The guide's kit section gives 1 cm base-ten unit cubes as an example counter and about an hour to prepare three kits, marked as an estimate not yet timed (F91-FAC-v3). Band views rebuilt. Unpiloted.

## Overlaps

Week 11's chip firing sends a chip along every edge, with order independence; here one chip follows one remembered edge, with block balance. On a path, Week 20's averaging values are the s/m that return P5 delivers exactly. Week 42 contrasts with P7. No merge; cross-reference all three.

## App fit

Not in themes.md. I propose Fit B, size M.

- **Program an order.** Tap switches to set the starting arrows, then Send. Cards flip on screen, enforcing the rule. Make a named order (P3, P4); on the eight-exit tree each has one start.
- **Find every.** Every D-first start, judged by That's all (P2).
- **Can't.** The certificate is a tap on one switch and the two letters that would leave it the same way on consecutive visits (A, B at the root in ABCD; at the left child in AEBFCGDH).
- **Roads.** A later group with exit targets (return P2–P3). Its "can't" certificate is the live score.
- **Avoid.** Auto-runs that the child only watches, and P6-style coverage prediction. Require the whole start before the first Send, so the eight four-exit starts cannot be brute-forced.

## Classroom evidence

None reported.
