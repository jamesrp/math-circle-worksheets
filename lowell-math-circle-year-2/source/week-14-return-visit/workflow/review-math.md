# Week 14 fresh independent mathematical review

Reviewed 2026-10-04. Scope: the actual six-page `draft/return-visit.pdf`, with three investigations and their continuation pages, as required by the delegated layout override. Read `PROMPT.md` and `CRITIC-MATH.md`; inspected all six rendered pages and the compiled PDF vector paths. No writer verification program or answer comments were used. Draft/source/base material was not edited.

PDF SHA-256: `431adadf27b66bdaf92c932bccf8dd3001cb861dd257e17162f114a4b12b3563`.

**No located mathematical defects. All three bands check out.** No mathematical correction is needed. The evidence below records the independently verified answers and procedures; it is for adults, not student-page additions. Physical tracing/erasing and classroom use remain untested.

## Grades K-1, pages 1-2, Problem 1: passes

Printed task: “Peel ears from both drawings until one triangle remains, writing the peeled corner letters in order. Can your choices leave different last triangles?”

The compiled diagrams are the fan with diagonals `AC, AD, AE` and the central drawing with diagonals `AC, AE, CE`. Both have four triangular regions. The task is possible, and choices can leave different last triangles in each drawing. No new diagonal is needed: each removal deletes the two boundary sides incident to the peeled corner and promotes the existing third side to the boundary.

Exhaustive independent enumeration of removable vertices in the current cyclic polygon gives every legal order below. Each word contains the three peeled corners, in order; the remaining triangle follows the arrow.

| Drawing | All valid orders and final triangles |
|---|---|
| Fan, page 1 | `BCD -> AEF`; `BCF -> ADE`; `BFC -> ADE`; `BFE -> ACD`; `FBC -> ADE`; `FBE -> ACD`; `FEB -> ACD`; `FED -> ABC` |
| Central, page 2 | `BDC -> AEF`; `BDF -> ACE`; `BFA -> CDE`; `BFD -> ACE`; `DBC -> AEF`; `DBF -> ACE`; `DFB -> ACE`; `DFE -> ABC`; `FBA -> CDE`; `FBD -> ACE`; `FDB -> ACE`; `FDE -> ABC` |

Thus the fan has 8 valid orders and final-triangle multiplicities `ABC:1, ACD:3, ADE:3, AEF:1`. The central drawing has 12 valid orders and multiplicities `ABC:2, ACE:6, AEF:2, CDE:2`. The fan initially has ears at B and F; the central drawing initially has ears at B, D and F. In both, all four original triangular regions can be the last triangle.

The pentagon worked convention is correct. Its input has boundary `ABCDE` and diagonals `AC, AD`, hence triangles `ABC, ACD, ADE`. The highlighted B ear is `ABC`. Removing `AB`, `BC` and B leaves the quadrilateral `ACDE`, boundary `AC, CD, DE, EA`, and diagonal `AD`. That is exactly the printed “After” picture. The resulting quadrilateral is deliberately not regular; its coordinates are the four retained pentagon corners. The instruction to stop at one triangle avoids attempting to erase the final triangle.

## Grades 2-3, pages 3-4, Problem 2: passes

Printed task: “Color the corners of both drawings so every triangle has all three colors. Circle as few corners as possible so every triangle touches a circled corner.”

The task allows any minimum corner cover, including corners of different colors. Independent enumeration considered all `3^6 = 729` color assignments and all `2^6 = 64` corner subsets for each compiled drawing.

| Drawing | Triangular regions | Valid three-colorings | Minimum covers |
|---|---|---|---|
| Fan, page 3 and its two copies | `ABC, ACD, ADE, AEF` | Exactly 6, obtained by permuting the colors of `A / BDF / CE` | Exactly one singleton: `{A}` |
| Central, page 4 and its two copies | `ABC, ACE, AEF, CDE` | Exactly 6, obtained by permuting the colors of `AD / BE / CF` | Exactly six pairs: `{A,C}`, `{A,D}`, `{A,E}`, `{B,E}`, `{C,E}`, `{C,F}` |

The complete fan coloring words in A-through-F order are `RBYBYB, RYBYBY, BRYRYR, BYRYRY, YRBRBR, YBRBRB`. The central words are `RBYRBY, RYBRYB, BRYBRY, BYRBYR, YRBYRB, YBRYBR`.

The fan minimum is one because A meets all four regions and no empty set can cover a triangle. The central minimum cannot be one: A misses `CDE`, C misses `AEF`, E misses `ABC`, and B, D and F each meet only their own outer ear. Each of the six listed pairs covers all four regions. Its three color classes `{A,D}`, `{B,E}`, `{C,F}` are three of those six minima. The central minimum therefore does not require choosing a single color class, consistently with the printed wording.

## Grades 4-5, pages 5-6, Problem 3: passes

Printed task: “Find all triangulations that match after a half-turn, a one-third-turn or a one-sixth-turn. Save each with its turn on the next page. Explain why each list is complete.”

An independent exhaustive check formed all 3-element subsets of the regular hexagon's nine possible diagonals, rejected every subset with intersecting interiors, and confirmed four triangular regions for every survivor. There are 14 fixed-label triangulations. Rotation was then tested as equality of diagonal sets under the corner permutation, without identifying rotated sets as one answer.

