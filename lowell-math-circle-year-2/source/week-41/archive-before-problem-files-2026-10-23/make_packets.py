from common import *
LETTERS=[['A','B','C'],['D','H','E'],['F','G','I']]
def tile(x,y,s,portals=True,all_letters=True,home=True,fs=11):
 out=rf'\draw[line width=.9pt] ({x},{y}) rectangle ++({s},{s});'+'\n'
 for k in [1,2]:out+=line(x+k*s/3,y,x+k*s/3,y+s,'gray!50,line width=.4pt')+line(x,y+k*s/3,x+s,y+k*s/3,'gray!50,line width=.4pt')
 for r in range(3):
  for c in range(3):
   if all_letters or (home and r==c==1):
    out+=lab(x+(c+.5)*s/3,y+(r+.5)*s/3-4,LETTERS[r][c],fs)
    out+=rf'\fill[gray] ({x+(c+.5)*s/3},{y+(r+.5)*s/3}) circle (.55);'+'\n'
 if portals:
  for xx in [x,x+s]:
   out+=rf'\draw[fill=white,line width=.7pt] ({xx},{y+s*.18}) circle (1.7);'+'\n'
   out+=line(xx,y+s*.77,xx,y+s*.61,'-{Stealth[length=2.4mm]},line width=1.3pt')
  for yy in [y,y+s]:
   xx=x+s*.18
   out+=rf'\draw[fill=white,line width=.7pt] ({xx},{yy-1.8})--({xx+1.8},{yy})--({xx},{yy+1.8})--({xx-1.8},{yy})--cycle;'+'\n'
   out+=line(x+s*.61,yy,x+s*.77,yy,'-{Stealth[length=2.4mm]},line width=1.3pt')
 return out

def tiled(x,y,s,coords=False):
 out=''
 for r in range(3):
  for c in range(3):
   out+=tile(x+c*s,y+r*s,s,False,False,True,10 if s>40 else 8)
   if coords:out+=lab(x+(c+.5)*s,y+(r+1)*s-4,f'$({c-1},{1-r})$',9)
 out+=rf'\draw[line width=1.7pt] ({x+s},{y+s}) rectangle ++({s},{s});'+'\n'
 if not coords:out+=lab(x+1.5*s,y+1.88*s,'original',9 if s>40 else 7)
 return out

def arrtrip(x,y,w,s,size=15):return text(x,y,w,'$'+r'\;'.join({'R':r'\rightarrow','L':r'\leftarrow','U':r'\uparrow','D':r'\downarrow'}[c] for c in s)+'$',size)
def example():
 s=lab(41,62,'input',10)+lab(88,62,'process',10)+lab(151,62,'output',10)
 s+=tile(17,73,48,True,True,True,9)
 # H -> E -> D on quotient, paired with a continuous path in two copies.
 s+=line(41,97,65,97,'-{Stealth[length=2mm]},blue!65!black,line width=1.1pt')+line(17,97,25,97,'-{Stealth[length=2mm]},blue!65!black,line width=1.1pt')
 s+=text(73,80,29,'two steps right',10)
 s+=tile(106,73,45,False,True,True,9)+tile(151,73,45,False,True,True,9)
 s+=line(128.5,95.5,158.5,95.5,'-{Stealth[length=2mm]},blue!65!black,line width=1.1pt')
 s+=lab(128.5,125,'original copy',9)+lab(173.5,125,'next copy',9)
 return s


def slide_example(y):
 out=''
 for x,title,way in [(23,'input',0),(144,'output',1)]:
  out+=lab(x+24,y-7,title,10)+blank(x,y,48,48)
  out+=line(x+24,y,x+24,y+48,'gray!50')+line(x,y+24,x+48,y+24,'gray!50')
  # These are the lower-left four cells of the same portal map.
  for k,xx,yy in [('D',x+12,y+12),('H',x+36,y+12),('F',x+12,y+36),('G',x+36,y+36)]:
   out+=lab(xx-5,yy-5,k,11)+rf'\fill ({xx},{yy}) circle (.7);'+'\n'
  path=[(x+12,y+36),(x+36,y+36),(x+36,y+12)] if way==0 else [(x+12,y+36),(x+12,y+12),(x+36,y+12)]
  out+=rf'\draw[-{{Stealth[length=2.5mm]}},blue!65!black,line width=1.4pt] '+'--'.join(f'({a},{b})' for a,b in path)+';\n'
 out+=line(82,y+19,132,y+19,'{Stealth[length=2.5mm]}-{Stealth[length=2.5mm]},line width=.8pt')
 out+=text(82,y+25,52,'slide through the squares',10)
 return out

