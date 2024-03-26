import tkinter as tk


def on_button_click():
    text = entry.get()
    if text:
        do_command(text)


def do_command(command: str):
    global x, y, vector
    ciara_cmd = "ciara"
    direction_cmd = ['vpravo', 'vlavo']
    if ciara_cmd in command:
        command = command.split(' ')
        length = int(command[1])
        new_x = x + vector[0] * length
        new_y = y + vector[1] * length
        canvas.create_line(x, y, new_x, new_y)
        x = new_x
        y = new_y
    elif direction_cmd[0] in command or direction_cmd[1] in command:
        if command == direction_cmd[0]:
            vector[0], vector[1] = vector[1] * -1, vector[0]
        else:
            vector[0], vector[1] = vector[1], vector[0] * -1
    else:
        print("invalid input")


root = tk.Tk()
root.geometry('500x550')

canvas = tk.Canvas(root, width=500, height=500, bg='white')
canvas.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='Enter command', command=on_button_click)
button.pack()

x = 250
y = 250
# vector = [x, y]
vector = [0, -1]

root.mainloop()