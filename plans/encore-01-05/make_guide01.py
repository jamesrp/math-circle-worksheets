from pathlib import Path
import json, math
run=Path('tmp/worksheet-runs/encore-week-01-20261004-v1')
guide=run/'guide-src'; guide.mkdir(exist_ok=True)
d=json.loads((run/'draft/render/mathematical-checks.json').read_text())['problem_1']
for name in ['compact','stretched']:
 e=d[name+'_example'];txt=['\\begin{tikzpicture}[x=0.5in,y=0.5in,line width=0.7pt]']
 for group in e['block_cell_groups']:
  pts=set(tuple(p) for i in group for p in e['triangle_cells'][i]);xy=[(a+b/2,math.sqrt(3)*b/2) for a,b in pts];cx=sum(x for x,y in xy)/len(xy);cy=sum(y for x,y in xy)/len(xy)
  xy.sort(key=lambda q:math.atan2(q[1]-cy,q[0]-cx))
  col='blue!25' if len(group)==2 else 'green!25'
  txt.append('\\draw[fill='+col+'] '+' -- '.join(f'({x:.5f},{y:.5f})' for x,y in xy)+' -- cycle;')
 txt+=['\\end{tikzpicture}'];(guide/(name+'.tex')).write_text('\n'.join(txt))
