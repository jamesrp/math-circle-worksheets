# Independent review of final assembled contents

Reviewer: expand_ga1. Date: 2026-09-26.

Status: **CLOSED for all 20 contents pages across the six final books**. Geometry and analysis, algebra and discrete mathematics, and probability and applications all passed. No open contents finding.

Scope: only the newly assembled contents pages. The previously reviewed body pages and frozen author inputs were not edited or re-reviewed. The root reviewer owns the separate final link, bookmark, page-map and body-identity audit.

## Method and coverage

Every contents PNG listed below was opened and visually inspected as an individual full-page image, rather than accepted from a contact sheet. I checked subject and volume titles, readable prerequisite lines, IDs and page numbers, row separation, clipping, headings, footers, and printing instructions. An oversized initial image response was discarded; those geometry images were reopened in smaller batches and actually inspected.

For each printed row, I independently extracted the final PDF text with pypdf and required the entire normalized sequence ID + family title + prerequisite line + start page to occur once on its contents page. I compared titles and prerequisite lines to the frozen batch data, and printed page numbers to that volume’s own build-report starts. I also checked each ID appears exactly once, the ID sets agree, and the row title/gate bounds remain vertically separated. Only typographic dash/whitespace normalization was allowed. Final PDF hashes were recomputed and agree with the per-kind reports.

All inspected contents have legible instructions to print selected pages single-sided, on US Letter at actual size, keep student pages and solutions separate, and retain the original random-ten book as a separate volume. The student introduction encourages choosing known tools and exploration. The guide introduction distinguishes finite checks from general arguments and explicitly says preparation, timing and engagement remain untested. Continuation pages explain that prerequisites are gates, not age labels.

## Geometry and analysis: CLOSED

No clipped text, overlapping rows, ambiguous page-number alignment, missing gate, title mismatch, or printing-instruction problem found.

- **Student:** pages 1–4 full-size; `geometry-analysis/student/pages/page-001.png` through `page-004.png`. 32 exact printed title/gate/page rows passed; 103 final PDF pages.
  - PDF: `lowell-math-circle-year-2/combined/atlas-geometry-analysis-student-worksheets.pdf`
  - SHA-256: `6cee094dd12112dadcefd24fbbb2657f7303d59953a0e51a3606f3aac2a55247`
  - Start records: `tmp/pdfs/atlas-remaining/geometry-analysis/student/build-report.json` (`starts`).
- **Facilitator:** pages 1–4 full-size; `geometry-analysis/facilitator/pages/page-001.png` through `page-004.png`. 32 exact printed title/gate/page rows passed; 155 final PDF pages.
  - PDF: `lowell-math-circle-year-2/combined/atlas-geometry-analysis-facilitator-guide.pdf`
  - SHA-256: `c64f023d4890435dfdc5fc2070a565a1188d960778fbb80464d641f1abc9f979`
  - Start records: `tmp/pdfs/atlas-remaining/geometry-analysis/facilitator/build-report.json` (`starts`).

Verified title/page pairs (the prerequisite line also matched for every entry):

