import tkinter as tk
from random import choice

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=500, bg='white')
canvas.pack()

colors = ['red', 'green', 'orange', 'blue', 'turquoise']
width = 300
height = 15
ux = 100
uy = 100
wires = []
explosion = 0
ftime = 100


def DrawWires():
    global wires, explosion
    for i in range(len(colors)):
        wires.append(canvas.create_rectangle(ux, uy+(i*height), ux+width, uy+height*(i+1), fill=colors[i]))
    explosion = choice(wires)
    print(explosion)


def clicker(e):
    global temp
    a = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if a[0] == explosion:
        vys = canvas.create_text(width//2, 250, text='vyhral si')
        temp = True
    else:
        canvas.delete('all')


def changer():
    global ftime
    ftime -= 1
    canvas.itemconfig(t, text=ftime)
    canvas.after(1000, changer)

canvas.bind('<Button-1>', clicker)
t = canvas.create_text(10,10,text=ftime)
changer()
DrawWires()
root.mainloop()