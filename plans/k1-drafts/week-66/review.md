# Review: Week 66 K–1 draft (Lamplighter streets, GGT66-K-v1)

Reviewed: `draft/k-1.pdf` (8 pages, US Letter), rendered at 100 dpi for every page and at 200–400 dpi for the rules diagram, the Problem 6 arrows and Problem 8. Sources read: `draft/src/pages.py`, `problems.py`, `lamps.py`, `check.py`. I checked every printed picture by hand against `problems.py`, and checked every count with my own breadth-first search, separate from the author's code (`review-check/verify.py`: 7-lamp street compared with a 21-lamp street, plus exact-length word counts).

## Verdict

This is a strong draft. The mathematics is correct. The problem order follows the brief: single lamps, then where the walker ends, then the order of visiting, then counting the shortest ways with an explanation, then the dead end set against a non-dead end, then evenness. None of the pictures copies the launch goal, its mirror image, or any older-band target. The pages have no titles, no encouragement and no hints. The working street is sized for the 17 mm counters, and all 8 pages are full enough for a quick pair.

The fixes I recommend are mostly about K–1 operation and wording:

- The partner rule has lost its check on flips.
- "Dark street" contradicts the drawn and counter convention.
- The record squares are too small for kindergarten pencils.
- Problem 5's "every way" record cannot be read by the children.
- Problem 8's sentence is hard to follow when read aloud.
- Two arrow labels collide with their arrows.

None of these requires changing the problem sequence.

## Math check (all confirmed)

| Problem | Picture (writer notation: lit places; walker) | Fewest | Notes |
|---|---|---|---|
| 1 | {0}; 0 / {}; −2 / {2}; 2 / {−3}; −3 | 1 / 2 / 3 / 4 | one shortest word each |
| 2 | {2}; walker 3 / 1 / 0 / −1 | 4 / 4 / 5 / 6 | overshoot and step back tie at 4 |
| 3 | {1,2}; 2 / {−1,2}; 2 / {−3,1}; −3 / {−2,3}; 3 | 4 / 6 / 7 / 9 | wrong order costs 10, 13, 15 |
| 4 | {−2,1}; walker 1 / 0 / −1 / −2 | 7 / 8 / 7 / 6 | walker at 0 has 2 shortest words, both orders tie |
| 5 | {0,1}; 0 / {0,1,2}; 0 | 4 / 7 | exactly 2 and 4 shortest words |
| 6 | {−2,−1}; −1, then L / R / F | 5, then 4 / 6 / 4 | not a dead end; R is the harder move |
| 7 | {−1,0,2}; 0, then L / R / F | 9, then 8 / 8 / 8 | dead end (confirmed: all three moves give 8) |
| 8 | {0}; 0, towers 1–4 / {}; 0, towers 1–4 / {1}; −1, towers 4–7 | works: 1, 3 / 2, 4 / 4, 6 | 2, 4 / 1, 3 / 5, 7 never work |

Every answer is the same on the printed 7-lamp street and on an endless street. Every picture is within three places of home. The diagrams match `problems.py` exactly; I checked each lamp, walker and home mark on all 8 pages. The longest shortest build is 9 cubes, inside a child's dozen and the 12 record squares.

## Must fix

### 1. The partner rule no longer controls which lamp gets flipped (page 1, rules)

The draft says: "One partner moves the walker and the other flips lamps." The brief is explicit that this rule exists only on paper. Week 2 failed because children changed whichever lamp they wanted. The older pages guard against this with "the other flips only after pointing to the walker's lamp." The draft drops the pointing check, and "flips lamps" even reads as permission to flip any lamp. This is the one behaviour the session context says the materials and the partner must enforce.

Fix: "One partner moves the walker. The other points to the lamp under the walker, then flips it." (Or: "...flips only the lamp under the walker.") Keep "Swap jobs for each new picture."

### 2. "Dark street" contradicts the picture convention (page 1 rules; Problems 6 and 7)

On these pages a lit lamp is a filled black circle, and the counter's dark side means lit. The guide's fallback is paper squares that are dark on one side, with the dark side up for lit. Yet the rules say "Start every picture from a dark street," and the dark street is drawn as seven white circles and built with every counter light side up. A K–1 child hears "dark" and sees, or turns over to, the light side. Problems 6 and 7 repeat the phrase ("Build each picture from a dark street...").

Fix: say "with every lamp off" (or "all lamps off") on the page. For example, rules: "Start every try with every lamp off and the walker at home." Problems 6 and 7: "Build each picture, starting with every lamp off, with as few moves as you can." The shared launch can still call it the dark street aloud. Optional, if the reviser wants a stronger visual cue for "on": add a few short rays around each filled lamp in the target pictures. Rays keep the filled-means-lit convention and make "lit" unmistakable without colour.

## Should fix

### 3. The record squares are too small for K–1 pencils (Problems 1–7)

Each target has 12 squares of 5.7 mm (`SQ = 5.7` in `pages.py`). Kindergartners colouring 5.7 mm boxes with a pencil will overrun them or give up. This is the one recurring pencil task in the packet. Pages 2–5 also have a blank band of about 80–90 mm between the last target and the working street (page 2: about 91 mm; page 5: about 81 mm), so there is room.

