from testGagnant import testGagnant
import random
from testValid import watPos

#plateaux=[[random.randrange(0,3) for x in range(7)] for y in range(6)]
tableaux=[[0 for x in range(7)] for y in range(6)]
def draw(tabl):
    print(' '+'==='*(len(tabl)-1))
    for y in tabl:
        print('|',end='')
        for x in y:
            if x==1:
                print(u"\u25A0",end=' ')
            elif x==2:
                print("o",end=' ')
            else:
                print(' ',end=' ')

        print('|')
    print(' '+'==='*(len(tabl)-1))
    return True
inp=''
juer=[u"\u25A0",'o']
draw(tableaux)
while inp!="q":
    j=1
    while j<3:
        inp=input('J'+str(j)+' '+juer[j-1]+': >')
        if inp=='q':break
        if inp in '0123456789':
            inp=int(inp)
            y=watPos(inp,tableaux)
            if y!=-1:
                tableaux[y][inp]=j
                j+=1
                draw(tableaux)
                if (testGagnant(tableaux,inp,y)):
                    print('J'+str(j-1),'à gagné')
            else:
                print('Erreur fatale')
        else:
            print('Erreur fatale')

    
    
    
