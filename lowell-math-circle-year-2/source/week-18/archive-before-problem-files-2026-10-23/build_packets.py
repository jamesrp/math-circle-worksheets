from pathlib import Path
import itertools, json
from examples import training
ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'src'
PRE=r'''\RequirePackage{fix-cm}
\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.5in]{geometry}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000\exhyphenpenalty=10000
\pdfmapfile{+cm.map}
\begin{document}
'''
class Packet:
    def __init__(self,filename,level,ident):
        self.filename=filename;self.level=level;self.ident=ident;self.pages=[]
    def page(self):
        if self.pages:self.endpage()
        self.parts=[r'\null\begin{tikzpicture}[remember picture,overlay]',r'\begin{scope}[shift={(current page.north west)},x=1cm,y=-1cm]',r'\begin{scope}[shift={(1.5,1.5)}]']
        self.text(0,-.45,18.5,f'Week 18 / Hidden changes / {self.level}',11,14)
        self.text(0,24.5,16.5,f'Bellingham Math Circle / Week 18 / {self.ident}',10,12)
        self.parts.append(r'\node[anchor=north east,inner sep=0,font=\sffamily\fontsize{10}{12}\selectfont] at (18.59,24.5) {'+str(len(self.pages)+1)+'};')
        self.pages.append(None)
    def text(self,x,y,w,txt,size=14,lead=None):
        lead=lead or size*1.24
        self.parts.append(r'\node[anchor=north west,inner sep=0,align=left,text width='+str(w)+'cm,font=\\sffamily\\fontsize{'+str(size)+'}{'+str(lead)+'}\\selectfont] at ('+str(x)+','+str(y)+') {'+txt+'};')
    def problem(self,n,txt,y=.45,size=15):
        self.text(0,y,18.4,r'\textbf{Problem '+str(n)+':} '+txt,size)
    def shape(self,x,y,shape,scale=.38):
        if shape=='triangle':
            self.parts.append(f'\\draw[line width=.8pt] ({x},{y-scale}) -- ({x-scale},{y+scale*.8}) -- ({x+scale},{y+scale*.8}) -- cycle;')
        elif shape=='square':
            self.parts.append(f'\\draw[line width=.8pt] ({x-scale},{y-scale}) rectangle ({x+scale},{y+scale});')
        elif shape=='diamond':
            self.parts.append(f'\\draw[line width=.8pt] ({x},{y-scale*1.2}) -- ({x+scale},{y}) -- ({x},{y+scale*1.2}) -- ({x-scale},{y}) -- cycle;')
        elif shape=='star':
            self.parts.append(f'\\node[star,star points=5,star point ratio=2.1,draw,line width=.8pt,minimum size={scale*2.4}cm,inner sep=0] at ({x},{y}) {{}};')
    def strip(self,x,y,bits,cell=2.05,h=None,mode='circle'):
        h=h or cell
        self.parts.append(f'\\fill ({x-.32},{y+h/2-.14}) -- ({x-.12},{y+h/2}) -- ({x-.32},{y+h/2+.14}) -- cycle;')
        self.parts.append(f'\\draw[line width=.7pt] ({x},{y}) rectangle ({x+len(bits)*cell},{y+h});')
        for i,b in enumerate(bits):
            if i:self.parts.append(f'\\draw[line width=.7pt] ({x+i*cell},{y}) -- ({x+i*cell},{y+h});')
            cx=x+(i+.5)*cell;cy=y+h/2
            if b in '01':
                if mode=='circle':self.parts.append(f'\\draw[line width=.9pt,fill={"black" if b=="1" else "white"}] ({cx},{cy}) circle ({min(cell,h)*.205});')
                else:self.parts.append(f'\\node[font=\\ttfamily\\fontsize{{16}}{{18}}\\selectfont] at ({cx},{cy}) {{{b}}};')
    def keyed(self,x,y,shape,bits,cell=2.05,h=None,mode='circle'):
        h=h or cell
        if self.filename=='grades-2-3':
            self.shape(x+.25,y+h/2,shape,.27);self.strip(x+.9,y,bits,cell,h,mode)
        else:
            self.shape(x+.45,y+h/2,shape,.34);self.strip(x+1.2,y,bits,cell,h,mode)
    def line(self,x,y,w):self.parts.append(f'\\draw[gray!50,line width=.35pt] ({x},{y}) -- ({x+w},{y});')
    def endpage(self):
        if self.pages and self.pages[-1] is None:self.pages[-1]='\n'.join(self.parts)+r'\end{scope}\end{scope}\end{tikzpicture}'
    def save(self):
        self.endpage();(SRC/(self.filename+'.tex')).write_text(PRE+'\n\\newpage\n'.join(self.pages)+'\n\\end{document}\n')

