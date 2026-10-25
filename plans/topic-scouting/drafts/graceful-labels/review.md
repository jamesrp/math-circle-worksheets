# Review: Graceful labels, draft v1

Reviewed: `draft/k-1.pdf` (6 pp.), `draft/grades-2-3.pdf` (6 pp.), `draft/grades-4-5.pdf` (8 pp.). I rendered every page at 90 dpi, and the K4, K5, K–1 example and ruler-strip figures at 150 dpi. I read `gen.py`, the three `.tex` files and `answers-check.txt`, and ran my own enumeration. I also rebuilt the packet from a copy of `draft/src/`: `build.sh` runs cleanly, the text matches the delivered PDFs, and the LaTeX logs have no overfull or underfull boxes.

## Verdict

This is a strong draft. Every answer is mathematically correct. The format is clean: header, footer, "Problem N:" labels, no titles, no encouragement, no hints. The draft also covers all three kernels in the 4–5 band, and K–1 gets real "decide whether it can be done" work. Three problems should be fixed before approval:

1. The 2–3/4–5 shared rule states the success condition only for 5 links, and its own example contradicts it.
2. K–1 never shows how to record a tower as a number in a dot, yet Problem 3 depends on that convention.
3. In 4–5, a long trial-and-error problem (loops of 7 and 8) comes before the central parity explanation. Most children may never reach the proof.

The remaining items are smaller wording, sequencing and physical-fit issues.

## Mathematics (all verified independently)

| Item | Claim on page / implied answer | Check |
|---|---|---|
| K–1 P1, path of 3, towers 1, 2 | find all | 4 ways: 1-0-2, 2-0-1, 0-2-1, 1-2-0; 7 boards, so the board count does not reveal the answer |
| K–1 P2, path of 4, towers 1–3 | find all | 4 ways: 0-3-1-2, 3-0-2-1 and reversals |
| K–1 P3, 3-link star, centre printed 0/1/2/3 | finish or cross out | centre 0 and 3 work (6 each); centre 1 and 2 impossible. The leaves are then forced to the same three values, so differences are 1, 1, 2 however they are arranged |
| K–1 P4, triangle, towers 1–3 | which tower left over | 1 or 2 (the empty dot, 0, must be used) |
| K–1 P5, square, towers 1–4 | which tower left over | 1 or 3 |
| K–1 P6 path of 5; P7 fork tree | label | 8 and 12 labellings |
| 2–3 P2 fork, H-tree | label | 12 and 48 labellings |
| 2–3 P3, 5-link star | middle cards | 0 or 5 only (the link of difference 5 must touch the middle) |
| Loops 3–8 | which can be labelled | 3: 12, 4: 16, 5: 0, 6: 0, 7: 168, 8: 384 |
| 4–5 P6: 9, 10, 11, 12, 100, 101 | which can be shown impossible | 9, 10, 101 (sum 1+…+n odd). The wording "can you show" is honest, because 11, 12 and 100 are possible only by Rosa's construction |
| 4–5 P7 ruler | 4 marks on 0..6; 5 marks on 0..10 | {0,1,4,6}, {0,2,5,6}; none with 5 marks. A child-accessible proof: k odd marks give k(5−k) ∈ {0,4,6} odd distances, but 1..10 contains 5 odd numbers |
| 4–5 P8 K4, K5 | label or explain | K4: 0,1,4,6; K5: none |
| 4–5 P9 trees of 7–9 dots | find one that cannot be labelled | none exists (all trees up to 35 dots are checked); the open-ended phrasing is appropriate |

All drawn networks have the intended dot and link counts, and the regular polygons are regular. I traced the 10 boxes on the K5 drawing: each sits on exactly one link and away from the crossings.

## Must fix

### 1. The 2–3/4–5 shared rule only works for 5 links, and the example contradicts it (2–3 p.1, 4–5 p.1)
"If a network has 5 links, use cards from 0 to 5 … The network is labelled when its link numbers are 1, 2, 3, 4 and 5, each once." The ✓ example directly below has 2 links, cards 0–2, and link numbers 1 and 2. Read literally, that example fails the stated condition. The general rule ("link numbers 1 up to the number of links") is never stated. Each child has to infer it from one instance plus the captions.

