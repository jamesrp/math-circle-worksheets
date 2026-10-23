+++
id = "w54.join-until-different"
title = "Join equal pairs until all sizes differ"
grades = ["shared"]
route = "first"
page = "same"
kernel = 'Joining equal pairs always ends, with all sizes different; nine 1s end as 8 + 1, the binary digits of 9.'
+++

## prompt @7.31
Build each collection. Join equal-size pairs until all sizes are different. Record the final collection.

## text
\centerlabel{1.59}{6.66}{Before}
\centerlabel{5.37}{6.66}{All sizes different}
\foreach \top in {6.34,4.48,2.62}{
 \draw[rulegray,line width=0.5pt] (0.6,\top) rectangle ++(7.3,-1.58);
 \draw[gridgray,line width=0.4pt] (2.6,\top)--++(0,-1.58);
}
\strips{0.87}{6.18}{0.105}{1,1,1,1,1,1,1,1,1}
\strips{0.87}{4.3}{0.13}{5,5,3,3,3,1,1}
\strips{0.87}{2.44}{0.19}{5,3,1}
