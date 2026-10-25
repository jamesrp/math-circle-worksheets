# Review: Train-yard sorting, draft v1

Reviewed: `draft/k-1.pdf` (5 pages), `draft/grades-2-3.pdf` (4 pages) and `draft/grades-4-5.pdf` (5 pages). I rendered every page and read `draft/src/build.py`, `verify.py` and `check_pages.py`. I checked every printed train, path and insertion task with my own brute-force code, which tries every legal move sequence and does not rely on the author's 2-3-1 test or greedy method. Every printed answer is correct (details in the last section).

## Overall verdict

The draft is strong. The mathematics is correct and follows the outline's three kernels. The page format is close to the organizer's standard: correct header and footer, no titles, no Name/Date, no encouragement, no hints. Problems are substantial. The left-to-right convention is the same on the page, in the worked picture and on the mat. The 2-3 insertion problem and the 4-5 path-decoding problem are especially good.

Two things must change before printing:

1. **Answer positions give the answers away.** In five of the six "mark each one ✓ or ✗" grids, all the trains that work sit in one column. Every row has exactly one train that works and one that does not.
2. **The track mat does not exist.** No page in any packet is the mat the whole activity depends on, yet 4–5 Problem 8 asks for two of them.

The other items below are smaller.

---

## Must fix

### 1. The ✓/✗ answers follow the layout (all three bands)

The grids fill row by row in two columns, and the writer listed the trains alternating works / stuck. Checked with my own code:

| Grid | Left column | Right column |
|---|---|---|
| K–1 P2 (p. 2) | 4321 ✓, 2143 ✓, 3124 ✓, 1432 ✓ | 3412 ✗, 1342 ✗, 4231 ✗, 4132 ✓ |
| K–1 P5 (p. 5) | 54321 ✓, 21543 ✓, 51324 ✓ | 45123 ✗, 13524 ✗, 32514 ✗ |
| 2–3 P3 (p. 2) | 31542 ✗, 24351 ✗, 15342 ✗, 45321 ✗ | 41325 ✓, 52143 ✓, 32154 ✓, 12534 ✓ |
| 2–3 P5 (p. 3) | 53412 ✗, 42513 ✗, 34521 ✗ | 21534 ✓, 14235 ✓, 54132 ✓ |
| 4–5 P2 (p. 2) | 24153 ✗, then four ✓ | 31254 ✓, then four ✗ |

The pairing does damage even apart from the columns. In every row of these grids except the last row of K–1 P2, exactly one train works. A child who settles one train in a row gets the other free. Children who mark two or three rows will notice "every other one works". The worst case is 2–3 Problem 5 ("Decide without driving…"), because a wrong rule still scores perfectly if the child follows the pattern. Adults checking the sheets can be misled the same way.

**Fix:** Reorder each list so that no column, row or alternation pattern carries the answers. Mix rows with two ✓, two ✗ and one of each, and keep the overall balance roughly as it is. In 4–5 P2, keep the pairing by length for layout if you like, but do not make every length-pair one ✓ and one ✗. K–1 P1 uses dictionary order, which is fine.

### 2. No track mat, and its size needs working out (all bands; may be outside the reviser's three-file scope)

The outline's materials list a printed mat per pair at 100%. It needs walls, a siding exactly one car wide and five cars long, and 25 mm cars. The rules on every packet and 4–5 P8 ("Place a second track mat to the left of yours") assume the mat exists. The packets contain only the 7 mm schematic at the top of page 1. Nothing in `draft/src/` builds a mat.

The physical fit is not trivial. A five-car arrival track, a one-car junction and a five-car departure track add up to about 275–290 mm, depending on the slack given to each 25 mm car. That is wider than the printable width of US Letter in landscape (about 266 mm). The siding direction fits easily (about 156 mm). So the mat must let the arrival and departure tracks run off the page edges, with cars waiting on the table, or it must shorten one of them. If the cars are 2 cm cubes rather than 25 mm squares, the cell size changes.

**Fix:** Produce the mat as its own print file, built from the same `mat_panel` geometry at full scale. Mark it as not yet rehearsed with the actual cubes. If the revision stage cannot add a fourth file, the session cannot run without this, and the organizer needs to be told. Do not quietly append an unnumbered mat page to each child's packet: that departs from the page format and would print 11 mats where 5–6 are needed. The 4–5 table needs two mats for P8 (see item 3).

---

## Should fix

### 3. The answer to 4–5 Problem 8 depends on the mat's siding length (p. 5)

