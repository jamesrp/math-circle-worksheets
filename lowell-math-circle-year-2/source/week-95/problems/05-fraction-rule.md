+++
id = "w95.fraction-rule"
title = "A fraction-matching guess"
grades = ["4-5"]
route = "first"
kernel = "Matching the marked fraction gives the estimate $Mn/R$, which a different possible bag shows is not forced."
+++

## prompt
A proposed guessing rule chooses a total that makes the marked fraction in the bag match the marked fraction in the second catch.

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth]
\node[font=\small,align=center] at (2.1,2.25) {Example: 2 marked in the bag};
\node[font=\small] at (2.1,1.75) {Second catch};
\draw[rounded corners] (.6,.65) rectangle (3.6,1.45);
\card{1}{.82}{A}{1}\card{1.9}{.82}{B}{0}\card{2.8}{.82}{C}{0}
\node[font=\small] at (2.1,.28) {1 marked out of 3};
\draw[->,thick] (4.1,1.1)--(4.9,1.1);
\node[font=\small] at (8.15,2.25) {Matching bag model: 2 equal groups};
\node[font=\scriptsize] at (6.45,1.75) {Same sample};
\node[font=\scriptsize] at (9.85,1.75) {Same marked fraction};
\draw[rounded corners] (4.95,.55) rectangle (11.35,1.5);
\draw[rounded corners] (5.05,.65) rectangle (7.95,1.4);
\draw[rounded corners] (8.35,.65) rectangle (11.25,1.4);
\card{5.4}{.82}{A}{1}\card{6.25}{.82}{B}{0}\card{7.1}{.82}{C}{0}
\card{8.7}{.82}{D}{1}\card{9.55}{.82}{E}{0}\card{10.4}{.82}{F}{0}
\node[font=\small] at (8.15,.12) {1 marked out of 3 in each group};
\draw[->,thick] (11.55,1.1)--(12.2,1.1);
\node[font=\small,align=center] at (14,1.4) {Rule's guess: 6 total};
\node[font=\small] at (14,.65) {$\dfrac{2}{6}=\dfrac{1}{3}$};
\end{tikzpicture}
\end{center}
Find the rule's guess for record A. Does the catch record force that total?

\begin{center}
\begin{tikzpicture}
\node[anchor=west] at (0,1.1) {Whole bag after marking};
\node[anchor=west] at (9,1.1) {Second catch};
\draw[rounded corners] (0,-.65) rectangle (6.8,.65);
\foreach \x in {0,...,5}{\draw (0.5+\x*.65,0) circle (.23);\fill (0.5+\x*.65,0) circle (.055);}
\node at (5.25,0) {\Large ?};
\foreach \x in {0,...,5}{\draw (9.3+\x*.65,0) circle (.23);}
\fill (9.3,0) circle (.055);\fill (9.95,0) circle (.055);
\node at (3.4,-1.05) {6 marked; total unknown};
\node at (10.9,-1.05) {2 marked out of 6};
\end{tikzpicture}
\end{center}
