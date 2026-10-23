+++
id = "w54.collections-of-4-and-5"
title = "Every collection of 4 and of 5 units"
grades = ["shared"]
route = "first"
page = "same"
kernel = 'A collection of strips is a partition: unordered positive sizes adding to the total; 4 has five and 5 has seven.'
+++

## prompt @7.53
Find every collection you can make with 4 units, and with 5 units. Record each once, as rows or sizes.

## text
\labelat{0.6}{6.78}{4 units}
\draw[rulegray,line width=0.5pt] (0.6,6.51) rectangle (7.9,4.43);
\draw[gridgray,line width=0.4pt] (0.6,5.47)--(7.9,5.47);
\foreach \xx in {3.03333,5.46666}{\draw[gridgray,line width=0.4pt] (\xx,6.51)--(\xx,4.43);}
\labelat{0.6}{4.12}{5 units}
\draw[rulegray,line width=0.5pt] (0.6,3.85) rectangle (7.9,0.9);
\draw[gridgray,line width=0.4pt] (0.6,2.375)--(7.9,2.375);
\foreach \xx in {2.425,4.25,6.075}{\draw[gridgray,line width=0.4pt] (\xx,3.85)--(\xx,0.9);}
