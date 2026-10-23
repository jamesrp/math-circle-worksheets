+++
id = "w26.area-rule"
title = "A rule for the greatest area, and 37, 50 and 73 squares"
grades = ["4-5"]
route = "return"
kernel = 'The greatest area inside boundary $2s$ is $\lfloor s/2\rfloor\lceil s/2\rceil$, so the least boundary for $n$ tiles is $2\lceil 2\sqrt{n}\,\rceil$: 26, 30 and 36 for 37, 50 and 73.'
+++

## prompt
Give a rule for the greatest number of squares in a shape with any even boundary length of at least 4. Explain why your rule works. Use it to find the shortest possible boundaries for shapes with 37, 50, and 73 squares, and draw shapes that reach them.

## figure
u_rule_grids()

## key
\emph{Print guide, p. 17.} \textbf{Rule:} halve the even boundary $P$ to get $s$. Split $s$ into two positive whole numbers as equal as possible, $a = \lfloor s/2\rfloor$, $b = \lceil s/2\rceil$. The greatest area is $ab$.

Every shape has area $n$ at most $rc$ and $r + c$ at most $s$. If $r + c$ is smaller, increase a dimension until the sum is $s$; the product increases. With sum $s$ fixed, replacing $(r,c)$ by $(r + 1,c - 1)$ when $c$ is at least $r + 2$ increases the product by $c - r - 1$. Repeat until the dimensions differ by at most one. This proves $n$ at most $ab$. The full $a$-by-$b$ rectangle has area $ab$ and boundary $2(a + b) = P$, so the bound is attained. $P$ at least 4 makes both dimensions positive.

\textbf{37:} boundary 24 permits at most $6 \times 6 = 36$. The pictured 6-by-6 square plus one tile has 37 and boundary $24 + 2 = 26$. \textbf{50:} boundary 28 permits at most $7 \times 7 = 49$. The pictured 7-by-7 square plus one tile has 50 and boundary $28 + 2 = 30$. \textbf{73:} boundary 34 permits at most $8 \times 9 = 72$. The pictured 8-by-9 rectangle plus one tile has 73 and boundary $34 + 2 = 36$.

All three added tiles meet the rectangle on exactly one side. Each next even boundary is attained; the preceding one and all smaller values are impossible. Thus the exact minimum boundaries are \textbf{26, 30, 36}.
