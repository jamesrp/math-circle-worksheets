# Week 7: Take-away games — mathematical design

This document is for the page writer and the three adults. It fixes the problems, their exact instances, their answers, and the order. The writer turns each "Page words" entry into page text (the wording may be polished, but the instances, rules and asks must stay as given) and draws the pictures described. Everything under "Answer" and "Watch for" is for adults only and must not appear on student pages.

All answers below were checked by brute-force game search; see the last section, "Verification", for what each script in `design-checks/` confirmed.

---

## 0. Conventions that hold in every band

**The game.** One pile of counters (later, two or three piles or rows). Two players take turns. A rule says how many counters you may take on a turn. You can never take more than are there. Whoever takes the last counter wins. The one exception is the K–1 "poison" problem (K–1 Problem 8), where the page says plainly that whoever takes the last counter loses.

**Every rule on every page allows taking 1.** Because of this, a player always has a legal move while counters remain, every game ends with someone taking the last counter, and no starting position can leave a child stuck. Rules such as "take 2 or 3", which would strand a single counter, are deliberately left out. `run_all.py` checks this for every rule used.

**What "who wins" means.** A pile is a *losing pile* when the player who must move from it loses, however well they play, against an opponent who plays well. On the pages this is phrased as "you would rather be 2nd" (K–1), "the second player can always win, however the first player plays" (2–3), and, once the idea has been used, "losing pile" (4–5, from Problem 2 on). A pile is losing when every move leads to a winning pile. It is winning when at least one move leads to a losing pile. A winning strategy means always moving to a losing pile, and it must answer every reply. That is Kernel 1, and every band is built on it.

**Layout warning for the writer (this matters).** Do not lay out a row of piles or a table in rows whose length is the period the child is trying to find, or a multiple of it. For example, piles 1–12 under "take 1 or 2" must not go in rows of 3 or 6, and a table for "take 1, 3, or 4" must not go in rows of 7. The losing piles would then line up in a column before the child had found them. Use rows of 5 for K–1 strips and rows of 10 (or a single long row) for the tables in grades 2–5, as specified per problem.

The one deliberate exception is 4–5 Problem 6. It uses rows of 10 for a period-5 pattern because the point there is to see where the repeating *starts*.

**Whole-group demonstration (about 3 minutes).** The organizer plays "take 1 or 2" from a pile of 7 counters against a child volunteer, once or twice. The demonstration shows only the action: take turns, take exactly 1 or 2, put taken counters aside, and whoever takes the last counter wins. It says nothing about who should win or how. This is the shared action for all three bands.

**Adults.** Every answer, every winning move, and every reply tree a child might need checked is written out below, so any adult can run any band. If the organizer wants a suggestion, the 4–5 group gets the most from a research mathematician (Problems 5–9: impossibility arguments, the pigeonhole argument, sums of games). The parent volunteer can run K–1 entirely from these notes.

**Sharing time (end of the hour).** Suggested prompts: K–1, "Which piles are traps?" (3, 6, 9, 12). Grades 2–3, "Kai's first move from 13 was right. How did he still lose?" Grades 4–5, "Why are piles of 4 and 6 a loss, when each pile alone is a win?" The organizer may add that for bigger families of games, where a move can also split a pile in two (octal games), nobody knows whether the patterns always repeat. That question is Guy's conjecture, and it is still open.

---

## 1. K–1 (two kindergartners and one first grader)

### 1.1 Mathematical thread

The children find out how to win a game by thinking backward from the end, with real counters and very few words.

- **Kernel 1 (backward induction).** With "take 1 or 2", a pile of 3 is a *trap*: whatever you take, your partner takes the rest. So you want to *leave* 3 for your partner (piles 4 and 5). A pile of 6 is a trap too, because whatever your partner takes from 6, you can leave 3. A winning plan must answer *every* move the partner can make. Problem 3 asks the child to answer all four ways the partner can play from 6, which is "find all the ways" at K–1 scale.
- **Kernel 2 (patterns; changing the rule).** The traps come every third pile: 3, 6, 9, 12. Change the rule and the traps change. With "take 1, 2, or 3" the traps are 4 and 8, and 3 is no longer a trap. With "take 1 or 3" the traps are every other pile. In the poison game the traps are 1, 4, 7. Taking the most is often wrong: from 4 under "take 1 or 2", or from 5 under "take 1, 2, or 3".
- **Kernel 3 (two piles), as play.** With two equal rows the second player wins by copying in the other row. Two rows of 2 and 2 is a win for the second player, even though a single pile of 4 is a win for the first. With three rows of 2, the first player takes a whole row and then copies.

The kinds of real mathematics in this band are: how to win, whether winning is possible (going first from 3, 6, 9 or 12, it is not), all the ways (Problem 3 covers every partner line), and patterns.

### 1.2 Packet rule (top of page 1, read aloud once)

"Play with a partner. Take turns. On your turn, take 1 counter or 2 counters. Whoever takes the last counter wins."

### 1.3 How the pages look

- Counters are drawn as circles about 1.5 cm across, in rows of at most 5 (like a ten-frame), so children can count them.
- "Circle who you would rather be" always offers two large chips printed **1st** and **2nd**.
- An adult reads every problem aloud. Each problem is at most two short sentences, and the pictures carry the rest.
- With three children, two play while the third watches and then plays the winner. The children swap who goes first often.

### 1.4 Problems

**K–1 Problem 1**
- *Page words:* "Play with 3 counters, then 4, then 5. Circle who you would rather be."
- *Pictures:* three piles (3, 4 and 5 counters), each on its own line with a **1st** chip and a **2nd** chip beside it.
- *Materials:* real counters. Several games per pile, swapping who starts.
- *Record:* one circled chip per pile. About one third of a page.
- *Answer:*
  - 3: **2nd**. Whatever the first player takes, 1 or 2 counters are left, and the second player takes them all.
  - 4: **1st**, but only by taking 1, which leaves 3.
  - 5: **1st**, but only by taking 2, which leaves 3.
