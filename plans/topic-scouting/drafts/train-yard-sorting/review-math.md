# Mathematical review: train-yard sorting draft (v1)

Reviewer: independent math check (CRITIC-MATH stage). Draft read: `draft/k-1.pdf` (5 pages), `draft/grades-2-3.pdf` (4 pages), `draft/grades-4-5.pdf` (5 pages). The PDF text matches the train lists in `draft/src/build.py`.

How I checked: I wrote my own scripts and did not use `verify.py`. The first does an exhaustive search over every in/out move sequence for one siding, with an unlimited siding and with a 5-car siding. It also gives the shallowest siding each run needs, the number of successful runs, and a direct 2-3-1 pattern test. The second searches two sidings in a row, with and without a first-in-first-out waiting track between the mats. Checked facts:

- With one siding, a train can be sorted exactly when it has no 2-3-1 pattern. This holds for every order of 1 to 8 cars.
- Sortable counts for 1 to 8 cars: 1, 2, 5, 14, 42, 132, 429, 1430.
- Every sortable train has exactly one successful run.
- Mountain paths of 4 ups and 4 downs and sortable four-car trains match one to one: 14 of the 70 up/down words.
- With two sidings, every order of up to 6 cars can be sorted. Among 7-car orders, 22 fail with unlimited sidings and 51 fail with 5-car sidings. Adding a waiting track between the mats changes no answer.

I also checked every diagram against the text: the rules picture, the worked 1 3 2 path, the four Problem 5 paths, the lattice dot rows and the insertion rows.

## Located problems

### 1. Grades 4–5, page 1 (shared rules) and page 5 (Problems 7 and 8): the answers assume a siding longer than the printed one

- **Text.** Rules: "Make extra cars from paper squares for trains with more than five cars." Problem 7: "How many of the 720 six-car trains? Explain how you know your counts are right." The outline's mat has a siding "exactly one car wide and five cars long".
- **Evidence.** The intended answer is 132, which needs a siding that holds 6 cars. With the printed 5-car siding, 131 six-car trains can leave in order. The one exception is 6 5 4 3 2 1: all five larger cars must sit in the siding before car 1 arrives, so the siding needs six places.
  - Problem 8 has the same issue. With unlimited sidings, 22 of the 5,040 seven-car trains fail. With two 5-car sidings, 51 fail. The 29 extra failures come only from the siding being full.
  - Every drawn train in Problem 2, including the 6-, 7- and 8-car ones, needs at most 4 places, so Problem 2 is not affected.
- **Smallest fix.** Extend the rules sentence: "Make extra cars from paper squares for trains with more than five cars, and pretend the siding is long enough to hold every car." The counts 132 and 22 are then correct.

### 2. Grades 4–5, page 5, Problem 8: the last question's answer needs seven cars, and testing smaller trains suggests the wrong answer

- **Text.** "Is there any train that cannot leave in order through two sidings?"
- **Evidence.** The answer is yes. However, every train of 1 to 6 cars can be sorted with two sidings, with either siding length.
  - The smallest failing trains have 7 cars, and only 22 of the 5,040 fail with unlimited sidings. One example is 2 4 3 5 7 6 1. All 22 end in car 1.
  - The three printed trains (2 3 1, 3 4 1 2, 2 5 3 4 1) all leave in order with two sidings.
  - A child with five cubes plus a few paper squares will find that everything works. The natural conclusion, "no such train", is false. Nothing on the page and no facilitator guide warns the adult.
  - Showing that a particular 7-car train fails needs a full impossibility argument, which is hard at this level.
- **Smallest fix.** Give the size: "Is there a train of seven cars that cannot leave in order through two sidings?" If the organizer prefers the open wording, pass the facts above to the adult at the 4–5 table.

### 3. Grades K–1, page 1 (shared rules): no rule keeps the cars in line, so another reading makes every train sortable

- **Text.** "Line up a train on the arrival track the way it is drawn. Each car drives down into the siding and then out to the departure track. Only the top car in the siding can drive out."
- **Evidence.** The text never says that the front car of the arrival train must go in first, or that cars cannot pass one another. The upper-band rules do say this: "sends the front car of the arrival track", "never jump over each other".
  - Under the K–1 reading, a child may take car 1 from the back of 2 3 1 and drive it first. Then every train in Problems 1, 2, 3 and 5 works, and the 2-3-1 obstruction disappears.
  - The picture and the launch show the right action, but the read-aloud text allows the wrong one.
- **Smallest fix.** Add one short sentence after the first: "The cars stay in line and never jump over each other."

### 4. Grades 2–3, page 1, Problem 1: the page shows more boxes than there are answers

