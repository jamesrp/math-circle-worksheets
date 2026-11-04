# Week 200 (draft plan): Kaprekar's sorting machine

**Strand:** number (Numbers). **Deep-math field:** discrete dynamics and number theory (iterated maps on a finite set, fixed points and cycles, proof by exhaustion with symmetry). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Kaprekar's routine (D. R. Kaprekar, 1949): take a four-digit string, sort its digits high to low and low to high, subtract, and repeat, keeping leading zeros (2111 gives 2111 − 1112 = 0999, then 9990 − 0999 = 8991). Every start whose digits are not all equal reaches 6174, which maps to itself (7641 − 1467 = 6174), within 7 steps; 7 are sometimes needed, and 6174 is the only fixed point other than the all-equal strings. This is a finite theorem proved by exhaustion: Nishiyama (Plus, 2006) lists how many of the 8991 starts from 1000 to 9999 need 0 to 7 steps (1, 356, 519, 2124, 1124, 1379, 1508, 1980), and this plan's script checks them all. The exhaustion is much smaller than it looks, which is the mathematical point for children. If the sorted digits are a ≥ b ≥ c ≥ d, the first difference is 999(a − d) + 90(b − c), so it depends only on two gaps, and there are only 54 possible first results; checking those 54 (each reaches 6174 within 6 more steps) proves the theorem. Three digits work the same way: the difference is 99(a − c), only nine values (099, 198, …, 891), all reaching 495 within 6 steps, a proof a group of children can finish by hand. Two digits give 9 times the gap and a loop, 09 → 81 → 63 → 27 → 45 → 09, with no fixed point; Nishiyama reports that five-digit strings also fall into loops with no single kernel. The general principle is proved and simple: a machine on a finite set of states must eventually repeat, so every orbit ends in a fixed point or a loop; what is special about 4 digits in base 10 is that the only end is one fixed point. Happy numbers (repeatedly sum the squares of the digits) are the extension: every start ends at 1 or in the eight-number loop 4, 16, 37, 58, 89, 145, 42, 20 (OEIS A007770), and a short size argument (a number with many digits has a much smaller sum of squares) reduces the proof to finitely many cases. Proved: all of the above, by finite checking. Children can discover the fixed point, that the machine ignores the order of the digits, that the first answer is always a multiple of 9, and that a few cases settle every start.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Mysterious number 6174](https://plus.maths.org/issue38/features/nishiyama/feat.pdf). Yutaka Nishiyama, Plus Magazine, March 2006. The routine, the leading-zero rule, a computer check of all 8991 starts reaching 6174 within 7 steps with a frequency table (1 at step 0, 1980 at step 7), 495 for three digits, a loop for two digits, loops for five (read November 4, 2026).
- [Kaprekar's Constant](https://math.hmc.edu/funfacts/kaprekars-constant/). Francis E. Su et al., Math Fun Facts, Harvey Mudd College. At most 7 steps, padding with leading zeros (3222 − 2333 = 0999), finitely many states so every run repeats (read November 4, 2026).
- [A007770: Happy numbers](https://oeis.org/A007770). OEIS. Happy numbers 1, 7, 10, 13, 19, 23, … and the 8-loop that every other start falls into (read November 4, 2026).
- Prior use with children: [Ganita Prakash, Grade 6, Chapter 3 "Number Play"](https://evidyarthi.in/wp-content/uploads/2024/08/cbse-class-6-maths-book-ganit-prakash-chapter-3-pdf-download.pdf). NCERT's national grade 6 textbook (India), section 3.6 "The Magic Number of Kaprekar" (a copy hosted by eVidyarthi). Students try 4-digit starts, compare with friends, try 3-digit numbers, and count rounds for 5683 (read November 4, 2026).

## A kid-friendly way in

The machine is physical: digit cards in a tray. Lay four digit cards, slide them into high-to-low order to make the big number, then low-to-high to make the small one, subtract, and write the answer on new cards. Younger children use two digit cards and a 0–9 number track to find the gap. Prep: print digit cards (four sets of 0–9 per pair), a 0–9 track, and a "gap chart" listing 9 × 1 to 9 × 9 as two-digit cards, about 15 minutes. Launch (2 to 3 minutes): run one three-digit start together on large cards (sort, sort, subtract) until it repeats, without saying what it repeats at.

## By band

- **K–1:** two-digit machine. Pick two digit cards, find the gap by stepping along the 0–9 track, take the matching card pair from the gap chart (gap 3 gives 2 and 7), and go again. The pairs go round a loop; walk it and find that every start joins the same loop. No subtraction written; counting steps only.
- **2–3:** three-digit machine (subtraction of three-digit numbers, with base-ten blocks or a supported column method). Where does every start end? Then the big question: are the first answers always from a short list? Find the whole list (nine) by pooling, and check that each one ends at 495, so every start does.
- **4–5:** four-digit machine with a calculator allowed for subtraction after the first few by hand: do all starts end at 6174, and how many steps can it take? Then prove it by cases: why do 3524 and 5432 give the same first answer (only the digits matter, not their order)? Show the first answer depends only on two gaps, list the possible gap pairs, and share the 54 cases among the table. Extension: happy numbers, and why every start eventually gets small.

## Checked facts

Computed in `check_symmetry_number_3.py`, `check_week_200()`:

- all 9990 strings 0000–9999 with two different digits reach 6174 within 7 steps; 7 is attained; 6174 is the only fixed point among them;
- among the 8991 starts 1000–9999: 1, 356, 519, 2124, 1124, 1379, 1508, 1980 need 0 to 7 steps;
- 3524 → 3087 → 8352 → 6174; 2111 → 0999 → 8991;
- the first difference is always 999(a − d) + 90(b − c); there are 54 possible first results, each reaching 6174 within 6 steps;
- three digits: the first results are exactly 99, 198, …, 891, and every start reaches 495 within 6 steps;
- two digits: 09 → 81 → 63 → 27 → 45 → 09, gaps 9, 7, 3, 5, 1;
- happy numbers below 50: 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49; every start up to 1000 ends at 1 or in the 8-loop.

Cited, not computed: Nishiyama's statement about five-digit loops.

## Nearest existing themes

Draft 108 (hailstone numbers) mentions Kaprekar as a side contrast: a machine whose question is settled by checking every case, set against Collatz, which is open. This week makes Kaprekar the main object and adds what 108 does not: the reduction from thousands of starts to 54 (and to 9 for three digits), the invariance under reordering digits, the multiple-of-9 structure, the two-digit loop as a K–1 entry, and happy numbers. The two should be sequenced (this one first, as the case where "try everything" works), and 108's Kaprekar station dropped if both are built. Week 3's shuffle machines also come back because there are only finitely many states, but each of them can be undone, so they return to the start; Kaprekar's machine cannot be undone (many starts share a next value), so it funnels starts into one end. That contrast is worth saying aloud to 4–5.

## App connection

Numbers. A "Sorting machine" family: tap digit tiles into order, the board subtracts and lays the next tiles. Puzzles: "Find a start that takes exactly 7 steps"; "Which two of these starts give the same first answer?"; "Fill the missing row in this run". Draft 108 proposed the same machine frame for hailstones; one family could hold both machines.

## Open questions

- Is three-digit subtraction with regrouping too heavy for 2–3, so that the machine becomes arithmetic practice? Test with blocks, or give a subtraction strip.
- The K–1 gap chart replaces subtraction by lookup; check that children still feel they are running a machine.
- Decide whether happy numbers belong here or in a separate return visit.
