from pathlib import Path
from examples import region_key

ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'src'

PREAMBLE=r'''\documentclass[12pt,letterpaper]{article}
\usepackage[letterpaper,left=0.65in,right=0.65in,top=0.76in,bottom=0.67in,headheight=16pt,headsep=14pt,footskip=25pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage{tikz}
\usepackage{fancyhdr}
\renewcommand{\familydefault}{\sfdefault}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\setlength{\emergencystretch}{2em}
\raggedright
\newcommand{\problem}[2]{\textbf{Problem #1:} #2\par}
\newcommand{\recordlines}[1]{\vspace{0.30cm}\foreach \n in {1,...,#1}{\noindent\rule{\linewidth}{0.25pt}\par\vspace{0.72cm}}}
'''

RULES=r'''Use each label once in two groups, with at least one label in each. Draw each group's stretched-band region and lightly shade its inside. Use the centers of the marks. Sharing even one point counts. Swapping the two groups is the same split.'''


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


def packet(filename,level,packet_id,pages,k=False):
    fs='14' if k else '13'
    leading='18' if k else '17'
    out=[PREAMBLE,fr'\fancyhead[L]{{\fontsize{{10.5}}{{12}}\selectfont Week 22 / Meeting regions / {level}}}',fr'\fancyfoot[L]{{\fontsize{{9}}{{11}}\selectfont Bellingham Math Circle / Week 22 / {packet_id}}}',r'\fancyfoot[R]{\fontsize{9}{11}\selectfont\thepage}',r'\begin{document}',fr'\fontsize{{{fs}}}{{{leading}}}\selectfont']
    for i,p in enumerate(pages,1):
        if i>1:out.append(r'\newpage')
        else:out += [RULES+r'\par',region_key(),r'\vspace{0.15cm}']
        out.append(fr'\problem{{{i}}}{{{p[0]}}}')
        out.append(p[1])
        if len(p)>2 and p[2]:out.append(fr'\recordlines{{{p[2]}}}')
        if len(p)>3:
            for content,lines in p[3]:
                continuation_text = 'Find every split whose regions meet.' if k else p[0]
                out.extend([r'\newpage',fr'\problem{{{i}}}{{{continuation_text}}}',content])
                if lines:out.append(fr'\recordlines{{{lines}}}')
    out.append(r'\end{document}')
    (SRC/(filename+'.tex')).write_text('\n'.join(out)+'\n')

k_tri=[('A',2,2,'below left=5pt'),('B',10,3,'below right=5pt'),('C',4,10,'above=5pt')]
k_edge=[('A',2,3,'below=5pt'),('B',8,3,'below=5pt'),('C',5,10,'above=5pt')]
k_line=[('A',1.8,6.3,'above=6pt'),('B',10.8,6.3,'above=6pt'),('C',7.5,6.3,'above=6pt'),('D',4.5,6.3,'above=6pt')]
packet('k-1','K--1','F22-K-v3',[
    ('Put D on each cross. Each time, make two regions that meet and mark a point they share.',board(k_tri,[(9,9),(4.3,4.7),(0.8,7.2)])),
    ('Try D on each cross. Find every split whose regions meet.',board(k_edge,[(5,3),(11,3),(3.5,6.5)]),0,[(recording_boards([k_edge+[('D',x,y,'above right=5pt')] for x,y in [(5,3),(11,3),(3.5,6.5)] for _ in range(3)],columns=3,size=5.35),0)]),
    ('Find every split whose regions meet.',board(k_line),0,[(repeated(k_line),0)]),
    ('Keep A, B, and C fixed, and take turns placing D. Can the other player always make two regions that meet?',board(k_tri)),
    ('Keep A and B fixed, and try C on each cross. Find every place in the box where C can go so the two regions meet.',board([('A',2.5,5.6,'below=5pt'),('B',8.8,5.6,'below=5pt')],[(6,5.6),(11,5.6),(5.5,9.5)])),
    ('Take turns placing A, B, C, and D in the box. Can the other player always make two regions that meet?',board()),
],True)

m_tri=[('A',2,3,'below left=5pt'),('B',10,2,'below right=5pt'),('C',3,10,'above=5pt')]
m_line=[('A',2,6.3,'above=6pt'),('B',7.8,6.3,'above=6pt'),('C',10.8,6.3,'above=6pt'),('D',4.6,6.3,'above=6pt')]
packet('grades-2-3','Grades 2--3','F22-23-v3',[
    ('Put D on each cross. For each position, split A, B, C, and D so their two regions meet, and mark a shared point.',board(m_tri,[(9,9),(4,5),(6,2.5),(6,1)])),
    ('Find every split of A, B, C, and D whose regions meet. Explain how you know your list is complete.',board(m_line),2,[(repeated(m_line),0)]),
    ('Place A, B, C, and D so that their two regions share a whole straight segment. Can two groups made from these four labels share a filled triangle? Explain.',board(),2),
    ('Make two arrangements of A, B, C, and D. No split may work for both arrangements. Show a working split for each.',board(),0,[(board(),0)]),
    ('Can these three dots be split into two groups whose regions meet? Explain why your answer covers every split. Keep A and B fixed. Find every place in the box where C could go so that the regions meet.',board([('A',2,3,'below left=5pt'),('B',10,4,'below right=5pt'),('C',6,10,'above=5pt')]),2),
    ('Take turns placing A, B, C, and D in the box. Try to make an arrangement that the other player cannot split successfully. Can four dots always be split so their regions meet?',board(),2),
])

u_tri=[('A',2,2,'below left=5pt'),('B',10.5,3,'below right=5pt'),('C',4.5,10,'above=5pt')]
u_line=[('A',2,3,'below right=5pt'),('B',8,9,'below right=5pt'),('C',5,6,'below right=5pt'),('D',10,11,'below right=5pt')]
packet('grades-4-5','Grades 4--5','F22-45-v3',[
    ('Put D on each cross. For each position, split A, B, C, and D so their two regions meet, and mark a shared point.',board(u_tri,[(9.8,9),(5,5),(6.25,2.5),(1,6)])),
    ('Find every split whose regions meet. Explain how you know your list is complete.',board(u_line),2,[(repeated(u_line),0)]),
    ('Take turns placing A, B, C, and D in the box. Try to make an arrangement with no successful split. Decide whether your opponent must always be able to find one.',board(),2),
    ('A and D share a location. Find every split whose regions meet. Does a successful split always exist when two of four labels share a location? Explain.',board([('A, D',3,3,'below=6pt'),('B',10,4.5,'right=6pt'),('C',5.5,10,'above=6pt')]),2,[(repeated([('A, D',3,3,'below=6pt'),('B',10,4.5,'right=6pt'),('C',5.5,10,'above=6pt')]),0)]),
    ('Make two four-dot arrangements that each have exactly one successful split, with different successful splits. Make a third arrangement with more than one successful split. Explain how you checked the number of successful splits.',board(),2,[(board(),2),(board(),2)]),
    ('Can every arrangement of A, B, C, and D be split into two groups whose regions meet? Give an explanation that covers all arrangements, including dots in a straight line and labels at the same point.',board(),3),
    ('Can these three dots be split into two groups whose regions meet? Explain why your answer covers every split. Find the smallest number of dots that guarantees a successful split for every arrangement, and explain why fewer cannot give that guarantee.',board([('A',2,3,'below left=5pt'),('B',10.3,4,'below right=5pt'),('C',4.8,10.1,'above=5pt')]),2),
])
print('Wrote 8, 8, and 11 pages of LaTeX, including unassigned recording and construction boards.')
