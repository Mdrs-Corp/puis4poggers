import random
from testValid import watPos
plateaux=[[random.randrange(0,3) for x in range(7)] for y in range(6)]
import tkinter as tk

f=tk.Tk()
s=tk.Frame(f)
s.pack(expand=tk.YES)
c=tk.Canvas(f,width = 500,
            height = 500)
c.pack(expand=tk.YES)
size=50

def tket():
    coord=[0,0]
    for y in plateaux:
        for x in y:
            if x==1:
                c.create_rectangle(coord[0]*size, coord[1]*size, coord[0]*size+size, coord[1]*size+size,
                outline="#ff0000", fill="#05f")
            else:
                c.create_rectangle(coord[0]*size, coord[1]*size, coord[0]*size+size, coord[1]*size+size,
                outline="#000000", fill="#ffffff")
            coord[1]+=1
        coord[0]+=1
        coord[1]=0
tket()
f.bind('<KeyRelease>',lambda x:print(x.x//50,x.y//50))
f.mainloop()
