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

\begin{tikzpicture}[x=1cm,y=1cm,font=\fontsize{11}{13}\selectfont]
\path[use as bounding box] (0,-.6) rectangle (17.2,2.05);
\foreach \x/\y/\n in {1/0/K,3/0/L,3/1.5/M,1/1.5/N}{\fill (\x,\y) circle (.05);\node[above left] at (\x,\y) {\n};}
\node at (2,-.45) {four labels};
\draw[->] (3.7,.75)--(4.7,.75);
\node[align=center] at (7,.75) {one group: K, M\\other group: L, N};
\draw[->] (9.3,.75)--(10.3,.75);
\draw[blue!65!black,line width=1.2pt] (11,0)--(13,1.5);
\draw[red!65!black,dashed,line width=1.2pt] (13,0)--(11,1.5);
\foreach \x/\y/\n in {11/0/K,13/0/L,13/1.5/M,11/1.5/N}{\fill (\x,\y) circle (.05);\node[above left] at (\x,\y) {\n};}
\draw[line width=.8pt] (12,.75) circle (.16);
\node[align=left,anchor=west] at (13.6,.75) {both regions\\contain this point};
\draw[->] (13.5,.6)--(12.2,.75);
\end{tikzpicture}
\end{center}"""