- *Watch for:*
  - The belief that going first is always better.
  - At 4, a child who grabs 2 (the most), loses, and circles 2nd. Whether "always" is meant against every partner move is the adult's question to raise.
  - Listen for "leave 3". Once children have noticed that 3 is bad, the adult may give it a name, such as "trap".

**K–1 Problem 2**
- *Page words:* "Play with 6 counters, then 7, then 8. Circle who you would rather be."
- *Pictures:* piles of 6, 7 and 8 (a row of 5 plus the rest), each with the chips.
- *Record:* chips. About one third of a page. Problems 1 and 2 fit on one page.
- *Answer:*
  - 6: **2nd**. Whatever the first player takes, the second player leaves 3.
  - 7: **1st**, only by taking 1, which leaves 6.
  - 8: **1st**, only by taking 2, which leaves 6.
- *Watch for:*
  - Children trying to leave 3 straight from 7 or 8. That is impossible in one move.
  - The step forward is seeing that 6 is as bad as 3. A child who says "from 6, whatever you take, I can make it 3" has backward induction.

**K–1 Problem 3**
- *Page words:* "Your partner goes first with 6 counters. In each picture, cross out what you take so that you win."
- *Pictures:* four panels, drawn as a small tree.
  - Panel A: a row of 6 counters with the leftmost 1 drawn faded or dashed (the partner took it), so 5 are solid.
  - Panel B: a row of 6 with the leftmost 2 faded, so 4 are solid.
  - Under A and B, an arrow to the words "3 left — partner's turn again".
  - Panel C: 3 counters with the leftmost 1 faded, so 2 are solid.
  - Panel D: 3 counters with the leftmost 2 faded, so 1 is solid.
- *Materials:* act out each panel with counters before marking it.
- *Record:* cross out counters in the four panels. About two thirds of a page.
- *Answer:* the only winning reply in each panel is:
  - A: take 2, leaving 3.
  - B: take 1, leaving 3.
  - C: take 2, the last ones.
  - D: take 1, the last one.
  
  These four panels are *every* way the partner can play from 6, so together they are a complete winning plan.
- *Watch for:*
  - Children re-crossing the partner's faded counters.
  - Whether the child notices that both top panels end at 3.
  - This is the "answer every reply" idea. Ask "Could your partner have done anything else?"

**K–1 Problem 4**
- *Page words:* "Here are piles from 1 to 12. Color every pile you would not want on your turn."
- *Pictures:* 12 boxes, each holding a pile of 1, 2, …, 12 counters (counters in rows of 5 inside the box), with a small numeral in the corner. The boxes go in **rows of 5**: 1–5, 6–10, then 11–12. Do not use rows of 3 or 6, or the traps line up in a column. Boxes are about 3.5 cm wide.
- *Materials:* build and play any pile they are unsure of.
- *Record:* color boxes. A full page.
- *Answer:* **3, 6, 9, 12**. Every third pile.
- *Watch for:*
  - New work here is 9–12. Did the child check 9, or just guess "it's like 3 and 6"? Both are worth hearing.
  - A child who can say what comes after 12 (15) has the pattern.

**K–1 Problem 5**
- *Page words:* "Now you may take 1, 2, or 3 counters. Play with 3, 4, 5, and 8 counters, and circle who you would rather be."
- *Pictures:* piles of 3, 4, 5 and 8, with chips.
- *Record:* chips. About half a page.
- *Answer:*
  - 3: **1st**. Take all 3.
  - 4: **2nd**.
  - 5: **1st**, only by taking 1, which leaves 4.
  - 8: **2nd**.
  
  The traps are now 4, 8, 12.
- *Watch for:*
  - Carrying over "3 is a trap" from the old rule.
  - At 5, taking 3 (the most) loses, because the partner takes the last 2.
  - Children who say "now it's every 4".

**K–1 Problem 6**
- *Page words:* "Now you may take 1 or 3 counters, but not 2. Color every pile you would not want on your turn."
- *Pictures:* piles 1–10 in boxes, **rows of 5** (1–5, 6–10).
- *Record:* color boxes. About two thirds of a page.
- *Answer:* **2, 4, 6, 8, 10**. Every other pile.
- *Watch for:*
  - At 2, children want to take 2, which is not allowed.
  - Children noticing "every other one", or connecting it to even numbers.

**K–1 Problem 7**
- *Page words:* "Make two rows like the picture. Take turns taking 1 or 2 counters from one row, and circle who you would rather be."
- *Pictures:* three cases, each drawn as two horizontal rows: 2 and 2; 4 and 4; 4 and 5. Chips beside each case.
- *Record:* chips. About half a page.
- *Answer:*
  - 2 and 2: **2nd**.
  - 4 and 4: **2nd**. Copy the partner's move in the other row.
  - 4 and 5: **1st**. Take 1 from the row of 5 to make 4 and 4, then copy. Taking 2 from the row of 4 (leaving 2 and 5) also wins, but no child needs to find that.
- *Watch for:*
  - The copycat idea.
  - Children who count the total. A single pile of 4 or of 8 is a win for 1st, but 2 and 2 and 4 and 4 are wins for 2nd.

**K–1 Problem 8**
- *Page words:* "Now whoever takes the last counter loses. Play with 3, 4, 5, and 7 counters, and circle who you would rather be."
- *Pictures:* piles of 3, 4, 5 and 7, with chips. The rule is still "take 1 or 2". A small picture of the last counter with a frowning face may help.
- *Record:* chips. About half a page.
- *Answer:*
  - 3: **1st**. Take 2, which leaves 1.
  - 4: **2nd**.
  - 5: **1st**. Take 1, which leaves 4.
  - 7: **2nd**.
  
  The traps are now 1, 4, 7, 10.
