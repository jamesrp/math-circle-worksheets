from draw import *
from examples import height_example
intro=text(0,0,'Heights are whole numbers, including 0. Neighbors differ by at most 1. Black circles are fixed clues.',size=12)
intro+=height_example(text,label,line,rect,circle,hill)
for band,name in [('K--1','k-1'),('Grades 2--3','grades-2-3'),('Grades 4--5','grades-4-5')]:
    k=band=='K--1'; upper=band=='Grades 4--5'; pages=[]
    p=intro+text(0,80,r'\textbf{Problem 1:} '+('Make different landscapes with these clues.' if k else 'Make four different landscapes with these clues. Can the middle height be 0? Can it be 3?'),w=113,size=14 if k else 13)
    p+=hill(142,99,[1,3,2])+label(152,110,'jump too big',11)
    p+=board(40,118,5,4,{0:1,4:1})
    pages.append(p)
    p=prob(2,'Put the starred marker as high as you can, then as low as you can.' if k else 'Which heights can the starred marker have? Make a landscape for each possible height and explain why the other heights cannot work.',size=14 if k else 13)
    p+=board(40,50,5,4,{0:0,4:2},2)
    p+=prob(3,'Move the right clue to 4. Find every landscape that works.' if k else 'Keep the left clue at 0. Choose a height for the right clue that forces every marker. Find all such right-clue heights.',170,size=14 if k else 13)
    p+=text(40,197,'Shaded boxes are fixed clues.',w=140,size=11)
    p+=row(40,216,[0,None,None,None,4 if k else None],(0,4))
    pages.append(p)
    p=prob(4,'Which clues can go together? Build the ones that work.' if k else 'Decide which clue sets can be completed. Build the possible ones; explain what prevents the others.',size=14 if k else 13)
    for y,vs in [(36,[0,None,3,None,None]),(69,[3,None,None,None,0]),(102,[None,0,None,3,None])]: p+=row(35,y,vs,tuple(i for i,v in enumerate(vs) if v is not None))
    p+=board(35,151,5,3,dx=25,dy=20)
    pages.append(p)
    p=prob(5,'Make three different landscapes with these clues.' if k else ('Make one landscape that is as low as possible at every site, and one that is as high as possible at every site. Explain why no marker can go beyond yours.' if upper else 'Make a landscape with the fewest blocks, then one with the most blocks. Keep all three clues.'),size=14 if k else 13)
    p+=board(25,47,7,5,{0:1,4:3,6:1})
    p+=row(18,176,[None]*7,dx=23)+row(18,207,[None]*7,dx=23)
    pages.append(p)
    if k:
        p=prob(6,'Move one white marker one level up or down in its own column each turn, keeping the rule. Reach the second landscape in as few moves as you can.',size=14)
        p+=row(30,36,[1,2,1,2,1],(0,4),dx=25)+row(30,70,[1,0,0,0,1],(0,4),dx=25)
        p+=board(40,113,5,3,{0:1,4:1})
        p+=prob(7,'Replace the old clues with two new clues for a friend to solve.',206,size=14)
    elif not upper:
        p=prob(6,'Choose two clues on the seven-site board that force exactly one whole landscape. Then choose two clues that allow more than one. Let a partner solve both.')
        p+=board(25,48,7,6)
        p+=prob(7,'Two clues are 4 steps apart. One is height 1. Which heights for the other clue are possible? Explain a rule for clues any number of steps apart.',195)
    else:
        p=prob(6,'A single clue is fixed at height 2. The shaded marks show all allowed heights at nearby sites. Find the allowed heights at sites 0 and 6.')
        # example explicitly shows permitted single-clue bands, not combined envelopes
        p+=board(25,48,7,5,{3:2})
        for i in [1,2,4,5]:
            for h in range(max(0,2-abs(i-3)),min(5,2+abs(i-3))+1):p+=circle(25+22*i,48+(5-h)*20,3,'fill=gray!45')
        p+=prob(7,'A row has at least one clue. Suppose every pair of clues differs by no more than the steps between them. Must the whole row be fillable? Give a construction that always works, or a set of clues that defeats the claim.',181)
    pages.append(p)
    write(name,47,'Gentle-step landscapes',band,pages)
buildscript()
# Independent finite checks for the concrete instances.
from itertools import product
sol=[s for s in product(range(6),repeat=7) if s[0]==1 and s[4]==3 and s[6]==1 and all(abs(a-b)<=1 for a,b in zip(s,s[1:]))]
assert len(sol)==10
assert tuple(min(s[i] for s in sol) for i in range(7))==(1,0,1,2,3,2,1)
assert tuple(max(s[i] for s in sol) for i in range(7))==(1,2,3,4,3,2,1)
(ROOT/'checks.txt').write_text('Seven-site instance: 10 completions; coordinatewise minima and maxima verified.\n')
