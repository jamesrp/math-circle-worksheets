+++
id = "w26.longest-boundary"
title = "Longest boundary with 4, 7, 10 and 12 tiles"
grades = ["2-3"]
route = "first"
kernel = 'A connected shape of $n$ tiles has at least $n - 1$ shared sides, so its boundary is at most $2n + 2$: 10, 16, 22 and 26.'
+++

## prompt
Find the longest possible boundary with 4, 7, 10, and 12 tiles. Explain why no shape with that many tiles can have a longer boundary.

## figure
m_longest_grids()

## key
\emph{Print guide, p. 10.} Maxima 10, 16, 22, 26.

A connected shape needs at least $n - 1$ meetings, so $P = 4n - 2e$ is at most $2n + 2$. The rows attain it. Explain the connection bound by discovering tiles one at a time through the already connected part, assigning each new tile a distinct joining edge. Extra meetings can only make the boundary shorter. This proves the maximum for every n, not just these four trials.
