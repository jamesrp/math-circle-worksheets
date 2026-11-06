+++
id = "w22.collinear-splits"
title = "Every meeting split of four dots on a line"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "new"
kernel = "For four dots on a line, exactly four of the seven splits work: either middle dot alone, and the two pair splits that interleave or nest; an end dot alone, or the left pair against the right pair, fails."
+++

## prompt [K-1]
Find every split whose regions meet.

## prompt [2-3]
Find every split of A, B, C, and D whose regions meet. Explain how you know your list is complete.

## prompt [4-5]
Find every split whose regions meet. Explain how you know your list is complete.

## figure [K-1]
board(k_line)

## figure [2-3]
board(m_line)

## figure [4-5]
board(u_line)

## text [2-3, 4-5]
\recordlines{2}

\newpage

## text
\newpage

## prompt [K-1]
Find every split whose regions meet.

## prompt [2-3]
Find every split of A, B, C, and D whose regions meet. Explain how you know your list is complete.

## prompt [4-5]
Find every split whose regions meet. Explain how you know your list is complete.

## figure [K-1]
repeated(k_line)

## figure [2-3]
repeated(m_line)

## figure [4-5]
repeated(u_line)
