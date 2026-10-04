# Hidden turns facilitator guide

## Mathematical overview

**Object and allowed motions.** Color all n equally spaced spots of a regular ring, n ≥ 3. Counter kinds are fixed categories and may not be permuted during testing; icon direction is ignored. A match is a dihedral motion carrying every spot to a same-kind spot. Exclude the identity, including a whole turn. There are n - 1 nonidentity rotations and n reflections. This is a distinguishing coloring, not a proper coloring: neighbors may agree.

**Exact optimum.** The minimum number of kinds is 3 for n = 3, 4, 5 and 2 for every n ≥ 6. For the small lower bound, a binary ring has at most two spots of a minority kind, and that set always admits a polygon reflection. Three kinds suffice by putting distinct unique kinds at adjacent spots and a third kind everywhere else.

**Uniform large-ring construction.** Number spots temporarily 0 through n - 1 around the ring. Mark 0, 1, 3 with one kind and all others with another. The cyclic gaps are 1, 2, n - 3, all different for n ≥ 6. They rule out every nonidentity rotation and reflection. Any binary distinguishing ring needs at least three of each kind; this lower bound is attained by the construction. It answers the eight-ring minority question with 3.

**Limits.** These statements use all dihedral motions of an unmarked regular ring. An extra fixed home mark, unequal spacing, interchangeable color names, or testing rotations alone changes the problem. Finite computer checks support the keys but do not prove the claim for every n.

## What children are meant to discover

- **K-1:** Act on a tracing copy, distinguish a match from a near match, and discover that some patterns reveal every allowed move. Physical counterexamples matter more than a complete impossibility argument.

- **Grades 2-3:** Optimize the number of kinds on 3, 4, 5 and 6 spots, then minimize a minority kind on 8 spots. A construction establishes an upper bound; an argument ruling out fewer kinds establishes optimality.

- **Grades 4-5:** Explain the small-ring obstruction and turn the six-ring discovery into a construction for every larger ring. Unequal gaps are a useful explanation after a child has a successful pattern.

**Status.** This guide keys the final v2 student PDFs, with 6 / 5 / 5 problems. Mathematical cases are checked. These pages and the proposed pacing have not been classroom-tested.

---page---

# Running the session

## Materials and preparation

**For ten children and three adults:** use three stable adult-led tables. At three-child tables, rotate builder, tester and observer; budget five pair-sized material sets overall. Supply each pair with about 24 counters, eight in each of three easily distinguished kinds, and a small bowl. Use pieces at least 20 mm wide; colors should have a shape or texture backup. Loose counters make changes quick; no bead threading is needed.

Print the selected student mats at actual size. Each pair needs tracing paper large enough to cover the whole ring, pencils or washable markers, and at least two separate copies for K-1 Problem 6. Keep spare tracing sheets so successful patterns can be saved. One eight-ring per pair is enough if partners take turns. The final spot circles are roughly 28 mm across.

**Adult preparation, estimated 15-20 minutes:** print only likely starting pages, check a tracing-sheet flip on a blank ring, and prepare the alternating four-ring shown in the student introduction. The drawing should be visible from both sides. A reflected category symbol can face backward; its direction is deliberately ignored. Remove any temporary home tick before testing a pattern. Do not flip a loose-counter board and spill the pieces.

**Readiness:** no arithmetic beyond comparing or counting small collections is required. Adults read aloud and can record a child's construction. Before offering optimization, check that the child keeps the original fixed, lines up all spots, and checks every kind. A turn that leaves even one spot between printed positions is not an allowed comparison.

## Common launch and flexible hour

**0-7 minutes:** let children handle counters and overlays. On the alternating four-ring, demonstrate the printed two-spot matching turn and one-spot mismatch. Flip the tracing copy once, keeping the original still. Ask, “Could I change this pattern without you noticing?” Do not reveal a successful six-ring.

**7-23 minutes:** youngest children start K-1 Problems 1-2; middle and upper groups try the three- and four-rings. Partners alternate builder and tester. Save at least one candidate before changing it.

**23-27 minutes:** take a short movement break. Children can hold four places in a circle while an adult models moving a copy; then return to the exact table rules.

