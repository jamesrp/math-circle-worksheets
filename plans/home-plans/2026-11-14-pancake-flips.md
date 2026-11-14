# Home plan: pancake flips

Weekend of November 14 and 15, 2026 (James picked it November 14, alongside Chomp), at the kitchen table: James with Jay, Rose and perhaps a third child. **Untried:** nobody has played this plan yet, and every time is a guess. Nothing to print. It is a home version of the [pancake flips draft](../topic-scouting/drafts/pancake-flips/) without its worksheets, and borrows that draft's review notes on materials and on 4-2-3-1. Every fact below is checked by [src/pancake_check.py](src/pancake_check.py).

## At the table

- A stack is written top to bottom, 1 the smallest lid: 3-1-4-2 has lid 3 on top and lid 2 on the plate. To build it, start at the plate: 2, then 4, then 1, then 3.
- A flip: slide a finger under any lid, lift it and everything above it, turn that part over, put it back. Goal: smallest on top, biggest on the plate.
- Rose's recipe: find the biggest lid that isn't in its place, flip it to the top, flip it down to its place. Nobody can beat it on 3 lids.
- Hardest stacks of 4 (4 flips each): **3-1-4-2** (build 2, 4, 1, 3), **2-4-1-3** (build 3, 1, 4, 2), **4-2-3-1** (build 1, 3, 2, 4).
- Stacks where the recipe takes 5 but 3 will do: **2-4-3-1** (flip 3, 2, 4) and **3-2-4-1** (flip 2, 3, 4).
- Fewest flips that always work: 3 lids 3, 4 lids 4, 5 lids 5, **6 lids 7**.
- Stop on a high point: Rose's recipe win, or Jay's reason a stack can't be done faster.

## The mathematics, for you

**The puzzle.** A stack of n lids of different sizes; a flip turns over the top k of them (any k from 2 to n), which reverses their order. Sort it, smallest on top. Each flip undoes itself, so the puzzle can be run backwards: a stack someone scrambled in k flips can be sorted in k.

1. **Theorem (the recipe always works, in at most 2n − 3 flips).** Flip the biggest unsorted lid to the top, then flip it down to its place; it never moves again. Each lid from the biggest down to lid 3 costs at most 2 flips, and the last two lids at most 1, so at most 2(n − 2) + 1 = 2n − 3. The checker confirms the bound is reached for 2 to 7 lids. *Limits:* it is a recipe, not the fastest way. On 3 lids it always uses the fewest flips. On 4 lids it wastes flips on 4 of the 24 stacks (1-2-4-3 and 1-4-3-2 take it 4, not 3; 2-4-3-1 and 3-2-4-1 take it 5, not 3). On 5 lids it wastes flips on 45 of 120 stacks, up to 3 extra.
2. **Theorem (a lower bound you can see).** Call two neighbouring lids a *good pair* if their sizes are next to each other (like 2 and 3), counting the plate as one size bigger than the biggest lid. A sorted stack has every pair good. A flip changes only one pair, the one where your finger went in, so it adds at most one good pair. So **a stack with b bad pairs needs at least b flips.** The zigzags 3-1-4-2 and 2-4-1-3 have all 4 pairs bad (3–1, 1–4, 4–2, and 2 on the plate), so they need 4 flips, and 4 is enough. *Limits:* the bound is often not the answer. 4-2-3-1 has only 3 bad pairs and still needs 4: each of its three flips leads to 2-4-3-1, 3-2-4-1 or 1-3-2-4, and each of those needs 3 (the first two have 3 bad pairs; the third takes trying). The two hardest stacks of 6 have 6 bad pairs and need 7: a 6-flip sort would have to fix a pair with every flip, and following only pair-fixing flips from either stack always gets stuck.
3. **What is true, by computer search** (every stack, breadth-first search in the checker). The fewest flips that always suffice is 1, 3, 4, 5, 7, 8 for 2 to 7 lids. With 3 lids only one stack needs 3 flips: 1-3-2. With 4 lids exactly three stacks need 4: 3-1-4-2, 2-4-1-3, 4-2-3-1. With 5 lids, 20 of the 120 stacks need 5. With 6 lids only two need 7: 5-3-6-1-4-2 and 4-6-2-5-1-3. So "n lids, n flips" holds up to 5 lids and fails at 6. On the three hardest stacks of 4 the recipe happens to use the fewest flips (4); the recipe is wasteful elsewhere. Cited, not rechecked: the puzzle was posed in 1975 in the *American Mathematical Monthly* under the pen name Harry Dweighter; Gates and Papadimitriou (1979) proved the first good general bounds and introduced burnt pancakes; nobody knows a formula, and exact answers are known only for small stacks.
4. **Burnt pancakes (stretch).** Now each lid must also end rim down, and every lid in a flip turns over, so flipping just the top lid counts. Fewest flips that always suffice: 1, 4, 6, 8, 10 for 1 to 5 lids (checked). The right order with every lid rim up needs 2n flips: 4 for 2 lids, 6 for 3, 8 for 4.

