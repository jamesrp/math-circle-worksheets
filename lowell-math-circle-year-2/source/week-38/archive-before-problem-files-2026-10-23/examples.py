def edge_groups_example(text,lab,line):
    s=text(16,60,180,'Dots on one edge go in one ring.',14)
    s+=lab(58,82,'flat paper washer',11)+lab(153,82,'dot groups',11)
    s+=r'\fill[gray!10] (58,121) circle (29);\fill[white] (58,121) circle (13);'+'\n'
    s+=r'\draw[line width=1.2pt] (58,121) circle (29);\draw[dashed,line width=1.2pt] (58,121) circle (13);'+'\n'
    s+=r'\draw[-{Stealth[length=2.2mm]},line width=1.2pt] (58,92) arc[start angle=-90,end angle=0,radius=29];'+'\n'
    s+=r'\draw[dashed,-{Stealth[length=2.2mm]},line width=1.2pt] (58,108) arc[start angle=-90,end angle=-180,radius=13];'+'\n'
    for x,y,ch,lx,ly in ((58,92,'P',58,87),(87,121,'Q',94,121),(58,134,'R',58,126)):
        s+=fr'\fill ({x},{y}) circle (1.5);'+'\n'+lab(lx,ly,ch,11)
    s+=line(102,121,121,121,'-{Stealth[length=2.6mm]},line width=.9pt')
    s+=r'\draw[line width=.7pt] (153,108) ellipse (25 and 12);\draw[line width=.7pt] (153,143) ellipse (16 and 12);'+'\n'
    for x,y,ch in ((145,110,'P'),(161,110,'Q'),(153,146,'R')):
        s+=fr'\fill ({x},{y}) circle (1.5);'+'\n'+lab(x,y-6,ch,11)
    s+=line(27,164,44,164,'line width=1.2pt')+lab(57,164,'outer trip',10)
    s+=line(94,164,111,164,'dashed,line width=1.2pt')+lab(124,164,'inner trip',10)
    s+=text(16,181,180,'The rings record which dots share an edge.',12)
    return s
