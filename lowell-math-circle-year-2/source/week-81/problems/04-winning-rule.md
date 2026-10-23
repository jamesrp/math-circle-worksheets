+++
id = "w81.winning-rule"
title = "A rule for winning moves"
grades = ["2-5"]
route = "first"
page = "new"
kernel = "When some bucket is odd, take one from the rightmost odd bucket and add one to each earlier odd bucket: every bucket is then even, and the opponent must break that."
+++

## prompt
Play from these three-bucket starts. Can you find a rule for choosing a winning move whenever there is one?

## text
\begin{center}
\begin{tabular}{@{}c@{\hspace{.75in}}c@{}}
 \smallstart{2}{2}{2} & \smallstart{1}{2}{2} \\[22pt]
 \smallstart{2}{1}{2} & \smallstart{2}{2}{1} \\[22pt]
 \smallstart{0}{2}{0} & \smallstart{3}{3}{1}
\end{tabular}
\end{center}
\vspace{10pt}
\begin{tikzpicture}
 \draw[black!35] (0,0) rectangle (17.5,3.8);
\end{tikzpicture}