- *Watch for:*
  - Forgetting the reversed ending in the middle of a game.
  - Discovering that now you want to leave 1, and then 4.

**K–1 Problem 9**
- *Page words:* "Make three rows like the picture. Take turns taking 1 or 2 counters from one row, and circle who you would rather be."
- *Pictures:* three cases of three rows each: 1, 1, 1; 2, 2, 2; 3, 3, 3. Chips beside each case.
- *Record:* chips. About half a page.
- *Answer:*
  - 1, 1, 1: **1st**. Three turns in all, so 1st takes the last counter.
  - 2, 2, 2: **1st**. The only winning first moves take a whole row of 2. That leaves 2 and 2, and then 1st copies.
  - 3, 3, 3: **2nd**. Whenever 1st takes from a row, 2nd can take the rest of that row (each row is a "3 trap"). Other winning replies also exist.
- *Watch for:*
  - Children trying to copy with three rows.
  - The "aha" that taking a whole row turns this into Problem 7.

### 1.5 Time budget (minutes)

| Problem | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| Quick child | 5 | 5 | 5 | 6 | 6 | 5 | 6 | 5 | 5 | **48** |
| Typical child | 7 | 7 | 7 | 8 | 8 | 7 | 8 | 7 | 7 | 66 |

A typical child finishes around Problem 5 or 6 in 40 minutes, having found the trap pattern and met one rule change. A quick child still has Problems 7–9 (copycat, poison, three rows), each a new game with a new surprise. The pages come to about 6, with Problems 1 and 2 sharing a page and Problems 8 and 9 sharing a page.

### 1.6 Why the level is right

- **Easy entry.** Piles of 3–5 with only two possible moves. A game lasts under a minute, and the outcome is visible. Recording is circling, crossing out, or coloring, so no writing is needed.
- **Real challenge.**
  - Seeing why 3 is a trap and using it on 4 and 5.
  - The two-step thought that 6 is a trap because every move from 6 lets me make 3.
  - Answering *every* partner move (Problem 3).
  - Seeing that a rule change destroys the old traps (Problems 5, 6, 8).
  - Copying (Problems 7, 9).
- **Same ideas as the older bands.** These are the older bands' ideas at a smaller scale: classify every pile (Problems 4 and 6), test a plan against every reply (Problem 3), see that a pattern changes with the rule (Problems 5, 6, 8), and play a sum of games (Problems 7, 9).
- **As much to do as the other bands.** Nine problems, about 48 minutes for a quick child.

---

## 2. Grades 2–3 (four third graders)

### 2.1 Mathematical thread

- **Kernel 1.** The children classify every pile from 1 to 20 under "take 1, 3, or 4". To do it efficiently they must work upward and reuse what they know about smaller piles. A pile is a second-player pile when every move leaves a first-player pile. They then test claimed strategies against *every* reply. One claim (Ravi's) is beaten by only one of the three possible replies. One habit (Kai's) starts with a correct move and still loses later.
- **Kernel 2.** The second-player piles under "take 1, 3, or 4" are 2, 7, 9, 14, 16, …. They repeat every 7, and the children use the repeat to handle piles of 23–31. Changing the rule changes the pattern (Problem 5). Taking the most is right from 11 and wrong from 8 and 6 (Problems 3 and 7).
- **Kernel 3, as a glimpse.** Two piles under "take 1, 3, or 4". Piles of 1 and 3, and piles of 4 and 6, are wins for the second player, even though each pile alone is a win for the first. Piles do not simply add up.

### 2.2 Packet rule (top of page 1)

"Two players take turns taking counters from a pile. Each problem says how many counters you may take on a turn, and you can never take more than are there. Whoever takes the last counter wins."

Keep the phrase "who can always win, the first player or the second player, however the other one plays" throughout. No new terms are needed in this band.

### 2.3 Problems

**2–3 Problem 1**
- *Page words:* "The rule is: take 1 or 2 counters. For piles of 7, 9, 11, and 12 counters, decide who can always win, the first player or the second player, however the other one plays. If it is the first player, write the first move."
- *Pictures:* the four piles drawn small, in rows of 5.
- *Materials:* counters, played in pairs.
- *Record:* a 4-row table with the columns pile | who can always win | first move. About a quarter of a page.
- *Answer:* in each case the move given is the only winning move.
  - 7: first player, take 1 (leaves 6).
  - 9: second player.
  - 11: first player, take 2 (leaves 9).
  - 12: second player.
- *Watch for:*
  - Deciding from one game.
  - Whether children reason from small piles (3, 6) or play everything out.

**2–3 Problem 2**
- *Page words:* "Now the rule is: take 1, 3, or 4 counters. For every pile from 1 to 20, decide who can always win, the first player or the second player. Write 1st or 2nd under each pile."
- *Pictures:* a table of piles 1–20 in **two rows of 10**, with the pile number above each box. Boxes are about 1.6 cm. Not rows of 7.
- *Record:* "1st" or "2nd" in 20 boxes. About a third of a page.
- *Answer:* **2nd at 2, 7, 9, 14, 16**, and 1st at all the others. The winning first moves, for adults:

  | Pile | 1 | 3 | 4 | 5 | 6 | 8 | 10 | 11 | 12 | 13 | 15 | 17 | 18 | 19 | 20 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | Take | 1 | 1 or 3 | 4 | 3 | 4 | 1 | 1 or 3 | 4 | 3 | 4 | 1 | 1 or 3 | 4 | 3 | 4 |

- *Watch for:*
  - Forgetting that from 3 or 4 you can take everything.
  - Children who replay each pile from scratch, compared with those who reuse earlier boxes. The key sentence to listen for is "from 7, every move leaves 6, 4, or 3, and those are all 1st piles".

