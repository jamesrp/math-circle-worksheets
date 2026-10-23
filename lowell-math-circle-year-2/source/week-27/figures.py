"""Week 27 figures and canvas page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py and examples.py).

Coordinates are inches from the top-left corner of the paper, y down (tx and the other
primitives negate y). Each page is one overlay picture on the whole sheet that draws its
own header, rule, footer and page number (page_open and page_close). The preference
lists come from editable/src/math_checks.json, the data the kit builder also reads.
Problem files call the functions below by name in their `figure` sections; the rule,
prompt and example wording lives in the problem files.
"""
from pathlib import Path
import json

_HERE = Path(__file__).resolve().parent
for _data in (_HERE / 'editable' / 'src' / 'math_checks.json',   # in the repository
              _HERE.parent / 'src' / 'math_checks.json'):          # in the portable ZIP (problem-files/)
    if _data.exists():
        break
else:
    raise FileNotFoundError('Week 27 figures need src/math_checks.json beside the problem files')
DATA = json.loads(_data.read_text())


# ---------------------------------------------------------------- drawing primitives (build_packets.py)

def tx(x,y,s,w=7.25,size=14,lead=None):
 if lead is None:lead=size*1.24
 return rf'\node[anchor=north west,inner sep=0pt,text width={w}in,font=\fontsize{{{size}}}{{{lead}}}\selectfont] at ({x},{-y}) {{{s}}};'+'\n'
def ln(x,y,x2,y2,style='gray!40,line width=0.5pt'):
 return rf'\draw[{style}] ({x},{-y}) -- ({x2},{-y2});'+'\n'
def token(x,y,label,side,d=.79,size=20):
 style='circle' if side=='L' else 'rectangle'
 return rf'\node[draw,line width=0.8pt,{style},fill=white,minimum size={d}in,inner sep=0pt,font=\fontsize{{{size}}}{{{size+2}}}\selectfont] at ({x},{-y}) {{{label}}};'+'\n'
def box(x,y,w,h,style='gray!45,line width=.5pt'):
 return rf'\draw[{style}] ({x},{-y}) rectangle ({x+w},{-(y+h)});'+'\n'
def prob(n,y,text,size=15):return tx(.6,y,rf'\textbf{{Problem {n}:}} {text}',size=size)
def get(key):return DATA[key]['left'],DATA[key]['right']

# Large two-choice strips for the adult-read entry.
def kstrips(y,L,R):
 out=''
 for col,side,prof in [(0,'L',L),(1,'R',R)]:
  base=.6+col*3.85
  for row,(who,prefs) in enumerate(prof.items()):
   cy=y+.50+row*.86
   out+=token(base+.45,cy,who,side)
   out+=tx(base+.94,cy-.19,':',w=.2,size=20)
   out+=box(base+1.11,cy-.425,2.0,.85,'black,line width=.65pt')
   for j,val in enumerate(prefs):
    xx=base+1.60+j*.99
    out+=token(xx,cy,val,'R' if side=='L' else 'L')
 return out

def kboard(x,y,kind=None):
 # Every icon is 20.1 mm wide at 100 percent scale.
 out='';lx=x+.40;rx=x+2.30
 if kind:
  for i,j in enumerate(kind):out+=ln(lx,y+i*.87,rx,y+j*.87,'black,line width=1.2pt')
 for i,ch in enumerate('AB'):out+=token(lx,y+i*.87,ch,'L')
 for i,ch in enumerate('XY'):out+=token(rx,y+i*.87,ch,'R')
 return out

def kcase(y,L,R,kinds=((0,1),(1,0))):
 s=kstrips(y,L,R)
 for i,kind in enumerate(kinds):s+=kboard(.72+i*3.85,y+2.27,kind)
 return s

blankL={'A':['',''],'B':['','']};blankR={'X':['',''],'Y':['','']}

# Compact pencil-recording diagrams for the reading groups.
def strips(y,L,R,n=None,step=.62,d=.47,size=16):
 out='';n=n or len(L)
 # Rows are first-to-last left-to-right. Both sides use the same rank labels.
 for col,side,prof in [(0,'L',L),(1,'R',R)]:
  base=.65+col*3.85
  dx=.75 if n==3 else (.61 if n==4 else 1.05)
  for j in range(n):out+=tx(base+.92+j*dx-.025,y-.12,str(j+1),w=.18,size=10)
  for row,(who,prefs) in enumerate(prof.items()):
   cy=y+.35+row*step
   out+=token(base+.23,cy,who,side,d=d,size=size)
   out+=tx(base+.57,cy-.16,':',w=.18,size=size)
   out+=box(base+.70,cy-.27,(n-1)*dx+.54,.54,'black,line width=.55pt')
   for j,val in enumerate(prefs):out+=token(base+.97+j*dx,cy,val,'R' if side=='L' else 'L',d=d,size=size)
 return out

def board(x,y,left='ABC',right='XYZ',match=None,w=1.72,step=.54,d=.39,size=15):
 out='';lx=x+.20;rx=x+w
 if match:
  for i,a in enumerate(left):out+=ln(lx,y+i*step,rx,y+right.index(match[a])*step,'black,line width=.95pt')
 for i,a in enumerate(left):out+=token(lx,y+i*step,a,'L',d=d,size=size)
 for i,r in enumerate(right):out+=token(rx,y+i*step,r,'R',d=d,size=size)
 return out

def sixboards(y,left='ABC',right='XYZ',rowgap=2.35):
 return ''.join(board(.70+col*2.55,y+row*rowgap,left,right) for row in range(2) for col in range(3))
