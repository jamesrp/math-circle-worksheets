# Week 140 (draft plan): Proving without telling

**Strand:** logic (Codes and logic), with chance. **Deep-math field:** cryptography, interactive proofs, probability. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A zero-knowledge proof convinces a verifier that a statement is true while revealing nothing else. The idea was introduced by Goldwasser, Micali and Rackoff in the mid-1980s (credited in the GMW paper below). Goldreich, Micali and Wigderson (FOCS 1986, Journal of the ACM 1991) showed that every NP statement has such a proof, through a protocol for map colouring: the prover secretly re-colours a proper 3-colouring with a random shuffle of the three colours, covers every region, and the verifier picks one border and uncovers only its two regions. Three facts make it work. Completeness: an honest prover always passes. Soundness: if the map has no proper 3-colouring, every covered colouring has at least one bad border, so with m borders each round catches a cheater with chance at least 1/m, and k rounds let a cheater through with chance at most (1 − 1/m)^k. Zero knowledge: because the colours are shuffled each round, the two uncovered colours are just a random pair of different colours, which the verifier could have produced alone. The "proof" is therefore probabilistic: never certain, but as convincing as you like. Quisquater and Guillou's cave story (Crypto '89) is the same structure with one bit: a prover who knows the password through a ring-shaped cave can always come out the side the verifier calls; a bluffer passes each round with chance 1/2, so 20 rounds leave about one chance in a million. A related idea, Shamir's secret sharing (1979): hide a secret as the height at 0 of a line; give three people the heights at 1, 2 and 3. Any two can rebuild the line and the secret; with clock arithmetic one share alone fits every possible secret equally well, so it reveals nothing (proved). Children can discover why a single uncovered border reveals nothing, why a cheater survives one round but not many, and why two points of a line are enough and one is not.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [How to explain zero-knowledge protocols to your children](https://www.fermatslibrary.com/s/how-to-explain-zero-knowledge-protocols-to-your-children) — Jean-Jacques Quisquater and Louis Guillou, with Tom Berson, Advances in Cryptology (CRYPTO '89), LNCS 435, 1990 (read November 3, 2026). The cave story, coin-chosen exits, (1/2)^40 for 40 rounds.
- [Proofs That Yield Nothing But Their Validity or All Languages in NP Have Zero-Knowledge Proof Systems](https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Zero%20Knowledge/Proofs_That_Yield_Nothing_But_Their_Validity_or_All_Languages_in_NP_Have_Zero-Knowledge_Proof_Systems.pdf) — Oded Goldreich, Silvio Micali and Avi Wigderson, Journal of the ACM 38(1), 1991 (preliminary version FOCS 1986) (read November 3, 2026). The 3-colouring protocol with locked boxes, the 1/m catch bound per round, the shuffled pair argument.
- [How to Share a Secret](https://courses.csail.mit.edu/6.857/2017/files-2017/shamir.pdf) — Adi Shamir, Communications of the ACM 22(11), November 1979 (read November 3, 2026). The polynomial threshold scheme mod p and the proof that k − 1 shares leave the secret completely undetermined.
- Prior use with children: [Math Circle, Intermediate I, October 23, 2024](https://mathcircle.berkeley.edu/sites/default/files/handouts/2024/Math%20Circle%2C%20Intermediate%20I%2C%20October%2023rd%202024.pdf) — Berkeley Math Circle (read November 3, 2026). Graph colouring and zero-knowledge: a colour-blind verifier warm-up, the edge-checking protocol, the probability of catching a liar over k rounds, and why the verifier learns nothing. Middle-school level; no K–5 use found beyond the cave story's own framing.
- [Zero Knowledge Proofs: An illustrated primer](https://hn.jakechampion.name/reader/https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer) — Matthew Green, 2014, via a reader copy (read November 3, 2026). The hats-over-vertices version used here with cups; a facilitator-friendly explanation.

## A kid-friendly way in

Two acts. The cave: a ring of chairs with one gap closed by a curtain or a rope "door" that only opens for the password (an adult whispers it to the prover; the door-keeper adult checks it). The verifier waits outside the ring, the prover walks in on either side out of sight, and the verifier calls "left" or "right" by coin flip. The cups: a printed flower map (a centre region and petals) with paper cups covering each region and coloured counters under them. Prep: print maps, gather 6 cups and three colours of counters per table, a folder for a screen, a coin; about 15 minutes. Launch (3 minutes): run the cave twice with an honest prover, then once with a prover who does not know the password and gets lucky. Ask: how many times would you need to see it before you believed?

## By band

- **K–1:** Play the cave, with children taking turns as verifier and prover. Then a bluffer game: the bluffer guesses a side before the coin is flipped; how many rounds in a row can a bluffer survive? Children notice that one lucky round is common and five in a row is rare. No reading.
- **2–3:** The cup map. The prover colours the four-petal flower so neighbours differ, hides it, and the verifier lifts the two cups on one border. Then the prover re-colours by swapping colours behind the folder. Questions: what does the verifier learn from one lift? Can a prover who uses a bad colouring keep fooling you? Then the five-petal flower: try to colour it with three colours (it cannot be done) and play the cheater.
- **4–5:** Explain the three facts with the cups: why the honest prover always passes; why a cheater on the five-petal flower (10 borders) is caught at least 1 time in 10 per round and how many rounds bring the cheater's chance below a half and below 1 in 100; why every lift on the four-petal flower, over the six colour shuffles, shows each pair of different colours equally often. Extension: secret sharing on grid paper; three children each get one point of a line, any two find where it crosses the left edge.

## Checked facts

All in `check_logic.py`, function `check_week_140()`:
- Cave: (1/2)^10 = 1/1024; 2^20 = 1,048,576; 7 rounds bring a bluffer below 1 in 100.
- Flowers (centre plus r petals): r = 4 has 8 borders and a proper 3-colouring; r = 5 has 10 borders and none; r = 6 has 12 borders and one. The five-petal flower can be 3-coloured with exactly one bad border, so a cheater's best is caught with chance 1/10 per round: 7 rounds to fall below a half, 44 rounds below 1 in 100.
- Four regions all touching (a centre with three around it): 6 borders, needs four colours, best cheat has one bad border; 4 rounds below a half, 26 below 1 in 100.
- The four-petal flower has exactly 6 proper 3-colourings, the 6 shuffles of one; across the shuffles every border shows each of the 6 ordered pairs of different colours exactly once.
- Secret sharing on an 11-hour clock: each single share fits all 11 secrets exactly once; any two of the shares at 1, 2, 3 determine the line. With ordinary numbers it leaks: secret 0–9 and step 1–3 with share 3 at position 1 leaves only 0, 1, 2. Paper example: secret 4, step 3, shares 7, 10, 13; any two give 4.
- Cited, not computed: the NP-wide theorem (GMW), the original cave (Quisquater et al.), Shamir's general k-of-n scheme.

## Nearest existing themes

Week 84 (Public knowledge) is about what each person can deduce; here the design goal is that the verifier gains certainty about one fact and nothing else, a new move. Week 62 (Conflict networks) uses the same proper colourings and the odd-ring obstruction; this week deliberately reuses the flower maps (an odd ring of petals around a centre needs four colours) so the colouring itself is familiar and the new idea is the protocol. Week 6 and Week 18 involve hidden rows and information but no prover or verifier. Week 139 (Secret messages) is the companion week on secrecy. New: interactive proof, soundness by repetition, and simulation as the meaning of "learns nothing".

## App connection

Chance and machines region (or Codes and logic), possible family "Prove it without telling": the board shows a covered flower map; the child plays verifier, taps a border to lift two cups, and a meter shows how many rounds have passed. Puzzles: "This prover might be cheating. Lift borders until you catch them" (a five-petal map with one bad border); "You are the prover: re-colour the hidden map so the verifier cannot learn which petal is red." The cave can be a short animated warm-up with left/right buttons. First fit in Neighbor Lanterns (Week 62) shares the map drawing.

## Open questions

- Re-colouring behind a folder: can a 2–3 prover swap colours correctly and quickly, or does an adult need to? A colour-swap card ("every red becomes blue, every blue becomes red") may help; rehearse.
- The cave needs two adults (door-keeper and organiser) or a reliable older child; check staffing.
- Whether "learns nothing" can be made concrete for 4–5 without the simulation idea; the six-shuffle table is the candidate.
- Goldwasser–Micali–Rackoff's exact date and venue are not confirmed from a source opened here; find one before the guide cites it.
