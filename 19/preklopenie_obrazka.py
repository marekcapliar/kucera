import tkinter as tk


def draw_picture(pic):
    for y, i in enumerate(pic):
        for x, j in enumerate(i):
            match j:
                case '1':
                    canvas.create_rectangle(x*ZOOM, y*ZOOM, x*ZOOM+ZOOM, y*ZOOM+ZOOM, fill='black')


def switch_image():
    global switched, WIDTH
    canvas.delete('all')
    if switched:
        draw_picture(picture)
        switched = False
    else:
        switched = True
        for y, i in enumerate(picture):
            for x, j in enumerate(i):
                match j:
                    case '1':
                        canvas.create_rectangle(WIDTH-x*ZOOM, y*ZOOM, WIDTH-x*ZOOM-ZOOM, y*ZOOM+ZOOM, fill='black')


fr = open('kucera/19/preklopenie_obrazka.txt', 'r', encoding='UTF-8')
WIDTH, HEIGHT = fr.readline().split(' ')
WIDTH, HEIGHT = int(WIDTH), int(HEIGHT)
picture = fr.readlines()
picture = [i.split(' ') for i in picture]

root = tk.Tk()

ZOOM = 5
WIDTH, HEIGHT = WIDTH*ZOOM, HEIGHT*ZOOM
switched = False
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()

button = tk.Button(root, text="Preklop obrazok", command=switch_image)
button.pack()

draw_picture(picture)

root.mainloop()