def lines(y,n,step=.55,x=.65,w=7.15):
 return ''.join(ln(x,y+i*step,x+w,y+i*step) for i in range(n))

BL={a:['','',''] for a in 'ABC'};BR={a:['','',''] for a in 'XYZ'}

def two_pair_case(y,key):  # grades 2-3 Problem 1: strips, then the straight and crossed pairings
 c=strips(y,*get(key),n=2,step=.68,d=.51,size=17)
 c+=board(1.05,y+1.9,'AB','XY',{'A':'X','B':'Y'},w=1.9,step=.68,d=.51,size=17)
 c+=board(4.88,y+1.9,'AB','XY',{'A':'Y','B':'X'},w=1.9,step=.68,d=.51,size=17)
 return c


# ---------------------------------------------------------------- worked examples

def blocking_example(intro,current,p_line,u_line,both_yes,not_both,caption):  # examples.py: K-1 and 2-3 page 1
    s=tx(.6,2.1,intro,size=14)
    for base,both in ((.65,True),(4.5,False)):
        s+=tx(base,2.9,current,w=3.25,size=12)
        x=base+.4; X=base+2.75
        s+=ln(x,3.65,X,3.65,'black,line width=1.2pt')+ln(x,4.5,X,4.5,'black,line width=1.2pt')
        s+=ln(x,3.65,X,4.5,'gray!65,dashed,line width=.8pt')
        for xx,yy,ch,side in ((x,3.65,'P','L'),(x,4.5,'Q','L'),(X,3.65,'V','R'),(X,4.5,'U','R')):
            s+=token(xx,yy,ch,side,d=.55,size=17)
        for row,who,choices,cur in ((0,'P','UV','V'),(1,'U','PQ' if both else 'QP','Q')):
            y=5.65+row*.8
            s+=token(base+.25,y,who,'L' if who=='P' else 'R',d=.5,size=16)
            s+=tx(base+.62,y-.16,':',w=.15,size=16)
            s+=box(base+.85,y-.33,2.1,.66,'black,line width=.65pt')
            for i,ch in enumerate(choices):
                t=token(base+1.36+i*.99,y,ch,'R' if who=='P' else 'L',d=.5,size=16)
                if ch==cur:t=t.replace('fill=white','fill=gray!22')
                s+=t
        s+=tx(base,7.25,p_line,w=3.35,size=13.5)
        s+=tx(base,7.8,u_line+('yes' if both else 'no'),w=3.35,size=13.5)
        s+=tx(base,8.6,both_yes if both else not_both,w=3.35,size=14)
    s+=tx(.6,9.35,caption,size=12.5)
    return s

def hold_release_example(sentence,before,after):  # grades 4-5 Problem 2: one hold/release step
 c=tx(.6,3.12,sentence,size=11.8,lead=14)
 c+=ln(1.15,3.74,2.35,3.74,'black,line width=.9pt')+token(1.15,3.74,'P','L',d=.30,size=12)+token(2.35,3.74,'U','R',d=.30,size=12)
 c+=tx(.65,4.02,before,w=3.20,size=11.5)
 c+=ln(5.10,3.74,6.30,3.74,'black,line width=.9pt')+token(5.10,3.74,'Q','L',d=.30,size=12)+token(6.30,3.74,'U','R',d=.30,size=12)
 c+=tx(4.55,4.02,after,w=3.25,size=11.5)
 c+=r'\draw[->,line width=.7pt] (3.43,-3.74) -- (4.26,-3.74);'+'\n'
 return c

def record_boxes(left,right):  # grades 4-5 Problem 2: one record box per asking side, labelled (card could 9)
 return (tx(.65,6.98,left,w=3.35,size=11.5)+box(.65,7.24,3.35,.75)
         +tx(4.5,6.98,right,w=3.35,size=11.5)+box(4.5,7.24,3.35,.75))

# Guidance-revision single hold/release step uses distinct example labels (build_packets.py).
_receiver_order = ['Q', 'P']
_old_hold, _new_asker = 'P', 'Q'
_kept = min((_old_hold, _new_asker), key=_receiver_order.index)
_released = next(x for x in (_old_hold, _new_asker) if x != _kept)
assert (_kept, _released) == ('Q', 'P')


# ---------------------------------------------------------------- page template (build_packets.py's page)

PRE=r'''\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.5in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage{tikz}
\usetikzlibrary{calc}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''


def page_preamble(week, topic, header, footer):
    return PRE


def page_open(page):
    return ('\\null\n\\begin{tikzpicture}[remember picture,overlay,x=1in,y=1in]\n\\begin{scope}[shift={(current page.north west)}]\n'
            + tx(.55,.35,rf'Week {page.week} / {page.topic} / {page.header}',size=11.5)
            + ln(.55,.66,7.95,.66,'black,line width=.55pt'))


def page_close(page):
    # The old builder ended every page, the last one too, with \newpage; the tools put one between pages.
    return (tx(.55,10.49,rf'Bellingham Math Circle / Week {page.week} / {page.footer}',size=10.2,w=6.8)
            + tx(7.60,10.49,str(page.number),size=10.2,w=.35)
            + '\\end{scope}\n\\end{tikzpicture}\n' + ('\\newpage\n' if page.number == page.count else ''))


# The shared rules and the grades 4-5 asking rules keep their own leading; other text and every
# prompt use the old default of 1.24 times the size.
LEAD={13.7:17,13:16,12.7:16}


def page_prompt(n, body, x, y, size):
    return prob(n,y,body,size)


def page_text(x, y, body, w, size):
    return tx(.6 if x is None else x,y,body,w=7.25 if w is None else w,size=size,lead=LEAD.get(size))
