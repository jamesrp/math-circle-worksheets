+++
id = "w95.rules"
kind = "setup"
title = "Catch, mark, return, catch again"
grades = ["2-3", "4-5"]
route = ["first", "return"]
+++

## text
Use identical-size cards or counters with visible marker dots that cannot be felt. Keep the same objects throughout a series; add, remove or exchange none except for temporary catches. For sampling trials, draw without looking; every group of the chosen size should have the same chance, whether marked or unmarked.

Keep each catch out until it is counted. Mark the first catch, return \emph{all} of it, and mix before the second catch. Marks stay on through both catches. An overlap is a marked object in the second catch. Before a new round, return everything and clear the marks. To show a record is possible, you may arrange catches: use distinct objects in each catch, from the same bag.
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth]
% Six identities persist through the entire operation.
\node[anchor=west,font=\small] at (0,5.55) {Start: six unmarked objects};
\draw[rounded corners] (0,4.25) rectangle (4.95,5.25);
\card{.5}{4.52}{A}{0}\card{1.15}{4.52}{B}{0}\card{1.8}{4.52}{C}{0}\card{2.45}{4.52}{D}{0}\card{3.1}{4.52}{E}{0}\card{3.75}{4.52}{F}{0}
\draw[->,thick] (2.5,4.12)--(2.5,3.57) node[midway,right,font=\scriptsize]{catch 2};
\node[anchor=west,font=\small] at (0,3.28) {First catch: A, C};
\draw[rounded corners] (0,1.5) rectangle (4.95,3);
\node[font=\scriptsize] at (2.5,2.78) {Bag: B, D, E, F};
\card{.45}{2.02}{B}{0}\card{1.5}{2.02}{D}{0}\card{2.55}{2.02}{E}{0}\card{3.6}{2.02}{F}{0}
\card{.6}{.68}{A}{0}\card{1.17}{.68}{C}{0}
\draw[->] (1.85,.91)--(2.65,.91) node[midway,above,font=\scriptsize]{mark};
\card{2.85}{.68}{A}{1}\card{3.42}{.68}{C}{1}
\node[font=\scriptsize] at (2.5,.30) {Same A and C, now marked};
\draw[->,thick] (5.15,2.1)--(5.75,2.1);
\node[anchor=west,font=\small] at (5.95,3.28) {Return all; mix};
\draw[rounded corners] (5.95,.65) rectangle (9.83,3);
\card{6.3}{2.03}{D}{0}\card{7.43}{2.03}{A}{1}\card{8.56}{2.03}{F}{0}
\card{6.3}{1.13}{C}{1}\card{7.43}{1.13}{E}{0}\card{8.56}{1.13}{B}{0}
\node[font=\scriptsize] at (7.9,.30) {Same six objects};
\draw[->,thick] (10.03,2.1)--(10.63,2.1);
\node[anchor=west,font=\small] at (10.83,3.28) {Second catch: C, D, F};
\draw[rounded corners] (10.83,1.5) rectangle (15.85,3);
\node[font=\scriptsize] at (13.35,2.78) {Bag: A, B, E};
\card{11.55}{2.02}{A}{1}\card{12.85}{2.02}{B}{0}\card{14.15}{2.02}{E}{0}
\card{11.55}{.68}{C}{1}\card{12.85}{.68}{D}{0}\card{14.15}{.68}{F}{0}
\draw (11.76,.9) ellipse (.36 and .36);
\node[font=\scriptsize] at (13.35,.22) {Overlap: C (1 object)};
\end{tikzpicture}
\end{center}