**2–3 Problem 3**
- *Page words:* "The rule is: take 1, 3, or 4. Four children make claims. Decide if each claim is right. If it is right, show how that child wins whatever the other player does. If it is wrong, show how the other player wins."
  - (a) Maya: "There are 8 counters and I go first. I take 4, because taking the most is best. Then I will win."
  - (b) Leo: "There are 11 counters and I go first. I take 4. Then I will win."
  - (c) Ravi: "There are 6 counters and I go first. I take 1. Then I will win."
  - (d) Zoe: "There are 9 counters. I will go second. Then I will win."
- *Record:* for each claim, circle *right* or *wrong*, with space for lines such as "if they take __, then __". About a quarter of a page per claim, so one full page.
- *Answer:*
  - (a) **Wrong.** The other player takes all 4. Maya's winning first move is take 1, which leaves 7.
  - (b) **Right.** Take 4 is the only winning move from 11, leaving 7. Leo's replies (the other player moves, then Leo):
    - They take 1 (6 left). Leo takes 4 (2 left). They must take 1, and Leo takes the last.
    - They take 3 (4 left). Leo takes 4 and wins.
    - They take 4 (3 left). Leo takes 3 and wins (or takes 1, leaving 2).
  - (c) **Wrong, and sneaky.** From 5 the other player beats Ravi only by taking 3, which leaves 2. Ravi must then take 1, and the other player takes the last counter. If the other player takes 1 or 4 instead, Ravi wins. A child who tests only one or two replies may wrongly call Ravi right. Ravi's winning first move is take 4, which leaves 2.
  - (d) **Right.** Zoe's replies to each first move from 9:
    - They take 1 (8 left). Zoe takes 1 (7 left), and goes on as Leo does from 7.
    - They take 3 (6 left). Zoe takes 4 (2 left).
    - They take 4 (5 left). Zoe takes 3 (2 left).
    - From 2 the other player must take 1, and Zoe takes the last.
- *Watch for:*
  - "I tried it and she won" as proof. Push toward *every* reply.
  - Ravi is the test case for this.
  - A child who notices that Leo's plan and Zoe's plan both go through 7 is linking ideas.

**2–3 Problem 4**
- *Page words:* "The rule is: take 1, 3, or 4. For piles of 23, 25, 28, and 31 counters, decide who can always win. If it is the first player, write the first move. Explain how you know who wins with 28 counters."
- *Record:* a 4-row table and about 5 lines. About a third of a page.
- *Answer:*
  - 23: second player.
  - 25: first player, take 4 (leaves 21).
  - 28: second player.
  - 31: first player, take 1 (leaves 30) or take 3 (leaves 28).
  
  The expected explanation is "the 2nd piles go 2, 7, 9, 14, 16, 21, 23, 28, 30: add 5, then 2, again and again", or "every 7 it starts over". Why it must continue is a 4–5 question. A quick child can be asked it out loud.
- *Watch for:* children extending the table one pile at a time (fine, but slow), compared with children using the repeat.

**2–3 Problem 5**
- *Page words:* "Here are three other rules. For each rule, find every pile from 1 to 15 where the second player can always win, and describe the pattern."
  - (a) Take 1 or 3.
  - (b) Take 1, 2, or 3.
  - (c) Take 1 or 4.
- *Record:* three single rows of 15 boxes (mark the 2nd piles), each with 2 lines for the pattern. About half a page.
- *Answer:*
  - (a) 2, 4, 6, 8, 10, 12, 14. Every even pile.
  - (b) 4, 8, 12. Every fourth pile.
  - (c) 2, 5, 7, 10, 12, 15. Add 3, then 2. It repeats every 5.
- *Watch for:* comparing (c) with "take 1, 3, or 4". Both have pairs two apart and then a gap. In (a), taking 2 is not allowed.

**2–3 Problem 6**
- *Page words:* "Now there are two piles. On your turn, take 1, 3, or 4 counters from one of the piles. Whoever takes the last counter wins. For each start, decide who can always win; if it is the first player, write a first move. Explain how the second player wins with piles of 1 and 3."
  - (a) 5 and 5.
  - (b) 1 and 3.
  - (c) 3 and 4.
  - (d) 4 and 6.
- *Pictures:* each start drawn as two small piles side by side.
- *Record:* a 4-row table and about 6 lines. About half a page.
- *Answer:*
  - (a) **2nd.** Copy the other player in the other pile.
  - (b) **2nd.** The second player's answers:
    - They take the single counter: take all 3.
    - They take 1 from the 3, leaving 1 and 2: take the single counter, which leaves a lone 2.
    - They take all 3: take the last one.
  - (c) **1st.** Take 1 or 3 from the pile of 4, leaving 3 and 3 or 3 and 1.
  - (d) **2nd.** The second player's replies:

    | They take | Leaving | You take | Leaving |
    |---|---|---|---|
    | 1 from the 4 | 3, 6 | 3 from the 6 | 3, 3 |
    | 3 from the 4 | 1, 6 | 3 from the 6 | 1, 3 |
    | 4 from the 4 | 0, 6 | 4 from the 6 | 0, 2 |
    | 1 from the 6 | 4, 5 | 1 from the 5 | 4, 4 |
    | 3 from the 6 | 4, 3 | 1 from the 4 | 3, 3 |
    | 4 from the 6 | 4, 2 | 4 from the 4 | 0, 2 |

- *Watch for:*
  - Adding the piles into one pile. A single pile of 4 or of 10 is a 1st-player pile, but (b) and (d) are 2nd.
  - The surprise that two 1st-player piles together make a 2nd-player start.

**2–3 Problem 7**
- *Page words:* "Kai plays 'take 1, 3, or 4' with a habit: on every turn he takes as many counters as he can (4 if there are at least 4, all 3 if there are 3, and 1 if there are 1 or 2). Kai always goes first. For which piles from 1 to 20 does Kai win however you play? Show how you beat Kai when he starts with 13."
- *Materials:* one child plays "Kai" like a robot.
- *Record:* 20 boxes ("Kai" or "me") in two rows of 10, and about 4 lines for the 13 game. About a third of a page.
- *Answer:*
  - Kai wins **only from 1, 3, 4, 6, 11**.
  - From 13: Kai takes 4 (9 left). You take 1 (8 left). Kai takes 4 (4 left). You take 4 and win.
  - From 13, 18 and 20, Kai's *first* move is correct, but his habit loses later. From 5, 8, 10, 12, 15, 17 and 19 his first move is already wrong.
