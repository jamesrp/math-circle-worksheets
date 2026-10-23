+++
id = "w54.split-and-rejoin"
title = "Split, then join again: does each collection return?"
grades = ["shared"]
route = "first"
page = "same"
kernel = 'Splitting every even strip and then joining equal pairs returns any collection whose sizes all differ.'
+++

## prompt @7.34
Build each collection. Split even-size strips until only odd sizes remain. Join equal pairs until all sizes are different again. Does each starting collection return?

## text
\centerlabel{1.46}{6.33}{Before}
\centerlabel{3.73}{6.33}{Only odd sizes}
\centerlabel{6.51}{6.33}{After joining}
\foreach \top in {6.01,4.28,2.55}{
 \draw[rulegray,line width=0.5pt] (0.6,\top) rectangle ++(7.3,-1.5);
 \foreach \xx in {2.28,5.08}{\draw[gridgray,line width=0.4pt] (\xx,\top)--++(0,-1.5);}
}
\strips{0.76}{5.79}{0.105}{10,7,4,2,1}
\strips{0.76}{4.06}{0.105}{12,6,3}
\strips{0.76}{2.31}{0.13}{7,3,1}
