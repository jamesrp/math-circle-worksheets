+++
id = "w100.number-cards"
kind = "setup"
title = "Cut-out number cards 0-7"
grades = ["3-5"]
route = "return"
page = "same"
+++

## text
\foreach \x/\n in {6/0,36/1,66/2,96/3,126/4,156/5,186/6,216/7}{
\draw[dashed,black!60,line width=.55pt] (\x,151) rectangle (\x+27,178);
\node[font=\fontsize{25}{28}\selectfont] at (\x+13.5,164.5) {\n};}
