+++
id = "w92.band-rule"
title = "A band of possible places"
grades = ["shared"]
route = "first"
kind = "setup"
+++

## text @0
A band includes every position between its ends, including the ends. Move all of them through the map. One marker follows the rule from its unknown start; it is never placed at a fresh start.

## figure
r'''\movemap{-83}{3}
\fill[bandfill] (62,-84.3) rectangle (112,-81.7);
\draw[ink,line width=1.3mm] (62,-53)--(92,-35)--(112,-47);
\draw[ink,line width=1.3mm] (12,-53)--(12,-35);
\draw[ink,line width=1.3mm] (172,-53)--(172,-35);
\foreach \x/\y in {62/-53,92/-35,112/-47}{\draw[ink,dashed] (\x,-83)--(\x,\y);\draw[ink,dashed] (12,\y)--(172,\y);\fill[ink] (\x,-83) circle(0.8);\fill[ink] (\x,\y) circle(0.8);}
\node[anchor=north,font=\scriptsize] at (90,-98){Input band 5--10 $\longrightarrow$ distance band 5--8 $\longrightarrow$ output band 10--16};'''
