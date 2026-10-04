# Week 8 return-visit companion: adversarial review

**Verdict: revise before approval.** The three investigations are mathematically sound and offer substantial concrete work. The definite brief mismatch is the rook-board size: every rook grid is 4 by 4, while the supplied outline requires 5 by 5. Problem 1 also needs a small clarification and a contrasting empty-pile example to support its stated all-starts goal.

Scope reviewed: `draft/return-visit.pdf`, all five landscape Letter pages, and `draft/src/return-visit.tex`, `check_math.py`, and `build.sh`. I rendered the actual PDF independently with PyMuPDF and viewed every page. I read the writer notes after that inspection. This review respects the explicit one-companion/three-investigation scope; there is no request for three packets, a forced K–1 Nim or rook version, or a facilitator guide. No draft source or base packet was edited.

## Required revisions

### 1. Restore the specified 5-by-5 rook boards (pages 4–5)

`\rookgrid` draws lines at indices 0 through 4 and uses a bottom-left star at `3.5 * cellsize`: these are **4-by-4** boards, confirmed on the rendered procedure example, both active boards, all twelve catalog boards, and the invented-pair record. The active boards measure 244.805 points per side, or 3.400 inches, with four 0.850-inch squares. Thus the square size passes, but the square count does not.

Use five squares in both directions, move the star and token vertical coordinates accordingly, and update pair offsets and labels so the orientation stays consistent across every version. The present coordinates 0 through 3 remain valid on a 5-by-5 board, so the six selected pairs need not change. Extend the mathematical domain check to distances 0 through 4 (625 four-coordinate states) and update the notes' board-size statements.

Do not shrink the active squares to make this fit. A 5-by-5 active board needs a 4.25-inch side. With the current top edge at 4.08 inches, it would reach 8.33 inches and collide with the footer. Move the active boards to an additional page, or rearrange the existing pages with sufficient measured clearance. Two 4.25-inch boards can fit side by side on landscape Letter. Recheck the reference-page spacing after increasing its grids: the current winner-label offsets were chosen for four rows.

### 2. Complete the two-pile boundary examples and define the requested domain (page 1)

The task says “Find a rule for all two-pile starts,” but the empty start `(0,0)` is not a playable start under the rule that the game ends when the final counter is taken. Qualify this as two-pile starts **with at least one counter**.

`(1,0)` is the sole printed case with an empty pile. A child can fit the observed cases with the incorrect rule that any empty pile makes the next player lose. Add a purposeful contrast such as `(2,0)` or `(3,0)`, preferably replacing an existing unequal positive two-pile case so the page does not grow denser. `(2,0)` is a first-player win: remove one counter, leaving the opponent to take the last one. This strengthens the boundary investigation without supplying the intended general rule.

### 3. Provide space for the rule actually requested on page 1

There are winner lines for the starts and three physical pile mats, but no recording space for “Find a rule.” Add a brief rule-answer area, as page 3 already has. Preserve the playable pile-mat area and avoid adding hints or a prescribed method. One clear line or small blank area is sufficient.

## Page-by-page findings

| Page | Actual content and entry | Findings |
|---|---|---|
| 1 | Grades 2–5; seven two-pile and five three-pile misère starts; three 2.9-by-1.4-inch pile mats | Clear legal move and losing-last-counter rule. Small reference drawings are suitable for rebuilding with counters. The cases include `(1,1)` versus larger equal piles and useful three-pile boundary cases. Plenty of play is available. Make the domain/example/answer-space fixes above. No unfamiliar code or representation requires a procedure example here. |
| 2 | Grades K–3; six two-coin starts; non-task worked slide; large 12-square strip | A genuine young-child entry with adult reading and two movable coins. Adjacent starts are contrasted with separated starts at several distances from the wall. The input `(4,10)`, arrow/destination intermediate, and output `(2,10)` demonstrate a legal slide without revealing the adjacency strategy. Rules and thick wall make square 0 unavailable. The large strip has twelve 0.850-by-0.850-inch squares and fits inside the page. All number labels are centered correctly. |
| 3 | Grades 2–5; eight three-coin starts and rule space; large strip | Clear continuation of the same game. Equal and unequal relevant gaps are contrasted across small and larger positions, including a non-adjacent left pair. The rule task retains children's choice of representation. Pairing/xor notation is not introduced on the student page, so a pairing-conversion example is not required. The 12-square active strip passes the same dimensional and labeling checks as page 2. |
| 4 | Grades 4–5; shared two-board rule and worked two-turn example; two active boards | The example correctly changes only A on the first turn and only B on the next. Stars consistently mark bottom-left destinations. The one-board-per-turn rule is explicit. The new cancellation/invention task is substantial and appropriate after familiar single-board play. Fix the required board count and resulting page layout. |
| 5 | Grades 4–5; six pairs and invented-pair record | Reference starts are legible and match the checked coordinates. The catalog includes identical winning components, two separately losing components, distinct winning components that cancel, and useful failures. In particular, Starts 3 and 5 cancel despite different coordinate totals; Start 4 has equal totals but is a first-player win. The invented-pair record gives a concrete output target. Update every reference grid to agree with the required active grids. |

Headers, footers, consecutive Problem 1/2/3 numbering, and continuation labels are consistent. There are no Name/Date fields, teaching commentary, enrichment headings, routine arithmetic drill, or printed solution methods. No clipping or text outside the PDF page was found. The board labels and answer labels serve real recording purposes.

## Mathematical verification

I independently computed the outcomes from legal-move recurrences, treating removal of the final counter as an immediate loss in Problem 1. They agree with the writer's results and with the rendered positions:

- **Problem 1, Starts 1–12:** Second, First, First, Second, First, Second, First, Second, First, First, Second, First.
- **Problem 2, Starts 1–14:** Second, First, Second, First, Second, First, Second, First, Second, First, Second, First, Second, First.
- **Problem 3, Starts 1–6:** Second, Second, Second, First, Second, First.

For nonempty two-pile misère Nim, the second-player positions are `(1,0)`, `(0,1)`, and `(a,a)` for `a >= 2`; `(1,1)` is a first-player position. For two coins, adjacency is the losing condition regardless of distance from the wall. For three coins at `x1 < x2 < x3`, the second player can force a win exactly when `x1-1 = x3-x2-1`. For the two-board game, xor of the four distances from the stars decides the outcome. An additional valid invented pair is A `(0,3)`, B `(1,2)`: both individual games favor the first player, while their combination favors the second.

The supplied `check_math.py` also ran successfully. Its current rook check covers the actual 4-by-4 draft, rather than the requested 5-by-5 output; expand that check when revising. The source and build script are self-contained and use no external diagram assets. A clean packaged-source rebuild belongs after the revision, when there is a candidate final output.

## Limits and release status

These are unpiloted materials. The PDF measurements establish digital square size and page fit, not actual printer scale, counter fit, or children's ability to carry out the game after the normal launch. No physical rehearsal or classroom test was performed in this critic stage. The three concrete entry routes and readiness-dependent deeper questions are useful as a return-visit companion; page completion is not a proposed one-hour requirement.
