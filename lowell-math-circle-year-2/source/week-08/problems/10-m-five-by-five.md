+++
id = "w08.m-five-by-five"
title = "Four starts on a 5-by-5 board"
grades = ["2-3"]
route = "first"
+++

## prompt
Play many games on a 5-by-5 board from each of these starting squares. Would you
rather go first or second?

## text
\vspace{0.3in}

## figure
grid2([stack(board(5, 0.46, dots=[d]), answer_line(1.8), sep="0.45in")
       for d in [(4, 4), (4, 2), (3, 3), (1, 4)]], vsep="0.4in")
