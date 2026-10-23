+++
id = "w60.new-bags-continued"
kind = "setup"            # the second page of the problem before it; headed "Problem 7 (continued)" with no restated task
title = "Best first-offer choices for new bags, continued: bag 0, 2, 6"
grades = ["shared"]
route = "first"           # the same route as w60.new-bags
page = "new"
kernel = "For 0, 2, 6 the middle 2 is below the next draw's average 8/3, so pass 0 and 2 and take 6: total 34, uniquely best."
+++

## text
\renewcommand{\band}{Grades 3--5}
\textbf{Problem 7 (continued)}

\vspace{0.07in}
\begin{tikzpicture}[x=1in,y=1in]
\node[font=\normalsize,anchor=west] at (0,3.23) {Bag: 0, 2, 6};
\foreach \a [count=\r from 0] in {0,2,6}{
\foreach \b [count=\c from 0] in {0,2,6}{
\cardtwo{\c*2.28}{(2-\r)*1.01}{\a}{\b}
}}
\end{tikzpicture}

Choices: \rule{4.32in}{0.3pt}\hspace{0.16in}Total: \rule{0.82in}{0.3pt}
