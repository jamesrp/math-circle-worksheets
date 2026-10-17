# Week 86 independent mathematical review

Reviewed current `draft/shared.pdf` (4 pages), `draft/upper.pdf` (6 pages) and `draft/materials.pdf` (3 pages), not the superseded grade-named copies. No K–1 packet is intended under the outline's explicit override. The author’s verifier was not used. Independent finite-state solver and PDF graph extraction evidence is in `math-audit/`; see `math-audit/verification-notes.md` for every problem's checked outcome, general arguments, exact neighborhoods and assumptions. All 29 printed graph instances were checked for every edge/label and rendered for inspection.

## Located issue: unrestricted placement trivializes the first two-cop investigation

- **Band / location:** Grades 4–5, upper page 5, Problem 5, board Q6.
- **Exact text:** “Put down both cops before R chooses.” / “Use two cops to catch R on this ring. Find a plan that works however R starts and moves.”
- **Evidence:** Put C1 at a and C2 at d. Their closed neighborhoods are N[a]={f,a,b} and N[d]={c,d,e}, covering all six vertices. Wherever R is placed, a cop catches it on the first cop turn, before R ever moves. The independent joint-turn solver confirms optimum 1, attained precisely by opposite placements {a,d}, {b,e}, {c,f}. Thus the task can be finished through initial placement alone, bypassing pursuit and coordination. This is a **task-depth shortcut, not an incorrect theorem or impossible task**.
- **Smallest substantive repair to consider:** Add “Start both cops at a.” This changes only the starting state and keeps the movement choices open; the solver verifies a 3-turn optimal guarantee from that common start. The reviser can choose this or another start constraint that serves the intended investigation. Upper Problem 6 can retain unrestricted placement and its general-ring question.

**Shared Grades 2–5 packet:** All four problems check out mathematically, including optimal path starts/times, both trees, triangle capture, and eternal escape on rings of length 4–6.

**Upper Grades 4–5 packet:** Problems 1–4 and 6 check out mathematically. Problem 5's claim is also true, with the shortcut above. The minimum added-road counts are 1 for C4 and 2 for C5; all minimum choices were enumerated. Both six-dot map-design requests are feasible. F1 folds to one vertex; F2 has only the two initial folds of b and then the evasive square. The closed-neighborhood rule and worked example are correct on their current reduced states. Two cops catch on every finite ring under the printed turn convention.

**Materials:** Both copies of F1 and F2 have the correct edges and labels. The turn tiles match the one-cop and joint two-cop rules. Physical printing, counter fit, tile assembly, and fold-covering procedures remain untested; this review establishes mathematical and digital consistency only.
