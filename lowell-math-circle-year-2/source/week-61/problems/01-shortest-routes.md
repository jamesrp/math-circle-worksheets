+++
id = "w61.shortest-routes"
title = "Shortest routes for close, far and opposite pairs"
grades = ["shared"]
route = "first"
kernel = 'The shortest surface route between two points that are not opposite is the shorter great-circle arc; opposite points have infinitely many shortest routes.'
+++

## prompt
Choose a close pair of markers, a far-apart pair that is not opposite, and a pair exactly opposite each other on your ball. Find the shortest surface routes for each pair. Which pairs let you find two different routes of the same shortest length? Draw your routes.

## text
\begin{center}\begin{tabular}{ccc}
\small Close pair & \small Far-apart pair & \small Opposite pair\\
\begin{tikzpicture}[x=.82in,y=.82in]\draw[ink!60] (0,0) circle (1);\path[use as bounding box] (-1.25,-1.15) rectangle (1.25,1.15);\end{tikzpicture}&
\begin{tikzpicture}[x=.82in,y=.82in]\draw[ink!60] (0,0) circle (1);\path[use as bounding box] (-1.25,-1.15) rectangle (1.25,1.15);\end{tikzpicture}&
\begin{tikzpicture}[x=.82in,y=.82in]\draw[ink!60] (0,0) circle (1);\path[use as bounding box] (-1.25,-1.15) rectangle (1.25,1.15);\end{tikzpicture}
\end{tabular}\end{center}
\writing{3}
