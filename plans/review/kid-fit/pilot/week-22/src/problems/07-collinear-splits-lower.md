+++
id = "w22.collinear-splits-lower"
title = "Meeting splits of four dots on a line"
grades = ["K-1", "2-3"]
route = { "K-1" = "return", "2-3" = "first" }
page = "new"
kernel = "For four dots on a line, exactly four of the seven splits work: either middle dot alone, and the two pair splits that interleave or nest; an end dot alone, or the left pair against the right pair, fails."
+++

## prompt [K-1]
Find two different ways to make two groups whose regions meet. Draw one group just above the dots and the other group just below.

## prompt [2-3]
Find every split of A, B, C, and D whose regions meet. Explain how you know your list is complete.

## figure [K-1]
recording_boards([k_line_far]*4,columns=2,size=7.4)

## figure [2-3]
board(m_line_far)

## text [2-3]
\recordlines{2}

\newpage

## prompt [2-3]
Find every split of A, B, C, and D whose regions meet. Explain how you know your list is complete.

## figure [2-3]
repeated(m_line_far)
