case=[
[0,0,0,0,1,0,0],
[0,0,0,0,1,0,0],
[0,0,0,0,1,0,0],
[0,0,0,0,1,0,0],
[0,0,0,0,1,0,0],
[0,0,0,0,1,1,1]]

def watPos(coup,tab):
    if coup>6 or coup<0:
        return -1
    lin=5
    while lin>=0:
        if tab[lin][coup]==0:
            return lin
        else:
            lin-=1
    return -1
    
