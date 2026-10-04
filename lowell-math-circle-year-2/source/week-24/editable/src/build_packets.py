from pathlib import Path
ROOT=Path(__file__).resolve().parent
PRE=r'''\documentclass[letterpaper]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage[margin=0in]{geometry}
\usepackage{tikz}
\pagestyle{empty}
\renewcommand{\familydefault}{\sfdefault}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''

def text(x,y,t,size=14,width=7.2,anchor='north west'):
    return rf'\node[anchor={anchor},inner sep=0pt,text width={width}in,align=left,font=\fontsize{{{size}}}{{{size+4}}}\selectfont] at ({x},{y}) {{{t}}};'

def card(x,y,value,w=.62,h=.87,dots=False):
    # x,y is bottom-left; cards are illustrations, not a cutting template.
    s=[rf'\draw[line width=.8pt,rounded corners=2pt] ({x},{y}) rectangle ({x+w},{y+h});']
    if value is not None:
        s.append(rf'\node[font=\fontsize{{{25 if dots else 22}}}{{26}}\selectfont] at ({x+w/2},{y+h*(.76 if dots else .5)}) {{{value}}};')
        if dots:
            for i in range(value):
                col=i%3;row=i//3
                xx=x+w/2+(col-1)*.14; yy=y+.37-row*.125
                s.append(rf'\fill ({xx},{yy}) circle (.025);')
    return '\n'.join(s)

def kdeck(label,values,y,x=2.12):
    s=[rf'\node[font=\fontsize{{22}}{{25}}\selectfont] at (1.3,{y+.53}) {{{label}}};']
    for i,v in enumerate(values):s.append(card(x+i*1.26,y,v,.86,1.12,True))
    return '\n'.join(s)

def kpool(values,y):
    w=.73;gap=.29;start=(8.5-len(values)*w-(len(values)-1)*gap)/2
    return '\n'.join(card(start+i*(w+gap),y,v,w,1.1,True) for i,v in enumerate(values))

def group(label,values,x,y,columns=3):
    s=[rf'\node[anchor=south,font=\fontsize{{16}}{{19}}\selectfont] at ({x+.99},{y+1.02}) {{{label}}};']
    for i,v in enumerate(values):s.append(card(x+(i%columns)*.7,y-(i//columns)*1.0,v))
    return '\n'.join(s)

def decks(ds,y=7.7):
    return '\n'.join(group(l,v,.72+i*2.4,y) for i,(l,v) in enumerate(ds))

def pool(values,y,columns=6):
    width=(min(columns,len(values))-1)*.86+.62; x=(8.5-width)/2
    return '\n'.join(card(x+(i%columns)*.86,y-(i//columns)*1.0,v) for i,v in enumerate(values))

def pair(label1,a,label2,b,x,y):
    s=[]
    for i,(l,v) in enumerate(((label1,a),(label2,b))):
        yy=y-i*1.1
        s.append(rf'\node[font=\fontsize{{15}}{{18}}\selectfont] at ({x},{yy+.435}) {{{l}}};')
        for j,n in enumerate(v):s.append(card(x+.36+j*.74,yy,n))
    return '\n'.join(s)

def shared_pairs(label1,a,label2,b):
    # Nine explicitly pictured pairs: a single pooled record, with no numeral
    # transcription or row/column convention required. Circle either card.
    s=[]
    for i,left in enumerate(a):
        for j,right in enumerate(b):
            x=1.04+j*2.33; y=3.75-i*1.45
            for label,value,xx in ((label1,left,x),(label2,right,x+1.0)):
                s.append(rf'\node[font=\fontsize{{12}}{{15}}\selectfont] at ({xx+.365},{y+1.27}) {{{label}}};')
                s.append(card(xx,y,value,.73,1.1,True))
    return '\n'.join(s)

ABC=[('A',[2,4,9]),('B',[1,6,8]),('C',[3,5,7])]
K=[
('For each of Problems 1--3, split the pairs among you and circle all nine winners on one shared page. Which deck wins more pairs?',kdeck('A',[2,4,9],7.3)+kdeck('B',[1,6,8],5.85)+shared_pairs('A',[2,4,9],'B',[1,6,8])),
('Which deck wins more pairs?',kdeck('B',[1,6,8],7.9)+kdeck('C',[3,5,7],6.45)+shared_pairs('B',[1,6,8],'C',[3,5,7])),
('Does any of A, B, and C win more pairs than both other decks?',kdeck('C',[3,5,7],7.9)+kdeck('A',[2,4,9],6.45)+shared_pairs('C',[3,5,7],'A',[2,4,9])),
('For each of A, B, and C, choose a deck that wins more card pairs and play six rounds. Must your chosen deck win more rounds?',kdeck('A',[2,4,9],7.9)+kdeck('B',[1,6,8],6.5)+kdeck('C',[3,5,7],5.1)),
('Try 3, 5, 7, and 9 in A\'s empty place. Which choices make A win more card pairs than B?',kdeck('A',[2,4,None],7.8)+kdeck('B',[1,6,8],6.4)+kpool([3,5,7,9],4.85)),
('Swap one A card with one B card. Find every swap that makes B win more card pairs than A.',kdeck('A',[2,4,9],7.9)+kdeck('B',[1,6,8],6.45)),
('Put these six cards into two decks of three so both decks win the same number of pairs. Find a way, or show why it cannot be done.',kpool(list(range(1,7)),7.9)+kdeck('A',[None]*3,6.35)+kdeck('B',[None]*3,4.9)),
('Can these six cards make three two-card decks where A wins more pairs than B, B more than C, and C more than A? Show a way, or show why it cannot be done.',kpool(list(range(1,7)),7.9)+kdeck('A',[None]*2,6.35,2.65)+kdeck('B',[None]*2,4.95,2.65)+kdeck('C',[None]*2,3.55,2.65)),
]
G23=[
('For each pair of decks, find which deck wins more of the possible card pairs. Is there a deck that wins more pairs than both of the others?',decks(ABC,7.3)),
('Two bags hold two different decks from A, B, and C. You hear only which bag wins. The left bag wins six draws in a row. Can you be sure it wins more possible card pairs? Could any fixed number of these results make you sure? Explain.',decks(ABC,7.6)),
('Keep 9 in A, 8 in B, and 7 in C. Place cards 1 to 6 so A wins more pairs than B, B more than C, and C more than A. Find two arrangements different from Problem 1.',pool(list(range(1,7)),7.7)+decks([('A',[None,None,9]),('B',[None,None,8]),('C',[None,None,7])],5.95)),
('Choose 0, 2, 4, 9, or 10 for A\'s empty card. Find every choice that makes A win more pairs than B, B more than C, and C more than A.',decks([('A',[2,None,9]),('B',[1,6,8]),('C',[3,5,7])],7.8)+pool([0,2,4,9,10],6.05)),
('For each pair of these six-card decks, how many possible card pairs does each deck win? Does any winner change from Problem 1?',decks([('A',[2,2,4,4,9,9]),('B',[1,1,6,6,8,8]),('C',[3,3,5,5,7,7])],7.9)),
('Choose nine different cards from 1 to 12 and make three decks of three. Make A win more pairs than B, B more than C, and C more than A, with totals 15 in A, 18 in B, and 21 in C.',pool(list(range(1,13)),7.75)+decks([('A',[None]*3),('B',[None]*3),('C',[None]*3)],5.05)),
('Use cards 1 to 6 once each to make three two-card decks. Can A win more pairs than B, B more than C, and C more than A? Find an arrangement, or explain why there is none.',pool(list(range(1,7)),7.7)+decks([('A',[None]*2),('B',[None]*2),('C',[None]*2)],5.95)),
]
G45=[
('For each pair of decks, find how many of the possible card pairs each deck wins. Is there a deck that wins more than half its pairs against both others? Do the three deck totals settle this question?',decks(ABC,7.15)),
('Keep 9 in A, 8 in B, and 7 in C. Use cards 1 to 6 once each to finish the decks so A wins more than half its pairs against B, B against C, and C against A. Find every arrangement and explain why none are missing.',pool(list(range(1,7)),7.5)+decks([('A',[None,None,9]),('B',[None,None,8]),('C',[None,None,7])],5.75)),
('Write numbers from 1 to 6 on these nine cards. A number may repeat within one deck, but it cannot appear in two different decks. Make A win more than half its pairs against B, B against C, and C against A.',decks([('A',[None]*3),('B',[None]*3),('C',[None]*3)],7.65)),
('Find each deck\'s chance of winning against each other deck, first with the six-card decks and then with the four-card decks. Which chances changed from Problem 1?',decks([('A',[2,2,4,4,9,9]),('B',[1,1,6,6,8,8]),('C',[3,3,5,5,7,7])],7.6)+decks([('A',[2,2,4,9]),('B',[1,1,6,8]),('C',[3,3,5,7])],4.7)),
('Decide which deck, if either, wins more than half the pairs in each comparison. Find a rule that works for every pair of two-card decks with no number shared between decks, and explain why it works.',pair('A',[1,5],'B',[2,4],1.05,7.6)+pair('C',[2,6],'D',[1,5],4.8,7.6)+pair('E',[4,6],'F',[2,3],1.05,4.85)+pair('G',[1,3],'H',[2,6],4.8,4.85)),
('Can three one-card decks make A win more than half its pairs against B, B against C, and C against A? Can three two-card decks do it? Explain for any choice of numbers. What is the fewest cards per deck that allows this, with all decks the same size?',decks([('A',[None]),('B',[None]),('C',[None])],7.25)+decks([('A',[None]*2),('B',[None]*2),('C',[None]*2)],5.1)),
('Use cards 1 to 9 once each in three decks of three. Can A win at least six of its nine pairs against B, B at least six against C, and C at least six against A? Find an arrangement, or explain why it is impossible.',pool(list(range(1,10)),7.55,9)+decks([('A',[None]*3),('B',[None]*3),('C',[None]*3)],5.75)),
]

def write_packet(name,level,pid,problems,young=False):
    ss=[PRE]
    for n,(prompt,art) in enumerate(problems,1):
        if n>1:ss.append(r'\newpage')
        ss += [r'\null',r'\begin{tikzpicture}[remember picture,overlay,x=1in,y=1in]',r'\begin{scope}[shift={(current page.south west)}]']
        ss.append(text(.62,10.5,f'Week 24 / Three random decks / {level}',10.5,7.25,'west'))
        if n==1:
            rule=("Each card has the same chance. Mix the bags separately. Draw once from each bag, then put both cards back. The bigger number wins." if young else "Each physical card is equally likely. Mix each deck separately and draw one card from each. Return both cards before the next round. The larger number wins. The two decks in a comparison must not share a number. Card order in a deck does not matter.")
            ss.append(text(.62,10.07,rule,11.5))
        yy=9.02 if n==1 else 9.95
        ss.append(text(.62,yy,rf'\textbf{{Problem {n}:}} '+prompt,16 if young else 13.5))
        ss.append(art)
        ss.append(text(.62,.46,f'Bellingham Math Circle / Week 24 / {pid}',9.5,6.7,'west'))
        ss.append(rf'\node[anchor=east,inner sep=0pt,font=\fontsize{{9.5}}{{12}}\selectfont] at (7.88,.46) {{{n}}};')
        ss += [r'\end{scope}',r'\end{tikzpicture}']
    ss.append(r'\end{document}')
    (ROOT/f'{name}.tex').write_text('\n'.join(ss))

write_packet('k-1',r'K--1','F24-K-v2',K,True)
write_packet('grades-2-3',r'Grades 2--3','F24-23-v2',G23)
write_packet('grades-4-5',r'Grades 4--5','F24-45-v2',G45)
