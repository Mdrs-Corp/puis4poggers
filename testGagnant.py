pll=[[0 for i in range(6)] for j in range(7)]
pll[0][0]=1
pll[1][1]=1
pll[2][2]=1
pll[3][3]=1

pll[0][5]=2
pll[1][5]=2
pll[2][5]=2
pll[3][5]=2

pll[6][5]=2
pll[6][4]=2
pll[6][3]=2
pll[6][2]=2

pll[6][0]=2
pll[5][1]=2
pll[4][2]=2
pll[3][3]=2
for gjhk in pll:
    print(gjhk)
def from_begin(x,y,pl=1,ls=pll):
    '''Trouve depuis un bout si y'a un puis4 quelque soit le sens'''
    for fd in [[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]:
        cx,cy=x+fd[0],y+fd[1]
        puis=1
        while cx>=0 and cy>=0 and cx<len(ls[0]) and cy<len(ls) and puis<5:
            
            if ls[cy][cx]==pl:
                puis+=1
                cx+=fd[0]
                cy+=fd[1]
                
            else:
                cx=-1 #quitter si ce n'est plus le player
                
        if puis==4:
            return True
    return False
def check(x,y,carte):
    '''aller chercher le bout de la ligne'''
    pl=carte[y][x]
    mvx,mvy=x,y
    l=[]
    for move in [[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]:
        while mvx>=0 and mvy>=0 and mvx<len(carte[0]) and mvy<len(carte):
            if carte[mvy][mvx]==pl:
                mvx+=move[0]
                mvy+=move[1]
            else:
                mvx=-1
        if from_begin(mvx,mvy,pl,carte):
            print('paths')
            return mvx,mvy,x,y,'found'
        else:
            l.append((mvx,mvy))
    return l
            
def testGagnant(pl,x,y):
    #verticale
    n=0
    for i in range(len(pl[x])-1):
        if abs(i-y)<4:
            if pl[x][i]==pl[x][i+1] and pl[x][i]!=0:
                n+=1
            else:
                n=0
        if n>2:
            return True
    #horizontale
    n=0
    for i in range(len(pl)-1):
        if abs(i-x)<4:
            if pl[i][y]==pl[i+1][y] and pl[i][y]!=0:
                n+=1
            else:
                n=0
        if n>2:
            return True
    #diagonale1
    n=0
    for i in range(len(pl)-1):
        for j in range(len(pl[0])-1):
            if abs(i-x)<4 and abs(j-y)<4:
                if i-x==j-y:
                    if pl[i][j]==pl[i+1][j+1] and pl[i][j]!=0:
                        n+=1
                    else:
                        n=0
            if n>2:
                return True
    #diagonale2
    for i in range(len(pl)-1):
        for j in range(1,len(pl[0])-1):
            if abs(i-x)<4 and abs(j-y)<4:
                if i-x==y-j:
                    if pl[i][j]==pl[i+1][j-1] and pl[i][j]!=0:
                        n+=1
                    else:
                        n=0
            if n>2:
                return True
    return False
