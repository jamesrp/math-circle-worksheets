+++
id = "w39.tree-trips"
title = "Shortening trips on the tree"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = "On a tree every trip shortens to the one simple path between its start and finish, whichever out-and-back pairs are removed first."
+++

## prompt @158 [K-1]
Make a three-step trip from A to E and four-step trips from B back to B and from A to D. Make each one as a row of step tiles, then shorten it as much as you can.

## prompt @159
Shorten each recorded trip until no move is possible. Make a different seven-step trip from C to F that finishes with the same route as the last one.

## figure [K-1]
graph(36, 190, 32, TREE, TEDGES)

## figure
graph(119, 207, 23, TREE, TEDGES) + routes_beside_map(207, ['ABABDFDE', 'ABDFDE', 'CBCBDF'])

## key [K-1]
The three-step A-to-E trip is A-B-D-E. Every four-step B-home trip reduces to staying at B; every four-step A-to-D trip reduces to A-B-D. For example B-A-B-A-B disappears, while A-B-A-B-D leaves A-B-D.

## key [2-3]
The three printed routes reduce, in order, to ABDE, ABDE, and CBDF. One different seven-step route from C to F is CBABDEDF. Its two removable excursions are B$\to$A$\to$B and D$\to$E$\to$D; what remains is CBDF.

## key [4-5]
Printed results: ABDE, ABDE, CBDF. The seven-step construction CBABDEDF is one valid new C-to-F input with reduced path CBDF. The listed C-to-F input has five steps; the new route must meet the requested seven-step constraint.
