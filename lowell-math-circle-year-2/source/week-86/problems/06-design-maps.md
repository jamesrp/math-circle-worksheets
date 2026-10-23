+++
id = "w86.design-maps"
title = "Design a cop-win and a robber-win map"
grades = ["4-5"]
route = "return"
kernel = "Six dots and six roads force a cycle, yet such maps can go either way: a triangle with a tail is cop-win, the six-ring robber-win."
+++

## prompt
Draw two connected maps using all six dots and at least six roads on each. Make one where C can always catch R and one where R can escape forever. Challenge your partner on both. Roads join dots; crossings are not junctions. Join any pair at most once.

## figure
graph(cycle(6, 32)[0], [], 96, 86, label='D1: C can always catch R') + graph(cycle(6, 32)[0], [], 96, 186, label='D2: R can escape forever')

## key
One cop-win example uses the triangle a--b--c--a with tail c--d--e--f: six dots and six roads. Start C at c. Catch an initial robber at a or b immediately; otherwise sweep the tail. R cannot pass through C to use the triangle. The bare six-cycle is a robber-win example with the same dot/road counts. These examples show that a cycle's presence does not by itself imply escape.

The minimum six-road condition makes a tree unavailable as the cop example, so it serves this comparison rather than an arbitrary drawing restriction. Accept other connected maps with valid response strategies; do not judge from visual resemblance. A held hint is to attach a branch to a board whose behavior the children already understand. Crossings drawn without a dot do not create roads between the crossing routes.
