# Independent mathematics review

## 1. Grades 2–3 and grades 4–5, page 1, shared rules applying to every problem

**Exact text:** “Read left to right with one marker, hiding used cards. Only the current circle may affect the next move.”

**Intended mathematics:** The current circle is the machine's entire stored memory. Its next state is determined by that circle **and the card currently being read**.

**Evidence:** Read literally, the last sentence forbids the input card from affecting the move. That contradicts both printed diagrams. In grades 2–3 Problem 1, the left machine's starting YES circle sends R to NO but sends B back to YES. In grades 4–5 Problem 1, the starting YES circle likewise sends R to the next NO circle and B back to itself. Thus the same current circle must allow different next moves according to the next card. If only the circle could affect the move, all one-card inputs from the start would have the same answer, making these machines and the later recognition tasks impossible under that literal rule.

**Smallest fix:** Change the last sentence to “Only the current circle and the card being read may affect the next move.” This preserves the intended prohibition on hidden memory.

## 2. K–1, page 3, Problem 3: a length-only shortcut supplies every requested answer

**Exact text:** “Make six different rows that give these machines different answers. Use at most six cards in each row.”

**Intended outcome:** Produce six distinct inputs exposing a difference between the even-red machine and the last-card-red machine.

**Evidence:** The six rows B, BB, BBB, BBBB, BBBBB, and BBBBBB satisfy the entire instruction. In the left diagram, every B loops at the starting ✓; in the right diagram, every B loops at the starting ×. Consequently none of these trials makes either marker leave its start, and one observed disagreement can be padded to fill all six rows without any additional comparison of the machines. This is a valid-answer shortcut, not a faulty transition diagram. Independent enumeration confirms all six examples and finds 32 distinguishing rows of exactly six cards, so a fixed-length version remains feasible.

**Smallest fix:** Replace “Use at most six cards in each row” with “Use six cards in each row.” The six existing six-box answer rows already fit that change.

No other mathematical problems were located. Every remaining task, all supplied input pairs, the complete finite “find every” lists, the minimum-state claims, and the rendered state diagrams in all three bands were independently checked.
