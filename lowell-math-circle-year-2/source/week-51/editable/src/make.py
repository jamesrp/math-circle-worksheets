from draw import *
BS=chr(92)
def ruler(x,y,n=16,u=10,labels=True):
    s=line(x,y,x+n*u,y)
    for i in range(n+1):
        s+=line(x+i*u,y-2,x+i*u,y+2)
        if labels:s+=label(x+i*u,y+6,str(i),9)
    return s

def band(x,y,L,U,name,n=16,u=10,ht=12):
    s=rect(x,y,L*u,ht,'fill=gray!8')+rect(x+L*u,y,(U-L)*u,ht,'fill=gray!32')
    s+=line(x,y-2,x,y+ht+2,'line width=1.1pt')
    s+=label(x+(L+U)*u/2,y+ht/2,'?',12)
    s+=text(x,y-10,f'{name}: {L} to {U} units',w=min(180-x,n*u+10),size=11)
    s+=ruler(x,y+ht+6,n,u)
    return s

def joins(x,y,a,b,u=10):
    return rect(x,y,a*u,9,'fill=gray!12')+label(x+a*u/2,y+4.5,'A',9)+rect(x+a*u,y,b*u,9,'fill=gray!30')+label(x+(a+b/2)*u,y+4.5,'B',9)

def recipe(x,y,letters,nums):
    s=''
    for i,(l,num) in enumerate(zip(letters,nums)):
        s+=rect(x+i*50,y,50,16,'fill=gray!12' if l in ('A','B') else '')
        s+=label(x+i*50+25,y+8,l if num is None else f'{num} units',12)
    return s

def comparison(y,same=True):
    s=line(12,y-3,12,y+28,'line width=1pt')
    for yy,length,l,extra in [(y,50,'A',4),(y+16,50 if same else 40,'A' if same else 'B',1)]:
        s+=rect(12,yy,length,11,'fill=gray!25' if l=='A' else 'fill=gray!8')
        s+=label(12+length/2,yy+5.5,l,11)
        s+=rect(12+length,yy,extra*10,11,'fill=white,line width=1pt')
        s+=label(12+length+extra*5,yy+5.5,str(extra),11)
    s+=label(6,y+12,'0',10)
    s+=text(118,y,'Smallest gap: '+BS+'rule{12mm}{.3pt}'+BS+BS+'[4mm]Largest gap: '+BS+'rule{12mm}{.3pt}',w=65,size=11)
    return s

def intro():
    s=text(0,0,'A hidden end can be anywhere in its gray band, including the edges. Each trial may use new lengths. Join strips end to end from 0, with no gap or overlap.',size=12)
    s+=band(6,37,2,3,'A',7,10,10)+band(6,78,1,2,'B',7,10,10)
    s+=line(81,61,96,61,'-{Stealth[length=2mm]}')+band(104,45,3,5,'A + B',7,10,10)
    s+=joins(106,80,2,1)+label(149,84.5,'3',10)
    s+=joins(106,97,3,2)+label(169,101.5,'5',10)
    return s

