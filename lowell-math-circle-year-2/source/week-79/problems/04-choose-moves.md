+++
id = "w79.choose-moves"
title = "Choose the moves: which six cards can B hold?"
grades = ["2-5"]
route = ["first", "return"]
page = "new"
kernel = "A card cannot move before it enters, so by day d only cards 1 to 2d can be in B: a target is reachable exactly when, for every day d, at least d of its cards are at most 2d."
+++

## prompt
Start again, but now you choose which card in A moves to B each day. After six days, can B hold the six cards in each row?

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
  \foreach \row/\cards in {0/{1,3,5,7,9,11},1/{2,3,5,7,8,11},2/{1,4,6,9,11,12}} {
    \foreach \v [count=\i] in \cards {
      \draw[line width=0.7pt,rounded corners=2pt] (1.95*\i-1.95,-7.3*\row) rectangle (1.95*\i-0.45,-7.3*\row+1.5);
      \node[font=\fontsize{20}{24}\selectfont] at (1.95*\i-1.2,-7.3*\row+0.75){\v};
    }
    \draw[gray!55,line width=0.5pt] (0,-7.3*\row-0.5) rectangle (18.4,-7.3*\row-5.5);
  }
\end{tikzpicture}
\end{center}
