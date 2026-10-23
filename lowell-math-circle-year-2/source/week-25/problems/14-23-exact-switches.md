+++
id = "w25.23-exact-switches"
title = "Exactly one switch, exactly two switches"
grades = ["2-3"]
route = "return"
kernel = "One switch replaces one top-row column, so a picture whose top row shares no column with the start needs two switches."
+++

## prompt @27
Make a picture on the middle grid that takes exactly one switch to reach from the top picture. Make a picture on the bottom grid that takes exactly two switches and cannot be reached in one. Explain why one switch cannot reach it.

## figure
m_exact_switches()

## key
\emph{Print guide, p. 11.} \textbf{One complete answer:} use the middle picture below on the middle grid and the last picture on the bottom grid. The route switches columns 1,3 and then 2,4.

\textbf{Why two cannot be one:} initially A occupies columns 1 and 2; in the last picture it occupies 3 and 4. One switch removes only one top-row counter from its old column and puts it in one new column. Two unwanted top positions must be removed, so at least two switches are necessary. The displayed route achieves two.