- *Watch for:*
  - Children who copy the 1st piles from Problem 2. "Kai can win from 13" is true for a good player, but not for Kai's habit.
  - This is the strongest "test against every reply" lesson in the packet.

### 2.4 Time budget (minutes)

| Problem | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Total |
|---|---|---|---|---|---|---|---|---|
| Quick child | 5 | 8 | 9 | 5 | 8 | 8 | 8 | **51** |
| Typical child | 8 | 14 | 14 | 8 | 12 | 12 | 12 | 80 |

A typical child gets through Problems 1–3 and part of Problem 4 in 40 minutes. That covers the core: classifying with backward induction and testing claims. Problems 5–7 reward a quick child with new rules, two piles, and Kai. The pages come to about 5.

### 2.5 Why the level is right

- **Easy entry.** "Take 1 or 2" with piles under 12 can be settled by playing. Every task names exact piles and exact rules.
- **Real challenge.**
  - Twenty piles under "take 1, 3, or 4" cannot sensibly be done by playing every game. The children have to organize, and the natural organization is working upward. That is the mathematics, and the page does not suggest it.
  - Problem 3 makes "every reply" unavoidable: Ravi's claim survives two of the three replies.
  - Kai shows that a correct first move does not make a correct plan.
  - Two-pile starts break the "just add the piles" idea.
- **The outline's suggested emphasis.** This is exactly the outline's emphasis for grades 2–3: classify piles under {1, 3, 4} and test claimed strategies against every reply.

---

## 3. Grades 4–5 (two fourth graders and one fifth grader)

### 3.1 Mathematical thread

- **Kernel 2, in depth.**
  - Find the repeating patterns: {1, 2}: every 3. {1, 2, 3}: every 4. {1, 3, 4}: remainders 0 and 2 on division by 7. {1, 4}: every 5. {1, 4, 5}: every 8. {1, 3, 5}: even piles.
  - *Explain* why a pattern goes on forever. For {1, 3, 4} there is a remainder check: from remainder 0 or 2 every move lands outside {0, 2}, and from every other remainder some move lands inside.
  - Explain why some different rules give the same pattern. {1, 2, 4} behaves like {1, 2} because 4 leaves the same remainder on division by 3 as 1 does.
- **Inverse problems.** Design a rule for a given pattern, or show that none can exist. These use the two facts behind backward induction: two losing piles are never one allowed move apart, and every winning pile is one allowed move above a losing pile.
- **Eventually periodic.** With {1, 6, 9} the pattern does not start repeating until pile 10. In general it must eventually repeat, and the reason is the window argument (pigeonhole).
- **Kernel 3.** Two-pile sums. Piles split into "families". For {1, 3, 4} the families are {0, 2, 7}, {1, 3}, {4, 6} and {5}, and a two-pile start is a loss exactly when both piles are in the same family. These families are the Sprague–Grundy values 0, 1, 2 and 3, discovered rather than defined.

### 3.2 Packet rule (top of page 1)

"Two players take turns taking counters from a pile. Each problem says how many counters you may take on a turn. Every rule lets you take 1, and you can never take more than are there. Whoever takes the last counter wins."

The term *losing pile* is introduced in Problem 2, after the children have used the idea in Problem 1.

### 3.3 Problems

**4–5 Problem 1**
- *Page words:* "For each rule, find every pile from 1 to 20 where the second player can always win, however the first player plays. Then explain, for rule (b), why the second player can always win from those piles, and why the first player can always win from every other pile."
  - (a) Take 1 or 2.
  - (b) Take 1, 2, or 3.
- *Record:* two tables of piles 1–20 (two rows of 10 each), and about 6 lines. About half a page.
- *Answer:*
  - (a) 3, 6, 9, 12, 15, 18.
  - (b) 4, 8, 12, 16, 20.
  - The explanation for (b): from a multiple of 4, whatever the first player takes (1, 2 or 3), the second player takes the rest of 4, so the pile stays a multiple of 4 and the second player takes the last counter. From any other pile, the first player takes the remainder on division by 4 and is then in the second player's position. That is the only winning first move (checked).
- *Watch for:* explanations that cover only some replies, and explanations that forget the "every other pile" half.

**4–5 Problem 2**
- *Page words:* "From now on, call a pile where the second player can always win a **losing pile** (it loses for whoever has to move). The rule is: take 1, 3, or 4. Find every losing pile from 1 to 30, and describe the pattern."
- *Record:* a table of piles 1–30 in **three rows of 10** (not rows of 7), and 3 lines. About a third of a page.
- *Answer:* **2, 7, 9, 14, 16, 21, 23, 28, 30**. Add 5, then 2. It repeats every 7, at the piles with remainder 0 or 2 on division by 7.
- *Watch for:* children extrapolating after 2, 7, 9 instead of checking. Both "add 5 then 2" and "remainder 0 or 2 mod 7" are good descriptions.

