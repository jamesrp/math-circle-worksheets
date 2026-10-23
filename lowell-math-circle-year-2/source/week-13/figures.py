"""Week 13 boards and page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py).

The old builder wrote flowing LaTeX, one \\newpage per page, with a fancyhdr header and
footer. This week keeps that document through the canvas hooks below: page_prompt
writes the old prob(), page_text the old opening rules (each followed by a 0.1 in
space), and each problem's figure the old page() body: a space, the boards with
0.32 in between, then any tail. page_close ends a page as page() did, so the rebuilt
LaTeX is the old builder's byte for byte. Problem files call the figure functions
by name; the wording lives in the problem files.
"""

# ---------------------------------------------------------------- boards
G={}
def graph(name, pos, edges):
    G[name]={'pos':pos,'edges':[tuple(e.split('-')) for e in edges.split()]}; return name

graph('diamond', {'s':(0,0),'A':(7,2.2),'B':(7,-2.2),'t':(14,0)}, 's-A s-B A-t B-t')
graph('greedy', G['diamond']['pos'], 's-A s-B A-B A-t B-t')
graph('bowtie', {'s':(0,0),'A':(3.5,2.2),'B':(3.5,-2.2),'C':(7,0),'D':(10.5,2.2),'E':(10.5,-2.2),'t':(14,0)}, 's-A s-B A-C B-C C-D C-E D-t E-t')
graph('doubletrap', G['bowtie']['pos'], 's-A s-B A-B A-C B-C C-D C-E D-E D-t E-t')
graph('funnel', {'s':(0,0),'A':(3,2.2),'B':(3,-2.2),'C':(6,0),'D':(9,0),'t':(14,0)}, 's-A s-B A-C B-C C-D D-t')
graph('three_two', {'s':(0,0),'A':(3.5,2.3),'B':(3.5,0),'C':(3.5,-2.3),'D':(7,0),'E':(10.5,2.3),'F':(10.5,-2.3),'t':(14,0)}, 's-A s-B s-C A-D B-D C-D D-E D-F E-t F-t')
graph('three', {'s':(0,0),'A':(7,2.65),'B':(7,0),'C':(7,-2.65),'t':(14,0)}, 's-A s-B s-C A-t B-t C-t')
graph('greedy_three', G['three']['pos'], 's-A s-B s-C A-B A-t B-t C-t')
pos={'s':(0,0),'A':(2.5,2.4),'B':(2.5,0),'C':(2.5,-2.4),'D':(5,0),'E':(7.5,1.9),'F':(7.5,-1.9),'G':(10,0),'H':(12.5,2.4),'I':(12.5,0),'J':(12.5,-2.4),'t':(15,0)}
graph('bottleneck', pos, 's-A s-B s-C A-D B-D C-D D-E D-F E-G F-G G-H G-I G-J H-t I-t J-t')
graph('endpoint_two', {k:v for k,v in pos.items() if k!='B'}, 's-A s-C A-D C-D D-E D-F E-G F-G G-H G-I G-J H-t I-t J-t')
graph('backward', {'s':(0,0),'A':(4,2.4),'B':(4,-2.4),'C':(10,2.4),'D':(10,-2.4),'t':(14,0)}, 's-A s-B A-C B-D C-t D-t B-A C-D C-B')
graph('staircase', {'s':(0,0),'A':(4,2.5),'B':(4,0),'C':(4,-2.5),'D':(10,2.5),'E':(10,0),'F':(10,-2.5),'t':(14,0)}, 's-A s-B s-C A-D B-D B-E C-E C-F D-t E-t F-t')

def reserved(*routes):
    return set((a,b) for r in routes for a,b in zip(r.split(),r.split()[1:]))
R1=reserved('s A B t');RDOUBLE=reserved('s A B C D E t')       # the reserved (thick) routes on the rerouting boards
RSTAIR=reserved('s B D t','s C E t')
RBOT=reserved('s A D E G H t','s C D F G J t')