| ID | Printed title | Student page | Guide page |
| --- | --- | ---: | ---: |
| GA-01 | Can a box keep a secret? | 5 | 5 |
| GA-02 | Design a fence that defeats a match | 8 | 10 |
| GA-03 | A cover with a tiny budget | 11 | 15 |
| GA-04 | A root takes a journey | 14 | 20 |
| GA-05 | Can a network hide a high point? | 17 | 24 |
| GA-06 | What does a real picture miss? | 20 | 29 |
| GA-07 | Build an angle machine | 23 | 34 |
| GA-08 | Can a rate law choose a future? | 26 | 38 |
| GA-09 | Choose a shape, then choose its future | 30 | 44 |
| GA-10 | Program the folded interval | 33 | 49 |
| GA-12 | Can tiny payments break a budget? | 37 | 54 |
| GA-13 | How narrow can the error band be? | 40 | 58 |
| GA-14 | Choose a photograph that reveals the motion | 43 | 62 |
| GA-15 | Decode a picture from four sign patterns | 46 | 67 |
| GA-16 | Predict what the sliding window draws | 49 | 72 |
| GA-17 | A graph feeds back its own mean | 52 | 78 |
| GA-18 | Choose what best flat height means | 55 | 82 |
| GA-19 | Defeat a claimed derivative bound | 58 | 86 |
| GA-20 | Choose a journey and its effort bill | 61 | 90 |
| GA-21 | A mirror that is too short | 64 | 94 |
| GA-22 | Make a four-peg challenge | 67 | 100 |
| GA-23 | Let the route turn a tangent arrow | 70 | 105 |
| GA-24 | Test a reversible reshaping | 74 | 112 |
| GA-27 | Find the flood’s joining height | 77 | 117 |
| GA-28 | How much can one question guarantee? | 80 | 123 |
| GA-30 | Find every shortest route around a cylinder | 83 | 127 |
| GA-31 | Can every pair agree and everyone disagree? | 86 | 131 |
| GA-32 | Predict the cut before using scissors | 89 | 136 |
| GA-33 | Where did the starting value go? | 92 | 140 |
| GA-34 | Infinitely many doublings before the deadline | 95 | 144 |
| GA-35 | Can four samples fool the average? | 98 | 148 |
| GA-36 | Will feedback find the point that exists? | 101 | 152 |

## Algebra and discrete mathematics: CLOSED

No clipped text, overlapping rows, ambiguous page-number alignment, missing gate, title mismatch, or printing-instruction problem found.

- **Student:** pages 1–3 full-size; `algebra-discrete/student/pages/page-01.png` through `page-03.png`. 24 exact printed title/gate/page rows passed; 77 final PDF pages.
  - PDF: `lowell-math-circle-year-2/combined/atlas-algebra-discrete-student-worksheets.pdf`
  - SHA-256: `81db4ecb163475e52cf57ed4726dc98e271daca85ae88eccdb38062f190b8993`
  - Start records: `tmp/pdfs/atlas-remaining/algebra-discrete/student/build-report.json` (`starts`).
- **Facilitator:** pages 1–3 full-size; `algebra-discrete/facilitator/pages/page-001.png` through `page-003.png`. 24 exact printed title/gate/page rows passed; 117 final PDF pages.
  - PDF: `lowell-math-circle-year-2/combined/atlas-algebra-discrete-facilitator-guide.pdf`
  - SHA-256: `e08c39113613259ae02c98bb5a4e84c5d02196bd35301b4ffe25a949f1bffac6`
  - Start records: `tmp/pdfs/atlas-remaining/algebra-discrete/facilitator/build-report.json` (`starts`).

Verified title/page pairs (the prerequisite line also matched for every entry):

| ID | Printed title | Student page | Guide page |
| --- | --- | ---: | ---: |
| AD-01 | Build a world that defeats a rule | 4 | 4 |
| AD-02 | Can your list catch my pattern? | 7 | 8 |
| AD-03 | A collection with no card inside another | 10 | 12 |
| AD-04 | Send a network in a tiny message | 13 | 17 |
| AD-05 | How many connecting networks survive? | 16 | 23 |
| AD-06 | Do two calculation routes agree? | 20 | 29 |
| AD-07 | Everything your starting clues force | 23 | 34 |
| AD-08 | Which numbers may share a name? | 26 | 38 |
| AD-09 | Can both schedules be right? | 29 | 43 |
| AD-10 | Can the next match hide between our answers? | 32 | 47 |
| AD-11 | Choose a rule that never loses a symbol | 35 | 51 |
| AD-12 | Which cube volumes can these tools reach? | 38 | 55 |
| AD-13 | Move a corner, change the whole staircase | 41 | 60 |
| AD-14 | Can one calculation remember a rate? | 44 | 65 |
| AD-15 | Encode a rational point with one slope | 47 | 69 |
| AD-16 | Can these finite points make one cycle? | 50 | 73 |
| AD-17 | Design the round when closeness begins | 54 | 78 |
| AD-18 | Can you preserve area without preserving shape? | 57 | 82 |
| AD-19 | Choose bases that reveal what an arrow does | 60 | 87 |
| AD-20 | Find what commutes, then explain the cancellations | 63 | 91 |
| AD-21 | Make a catalog that remembers every choice | 66 | 96 |
| AD-22 | Which face cards erase the same edge pattern? | 69 | 101 |
| AD-23 | How much free space completes this module? | 72 | 107 |
| AD-24 | Count necklaces when every bead count is fixed | 75 | 112 |

