import tkinter as tk


def open_file(file):
    krizovka = file.readlines()
    krizovka = [i.strip().split(' ') for i in krizovka]
    krizovka = [[int(i[0]), i[1]] for i in krizovka]
    return krizovka


def create_empty_krizovka(begin_x, krizovka):
    text_widgets = []
    square_size = 50
    y = 10
    largest_word_lenght = max([i[0] for i in krizovka]) - 1
    tajnicka_x = begin_x + largest_word_lenght * square_size
    for i in krizovka:
        tajnicka_place = i[0] - 1
        word = i[1]
        beginning = begin_x + tajnicka_x - square_size * tajnicka_place
        end = beginning + square_size * (len(word) - 1)
        for x in range(beginning, end + square_size, square_size):
            print(x//square_size, tajnicka_place)
            color = "grey" if x == beginning + tajnicka_place * square_size else "white"
            canvas.create_rectangle(x, y, x + square_size, y + square_size, fill=color)
            text_x = (x + x + square_size)//2
            text_y = (y + y + square_size)//2
            text_widgets.append(canvas.create_text(text_x, text_y, text=' ', font="Helvetica 30", anchor='center'))
        y += square_size
        print("new word")
    return text_widgets


def insert_words_to_tajnicka(text_widgets, krizovka):
    krizovka_str = ''.join([i[1] for i in krizovka])
    for i in range(len(text_widgets)):
        canvas.itemconfig(text_widgets[i], text = krizovka_str[i])


k1 = open("kucera/10/krizovka1-1.txt", 'r', encoding="UTF-8")
k2 = open("kucera/10/krizovka1-2.txt", 'r', encoding="UTF-8")

krizovka1 = open_file(k1)
krizovka2 = open_file(k2)

root = tk.Tk()

WIDTH = 1000
HEIGHT = 500
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg = 'white')
canvas.pack()

create_empty_krizovka(5, krizovka1)
empty_text = create_empty_krizovka(240, krizovka1)
insert_words_to_tajnicka(empty_text, krizovka1)

root.mainloop()