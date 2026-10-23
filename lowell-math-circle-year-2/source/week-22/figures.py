"""Week 22 figures, carried over from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py and examples.py).

Coordinates are centimetres on a 12.6 cm board, y up. board() draws a full work board
with labelled dots and optional crosses; recording_boards() draws small copies that keep
answers (their number does not give a count); region_key() draws the opening key of
regions and the K-L-M-N worked split. Problem files call these by name in their
`figure` sections, with the point lists below.

October 23, 2026 card fixes: the key's triangle HIJ marks an inside location with a small
dot instead of a cross, so it no longer looks like the boards' crosses for D.
"""


def board(points=(), crosses=(), coincidence=False):
    out=[r'\vspace{0.38cm}',r'\begin{center}',r'\begin{tikzpicture}[x=1cm,y=1cm]',r'\path[use as bounding box] (-0.04,-0.04) rectangle (12.64,12.64);',r'\draw[black!27,line width=0.4pt] (0,0) rectangle (12.6,12.6);']
    for label,x,y,anchor in points:
        out.append(fr'\fill ({x},{y}) circle (0.057cm);')
        out.append(fr'\node[{anchor},inner sep=0pt,font=\fontsize{{14}}{{16}}\selectfont] at ({x},{y}) {{{label}}};')
    for x,y in crosses:
        out.append(fr'\draw[line width=0.8pt] ({x-0.09:.3f},{y-0.09:.3f}) -- ({x+0.09:.3f},{y+0.09:.3f}) ({x-0.09:.3f},{y+0.09:.3f}) -- ({x+0.09:.3f},{y-0.09:.3f});')
    out.extend([r'\end{tikzpicture}',r'\end{center}'])
    return '\n'.join(out)


def recording_boards(configurations, columns=2, size=5.7):
    """Unassigned copies to keep answers; their number does not give a count."""
    rows=(len(configurations)+columns-1)//columns
    gap=0.48
    scale=size/12.6
    out=[r'\vspace{0.38cm}',r'\begin{center}',r'\begin{tikzpicture}[x=1cm,y=1cm]']
    for i,points in enumerate(configurations):
        col=i%columns
        row=rows-1-i//columns
        ox=col*(size+gap)
        oy=row*(size+gap)
        # A single affine coordinate transform preserves all exact incidences.
        out.append(fr'\begin{{scope}}[shift={{({ox:.4f},{oy:.4f})}},x={scale:.14f}cm,y={scale:.14f}cm]')
        out.append(r'\draw[black!27,line width=0.4pt] (0,0) rectangle (12.6,12.6);')
        for label,x,y,anchor in points:
            anchor=anchor.replace('5pt','4pt').replace('6pt','4pt')
            out.append(fr'\fill ({x},{y}) circle (0.045cm);')
            out.append(fr'\node[{anchor},inner sep=0pt,font=\fontsize{{11}}{{13}}\selectfont] at ({x},{y}) {{{label}}};')
        out.append(r'\end{scope}')
    out.extend([r'\end{tikzpicture}',r'\end{center}'])
    return '\n'.join(out)


def repeated(points, count=6):
    return recording_boards([points]*count)


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
\fill (14.38,1.48) circle (.04);
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


# Point lists: (label, x, y, label anchor).
k_tri=[('A',2,2,'below left=5pt'),('B',10,3,'below right=5pt'),('C',4,10,'above=5pt')]
k_edge=[('A',2,3,'below=5pt'),('B',8,3,'below=5pt'),('C',5,10,'above=5pt')]
k_line=[('A',1.8,6.3,'above=6pt'),('B',10.8,6.3,'above=6pt'),('C',7.5,6.3,'above=6pt'),('D',4.5,6.3,'above=6pt')]
m_tri=[('A',2,3,'below left=5pt'),('B',10,2,'below right=5pt'),('C',3,10,'above=5pt')]
m_line=[('A',2,6.3,'above=6pt'),('B',7.8,6.3,'above=6pt'),('C',10.8,6.3,'above=6pt'),('D',4.6,6.3,'above=6pt')]
u_tri=[('A',2,2,'below left=5pt'),('B',10.5,3,'below right=5pt'),('C',4.5,10,'above=5pt')]
u_line=[('A',2,3,'below right=5pt'),('B',8,9,'below right=5pt'),('C',5,6,'below right=5pt'),('D',10,11,'below right=5pt')]
