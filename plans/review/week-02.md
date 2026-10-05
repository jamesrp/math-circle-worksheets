# Week 2: Switches and lamps

**Verdict: revise.** The mathematics and both problem sets are right, and the upper catalog is at the bar. Two musts lie outside the problems: the compact catalog gives no board on which a printed ON lamp can be turned OFF, and it has no current adult guide.

Reviewed October 5, 2026 by Claude, blind (calibration round 3), with the math check in [week-02-math.md](week-02-math.md); classroom evidence added afterwards, and two ratings adjusted (see [calibration.md](calibration.md)). Packets: week-02-shared-catalog.pdf (F02-S-CAT-v2, 4 pp.) and week-02-shared-catalog-upper.pdf (F02-S-CAT-UP-v1, 6 pp.). Adult guide: plans/week-02-catalog-upper.md; for the compact catalog, only the archived F02-S-FAC-v1 (old P2, P5–P13). Companions noticed but not reviewed: return visit F02-R-v1, bonus F02-BONUS-v1, the archived 42-page collection. Status: a paper lamp session went poorly, and the record does not say which pages it used; the organizer still counts the week as good (see Classroom evidence). The source README marks the upper catalog unpiloted.

## The mathematics

A press flips both lamps at the ends of one line. Children can reach five results. A target can be made exactly when every connected piece has an even number of changed lamps (upper P1–2, compact P8–9). A path changes only its ends (compact P2–5). On a ring the solutions are one set and its complement, so the hardest target needs ⌊n/2⌋ presses (upper P3, P5). Graph lower bounds beat simple counting (upper P4). A tree has at most one solution (upper P6). A mathematician would enjoy this. The compact catalog reaches only paths and the islands.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Each result has a proof children can show with objects. |
| Problems | strong | Upper: 4–6 contrasting cases per question, and the order carries the argument. These catalogs set the bar for this rating. Compact P2, P3 and P5 are each one short route, and all 18 targets in P1–7 can be made (fixes 6 and 9). |
| Student pages | strong | These catalogs set the bar: one-line prompts, no hints, cases rather than sub-steps, regular polygons. The compact catalog lacks working boards (fix 1), and P9's "islands" and "trip" are undefined (fix 7). |
| Concreteness | weak | Pencil dots on 5.6 mm lamps. Compact P2, P3, P4 and P8 and 14 of the 26 upper cases start with printed dots. Nothing enforces the pair and no record survives, so a one-lamp change "solves" P8 or upper 1C unnoticed. context.md asks that materials or a partner enforce rules. The upper launch is good; the compact catalog has none. |
| Correctness | strong | The math check finds no wrong answer in 45 pairs. My BFS agrees: upper minima 2, 4, 3, 5, 4, 4; ring records 2, 3, 3, 4; tree counts 1, 1, 0, 1. |
| Adult guide | weak | Compact: none current (fix 2). Upper notes: full answers, bounds, proofs and launch, but no theorem-first overview. |
| Age fit, K–1 | weak | Each problem is one sentence an adult reads aloud, with no arithmetic. But P2's first move erases a printed dot, the parent has no matching guide, and no connected board has an impossible target. |
| Age fit, grades 2–3 | adequate | Compact P1–7 go quickly. Upper P1, P2 and P4 suit third graders on a whiteboard copy, though they track several lamps and a count. |
| Age fit, grades 4–5 | strong | The upper catalog with whiteboards and the organizer. Recording sets of lines is the main load (fix 5). |

## Keep

- Upper, the whole sequence: P1B and P1D go odd to odd, defeating "targets need an even count"; P2B and P2C differ only by a bridge; P2E has an even total yet is impossible; P4A and P4B share a graph and changed count but have minima 2 and 4; P5 asks for the hardest target; P6C is impossible on a tree.
- Compact: the rule sentence and arrow; P4 against P5 (one route, two starts); P8 then P9; P10.
- The upper notes' P4 bounds and proofs; the archived guide's answers and trio roles.

## Fix