**27-46 minutes:** continue a worthwhile construction. Offer the five- or six-ring when the small-ring pattern is clear; offer the eight-ring or general construction only when testing is reliable.

**46-57 minutes:** compare one pattern that failed and one that resisted every tested move. Separate “we tried these moves,” “we think this always works,” and “this feature rules out every move.”

**57-60 minutes:** save or photograph the children's patterns with permission under the circle's normal practice; note which tasks they actually reached. Finishing all pages is unnecessary. A productive stopping point is one defended construction and one newly noticed obstruction.

---page---

# Key for K-1

**Reading the key.** Words below list counter kinds clockwise, beginning at any spot. A, B and C are category names, not directional marks. Rotated or reflected versions of a witness are equally valid. When checking a child's own pattern, keep the actual kind names fixed.

## Problems 1 through 3

**Problem 1, three-ring exploration.** Every two-kind pattern admits a nonidentity reflection. If all three spots match, every motion works. Otherwise one kind occurs once and the other twice; a reflection fixes the lone spot and exchanges the other two. A mixed ring has no nonidentity matching rotation, so “no matching turn” is not enough. Accept repeated experiments and a physically demonstrated surviving flip.

**Problem 2, four-ring minimum.** The answer is 3 kinds. A B C C is a witness. Since A and B each occur once, any matching motion must fix both adjacent spots; only the identity does. With two kinds, the minority has 0, 1 or 2 spots and a reflection survives. The general lower-bound reason appears on page 5.

**Problem 3, changing one counter.** Outcomes depend on the starting construction. From A B C C, changing the third spot C to A gives A B A C, which has a reflection through the B and C spots. Changing that same C to B gives A B B C, which remains distinguishing because unique A and C are adjacent. Thus one-counter edits can either create a hidden motion or preserve asymmetry. Restore the starting pattern between trials if comparing edits. Do not teach that every change must destroy asymmetry.

## Problems 4 through 6

**Problem 4, five-ring.** Two kinds cannot stop all motions. Three kinds can: A B C C C. The unique A and B are adjacent, so both must be fixed and no nonidentity motion remains. Let children exhibit failures with two kinds; the adult can supply the all-cases argument later.

**Problem 5, six-ring.** One answer is A A B A B B, whose A spots are 0, 1, 3. The gaps between A spots are 1, 2, 3. No rotation or reflection preserves their cyclic placement. Children may instead check all five nonidentity rotations and six reflections using an overlay. Record the candidate before testing.

**Problem 6, two genuinely different eight-rings.** Use A A B A B B B B and A A B B A B B B. Their A-gap multisets are {1, 2, 5} and {1, 3, 4}; both contain three different gaps and so are distinguishing. Dihedral motions preserve the gap multiset, so the two patterns cannot match each other. Separate tracing copies are essential. A mere rotation, reflection, or shifted drawing of the first pattern is not a second answer.

**Optional hints, one at a time:** “Show me one place where the copy fails.” “Which counter kind is easiest to track?” “Can a flip keep that spot fixed?” For a child ready for the eight-ring distinction: “How far apart are the three A spots as you go around?” Do not give the 0, 1, 3 construction before exploration has a chance to work.

---page---

# Keys for the older bands

## Grades 2-3

**Problem 1, three-ring:** 3 kinds; A B C. Any binary ring has a reflected match. With three distinct kinds, every spot must stay fixed.

**Problem 2, four-ring:** 3 kinds; A B C C. Unique adjacent A and B rule out every nonidentity motion. Every binary pattern has a minority-set reflection.

**Problem 3, five-ring:** 3 kinds; A B C C C. The same upper- and lower-bound arguments apply. This is not a claim that the child must find the proof before moving on.

**Problem 4, six-ring:** A A B A B B works. A complete physical verification checks five nonidentity rotations and six reflections, always lining up every spot. An explanation from gaps 1, 2, 3 is shorter and generalizes. In the adult indexing, rotations send i to i + k and reflections send i to k - i, modulo 6; these exhaust the possibilities.

**Problem 5, eight-ring:** A A B A B B B B works and has the least possible minority count, 3. Zero, one or two counters of one kind always leave a reflection. The three A gaps 1, 2, 5 establish that three suffice. The question concerns the less frequent kind; the number of kinds is already fixed at two.