# K--1: all counter cells are 2.05 cm wide and tall.
k=Packet('k-1','K--1','W18-K-v3')
training(k,'Keep the arrow at the left. The sender hides a picture and its row. The changer turns over zero or one counter in secret. Only the final row crosses the folder; the receiver uses the key to find the picture.')
k.page()
k.problem(1,'Send both pictures with this key many times. Can the changer fool the receiver?',3.45,17)
k.keyed(.35,6.15,'triangle','000');k.keyed(9.7,6.15,'square','111')
for y in [10.25,14.35,18.45]:
    k.strip(1.1,y,'---');k.strip(10.45,y,'---')
k.page()
k.problem(2,'Draw every possible picture beside each final row. Which key lets the changer fool the receiver?',.45,17)
k.keyed(.35,2.8,'triangle','000');k.keyed(9.7,2.8,'square','111')
for x,y,bits in [(.45,6.05,'000'),(9.8,6.05,'101'),(.45,9.3,'010'),(9.8,9.3,'111')]:
    k.strip(x,y,bits);k.line(x+6.6,y+1.6,1.4)
k.keyed(.35,13,'triangle','00');k.keyed(9.7,13,'square','11')
for x,y,bits in [(.45,16.25,'00'),(9.8,16.25,'01'),(.45,19.5,'10'),(9.8,19.5,'11')]:
    k.strip(x,y,bits);k.line(x+4.65,y+1.6,3.4)
k.page()
k.problem(3,'Make two two-counter rows for the pictures. Can you keep the changer from fooling the receiver?',.45,17)
for y in [4,9,14,19]:
    k.keyed(.35,y,'triangle','--');k.keyed(9.7,y,'square','--')
k.page()
k.problem(4,'Find every three-counter key that always tells the two pictures apart; use more paper if needed. Swapping the pictures makes a different key.',.45,17)
for y in [3.15,6.75,10.35,13.95,17.55,21.15]:
    k.keyed(.35,y,'triangle','---');k.keyed(9.7,y,'square','---')
k.page()
k.problem(5,'For each key, find every square row that always works. Use both kinds of counter in each row, and use more paper if needed.',.45,17)
for y,bits in [(3.4,'0011'),(14.25,'0100')]:
    k.keyed(3.4,y,'triangle',bits);k.keyed(3.4,y+3.15,'square','----')
k.page()
k.problem(6,'Can three pictures share a three-counter key that always works? Make one, or show why it cannot be done.',.45,17)
for x in [.35,9.7]:
    for y,shape in zip([4,8.2,12.4],['triangle','square','star']):k.keyed(x,y,shape,'---')
k.save()

# Grades 2--3: all counter cells are at least 2 cm wide and tall.
g=Packet('grades-2-3','Grades 2--3','W18-23-v3')
training(g,'Keep the arrow at the left. A key gives each picture a different row, all the same length. The sender hides the picture and its row. A changer secretly turns over zero or one counter. Only the final row crosses the folder. The receiver knows the key.')
g.page()
g.problem(1,'Use each key to send both pictures several times. Which keys always let the receiver tell which picture was sent?',3.85,15)
for x,a,b in [(.8,'000','111'),(10,'001','101')]:
    g.keyed(x,6.35,'triangle',a,2);g.keyed(x,9.0,'square',b,2)
for y in [12.2,15.8,19.4]:
    g.strip(1.8,y,'---',2);g.strip(11,y,'---',2)
g.page()
g.problem(2,'For each key, find a row that the receiver could get from either picture. If there is no such row, explain why.',.45,15)
for x,y,a,b in [(0,3.1,'0000','0001'),(9.5,3.1,'0101','0110'),(0,13.7,'0001','1111'),(9.5,13.7,'0011','1100')]:
    g.keyed(x,y,'triangle',a,2);g.keyed(x,y+2.6,'square',b,2)
g.page()
g.problem(3,'Make a key for the two pictures with 1, 2, or 3 counters in each row. What is the shortest length that always works? Explain why no shorter key works.',.45,15)
for y,n in [(3.8,1),(9.6,2),(15.4,3)]:
    g.keyed(1,y,'triangle','-'*n,2);g.keyed(10.2,y,'square','-'*n,2)
g.page()
g.problem(4,'Make four-counter keys for the two pictures with exactly two filled circles in each row. Find every key that always works. Swapping the pictures counts as a different key. Use more paper if needed.',.45,15)
for y in [4,8.6,13.2,17.8]:
    g.keyed(0,y,'triangle','----',2);g.keyed(9.5,y,'square','----',2)
g.page()
g.problem(5,'Make a key for all four pictures with five counters in each row. The receiver must always know the picture after zero or one change. Explain how you know your key works.',.45,15)
for y,shape in zip([3.8,7,10.2,13.4],['triangle','square','star','diamond']):g.keyed(1.4,y,shape,'-----',2)
g.page()
g.problem(6,'This time the changer may turn over zero, one, or two counters. Make the shortest key you can for the two pictures, using at most five counters in each row. Explain why your length is the shortest.',.45,15)
for y,shape in [(4,'triangle'),(7.15,'square')]:g.shape(1.9,y+.7,shape);g.line(3.0,y+1.5,12.7)
for y,shape in [(13.5,'triangle'),(16.65,'square')]:g.shape(1.9,y+.7,shape);g.line(3.0,y+1.5,12.7)
g.save()

