+++
id = "w12.rules"
kind = "setup"            # unnumbered shared rules and a worked example, on page 1 with Problem 1
title = "Pairing rules (K-1, grades 2-3) and tree rules (grades 4-5)"
grades = ["K-1", "2-3", "4-5"]
route = ["first", "return"]
+++

## text @18,29 size=12.5 [K-1]
Use each dot once. Keep dots in place. Strings stay inside the circle without crossings. Pairings are different when a dot has a different partner. Use strings on large circles and a pencil on small circles.

## text @18,29 size=12.3 [2-3]
\fontsize{12.3}{15}\selectfont Use each dot once. Keep strings above the row without crossings. Keep dots in place. Pairings are different when a dot has a different partner.\par

## text @18,29 size=12.3 [4-5]
Draw dots joined by lines called edges. The filled dot at the top is the root. Each edge joins a parent dot to a child dot below it. Every dot except the root has exactly one parent. Keep each parent's children in a fixed left-to-right order. All dots connect to the root. Only the branching and its order matter.

## figure [K-1]
k1_four_dot_example('The two pairings of four dots:')

## figure [2-3]
ten_dot_example('Example with ten dots:')

## figure [4-5]
five_edge_example('Example with five edges:')