"Use cards from 0 to 5" also reads as "use all of them". That reading breaks on every loop (one card left over) and on K4/K5 (3 and 6 left over). Problem 3/4 then patches the loops with "Each loop has one card left over", but P8 (K4, K5) has no such note.

Suggested fix: state the rule generally and let the captions carry the specifics. For example: "Put a different number card on each dot, choosing from the cards named under the network. In the box on each link, write the difference between the numbers at its two ends. The network is labelled when its link numbers are 1, 2, 3 and so on up to the number of links, each once." Caption the example "cards 0 to 2", like every working board.

### 2. K–1: the conversion from tower to written number is never shown (K–1 pp. 1–5)
The opening example shows towers standing on dots and a number in the link box, but never a number written in a dot. Yet:
- P1 and P2 ask for "all the ways" on small boards (dots about 1.4–1.5 cm), which are too small for towers. A child must record each way somehow, and nothing shows how.
- P3 prints 0, 1, 2, 3 inside the centre dots of the small stars. A non-reading kindergartner has never been told that a printed "2" in a dot means a 2-cube tower stands there, or that "0" means an empty dot.

This is exactly the "unfamiliar conversion" case in the project guidance: input, intermediate step, output. Suggested fix: add a recorded copy to the opening example beside each tower pair: dot "4", box "3", dot "1", and dot "0", box "2", dot "2". Do this in the picture, not in words.

### 3. 4–5 sequencing hides the main proof behind a time sink (4–5 pp. 3–5)
The outline's central 4–5 kernel is "prove the loop rule by parity". The draft goes: P3 loops 3–6 → P4 loops 7 and 8 → P5 explain 5 and 6 → P6 which loops. P4 is long trial and error. Only about 1 in 240 arrangements of the cards on the 7-loop works, and about 1 in 945 on the 8-loop. A child working in order can spend the rest of the hour on P4 and never reach P5.

Suggested order: P3 (loops 3–6), then the explanation (current P5), then loops 7 and 8 (current P4), then the list (current P6). This order is also more logical. Once a child knows the parity reason, the 7- and 8-loops become the natural question: parity does not forbid them, so can they actually be done? That then sets up "which can you show cannot be labelled" for 9–101.

## Should fix

### 4. Explanation prompts give away the decision, and "cannot" has no way to be recorded
- 2–3 P4 and 4–5 P3 say "Label each loop that can be labelled." That presupposes some cannot, but gives no way to mark a decision. K–1 P3 has "or cross it out if it cannot be done"; the older bands should get the same.
- 2–3 P6 and 4–5 P5 say "Explain why the loops with 5 and 6 links cannot be labelled." This announces which loops fail, one or two pages after the child is supposed to decide that for themselves. In 2–3, P6 sits on the same page as P5. It also prescribes the conclusion, which the guidance on open questions warns against.

Suggested wording: "Label each loop, or cross it out if it cannot be done." Then later: "Explain why the loops you crossed out in Problem N cannot be labelled." Alternatively: "Which loops in Problem N cannot be labelled? Explain how you know." 4–5 P8 already uses the better pattern ("Label each network, or explain why it cannot be done").

### 5. Weak endings in K–1 and 2–3
The context says the deeper questions belong late, where the quickest children arrive. Both younger packets end on their shallowest task.
- **K–1** ends with P6 (path of 5) and P7 (fork tree). Each is a single labelling with no decision. P6 is the natural next step after P1–P2 (paths of 3, 4, 5 dots), so it belongs right after P2. To end with something deeper, one option is a 4-link star with towers 1–4: "Which towers can stand on the middle dot?" The answer is none (an empty middle) or the 4-tower. This mirrors 2–3 P3, needs 10 cubes, and is a decide-and-check task.
- **2–3** ends with P7 (an 11-dot path) right after the hardest problem in the packet (P6). Move it next to P1, or merge it into P1 as a fourth path. If space allows, the four-counter ruler from 4–5 P7 (0 and 6 fixed; subtraction within 6) would give 2–3 a small-scale taste of kernel 3. "Draw a tree of your own with 6 dots and label it" would give them a taste of the conjecture. Both are optional, since the outline does not require either for 2–3.

