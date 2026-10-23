+++
id = "w92.move-rule"
title = "The move and its map"
grades = ["shared"]
route = "first"
kind = "setup"
+++

## figure
band('Grades 2--5')

## text @0
One move: find the nearer-end distance in track units, then double it. On the map, go up from your input to the sloping line, then across to read the distance and output. Put the marker at the output on the 0--16 track. Points between ticks are allowed.

## figure
r'''\movemap{-123}{5}
\draw[arr,dashed] (142,-123)--(142,-93);
\draw[arr,dashed] (142,-93)--(172,-93);
\draw[arr,dashed] (142,-93)--(12,-93);
\fill[ink] (142,-123) circle(1);\fill[ink] (142,-93) circle(1);
\node[fill=white,inner sep=1.5mm,font=\scriptsize] at (89,-110){input 13 $\longrightarrow$ distance 3 $\longrightarrow$ output 6};'''
