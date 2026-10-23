+++
id = "w70.first-target-on-the-map"
title = "Shots on the unfolded map"
grades = ["4-5"]
route = "first"
page = "new"
kernel = "Unfolding turns a shot that crosses edges into a straight line; it stops at the first T copy it reaches."
+++

## prompt
Aim straight shots from S at the T copies A $(2,6)$, B $(6,2)$, C $(6,6)$ and D $(10,6)$. Your partner marks the first T each shot reaches. In the small room, draw one shot that crosses an X or Y edge before reaching T.

## text
\begin{center}\mapwindow[1.0]{\foreach\x/\y/\l in{2/6/A,6/2/B,6/6/C,10/6/D}{\node[below right,font=\small\bfseries]at(\x,\y){\l};}}\end{center}
\begin{center}\room{1.0}{0}\end{center}
