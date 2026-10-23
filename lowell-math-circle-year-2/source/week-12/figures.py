"""Week 12 figures and canvas page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/make_packets.py).

Coordinates are millimetres from the top-left corner of the paper, y down, as the old
builder wrote them; pt() negates y for its y-up picture. Each page is one overlay picture
on the whole sheet that draws its own header, footer and page number (page_open and
page_close). Problem files call the functions below by name in their `figure` sections;
the rule, prompt and caption wording lives in the problem files.
"""
import math
from functools import lru_cache


# ---------------------------------------------------------------- codes, pairings and trees

@lru_cache(None)
def words(n):
    """Every legal code with n U's and n D's."""
    if n == 0: return ('',)
    return tuple('U'+p+'D'+q for i in range(n) for p in words(i) for q in words(n-1-i))

def pairs_from_word(w):
    stack=[]; pairs=[]
    for k,c in enumerate(w,1):
        if c=='U': stack.append(k)
        elif stack: pairs.append((stack.pop(),k))
        else: raise ValueError(w)
    if stack: raise ValueError(w)
    return sorted(pairs)

def tree_from_word(w):
    root=[]; stack=[root]
    for c in w:
        if c=='U':
            child=[]; stack[-1].append(child); stack.append(child)
        else:
            if len(stack)==1:raise ValueError(w)
            stack.pop()
    if len(stack)!=1:raise ValueError(w)
    return root


# ---------------------------------------------------------------- drawing primitives (the old Packet methods)

def f(v): return f'{v:.3f}'.rstrip('0').rstrip('.')
def pt(x,y): return f'({f(x)},{f(-y)})'

def text(x,y,text,width=180,font=13,leading=16,bold=False):
    weight=r'\bfseries' if bold else ''
    return (r'\node[anchor=north west,inner sep=0pt,align=left,text width='+f(width)+r'mm,font=\fontsize{'+f(font)+'}{'+f(leading)
            +r'}\selectfont'+weight+'] at '+pt(x,y)+' {'+text+'};\n')

def circle(x,y,n,r=27,fixed=(),physical=False):
    """n numbered dots on a circle; physical=True is a string mat with labels clear of the discs."""
    label_gap = 12.5 if physical else 4.3
    s=r'\draw[gray!55,line width=.45pt] '+pt(x,y)+' circle ('+f(r)+'mm);\n'
    coords={i:(x+r*math.cos(math.radians(90-(i-1)*360/n)),y-r*math.sin(math.radians(90-(i-1)*360/n))) for i in range(1,n+1)}
    for a,b in fixed:s+=r'\draw[line width=1.05pt] '+pt(*coords[a])+' -- '+pt(*coords[b])+';\n'
    for i,(xx,yy) in coords.items():
        s+=r'\fill '+pt(xx,yy)+' circle (1.45mm);\n'
        th=math.radians(90-(i-1)*360/n)
        s+=(r'\node[inner sep=0pt,font=\fontsize{9}{10}\selectfont] at '+pt(x+(r+label_gap+(1 if physical and i>=10 else 0))*math.cos(th),
            y-(r+label_gap+(1 if physical and i>=10 else 0))*math.sin(th))+' {'+str(i)+'};\n')
    return s

def row(x,y,n,spacing=11,pairs=(),max_h=22,labels=True,dot=1.2,label_gap=2.4):
    """n numbered dots in a row, with arcs above it for the given pairs."""
    s=r'\draw[gray!45,line width=.35pt] '+pt(x,y)+' -- '+pt(x+(n-1)*spacing,y)+';\n'
    for a,b in pairs:
        xa=x+(a-1)*spacing;xb=x+(b-1)*spacing
        h=max_h*(b-a)/(n-1)
        s+=r'\draw[line width=.9pt] '+pt(xa,y)+' .. controls '+pt(xa,y-h*1.333)+' and '+pt(xb,y-h*1.333)+' .. '+pt(xb,y)+';\n'
    for i in range(n):
        s+=r'\fill '+pt(x+i*spacing,y)+' circle ('+f(dot)+'mm);\n'
        if labels:s+=r'\node[anchor=north,inner sep=0pt,font=\fontsize{9}{11}\selectfont] at '+pt(x+i*spacing,y+label_gap)+' {'+str(i+1)+'};\n'
    return s

