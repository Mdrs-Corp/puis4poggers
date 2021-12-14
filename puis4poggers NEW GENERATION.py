plato= [[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."]]
tour=0
nmj1=""
nmj2=""
lp=[]

def nomjoueur():
    global nmj1,nmj2
    nmj1=input("Quel est ton nom Joueur 1? ")
    nmj2=input("Quel est ton nom Joueur 2? ")
    while nmj1==nmj2:
        print("Nom déjà pris!")
        nmj2=input("Quel est ton nom Joueur 2? ")
    print(nmj1 + " tu es x, "+nmj2+" tu es o.")

def coloume():
    global nmj1,nmj2
    if tour%2==0:
        lol = input("Ou mettre le chton "+nmj1+"? (int entre 1 et 7) ")
    else:
        lol = input("Ou mettre le chton "+nmj2+"? (int entre 1 et 7) ")
    if lol.isdigit() and int(lol)>=1 and int(lol)<=7:
        return int(lol)-1
    return coloume()

def jouer():
    global plato
    global tour
    global lp
    col=coloume()
    lin=5
    while plato[lin][col]!=".":
        lin-=1
        if lin <0:
            print("colonne pleine")
            jouer()
            return
    if tour%2==0:
        plato[lin][col]="x"
        affichage()
        lp=[nmj1,lin,col]
        if fred()==True:
            print(nmj1 + " a gagné !")
            return True
    else:
        plato[lin][col]="o"
        affichage()
        lp=[nmj2,lin,col]
        if fred()==True:
            print(nmj2 + " a gagné !")
            return True
    tour+=1
    return False

def affichage():
    global plato
    mdrs=''
    for i in plato:
        for k in i:
            mdrs+=k
        mdrs+='\n'
    print(mdrs)

def fred():
    global plato,lp
    y=lp[1]
    x=lp[2]
    counter=1
    if lp[0]==nmj1:
        while x<7:
            if plato[y][x+1]=="x":
                x+=1
                counter+=1
            else:
                break
        x=lp[2]
        while x>=0:
            if plato[y][x-1]=="x":
                x-=1
                counter+=1
            else:
                break
        x=lp[2]
        if counter >=4:
            return True
        counter = 1
        while y<=4:
            if plato[y+1][x]=="x":
                y+=1
                counter+=1
            else:
                break
        y=lp[1]
        while y>=0:
            if plato[y-1][x]=="x":
                y-=1
                counter+=1
            else:
                break
        y=lp[1]
        if counter >=4:
            return True
        counter = 1
        while y<=4 and x<7:
            if plato[y+1][x+1]=="x":
                y+=1
                x+=1
                counter+=1
            else:
                break
        y=lp[1]
        x=lp[2]
        while y>=0 and x>=0:
            if plato[y-1][x-1]=="x":
                y-=1
                x-=1
                counter+=1
            else:
                break
        y=lp[1]
        x=lp[2]
        if counter >=4:
            return True
        counter =1
        while y>=0 and x<7:
            if plato[y-1][x+1]=="x":
                y-=1
                x+=1
                counter+=1
            else:
                break
        y=lp[1]
        x=lp[2]
        while y<=4 and x>=0:
            if plato[y+1][x-1]=="x":
                y+=1
                x-=1
                counter+=1
            else:
                break
        y=lp[1]
        x=lp[2]
        if counter>=4:
            return True
    else:
        while x<7:
            if plato[y][x+1]=="o":
                x+=1
                counter+=1
            else:
                break
        x=lp[2]
        while x>=0:
            if plato[y][x-1]=="o":
                x-=1
                counter+=1
            else:
                break
        x=lp[2]
        if counter >=4:
            return True
        counter = 1
        while y<=4:
            if plato[y+1][x]=="o":
                y+=1
                counter+=1
            else:
                break
        y=lp[1]
        while y>=0:
            if plato[y-1][x]=="o":
                y-=1
                counter+=1
            else:
                break
        y=lp[1]
        if counter >=4:
            return True
        counter = 1
        while y<=4 and x<7:
            if plato[y+1][x+1]=="o":
                y+=1
                x+=1
                counter+=1
            else:
                break
        y=lp[1]
        x=lp[2]
        while y>=0 and x>=0:
            if plato[y-1][x-1]=="o":
                y-=1
                x-=1
                counter+=1
            else:
                break
        y=lp[1]
        x=lp[2]
        if counter>=4:
            return True
        counter = 1
        while y>=0 and x<7:
            if plato[y-1][x+1]=="o":
                y-=1
                x+=1
                counter+=1
            else:
                break
        y=lp[1]
        x=lp[2]
        while y<=4 and x>=0:
            if plato[y+1][x-1]=="o":
                y+=1
                x-=1
                counter+=1
            else:
                break
        y=lp[1]
        x=lp[2]
        if counter>=4:
            return True
    return False

def game():
    nbtour=0
    nomjoueur()
    affichage()
    while jouer()==False:
        nbtour+=1
        
    













    
    
