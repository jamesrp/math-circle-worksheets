# Week 143 (draft plan): Domino computers

**Strand:** logic (Codes and logic). **Deep-math field:** Boolean functions and circuits. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A gate takes on/off inputs and gives an on/off output; its whole behaviour is a truth table. There are 2^4 = 16 truth tables with two inputs, and every truth table with any number of inputs can be built from AND, OR and NOT (write one AND-clause for each row that should light, then OR them together). One gate is enough: NAND ("not both") alone is functionally complete, since NOT A = A NAND A, A AND B = (A NAND B) NAND (A NAND B), and A OR B = (A NAND A) NAND (B NAND B). Peirce found this around 1880 but never published it; Stamm published a proof in 1911 and Sheffer in 1913 (for the dual gate NOR). Post's criterion says exactly which sets of gates are complete. Checked here by search over all small circuits (inputs A and B, no constant signals): NOT needs 1 NAND, AND 2, OR 3, XOR ("exactly one") 4, and a half adder 5. A half adder adds two bits: the XOR is the ones digit and the AND is the carry, so its two outputs count how many inputs are on (00, 01, 01, 10). Two half adders and an OR make a full adder (three bits in, a two-bit count out), and chaining adders adds numbers of any length: one half adder and two full adders add any two 3-bit numbers (all 64 pairs checked). Matt Parker's domino computer (Manchester Science Festival, 2012, about 10,000 dominoes, layout co-designed by Andrew Taylor) was exactly this 3-bit adder. Dominoes are honest about the limits of such circuits: a wire is a falling line that can be used once, signals only move forward, OR is just two lines merging, and timing is the hard engineering problem (the builders oversized sections so signals arrived in order, and an earlier 4-bit attempt failed when lines knocked over their neighbours). A domino circuit has no loops and no memory, so it computes one fixed-size table. A marble machine with two-state parts that remember (Turing Tumble) is different: deciding where a marble ends up is P-complete (Johnson, 2019), and on an unbounded board the toy can simulate any Turing machine (Pitt, 2021). Proved: completeness of NAND; adders compute sums. Checked here: the gate counts and the adder tables. Children can discover that a merge is an OR, that "both" is much harder to build than "either", that a pair of gates can count, and that one kind of gate can imitate all the others.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Domino Computer](https://andrewt.net/maths/domputer) — Andrew Taylor, personal site (read November 4, 2026). Parker's 2012 build of about 10,000 dominoes adding two 3-bit numbers once; domino wires, OR, AND (the simplest version cannot be chained), XOR as the hardest gate; half and full adders; one half adder and two full adders; timing, the clock line and the failed 4-bit attempt.
- [Turing Tumble is Turing-Complete](https://arxiv.org/pdf/2110.09343) — Lenny Pitt, University of Illinois, arXiv 2021 (read November 4, 2026). The marble toy's bits and gear bits; Turing-completeness on an infinite board; cites Johnson's P-completeness (and PSPACE-completeness with exponentially many marbles).
- [Sheffer stroke](https://en.wikipedia.org/wiki/Sheffer_stroke) — Wikipedia, secondary pointer (read November 4, 2026). Peirce (1880, unpublished), Stamm (1911) and Sheffer (1913) on the completeness of NAND and NOR; the five properties of Post's completeness criterion.
- Prior use with children: [Domino Computer worksheets](https://think-maths.co.uk/?p=209) — Think Maths (read November 4, 2026). Binary, logic gates and a group-built domino half adder of about 200 dominoes, aimed at Key Stages 3 to 5 (secondary school). Also [human logic circuit activity sheet](https://www.computingatschool.org.uk/media/4jhashlo/0103humanlogiccircuitresources.pdf) — Computing at School, undated (read November 4, 2026): pupils act as inputs and gates, passing a shoulder squeeze as a 1, with a recorder filling a truth table; no age given. No K–5 domino-gate activity was found (searched "domino logic gates activity children", "logic gates for kids").

## A kid-friendly way in

Dominoes first. A line of dominoes is a wire: push the start and the end falls. A fork makes one push knock down two lines; a merge lets two lines knock down one. A paper cup at the end of a line is the "light": it is on if it falls over. Materials: about 300 wooden dominoes per room (60 per table), cups, masking-tape start marks, and a 2-by-2 truth-table card per table with pictures (left pushed? right pushed? cup down?). For gates that dominoes do badly, children become gates (the Computing at School format): a child gate raises a hand by a rule card such as "raise if both of your hands are tapped". Prep: sort dominoes into tubs, print table cards and rule cards; about 20 minutes. Launch (3 minutes): build a fork and a merge in front of everyone, push one input and then the other, and fill the merge's truth table together; ask whether any table can make the cup fall only when both starts are pushed.

## By band

- **K–1:** Build wires, forks and merges; predict and test which pushes knock the cup. Fill the 2-by-2 picture table for a merge. Sort four "machines" (wire, fork, merge, and a merge with a gap) by their tables. No reading.
- **2–3:** The "both" challenge with dominoes (hard; partial designs count) and then as human gates. Be a class half adder: two input children, an "exactly one" child and a "both" child; the two output hands show the count in binary. Which of the 16 tables can a table group act out?
- **4–5:** NAND only. With NAND rule cards, build NOT, AND, OR and XOR, and try to use fewer cards than another table (1, 2, 3, 4 is best). Chain half adders into a 2-bit adder on paper and check 1 + 3. Discussion question: why is NOT hard for dominoes (a cup that falls when nothing is pushed needs its own start and a way to be stopped)?

## Checked facts

All in `check_logic_games_2.py`, function `check_week_143()`:
- 16 two-input truth tables, and NAND circuits on A and B produce all 16.
- NOT, AND and OR from NAND as above; fewest NAND gates (no constants): NOT 1, AND 2, OR 3, XOR 4, XOR and AND together 5.
- Half adder outputs 00, 01, 01, 10; the full adder from two half adders and an OR counts all 8 input rows correctly.
- One half adder and two full adders add every pair of 3-bit numbers (64 pairs) into a 4-bit total.
- A merge's table is 0, 1, 1, 1 (OR).
- Cited, not computed: the 2012 build and its 10,000 dominoes (Taylor); P-completeness and Turing-completeness of Turing Tumble (Pitt, citing Johnson); the history of NAND completeness and Post's criterion (Wikipedia).

## Nearest existing themes

Week 2 (Lamp lab) is linear algebra over two elements, which is XOR arithmetic; here XOR is one gate among sixteen and the point is building tables. Week 17 (Machine memory) has machines with states that read a word; these circuits have no memory at all, which is the contrast to draw. Week 74 (Doubling elevators) and Week 6 touch binary; draft 137 (Game of Life) and draft 138 (busy beaver) are computation with memory and loops. New: truth tables as objects, functional completeness, and the adder as a counting machine.

## App connection

Codes and logic region, possible family "Gate gardens": a board of wires where the child drags gate tiles (merge, both, not, NAND) between input switches and a lamp, then toggles the switches to test. Puzzles: "Make the lamp match this table"; "Use only NAND tiles to make OR in three tiles"; "Build a machine whose two lamps count the switches that are on". The app can grade a design by running all input rows. It could reuse the switch-and-lamp art of Lamp lab.

## Open questions

- Material fit: can children reliably build a domino AND at table scale, or does it need a pre-built jig? Rehearse Taylor's designs and a head-on collision XOR (two falling lines meeting and stopping each other), which is an idea to test, not a claim checked here.
- Is 300 dominoes enough, and are wooden dominoes stable on school tables? Knock-overs during building are frustrating; a "safety gap" habit may be needed.
- Age fit for 4–5 NAND-only puzzles without symbols: rule cards with pictures may be enough.
- Whether to show a real Turing Tumble set as an extension; it is costly and not needed for the core.
