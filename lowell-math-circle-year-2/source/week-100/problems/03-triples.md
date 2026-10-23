+++
id = "w100.triples"
title = "Which triples of distances can loops make?"
grades = ["3-5"]
route = "first"
page = "new"
kernel = "Among any three cards the largest distance occurs at least twice: 2, 2, 4 and 2, 4, 8 cannot be made."
+++

## text
% Page 2: contrasting triples, with no count of possible cases disclosed.

## prompt
Use A, B, C and labels 2, 4, 8. Make each set of distances with loops, or cross it out if it cannot be made. Choose one crossed-out set and explain why no arrangement works.

## text
\foreach \x/\y/\a/\b/\c in {0/29/2/2/2,85/29/2/4/4,170/29/2/2/4,0/105/4/4/4,85/105/2/4/8,170/105/2/8/8}{
\draw[black!35,rounded corners=1mm] (\x,\y) rectangle (\x+80,\y+70);
\node[anchor=north,inner sep=0pt,font=\fontsize{12}{14}\selectfont] at (\x+40,\y+4) {A--B = \a\quad A--C = \b};
\node[anchor=north,inner sep=0pt,font=\fontsize{12}{14}\selectfont] at (\x+40,\y+12) {B--C = \c};
}