| Turn | All invariant diagonal sets | Count |
|---|---|---|
| Half-turn, corner shift 3 | `AC,AD,DF`; `AC,CF,DF`; `AD,AE,BD`; `AE,BD,BE`; `BE,BF,CE`; `BF,CE,CF` | 6 |
| One-third-turn, corner shift 2 or 4 | `AC,AE,CE`; `BD,BF,DF` | 2 |
| One-sixth-turn, corner shift 1 or 5 | None | 0 |

No drawing belongs to both the half-turn and one-third-turn lists. The nine recording hexagons on page 6 suffice for the eight drawings and a record that the one-sixth-turn list is empty.

Completeness can also be explained without the program. A half-turn permutes the three diagonals, so at least one is fixed individually and must be a diameter. Two diameters would cross, so exactly one is present. There are three possible diameters; either quadrilateral side has two triangulations, and the opposite side is forced by the half-turn, giving `3 x 2 = 6`. Under a one-third-turn, diameters have a three-element orbit that crosses. Each short diagonal has a three-element orbit; the only admissible ones form either alternating central triangle, giving two drawings. Under a one-sixth-turn, a short diagonal has a six-element orbit, too many for a triangulation. The three-element diameter orbit crosses, so there is no invariant triangulation.

The worked half-turn convention is correct: clockwise A-through-F labels remain fixed; the traced diagonal `AC` maps to `DF`. The intermediate picture shows the original `AC` dashed, its turned image `DF`, and a 180-degree arc. The output retains only `DF`. This is a convention demonstration on one diagonal, not a claimed complete triangulation. The center marks coincide with the actual polygon centers.

## Compiled diagram and scale checks

All six pages are US Letter, `612 x 792` PDF points. Inspected every outer polygon path and its nearest printed corner labels: 21 hexagons, two pentagons, and the one retained-corner quadrilateral in the peeling demonstration. Every hexagon has exactly six boundary segments and fixed clockwise labels `ABCDEF`. Every regular diagram has equal edge lengths and equal vertex radii within PDF rounding (maximum radius spread below `0.00032` point). No unintended diagonal crossing appears in either fixed triangulation.

| Pages / use | Number | Actual geometric diameter at 100% scale | Diagonal check |
|---|---:|---:|---|
| Pages 1-5, large working hexagons | 5 | `4.00005` inches | Fan on 1 and 3; central on 2 and 4; blank on 5 |
| Pages 3-4, smaller copies | 4 | `2.16003` inches | Two copies of the correct page-specific triangulation |
| Page 5, worked turn convention | 3 | `0.94002` inches | `AC`; `AC` plus `DF` as intermediate; `DF` |
| Page 6, saving boards | 9 | `1.62002` inches | Blank |
| Page 1, pentagon before/intermediate | 2 | Circumdiameter `0.98003` inches | Both `AC, AD`; correct B ear highlighted |
| Page 1, peeling output | 1 | Four original pentagon corners retained | Boundary `ACDE`, diagonal `AD` |

The five large hexagons have sides `2.00003` inches and width `3.46416` inches, consistent with regular point-up hexagons of four-inch circumdiameter, rather than a stretched four-inch-wide shape. Page 5's main center mark differs from the coordinate centroid by less than `0.000006` point. Coloring circles sit on all six corners in every Problem 2 diagram. Nothing was inferred to be physically rehearsed from these digital measurements.

## Reproducible independent enumeration

The following review code reproduces the enumeration. Diagonal inputs were checked against the actual compiled PDF paths. It uses no writer verification script, source assertions or answer comments.

```python
from itertools import combinations, product

def edge(a, b):
    return tuple(sorted((a, b)))

boundary = {edge(i, (i + 1) % 6) for i in range(6)}

def triangles(edges):
    return [t for t in combinations(range(6), 3)
            if all(edge(*p) in edges for p in combinations(t, 2))]

def peel(active, edges, order=()):
    if len(active) == 3:
        return [(order, tuple(sorted(active)))]
    result = []
    for i, v in enumerate(active):
        # An ear's third side is already present between its neighbors.
        if edge(active[i - 1], active[(i + 1) % len(active)]) in edges:
            result += peel(active[:i] + active[i + 1:],
                           {e for e in edges if v not in e}, order + (v,))
    return result

for diagonals in [{(0, 2), (0, 3), (0, 4)},
                  {(0, 2), (0, 4), (2, 4)}]:
    edges = boundary | diagonals
    regions = triangles(edges)
    orders = peel(list(range(6)), edges)
    colorings = [c for c in product(range(3), repeat=6)
                 if all(len({c[v] for v in t}) == 3 for t in regions)]
    covers = {k: [s for s in combinations(range(6), k)
                  if all(set(s) & set(t) for t in regions)]
              for k in range(7)}
    minimum = next(k for k in covers if covers[k])
    print(regions, orders, colorings, minimum, covers[minimum])

def cross(e, f):
    a, b = e
    c, d = f
    return len({a, b, c, d}) == 4 and ((a < c < b) != (a < d < b))

diagonals = set(combinations(range(6), 2)) - boundary
triangulations = [frozenset(ds) for ds in combinations(diagonals, 3)
                  if not any(cross(e, f) for e, f in combinations(ds, 2))]
assert len(triangulations) == 14
assert all(len(triangles(boundary | set(ds))) == 4 for ds in triangulations)

def turn(ds, k):
    return frozenset(edge((a + k) % 6, (b + k) % 6) for a, b in ds)

for k in [3, 2, 1]:
    print(k, [ds for ds in triangulations if turn(ds, k) == ds])
```
