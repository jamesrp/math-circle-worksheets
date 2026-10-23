+++
id = "w92.widest-band"
title = "The widest band that stays near 0"
grades = ["shared"]
route = "return"
kernel = '$[0,q]$ stays in $[0,2]$ through $n$ moves exactly when $q\le 2/2^n$: $1/4$, $1/8$ and $1/32$ for 3, 4 and 6 moves.'
+++

## figure
band('Grades 4--5')

## prompt @0
A marker starts somewhere in a band with one end at 0. Make the widest starting band you can that keeps every possible position between 0 and 2 through the first 3 moves. Then try 4 moves and 6 moves.

## figure
r'''\track{-34}{The whole track}
\draw[ink,very thick] (8,-34)--(18,-34);
\fill[ink] (13,-34) circle(0.8);
\draw[gray,dashed] (8,-39)--(8,-62);\draw[gray,dashed] (18,-39)--(168,-62);
\draw[ink] (8,-62)--(168,-62);
\foreach \x/\lab in {8/0,88/{$\frac12$},168/1}{\draw[ink] (\x,-64)--(\x,-60);\node[anchor=north,font=\scriptsize] at (\x,-65){\lab};}
\fill[ink] (88,-62) circle(1);
\draw[ink,dashed] (13,-39)--(88,-60);
\node[anchor=west,fill=white,inner sep=1mm,font=\scriptsize] at (67,-48){The same position: $\frac12$};'''

## text @-77
Mark starting bands on these enlarged 0--1 lines. Moves still use the original 0--16 rule.

## figure
r'''\foreach \y/\lab in {-104/3 moves,-139/4 moves,-174/6 moves}{
\node[anchor=south west] at (8,\y+3){\lab};
\draw[ink] (8,\y)--(168,\y);
\draw[ink] (8,\y-2)--(8,\y+2);\draw[ink] (168,\y-2)--(168,\y+2);
\node[anchor=north,font=\scriptsize] at (8,\y-3){0};\node[anchor=north,font=\scriptsize] at (168,\y-3){1};}'''