## Grades 4-5

**Problem 1:** 3 kinds on three spots, with witness A B C. If fewer kinds are used, some kind occupies at most one spot, or the ring is constant, leaving a reflection.

**Problem 2:** 3 kinds on four spots, with witness A B C C. The minority-set argument covers both adjacent and opposite two-counter patterns without a lengthy catalog.

**Problem 3:** 3 kinds on five spots, with witness A B C C C. The common proof for Problems 1-3 is that a binary minority set has size at most two and therefore a reflection. A one-kind coloring also has all reflections.

**Problem 4:** A A B A B B on six spots; use the distinct-gap argument or a complete overlay test. Do not require a written algebraic proof from a child whose geometric explanation is complete.

**Problem 5:** For every n ≥ 6, place A at spots 0, 1, 3 and B elsewhere. On the printed eight-ring this is A A B A B B B B. The cyclic gaps 1, 2, n - 3 are all different. Page 5 proves that this excludes every nonidentity dihedral motion; trying sizes 6, 7 and 8 alone is only evidence for the conjecture.

## Prompts for explanation

Ask a child to point to the feature a hypothetical matching motion must preserve. “That unique counter must go to itself” and “these three gaps are different” can become proofs with gestures. For a stronger extension, ask why three is the smallest minority count on every binary distinguishing ring. Avoid replacing the investigation with an exhaustive list of binary strings.

---page---

# Proofs and source notes

## Why the bounds are exact

**At most two marked spots always have a reflection.** An empty marked set is preserved by every reflection. One marked vertex is fixed by the reflection through that vertex and the polygon center. For two distinct marked vertices, the perpendicular bisector of their chord passes through the center and is an axis of a polygon reflection; it exchanges those vertices and preserves their complement. Thus any binary ring with a kind appearing at most twice has a surviving reflection. For n = 3, 4, 5, a minority kind occurs at most twice.

**Why adjacent unique kinds work.** A matching motion fixes each unique-colored vertex individually. A nonidentity polygon rotation fixes no vertex. A reflection can fix two polygon vertices only when they are opposite, so it cannot fix two distinct adjacent vertices for n ≥ 3. Giving those two vertices different unique kinds and all remaining vertices a third kind is therefore distinguishing.

**Why three unequal gaps work.** A motion preserving a three-point marked set permutes its cyclic gaps. A nonidentity rotation would cycle the three marked points and force all three gaps equal. A reflection reverses their cyclic order, fixing one gap and interchanging the other two, forcing an equal pair. When the gaps are 1, 2, n - 3 with n ≥ 6, neither is possible. A motion fixing all three marked vertices is the identity. One kind never distinguishes, so the two-kind construction is optimal.

## Verification and interpretation

A fresh finite check enumerates all binary rings of sizes 3 through 10 under the exact maps i → i + k and i → k - i. Counts of distinguishing binary words in fixed indexed positions are 0, 0, 0, 12, 28, 96, 252 and 600. These are counts of labeled-position words, not counts up to rotation/reflection. It also checks every printed witness and both one-counter edit outcomes. The accompanying editable source includes the verification script and its results.

**What to record after use:** whether overlay flips were understood, whether kind direction or a hidden home mark affected testing, which patterns children invented, and whether the six-ring search remained engaging. Mathematical verification does not establish developmental suitability or timing.

## Sources

Michael O. Albertson and Karen L. Collins, **Symmetry Breaking in Graphs**, Electronic Journal of Combinatorics 3(1), R18 (1996), DOI 10.37236/1242. Primary research source for distinguishing colorings and the group-action setting. The complete elementary cycle proofs above are supplied here. [Article and PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v3i1r18).

Laura Givental, Maria Nemirovskaya and Ilya Zakharevich, **Math Circle by the Bay**, AMS/MSRI Mathematical Circles Library 21 (2018), Preface pp. viii-ix. The authors describe deep themes with multiple entry levels, varied pace, manipulatives and returning to children's explanations. The timing, exact tasks and readiness judgments in this guide are local proposals, not classroom claims from that book.