"Is there any train that cannot leave in order through two sidings?" Mathematically, every order of up to six cars works and 22 of the 5,040 seven-car orders fail. On the printed mats, each siding has a dead end after five cars. With that limit, 51 seven-car orders fail. I recomputed this independently, and the author's own `verify.py` comment says the same. So 29 of the 51 failures a child could find on the mats come only from the wall, not from the two-siding machine. Example: 2 3 5 7 4 6 1 fails with five-car sidings but works with longer ones.

A child who finds a seven-car failure on the mat will most likely have found the wrong thing. P8 also needs a second mat, but the outline supplies one per pair and the 4–5 table is one pair plus a referee.

**Fix:** Add one task-specific rule to P8, for example: "If a siding fills up, line extra cars up on the table beyond its end." Use whatever wording fits the mat design. Count an extra mat for the 4–5 table in the print run. The three listed trains (231, 3412, 25341) all work with two sidings. That is unavoidable with six cars or fewer, and it is fine, because the real task is finding the drives.

### 4. 4–5 Problem 1 runs two tasks together and prescribes the method (p. 1)

"Which of these six trains… Mark each one ✓ or ✗. Then make a card for each of the 24 trains…, drive them, and sort the cards…" The 3-car task and the 4-car enumeration are separate jobs joined by "Then". The second prescribes the method: write cards, drive, sort. Writing 24 four-digit cards is mostly transcription for one pair and a referee. It also repeats the 2–3 table's main task and will probably take 15 minutes of a 35–40 minute block. As a result, the parts the outline puts at the heart of this band (paths on pp. 3–4, two sidings on p. 5) are unlikely to be reached in a first visit.

**Fix:** Keep the six 3-car trains, and ask "How many of the 24 trains with cars 1, 2, 3, 4 can leave in order?" without prescribing cards. Children who want cards can still make them; the blank cards are on the table. Alternatively, make the six 3-car trains their own short opening and keep the 24-count as P2. Either way, drop the method from the sentence.

### 5. Grades 2–3 is the thinnest band and needs a late problem (p. 4)

There are four pages, and page 4 is half empty. After P6, a quick third grader has nothing left, while K–1 has five pages and 4–5 has eight problems. P6 (where car 5 can join) sets up a beautiful continuation that the packet does not use. Every five-car train that leaves in order comes from exactly one four-car train that leaves in order, with car 5 put into one of its allowed gaps. Adding up the allowed gaps over the 14 four-car trains from the Problem 2 pile gives 42. I checked this sum with code.

**Fix:** Add a Problem 7 on page 4, for example "How many trains of cars 1, 2, 3, 4, 5 can leave in order?", with answer space. The pile from P2 and the idea from P6 are the tools, so keep any hint about using them for the adults. That gives the 2–3 table a route to the Catalan count without the path representation.

### 6. 4–5 Problem 4 assumes something Problem 6 asks (p. 3)

"A drive can be recorded as a path… Draw **the** path of every four-car train that can leave in order." The definite article assumes each train has exactly one successful drive. P6 asks this as its first question: "Can one train be driven out in order in two different ways?" (The true answer is no, which I checked for every order of up to 7 cars.)

**Fix:** "Draw a path for each four-car train that can leave in order…", or drop that question from P6.

---

## Consider

7. **K–1 rules never say which end of the train goes first** (p. 1). The upper bands say "so the car on the left arrives first"; K–1 has only "the way it is drawn". Reversing a train swaps answers (2 3 1 reversed is 1 3 2), and in P3 it turns "car 1 is last" into "car 1 is first". The picture and the launch should prevent this, but a short clause such as "The car on the left goes first." costs little when read aloud.

8. **The worked picture is one of the Problem 1 trains in every band.** The three panels show 1 3 2 working, and 1 3 2 is one of the six trains in K–1 P1, 2–3 P1 and 4–5 P1, as well as the 4–5 P4 example. The outline suggests 1, 3, 2 for the launch, and with three cars every order is a task, so this is acceptable. Just note that the page pre-answers one of the six cells. If you want a non-task example, a two-car "2 1" shows a car waiting, but it is less vivid.

9. **"never jump over each other or go backward" (upper-band rules)** can be read as forbidding the move up out of the siding, since that reverses direction. The intended meanings are that a car never returns to the arrival track and that a departed car stays on the departure track. Consider "A car in the siding cannot go back to the arrival track."

