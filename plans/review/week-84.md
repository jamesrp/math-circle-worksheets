# Week 84: Public knowledge

**Verdict: revise.** The mathematics, problems and cards are right, and every answer checks. One must: Problem 3's "the same three replies" has a second reading whose right answer is no, and the key gives only yes.

Reviewed October 23, 2026 by Claude, reconciled from two independent card runs, with the math check in [week-84-math.md](week-84-math.md) and `second_card_checks.py` in [checks/week-84/](checks/week-84/). A first run, kept as [checks/week-84/card-first-run.md](checks/week-84/card-first-run.md), rated fix 1 a should and the week keep, because the reply slots and Problem 2 favour the doll-by-doll reading; it is a must here for the same reason as in Weeks 39 and 43, where a second reading the key rejects would lead an adult to correct a child who reasoned rightly. Packet: week-84-students.pdf (W84-PK-draft-v2, 8 pp.: P1–P4 on pp. 1–3, cards and labels on pp. 4–8; one Grades 2–5 packet; the band menu gives K–1 nothing). Adult guide: week-84-facilitator.pdf (5 pp.). Companions noticed but not reviewed: the guide's number grid and encore. Status: unpiloted, a draft awaiting the organizer's first review. I agree with math.md's three findings but rate its item 1 must, not minor.

## The mathematics

A person knows something when every remaining possibility that fits their private view agrees on it. In the café a first NOT YET proves a YES card, and after the first NO, later answers reveal nothing (P1: 1, 4, 2 and 1 deals fit). With "at least one headband is blue", k blue dolls first prove blue in round k (P2), and onlookers pin down every deal by round 2 (P3). Without the announcement no card is ever removed and no doll proves, though with two or three blues every doll already sees a blue (P4). This is the muddy-children puzzle on eight cards; a mathematician would enjoy it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Possible worlds, silence as evidence, a fixed point without the announcement. |
| Problems | strong | Four contrasting transcripts; k = 1, 2, 3; all seven deals; one sharp contrast. Each is minutes of work; the order carries the induction. |
| Student pages | adequate | Spec header and footer, rules once, worked examples, no slop, large lettered cards. Fixes 1, 3, 5. |
| Concreteness | adequate | Cards hold every world; face-down replies in p. 8's slots enforce simultaneity. Fixes 2, 4. |
| Correctness | strong | math.md's 58 checks pass; card_checks.py agrees. Fixes 6, 8. |
| Adult guide | adequate | Theorem-first with hypotheses, launch, timing, staffing, every key, an observation record. Fixes 6, 7. |
| Age fit, K–1 | weak | No route, by design ("No K–1 edition", outline). |
| Age fit, grades 2–3 | adequate | No arithmetic; an adult reads. Deal 2's first removal needs 21 private-view checks (7 cards × 3 dolls); prediction: the adult runs it. |
| Age fit, grades 4–5 | strong | Cards carry the bookkeeping; P3 and P4 are real work for the quickest. |

## Keep

- P1's transcripts, exactly the four possible conversations; p. 1's Before / Heard / After example.
- p. 2's "A doll shows PROVE BLUE only when every possible arrangement matching what it sees gives it a blue headband."
- One unchanged shared set per round, replies revealed together, p. 8's doll slots; P2's three deals, P3, P4 and all sixteen possibility cards.
- Guide: "The all-worlds check, not a child's confidence or delay, establishes a declaration"; the BBR private views; the warning against removing cards doll by doll.

## Fix

