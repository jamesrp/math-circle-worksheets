+++
id = "w100.rebuild"
title = "Rebuild a world from ten clue cards"
grades = ["3-5"]
route = "first"
page = "new"
kernel = "Complete consistent distances determine the groups and their labels."
+++

## text
% Page 4: complete five-card data on movable clue cards.

## prompt
Use cards A through E to make a world that fits all ten clue cards. Use labels 2, 4, 8. Your partner checks each clue against the loops. Draw your world. Could a world with different groups fit the same ten clues?

## text
\draw[black!25,rounded corners=2mm] (0,29) rectangle (121,120);
\draw[black!25,rounded corners=2mm] (129,29) rectangle (250,120);
\foreach \x/\y/\pair/\n in {0/131/A--B/2,51/131/A--C/4,102/131/B--C/4,153/131/D--E/2,204/131/A--D/8,0/156/A--E/8,51/156/B--D/8,102/156/B--E/8,153/156/C--D/8,204/156/C--E/8}{
\draw[dashed,black!60,line width=.55pt] (\x,\y) rectangle (\x+46,\y+21);
\node[font=\fontsize{17}{19}\selectfont] at (\x+23,\y+10.5) {\pair\ = \n};}