- **Text.** "Write every different train you can make with cars 1, 2, 3." The page has nine empty three-car trains with check boxes.
- **Evidence.** There are 3! = 6 trains, and five of them can leave in order (only 2 3 1 cannot). Nine boxes on a "write every" task suggest nine answers. Children may keep searching or fill the extra boxes with repeats.
- **Smallest fix.** Draw six trains, as two rows of three.

### 5. Grades 4–5, page 3, Problem 4: sixteen grids for fourteen paths

- **Text.** "Draw the path of every four-car train that can leave in order, and write the train under its path." The page has 16 lattice grids, each with a four-car answer row.
- **Evidence.** Exactly 14 four-car trains can leave in order, and each has exactly one path (checked exhaustively). The children already found the number 14 in Problem 1, so the extra two grids contradict their own count. Some children may also force invalid paths or repeats into the spare grids.
- **Smallest fix.** Draw 14 grids, for example three rows of four plus a row of two. This gives nothing away, because the count comes from Problem 1.

### 6. Grades K–1, page 4, Problem 4: twelve boxes for ten answers

- **Text.** "Find trains of cars 1, 2, 3, 4 that cannot leave 1, 2, 3, 4, and write each one below. How many different ones can you find?" The page has 12 empty four-car trains.
- **Evidence.** Exactly 10 four-car trains cannot leave in order: 1342, 2314, 2341, 2413, 2431, 3142, 3241, 3412, 3421, 4231. A child who fills all 12 boxes must have written a repeat or made a driving error, and the boxes suggest 12 exist. Seven of the ten already appear as ✗ answers in Problems 2 and 3. The three new ones are 2 3 1 4, 2 4 1 3 and 3 1 4 2.
- **Smallest fix.** Draw 10 boxes. If the organizer does not want the box count to reveal the answer, keep 12 but tell the K–1 adult (a non-mathematician) that the total is 10.

## Notes that are not errors (for whoever rehearses the materials)

- K–1 Problem 5, first train "5 4 3 2 1": this is the only drawn single-siding train that needs all five places in the siding, so it fills the siding exactly. Every other drawn train in all bands needs 4 places or fewer. Check with the real cubes or squares that five cars fit inside the drawn siding walls. This is untested physically.
- The rules picture in every band shows the run of 1 3 2. That train is also a task in K–1 Problem 1, grades 2–3 Problem 1 and grades 4–5 Problem 1, so its answer (✓) is visible on the page. With three cars this cannot be avoided, and the mathematics is correct.

## Verified answers (no issue found)

**K–1**
- P1: only 2 3 1 fails.
- P2: ✓ for 4321, 2143, 3124, 1432, 4132; ✗ for 3412, 1342, 4231.
- P3: the six fillings are exactly the 3! arrangements of 2, 3, 4. Only 4 3 2 1 works.
- P5: ✓ for 54321, 21543, 51324; ✗ for 45123, 13524, 32514.
- P6: 42 of the 120 five-car lineups work.

**Grades 2–3**
- P2: 14 can, 10 cannot.
- P3: ✓ for 41325, 52143, 32154, 12534; ✗ for 31542, 24351, 15342, 45321.
- P4: a train fails exactly when some car is followed later by a bigger car and, after that, by a smaller car (a 2-3-1 pattern).
- P5: ✓ for 21534, 14235, 54132; ✗ for 53412, 42513, 34521.
- P6: all four trains are sortable. Dashed boxes are counted 0 to 4 from the left, where 0 is before the first car and 4 is after the last.
  - 2 1 4 3: boxes 0, 2, 4
  - 4 3 2 1: boxes 0, 4
  - 1 3 2 4: boxes 0, 1, 3, 4
  - 3 1 2 4: boxes 0, 3, 4
  - The rule: car 5 fits in a gap exactly when every car to its left is smaller than every car to its right.

**Grades 4–5**
- P1: 2 3 1 fails; 14 of 24.
- P2: ✓ for 31254, 51423, 214365, 1726354, 43128576; ✗ for 24153, 13542, 361245, 3217564, 41328675.
- P3: no 2-3-1 pattern.
- P4: the worked path for 1 3 2 is up, down, up, up, down, down, matching the labels "1 in, 1 out, 3 in, 2 in, 2 out, 3 out". It is drawn correctly on the lattice.
- P5: drawn paths match up/down words. Trains:
  - UDUUUDDUDD → 1 5 3 2 4
  - UUUDDUUDDD → 5 2 1 4 3
  - UUDUUDDDUD → 4 1 3 2 5
  - UUUUDDDUDD → 5 3 2 1 4
- P6: one way only, one train per path, and exactly the 14 paths that never dip below the start.
- P7: 42 and 132 (but see issue 1).
- P8: all three printed trains work with two sidings (but see issues 1 and 2).
