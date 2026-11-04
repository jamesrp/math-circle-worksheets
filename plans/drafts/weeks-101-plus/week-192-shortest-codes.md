# Week 192 (draft plan): Short codes for common letters

**Strand:** logic (Codes and logic). **Deep-math field:** information theory, prefix-free codes, greedy algorithms. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A code gives each letter a string of 0s and 1s (or left and right turns). It is prefix-free when no codeword is the start of another; then a message sent with no gaps decodes in exactly one way, read from the front, and the codewords are exactly the leaves of a branching tree (left = 0, right = 1). Kraft's inequality: lengths l_1, …, l_k belong to some prefix-free binary code exactly when 2^(−l_1) + … + 2^(−l_k) ≤ 1 (a leaf at depth l uses up 2^(−l) of the tree; McMillan extended the "only if" to every uniquely decodable code). So lengths 1, 1, 2 are impossible, and a code that uses the whole budget (sum exactly 1) is a full tree. Huffman's theorem (D. A. Huffman, Proceedings of the IRE, 1952, from a term paper for Robert Fano's MIT class): to make the total length of a message as small as possible, repeatedly join the two rarest letters (or groups) into one group whose count is their sum; the joins build the tree, and the total message length equals the sum of all the joined counts. The reason it works: in some best tree the two rarest letters sit as siblings at the deepest level, so joining them first loses nothing (proved). For ABRACADABRA (A 5, B 2, R 2, C 1, D 1) the joins are 2, 4, 6, 11, total 23 bits, against 33 bits if all five letters get 3-bit codes; a brute-force search over all lengths allowed by Kraft confirms 23 is the minimum. Huffman is optimal among letter-by-letter codes with known counts; coding longer blocks, or arithmetic coding, can do better, and Shannon's entropy is the limit (cited, not developed here). Morse code (as arranged by Alfred Vail, who reportedly counted the type in a printer's cases) gave the commonest letters the shortest signals, E a single dot, but it is not prefix-free: E is the start of I and S, so "..." could be EEE, EI, IE or S, and Morse needs a gap as a third symbol. Children can discover that common letters deserve short codes, that some sets of codes cannot be read without gaps, that the code tree has a budget, and Huffman's join-the-two-rarest rule.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [A Method for the Construction of Minimum-Redundancy Codes](https://www.csd.uoc.gr/~hy474/bibliography/Huffman.pdf) — David A. Huffman, Proceedings of the I.R.E., September 1952, pp. 1098–1099 (read November 4, 2026). Only the title block and running headers were readable in this copy; it is cited for the title, author and venue, and the algorithm is taken from the next two sources.
- [Information Theory, Lecture 6](https://web.stanford.edu/class/ee376a/files/2017-18/lecture_6.pdf) — Tsachy Weissman, Stanford EE376A, January 25, 2018 (read November 4, 2026). The Kraft–McMillan inequality, its converse with prefix codes, and the theorem that the Huffman code is an optimal prefix code.
- [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) — Wikipedia, secondary pointer (read November 4, 2026). The Fano term-paper history, the merge-two-lowest algorithm, optimality for letter-by-letter coding and its limits, bottom-up against Shannon–Fano's top-down.
- [Case Work](https://www.futilitycloset.com/2017/11/04/case-work/) — Futility Closet, November 4, 2017 (read November 4, 2026). Vail's visit to a Morristown newspaper and the type-case counts behind giving common letters the shortest symbols, E a single dot.
- Prior use with children: none found for Huffman codes at K–5. [Text Compression](https://classic.csunplugged.org/activities/text-compression/) — CS Unplugged (read November 4, 2026) is a children's compression activity, but it uses Ziv–Lempel repeats, not Huffman trees, and mentions Huffman only in an external resource list. Searched "Huffman tree unplugged activity students" and "CS Unplugged Huffman".

## A kid-friendly way in

A floor tree and turn messages. Tape a branching path on the floor (or a large poster) whose ends hold picture cards. A message is a list of turns, L or R, with no gaps; the walker starts at the root, turns at each fork, and when they reach a picture they say it and jump back to the root. Then tables design their own code for a short message, ABRACADABRA, as a paper tree whose leaves are letter cards, and count the turns the message needs, using cubes for turns. Prep: a taped floor tree with 4 leaves, printed letter cards, blank tree templates, and message cards; about 20 minutes. Launch (3 minutes): a child walks "L, R, R, L" on the floor tree while the room calls out the pictures, then the room tries a gap-free message on a code where one picture sits in the middle of a path, and finds it can be read two ways.

## By band

- **K–1:** Walk turn messages on the floor tree and decode picture messages. Then compare two trees for the message "cat cat cat dog bird": with cat near the root, the walk is shorter. Count turns with cubes. No reading beyond L and R.
- **2–3:** Build a tree for ABRACADABRA that makes the message as short as possible. Tables compare totals on a class chart (23 is the best). Which sets of codes can be read without gaps? Find the Morse problem: E, I and S share a start.
- **4–5:** Discover Huffman's rule by trying it: join the two rarest, repeat. Why does the total equal the sum of the joins? Why can two codes of length 1 and one of length 2 never coexist (the tree budget)? Why should the two rarest letters be siblings at the bottom?

## Checked facts

All in `check_logic_3.py`, function `check_week_192()`:
- ABRACADABRA counts 5, 2, 2, 1, 1; Huffman total 23 bits; the brute-force minimum over all Kraft-allowed lengths is 23; equal 3-bit codes need 33.
- The code A 0, B 100, R 101, C 110, D 111 is prefix-free, sends the message in 23 bits, decodes in exactly one way, and uses the whole budget (sum 1).
- Lengths 1, 1, 2 break Kraft (sum 5/4).
- Atlas AP-29's counts 4, 2, 1, 1: 14 bits, the minimum; equal counts 1, 1, 1, 1 give 8 with the balanced tree.
- Morse without gaps (E, I, S, T, A, N, M) is not prefix-free; "..." has 4 readings.
- MISSISSIPPI: Huffman 21 bits against 22 with 2-bit codes (a weak example; ABRACADABRA is better).
- Cited, not computed: Huffman's optimality theorem and Kraft–McMillan in general (Weissman; Wikipedia); Vail's type-case story (Futility Closet).

## Nearest existing themes

Atlas family AP-29 is this topic: give four picture messages codewords at the leaves of a branching tree, decode without spaces, and beat 16 bits when one picture is common (counts 4, 2, 1, 1 send 14 bits). It has no K–1 entry and is in the path's left-out list for that reason. So this plan substantially duplicates AP-29's core; the distinct parts are Huffman's join-the-rarest algorithm and why it is optimal, the Kraft budget, Morse code's gaps, and a floor-tree K–1 entry. It is best built as AP-29's full-band home or a three-band expansion of it, not as an unrelated week. Week 6 (Code breaking) has yes-or-no question trees that find a secret in the worst case; here the same trees are weighted by how often each leaf is used. Week 18 (Hidden changes) adds redundancy to survive errors; here redundancy is removed. Weeks 17 and 76 mention "Morse" only as Thue–Morse, an unrelated word; no week uses Morse code. Week 12 (Catalan bijections) counts the tree shapes.

## App connection

Codes and logic region, possible family "Turn codes": a tree with draggable letter leaves; a message bar shows the gap-free string of turns and its length. Puzzles: "Make ABRACADABRA as short as you can" (23); "This code has a picture in the middle of a path: find a message with two readings"; "Join the two rarest" as a guided build where the tree grows from the leaves up. Week 18's "Codebooks in Signal Lanterns" could host it as a contrasting level (short codes against safe codes).

## Open questions

- Can K–1 children walk a tree and "jump back to the root" reliably, or does the restart need a physical marker (a hoop at the root)?
- Is ABRACADABRA too long to count for 2–3? A 9-letter message with a 4-letter alphabet may suit them better.
- How to present Morse fairly: its gaps make it a three-symbol code, so it is not "wrong", only not prefix-free.
- Whether to schedule it with AP-29's print pages instead of new ones.
