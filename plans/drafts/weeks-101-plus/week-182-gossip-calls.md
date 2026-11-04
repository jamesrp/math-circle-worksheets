# Week 182 (draft plan): Passing secrets by phone

**Strand:** networks (Maps and networks). **Deep-math field:** extremal combinatorics, information spreading in networks. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The gossip problem (posed around 1971; the attribution to Boyd is from Williams 2025): n people each know one secret, and in a call two people tell each other everything they know so far. The fewest calls after which everyone knows every secret is 1 for 2 people, 3 for 3 people and exactly 2n − 4 for every n ≥ 4. This was proved independently by Tijdeman (1971), Baker and Shostak (1972) and Hajnal, Milner and Szemerédi (1972). The upper bound is a construction children can find: four people finish in 4 calls (AB, CD, AC, BD), and each extra person calls one of the four before those four calls and again after them, so each new person costs 2 calls. The obvious "hub" plan (everyone tells one person, who calls everyone back) costs 2n − 3, one call too many. The lower bound is the hard part. A first argument children can follow: nobody can know everything until at least n − 1 calls have happened (each call joins at most two knowledge piles), and that call makes only its two people complete; the other n − 2 people still need at least one call each, and a call reaches at most two of them. This gives (n − 1) + ⌈(n − 2)/2⌉, which proves 4 calls for 4 people and 6 for 5, but only 7 for 6 people, where the truth is 8. Closing that gap takes the published proofs; Baker and Shostak's key lemma is that in a shortest scheme nobody ever hears their own secret back from someone else. Checked here by exhaustive search: 1, 3, 4, 6, 8 calls for 2 to 6 people. Proved for all n: 2n − 4. Still studied: what spreads fastest in a fixed number of calls (Williams 2025 shows the greedy plan is best for every m < 2n − 4), and versions with time limits or one-way messages. Children can discover the 4-call trick, beat the hub plan, find that each newcomer costs 2 calls, and prove that 3 calls cannot work for 4 people.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Gossips and telephones (three original papers)](https://www.math.uni-bielefeld.de/~sillke/PUZZLES/gossips.pdf) — reproductions on the ~sillke puzzle pages, University of Bielefeld, of Baker and Shostak, "Gossips and Telephones", *Discrete Mathematics* 2 (1972) 191–193; Tijdeman, "On a Telephone Problem", *Nieuw Archief voor Wiskunde* 19 (1971) 188–192; Hajnal, Milner and Szemerédi, "A Cure for the Telephone Disease", *Canadian Mathematical Bulletin* 15 (1972) 447–450. The 2n − 4 theorem, the four-chief construction, Tijdeman's AB, CD, AC, BD, and the "no one hears their own information" lemma (read November 4, 2026).
- [Gossiping](https://aeb.win.tue.nl/math/gossip.html) — Andries Brouwer's mathematics pages, TU Eindhoven. Small cases 0, 0, 1, 3 calls for n = 0 to 3 and 2n − 4 for n ≥ 4, with the list of independent proofs (read November 4, 2026).
- [Greedy Gossiping](https://arxiv.org/html/2506.17804v1) — Kada K. Williams, arXiv 2506.17804, 2025. Statement of the problem (Boyd, 1971), the three independent resolutions, and the theorem that greedy calling spreads the most gossip for every m < 2n − 4 (read November 4, 2026).
- Prior use with children: [The Gossip Problem](https://slmath-production-assets.sfo3.digitaloceanspaces.com/attachments/jrmf/activities/Gossip.pdf), a question sheet stored in SLMath's JRMF activities folder (the page itself names no author or grade): 3, 4 and 5 people first, then whether 2n − 1, 2n − 3 and 2n − 4 calls are possible (read November 4, 2026). Also Alex Bellos's Guardian puzzle suggested by Bobby Seagull, [republished by inkl](https://www.inkl.com/news/did-you-solve-it-get-the-gossip-with-bobby-seagull), whose solution gives 4 calls for 4 friends and 2n − 4 in general (read November 4, 2026). No K–5 classroom report found.

## A kid-friendly way in

Secret cubes. Each child (or toy animal at K–1) owns one colour of snap cube; a shared tray holds n cubes of every colour. A call: two children sit together, and each takes from the tray one cube of every colour the other holds and they lack. Done when every child holds a full rainbow. The only record is the call list (AB, CD, AC, …) on a whiteboard, so a plan can be replayed and checked. Prep: sort cubes into trays and make name or animal cards; about 15 minutes. Launch (2–3 minutes): three volunteers with red, blue and yellow; act out one call, show the cube rule, write "AB" on the board, and ask how few calls finish the job.

## By band

- **K–1:** three animals, then four. Act out calls with cubes; an adult writes the call list. Race the adult's "everyone calls everyone" plan (6 calls for four animals) and find a plan with fewer.
- **2–3:** find 4 calls for 4 people; then 5 people in 6 calls and 6 people in 8; compare with the hub plan (7 and 9 calls). Is there a rule for how many calls a newcomer costs?
- **4–5:** explain why the four-chief plan works for any number of people; prove that 3 calls cannot finish 4 people and 5 calls cannot finish 5 (nobody is complete before call n − 1, and that call completes only two people); see that the same argument gives only 7 for 6 people and hear that 8 needs a cleverer proof.

## Checked facts

Computed in `check_networks_3.py`, `check_week_182()`:

- fewest calls for 2 to 6 people: 1, 3, 4, 6, 8, by exhaustive search over knowledge states;
- the 2n − 4 four-chief scheme works for 4 to 14 people; the hub plan uses 2n − 3;
- for 4 people no 3-call list works (all 216 tried), and 24 of the 1296 four-call lists do;
- after n − 2 calls nobody knows all n secrets (n = 3, 4, 5); the bound (n − 1) + ⌈(n − 2)/2⌉ gives 4, 6, 7 for 4, 5, 6 people against the true 4, 6, 8;
- everyone calling everyone takes C(8, 2) = 28 calls for 8 people against 12.

Cited, not computed: 2n − 4 for all n ≥ 4 (Tijdeman; Baker and Shostak; Hajnal, Milner and Szemerédi) and the greedy theorem (Williams).

## Nearest existing themes

No catalog week, atlas family, scouting draft or earlier draft uses the gossip problem (searched "gossip", "telephone"). Week 84 (Public knowledge) is about what people know, but as deduction, not spreading. Week 13 (Route packing) and Week 53 (Cheapest connected networks) are optimisation on networks with a matching certificate; here the network is built in time and the lower bound is the new reasoning move. Draft 152 (random walks) and draft 188 (small worlds) also spread things through a network, but by chance. New here: a construction-plus-lower-bound optimum where the easy bound is not sharp.

## App connection

Maps and networks: a "phone tree" family. The child taps two people to make a call; each person's ring of coloured dots fills as secrets arrive; a call counter and a target ("4 people in 4 calls") set stars. Later puzzles fix some calls already made, or ask for a plan where nobody makes more than 3 calls. One puzzle: 5 people in 6 calls. A second: show that 3 calls can never finish 4 people by trying until the app reveals the "nobody is complete yet" counter.

## Open questions

- Cube bookkeeping: will children take the right cubes from the tray, or is a printed strip of colour boxes to tick quicker? Rehearse with 6 people.
- Whether K–1 can follow a call list, or only act calls as an adult reads them.
- How far grades 4–5 can go with the lower bound; the 6-person gap (7 against 8) should stay an honest open end in the session, not a hidden proof.
