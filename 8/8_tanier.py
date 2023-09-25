import tkinter as tk
import random


def setup():
    global crack
    for i, j in enumerate(tanier):
        id_tanier.append(canvas.create_oval(i*R+10*(i+1), 10, (R + 10)*(i+1), HEIGHT-10, fill='blue'))
        canvas.create_oval(i*R+10*(i+1) + 10, 20, (R + 10)*(i+1) - 10, HEIGHT-20, fill='blue')
        canvas.create_text(((i*R+10*(i+1))+((R + 10)*(i+1)))//2, HEIGHT//2, text=j, font=('Helvetica', str(R//3) , 'bold'), anchor=tk.CENTER, fill='white')
    crack = random.choice([*tanier])


def clicker(e):
    click = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if len(click) > 0:
        if click[0] in id_tanier:
            tanier_count[tanier[(click[0]-1)//3]] = tanier_count.get(tanier[(click[0]-1)//3], 0) + 1
            if tanier[(click[0]-1)//3] == crack:
                letters = ''
                for i in tanier_count:
                    if tanier_count[i]>1:
                        letters += i
                canvas.delete('all')
                canvas.create_text(WIDTH//2, HEIGHT//2, text='Gratulujem, oznacil si puknuty tanier', font=('Helvetica', str(R//3) , 'bold'), anchor= tk.CENTER, fill='blue')
                canvas.create_text(WIDTH//2, HEIGHT//2 + 30, text='Viackrat si klikol na taniere: ' + letters, font=('Helvetica', str(R//3) , 'bold'), anchor= tk.CENTER, fill='red')


root = tk.Tk()
R = 70
WIDTH = 10*R + 100
HEIGHT = R + 20
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
tanier = 'ABCDEFGHIJ'
id_tanier = []
tanier_count = {}
setup()

canvas.bind('<Button-1>', clicker)

root.mainloop()