### 6. Physical fit is unrehearsed, and some sizes look risky
These are hypotheses to check with the real materials, not observed failures.
- **Number cards vs dots and boxes.** Dots are 2.5 cm across (the outline asked for about 3 cm). Link boxes are 0.8 cm, with only 0.35–0.4 cm of line between a dot and its box. The card size is not specified anywhere. A card about the size of the dot will touch or cover box corners on the 45° links of the zigzag 6-dot path (2–3 P1, 4–5 P1) and on the slanted sides of the pentagon. A 3 cm card covers boxes on most slanted links. Check with the real cards. Either specify small cards (2 cm or less) or lengthen the links or the dot-to-box gap.
- **Box size for writing.** Children write link numbers up to 10 (path of 11 dots, K5, 8-loop) in 0.8 cm boxes, erasing as they rearrange cards. "10" in 0.8 cm is cramped; 1.0–1.2 cm would be safer. The 2–3 P3 small-star boxes are 0.56 cm.
- **K–1 recording boards.** The small boards have dots of 1.4–1.5 cm and boxes of 0.66 cm, which is small for kindergarten handwriting. Fewer, larger boards would suit K–1 better, for example 5–6 boards with dots of about 2 cm and boxes of about 1 cm. Keep more boards than answers so the count does not give the answer away.
- **Ruler strip vs counters (4–5 P7).** The working strip has 1.6 cm squares, about the most that 11 squares across a portrait page allow. Standard 1-inch two-colour counters, ¾-inch counters and 2 cm snap cubes will not sit in one square. Specify small markers, about 1.5 cm or less, or print the strip on its own page in landscape.

## Minor

- **K4 drawing (4–5 P8):** the three inner links show only about 3–4 mm of line on each side of their boxes. The drawing is legible but cramped, and cards on the centre dot will crowd those boxes. A slightly larger K4, with the outer triangle side at about 5 cm, would help.
- **"Small star" (K–1 P3):** "star" is never introduced. Read aloud with pointing it works, but "each small picture" avoids a new word for non-readers.
- **Spelling:** the pages use British "labelled". The group is in Bellingham, so US children expect "labeled". The outline uses the British form, so this is the organizer's call.
- **4–5 P9** is a blank page with "trees of your own". That fits the open conjecture. A quick child who draws a path and stops would be helped by two or three printed starter trees, for example a 7-dot spider with three legs of length 2 and a caterpillar, with the remaining space blank.
- **2–3 P6 age fit (hypothesis).** The outline puts the parity proof in 4–5 and asks 2–3 only to "decide which cannot be done". Keeping the explanation as a late stretch for third graders is reasonable with a mathematician at the table. The adult will need a third-grade route, for example: each odd link number flips the label between odd and even; going round a loop must flip an even number of times; 1–5 and 1–6 each contain three odd numbers. That belongs in the future facilitator guide, not on the page.

## Suggestions outside the student pages (for the facilitator guide and materials)

- **Make the "each once" rule physical.** The lamp-puzzle lesson was that rules existing only on paper get ignored. One way to enforce this rule with materials: a second, differently coloured set of difference tiles 1–10 per pair, placed on the link boxes. A duplicate or a missing tile then shows at once, and nothing has to be erased while cards move. K–1 could use towers or tiles of 1–4 cubes the same way.
- **Launch coordination.** The 2–3/4–5 ✓ example (1-0-2 on a 3-dot path) is one of the four answers to K–1 P1. If the whole-group launch uses a 3-dot path with towers, as the outline suggests, choose one that is not graceful with towers of 0–2, or show only single links as the K–1 page does.

## What to keep

- The K–1 opening example: the darker "extra" cubes and the dashed line make "how many cubes taller" visible. It uses two single links, so it reveals no Problem 1 answer.
- The 4–5 ruler example (counters at 0, 2, 7, with arcs 2, 5, 7). It demonstrates "all pairs" without revealing {0,1,4,6}.
- K–1 P3–P5. They are real decision tasks for young children, and the phrase "left over" parallels the older bands' "one card left over".
- The honest wording of 4–5 P6 and P9. Also the order in 4–5 of ruler (P7) and then K4/K5 (P8), which leaves the connection between them for the child to discover.
- The format discipline across all 20 pages.