body=r'''\lead{Mathematical overview: what the three investigations can establish}
For whole-side, edge-connected arrangements of $t$ green triangles and $r$ blue rhombi, the boundary is $P=3t+4r-2s$ unit sides, where $s$ counts shared full sides. Holes contribute boundary; a point contact does not connect blocks. With six greens and two blues the exact minimum is 8 and maximum is 12. Area stays ten small triangles while contact structure changes.

Around one point, every green corner and sharp blue corner occupies one of six equal sectors; a blunt blue corner occupies two. If $g,a,o$ count these corners, closure requires $g+a+2o=6$. Every such local mixture can be built. This says nothing about whether an arbitrary larger outline can be filled.

A symmetry must carry every block and internal seam to itself. In the regular one-block-side hexagon the possible matching non-full turns, measured in sixth-turn steps, are none, only 3, only 2 and 4, or all of 1--5. There are 18 green/blue tilings, with symmetry orders 1, 2, 3 or 6. The identity turn is always a symmetry and is omitted on the student page.

Experiments give candidate designs and bounds. A contact count proves the upper boundary bound; sector accounting explains corner mixtures; comparing all seams establishes symmetry for a built design. Complete classifications require arguments or enumeration, not a handful of successful trials.

\lead{Entries, materials and a manageable visit}
The shared packet is labeled Grades 2--5. K--1 can join concrete corner fitting or mosaic testing with an adult reading and recording; complete extremal proofs or all-mixture classification are readiness-dependent. Counting to 12 is enough for the concrete boundary route; no degree notation, fractions or multiplication are required. Grades 2--3 can compare designs and make records. Grades 4--5 can establish bounds and organize complete small cases.

Per pair: at least 6 small green triangles and 6 small blue rhombi (12 of each available allows continued making); set larger blocks and other colors aside. Use pencil and separate paper; tracing paper helps turn a seam pattern. For the current eleven children, prepare five pair trays (30 greens and 30 blues total), plus two of each for the demonstration; the third upper child rotates as builder, recorder or checker. One nominal small edge is one inch. The student copies are sketches, not working mats. No cutting is required if these blocks are already available.

Keep the usual fixed adult-led tables and pairs. Choose one investigation for a 20--35 minute revisit, with 2--4 minutes for launch and a few minutes to share. All three can occupy several meetings. Give time to handle blocks before stating a challenge; the adult may read or record, while children choose and change constructions. Finishing the packet is not the goal.

\lead{Launch together}
Place a green and a blue on the table. Let children join them along a whole side. Trace the outside with a finger and show that the joined side is no longer outside. For the next visit demonstrate the small worked corner example or a single sixth-turn of a marked hexagon before giving that page. Do not demonstrate an optimal target construction.
\newpage
\lead{Problem 1: shortest and longest boundaries}
\textbf{Entry and timing.} Start with the specified six greens and two blues spread out; pairs make one connected shape. Allow 20--35 minutes, including repeated reshaping. A younger entry is comparing two constructions by walking a finger around their uncovered sides; recording can be shared with an adult.

\textbf{Answers and constructions.} The shortest boundary is 8 unit sides. A compact hexagon with successive side lengths 2,1,1,2,1,1 works. The longest is 12; a strip of five rhombus-sized regions works when two stay blue and the other three are split into six greens. The following are recording-scale examples, not block-fitting mats.

\begin{center}\input{compact.tex}\hspace{0.45in}\input{stretched.tex}\end{center}

Each original green has three sides and blue has four, giving 26 sides before joining. Each shared side removes two from the exposed count. A connected contact graph on eight pieces has at least seven contacts, so $P\le26-14=12$. The strip has exactly seven contacts and attains the bound. Extra contacts shorten the boundary.

For the lower bound, ten triangle-spaces must be enclosed. Boundary is even. A closed triangular-lattice boundary of at most six unit edges encloses at most six triangle-spaces, so it cannot enclose ten. This small lattice bound was independently checked by all closed walks of lengths 1--6; a second check enumerated all 5,053 translation-distinct edge-connected ten-triangle boards and found minimum boundary 8. Holes can only add boundary. Children may establish the upper bound with a drawing; the complete lower-bound justification is an optional adult conversation, not a printed procedural demand.

\textbf{Questions and hints.} ``Which sides stopped being outside when these pieces joined?'' If a child counts only the outer silhouette, trace any hole too. If a child connects only at corners, demonstrate sliding them until a whole side is shared. Offer one extra contact as a hint without choosing their construction.

\textbf{Return-visit continuations.} Can the same shape have different internal contacts but the same boundary? The possible boundary lengths are 8, 10 and 12. For 10, attach one blue to each of two opposite sides of the six-green unit hexagon; each adds two exposed sides. Try six greens alone: boundary 6 or 8, with compact and stretched examples. Make a hole and investigate how its inner boundary contributes. Change inventory only after the original question has yielded real comparison; changing numbers alone is not a new investigation.

\textbf{Limits.} Whole sides must meet; no overlap, partial-edge contact, or disconnected pieces. The diagram sizes are for adult explanation. Digital verification does not establish physical fit or classroom readiness.
\newpage
\lead{Problem 2: corner mixtures}
\textbf{Entry and timing.} This is the most direct K--1 entry with adult reading. Use the worked visual: put one corner at a marked point, then add another without overlap. Children choose which corners and how many pieces. Allow 15--30 minutes; later visits can organize their discoveries.

\textbf{Exact result.} The following pairs (greens, blues) are all possible. Sharp and blunt blue corners may be selected independently.

\begin{center}\begin{tabular}{c|l}
Blues & Possible numbers of greens\\\hline
0 & 6\\
1 & 4,5\\
2 & 2,3,4\\
3 & 0,1,2,3\\
4 & 0,1,2\\
5 & 0,1\\
6 & 0
\end{tabular}\end{center}

There are 16 mixtures under the student convention, which distinguishes only green/blue counts, not rearrangements or different blue-corner choices. Eight record boxes invite a substantial sample; use separate paper if children want all 16. Do not count merely rotating a construction as another mixture.

\textbf{Explanation.} A small green triangle divides a full turn into six equal sectors. A sharp blue corner fits one sector and a blunt one fits two. If there are $g$ greens and $r$ blues, the number $o$ of blunt blue corners must equal $6-g-r$. It can range from 0 to $r$, so $0\le6-g-r\le r$. The table lists exactly those nonnegative choices. For each, place the corners as consecutive sector wedges; each convex piece stays inside its wedge, so no two overlap. The result closes the circle of angles, although its outside outline varies.

\textbf{Questions and hints.} ``Can you turn this blue so its other corner is at the point?'' Offer six green triangles around the point as a measuring tool only after exploration. Ask children to locate a gap or overlap with a finger. A local gap of one sector cannot be closed by a blunt blue corner.

\textbf{Deeper continuations.} Which mixtures use exactly three, four, five or six pieces? The number of blunt corners is respectively 3,2,1,0. Two pieces cannot close a full turn because even two blunt corners occupy only four sectors. If the children distinguish green, sharp blue and blunt blue as separate types, there are again 16 count triples, one for each row-entry in the table. Arrange the same mixture in different circular orders and compare the resulting outside shapes.

\textbf{Facilitation limit.} Fit around a point is a local angle result. It does not prove a chosen large polygon has a tiling, nor that an arbitrary angle inventory makes a specified outside boundary. No protractor or formal degree notation is needed.
\newpage
\lead{Problem 3: symmetry of the whole design}
\textbf{Entry and timing.} Build the regular one-block-side hexagon on the table, then record its seams on a sketch. Allow 20--40 minutes. Younger children can turn a tracing and check visible seams; older children can design one example for each different turn-set and explain completeness.

\textbf{Constructions and answers.} Six greens meeting at the center match after every step 1--5. Three blues filling the hexagon match after steps 2 and 4. Two blues on opposite neighboring pairs of triangle sectors, with greens filling the remaining opposite sectors, match only after step 3. One blue and four greens match after no step from 1--5. These are four different symmetry answers, not four arbitrary colors or orientations.

\textbf{Explanation and complete small case.} The regular unit hexagon contains six triangular sectors. Every blue replaces an adjacent pair of sectors; blues cannot share a sector. A tiling is thus a selection of non-touching edges on a six-cycle. There is one selection of size 0, six of size 1, nine of size 2, and two of size 3, totaling 18. Twelve tilings have no nonidentity symmetry, three have a half-turn, two have third-turns, and one has every sixth-turn. Distinct physical orientations count as distinct tilings here; rotating a design preserves its symmetry answer.

Matching turns are closed under doing turns one after another. If step 1 matches, every step matches. If step 2 matches, step 4 matches. If both step 2 and step 3 match, step 1 also matches (perform step 3 followed by the inverse of step 2). The only possibilities are therefore exactly the four listed sets. This is a concrete rotation argument; no group terminology is required.

\textbf{Questions and hints.} ``The outside matches, but do these two inside edges match?'' Put a tiny removable mark on one corner to track the turn, then remove it before testing the design's symmetry; the registration mark is not part of the design. If mentally turning is difficult, turn a tracing paper copy or rotate the entire built mosaic carefully as a unit.

\textbf{Return-visit continuations.} Classify the 18 tilings up to turning; there are five classes. Find which designs also match in a mirror and whether the mirror axis must pass through corners. Extend to a larger hexagon only when children want more design freedom, keeping area and material counts realistic. Reflection tests are a different transformation; do not merge them silently with the printed rotation task.

\lead{Novelty, evidence and status}
Week 1 base/encore already offers shape filling, packing, flips/ribbons, placement games, cube stacks, and fewest-piece tasks. These companions add boundary contact counts, local angle closure, and global seam symmetry. They are new investigations, not replacements or another set of the same boards.

Pedagogy: \emph{Math Circle by the Bay}, Preface printed viii--x (PDF 9--11), describes deepening themes, variable pace, manipulatives and dialogue. Prior-year \emph{Pattern Block Exercises}, pp.1--2, includes filling and symmetry classes of leftover triangles; whole-mosaic symmetry is a new direction here. No problem statement was copied. Mathematics is checked digitally; sources and independent review records are supplied. All pages are \textbf{unpiloted}; physical rehearsal is \textbf{untested}. Record the investigation, actual examples used, observed difficulties and children's next questions before deciding the next visit.
'''
t=Path('plans/encore-01-05/guide_template.tex').read_text().replace('@W@','1').replace('@TOPIC@','Pattern blocks').replace('@ID@','01').replace('@BODY@',body)
(guide/'facilitator.tex').write_text(t)