**4–5 Problem 3**
- *Page words:* "The rule is: take 1, 3, or 4. For piles of 50, 53, 54, 56, and 100 counters, decide whether you would rather go first or second, and if first, what you take first. Then explain why your pattern keeps going forever, not just as far as you checked."
- *Record:* a 5-row table and about 10 lines. About half a page.
- *Answer:* each first move given is the only winning move.
  - 50: first, take 1 (leaves 49).
  - 53: first, take 4 (leaves 49).
  - 54: first, take 3 (leaves 51).
  - 56: second.
  - 100: second (100 = 98 + 2).
  
  The explanation is the remainder check (verified):
  - From remainder 0, taking 1, 3 or 4 gives remainder 6, 4 or 3.
  - From remainder 2, taking 1, 3 or 4 gives remainder 1, 6 or 5.
  - So from 0 or 2, no move reaches 0 or 2.
  - From remainder 1 take 1; from 3 take 1 or 3; from 4 take 4; from 5 take 3; from 6 take 4. Each reaches 0 or 2, and the move is always available because the pile is at least as big as the amount taken.
  
  Piles are labelled one after another from the bottom, so the rule "losing exactly when the remainder is 0 or 2" can never break.
- *Watch for:* "It worked to 30, so it works forever." That is the gap this problem is about. The full induction does not need to be stated formally.

**4–5 Problem 4**
- *Page words:* "For each rule, find every losing pile from 1 to 20 and describe the pattern. Then explain why rule (c) has the same losing piles as 'take 1 or 2'."
  - (a) Take 1 or 4.
  - (b) Take 1, 4, or 5.
  - (c) Take 1, 2, or 4.
  - (d) Take 1, 3, or 5.
- *Record:* four single rows of 20 small boxes (about 0.8 cm each, so a row fits the page width), with 2 lines each and 4 lines for the explanation. About two thirds of a page to a full page. Do not use rows of 10, because (a) and (d) would then line up in columns.
- *Answer:*
  - (a) 2, 5, 7, 10, 12, 15, 17, 20. Repeats every 5.
  - (b) 2, 8, 10, 16, 18. Repeats every 8.
  - (c) 3, 6, 9, 12, 15, 18.
  - (d) Every even pile.
  - Explanation for (c): from a multiple of 3, taking 1, 2 or 4 never reaches a multiple of 3. Taking 4 changes the remainder exactly as taking 1 does, since 4 = 3 + 1. From any other pile, taking 1 or 2 still reaches a multiple of 3.
  - For adults: adding any one move that is *not* a multiple of 3 to {1, 2} changes nothing, and adding a multiple of 3 always changes the pattern (checked for 3–30). Note also that (a), (b) and {1, 3, 4} all have losing piles at remainders 0 and 2, with periods 5, 8 and 7.
- *Watch for:* children recomputing (c) from scratch and then being surprised. Ask what is special about 4.

**4–5 Problem 5**
- *Page words:* "Invent a rule. For each list, find a rule whose losing piles are exactly the piles on the list, or explain why no rule can do it. Your rule must let you take 1; you choose any other numbers."
  - (a) 2, 4, 6, 8, 10, 12, … (every even pile).
  - (b) 5, 10, 15, 20, 25, … (the numbers ending in 0 or 5).
  - (c) 3, 5, 8, 10, 13, 15, 18, 20, … (the numbers ending in 0, 3, 5, or 8).
  - (d) 3, 7, 10, 14, 17, 21, 24, 28, … (add 4, then 3, again and again).
- *Record:* for each list, a line for the rule and about 4 lines for checking or explaining. About three quarters of a page.
- *Answer:* each verified over all rules with moves up to 14.
  - (a) Any rule whose numbers are all odd: "take 1 or 3", or even "take 1 only". An even move would join two even piles.
  - (b) It must include 1, 2, 3 and 4, because piles 2, 3 and 4 have to reach 0 in one move. It must include no multiple of 5. "Take 1, 2, 3, or 4" works.
  - (c) **Impossible.** 3 and 5 are both on the list, so taking 2 cannot be allowed (it would go from one losing pile to another). Then the only move from pile 2 is to pile 1, which is a winning pile, so 2 would be a losing pile. But 2 is not on the list.
  - (d) **Take 1, 2, or 6.** Moves of 3 and 4 are forbidden, because 0 to 3 and 3 to 7 are differences between list numbers. Pile 2 needs the move 2 to reach 0. Pile 6 needs the move 6, because 3 is forbidden. Every working rule contains 1, 2 and 6 and avoids moves with remainder 0, 3 or 4 on division by 7.
- *Watch for:*
  - Guess-and-check with a 1–20 table is fine.
  - The two general facts are the prize: no two losing piles are an allowed move apart, and every other pile is an allowed move above a losing pile.
  - In (c), children may give up rather than explain impossibility. The explanation is the point.

**4–5 Problem 6**
- *Page words:* "The rule is: take 1, 6, or 9. Find every losing pile from 1 to 35. Describe what happens. Does the pattern repeat right from the start?"
- *Record:* a table of piles 1–35 in rows of 10 (1–10, 11–20, 21–30, 31–35), and 3 lines. About a third of a page.
- *Answer:* **2, 4, 7, 12, 14, 17, 19, 22, 24, 27, 29, 32, 34.**
  - From pile 10 on, the losing piles are exactly those ending in 2, 4, 7 or 9. The pattern repeats every 5 (checked to 2000).
  - Pile 9 breaks the pattern, because you can take all 9 at once.
  - So the pattern repeats only from pile 10 on, not from the start. With rows of 10, the 9 column is visibly missing its first entry once the child has filled the table.
- *Watch for:* lookback mistakes (each pile needs piles 1, 6 and 9 below it). This is the concrete example of "eventually repeats", which Problem 7 uses.

**4–5 Problem 7**
- *Page words:* "Every rule so far has losing piles that, sooner or later, repeat in a pattern forever. Could some rule (it lets you take 1, and a few other numbers) have losing piles that never settle into a repeating pattern? Explain."
- *Record:* about half a page of space.
- *Answer:* **No.** Let k be the largest number in the rule.
  - Whether a pile is winning or losing depends only on the k piles just below it.
  - A stretch of k labels in a row can look only so many ways (2^k).
  - So among the first 2^k + 1 stretches, two are the same.
  - After two identical stretches, the next labels are computed the same way, so everything after them repeats forever.
  - Example for {1, 3, 4}: the stretch L W L W (piles 0–3) appears again at piles 7–10.
  
  Checked for all 511 rules with moves up to 10: the repeat of a stretch happens within the bound, and periodicity follows from it.
