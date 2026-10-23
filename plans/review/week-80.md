# Week 80: Midnight laboratory

**Verdict: keep.** There is no must: every printed fact is right, every problem has its board, and the guide opens with the theorem. The fixes are a thin Grades 2–3 route, a leading clause in Problem 2 and a gap in the guide's endpoint notes.

Reviewed October 17, 2026 by Claude, with the math check in math.md. Packets: week-80-students.pdf (M80-D-v1, 5 pp.: Grades 2–5 P1–P2 on pp. 1–2, Grades 4–5 P3–P5 on pp. 3–4, and a cut-out page with two strips and the ON/OFF panels). Adult guide: week-80-facilitator.pdf (4 pp.). Companions noticed but not reviewed: none printed; guide p. 4 has a one-paragraph encore. Status: unpiloted. The organizer directed the October 15 revision and approved the packet on October 17, which is review, not piloting. The card agrees with both math-check findings, rating item 1 a should and item 2 a could. My checks are in card_checks.py.

## The mathematics

Switches come at 11:30, 11:45, 11:52:30 and so on, at times 1 − 2⁻ⁿ of the hour, so there is no last one (P1). The card alternates and has no limit, while a counter that halves its gap to END at the same marks converges (P2). The rule fixes the state only before midnight, so ON and OFF both fit at midnight and neither follows (P3–P4). "Use the state the earlier states approach" decides the counter but not the card (P5). This is Thomson's lamp, with Benacerraf's answer and a convergent control. A mathematician would enjoy the conversation, but each fact is met once, on one process.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | adequate | A classic paradox, all correct. There is one case of each fact and nothing for children to vary or build. |
| Problems | adequate | The order carries it, from marks and flips to the endpoint and the limit rule; P5 is the sharpest question. P1–P2 are four folds and a few flips, and P2's counter retraces P1's marks (fix 1). |
| Student pages | strong | Spec header and footer, a short story as the shared rule, and an Input / Fold / Unfold visual on a gap the rule already gives. No hints or slop, and the boards are empty. One leading clause (fix 2). |
| Concreteness | adequate | The fold makes halfway exact, the card has only two sides, a partner witnesses each flip, and guide p. 2's launch shows a fold and a flip. P3–P5 give nothing to act on or check. |
| Correctness | strong | Every printed fact, answer and diagram is right (math.md; my replays agree). |
| Adult guide | adequate | Theorem-first overview with assumptions and a band map; launch, route and keys. Gaps: fixes 1, 3 and 11. |
| Age fit, K–1 | weak | No route, by design ("No K–1 edition", outline). |
| Age fit, grades 2–3 | adequate | An adult reads, and no arithmetic or clock reading is needed. In P2, partners share the marks, the card and the counter. Prediction: a quick pair finishes the actions in P1–P2 in 15 minutes. |
| Age fit, grades 4–5 | adequate | P3–P5 are the right questions for the organizer's table. They are talk, and P4 largely answers P3. |

## Keep

- p. 1: the organizer's light story and the fold visual, which shows the action without answering anything.
- P1's "Can the rule have a last switching mark before midnight?" P2's card beside a counter. P3's "What, if anything". P4's empty "At midnight:" boxes. P5's added rule.
- Four physical marks (the last gap is 11.25 mm). Strips 180 mm long throughout. ON and OFF panels glued back to back. A separate START–END strip.
- Guide: the overview; "Do not offer 'half on' as an endpoint deduction or treat infinity as an even/odd integer."; "Let children act before naming limits."; the odd/even subsequence argument.

## Fix

1. **should**, Grades 2–3, pp. 1–2 and guide p. 2. The band gets two problems (spec: "four or more pages per band"), and its one contrast is a counter that retraces the time marks. The route says "for Grades 2–3 use Problems 1–2 only" but then times "five minutes considering extra endpoint rules", which is P4. Pages 3–4 say "Grades 4–5" where the guide says "a Grades 3–5 continuation". Fix: after p. 2, add a Grades 2–5 page that turns the guide's encore into a problem: "Problem 3: Use the same switching marks. Make up a flipping rule for a second card that does settle on one side. Make up a moving rule for the counter that does not get closer and closer to one place." Renumber P3–P5 as P4–P6. Key: flip only at the first two marks; jump end to end. Richer: flipping at every second mark never settles; halfway toward END on ON and toward START on OFF swings between about 60 and 120 mm (card_checks.py). The route becomes "Problems 1–3", and the continuation gets one band label.
2. **should**, p. 2, P2: "What place does the counter approach?" The card's question is open, but this one assumes its answer. Fix: "Does the counter get closer and closer to one place?"
3. **should**, guide p. 3, "Problems 3–4" (math.md item 1). Children are likely to propose "flip once more at midnight" or "stay as it was". Both need a last state before midnight, and there is none. The guide covers only ON, OFF and "undefined", so an adult may accept one of these as a third consistent rule. Fix: add math.md's sentence, which says such a rule "does not choose a side; this is the same obstacle Problem 5 meets", and state P3's answer there: ON and OFF both fit.
4. **should**, K–1, guide: there is no route for the K–1 table. This is a should, as on the Week 76 and 79 cards, because the selected-band design is deliberate. Prediction: P1's fold and flip need no reading.
5. **could**, p. 3: the MIDNIGHT box is 66 × 53 mm and the card is 76 × 54 mm (math.md item 2). Draw the box at 80 × 58 mm.
6. **could**, p. 1: P1 says "on a paper strip" above a printed line; the guide could say to copy the folded marks onto it.
7. **could**, P3: drop "Use the card and switching marks to support your answer."
8. **could**, P4: "Keep every switch before midnight." can read as an order to move switches. Write "The switches before midnight stay the same."
9. **could**, guide p. 2: name a counter at most 15 mm across, list scissors and glue, and show one counter move in the launch.
10. **could**, guide p. 3: "six drawings" should say four.
11. **could**, guide pp. 3–4: cut the author-facing lines ("Do not provide those prompts after every small action on student pages", "not the old paper network-toggle rule", "(part0017)").
12. **could**, the guide header still reads "Facilitator draft".