1. **must**, compact, all pages, especially P2, P3, P4 and P8. This is the recorded failure (see Classroom evidence): the page says "add a dot or erase a dot", but these starts carry printed dots, and most lamps are 5.6 mm across. The only guide says "The printed working boards are blank", which is false here. Fix: one blank board per graph (square, six-ring, tree, 3×3 grid, islands), lamps about 2 cm, labelled extra workspace, with two-sided counters. The small pictures become start and target cards. Guide: one child points to a line and the partner flips both counters, as F02-R-v1 already does.
2. **must**, compact: no adult guide. F02-S-FAC-v1 uses old numbers, describes missing boards and assumes the dropped one-light rule. Its promise "Reversing the moves always succeeds" fails for P10 (math check, item 4). Fix: a short guide keyed to P1–10 with a theorem-first overview, a shared launch (press, press again to undo, one target), the old answers renumbered, a test for invented puzzles (an even number of changed lamps per island), and a decision on the one-light rule for P2–4 (math check, item 5).
3. **should**, the root README, the year-2 index and source/week-02/README.md link week-02-shared.pdf and week-02-shared-facilitator.pdf, which now sit in archive-before-deslopping/. The index omits the upper catalog. Fix: point all three to the catalogs and their guides.
4. **should**, plans/week-02-catalog-upper.md: no theorem-first overview. Fix: open with the five results, their assumptions and a band map.
5. **should**, upper P3 and P6 ("Find every set of lines"): nowhere to mark a set, and two solutions need two copies. Fix: unlit copies as extra workspace, more than any answer needs.
6. **should**, compact P6: no connected board has an impossible target, so K–1 never meets parity. Fix: add one odd target (all OFF → one lamp ON) and write "Make each target picture or explain why it can't be done."
7. **should**, compact P9: "Try the trip with your bridge" uses words P8 never introduces, and the bridge must go on P8's used pictures. P8's start and target sit closer together than its two islands do, so children may bridge start to target (a prediction). Fix: give P9 its own pair, write "Draw ONE new line from the left island to the right island. Then make the target picture.", and box each state in P8.
8. **should**, upper notes §3: "a different first line" can be met by reordering (math check, item 3). Use the math check's wording.
9. **could**, compact P2, P3 and P5 could become one walking-light problem.
10. **could**, upper notes §3 and §6: warn adults that children may not count "press nothing" in 3A and 6D.
11. **could**, upper notes §6: "upper/lower branch point" names two lamps at the same height (math check, item 1).
12. **could**, the upper catalog's header could say it is the upper set.

Where I differ from the math check: its point 2 is a could, since the notes say "Choosing no lines is allowed"; P9 is a should, not just layout; and it does not check the boards.

## Overlaps

Weeks 46 (toggle boards), 25 (uniqueness, as on trees), 10 (odd junctions), 53 (tree cuts) and 39 (cancelling repeats) share pieces only. Neither side should absorb the other.

## App fit

A, confirmed: Lantern Wires has shipped, and tapping a wire enforces the rule paper cannot. The solve is the target. The certificate for "can't" is an island with an odd number of mismatched lamps. The certificate for "best" is a set of changed lamps no wire joins (upper 4B, 4F), or a cut (4D). For "find every set", the child declares done; show no slots. Author impossible cases against "even total" (2E) and "even target" (1B, 1D). Draw on upper P2, P4–P6 and compact P8–9 (add one wire), after checking what the 42 shipped puzzles cover.

## Classroom evidence

- **On paper, observed.** A session on paper lamp puzzles went poorly ([context.md](../../worksheet-workflow/context.md), updated October 3, 2026). The rule lived only on paper, children kept changing just the lamp they wanted without noticing, and many could not tell what they were being asked to do. The record does not say which Week 2 pages were used. This is the failure fix 1 addresses, and it is why Concreteness and K–1 are rated weak.
- **In the app, observed.** Lantern Wires, where a tap flips both lamps, is among the families children most enjoyed (the organizer's playtest notes of October 5, 2026, in the app repository's AGENTS.md). The same mathematics works once something enforces the rule.
- **The organizer's judgement.** On October 4 the organizer counted Week 2 among the weeks tested with children and good, and on October 5 explained: it went well in the app, paper was harder to enforce in a larger group, and the activity itself is good, especially app-mediated. That matches this card: keep the mathematics and the problems, and give the paper version something that enforces the rule (fix 1).
