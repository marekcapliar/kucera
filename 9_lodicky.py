import tkinter as tk
import random


def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)


def setup():
    for i in range(15):
        lodicka(20, i * 40 + 40)
        lode.append(1 + 2 * i)
    canvas.create_line(650, 0, 650, 800, fill='red')


def start(e):
    global starter
    if starter:
        mover()
        starter = False


def mover():
    global step, first, counter
    for i, j in enumerate(lode):
        line_coord = canvas.coords(j)
        move = random.randint(1, 10)
        canvas.delete(j)
        canvas.delete(j+1)
        lodicka(line_coord[0] + move, line_coord[1])
        if first:
            lode[i] += 31
        else:
            lode[i] += 30
        if len(canvas.find_overlapping(650, 0, 650, 800)) > 1:
            winner.append((j - 30 * counter - 1)//2 + 1)
        if len(canvas.find_overlapping(700, 0, 700, 800)):
            canvas.create_text(350, 400, text='Vyhrala lodicka: ' + str(winner[0]), font=('Helvetica', '30', 'bold'), fill='red', anchor=tk.CENTER)
            return
    first = False
    counter += 1
    canvas.after(100, mover)


root = tk.Tk()
canvas = tk.Canvas(root, width=700, height=800)
canvas.pack()
lode = []
step = 0
winner = []
first = True
starter = True
counter = 0
setup()

canvas.bind('<Button-1>', start)

root.mainloop()