import tkinter as tk


def check_brackets(vyraz: str) -> bool:
    bracket_counter = 0
    for i in vyraz:
        if i == '(':
            bracket_counter += 1               
        elif i == ')':
            bracket_counter -= 1
            if bracket_counter < 0:
                return False
    return True if bracket_counter == 0 else False


def create_vyraz(vyraz: str):
    global colors
    left_brackets = []
    letter_width = 20
    y = letter_width//2
    color_num = 0
    # vytvori vyraz bez farbiciek
    for i in range(len(vyraz)):
        x = i * letter_width
        letter = vyraz[i]
        temp = canvas.create_text(x + 10, y, text=letter, font= f"Helvetica {letter_width}", anchor='nw')
        if letter == '(':
            left_brackets.append(temp)
            canvas.itemconfig(temp, fill=colors[color_num])
            color_num += 1
        elif letter == ')':
            color = canvas.itemcget(left_brackets[-1], 'fill')
            canvas.itemconfig(temp, fill=color)
            left_brackets.pop()        


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=100, bg='white')
canvas.pack()

colors = ["blue", 'magenta', 'red', 'purple', 'green', 'orange', 'pink']
vyraz = "(x + y) - x + 2 (x(x+y))"
check = check_brackets(vyraz)
if check:
    create_vyraz(vyraz)

root.mainloop()