def shadow_example(board,text,rules):
    s=[text(25,rules,12,15.5),text(49,'Example: two counters become row and column counts.',14,18)]
    s += [board(36,83,2,2,picture=['11','00']),board(128,83,2,2,[2,0],[1,1],['11','00'])]
    s += [r'\draw[->,>=stealth,line width=1pt] (92,105) -- (113,105);']
    # Sweeps run beside the discs and finish at the associated circled count.
    for y in (94,116):
        s += [fr'\draw[black!55,dashed,->,>=stealth,line width=.8pt] (131,{y-5.5}) -- (169,{y-5.5}) -- (174,{y});']
    for x in (139,161):
        s += [fr'\draw[black!55,dotted,->,>=stealth,line width=1pt] ({x-5.5},86) -- ({x-5.5},124) -- ({x},{129.4});']
    s += [r'\node[anchor=west,font=\fontsize{12}{15}\selectfont] at (128,153) {Across each row:};',r'\draw[black!55,dashed,->,>=stealth] (128,162) -- (150,162);',r'\node[anchor=west,font=\fontsize{12}{15}\selectfont] at (128,176) {Down each column:};',r'\draw[black!55,dotted,->,>=stealth,line width=1pt] (128,185) -- (150,185);']
    return s
