# Week 138 (draft plan): Tiny machines and the busy beaver

**Strand:** logic (Codes and logic), touching chance and machines. **Deep-math field:** computability theory. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A Turing machine with n states and two symbols is a rule card: for each state and each symbol read (0 or 1), it says what to write, which way to step, and which state to go to next, or to stop. Started on a blank tape, a card either stops after some number of steps or runs forever. Radó (1962) defined BB(n), the most steps any n-state card takes among those that stop, and Σ(n), the most 1s left on the tape. Proved values: BB(1) = 1, BB(2) = 6 (with Σ(2) = 4), BB(3) = 21 (Lin and Radó, 1965), BB(4) = 107 (Brady: machine 1966, proof 1974), and BB(5) = 47,176,870, proved in 2024 by the online Busy Beaver Challenge, with a Coq proof checked by computer. BB(6) is unknown: its known lower bound already exceeds 2↑↑↑5, and a six-state card called Antihydra almost certainly never stops but proving so is tied to a Collatz-like open problem (Quanta, 2025). Some single values are out of reach of ordinary mathematics: assuming the axioms of set theory (ZF) are consistent, ZF cannot prove the value of BB(748) (Aaronson's survey, citing O'Rear's 748-state machine). Two theorems explain why: BB eventually exceeds every computable function (a machine that computed a faster function could be used to out-run itself), and there is no general method to tell whether a card stops (Turing's halting problem). Every proof of a BB value is a proof, card by card, that the long runners really never stop. Children can discover the finite fact behind the game: with two states there are only 6561 cards, any card that stops does so within 6 steps, and therefore a two-state card that has run 7 steps will never stop. That "past the record means forever" reasoning is how BB values are used; settling BB(5) meant proving, for every five-state card that had not stopped, that it never would.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Busy Beaver Frontier](https://scottaaronson.com/bb.pdf) — Scott Aaronson, survey (data as of July 2020) (read November 3, 2026). Radó's 1962 definition, the table BB(1..4) = 1, 6, 21, 107 and Σ(1..4) = 1, 4, 6, 13, the BB(2) champion card, the proof that BB outgrows every computable function, the ZF-independence of BB(748).
- [With Fifth Busy Beaver, Researchers Approach Computation's Limits](https://quantamagazine.org/amateur-mathematicians-find-fifth-busy-beaver-turing-machine-20240702) — Ben Brubaker, Quanta Magazine, July 2, 2024 (read November 3, 2026). History of BB(3) (Lin, 1965) and BB(4) (Brady, 1966 and 1974), the 2022 founding of the Busy Beaver Challenge, the roughly 40,000-line Coq proof, the halting problem link.
- [Busy Beaver Hunters Reach Numbers That Overwhelm Ordinary Math](https://www.quantamagazine.org/busy-beaver-hunters-reach-numbers-that-overwhelm-ordinary-math-20250822/) — Ben Brubaker, Quanta Magazine, August 22, 2025 (read November 3, 2026). BB(6) unknown; a lower bound above 2↑↑↑5 (June 2025); the Antihydra card and its link to a Collatz-like question.
- [BB(5) = 47,176,870](https://discuss.bbchallenge.org/t/july-2nd-2024-we-have-proved-bb-5-47-176-870/237) — bbchallenge announcement, July 2, 2024 (read November 3, 2026). The value and that the proof was formalised in Coq and reviewed.
- Prior use with children: [Grade 7/8 Math Circles, Turing Machines](https://cemc.uwaterloo.ca/sites/default/files/documents/2024/Junior78_TuringMachine_Apr7.pdf) — CEMC, University of Waterloo, 2024 (read November 3, 2026). Students trace state tables on a tape of squares; no busy beaver content. Searches for busy beaver or Turing machine activities with K–5 children ("busy beaver math circle handout", "Turing machine unplugged primary school cups") found none.

## A kid-friendly way in

Be the machine. A tape is a row of 15 to 20 paper cups (or squares on a long strip of paper), all empty; a 1 is a counter in a cup. The "head" is a small toy standing in front of one cup. The state is a coloured card the head holds (red A, blue B). A rule card is a 2-by-2 table with pictures: for red-reading-empty, red-reading-counter, blue-reading-empty, blue-reading-counter, it shows "put or take a counter", an arrow left or right, and the next colour, or a STOP sign. Prep: print and laminate 6 blank rule cards and 3 filled ones, gather cups and counters; about 20 minutes. Launch (3 minutes): run the champion card (A0 1RB, A1 1LB, B0 1LA, B1 stop) with the whole group calling out each move; it stops after 6 steps with 4 counters. Then: can your table write a card that runs longer and still stops?

## By band

- **K–1:** Run filled cards with an adult reading colours, counting steps on a tally strip. Sort cards into "stops" and "goes forever" and notice the simplest forever card: it keeps walking right over empty cups. Reading: none; arrows and colours only.
- **2–3:** Design two-colour cards. Who can make a card that stops after the most steps? Which leaves the most counters? Tables pool their records on a class chart. Children meet the record of 6 steps and 4 counters and start to suspect it cannot be beaten. When a card runs 7 steps, the facilitator can reveal that it will never stop; children check by finding a repeating pattern.
- **4–5:** Three colours. Run the 21-step card (A0 1RB, A1 stop; B0 1LB, B1 0RC; C0 1LC, C1 1LA) and try to beat it. Then the explanation question: given a card that has not stopped, can you prove it never will? Children write short "forever proofs" (it keeps moving right on empty cups; it bounces between two cups forever). Discuss honestly that for some cards nobody knows how to write such a proof, and that this is what makes BB grow so fast.

## Checked facts

All in `check_logic.py`, function `check_week_138()` (convention: the stopping move counts as a step and writes a counter):
- The champion two-state card runs 6 steps and leaves 4 counters.
- One state: 25 cards, 5 stop, each after 1 step.
- Two states: 9 choices per box, 9^4 = 6561 cards; 1165 stop, with step counts 1:729, 2:324, 3:72, 4:26, 5:4, 6:10; so only 10 cards reach 6 steps and none leaves more than 4 counters. Since BB(2) = 6, a run cap of 50 is safe.
- Three states: 13^6 = 4,826,809 cards. Up to mirror image and renaming states, every card worth trying starts A0 → (write, right, B); among those that stop within 30 steps the longest run is 21 and the most counters is 6, consistent with BB(3) = 21 and Σ(3) = 6 (this is a consistency check, not a proof; the proof is Lin and Radó's). The 21-step card above leaves 5 counters.
- Brady's four-state card (A0 1RB, A1 1LB, B0 1LA, B1 0LC, C0 stop, C1 1LD, D0 1RD, D1 0RA) runs 107 steps and leaves 13 counters.
- A card with A0 → (1, right, A) never stops (checked to 10,000 steps; the proof is that it always reads an empty cup).
- Cited, not computed: BB(5) = 47,176,870 (bbchallenge, Quanta 2024); BB(6) lower bound and Antihydra (Quanta 2025); BB(748) independence and growth beyond computable functions (Aaronson).

## Nearest existing themes

Week 17 (Machine memory) uses finite machines that only read; a Turing machine also writes and moves both ways, which is what makes stopping undecidable. Atlas AD-02 (the diagonal argument with four counters) is the other half of the same story: Turing's halting proof is a diagonal argument, and a 4–5 return visit could connect them. Week 72 (A robot that remembers area) has a robot with a memory strip but a fixed instruction sequence. Week 91 (Rotor-router machines) and Week 11 (Chip-firing) prove that particular processes stop; here the point is that no single method can. New: the halting question, a function that is proved to exist but cannot be computed, and the "record means forever" argument.

## App connection

Chance and machines region (or Codes and logic), possible family "Busy beavers": a tape of cups along the bottom of the board, a rule card the child fills by tapping arrows, colours and stop signs, and a Run button that animates the head. Puzzles: "Make a two-colour card that stops after exactly 5 steps"; "Make a card that leaves 4 counters"; "This card has run 7 steps. Will it stop?" (answer forever, with the record shown). The app can check any two-state card instantly since there are only 6561. Card machines (Week 17) could share the rule-card editor.

## Open questions

- Material fit: does a toy head plus cups stay readable for 21 steps, or do children lose track of the state? A state "hat" or a colour clip on the head may help. Rehearse the 21-step card once.
- Age fit for 2–3: designing a card means filling four boxes with three choices each; is that too many simultaneous decisions? A half-filled card may be a better start.
- Which counting convention (stop move counts as a step) to print; it must match the sources' 6 and 21 or the records will confuse adults.
- Whether to show BB(5) as a number at all; it is a story, not something children can check.
