def region_key():
    return r"""\vspace{0.15cm}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\fontsize{11}{13}\selectfont]
\path[use as bounding box] (0,-.65) rectangle (17.2,2.8);
\node at (.4,1.5) {E};
\draw[->,line width=.7pt] (.95,1.5) -- (1.8,1.5);
\fill (2.65,1.5) circle (.055);
\node[above=5pt] at (2.65,1.5) {E};
\node at (2.65,.35) {point};
\node at (5.25,1.5) {F, G};
\draw[->,line width=.7pt] (6,1.5) -- (6.8,1.5);
\draw[line width=1pt] (7.35,1.5) -- (9.2,1.5);
\fill (7.35,1.5) circle (.055);\fill (9.2,1.5) circle (.055);
\node[above=5pt] at (7.35,1.5) {F};\node[above=5pt] at (9.2,1.5) {G};
\node at (8.275,.35) {whole segment};
\node at (11.1,1.5) {H, I, J};
\draw[->,line width=.7pt] (12.15,1.5) -- (12.8,1.5);
\filldraw[fill=black!9,line width=.7pt] (13.35,.8) -- (15.75,.8) -- (14.35,2.55) -- cycle;
\foreach \x/\y in {13.35/.8,15.75/.8,14.35/2.55}{\fill (\x,\y) circle (.055);}
\node[below left=2pt] at (13.35,.8) {H};\node[below right=2pt] at (15.75,.8) {I};\node[above=2pt] at (14.35,2.55) {J};
\draw[line width=.8pt] (14.3,1.40) -- (14.46,1.56) (14.3,1.56) -- (14.46,1.40);
\node at (14.55,-.35) {edge and inside};
\end{tikzpicture}
\end{center}"""
