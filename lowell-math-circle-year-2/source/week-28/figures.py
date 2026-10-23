"""Week 28 figures and canvas page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py).

Coordinates are centimetres with y pointing down, measured from a point 1.4 cm in
and 1.15 cm down from the page's top-left corner, as the old builder drew them.
Problem files call the figure functions below by name; the rule and prompt
wording lives in the problem files. The header and footer are drawn inside each
page's picture by page_open(page) and page_close(page), so the rebuilt LaTeX is
the old builder's byte for byte.
"""
import math


def coord(x,y): return f'({x:.4f},{y:.4f})'
def text(x,y,s,size=13,width=18.7,bold=False,align='left'):
    f=r'\bfseries ' if bold else ''
    return rf'\node[anchor=north west,inner sep=0pt,text width={width}cm,align={align},font=\fontsize{{{size}}}{{{size*1.3}}}\selectfont {f}] at {coord(x,y)} {{{s}}};'+'\n'
def point(cx,cy,r,a): return cx+r*math.sin(math.radians(a)),cy-r*math.cos(math.radians(a))
def line(x1,y1,x2,y2,opts='black!32,line width=.35pt'):
    return rf'\draw[{opts}] {coord(x1,y1)} -- {coord(x2,y2)};'+'\n'
def node(x,y,s,size=11,bold=False):
    return rf'\node[inner sep=1pt,fill=white,font=\fontsize{{{size}}}{{{size+2}}}\selectfont '+(r'\bfseries' if bold else '')+rf'] at {coord(x,y)} {{{s}}};'+'\n'
def disk(cx,cy,r=2,sectors=None,rays=None,nums=False,labels=None,degrees=False,shade=False,tag=None,ticks=False,sector_labels=None):
    o=''
    if sectors is not None:
        rays=[0]
        for a in sectors[:-1]: rays.append(rays[-1]+a)
    if rays is None: rays=[0,90,180,270]
    if shade and sectors:
        a=0
        for j,span in enumerate(sectors):
            if j%2==0:
                points=[(cx,cy)]+[point(cx,cy,r,a+span*k/60) for k in range(61)]
                o+=r'\fill[black!14] '+' -- '.join(coord(*p) for p in points)+r' -- cycle;'+'\n'
            a+=span
    o+=rf'\draw[black,line width=.65pt] {coord(cx,cy)} circle[radius={r}cm];'+'\n'
    if ticks:
        for a in range(0,360,30):
            x1,y1=point(cx,cy,r+.02,a);x2,y2=point(cx,cy,r+.12,a)
            o+=line(x1,y1,x2,y2,'black!50,line width=.4pt')
    for j,a in enumerate(rays):
        x,y=point(cx,cy,r,a); o+=line(cx,cy,x,y,'black,line width=.65pt')
        if nums:
            x,y=point(cx,cy,r+.22,a);o+=node(x,y,str(j+1),max(9,min(12,r*5.8)))
        if labels and j<len(labels) and labels[j]:
            x,y=point(cx,cy,r*.66,a);o+=node(x,y,labels[j],max(12,min(18,r*9)),True)
    o+=rf'\fill {coord(cx,cy)} circle[radius=.045cm];'+'\n'
    if degrees and sectors:
        a=0
        for span in sectors:
            x,y=point(cx,cy,r*.66,a+span/2)
            o+=node(x,y,rf'${span}^\circ$',10.5 if r<2 else 12)
            a+=span
    if sector_labels and sectors:
        a=0
        for span,label in zip(sectors,sector_labels):
            x,y=point(cx,cy,r*.68,a+span/2)
            o+=node(x,y,label,12,True)
            a+=span
    if tag:o+=node(cx-r-.2,cy-r-.38,tag,13,True)
    return o

def wedge(cx,cy,r,a,label,degrees=False):
    points=[(cx,cy)]+[point(cx,cy,r,-a/2+a*k/60) for k in range(61)]
    o=r'\draw[line width=.65pt,fill=black!4] '+' -- '.join(coord(*p) for p in points)+r' -- cycle;'+'\n'
    o+=node(cx,cy-r*.62,label,13,True)
    if degrees:o+=node(cx,cy-r*.31,rf'${a}^\circ$',10)
    return o

def half(cx,cy,r=2.2):
    ps=[point(cx,cy,r,-90+i*3) for i in range(61)]
    return r'\draw[line width=.65pt] '+' -- '.join(coord(*p) for p in ps)+r' -- cycle;'+'\n'

def record_lines(ys,cols=1):
    out=''
    for y in ys:
        for c in range(cols):
            w=18.7/cols
            out+=line(c*w+.1,y,(c+1)*w-.5,y)
    return out