October 23, 2026: shoulds 1–4 and coulds 5–12 fixed in v2 (M80-D-v2), after the organizer's October 17 approval; the K–1 route is a guide paragraph on pages 1 and 6, and the continuation is labelled Grades 4–5. Checks in the package's `check_card_fixes.py`.

**Critic follow-up, October 23, 2026 (M80-FAC-v2):** an independent critic's two shoulds are made. Problem 3's key now rules on a counter that stops moving: it has settled, like the card that never flips, so ask for a rule that keeps it moving at every mark but never settles. The guide's footer, which had no version id, reads M80-FAC-v2, so it can be told apart from the approved guide. The band-view menu and a K–1 slice now list the K–1 route's pages 1 and 6. The student packet did not change; v2 is still not re-approved. Unpiloted.

## Overlaps

Week 79 compares counts with a set-valued limit in the same supertask setting; Week 81 has plays that all end with no common bound; in Week 50 the limit of the lengths is not the length of the limit. None asks what an endpoint is. No merge: Weeks 79, 80 and 81 form a return sequence, and 80 is the simplest entry.

## App fit

Proposed C, not porting; themes.md has no row. It should read: | 80 | Midnight laboratory | Fold a strip to mark switches halfway to midnight; flip an ON/OFF card at each; move a counter halfway to END; ask what the rule says at midnight | Switch times 1 − 2⁻ⁿ have no last one; the card alternates with no limit while the counter converges to END; the rule before midnight leaves midnight open, and "use the limit" decides the counter but not the card | No | C | None: the rule makes every move, so a screen only plays switches to watch, and midnight is never on the board | S |

A port would give children no real solve. The rule makes every move, so a faithful port has one button, Next switch. The child watches the card flip and the counter creep, or predicts the card after switch 7, the mode children enjoyed least. The theorem is about midnight, which no finite board reaches. "No last switch", "the card never settles" and "the rule doesn't decide midnight" become yes/no taps that the app can only mark, the one-bit oracle port-common.md rules out. P3–P5 are a conversation about infinity and conventions, and that conversation is the week's substance. It belongs on paper with an adult.

Were it ported, it would be new substance, since no family teaches limits. It is not a group for Lantern Wires: there, and in its Lamplighter group, the child flips lamps toward a target, while here the rule does the flipping.

The only variant with a choice sends each move halfway toward START or toward END, to land on a target mark. That is a real solve, but every target k/2ⁿ has exactly one sequence: the binary digits of k, read backwards (card_checks.py, every n ≤ 10). So the solve repeats after a puzzle or two, as Week 73's and Week 79's did. It teaches binary addresses, which Week 6's yes/no questions already carry in Signal Lanterns, and the infinity is gone. Recommendation: not porting; no problem to draw on.

**Decision, October 17, 2026.** Not porting. The rule makes every move, so a screen version would have one button, Next switch, and children could only watch the card flip and the counter creep or predict what comes next, the mode the app avoids. The theorem is about midnight, which no finite board reaches: that there is no last switch, that the card never settles and that the rule leaves midnight open would become yes/no taps the app can only mark. The one variant with a choice (move halfway toward START or END to land on a mark) has exactly one sequence for each target, the binary digits read backwards, so it repeats after a puzzle or two, as Week 73's and Week 79's did, and it drops the infinity. The week's substance is the fold, the flips and the conversation about midnight, which the worksheet keeps. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. The organizer asked for the October 15 revision (start from the light at 11:00, 11:30 and 11:45, introduce the card model afterward, and keep the endpoint distinction) and approved the packet on October 17 after reading it. No session has used it. The source README says: "All activities are unpiloted; physical fit, actual-size printing, timing and classroom procedures have not been rehearsed."
