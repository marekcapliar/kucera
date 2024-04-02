import tkinter as tk, random


def zapalka(x, y):
    stick = canvas.create_line(x, y, x, y+100, width=5, fill='yellow')
    head = canvas.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown')
    return [stick, head]


def remove_zapalka(n):
    global matches
    print(n)
    for i in range(int(n)):
        canvas.delete(matches[-1][0])
        canvas.delete(matches[-1][1])
        matches = matches[:-1]
    player[0], player[1] = player[1], player[0]
    canvas.itemconfig(stats, text=f'taha hrac {player[0]}\npocet zapaliek: {len(matches)}')
    if len(matches) == 0:
        canvas.delete('all')
        canvas.create_text(650//2, 100, text=f"VYHRAL HRAC {player[1]}")


root = tk.Tk()

canvas = tk.Canvas(root, width=650, height=200)
canvas.pack()
player = [1, 2]
matches = []

for i in range(15):
    matches.append(zapalka(10 + 10*i + 10*(i+1), 50))

stats = canvas.create_text(650//2, 15, text=f'taha hrac {player[0]}\npocet zapaliek: {len(matches)}', anchor='center')

root.bind('1', lambda x: remove_zapalka(1))
root.bind('2', lambda x: remove_zapalka(2))
root.bind('3', lambda x: remove_zapalka(3))

root.mainloop()