1. **must**, p. 3, P3: "Put deals into groups that give the same three replies in round 1." Read as which replies appear, BRR, RBR and RRB give one PROVE BLUE and two NOT YETs in every round, and BBR, BRB and RBB never separate, so the answer is no (math.md item 1). Guide p. 3 says "the three one-blue configurations have distinct response patterns", so an adult would correct a child who reasoned rightly, as on the Week 39 and 43 cards. Fix: "Put deals into groups in which each doll gives the same reply in round 1." Guide p. 3: "Accept no from a child comparing only which replies appear, then ask whether onlookers see which doll proved."
2. **should**, p. 2 and guide p. 2: "Then remove arrangements that could not give those replies" is the central action, but the example stops at one private match and the launch gives no instance. Fix: make the example a two-doll round, actual RB: doll 1 sees B, matches BB and RB, NOT YET; doll 2 sees R, matches RB, PROVE BLUE; remove BB and BR (card_checks.py). Launch on it.
3. **should**, p. 2: "A doll's matching cards are a temporary private view. Leave the shared set unchanged…" New words before use. Fix: "Choose all three replies from the cards on the table, without removing any. Show them together. Then remove every card that would have given different replies."
4. **should**, guide p. 2: the coach sees the doll's own headband, on the doll and in P2's deal box, so in BBR a child may show PROVE BLUE for doll 1 in round 1 (prediction; the lamp failure in context.md). Fix: "While coaching doll k, cover its headband and its disk in the deal box, and position k on each card."
5. **should**, P2: the deal boxes leave 0.75 in under the numbers for up to nine replies; 3.4 in of the page is blank. Fix: boxes 3 in taller, without rows, which would give away BBB's three rounds.
6. **should**, guide p. 1: "Later NO need not mean the later speaker personally says NO" contradicts itself (math.md item 3), and the overview omits P4's fact and the discovery. Fix: "…the later speaker's own card is NO." Add: "Without the announcement no doll ever proves (P4). With two or more blues every doll already saw a blue; what changes is that everyone heard it, so silence becomes evidence."
7. **should**, guide: no hints or prerequisites. Fix: "No arithmetic; an adult reads; one doll's matches against one shared set." Hints: "Which matching card gives your doll red?"; "On this card, what would doll 1 have shown?"
8. **should**, guide p. 2: "reply cards (pages 6–7)", but p. 6 holds café cards and headbands, p. 7 has one NO where Conversation 2 has three (math.md item 2), and no set count. Fix: "café cards and headbands (page 6), reply cards (page 7); café replies are spoken; one set of pages 4–8 per pair."
9. **should**, K–1: no route; deliberate, so a should, as on the Weeks 79–83 cards. Fix in the guide: two children play the two-person café with p. 6 cards, then sort the four two-person deals by conversation (YY; YN; NY and NN). Prediction.
10. **could**, p. 1: "Your card says whether you want a cup"; "when your card and earlier answers settle it".
11. **could**, P1: "Make every YES/NO deal" reads as making cards; "Find every deal card".
12. **could**, pp. 1–2: the captions narrate the examples; shorten to "With two people:" and "With two dolls:".
13. **could**, 4–5 return visit: four blue dolls prove in round 4, BBBR in round 3 (card_checks.py); ask why.
14. **could**, guide: mark p. 6's café cards (no problem uses them) and the dolls (P2 prints the deals) optional; match "Grades 3–5 coach dolls" to the packet's Grades 2–5; drop p. 5's repeated Oxford title.

Fixed October 23, 2026 (packet W84-PK-draft-v3, problem files): the must, shoulds 2–9 and coulds 10–14. Problem 3 reads "in which each doll gives the same reply in round 1"; the deal boxes grew 7 cm, the space the page had.

## Overlaps

Weeks 5, 6, 45 and 94 also keep the possibilities that fit clues, answers or reports, but none has private views or public announcements. No merge; this fits after Week 5 or 45.

## App fit

Proposed B, size M. themes.md has no row; it should read: | 84 | Public knowledge | Find the deals that fit a café conversation; coach dolls round by round, removing possibility cards | Knowing means every remaining world agrees; k blues prove in round k; no announcement, no proof | No | B | Tap the fitting deals; choose each doll's reply with its own hat hidden; remove the cards the replies rule out | M |

The screen hides a doll's own position, which paper cannot. The solve is the removal: a wrong removal, or a card wrongly kept, is refused with the replies that card would give. Café: tap every fitting deal and declare done, with no counter; design a conversation fitting exactly two deals. Four dolls and "at least two are blue" vary it; P4's unchanged set certifies "can't". Avoid "which round will they prove?" and automatic removal. Draw on all four problems.

## Classroom evidence

None reported. The source README says "All activities are unpiloted"; the October 9 workflow stages are not classroom evidence.