# ---------------------------------------------------------------- page template
# The old builder's page: Latin Modern, one overlay picture per page holding the
# header, the problems and the footer with its page number.

def page_preamble(week, topic, header, footer):
    return r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=1.4cm]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
'''


def page_open(page):
    """The old builder's page(): the overlay picture, the header and its rule."""
    return r'\null\begin{tikzpicture}[remember picture,overlay,x=1cm,y=-1cm]'+'\n'+r'\coordinate (O) at ([xshift=1.4cm,yshift=-1.15cm]current page.north west);\begin{scope}[shift={(O)}]'+'\n'+text(0,0,f'Week {page.week} / {page.topic} / {page.header}',11.5,bold=True)+line(0,.59,18.7,.59)


def page_close(page):
    """The footer id and page number; the composer adds the \\newpage between pages."""
    return text(0,25.2,f'Bellingham Math Circle / Week {page.week} / {page.footer}',9.3,width=16)+text(17.4,25.2,str(page.number),9.3,width=1.3,align='right')+r'\end{scope}\end{tikzpicture}'


def page_prompt(n, body, x, y, size):
    """The old builder's problem(): the label and statement in one text node at the left margin."""
    return text(0,1.1 if y is None else y,rf'\textbf{{Problem {n}:}} '+body,size or 14)


def page_text(x, y, body, w, size):
    return text(x or 0,y or 0,body,size or 13,width=w or 18.7)


# ---------------------------------------------------------------- figures
# Each returns the drawing that followed a problem's statement on its page.

ANGLES=[[90,90,90,90],[45,90,90,135],[60,120,120,60],[30,60,150,120]]   # the four-ray disks A-D
CHECKS=[[45,90,90,135],[30,30,60,60,90,90],[30,30,30,60,90,120],[45]*8]   # grades 4-5 alternating-angle checks
ROUTE_LABELS=['MMMV','MMVM','MVMM','VMMM','MVVV','VMVV','VVMV','VVVM']    # K-1 route states A-H


def k1_four_ways():  # K-1, four blank right-angle disks
    b=''
    for y in (9.0,18.0):
        for x in (4.5,14.0): b+=disk(x,y,2.55,nums=True)
    return b

def k1_which_folds():  # K-1, six labelled disks A-F
    b=''
    assignments=['MMMV','MMMM','MVVV','MMVV','MMVM','MVMV']
    for i,labs in enumerate(assignments): b+=disk((4.5,14)[i%2],(6.2,13.4,20.6)[i//2],2.05,nums=True,labels=labs,tag='ABCDEF'[i])
    return b

def k1_ray1_mountain():  # K-1, six disks with ray 1 marked M
    b=''
    for y in (6.1,13.3,20.5):
        for x in (4.5,14): b+=disk(x,y,2.05,nums=True,labels=['M','','',''])
    return b

def k1_shared_tabs():  # K-1, three rows of three part-labelled disks and six tabs
    b=''
    partial_models=[['M','','V',''],['M','M','',''],['V','','V','']]
    for j,tabs in enumerate(['MMVVVV','MMMVVV','MMMMVV']):
        y=5.9+j*6.6
        for i,x in enumerate((3.1,9.4,15.7)):
            b+=disk(x,y,1.6,nums=True,labels=partial_models[i],tag='ABC'[j] if i==0 else None)
        for k,label in enumerate(tabs):
            x=5.1+k*1.55
            b+=r'\draw[line width=.5pt] '+coord(x-.45,y+2.2)+' rectangle '+coord(x+.45,y+3.05)+';\n'
            b+=node(x,y+2.625,label,15,True)
    return b

def ten_small_disks():  # K-1 and grades 2-3, ten blank right-angle disks
    b=''
    for y in (5.0,9.2,13.4,17.6,21.8):
        for x in (4.5,14):b+=disk(x,y,1.58,nums=True)
    return b

def k1_routes():  # K-1, the eight states A-H and two route strips
    b=''
    for i,labs in enumerate(ROUTE_LABELS):
        b+=disk((2.2,7.0,11.8,16.6)[i%4],(6.3,13.0)[i//4],1.5,nums=True,labels=labs,tag='ABCDEFGH'[i])
    for y,end in [(19.2,'H'),(22.6,'D')]:
        for j in range(8):
            x=1.15+j*2.35
            if j==0 or j==7:b+=node(x,y,'A' if j==0 else end,16,True)
            else:b+=line(x-.65,y+.2,x+.65,y+.2)
            if j<7:b+=line(x+.8,y,x+1.55,y,'black!55,line width=.5pt,->')
    return b

def wedge_groups():  # grades 2-3, seven wedges, a half-turn template and record lines
    b=''
    for x,a,lab in zip((2.2,6.8,11.4,16.0),(30,30,60,60),'ABCD'):b+=wedge(x,8.0,2.25,a,lab)
    for x,a,lab in zip((4.3,9.4,14.5),(90,120,150),'EFG'):b+=wedge(x,12.0,2.25,a,lab)
    b+=half(9.35,16.3,2.25)+record_lines((18.0,19.4,20.8,22.2,23.6),2)
    return b

def matching_wedge_disks():  # grades 2-3, shaded disks A-D with sector labels and answer blanks
    b=''
    for i,ss in enumerate(ANGLES):
        x=(4.5,14)[i%2];y=(7.1,17.1)[i//2]
        b+=disk(x,y,2.5,sectors=ss,shade=True,tag='ABCD'[i],sector_labels=['ABCD'[i]+str(j) for j in range(1,5)])
        b+=text(x-2.5,y+3.15,'Shaded: '+r'\rule{1.5cm}{.35pt}',11,width=5)+text(x-2.5,y+4.0,'White: '+r'\rule{1.5cm}{.35pt}',11,width=5)
    return b

def close_disks_23():  # grades 2-3, numbered disks A-D and record lines
    b=''
    for i,ss in enumerate(ANGLES): b+=disk((4.5,14)[i%2],(7.1,16.4)[i//2],2.4,sectors=ss,nums=True,tag='ABCD'[i])
    b+=record_lines((21.0,22.4,23.8))
    return b

def close_disks_45():  # grades 4-5, disks A-D with degrees
    b=''
    for i,ss in enumerate(ANGLES):b+=disk((4.5,14)[i%2],(9.0,19.0)[i//2],2.45,sectors=ss,nums=True,degrees=True,tag='ABCD'[i])
    return b

def add_ray_starts():  # grades 2-3, four three-ray starts with 30-degree ticks
    b=''
    for i,rays in enumerate(([0,90,180],[0,60,180],[0,30,180],[0,120,180])):b+=disk((4.5,14)[i%2],(7.3,18.0)[i//2],2.65,rays=rays,tag='ABCD'[i],ticks=True)
    return b

def odd_ray_disks():  # grades 4-5, three odd-degree patterns and record lines
    b=''
    for i,ss in enumerate(([120,120,120],[60,60,60,90,90],[30,30,60,60,60,60,60])):
        x,y=[(4.5,7.2),(14,7.2),(9.35,16.0)][i]
        b+=disk(x,y,2.35,sectors=ss,degrees=True,tag='ABC'[i])
    b+=record_lines((20.3,21.8,23.3,24.8))
    return b

def alternating_disks():  # grades 4-5, four shaded patterns and record lines
    b=''
    for i,ss in enumerate(CHECKS):b+=disk((4.5,14)[i%2],(6.4,13.8)[i//2],2.0,sectors=ss,degrees=True,shade=True,tag='ABCD'[i])
    b+=record_lines((18.2,19.7,21.2,22.7,24.2))
    return b

def labelings_45():  # grades 4-5, ten small disks and record lines
    b=''
    for y in (6.1,10.9):
        for x in (1.7,5.55,9.4,13.25,17.1):b+=disk(x,y,1.32,nums=True)
    b+=record_lines((14.8,16.4,18.0,19.6,21.2,22.8,24.4))
    return b

def ruled_out_disks():  # grades 4-5, labelled disks A-D and record lines
    b=''
    for i,labs in enumerate(['MMMM','VVVV','MMVV','MVMV']):
        b+=disk((4.5,14)[i%2],(6.1,13.1)[i//2],2.05,nums=True,labels=labs,tag='ABCD'[i])
    b+=record_lines((17.5,19.1,20.7,22.3,23.9))
    return b

def six_wedges_23():  # grades 2-3, six wedges AABBCC and four start disks
    b=''
    for i,(a,lab) in enumerate(zip((30,30,60,60,90,90),'AABBCC')):b+=wedge((3.1,9.4,15.7)[i%3],(6.0,9.4)[i//3],2.4,a,lab)
    for y in (13.0,21.0):
        for x in (4.5,14):b+=disk(x,y,2.4,rays=[0])
    return b

def angle_orders_45(rows=12):  # grades 4-5, a start disk and recording strips
    b=disk(15.75,7.0,1.75,rays=[0])+node(15.75,4.85,'start',10)
    # Recording strips show ordered slots, without supplying an approach.
    for j in range(rows):
        y=6.0+j*1.15
        for k in range(6):
            x=.35+k*1.7
            b+=line(x,y,x+1.35,y)
    b+=record_lines((21.6,23.0,24.4))
    return b
