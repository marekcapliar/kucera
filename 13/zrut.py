import tkinter as tk
from random import randrange


def create_eater():
    eater = canvas.create_oval(10, 10, BALL_DIAMETER + 10, BALL_DIAMETER + 10, fill="blue", tags="eater")
    return eater


def apple_create(n):
    max_width = WIDTH - BALL_DIAMETER
    max_height = HEIGHT - BALL_DIAMETER
    apples = []
    no_go = canvas.coords(eater)
    for i in range(n):
        x = randrange(0, max_width)
        y = randrange(0, max_height)
        while x <= no_go[2] and y <= no_go[3]:
            x = randrange(0, max_width)
            y = randrange(0, max_height)
        apples.append(canvas.create_oval(x, y, x + BALL_DIAMETER, y + BALL_DIAMETER, fill='red'))
    return apples


def setup(n):
    global eater, apples, vector
    eater = create_eater()
    apples = apple_create(n)
    mover()


def mover():
    global vector, eater, apples
    canvas.move(eater, vector[0], vector[1])
    eater_coord = canvas.coords(eater)
    overlap_with_eater = canvas.find_overlapping(eater_coord[0], eater_coord[1], eater_coord[2], eater_coord[3])
    if len(overlap_with_eater) > 1:
        for i in overlap_with_eater[1:]:
            canvas.delete(i)
            apples.pop(apples.index(i))
    if len(apples) == 0:
        canvas.create_text(WIDTH//2, HEIGHT//2, text='END', font="Helvetica 30 bold", fill='red', anchor='center')
        return
    canvas.after(2, mover)


def move_up(e):
    global vector
    vector = [0, -1]


def move_down(e):
    global vector
    vector = [0, 1]


def move_right(e):
    global vector
    vector = [1, 0]


def move_left(e):
    global vector
    vector = [-1, 0]


root = tk.Tk()

WIDTH = 500
HEIGHT = 500
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg = 'white')
canvas.pack()
BALL_DIAMETER = 50
# vector = [x_move, y_move]
vector = [1, 0]

setup(15)

root.bind('<w>', move_up)
root.bind('<a>', move_left)
root.bind('<s>', move_down)
root.bind('<d>', move_right)

root.mainloop()