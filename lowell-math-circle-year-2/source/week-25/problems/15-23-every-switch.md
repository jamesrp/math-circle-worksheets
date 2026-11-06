+++
id = "w25.23-every-switch"
title = "Every switch in four pictures"
grades = ["2-3"]
route = ["first", "return"]   # the return route's shortest-route problem needs the switch defined here
kernel = "A switch needs a column occupied in one row and not the other, and one the other way round; pictures whose rows nest have none."
+++

## prompt @27
A switch moves the two counters to the empty corners shown; every other cell stays fixed. The corners may use any two rows and columns. Find every switch in each picture and draw its rectangle. Which pictures have none?

## figure
m_switch_pictures('One switch:', record=True)

## key
\emph{Print guide, p. 11.} \textbf{Complete switch list:} children record a switch by drawing its rectangle through the four corner cells, as in the page 6 example. Top right has rows A,C and columns 1,3. The picture A1, A2, B3, C1 has rows A,B with columns 1,3; rows A,B with columns 2,3; and rows B,C with columns 1,3. Their results are respectively 011/100/100, 101/010/100, and 110/100/001, with slashes separating A/B/C. There are no others.

\textbf{Why the list is complete:} for each pair of rows, a switch needs a column occupied only in the first row and a column occupied only in the second. In the picture A1, A2, B3, C1, A versus B gives 2 choices; A versus C gives none because C is contained in A; B versus C gives 1. The top-left picture and the bottom staircase have nested occupied-column sets for every row pair, so no switch exists.

\textbf{Page 7} has four copies of the fourth picture, A1, A2, B3, C1, and no words of its own. Tell the children that these copies are extra workspace for further attempts: draw one switch's rectangle on each copy, and move on to a fresh copy when one gets crowded. The picture has three switches, so one copy stays spare.
