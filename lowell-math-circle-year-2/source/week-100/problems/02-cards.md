+++
id = "w100.cards"
kind = "setup"
title = "Cut-out cards A-F and labels 2, 4, 8"
grades = ["3-5"]
route = ["first", "return"]
page = "same"
+++

## text
% Letter-and-shape cards: 27 mm square.
\foreach \x/\letter in {0/A,29/B,58/C,87/D,116/E,145/F}{
\draw[dashed,black!60,line width=.5pt] (\x,151) rectangle (\x+27,178);
\node[font=\fontsize{21}{24}\selectfont] at (\x+8,160) {\letter};}
\draw[line width=.8pt] (19,169) circle (4mm);
\draw[line width=.8pt] (48,165)--(52,173)--(44,173)--cycle;
\draw[line width=.8pt] (73,165) rectangle (81,173);
\node[star,star points=5,star point ratio=2.2,draw,line width=.8pt,minimum size=10mm,inner sep=0pt] at (106,169) {};
\node[regular polygon,regular polygon sides=5,draw,line width=.8pt,minimum size=9mm,inner sep=0pt] at (135,169) {};
\node[regular polygon,regular polygon sides=6,draw,line width=.8pt,minimum size=9mm,inner sep=0pt] at (164,169) {};
\foreach \x/\n in {176/2,195/2,214/2,233/2}{\draw[dashed,black!60] (\x,151) rectangle (\x+17,163);\node[font=\fontsize{19}{21}\selectfont] at (\x+8.5,157) {\n};}
\foreach \x/\n in {176/4,195/4,214/8,233/8}{\draw[dashed,black!60] (\x,166) rectangle (\x+17,178);\node[font=\fontsize{19}{21}\selectfont] at (\x+8.5,172) {\n};}
