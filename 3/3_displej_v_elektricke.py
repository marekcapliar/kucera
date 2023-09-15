import tkinter as tk

def mover():
    global stop_id, LETTER_WIDTH, num_stop, check
    for i in stop_id:
        coords = canvas.coords(i)
        if coords[0] == LETTER_WIDTH//2:
            canvas.move(i, 19 * LETTER_WIDTH, 0)
        else:
            canvas.move(i, -LETTER_WIDTH, 0)
    if check == num_stop:
        canvas.after(500, mover)
    else:
        check = num_stop


def setup(stop):
    global LETTER_WIDTH, HEIGHT, stop_id
    letter = 0
    stop_id = []
    canvas.delete('all')
    # position = {}
    for i in stop:
        stop_id.append(canvas.create_text(letter * LETTER_WIDTH + LETTER_WIDTH//2, HEIGHT//2, text= i, font=('Helvetica', HEIGHT - 40), anchor=tk.CENTER, fill='red'))
        # position[stop_id[-1]] = letter
        letter += 1
    mover()


def next_station(e):
    global num_stop
    num_stop += 1
    setup(stop_list[num_stop])


root = tk.Tk()

HEIGHT = 100
LETTER_WIDTH = 60
WIDTH = 20 * LETTER_WIDTH
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

fr = open('3/zastavky.txt', 'r', encoding='utf-8')
stop_list = fr.readlines()
num_stop = 0
check = 0

setup(stop_list[num_stop])
print(stop_id)
root.bind('<Key>', next_station)

root.mainloop()