10. **"Make extra cars from paper squares for trains with more than five cars."** sits in the 4–5 shared rules, but only P2 uses more than five cars on one siding. Under the standard, task-specific rules belong in the problem. Move it into P2 (or P2 and P8).

11. **K–1 order: P4 before P5.** P4 ("Find trains… that cannot leave… How many different ones can you find?") is an open search with a lot of writing. P5 (six given five-car trains) is the more accessible and more physical task. A K–1 pair stuck on P4 never reaches the five-car trains. Consider swapping them. P4 still builds on P2 and P3 when it comes later.

12. **Small visual points.** The schematic labels ("departure track", "arrival track", "siding") are `\scriptsize`, under 8 pt on the 12 pt packets. Bump them one size. In 4–5 P2 the check boxes form a ragged column, because each box follows its own train length. Aligning them in one column per side looks tidier and makes marking easier.

13. **4–5 Problem 7 has only ruled lines.** Children counting 42 and 132 through paths will want to draw. One larger blank dot lattice (6 up, 6 down, the same parity lattice as P4) labelled only as extra workspace would provide the diagram without suggesting a method. It is optional, since the method must stay theirs.

14. **4–5 Problem 6 stacks three questions plus "Explain."** Together they are the bijection, so the bundle is purposeful. Note that the third question ("Which paths… come from a train…?") is partly answered by the grids, which have no dots below the bottom line. The substantive part is whether every such path comes from a train. This can stay as written. Do not narrow it to a yes/no that states the conclusion.

15. **Out of scope for the pages, but needed for the session.** "Week NN" is a placeholder in every header and footer, so the organizer must fill it in. The K–1 adult is the non-mathematician parent and will need a short answer key: 2 3 1 is the only stuck three-car train, 4 3 2 1 is the only train that ends in 1 and works, and 10 four-car trains are stuck. `check_pages.py` already contains all of these answers.

---

## What works and should be kept

- One convention everywhere: the leftmost car on the page sits next to the junction and arrives first, and departed cars read 1 2 3 left to right. The three-panel worked picture (start, car 3 waiting in the siding, finish) is exactly the "input, intermediate step, output" example the standard asks for.
- K–1 is real mathematics at a smaller scale. It decides which trains work with three, four and five cars and finds every train ending in car 1 (only 4 3 2 1 works). It runs an open search for stuck four-car trains, where 12 slots do not reveal the true count of 10, and it ends with a partner game. Problems are one or two sentences each.
- The 2–3 sequence goes from trying (P1–P3) to a conjectured rule (P4) to testing it (P5) to a new use of the idea (P6). P6's four trains have 3, 2, 4 and 3 allowed gaps, a good contrast.
- The 4–5 parity dot lattice keeps paths on legal points. P5 (path to train) before P6 (is the correspondence one-to-one and onto?) is the right order, and the four P5 paths decode to four different trains: 1 5 3 2 4, 5 2 1 4 3, 4 1 3 2 5 and 5 3 2 1 4.
- The cases mix ✓ and ✗ in roughly balanced numbers: K–1 P2 5/3, P5 3/3; 2–3 P3 4/4, P5 3/3; 4–5 P2 5/5. Only their positions need changing (item 1).
- Every long 4–5 train fits the five-car siding. I confirmed that at most 4 cars are ever in it, even for the stuck trains when driven as far as they go.

## Independent checks run

My scripts are in `/tmp/claude-0/-home-claude/d1d23a10-bfbf-5b59-a13a-5f6afdbf2b0f/scratchpad/critic-scripts/`.

- **Every printed train:** a brute-force search over all legal move sequences agrees with every intended answer in K–1 P1, P2 and P5, 2–3 P3 and P5, and 4–5 P2.
- **Uniqueness:** the successful drive is unique for every order of up to 7 cars.
- **Counts:** 1, 2, 5, 14, 42, 132 and 429 trains work for 1 to 7 cars, so the totals in 4–5 P1 (24 trains) and P7 (120 and 720 trains) are correct.
- **2–3 P6:** the allowed gaps are 2143 → Y.Y.Y, 4321 → Y...Y, 1324 → YY.YY and 3124 → Y..YY. Summed over all 14 working four-car trains they give 42.
- **4–5 P5:** I read the four paths from the drawn coordinates and decoded them by hand. The trains above are all valid and all different.
- **4–5 P8:** with two sidings, 0 failures up to 6 cars. With 7 cars, 22 orders fail when sidings are unbounded and 51 when each siding holds 5 cars. All three printed trains work.