for band in ['k-1','grades-2-3','grades-4-5']:
 pages=[]
 shared='One arrow moves to the center of the next small square. Right meets left at the same height; top meets bottom at the same place across. Keep moving in the arrow direction. Repeated copies continue beyond the page.'
 s=text(16,26,180,shared,12)+example()
 q='Start at H for each trip. Predict where it ends, then try it with your pawn.'
 s+=problem(1,142,q,band)+tile(20,177,75,True,True,True,14)
 for j,rt in enumerate(['RRD','UU','LD','UURR']):
  s+=arrtrip(113,177+20*j,62,rt)+line(175,183+20*j,195,183+20*j,'gray')
 pages.append(s)
 if band=='k-1':q='Start at H. Find every square you can reach in exactly two steps.'
 elif band=='grades-2-3':q='Find different trips from H back to H using exactly three steps, then exactly six steps. Draw or replay as many as you can.'
 else:q='Make four different trips from H back to H. Choose trips whose replays finish in different copies of H on the repeated map.'
 s=problem(2,27,q,band)+tile(18,71,180,True,True,True,15)
 pages.append(s)
 if band=='k-1':
  s=problem(3,27,'Find trips from H back to H with each number of steps. Look for more than one trip on each map.',band)
  for j,n in enumerate([2,3,4,5]):
   xx=23+(j%2)*94;yy=79+(j//2)*93
   s+=lab(xx+36,yy-10,f'{n} steps',13)+tile(xx,yy,72,True,True,True,11)
 elif band=='grades-2-3':
  s=problem(3,27,'Replay each trip on these copies, starting at the original H. Mark the copy where each trip finishes.',band)
  for j,rt in enumerate(['RRR','UUU','RRRUUU','RRLL']):s+=arrtrip(18+(j%2)*93,49+(j//2)*10,90,rt,12)
  s+=tiled(18,75,60)
 else:
  s=problem(3,27,'The original copy is (0,0). A full copy is three small-cell steps wide. One copy right adds 1 to the first number; one copy up adds 1 to the second. Find the finishing copy for each trip from H.',band)
  for j,rt in enumerate(['RRRUUU','UUURRR','RRLL','RRRUUULLLDDD']):s+=arrtrip(18+(j%2)*93,51+(j//2)*10,93,rt,11)
  s+=tiled(18,75,60,True)
 pages.append(s)
 if band=='k-1':
  s=problem(4,27,'Put one pawn on H and one on E. Give both pawns the same arrow steps; can you make them trade places?',band)+tile(18,71,180,True,True,True,15)

 elif band=='grades-2-3':
  s=problem(4,27,'Compare these two trips from H. Do they finish at the same place on the portal map and in the same copy on the repeated map?',band)
  s+=arrtrip(20,64,81,'RRRUUU',13)+arrtrip(116,64,81,'RURURU',13)
  s+=tiled(20,88,25)+tiled(116,88,25)+blank(16,185,180,69)
 else:
  s=text(16,25,180,'Journeys may move through the squares and cross themselves. Keep the start and finish of the whole journey at H, and keep its starting copy fixed. Add or erase two consecutive steps along the same segment in opposite directions. Within a journey, replace two adjacent sides of a square of cell centers by its other two sides, in either direction and any rotation.',11)
  s+=slide_example(80)
  s+=problem(4,145,'Use tracing paper on the repeated map from page 3. Which trip can shrink all the way to staying at H? Show changes to the whole trip.',band)
  s+=arrtrip(19,176,180,'RRRUUULLLDDD',14)+arrtrip(19,190,180,'RRR',14)
  s+=problem(5,217,'Change the first trip into the second using the allowed moves. Keep the same starting copy.',band)
  s+=arrtrip(19,245,81,'RRRUUU',13)+arrtrip(116,245,81,'UUURRR',13)
 pages.append(s)
 if band=='grades-2-3':
  s=problem(5,27,'Make a trip that visits another copy and finishes at the original H. Can you make one that visits both a copy above and a copy to the right?',band)
  s+=tiled(18,73,60)
  pages.append(s)
 elif band=='grades-4-5':
  s=problem(6,27,'When can two trips from H back to H be changed into each other? Explain what their finishing copies decide, using the repeated map. Add copies if your journey leaves the page.',band)
  s+=tiled(18,73,60,True)
  pages.append(s)
 write(41,'Portals',band,pages)