- *Watch for:*
  - "All the ones I tried repeat" is evidence, not an explanation.
  - The key sentence is "the next one only depends on the last few".
  - This is the natural place for the organizer to mention Guy's conjecture. When a move may also split a pile, a pile's value depends on many smaller piles, not on a fixed window, and nobody knows whether the patterns always repeat.

**4–5 Problem 8**
- *Page words:* "Now there are two piles. On your turn, take 1 or 2 counters from one of the piles. Whoever takes the last counter wins. In the grid, the square in row a and column b stands for starting piles of a and b. Mark every square where the second player can always win. Then explain how the second player wins from piles of 2 and 5."
- *Pictures:* a 7×7 grid, with rows and columns labelled 0–6. Squares are about 2 cm.
- *Record:* marks in the grid and about 5 lines. About two thirds of a page.
- *Answer:* the losing squares are those where both piles have the **same remainder on division by 3**. There are 17 squares:
  - (0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6).
  - (1,1), (1,4), (4,1), (4,4).
  - (2,2), (2,5), (5,2), (5,5).
  
  From 2 and 5, the second player always makes the remainders equal again:

  | They take | Leaving | You take | Leaving |
  |---|---|---|---|
  | 1 from the 2 | 1, 5 | 1 from the 5 | 1, 4 |
  | 2 from the 2 | 0, 5 | 2 from the 5 | 0, 3 |
  | 1 from the 5 | 2, 4 | 2 from the 4 (or 1 from the 2) | 2, 2 (or 1, 4) |
  | 2 from the 5 | 2, 3 | 1 from the 3 (or 2 from the 2) | 2, 2 (or 0, 3) |

- *Watch for:*
  - The diagonal (equal piles, copycat) comes first.
  - Unequal losing squares such as (1, 4) and (2, 5) are the discovery.
  - Row 0 and column 0 just repeat the single-pile answers.

**4–5 Problem 9**
- *Page words:* "Two piles again, but now take 1, 3, or 4 counters from one pile. Mark every square in the grid where the second player can always win. Explain how the second player wins from piles of 4 and 6."
- *Pictures:* an 8×8 grid, with rows and columns labelled 0–7. Squares are about 1.8 cm.
- *Record:* marks in the grid and about 6 lines. About two thirds of a page to a full page.
- *Answer:* a square is losing exactly when both piles are in the same **family**: {0, 2, 7}, {1, 3}, {4, 6} or {5}. That makes 18 squares, or 13 if you count a pair and its swap once: (0,0), (0,2), (0,7), (2,2), (2,7), (7,7), (1,1), (1,3), (3,3), (4,4), (4,6), (6,6), (5,5).
  
  Replies from 4 and 6 (the same as 2–3 Problem 6(d)):

  | They take | Leaving | You take | Leaving |
  |---|---|---|---|
  | 1 from the 4 | 3, 6 | 3 from the 6 | 3, 3 |
  | 3 from the 4 | 1, 6 | 3 from the 6 | 1, 3 |
  | 4 from the 4 | 0, 6 | 4 from the 6 | 0, 2 |
  | 1 from the 6 | 4, 5 | 1 from the 5 | 4, 4 |
  | 3 from the 6 | 4, 3 | 1 from the 4 | 3, 3 |
  | 4 from the 6 | 4, 2 | 4 from the 4 | 0, 2 |

  The families are exactly the piles with Sprague–Grundy value 0, 1, 2 and 3 (g(0..7) = 0, 1, 0, 1, 2, 3, 2, 0). This was checked against brute force up to 40×40.
- *Watch for:*
  - Children who start naming or numbering the families. That *is* the Grundy value. Only after they have found the families, the adult may say that mathematicians number them 0, 1, 2, 3.
  - Oral extension for anyone who finishes: put one pile under "take 1 or 2" next to one pile under "take 1, 3, or 4". The start is a loss exactly when the family numbers match (verified to 30×30).

### 3.4 Time budget (minutes)

| Problem | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| Quick child | 5 | 6 | 6 | 7 | 8 | 6 | 6 | 6 | 8 | **58** |
| Typical child | 8 | 10 | 10 | 12 | 14 | 10 | 10 | 10 | 14 | 98 |

A typical child reaches Problem 4 in 40 minutes. That covers the outline's emphasis for the band: find and explain patterns, and compare rules. Problems 5–9 reward a quick child with design and impossibility, eventual repetition, the general argument, and sums. The pages come to about 7.

### 3.5 Why the level is right

- **Easy entry.** Problem 1 is quick for this age (familiar every-3 and every-4 patterns), but it asks at once for an explanation that covers every reply and every pile.
- **Real challenge.**
  - Problem 3 asks *why* a pattern lasts forever.
  - Problem 5 asks children to reason about which moves a rule must or cannot contain, including a proof of impossibility.
  - Problem 7 is a genuine general argument (pigeonhole on windows).
  - Problems 8 and 9 lead to Grundy families without naming them.
- **Concrete throughout.** Every task names exact rules, piles and grids.
- **Explanation where it is the point.** Explanations are asked only where explanation is the point: why a strategy always wins (Problems 1, 8, 9), why a pattern continues (Problem 3), why two rules agree (Problem 4), why something is impossible (Problem 5), and why every pattern must repeat (Problem 7).

---

## 4. Notes for the writer

- **No hints on the pages.**
  - Do not tell children to start from small piles, to look at remainders, to copy, or to think backward. The tables are recording space only.
  - Tables must not be laid out in rows of the period being sought (see the layout warning in section 0).