# Grades 4--5: direct binary notation and open workspace for lists and arguments.
h=Packet('grades-4-5','Grades 4--5','W18-45-v3')
training(h,'Use 0 for an empty circle and 1 for a filled circle. A key gives a different row to each picture, all the same length. The sender hides the picture and its row. A changer changes zero or one entry, without saying where or whether a change occurred. The receiver gets only the final row and knows the key. Keep the arrow at the left.')
h.page()
h.problem(1,'For each key, find every row the receiver might see. Mark any row that could mean either picture. Which keys always let the receiver recover the picture?',4.1,14)
for y,a,b in [(7,'00','11'),(12.7,'000','111'),(18.4,'0010','0100')]:
    h.keyed(.45,y,'triangle',a,.85,.95,'number');h.keyed(9.7,y,'square',b,.85,.95,'number')
h.page()
h.problem(2,'Make a key for all four pictures with five entries in each row. The receiver must always recover the picture after zero or one change. Explain why your key works.',.45,14)
for y,shape in zip([3.4,5.65,7.9,10.15],['triangle','square','star','diamond']):h.keyed(1.5,y,shape,'-----',1.2,1.1,'number')
h.page()
h.problem(3,'For each pair, could the receiver see the same row after either picture was sent? What is the smallest number of differing positions that keeps two pictures apart for rows of any length? Explain why that number is enough and why a smaller number fails.',.45,14)
for x,a,b in [(.3,'000000','110000'),(9.6,'010010','101010')]:
    h.keyed(x,4.4,'triangle',a,.85,.95,'number');h.keyed(x,6.3,'square',b,.85,.95,'number')
h.page()
h.problem(4,'Find every row the receiver might see from each row below, and explain why none are missing. How many received rows can come from any one row of length 10?',.45,14)
for y,bits in [(3.4,'010'),(9.5,'0110'),(15.6,'00111')]:h.strip(.7,y,bits,1,.95,'number')
h.page()
h.problem(5,'What is the shortest row length for a key that always works for four pictures? Give a working key and explain why every shorter length is impossible.',.45,14)
for y,shape in zip([3.3,5.5,7.7,9.9],['triangle','square','star','diamond']):
    h.shape(1.3,y+.35,shape);h.line(2.45,y+1,10.9)
h.page()
h.problem(6,'Can three pictures have a key that always works with four entries in each row? Find one, or explain why every choice fails.',.45,14)
for y,shape in zip([3.4,5.9,8.4],['triangle','square','star']):h.keyed(1.5,y,shape,'----',1.3,1.1,'number')
h.save()

# Independent finite checks for the mathematical claims and construction tasks.
def d(a,b):return sum(x!=y for x,y in zip(a,b))
def strings(n):return [''.join(x) for x in itertools.product('01',repeat=n)]
def ball(s,r=1):return {t for t in strings(len(s)) if d(s,t)<=r}
def reliable(code,r=1):return all(d(a,b)>=2*r+1 for a,b in itertools.combinations(code,2))
checks={}
checks['k_decode']={s:[m for m,c in [('triangle','000'),('square','111')] if s in ball(c)] for s in strings(3)}
checks['two_counter_ambiguity']={s:[c for c in ['00','11'] if s in ball(c)] for s in strings(2)}
checks['ordered_three_counter_keys']=[(a,b) for a in strings(3) for b in strings(3) if reliable([a,b])]
checks['mixed_four_counter_completions']={a:[b for b in strings(4) if '0' in b and '1' in b and reliable([a,b])] for a in ['0011','0100']}
assert [len(v) for v in checks['mixed_four_counter_completions'].values()]==[5,4]
assert len(checks['ordered_three_counter_keys'])==8
checks['weight_two_ordered_keys']=[(a,b) for a in strings(4) for b in strings(4) if a.count('1')==b.count('1')==2 and reliable([a,b])]
assert len(checks['weight_two_ordered_keys'])==6
checks['four_picture_five_entry_example']=['01001','01110','10000','10111']
assert reliable(checks['four_picture_five_entry_example'])
checks['three_picture_four_entry_keys']=sum(reliable(c) for c in itertools.combinations(strings(4),3))
assert checks['three_picture_four_entry_keys']==0
checks['four_picture_four_entry_keys']=sum(reliable(c) for c in itertools.combinations(strings(4),4))
assert checks['four_picture_four_entry_keys']==0
checks['five_entry_received_count']=len(set.union(*(ball(c) for c in checks['four_picture_five_entry_example'])))
assert checks['five_entry_received_count']==24
checks['two_change_minimum']=next(n for n in range(1,6) if any(reliable([a,b],2) for a,b in itertools.combinations(strings(n),2)))
assert checks['two_change_minimum']==5
checks['neighborhood_counts']={n:len(ball('0'*n)) for n in [2,3,4,5,10]}
(SRC/'mathematical-checks.json').write_text(json.dumps(checks,indent=2))
print('Wrote three six-page sources; finite mathematical checks passed.')
