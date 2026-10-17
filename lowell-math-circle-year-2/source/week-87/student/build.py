#!/usr/bin/env python3
"""Portable Week 87 revised student packet. Python stdlib + pdflatex/TikZ only."""
import argparse, os, shutil, subprocess
from pathlib import Path
P=[]
def t(x,y,s,w=178,size=12):
 return rf'\node[anchor=north west,inner sep=0pt,text width={w}mm,font=\fontsize{{{size}}}{{{size*1.25}}}\selectfont] at ({x},{y}) {{{s}}};'
def line(x,y,x2,y2): return rf'\draw ({x},{y})--({x2},{y2});'
def box(x,y,w,h,label='',size=12):
 return rf'\draw ({x},{y}) rectangle ++({w},{h});'+ (t(x+2,y+2,label,w-4,size) if label else '')
def circle(x,y,r,label,size=10): return rf'\draw ({x},{y}) circle ({r});\node[font=\fontsize{{{size}}}{{{size+1}}}\selectfont] at ({x},{y}) {{{label}}};'
def page(level,ident,content):
 n=len(P)+1
 P.append(t(18,13,'Week 87 / Voting and agendas / '+level,size=10)+line(18,21,198,21)+content+line(18,262,198,262)+t(18,266,f'Bellingham Math Circle / Week 87 / {ident}',size=9)+t(190,266,str(n),8,9))
def card(x,y,seq,vid,w=36,h=51):
 out=box(x,y,w,h)+t(x+2,y+2,vid,w-4,9)
 for i,c in enumerate(seq):
  yy=y+10+i*(h-10)/3
  out+=line(x,yy,x+w,yy)+t(x+2,yy+2,['1st','2nd','3rd'][i],8,8)+t(x+11,yy+1,c,max(w-13,5),15)
 return out

def cards(x,y,profile,w=36,h=51,gap=9): return ''.join(card(x+i*(w+gap),y,s,'V'+str(i+1),w,h) for i,s in enumerate(profile))
def space(y,h=35):return box(18,y,180,h)
def problem(n,y,s):return t(18,y,rf'\textbf{{Problem {n}:}} '+s)
def numberline(x,y,span=160,favs=None,proposals=None,small=False):
 out=line(x,y,x+span,y)
 for i in range(11):
  xx=x+span*i/10
  out+=line(xx,y-1.5,xx,y+1.5)+t(xx-2,y+3,str(i),6,7 if small else 9)
 if favs:
  for i,f in enumerate(favs):
   yy=y-8-(i%3)*7
   out+=line(x+span*f/10,yy+2,x+span*f/10,y-2)+t(x+span*f/10-4,yy-4,'V'+str(i+1),10,7 if small else 9)
 if proposals:
  for lab,f in proposals:
   xx=x+span*f/10
   out+=box(xx-3,y+13,6,6)+t(xx-2,y+14,lab,5,7)
 return out