- **K–1 wording.**
  - At most two short sentences per problem, using the page words above or something equally short.
  - The rule change in Problems 5, 6 and 8 must be the first thing said.
  - Use the **1st/2nd** chips throughout.
  - In Problem 3 the partner's counters must look clearly "already taken" (faded or dashed), as distinct from the counters the child crosses out.
- **Headings and labels.** The header and the "Problem N:" labels are the only headings. Sub-cases are listed as (a), (b), … inside a problem, with their pictures.
- **Order.** Keep the given order. Each band is ordered so that stopping anywhere is fine and the core comes first.

---

## 5. Verification (`design-checks/`)

Run `python3 design-checks/run_all.py`. It runs all three checks and writes the full log to `design-checks/output.txt`. The current log ends with **EVERYTHING PASSED**. All checks use brute-force game search, in which a position is losing exactly when every move leads to a winning position. Grundy values are used only to compare against brute force.

- **`games.py`** is the shared library. It contains:
  - backward-induction outcome tables for normal play and for the poison game;
  - all winning moves from a pile;
  - Grundy values;
  - eventual-period detection;
  - brute-force outcomes and winning moves for sums of two or three piles, possibly under different rules.
- **`run_all.py`** confirms that every rule on every page contains 1, so no non-empty position is stuck. It then runs the three band checks.
- **`check_k1.py`** confirmed:
  - **Problems 1–2:** piles 3, 6 → 2nd. Piles 4, 7 → 1st, and take 1 is the only winning move. Piles 5, 8 → 1st, and take 2 is the only winning move. Taking 2 from 4 loses.
  - **Problem 3:** from 6, all four partner lines have exactly one winning reply each: 5→take 2, 4→take 1, 2→take 2, 1→take 1.
  - **Problem 4:** the traps from 1 to 12 are 3, 6, 9, 12.
  - **Problem 5:** under {1, 2, 3}: 3 → 1st (take 3); 4 → 2nd; 5 → 1st (take 1 only); 8 → 2nd. The traps are 4, 8, 12.
  - **Problem 6:** under {1, 3} the traps from 1 to 10 are 2, 4, 6, 8, 10.
  - **Problem 7:** rows 2&2 and 4&4 → 2nd; 4&5 → 1st, with exactly two winning first moves. Copying wins for every pair of equal rows from 1 to 10 (brute force over every first-player line).
  - **Problem 8 (poison game):** 3 → 1st (take 2); 4 → 2nd; 5 → 1st (take 1); 7 → 2nd. The traps are 1, 4, 7, 10.
  - **Problem 9:** 1,1,1 → 1st; 2,2,2 → 1st, and the only winning first moves take a whole row; 3,3,3 → 2nd, and "finish the row" is a valid reply.
- **`check_23.py`** confirmed:
  - **Problem 1:** the answers and that each winning move is the only one.
  - **Problem 2:** the second-player piles 2, 7, 9, 14, 16, and the full table of winning first moves (3, 10 and 17 have two each).
  - **Problem 3:** Maya wrong and Leo right (take 4 from 11 is the only winning move). Ravi wrong, and taking 3 is the only refutation. Zoe right. The script prints the complete reply trees for Leo and Zoe.
  - **Problem 4:** 23, 28 → 2nd; 25 → take 4; 31 → take 1 or 3. The losing piles are exactly remainders 0 and 2 mod 7, checked to 35 here and to 600 in `check_45.py`.
  - **Problem 5:** the three patterns for {1, 3}, {1, 2, 3} and {1, 4}.
  - **Problem 6:** 5&5, 1&3 and 4&6 → 2nd; 3&4 → 1st, take 1 or 3 from the 4. Every reply from 1&3 and from 4&6 is listed. Piles 1, 3, 4 and 6 are each a 1st-player pile alone.
  - **Problem 7:** Kai's habit wins against best play only from 1, 3, 4, 6, 11. From 13, 18 and 20 his first move is correct but he still loses. The script prints explicit winning lines.
- **`check_45.py`** confirmed:
  - **Problem 1:** the patterns; multiples of 3 and 4 hold to 600; the remainder is the only winning take under {1, 2, 3}.
  - **Problem 2:** the list to 30; remainders 0 and 2 mod 7 hold to 600.
  - **Problem 3:** the five big piles with their unique winning moves, and the residue-by-residue remainder argument.
  - **Problem 4:** the four patterns and their periods (5, 8, 3, 2, each from the start). Adding a move x (3–30) to {1, 2} keeps the multiples of 3 exactly when x is not a multiple of 3. {1, 3, 5} gives the even piles, checked to 600.
  - **Problem 5:** an exhaustive search over all 8192 rules containing 1 with moves up to 14:
    - (a) works exactly for all-odd rules;
    - (b) works exactly for rules containing 1–4 and no multiple of 5;
    - (c) has **no** solution, and the impossibility argument's steps are checked;
    - (d) works exactly for rules containing 1, 2 and 6 and avoiding remainders 0, 3 and 4 mod 7.
  - **Problem 6:** the losing piles from 1 to 35 under {1, 6, 9}; "ends in 2, 4, 7 or 9, except 9" holds to 2000; the pattern settles into period 5 from pile 10; 9 is winning only by taking all 9.
  - **Problem 7:** for all 511 rules with moves up to 10, a window of k labels repeats within 2^k + 1 steps, and the labels repeat forever after it. Rules whose pattern does not repeat from the start include {1, 6, 9}, {1, 4, 10} and {1, 8, 11}.
  - **Problem 8:** losing exactly when the remainders mod 3 match (checked to 24×24); the 17 squares; every reply from 2&5.
  - **Problem 9:** the 18 losing squares; the four families; agreement with Sprague–Grundy (losing exactly when g(a) = g(b)) to 40×40; the families equal Grundy values 0–3; every reply from 4&6.
  - **Outline claims:** {1, 3, 4} has period 7 with losing remainders 0 and 2. A pile under {1, 2} next to a pile under {1, 3, 4} is losing exactly when the Grundy values match (checked to 30×30).
