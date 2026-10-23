+++
id = "w76.grow-and-triples"
title = "Grow 16 tiles and find every triple"
grades = ["3-5"]
route = "first"
kernel = "Each row grown from A begins with the one before, and only six of the eight possible triples ever appear."
+++

## text
\promptat{76}

## prompt
Grow a row of 16 tiles from A. Find every different strip of three neighboring tiles in your row. Record each short strip once.

## text
\Blank{11}{105}{16}{10}
\foreach \x in {9,54,99,144}{\Blank{\x}{130}{3}{10}\Blank{\x}{153}{3}{10}}
