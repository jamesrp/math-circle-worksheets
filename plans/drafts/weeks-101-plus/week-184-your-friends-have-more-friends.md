# Week 184 (draft plan): Your friends have more friends

**Strand:** networks (Maps and networks), with chance. **Deep-math field:** graph theory, averages and the sum of squares (Cauchy–Schwarz). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The friendship paradox (Scott Feld, 1991): in any network of friendships, the average number of friends that friends have is at least the average number of friends people have, with equality exactly when everyone has the same number. Precisely, if person i has k_i friends, list one entry for every end of every friendship; the average of the friend-counts on that list is Σk_i² / Σk_i, while the average over people is Σk_i / n, and Σk_i²/Σk_i = mean + variance/mean ≥ mean. The counting proof children can do: each person writes their friend count on one note for each friend and hands it along the friendship. A person with 4 friends writes "4" four times, so the notes add up to the sum of the squares, and there are Σk_i notes. People with many friends write many notes, so the notes are pulled upward. A second, per-person version is also always true (Cantwell, Kirkley and Newman 2020, and a short argument here): if nobody is friendless, the average over people of "my friends' average minus my own count" is at least 0, because each friendship between people with a and b friends contributes a/b + b/a ≥ 2. Neither statement says every person has fewer friends than their friends: in a star, the hub has 4 and its friends average 1. Real networks are lopsided, so most people are on the short side (Feld's high-school data: 80 of 146 girls had fewer friends than their friends' average, 41 more). Proved: both inequalities and the equality case. Checked here on every network with up to 6 people. Children can discover that the notes average beats the people average, that only an "everyone equal" network ties, and why.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Why Your Friends Have More Friends than You Do](https://fermatslibrary.com/s/why-your-friends-have-more-friends-than-you-do) — Scott L. Feld, *American Journal of Sociology* 96(6), 1991, 1464–1477 (Fermat's Library reproduction). The formula mean + variance/mean, the statement that the mean among friends is always at least the mean among individuals, and the Coleman high-school data (read November 4, 2026).
- [The friendship paradox in real and model networks](https://ar5iv.arxiv.org/html/2012.03991) — George T. Cantwell, Alec Kirkley and M. E. J. Newman, arXiv 2012.03991, 2020. Separates the network-wide statement (always true, equality only for regular networks) from the individual one (can fail for many people) and shows the per-person average difference is nonnegative (read November 4, 2026).
- Prior use with children: [The Friendship Paradox: Why We Can't All Be Popular, teacher guide](https://web.mit.edu/blossoms/sites/default/files/video/guide/Friendship-Paradox-Teacher-Guide_0.pdf) — MIT BLOSSOMS, for high school; students act as dots with string for friendships on made-up data, then compute both averages and the all-equal case (read November 4, 2026). No K–5 use found.

## A kid-friendly way in

A yarn animal town. Children take animal role cards (never their real friendships) and stand where a floor map says; an adult ties yarn between animals per a printed friendship list. Each animal counts its strands, then writes that number on one sticky note per strand and passes each note along its strand. Two piles: one card per animal with its own count, and all the notes. Which pile has the bigger average? Prep: role cards, a ball of yarn cut into 10 to 12 pieces, sticky notes, two network lists (one lopsided, one ring); about 20 minutes. Launch (2–3 minutes): five volunteers as a star (a hub animal and four friends); count strands, pass notes, and line up both piles as cube towers.

## By band

- **K–1:** the star and a ring with cube towers for counts. Each animal builds a tower for its own count and receives one tower from each friend; compare "my tower" with "my friends' towers". Who has fewer than their friends?
- **2–3:** the eight-animal town in the plan: averages 2.5 for animals and 3 for notes; six of eight animals have fewer friends than their friends' average. Invent a town where the two piles tie (everyone equal), and one where the notes are much bigger.
- **4–5:** explain why a 4-friend animal adds 16 to the notes total, so the notes total is the sum of the squares; argue that the notes average can never be smaller; meet the per-friendship argument a/b + b/a ≥ 2 with cube towers (3/1 + 1/3 against 2).

## Checked facts

Computed in `check_networks_3.py`, `check_week_184()`:

- the five-animal star: animals average 8/5, notes average 20/8 = 5/2; four of five have fewer friends than their friends' average;
- the eight-animal town (A–B, A–C, A–D, A–E, B–C, D–E, E–F, F–G, G–H, A–F): counts 5, 2, 2, 2, 3, 3, 2, 1; 20 strand ends; animals average 5/2; notes total 60 and average 3; 6 of 8 below their friends' average;
- a ring of six: both averages 2;
- every network on 2 to 6 people with at least one friendship: notes average ≥ people average, equal exactly when all counts are equal; n·Σk² ≥ (Σk)²;
- every such network with nobody friendless: the per-person average difference is ≥ 0 and equals the sum over friendships of a/b + b/a.

Cited, not computed: Feld's Coleman data (80 of 146) and the large-network fractions in Cantwell, Kirkley and Newman.

## Nearest existing themes

Week 20 (Averaging) and Week 10 (counting links at each island) are the nearest; no week, atlas family or draft names the friendship paradox (searched). Draft 133 (Simpson's paradox) and draft 171 are other chance surprises; draft 152 (Who is most important?) visits people in proportion to their links, which is the same bias (a random strand end lands on a busy person). New here: a weighted average that always exceeds a plain one, with a sum-of-squares proof made of sticky notes.

## App connection

Maps and networks: a "friend counts" family. The child builds or edits a small network, and two bars show the people average and the notes average live; puzzles ask for a network where the bars tie, where the gap is at least 2, or where exactly one animal has more friends than its friends' average. Another: drag one strand to make the gap as large as possible with 6 animals and 6 strands.

## Open questions

- Social safety: use role cards and printed networks only, never children's real friendships or popularity; the facilitator guide should say so plainly.
- Whether K–1 can compare one tower with a group of towers fairly; levelling the friends' towers (Week 20's move) may be the needed bridge.
- Whether the per-person version is worth the extra arithmetic for 4–5, or should stay in the facilitator guide.
