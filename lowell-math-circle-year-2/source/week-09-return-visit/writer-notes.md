# Week 9 return visits: writer-stage notes

Status: prepared student draft, unpiloted. Writer stage only. No facilitator
guide, base packet, global index, or repository guidance was edited.

## Delivered scope

One shared `draft/return-visit.pdf`, seven Letter pages, with exactly three
numbered investigations. The explicit return-visit scope overrides the generic
three-band filenames in the workflow harness. This is a companion rather than a
one-hour completion plan.

| Pages | Investigation | Actual page header |
|---|---|---|
| 1-3 | All legal two-bounce wall words for two finishes | Grades 2-5 |
| 4-5 | All 15 interior starts on a 6 by 4 rectangle | Grades 4-5 |
| 6-7 | Crossing counts on four boards; a ten-crossing construction | Grades 2-5 |

The wall-word investigation supplies eight separate 4 by 4 boards per finish so
successful paths can remain separate. Its record is the two-letter wall word;
the finish dot is labelled F, keeping top-wall T unambiguous. The third page was
added after checking space for the complete collection. Pages 2, 3, 5 and 7 are
workspace for the same numbered investigation, not additional problems.

The loop master board has 22 mm squares. Its two extra boards have 18 mm squares.
All wall-word and crossing working grids use 12.5 mm squares. Each board uses
equal scaling on both axes. The ten-crossing task has a 12 by 12 grid, large
enough for a 5 by 6 example and scaled variants within that workspace.

## Prerequisites and conventions

The wall-word entry requires handling a ruler, recognizing a straight ray and
equal bounce angles from a visual, and following a two-letter order. It does not
require angle measurement, fractions, roots or shortest-route calculations.
The non-task one-bounce visual shows incoming ray, equal-angle turn and the
completed S-to-F path with word R. It establishes a convention and is not a
fourth investigation. The prose defines LR as left, then right before first use.

The loop investigation requires following one diagonal square at a time and
keeping a visible counter arrow. Its non-task 3 by 3 example shows a starting NE
state, the right-wall NW state after one step, and the top-wall SW state after
the next step. The stopping condition is stated as both the same starting dot
and NE heading. The child can walk the counter without prior lcm knowledge.

The crossing investigation requires following a familiar diagonal launch and
recognizing an interior X. Its small visual shows the first pass, later pass,
then one marked crossing location; it is not one of the target boards. Wall
contacts and corners are excluded explicitly. Children own the choice of the
ten-crossing rectangle. No formula is printed.

Materials from the brief remain ruler, coloured pencils, tracing paper or mirror
copies for reflection checks, and a small counter with a visible direction
arrow. No independent K-1 entry was forced. Adult reading can reduce text demand
without having adults operate the whole investigation. Physical handling and
classroom pacing remain untested.

## Exact mathematics checked

`draft/src/check_math.py` uses exact rational wall times and segment intersections,
and integer counter states. It checks actual wall order and excludes corners and
extra contacts, rather than accepting a reflected image alone. Its report is
`draft/build/math-checks.json`.

On both 4 by 4 boards S=(1,1). Finish A is F=(2,3), and finish B is F=(3,3).
The code independently confirms all 16 candidate words for each printed finish:

- A: LR, LT, RL, RT, BL, BR, BT, TB are legal.
- B: LR, LT, RL, BR, BT, TB are legal.
- All repeated-wall words are impossible. For B the distinct-wall words LB, BL,
  RT and TR meet corners. The other rejected distinct-wall words have the wrong
  actual traversal order.

These are inverse prescribed-contact investigations; shortest lengths are not
student tasks. The check also confirms the outline's A squared lengths:
LR 53, RL 85, BT 37, TB 101, LT 25, BL 25, RT 41, BR 41.

The printed interior letters are A-E at y=3, F-J at y=2, K-O at y=1, with x=1-5
in each row. All launches are NE. The corner starts are A, C, E, G, I, K, M, O;
the loops are B, D, F, H, J, L, N. Every loop first returns to its full starting
state after 24 diagonal steps. The check explicitly confirms that H=(3,2)
returns to the dot after 12 steps with SE heading, then reaches the full NE
starting state at step 24. That distinction is not revealed on the worksheet.

The four printed crossing counts are 1, 3, 6 and 1 for 2 by 3, 3 by 4, 4 by 5,
and 4 by 6 respectively. Exact intersections are deduplicated by location.
A 5 by 6 rectangle has ten crossings; 10 by 12 has ten too. The underlying
reduced-dimension theorem and its proof remain adult mathematics, not a printed
student procedure.

## Source ancestry and distinct return directions

The outline supplies the ancestry; existing base worksheets were not used as
drafting templates in this writer stage. Prior-year Lowell Handout 10 Problems
10.2-10.7 already explored 45-degree endpoints and scaling. Current Week 9 F09-v4
already develops the corner/bounce/lcm rule. The archived grades 6-7 extra already
contains rational-slope launches and a midpoint periodic example. Looping and
reflection themselves are therefore not claimed as new themes.

Week 21 already has shortest one-contact mirror routes, and its companion
`week-21/week-21-bonus.pdf` optimizes two contacts on parallel walls. Problem 1
here also uses repeated reflection, but asks for rectangle wall words and rejects
wrong orders and corner contacts. The other return directions are complete
interior-dot classification with full-state termination, and intersection
geometry. The one-bounce convention picture is not counted as novelty.

## Verification

The final writer PDF was compiled twice with pdfLaTeX. `check_pdf.py` verifies the
seven bands, footers, Letter dimensions, every working board's four sides and
specified unit size, equal scaling, and the 150 by 150 mm extra grid. All seven
final rendered pages were inspected for legibility and overlap. No overfull or
underfull boxes were reported.

`draft/return-visit-source.zip` contains the standalone `src/` directory. It was
extracted to `clean-rebuild/` and built there using only its own source files.
The rebuilt PDF passes the same mathematics, page, band and geometric checks.
All seven page-render SHA-256 hashes match the final writer draft exactly; the
record is `draft/build/rebuild-checks.json`. No overfull or underfull boxes were
reported by either build. Digital and mathematical checks do not establish a
physical reflection rehearsal or classroom piloting.