## Probability and applications: CLOSED

No clipped text, overlapping rows, ambiguous page-number alignment, missing gate, title mismatch, or printing-instruction problem found. All six contents pages were inspected individually full-size after the final assembly handoff. The visible title is “Probability and applications”; the build directory is `applied-probability`.

- **Student:** pages 1–3 full-size; `applied-probability/student/pages/page-01.png` through `page-03.png`. 24 exact printed title/gate/page rows passed; 75 final PDF pages.
  - PDF: `lowell-math-circle-year-2/combined/atlas-probability-applications-student-worksheets.pdf`
  - SHA-256: `b05328148e8be2a23fc70b6fbc74dd99f3a51438c97a809436f735ba9a5ba7ba`
  - Start records: `tmp/pdfs/atlas-remaining/applied-probability/student/build-report.json` (`starts`).
- **Facilitator:** pages 1–3 full-size; `applied-probability/facilitator/pages/page-001.png` through `page-003.png`. 24 exact printed title/gate/page rows passed; 127 final PDF pages.
  - PDF: `lowell-math-circle-year-2/combined/atlas-probability-applications-facilitator-guide.pdf`
  - SHA-256: `c0955f682436ce6744627a2d88af8feb05fd01de87c40a2c8ca3b3f3a5a0a827`
  - Start records: `tmp/pdfs/atlas-remaining/applied-probability/facilitator/build-report.json` (`starts`).

Verified title/page pairs (the prerequisite line also matched for every entry):

| ID | Printed title | Student page | Guide page |
| --- | --- | ---: | ---: |
| AP-02 | The same clue, a different experiment | 4 | 4 |
| AP-03 | How surprising are these labels? | 7 | 9 |
| AP-04 | A very precise wrong answer | 10 | 14 |
| AP-05 | Build a promise an interval can keep | 13 | 18 |
| AP-06 | When the tangent robot comes back | 16 | 22 |
| AP-08 | How many rooms must a machine remember? | 19 | 27 |
| AP-09 | Two motions hiding in one machine | 22 | 32 |
| AP-10 | Add a spring: softer or stiffer? | 25 | 36 |
| AP-11 | What can a flow map actually tell you? | 28 | 42 |
| AP-12 | Choose the fastest crossing | 31 | 47 |
| AP-13 | A dimmer signal, a hidden phase | 34 | 53 |
| AP-14 | A sales pitch that balances energy and still fails | 37 | 58 |
| AP-15 | The question between two identical questions | 40 | 63 |
| AP-16 | Build a sampler for a tiny magnet | 43 | 68 |
| AP-17 | Choose a route for a clock | 46 | 74 |
| AP-18 | What can an orbit reveal about an unseen center? | 49 | 80 |
| AP-19 | Design a survey that can identify the depth | 52 | 85 |
| AP-20 | Sell products, then price a proof | 55 | 91 |
| AP-22 | Build a randomizer your opponent cannot exploit | 58 | 95 |
| AP-24 | A fair copying rule can erase a color | 61 | 100 |
| AP-25 | Design labels that survive a reaction | 64 | 106 |
| AP-27 | Choose when one sensor can separate two tanks | 67 | 111 |
| AP-28 | Four messages through a damaged strip | 70 | 116 |
| AP-30 | Design a meter that disturbs the circuit less | 73 | 122 |

## Final disposition

**CLOSED for all six books: 20 contents pages inspected full-size and all 160 ID/title/prerequisite/page entries independently matched. No open contents finding.** This closure concerns the contents only; separate body and final assembly audits remain in their own records. No frozen data, renderer, PDF or body image was edited for this review.
