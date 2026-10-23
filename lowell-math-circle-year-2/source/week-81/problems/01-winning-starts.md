+++
id = "w81.winning-starts"
title = "Which starts let the first player win?"
grades = ["2-5"]
route = "first"
kernel = "With at most one counter added to each earlier bucket, the second player wins exactly from the all-even starts, so (2, 2, 2) is the only second-player win here."
+++

## prompt
Play each start with a partner. Which starts let the first player win whatever the second player does?

## text
\begin{center}
\begin{tabular}{@{}c@{\hspace{.75in}}c@{}}
 \smallstart{0}{0}{1} & \smallstart{1}{1}{0} \\[25pt]
 \smallstart{2}{1}{1} & \smallstart{2}{2}{2}
\end{tabular}
\end{center}
\vspace{12pt}
\begin{tikzpicture}
 \draw[black!35] (0,0) rectangle (17.5,2.5);
\end{tikzpicture}