**What children might find.** By experiment: every stack can be sorted; some need more flips than others; the same stack can be sorted in different numbers of flips. As conjectures: "4 lids never needs more than 4", "n lids, n flips" (true to 5, false at 6). As explanations: the recipe, which works for any number of lids, and good pairs, which prove a zigzag can't be done in 3. Why the worst cases are 4 and 5 for 4 and 5 lids is a computer result; the 6-lid monster can be argued at the table but takes patience.

## Materials and setup (2 minutes)

- 4 or 5 lids of clearly different sizes: jar lids, coasters, small plates, or paperback books. A 6th for the stretch. Flat things stack and flip best, and lids are thick enough to read the order from the side; paper circles aren't, and from above a big one hides the smaller ones. Nesting cups work only mouth up and nested inside each other, where the order hides; skip them.
- A placemat or cutting board as the plate.
- Nothing to write with. Count flips out loud; for a record, one sticky note with the best count for a stack.
- In the plain game, ignore which way up a lid lands.

## The route

Each part stands alone. Stop after any of them and pick up anywhere next time.

**1. Launch (3 minutes).** Stack three lids as 2-3-1 (build: smallest on the plate, then the biggest, then the middle one on top). "These pancakes are in a mess. A flip: put your finger under any lid, lift it and everything above it, turn it over, put it back. I want the smallest on top and the biggest on the plate." Flip the top two (now 3-2-1), then all three (1-2-3), counting "one, two." Each child scrambles and sorts three lids once. Say only whether a flip is allowed. *Watch for* lifting lids from the middle, or turning only one lid in a group.

**2. Rose's part (5 to 10 minutes).**

- *Three lids, her recipe.* "Find the biggest. Flip it to the top. Then flip it to the bottom." Then the top two, if they're wrong. Do it with her a couple of times, then let her run it. Her tricky stack is 1-3-2 (build: middle, biggest, smallest on top): it needs all three flips, and no way is faster.
- *Chef.* She scrambles three lids for Jay or the third child, and counts their flips out loud.

*Rose's moment:* "Can you sort it in fewer flips than Rose?" On 3 lids her recipe always uses the fewest, so nobody can beat her; let Jay try to. Also, she scrambles in 2 flips and says "You get 2." *Stop* when she would rather build towers.

**3. Fewest flips (10 minutes).** Jay and the third child, 4 lids. Scramble one for them; whoever sorts it, then "Can you do it in fewer?" Then they scramble for each other with a promise: "I scrambled it in 3 flips; you get 3." (Always possible, because each flip undoes itself; wait for someone to notice why.) Then: "What's the worst stack of 4? Make one that needs as many flips as you can." To find: no stack of 4 needs more than 4, and three stacks need exactly 4 (in "At the table"). Hint if asked: "Try putting lids next to sizes they don't belong with." *Watch for* "4 lids, 4 flips."

**4. Why not 3? (5 to 15 minutes).** Build 3-1-4-2. "I don't think anyone can sort this in 3 flips. Can you prove me wrong?" After some tries: "Which neighbours are already right? Count the plate as a lid one size bigger than the biggest." To find: none are right (3–1, 1–4, 4–2, 2 on the plate); a flip changes only the pair where the finger went in, so each flip fixes at most one; 4 bad pairs need 4 flips. Then, if keen: "Does that prove 4-2-3-1 needs 4?" (No: it has only 3 bad pairs, yet it needs 4. Try all three of its flips: each leads to a stack that still needs 3.)

**5. Beat the recipe (5 to 10 minutes).** "Use Rose's recipe on 4 lids. Can you find a stack where the recipe is slow and you're faster?" To find: 2-4-3-1 and 3-2-4-1 take the recipe 5 flips and can be done in 3; 1-4-3-2 and 1-2-4-3 take it 4 and can be done in 3. Surprise worth saying if they find it: the recipe is perfect on the three hardest stacks.

**6. More lids (open).** "With 5 lids, what's the most flips you'd ever need? With 6?" Let them guess before they play. The answers are 5, then 7, so the pattern breaks. If they want the 6-lid monster: 5-3-6-1-4-2 (build from the plate: 2, 4, 1, 6, 3, 5). It has 6 bad pairs, so 6 flips would have to fix a pair every time; if Jay tries only pair-fixing flips, he always gets stuck. That is why it needs 7.

**7. Burnt pancakes (stretch, for Jay).** "Each pancake has a burnt side: rim up is burnt. Now every lid must also end rim down, and you may flip just the top one." Start with 2 lids, right order, both rim up: "Can you fix it in 3?" (No: it needs 4.) Then 3 lids, the same way: 6.

**When to stop.** On a high point: Rose's recipe beating someone, or the "every pair is wrong" reason. Next time, start at Move 5 or 7.

## How it went

(Add a dated line after the weekend.)