Fix: make the squares at least 8–9 mm and keep at least 12 of them, so that the box length does not hint at the answer (the longest answer is 9; a child's best try may be 10–12). Two rows of 6 under each picture fit the current 80 mm frame width. The blank band absorbs the extra height on pages 2–5. On pages 1, 6 and 7, check the fit after the change; page 1 may need slightly tighter row spacing.

### 4. In Problem 5, the children cannot read the record of "every way" (page 5)

"Find every way to build each picture with the fewest moves." The only record is five ruled lines beside each picture. Per the brief, the adult writes the L/R/F words there, which children cannot read. Finding every way is the mathematics of this problem: knowing which ways you already have, and deciding whether a new try is different. With letter words only, the adult does the completeness check for the children. This is the "adult operating the investigation" case in AGENTS.md, not routine adult recording. The difference between the ways (lighting a lamp on the way out or on the way back) is visible on the street but leaves no trace that a child can read.

Two acceptable fixes, reviser's choice:
- (a) Keep the lines for the adult, and accept that this problem is adult-recorded. Then nothing on the page needs to change, but the future guide should tell the adult to read each word back by acting it out.
- (b) Replace the lines with about 5 blank rows of 8 squares per picture, all the same length so the length gives nothing away. The child marks each move in order: a filled dot for a flip, ← or → for a step. With this record, FRFL and RFLF look different to a child who cannot read. It is a new notation, so it needs one tiny worked row (a non-task instance, for example → dot for "step right, flip"). Put that row in the problem, not in the rules.

Option (b) is more in the spirit of the brief. Option (a) is lighter for the adult. Either way, the 5-line or 5-row allowance is good: it hides that the answers are 2 and 4.

### 5. Problem 8's sentence is hard to follow when read aloud once (page 8)

"Build each picture with exactly as many moves as there are cubes in a tower beside it. Circle every tower that works." Read aloud, "a tower beside it" sounds like one tower, and the inverted "as many moves as there are cubes in" is hard to follow on one hearing. Do not switch to "as tall as" either: the drawn cubes are 5 mm and real cubes are about 2 cm.

Fix, for example: "For each tower, try to build the picture in exactly that many moves. Circle every tower that works." Or: "Try to build each picture using exactly the cubes in each tower beside it. Circle every tower that works."

### 6. Arrow labels collide with their arrows (page 1 rules diagram; Problems 6 and 7)

In the rules diagram, the foot of the "L" touches the upper arrow, and the lower arrow passes through the "F" (visible at 200 dpi and above). On pages 6 and 7, the "L" and "F" labels touch their arrow shafts.

Fix: give the labels clearance. In `moves_picture()` and `one_more()`, change the node anchor to `above left` and `below left`, with a larger `inner sep` of about 2.5 pt, or place each label beside the arrowhead. Optional, for K–1: add a small ← or → inside or beside the L and R labels, because all three arrows point right and a pre-reader cannot tell "L" from the arrow's direction.

## Minor

- **"Start every picture" should say "Start every try."** Children rebuild the same picture several times when they look for fewer moves. Each try must start from all lamps off, the walker home and no tower. "Every picture" can be heard as once per picture. Item 2's rewording already covers this.
- **"Under a picture" should say "Under each picture"** (rules, last sentence).
- **The repeated "from a dark street" in Problems 6 and 7 is justified.** The arrows invite building the right-hand pictures from the left-hand one. Keep a reminder there, reworded as in item 2. It is the only place where repeating a shared rule earns its place.
- **Source hygiene.** The `__main__` block of `lamps.py` still checks an older Problem 6 instance ({1,2} with the walker at 1). That does not match what is printed ({−2,−1} with the walker at −1). `check.py` checks the printed pictures correctly. Delete or update the stale block so later readers are not misled.
- **Physical readiness.** Counter fit on the 20 mm lamps (24 mm pitch, about 7 mm between 17 mm counters), the pawn in the 17 mm walker spot, and K–1 handling of towers up to 9 cubes have not been tried. When the packet is filed, record it as unpiloted and unrehearsed, as the brief says.

## Keep as is

- **Problem sequence and instances.** Problems 1–4 each add one idea: walk only versus flip in Problem 1; overshoot versus step back in Problem 2; order in Problem 3; ending changes order in Problem 4. Four contrasting builds per page is right for K–1, and stopping anywhere is fine.
- **Problems 6 and 7 as a pair.** Problem 6 is a typical target with one harder neighbour (5, then 4/6/4). Problem 7 is a dead end (9, then 8/8/8). Choosing the second dead end, not the 7-move one that is the older Problem 3/4 target, respects "do not copy the older problems." The record squares remove the 33-cube problem, because towers need not stay standing.
- **Problem 8's three rows.** They give opposite parity patterns (1 and 3 work in one row, 2 and 4 in the next, then 4 and 6), which is the right experience for the "goes up by twos" conjecture. The dark-street row is a good zero case. Use "every lamp off" wording if it is mentioned.
- **The working street on every page,** with walker spots above the lamps and the home mark under the middle lamp. Target pictures at 8 mm lamps are legible and plainly too small for counters, so children build on the street.
- **The rules diagram as the convention example.** It shows each move from one non-task position. It needs only the label fix in item 6.
- **Header, footer and page numbers.** These are correct on all 8 pages.

## Out of scope but needed before use

There is no facilitator guide. The K–1 adult is the parent volunteer, not a mathematician. Before this table runs, that adult needs at least the answer table above, the shortest words (in `check.py` output), and the "no quicker" argument for Problem 5: each lit lamp needs its own flip, and the walker must reach the farthest lamp and come back.
