+++
id = "w63.home-rules"
title = "Cards, homes and home matches"
kind = "setup"
grades = ["shared"]
route = ["first", "return"]
+++

## text
\renewcommand{\band}{Grades K--5}
Use a card set and the home strip with the same letters. Use each card once, with one card in every home. Keep the home labels fixed. A \emph{home match} means the card and its home have the same letter. Check a complete row before moving any card. Record the cards from left to right. A row with no home matches is \emph{home-free}.

\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \node[anchor=west,font=\small] at (0,14) {Placement};
  \rowdraw{0}{7}{U,V,W,X}{V,U,W,X}
  \draw[-{Stealth[length=2mm]}] (53,1)--(61,1);
  \node[anchor=west,font=\small] at (67,14) {Check the same placement};
  \rowdraw{67}{7}{U,V,W,X}{V,U,W,X}
  \foreach \s/\x in {no/73,no/85,yes/97,yes/109}{\node[font=\small] at (\x,-8) {\s};}
  \draw[-{Stealth[length=2mm]}] (120,1)--(128,1);
  \node[anchor=west,font=\small] at (133,14) {Record};
  \node[anchor=west,font=\large] at (133,3) {VUWX};
  \node[anchor=west,font=\small] at (133,-8) {2 home matches};
\end{tikzpicture}
\end{center}
