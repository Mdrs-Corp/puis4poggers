from testGagnant import check
from testValid import watPos
import pygame as pg
tableaux=[[0 for x in range(7)] for y in range(6)]

def draw(tabl):
    pos=[0,0]
    for y in tabl:
        for x in y:
            if x==1:
                pg.draw.rect(f,0xff0000,(pos[0]*100+5,pos[1]*100+5,90,90))
            elif x==2:
                pg.draw.rect(f,0xffff00,(pos[0]*100+5,pos[1]*100+5,90,90))
            pos[0]+=1

        pos[0]=0
        pos[1]+=1
  
    return True


pg.init()
f=pg.display.set_mode((700,600))
draw(tableaux)
'''
while inp!="q":
    j=1
    while j<3:
        inp=input('J'+str(j)+' '+juer[j-1]+': >')
        if inp=='q':
            breakpoint()
        if inp in '0123456789':
            inp=int(inp)
            y=watPos(inp,tableaux)
            if y!=-1:
                tableaux[y][inp]=j
                j+=1
                draw(tableaux)
                if (testGagnant(tableaux,inp,y)):
                    print('J'+str(j-1),'à gagné')'''
B=1
j=1
solutions=[]
ltry=[]
while B:
    pg.display.flip()
    f.fill(0)
    
    jean=list(pg.mouse.get_pos())
    jean=(jean[0]//100*100,jean[1]-50)
    if j==1:c=0xff0000
    else:c=0xffff00
    pg.draw.rect(f,c,(jean,(100,100)))
    draw(tableaux)
    for poss in solutions:
        pg.draw.line(f,0xffffff,(poss[0]*100+45,poss[1]*100+45),(poss[2]*100+45,poss[3]*100+45),10)
    for tr in ltry:
        pg.draw.rect(f,0x0000ff,tr)
    for event in pg.event.get():
        
        if event.type==pg.QUIT:
            pg.quit()
            B=0
        elif event.type==pg.KEYUP:
            if 1073741922==event.key:
                x=0
            else:
                x=event.key+1-1073741913
            if abs(x)<=6:
                y=watPos(x,tableaux)
                if y!=-1:
                    tableaux[y][x]=j
                    if (check(x,y,tableaux)):
                        print('J'+str(j),'à gagné')
                j+=1
                j=(j-1)%2+1
        elif event.type==pg.MOUSEBUTTONUP:
            if event.button==1:
                x=event.pos[0]//100
                if abs(x)<=6:
                    y=watPos(x,tableaux)
                    if y!=-1:
                        tableaux[y][x]=j
                        poss=check(x,y,tableaux)
                        if poss[4]=='found':
                            solutions.append(poss)
                        else:
                            ltry=[]
                            for pos in poss:
                                ltry.append((pos[0]*-100+5,pos[1]*100+5,90,90))
                            
                    j+=1
                    j=(j-1)%2+1
            
      
  
    
    