for bandname,name in [('K--1','k-1'),('Grades 2--3','grades-2-3'),('Grades 4--5','grades-4-5')]:
    k=bandname=='K--1';upper=bandname=='Grades 4--5';pages=[]
    p=intro()+prob(1,'Make the shortest and longest joins with these strips. Can you make a join ending exactly at 8?' if k else 'Find the tightest guaranteed range for the join. Someone claims it must end between 8 and 9; build allowed strips that defeat that claim.',119,size=14 if k else 13)
    p+=band(12,164,4,6,'A')+band(12,204,3,4,'B')
    pages.append(p)
    p=prob(2,'Try A with B, C with D, and E with F; which pairs always reach 8? Let a friend try to defeat your choices.' if k else 'Try only A with B, C with D, and E with F. Choose a pair whose join always reaches 8 and fits within 10. For each rejected pair, let a partner defeat one promise with allowed lengths.',size=14 if k else 13)
    for y,vs in [(49,[(4,6,'A'),(3,4,'B')]),(111,[(4,5,'C'),(4,5,'D')]),(173,[(6,8,'E'),(2,4,'F')])]:
        p+=rect(0,y-15,185,51,'rounded corners=2mm,gray!55')
        for x,(L,U,l) in zip([5,101],vs):p+=band(x,y,L,U,l,8,10,12)
    p+=text(8,219,'Reaching 8 includes ending at 8.' if k else 'Reaching 8 includes ending at 8. Fitting within 10 includes ending at 10.',w=178,size=11)
    pages.append(p)
    if k:
        p=prob(3,'Pick a card for B so the join always reaches 7 and fits within 9. Try to break your choice with different allowed strips.',size=14)
        p+=band(12,48,3,4,'A')
        for y,L,U in [(99,3,4),(144,4,5),(189,5,6)]:p+=band(12,y,L,U,'B')
    else:
        p=prob(3,'A is 3 to 4 units long. Make a range card for B so every join reaches 7 and fits within 9. Make B\'s allowed range as wide as possible, and explain why it cannot be wider.')
        p+=band(12,50,3,4,'A')
        p+=text(12,97,'B:',size=13)+ruler(12,114)
        p+=rect(12,145,90,14)+rect(82,145,20,14,'fill=gray!25')+label(12,165,'0',10)+label(82,165,'7',10)+label(102,165,'9',10)
        p+=prob(4,'A different pair has A from 4 to 6 and B from 3 to 4. You may learn one exact length. Which strip would you uncover to leave the narrowest guaranteed range for the join?',190)
    pages.append(p)
    n=4 if k else 5
    p=prob(n,'Find how small and how big each end gap can be. Start at 0 and keep A unchanged within each comparison; B may vary separately.' if k else 'Compare the gaps between the right ends of these joins, starting at 0. Repeated A means the same unchanged length; B may vary separately. Find the tightest range for each gap.',size=14 if k else 13)
    p+=band(12,40,4,6,'A')+band(12,79,4,6,'B')
    p+=text(12,113,'One possible setting; the white pieces are exactly 4 and 1 units long.',size=10)
    p+=comparison(126,True)+ruler(12,161)
    p+=comparison(188,False)+ruler(12,223)
    pages.append(p)
    n=5 if k else 6
    p=prob(n,'Put both starts at 0. Make the biggest gap between the ends, then the smallest.' if k else 'Align both starts at 0. Find the tightest guaranteed range for the gap between the ends. Build lengths that show neither bound can be improved.',size=14 if k else 13)
    p+=band(12,52,7 if k else 13,9 if k else 15,'long strip')+band(12,108,5 if k else 10,6 if k else 12,'short strip')
    p+=prob(n+1,'Using these two strips, make a gap of 3 in two different ways.' if k else 'Someone subtracts the two middle values and announces one exact gap. Can you choose allowed strips that show why this is unsafe?',167,size=14 if k else 13)
    p+=ruler(12,216)
    pages.append(p)
    n=7 if k else 8
    if not upper:
        p=prob(n,'A and B must fill 9 units exactly. Find every pair of whole-unit lengths that fits both cards.',size=14 if k else 13)
        p+=band(12,47,4,6,'A')+band(12,91,3,5,'B')
        for y in [135,170,205]:
            p+=rect(12,y,90,13)+ruler(12,y+18,9)
    else:
        p=prob(8,'A is 7 to 10 units and B is 3 to 7 units. You learn that their join is exactly 12 units. Align their starts at 0. Find the smallest and largest possible gap between their ends.')
        p+=band(12,53,7,10,'A')+band(12,95,3,7,'B')
        p+=rect(12,142,120,14)+label(72,162,'A + B = 12 units',12)
        p+=prob(9,'Join A (4 to 6 units) to B (3 to 4 units), then remove that very same A. Someone uses the join\'s range and A\'s range separately to claim the remainder could be 1 to 6 units. Is that the tightest range? Explain with the pieces.',185)
    pages.append(p)
    write(name,51,'Honest measurement ranges',bandname,pages)
buildscript()
# Endpoint checks are algebraic deterministic bounds, not probabilities.
assert (4+3,6+4)==(7,10)
assert (13-12,15-10)==(1,5)
assert (7-6,9-5)==(1,4)
assert (4+4-(6+1),6+4-(4+1))==(1,5)
assert min(a-(12-a) for a in [7,9])==2 and max(a-(12-a) for a in [7,9])==6
assert [(a,9-a) for a in range(4,7) if 3<=9-a<=5]==[(4,5),(5,4),(6,3)]
(ROOT/'checks.txt').write_text('Joined 4..6 and 3..4: 7..10. Same A+4 versus A+1: gap 3; separate A,B each4..6: gap1..5. Long13..15 minus short10..12:1..5. Joint-length12 case A7..10 B3..7 narrows to A7..9, B3..5, gap2..6.\n')
