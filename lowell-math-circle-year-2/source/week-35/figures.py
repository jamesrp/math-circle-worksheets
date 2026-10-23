"""Week 35 figures and canvas page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py).

Coordinates are centimetres from the top-left corner of the page body, y down, inside a
scope shifted 1.5 cm from the paper's corner. Each page is one overlay picture that draws
its own header, footer and page number (page_open and page_close). The old builder wrote
every element on its own line, joined by newlines with none after the last; so every
function here returns its lines each starting with a newline. Problem files call the
functions below by name in their `figure` sections; the rule, prompt and example wording
lives in the problem files.
"""


def text(x,y,w,t,s=15):
 return '\n'+r'\node[anchor=north west,inner sep=0,align=left,text width='+str(w)+r'cm,font=\sffamily\fontsize{'+str(s)+'}{'+str(s*1.25)+r'}\selectfont] at ('+str(x)+','+str(y)+') {'+t+'};'


def lines(*items):
 return ''.join('\n'+i for i in items)


# ---------------------------------------------------------------- drawing (build_packets.py)

def motif(x,y,s=.65,reflect=False,angle=0):
 return lines(f'\\begin{{scope}}[shift={{({x},{y})}},rotate={angle},xscale={s},yscale={-s if reflect else s}]',
  r'\draw[line width=.7pt,fill=gray!15] (-1.3,-1.1) -- (1.3,-1.1) -- (1.3,-.4) -- (.8,-.4) -- (.8,-.65) -- (-.5,-.65) -- (-.5,0) -- (.6,0) -- (.6,.45) -- (-.5,.45) -- (-.5,1.1) -- (-1.3,1.1) -- cycle;',
  r'\draw[-{Stealth},line width=.65pt] (-.25,-.86) -- (.55,-.86);\end{scope}')

def strip(y,marks=None,h=6.0,vertical=False):
 s=lines(f'\\draw[gray!50,line width=.6pt] (.35,{y-h/2}) rectangle (18,{y+h/2});',
         f'\\draw[dashed,line width=.6pt] (.35,{y}) -- (18,{y});')
 for x,sign in [(0,-1),(18.4,1)]:s+=lines(f'\\draw[-{{Stealth}},line width=.9pt] ({x-sign*.6},{y}) -- ({x},{y});')
 for i in range(6):
  x=1.7+3*i
  s+=lines(f'\\draw[gray!45] ({x},{y-.12}) -- ({x},{y+.12});')
 if vertical:s+=lines(f'\\draw[densely dotted] (9.15,{y-h/2}) -- (9.15,{y+h/2});')
 if marks:
  for i,row,ref,ang in marks:s+=motif(1.7+3*i,y+row,1,ref,ang)
 return s

def glide_demo(start,flip,slide):
 # Three equally scaled panels show the same labelled motif under the two actions.
 s=lines(r'\begin{scope}[shift={(0,-2.5)}]')
 for x in [2.6,9.2,15.8]:s+=lines(f'\\draw[dashed,gray] ({x-2.1},4.9) -- ({x+2.1},4.9);')
 s+=motif(2.6,3.6,.68)+motif(9.2,6.2,.68,True)+motif(16.8,6.2,.68,True)
 for x,y,label in [(2.6,3.6,'A'),(9.2,6.2,'A'),(16.8,6.2,'A')]:s+=text(x-1.55,y-.3,.7,label,12)
 s+=lines(r'\draw[-{Stealth},line width=.9pt] (4.8,4.9) -- (6.8,4.9);',r'\draw[-{Stealth},line width=.9pt] (11.5,4.9) -- (13.4,4.9);')
 s+=text(.7,7.4,4.5,start,12)+text(7.1,7.4,5,flip,12)+text(13.7,7.4,4.7,slide,12)
 s+=lines(r'\draw[-{Stealth},line width=.8pt] (14.7,7.1) -- (15.7,7.1);',r'\end{scope}')
 return s


# ---------------------------------------------------------------- page template (build_packets.py's Packet)

PRE=r'''\RequirePackage{fix-cm}
\documentclass[12pt,letterpaper]{article}
\usepackage[margin=.5in]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,patterns}
\pdfmapfile{+cm.map}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
'''


def page_preamble(week, topic, header, footer):
    return PRE


def page_open(page):
    return (r'\null\begin{tikzpicture}[remember picture,overlay]'
            + lines(r'\begin{scope}[shift={(current page.north west)},x=1cm,y=-1cm]',r'\begin{scope}[shift={(1.5,1.5)}]')
            + text(0,-.5,18.5,f'Week {page.week} / {page.topic} / {page.header}',11)
            + text(0,24.7,17,f'Bellingham Math Circle / Week {page.week} / {page.footer}',10)
            + text(18,24.7,.5,str(page.number),10))


def page_close(page):
    return r'\end{scope}\end{scope}\end{tikzpicture}'+'\n'


def page_prompt(n, body, x, y, size):
    """The old problem(): 17 pt for K-1 and 15 pt otherwise (week.toml), at y = .5 unless placed."""
    return text(0,.5 if y is None else y,18.4,r'\textbf{Problem '+str(n)+':} '+body,size)


def page_text(x, y, body, w, size):
    return text(0 if x is None else x,.3 if y is None else y,18.4 if w is None else w,body,size)
