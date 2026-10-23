+++
id = "w26.which-are-longest"
title = "Which eight-tile shapes have the longest boundary?"
grades = ["2-3"]
route = "return"
kernel = 'An eight-tile shape has the longest boundary, 18, exactly when it has 7 shared sides, so branches and bent paths qualify and the rectangle and the ring do not.'
+++

## prompt
Which of these eight-tile shapes have the longest possible boundary? Explain why each chosen shape reaches that length. Draw two more such shapes, with no straight row or column of four tiles.

## figure
m_which_longest()

## key
\emph{Print guide, p. 11.} In worksheet reading order the boundaries are \textbf{18, 18, 12, 16}. The straight and branching examples each have 7 shared sides. The rectangle has 10; the frame has 8. Since 8 tiles allow at most 18 exposed sides, exactly the first two reach the maximum.

Every eight-tile connected shape has at least seven meetings. A chosen example with exactly seven is automatically maximal, because $32 - 14 = 18$. Therefore a child does not have to compare it with every conceivable eight-tile shape. A branch is allowed: the key is the number of meetings, not whether the shape looks like a single path.