def diagram(name,letters=True,marks=None, yscale=1, compact=False):
    g=G[name];marks=marks or set();xscale=1.02 if name in ['bottleneck','endpoint_two'] else 1
    if compact: xscale=0.47; yscale=0.65
    head='Stealth[length=2.1mm,width=1.4mm]' if compact else 'Stealth[length=3.1mm,width=2.2mm]'
    lines=[] if compact else [r'\begin{center}']
    lines.append(r'\begin{tikzpicture}[x='+str(xscale)+'cm,y='+str(yscale)+'cm,>={'+head+r'},line cap=round,line join=round]')
    for n,(x,y) in g['pos'].items():lines.append(f'\\coordinate ({n}) at ({x},{y});')
    for a,b in g['edges']:
        if (a,b) in marks:lines.append(f'\\draw[line width=4.5pt,black!40] ({a}) -- ({b});')
        width,shorten=('0.8','2') if compact else ('0.95','3')
        lines.append(f'\\draw[->,line width={width}pt,shorten >={shorten}pt,shorten <={shorten}pt] ({a}) -- ({b});')
    for n in g['pos']:
        radius=1.9 if compact else 2.6
        lines.append(f'\\fill ({n}) circle ({radius}pt);')
        if n in ['s','t']:
            label='Start' if n=='s' else 'Finish'
            gap=2 if compact else 7
            where=f'left={gap}pt' if n=='s' else f'right={gap}pt'
            fs,lead=(8,9) if compact else (12,14)
            lines.append(f'\\node[{where},font=\\fontsize{{{fs}}}{{{lead}}}\\selectfont] at ({n}) {{{label}}};')
        elif letters:
            # Shift labels away from the vertical edges in the two diamond boards.
            where='above=6pt'
            if g['pos'][n][1]<0:where='below=6pt'
            if name=='greedy_three' and n=='B':where='below=6pt'
            lines.append(f'\\node[{where},fill=white,inner sep=1.4pt,font=\\fontsize{{11}}{{12}}\\selectfont] at ({n}) {{{n}}};')
    lines.append(r'\end{tikzpicture}')
    if not compact: lines.append(r'\end{center}')
    return '\n'.join(lines)


K1_RECORDING_COPIES=10   # K-1 P5: more copies than its 8 answers