def grid(x,y,n,height=None,step=8,word=None,mark_steps=False):
    """A path grid n steps wide; the dark line is the starting level, the filled dot the start."""
    height=height or n//2
    s=''
    for k in range(n+1):s+=r'\draw[gray!35,line width=.25pt] '+pt(x+k*step,y)+' -- '+pt(x+k*step,y-height*step)+';\n'
    for h in range(height+1):s+=r'\draw[gray!35,line width=.25pt] '+pt(x,y-h*step)+' -- '+pt(x+n*step,y-h*step)+';\n'
    s+=r'\draw[line width=.8pt] '+pt(x,y)+' -- '+pt(x+n*step,y)+';\n'
    if word:
        h=0;coords=[pt(x,y)]
        for k,c in enumerate(word,1):
            h += 1 if c=='U' else -1
            coords.append(pt(x+k*step,y-h*step))
        s+=r'\draw[line width=1.15pt,line join=round] '+' -- '.join(coords)+';\n'
        if mark_steps:
            h=0
            for k,c in enumerate(word):
                nh=h+(1 if c=='U' else -1)
                s+=text(x+(k+.5)*step-1.2,y-(h+nh)*step/2-5,c,width=5,font=9,leading=10)
                h=nh
    s+=r'\fill '+pt(x,y)+' circle (1.3mm);\n'
    s+=r'\draw[fill=white,line width=.8pt] '+pt(x+n*step,y)+' circle (1.3mm);\n'
    return s

def boxes(x,y,n,w=7,h=8):
    return ''.join(r'\draw[gray!65,line width=.45pt] '+pt(x+i*w,y)+' rectangle '+pt(x+(i+1)*w,y+h)+';\n' for i in range(n))

def code(x,y,w,font=15): return text(x,y,r'\texttt{'+w+'}',width=82,font=font,leading=font+3)

def root(x,y):
    return r'\fill '+pt(x,y)+' circle (1.5mm);\n'

def tree_positions(x,y,w,width=57,depth_step=11):
    t=tree_from_word(w); nodes=[]; edges=[]; leaf=0
    def rec(t,depth):
        nonlocal leaf
        idx=len(nodes);nodes.append(None)
        children=[]
        for ch in t:
            k=rec(ch,depth+1);children.append(k);edges.append((idx,k))
        if children:xx=sum(nodes[k][0] for k in children)/len(children)
        else:xx=leaf;leaf+=1
        nodes[idx]=(xx,depth)
        return idx
    rec(t,0)
    rng=max(1,leaf-1)
    return [(x+(xx-(leaf-1)/2)*width/rng,y+d*depth_step) for xx,d in nodes], edges

def tree(x,y,w,width=57,depth_step=11):
    """The ordered tree with code w, root (filled) at (x, y)."""
    pos,edges=tree_positions(x,y,w,width,depth_step)
    s=''.join(r'\draw[line width=.9pt] '+pt(*pos[a])+' -- '+pt(*pos[b])+';\n' for a,b in edges)
    for k,(xx,yy) in enumerate(pos):
        s+=(r'\fill ' if k==0 else r'\draw[fill=white,line width=.8pt] ')+pt(xx,yy)+' circle (1.5mm);\n'
    return s

def walk_example(x,y):
    # Two-edge ordered fork. U is away from the root, not upward on this drawing.
    s=tree(x,y,'UDUD',width=42,depth_step=24)
    for childx,up,down in [(x-21,1,2),(x+21,3,4)]:
        a=(x,y);b=(childx,y+24)
        dx=b[0]-a[0];dy=b[1]-a[1];length=math.hypot(dx,dy)
        ux,uy=dx/length,dy/length;nx,ny=-uy,ux
        for sign,num,letter,forward in [(1,up,'U',True),(-1,down,'D',False)]:
            start=(a[0]+ux*4+nx*3*sign,a[1]+uy*4+ny*3*sign)
            end=(b[0]-ux*4+nx*3*sign,b[1]-uy*4+ny*3*sign)
            if not forward:start,end=end,start
            s+=r'\draw[-{Stealth[length=1.5mm,width=1.1mm]},line width=.55pt] '+pt(*start)+' -- '+pt(*end)+';\n'
            lx=(a[0]+b[0])/2+nx*8.1*sign;ly=(a[1]+b[1])/2+ny*8.1*sign
            s+=r'\node[inner sep=.5pt,fill=white,font=\fontsize{9}{10}\selectfont] at '+pt(lx,ly)+' {'+str(num)+' '+letter+'};\n'
    s+=text(x+4,y-3,'root',width=25,font=9,leading=10)
    return s


