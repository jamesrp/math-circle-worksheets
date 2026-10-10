# Week 84 independent mathematical review

The selected Grades 2–5 student packet checks out mathematically. All four problems, both worked examples, all eight café cards, all eight headband cards, and the three pictured deals were checked independently. All eight student PDF pages and all five original facilitator PDF pages were rendered and inspected. No numerical or theorem error was found. This is a mathematical review, not classroom validation or a physical rehearsal.

## Located procedural ambiguity to clarify

**Facilitator, page 2, common launch.** The instruction says: “show how one private observation filters possibilities, using a worked non-target arrangement.” It then asks to “keep one unchanged public set throughout each round.” The guide should explicitly say that a private filter is temporary and does not remove cards from the shared public set. The present wording can be implemented correctly, but a durable private elimination changes the game.

**Counterexample:** start with the seven publicly allowed worlds and actual deal BBR. Doll 1 sees BR, so its private compatible worlds are BBR and RBR. If a coach leaves only those two cards in the public set, doll 2, seeing B on doll 1 and R on doll 3, finds only BBR and incorrectly proves blue in round 1. With the correct shared seven-world set, doll 2 also considers BRR, so it must say NOT YET in round 1.

**Smallest fix:** add that the coach points to, overlays, or temporarily lifts the privately matching subset, then restores the unchanged public set before another doll's calculation. Only the public announcement or the completed simultaneous response tuple removes public possibilities. This also clarifies the student worked example without adding another student task.

## Exact solution keys

`P` means PROVE BLUE and `N` means NOT YET. Words are ordered by doll/person 1, 2, 3.

### Problem 1, student page 1

The four conversations have the following complete compatible deals:

| Conversation | Replies | All compatible YES/NO deals |
|---|---|---|
| 1 | NOT YET / NOT YET / NO | YYN |
| 2 | NO / NO / NO | NYY, NYN, NNY, NNN |
| 3 | NOT YET / NO / NO | YNY, YNN |
| 4 | NOT YET / NOT YET / YES | YYY |

These four sets are disjoint and cover all eight deals. In conversation 2, later speakers who personally hold YES nevertheless answer NO because the first public answer has already settled “everyone wants a cup” as false. The two-person worked example correctly leaves NY and NN after the first NO.

### Problem 2, student page 2

| Pictured deal | Round 1 | Round 2 | Round 3 | First required stopping round |
|---|---|---|---|---|
| BRR | PNN | PNN | PNN | 1 |
| BBR | NNN | PPN | PPN | 2 |
| BBB | NNN | NNN | PPP | 3 |

Replies in later columns are supplied only to clarify persistence; the task stops when every blue doll can prove blue. A red doll always reports NOT YET under this particular reporting rule, even once it can prove that it is red. The two-doll worked example is correct: among BB, BR, RB, seeing R on doll 2 privately leaves BR for doll 1.

### Problem 3, student page 3

Round 1 groups are `{BRR}`, `{RBR}`, `{RRB}`, and `{BBR, BRB, RBB, BBB}`. Their response tuples are PNN, NPN, NNP, and NNN respectively. In the four-world group, round 2 replies are respectively PPN, PNP, NPP, and NNN. Thus every deal is separated by its **public response history after round 2**. The BBB dolls nevertheless first publicly declare blue in round 3. Distinguishing the deal from the audience's viewpoint and a doll proving its own color at the start of a round are different milestones.

### Problem 4, student page 3

No doll can ever prove blue. Starting from all eight arrangements, every private view has both a blue-own-color and a red-own-color possibility. Every reply is NNN; this public observation removes no arrangement. The resulting public set is an exact fixed point, so induction establishes the same result for every later finite round. Merely checking a fixed number of rounds would not establish “ever”; the fixed-point argument does.

### Optional bounded grid, facilitator page 4

The off-diagonal domain 0–6 starts with 42 ordered cells. Alice's first ignorance leaves 30 cells in rows 1–5. Bob's ignorance leaves 12 cells in columns 2–4. Alice's next ignorance leaves exactly `(3,2)` and `(3,4)`. Bob, privately knowing 2, knows the actual pair `(3,2)`. The public audience still has both cells. A public “Alice is larger” leaves `(3,2)`; a bare “I now know both numbers” would leave both, since Bob with 4 also knows the pair. The finite upper boundary is necessary to this stated elimination sequence, and the guide correctly identifies this as a bounded adaptation.

## Evidence and limits

- `independent_math_check.py` is an owned standard-library checker. It imports no author implementation and constructs private information partitions and public response branches independently.
- `independent-math-evidence.json` records all café solution groups, every headband world's synchronized history, public group sizes, the no-announcement fixed point, and every surviving grid cell at each stage.
- `math-render/` contains every-page PyMuPDF and Ghostscript renders. The displayed tool previews appeared to omit repeated regions; direct pixel comparison shows all 13 PyMuPDF page images are identical whether rendered in a shared process or isolated processes. `render-pixel-evidence.json` verifies nonwhite header/footer regions on every page. There is no PDF defect from that presentation effect.
- The adversarial critic separately identified physical staging space and source-link clipping. Those concerns do not invalidate the finite inference rules, but should be repaired before delivery.
- No transfinite epistemic theorem, real children's reasoning speed, physical headband fit, card manipulation, or classroom readiness is certified by these checks.