def recording_grid(name,copies=8):
    row=r'\noindent\begin{minipage}{0.48\linewidth}\centering'+'\n'+diagram(name,False,compact=True)+r'\end{minipage}\hfill\begin{minipage}{0.48\linewidth}\centering'+'\n'+diagram(name,False,compact=True)+r'\end{minipage}'
    return ('\n'+r'\par\vspace{0.15in}'+'\n').join([row]*(copies//2))


def cancellation_example():
    return r'''\begin{center}\begin{tikzpicture}[x=1in,y=1in,>=Stealth]
\node[font=\small] at (.7,.55) {Reserved arrow};
\node[font=\small] at (2.7,.55) {Change-step};
\node[font=\small] at (4.7,.55) {After cancellation};
\draw[black!40,line width=4pt] (.15,0)--(1.25,0);
\draw[->] (.15,0)--(1.25,0);
\draw[->,dashed] (3.25,0)--(2.15,0);
\draw[->] (4.15,0)--(5.25,0);
\foreach \x/\t in {.15/X,1.25/Y,2.15/X,3.25/Y,4.15/X,5.25/Y}{\fill (\x,0) circle(1.5pt);\node[below=4pt,font=\small] at (\x,0){\t};}
\node[font=\small] at (2.7,.22) {walk Y to X};
\node[font=\small] at (4.7,-.48) {X to Y is now unused};
\end{tikzpicture}\end{center}
'''


def boards(*ds,tail='',space='0.26in'):
    """The old page() after its text: a space, the boards 0.32 in apart, then the tail."""
    return '\n\\vspace{'+space+'}\n'+('\n\\vspace{0.32in}\n'.join(ds))+'\n'+tail


# ---------------------------------------------------------------- page template

PRE=r'''\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.65in,top=0.75in,bottom=0.65in,headheight=15pt,headsep=17pt,footskip=24pt]{geometry}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\pdfmapfile{+cm.map}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{fancyhdr}
\renewcommand{\familydefault}{\sfdefault}
\setlength{\parindent}{0pt}
\setlength{\parskip}{7pt}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancyhead[L]{\fontsize{11}{13}\selectfont Week WEEK / TOPIC / LEVEL}
\fancyfoot[L]{\fontsize{9}{11}\selectfont Bellingham Math Circle / Week WEEK / PACKET}
\fancyfoot[R]{\fontsize{9}{11}\selectfont\thepage}
\begin{document}
\fontsize{FS}{LEAD}\selectfont
'''
SIZES={'K--1':(14,18)}      # type size and leading; other bands 12 on 16


def page_preamble(week, topic, header, footer):
    fs,lead=SIZES.get(header,(12,16))
    return (PRE.replace('WEEK',str(week)).replace('TOPIC',topic).replace('LEVEL',header).replace('PACKET',footer)
            .replace('FS',str(fs)).replace('LEAD',str(lead)))


PAGE_OPEN=''
PAGE_CLOSE='\n\n'


def page_prompt(n, body, x, y, size):
    """The old prob()."""
    return r'\par\textbf{Problem '+str(n)+r':} '+body+'\n'


def page_text(x, y, body, w, size):
    """Opening rules or a definition, then the old 0.1 in space."""
    return body+'\n\\vspace{0.1in}\n'


# ---------------------------------------------------------------- figures, one per problem page

def k1_fit_routes(): return boards(diagram('greedy',False),diagram('bowtie',False),space='0.05in')     # K-1 P1
def fit_and_close_23(): return boards(diagram('bowtie'),diagram('greedy'),space='0.05in')           # grades 2-3 P1
def reroute_boards(space='0.26in'): return boards(diagram('greedy',marks=R1),diagram('doubletrap',marks=RDOUBLE),space=space)  # 2-3 P5, 4-5 P1
def clean_copies(): return boards(diagram('greedy'),diagram('doubletrap'),space='0.05in')           # the rerouting boards without reservations
def k1_fewest_markers(): return boards(diagram('diamond',False),diagram('funnel',False))            # K-1 P2
def k1_routes_and_markers(): return boards(diagram('three_two',False),diagram('three',False))      # K-1 P3
def bottleneck_23(): return boards(diagram('bottleneck',yscale=1.15),tail=r'\vspace{0.45in}')      # grades 2-3 P2
def bottleneck_45(): return boards(diagram('bottleneck',yscale=1.2))                              # grades 4-5 P2
def k1_one_closure(): return boards(diagram('three_two',False),diagram('greedy',False))            # K-1 P4
def k1_closure_pairs(): return boards(diagram('bowtie',False),tail=r'\vspace{0.08in}'+'\n'+recording_grid('bowtie',K1_RECORDING_COPIES),space='0.08in')  # K-1 P5
def closure_pairs_23(): return boards(diagram('bowtie'),tail=r'\vspace{0.3in}')                   # grades 2-3 P3
def add_arrow(): return boards(diagram('bottleneck'),diagram('endpoint_two'))                     # grades 2-3 P4
def two_splits(): return boards(diagram('backward'),diagram('backward'))                          # grades 4-5 P3
def route_two_cut(): return boards(diagram('backward',yscale=1.2))                                # grades 4-5 P4
def staircase_boards(): return boards(diagram('staircase',marks=RSTAIR,yscale=.84),diagram('staircase',yscale=.84),space='0.02in')  # 4-5 P5
def reachable_board(): return boards(diagram('bottleneck',marks=RBOT),tail=r'\vspace{0.75in}'+'\n')  # grades 4-5 P6, with P7 below
def game_boards(letters=True): return boards(diagram('diamond',letters),diagram('greedy',letters))  # K-1 and 2-3 P6
