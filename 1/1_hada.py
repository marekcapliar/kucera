import tkinter as tk


def move_up(e):
    global vector
    vector = [0, -1]

def move_left(e):
    global vector
    vector = [-1, 0]

def move_down(e):
    global vector
    vector = [0, 1]

def move_right(e):
    global vector
    vector = [1, 0]

def speed_up(e):
    global speed
    if speed > 10:
        speed -= 10

def speed_down(e):
    global speed
    speed += 10

def speeder(e):
    global speed
    if speed <= 10:
        speed = 200
    else:
        speed -= 10

def mover():
    global vector, head, snake, speed
    canvas.create_rectangle(head[0], head[1], head[0] + 1, head[1] + 1, fill='black')
    head[0] += vector[0]
    head[1] += vector[1]
    if head in snake:
        canvas.create_text(500//2, 10, text='prehral si')
        return
    snake.append([head[0], head[1]])
    canvas.after(speed, mover)


root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

speed = 100
vector = [0, -1]
head = [500//2, 500//2]
snake = [[500//2, 500//2]]
root.bind('w', move_up)
root.bind('a', move_left)
root.bind('s', move_down)
root.bind('d', move_right)
root.bind('k', speed_up)
root.bind('l', speed_down)
root.bind('<space>', speeder)
mover()

root.mainloop()