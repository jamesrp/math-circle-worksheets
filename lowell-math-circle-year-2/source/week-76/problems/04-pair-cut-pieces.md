+++
id = "w76.pair-cut-pieces"
title = "Every way to pair four cut pieces"
grades = ["3-5"]
route = "first"
page = "new"
kernel = "Trying both alignments recovers a cut piece's seams; equal neighbours always straddle a seam."
+++

## text
\promptat{0}

## prompt
Each piece below was cut from a longer row grown from A. Find every way to pair the tiles as AB or BA. Use every tile, apart from at most one lone tile at each end. Decode only complete pairs.

## text
\Label{24}{38}{cut piece}
\Label{91}{38}{pairs}
\Label{156}{38}{old tiles kept}
\Strip{4}{42}{A,A,B,B,A}{8}
\Arrow{48}{46}{58}{46}
\draw[dashed,line width=.5pt] (64,42) rectangle (72,50);
\node[font=\large,inner sep=0pt] at (68,46) {A};
\Strip{77}{42}{A,B}{8}
\Strip{98}{42}{B,A}{8}
\node[font=\scriptsize,anchor=north,inner sep=0pt] at (68,53) {lone};
\Arrow{121}{46}{138}{46}
\Strip{148}{42}{A,B}{8}
\Strip{7}{80}{A,B,A}{9}
\Strip{100}{80}{B,A,A,B,A}{9}
\Strip{7}{127}{A,A,B,B}{9}
\Strip{100}{127}{A,B,B,A,A,B,B,A}{9}