def tally(x,y,labels,groups,scale=1):
 out=''
 for j,(lab,vs) in enumerate(zip(labels,groups)):
  xx=x+j*19*scale
  out+=box(xx,y,18*scale,26*scale)+t(xx+1,y+1,lab,16*scale,7*scale)
  for k,v in enumerate(vs):out+=circle(xx+(5+(k%2)*8)*scale,y+(12+(k//2)*8)*scale,3.1*scale,v,5*scale)
 return out

def doc(path):
 pre=r'''\documentclass[letterpaper]{article}
\usepackage[margin=0pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,tikz}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\pdfinfoomitdate=1
\pdftrailerid{}
\pdfsuppressptexinfo=15
\begin{document}
'''
 body='\n\\newpage\n'.join(r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]\begin{scope}[shift={(current page.north west)}]'+p+r'\end{scope}\end{tikzpicture}' for p in P)
 path.write_text(pre+body+'\n\\end{document}\n')

def shared():
 P.clear()
 s=t(18,29,'Keep the voter cards unchanged. For each pair, each voter chooses the higher of the two letters on their card. Put that voter\'s token beside their choice. More votes wins.',size=11)
 s+=t(18,52,'Pair on offer: D and E',size=10)
 s+=cards(18,61,['DFE','EFD','FED'],16,38,2)
 s+=t(77,61,'Chosen from D/E',51,9)+t(80,73,r'V1 $\to$ D\\V2 $\to$ E\\V3 $\to$ E',40,11)
 s+=t(137,61,'All three votes',60,9)+tally(137,70,['D','E'],[['V1'],['V2','V3']])+t(140,101,'E wins, 2 to 1',55,10)
 s+=problem(1,119,'Use these three cards. Is there a letter that wins against each of the other two?')
 s+=cards(33,148,['ABC','BCA','CAB'],43,62,9)
 s+=space(226,25)
 page('Grades 2--5','W87-S-v1',s)
 s=t(18,29,'A knockout starts with two letters. The winner faces the waiting letter; that vote chooses the final winner. Put each loser in Out. Reset all three letters before a new knockout.',size=11)
 s+=cards(18,58,['DFE','EFD','FED'],20,38,3)
 s+=t(99,60,'The same cards stay visible in both rounds.',96,10)
 s+=box(18,105,53,31,r'D vs E: E wins\\D goes to Out',10)+t(72,114,r'$\longrightarrow$',12,14)
 s+=box(86,105,47,31,r'E stays in\\F was waiting',10)+t(135,114,r'$\longrightarrow$',12,14)
 s+=box(148,105,50,31,r'E vs F: F wins\\E goes to Out',10)
 s+=problem(2,149,'Keep the A/B/C cards from Problem 1. Choose a first pair and a waiting letter so that A wins the knockout. Can you make B win? Can you make C win?')
 for i,goal in enumerate('ABC'):
  y=186+i*22
  s+=t(20,y+3,'Winner '+goal,30,11)+box(53,y,52,17,'First pair:',9)+box(111,y,39,17,'Waiting:',9)+box(156,y,40,17,'Final pair:',9)
 page('Grades 2--5','W87-S-v1',s)
 s=t(18,29,'Each ranking card must contain A, B and C once. Keep each set of cards unchanged while trying its knockouts.',size=11)
 s+=problem(3,48,'Make three different cards so that the same letter wins every knockout. Make another set of three different cards where changing the waiting letter changes the winner.')
 s+=t(18,82,'Same winner every time',180,10)+cards(29,91,['   ']*3,43,60,9)
 s+=t(18,165,'Different winners',180,10)+cards(29,174,['   ']*3,43,60,9)
 page('Grades 2--5','W87-S-v1',s)

def line_visit():
 P.clear()
 s=t(18,29,'Each favorite marker is one voter. Favorites stay still. Each voter chooses the nearer proposal, X or Y. Equal distances put that vote in Tie. More votes wins; equal vote counts give a tied vote. Keep X/Y proposals on the board; use the separate X/Y tally labels. Use only the numbered ticks.',size=10.5)
 # One unchanged five-voter input, all choices, then a complete tally.
 s+=t(18,63,'Fixed favorites; proposals X=2, Y=8',99,8)
 for i,f in enumerate([0,1,5,8,10]):
  yy=79+i*8
  s+=t(18,yy-3,'V'+str(i+1),10,7)+line(30,yy,110,yy)
  for j in range(11):s+=line(30+8*j,yy-1,30+8*j,yy+1)
  s+=circle(30+8*f,yy,3,'V'+str(i+1),5)
 s+=numberline(30,123,80,small=True)
 s+=box(43,137,6,6)+t(44,138,'X',5,7)
 s+=r'\draw (94,136)--(98,140)--(94,144)--(90,140)--cycle;'+t(92,138,'Y',5,7)
 s+=t(119,63,'Distances to X / Y; choice',79,8)
 for i,(dx,dy,vote) in enumerate([(2,8,'X'),(1,7,'X'),(3,3,'Tie'),(6,0,'Y'),(8,2,'Y')]):
  s+=t(121,77+i*9,rf'V{i+1}: {dx} / {dy} $\to$ {vote}',76,9)
 s+=tally(122,127,['X','Y','Tie'],[['V1','V2'],['V4','V5'],['V3']],1.15)
 s+=t(119,162,'Tied vote: 2 to 2; V3 in Tie.',79,9)
 s+=problem(1,176,'Use these five favorites. Find a location that wins a vote against every different location on the line.')
 s+=numberline(27,231,160,[0,2,4,7,10])+t(18,250,'Your location:',180,11)
 page('Grades 3--5','W87-L-v1',s)
 s=problem(2,30,'Find a location that beats every other location for each set of five favorites. Voters sharing a favorite still get one vote each.')
 for y,fs in [(110,[0,0,0,8,10]),(177,[1,4,4,4,9]),(244,[0,1,6,9,10])]:
  s+=numberline(27,y,160,fs)+t(20,y-43,r'Winning location: \rule{25mm}{0.3pt}',100,11)
 page('Grades 3--5','W87-L-v1',s)
 s=problem(3,30,'Put five favorites anywhere on the numbered ticks. Count all five markers, even when some share a place. Does the third favorite from the left always beat every different location? Show why, or find a set where it fails.')
 s+=numberline(27,103)+space(128,122)
 page('Grades 3--5','W87-L-v1',s)
 s=problem(4,30,'Use just four voters, with these favorites. Find every location that never loses against another location. Is there any location that beats every other one?')
 s+=numberline(27,110,160,[1,3,7,9])+numberline(27,157)+space(182,68)
 page('Grades 3--5','W87-L-v1',s)

def upper():
 P.clear()
 s=t(18,29,'Use the shared card-voting rules: each voter chooses the higher of the two available letters. The first winner faces the waiting letter. Cards stay unchanged.',size=11)
 s+=problem(1,52,'Can changing the waiting letter change the knockout winner for either set of cards? Explain how to tell from the pair votes, without playing every knockout.')
 s+=cards(29,91,['ABC','ACB','BAC'],43,52,9)+cards(29,160,['ACB','CBA','BAC'],43,52,9)+space(226,25)
 page('Grades 4--5','W87-U-v1',s)
 s=t(18,29,'A nearer letter ranks higher; equal distances make a tie, not a strict ranking. In this problem letters and favorites may be anywhere on a straight line.',size=11)
 s+=t(18,49,'Fixed locations',65,9)+numberline(23,72,52,[1],[('D',0),('E',4),('F',9)],True)
 s+=t(89,49,'From the same favorite',59,9)+t(90,61,r'D: 1 step\\E: 3 steps\\F: 8 steps',50,11)+card(159,49,'DEF','V1',25,47)
 s+=problem(2,110,'Could these three cards come from distance choices on one line? Put A, B and C at different places and choose a favorite for each voter, or explain why it cannot be done.')
 s+=cards(29,142,['ABC','BCA','CAB'],43,44,9)
 s+=line(23,210,193,210)+t(18,194,'Favorite markers above; letter tiles below',180,10)+space(225,26)
 page('Grades 4--5','W87-U-v1',s)

def materials():
 P.clear()
 s=t(18,29,r'Cut on outlines. Print at actual size (100\%).',size=11)+cards(25,43,['ABC','BCA','CAB'],45,80,11)
 for i,a in enumerate('AABBCC'):s+=box(21+i*29,139,28,28,a,23)
 for i in range(5):s+=circle(34+i*35,189,9,'V'+str(i+1),13)
 s+=line(23,229,123,229)+line(23,226,23,232)+line(123,226,123,232)+t(23,236,'100 mm scale check',140,10)
 page('Materials','W87-M-v1',s)
 for group in range(2):
  s=t(18,29,'Cut on outlines. One set of three blank ranking cards.',size=11)+cards(25,48,['   ']*3,45,80,11)
  # supplemental letter strips for ordinary reusable slips; no count substitution for real cards
  for row in range(3):
   for col,a in enumerate('ABCABC'):s+=box(25+col*27,155+row*27,21,21,a,19)
  page('Materials','W87-M-v1',s)
 s=t(18,29,'Keep these mats whole. Label the first two wells with the current option tiles, or with the separate X/Y tally labels for line votes.',size=11)
 s+=box(23,43,170,90)
 for j,lab in enumerate(['Option','Option','Tie']):
  xx=25+j*55
  s+=box(xx,77,54,54)
  if j<2:s+=box(xx+12,45,30,30,'Option',9)
  else:s+=t(xx+2,61,lab,50,9)
  for dx,dy in [(11,11),(43,11),(27,27),(11,43),(43,43)]:
   s+=circle(xx+dx,77+dy,9,'',8)
 s+=box(20,147,175,100)
 s+=box(25,154,61,39,'First pair',9)+box(92,154,33,39,'Waiting',9)+box(162,154,29,85,'Out',9)
 s+=box(25,200,33,39,'First winner',9)+box(63,200,61,39,'Final pair',9)+box(129,200,29,39,'Winner',9)
 page('Materials','W87-M-v1',s)
 s=t(18,29,'Keep the board whole. Favorite markers stay on their own lanes; proposal markers go below the line.',size=11)
 # Board: five lanes precisely aligned to the 16mm tick spacing.
 for i in range(5):
  yy=60+i*19
  s+=t(18,yy-6,'V'+str(i+1),12,8)+line(33,yy,193,yy)
  for j in range(11):s+=line(33+16*j,yy-2,33+16*j,yy+2)
 s+=numberline(33,153,160)+t(18,173,'Proposals X and Y',180,9)
 s+=t(18,184,'Cut the pieces below. Keep proposals on the board while voting.',180,9)
 for i in range(5):s+=circle(35+i*34,203,6.5,'V'+str(i+1),9)
 s+=t(30,217,'Proposal markers',85,9)+t(126,217,'Tally labels',68,9)
 s+=box(126,227,23,23,'X',18)+box(162,227,23,23,'Y',18)
 s+=box(42,229,13,13)+t(45,230,'X',10,12)
 s+=r'\draw (90,226)--(99,235)--(90,244)--(81,235)--cycle;'+t(87,230,'Y',10,12)
 page('Materials','W87-M-v1',s)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--work',type=Path,required=True);args=ap.parse_args()
 args.out.mkdir(parents=True,exist_ok=True);args.work.mkdir(parents=True,exist_ok=True)
 tex=shutil.which('pdflatex') or '/Library/TeX/texbin/pdflatex'
 env=dict(os.environ,SOURCE_DATE_EPOCH='1704067200',FORCE_SOURCE_DATE='1',TZ='UTC')
 for name,fn in [('shared',shared),('line',line_visit),('upper',upper),('materials',materials)]:
  fn();src=args.work/(name+'.tex');doc(src)
  cp=subprocess.run([tex,'-interaction=nonstopmode','-halt-on-error','-output-directory',str(args.work),str(src)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  if cp.returncode: print(cp.stdout);raise SystemExit(cp.returncode)
  subprocess.run([tex,'-interaction=nonstopmode','-halt-on-error','-output-directory',str(args.work),str(src)],env=env,stdout=subprocess.DEVNULL,check=True)
  shutil.copyfile(args.work/(name+'.pdf'),args.out/(name+'.pdf'))
  print(name,len(P),'pages')
if __name__=='__main__':main()