# ---------------------------------------------------------------- page template (the old Packet.page and save)

PREAMBLE = r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=0in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\pdfmapfile{+cm.map}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\renewcommand{\familydefault}{\sfdefault}
\begin{document}
'''


def page_preamble(week, topic, header, footer):
    return PREAMBLE


def page_open(page):
    return (r'\begin{tikzpicture}[remember picture,overlay,x=1mm,y=1mm]'+'\n'+r'\begin{scope}[shift={(current page.north west)}]'+'\n'
            + text(18,15.5,f'Week {page.week} / {page.topic} / {page.header}',font=11.5,leading=14,bold=True)
            + text(18,266.5,f'Bellingham Math Circle / Week {page.week} / {page.footer}',font=9,leading=11)
            + r'\node[anchor=north east,inner sep=0pt,font=\fontsize{9}{11}\selectfont] at '+pt(198,266.5)+' {'+str(page.number)+'};\n')


def page_close(page):
    return '\\end{scope}\n\\end{tikzpicture}\n\\null\n'


def page_prompt(n, body, x, y, size):
    """The old problem(): label and statement in one node at the left margin, 30 mm down unless placed."""
    return text(18,30 if y is None else y,r'\textbf{Problem '+str(n)+':} '+body,font=size,leading=size+3.5)


# Line spacing of the old builder's shared rules: 12.5 pt on 15.5 (K-1), 12.3 pt on 15.5 (grades 2-3
# page 2 and grades 4-5). Grades 2-3 page 1 set 15 pt: its text starts with that \fontsize and ends
# with \par, so the paragraph ends while the 15 pt spacing holds.
LEADING = {12.3: 15.5}


def page_text(x, y, body, w, size):
    return text(18 if x is None else x,y,body,width=w or 180,font=size,leading=LEADING.get(size,size+3))


# ---------------------------------------------------------------- K-1 figures, by problem file
# Large circles (physical=True) are string mats; small circles are pencil records.
# 20 mm endpoint discs leave 12 mm or more between neighbors on the 4/6 mats,
# 10.6 mm on the 8-dot mats, and 6.6 mm on the 10-dot mat.

def k1_four_dot_example(caption):  # 00: the two pairings of four dots
    return (text(18,51,caption,font=12.5,leading=15.5)
            + circle(58,84,4,r=20,fixed=[(1,2),(3,4)]) + circle(159,84,4,r=20,fixed=[(1,4),(2,3)]))

def k1_six_dot_mat_and_records():  # 01
    s=circle(61,188,6,r=32,physical=True)
    for j in range(6):s+=circle([131,177][j%2],[154,198,242][j//2],6,r=15)
    return s

def k1_mat_and_records(n,count=6,fixed=(),mat_y=107,mat_r=40):
    """A string mat and a 3-across block of pencil records (02, 03, 04)."""
    s=circle(108,mat_y,n,r=mat_r,physical=True)
    for j in range(count):s+=circle([41,108,175][j%3],[190,240][j//3],n,r=18.5,fixed=[fixed[j]] if fixed else ())
    return s

def k1_parity_circles():  # 05: a ten-dot mat, then 3 to 7 dots
    s=circle(108,104,10,r=43,physical=True)
    for j,n in enumerate([3,4,5,6,7]):s+=circle([41,108,175][j%3],[190,240][j//3],n,r=18.5)
    return s

def k1_neighbor_records():  # 06: an eight-dot mat and four records
    s=circle(108,107,8,r=40,physical=True)
    for j in range(4):s+=circle([61,155][j%2],[190,240][j//2],8,r=18.5)
    return s


# ---------------------------------------------------------------- grades 2-3 figures
# The large first row is an object mat (24 mm spacing, about 60 mm clear height).

def ten_dot_example(caption):  # 00
    return text(18,50,caption,font=12,leading=15)+row(26,77,10,spacing=18,pairs=pairs_from_word('UUDDUUDUDD'),max_h=22)

def six_dot_row_mat_and_records():  # 07
    s=row(48,167,6,spacing=24,max_h=60,dot=1.6,label_gap=12.5)
    for j in range(6):s+=row([25,123][j%2],[205,230,255][j//2],6,spacing=12,max_h=19)
    return s

def code_example(caption):  # 08: one pairing, its letters and its path
    example='UDUUDDUD'
    s=text(18,56,caption,font=12,leading=15)+row(25,91,8,spacing=10.2,pairs=pairs_from_word(example),max_h=23)
    for j,c in enumerate(example):s+=text(23.5+j*10.2,102,c,width=6,font=12,leading=14)
    return s+grid(126,103,8,height=3,step=8,word=example,mark_steps=True)

def pairings_to_paths():  # 08
    s=''
    for j,w in enumerate(['UUUDDD','UUDDUD','UDUDUD']):
        y=[167,207,247][j]
        s+=row(25,y,6,spacing=12,pairs=pairs_from_word(w),max_h=23)+boxes(34,y+9,6,w=7,h=7)+grid(126,y+3,6,height=3,step=8)
    return s

def paths_to_pairings():  # 09
    s=''
    for j,w in enumerate(['UUDUDD','UDUUDD','UUDDUUDD','UUUDUDDD']):
        y=[91,143,195,247][j]
        s+=grid(23,y,len(w),height=len(w)//2,step=7.5,word=w)+row(119,y,len(w),spacing=10.3,max_h=31)
    return s

def six_path_grids():  # 10
    return ''.join(grid([27,126][j%2],[105,167,229][j//2],6,height=3,step=10) for j in range(6))

def pairing_codes():  # 11
    s=''
    for j,w in enumerate(['UUUDDUDD','UDDUUDUD','UUDUDUDD','UUUUDDUD']):
        y=[74,122,170,218][j]
        s+=code(21,y,w,font=15)+row(109,y+27,8,spacing=11.4,max_h=28)
    return s

def eight_dot_rows():  # 12: sixteen rows for the fourteen pairings
    return ''.join(row([23,121][j%2],[70,96,122,148,174,200,226,252][j//2],8,spacing=10.5,max_h=19,dot=1.05) for j in range(16))


# ---------------------------------------------------------------- grades 4-5 figures

def five_edge_example(caption):  # 00
    return (text(18,74,caption,width=83,font=12.5,leading=15)+tree(133,78,'UUDUDDUUDD',width=60,depth_step=15)
            + text(146,75,'root',width=35,font=9,leading=11))

def roots(xs,ys):
    """A filled root dot to start each drawing (13, 17)."""
    return ''.join(root(xs[j%len(xs)],ys[j//len(xs)]) for j in range(len(xs)*len(ys)))

def walk_code_example(caption,order_note,path_note):  # 14: the walk on a two-edge fork, and its path
    return (text(18,57,caption,font=12,leading=15)+walk_example(52,72)
            + (text(18,111,order_note,width=89,font=10,leading=12) if order_note else '')
            + text(112,62,path_note,width=83,font=10,leading=12)
            + grid(124,103,4,height=2,step=12,word='UDUD',mark_steps=True)
            + text(112,111,r'Walk code: \texttt{UDUD}',width=85,font=12,leading=15))

def trees_to_codes():  # 14
    s=''
    for j,w in enumerate(['UUUUDDDD','UDUDUDUD','UUDUDDUD','UDUUUDDD']):
        cx=[61,155][j%2]; y=[155,217][j//2]
        s+=tree(cx,y,w,width=56,depth_step=10)+boxes(cx-28,[200,254][j//2],8,w=7,h=8)
    return s

def codes_to_trees():  # 15
    s=''
    for j,w in enumerate(['UUDDUD','UDUUDD','UUDUDUDD','UUUDDUDD']):
        cx=[61,155][j%2]; y=[60,158][j//2]
        s+=code(cx-29,y,w,font=16)+root(cx,y+20)
    return s

def tree_codes():  # 16
    return ''.join(code([30,127][j%2],[84,110,136][j//2],w,font=17)
                   for j,w in enumerate(['UUUUDDDD','UUDDDUUD','UDUDUUDD','UUDUDUDU','UUUDUDDD','DUUUDDUD']))
