import tkinter as tk
import random


def generate_random_green():
    green = random.randint(40, 255)
    green_hex = format(green, '02x')
    color = "#00{}00".format(green_hex)
    return color


def generate_hill(iteration):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT//2 + iteration, HEIGHT - 50)
    x_coord = -10
    y_coord = y
    coordinates = [0, HEIGHT]
    while x_coord < x:
        x_coord += 10
        coordinates.append(x_coord)
        y_coord -= random.randrange(0, 10)
        coordinates.append(y_coord)
    while x_coord < WIDTH:
        x_coord += 10
        coordinates.append(x_coord)
        y_coord += random.randrange(0, 10)
        coordinates.append(y_coord)
    coordinates.append(WIDTH)
    coordinates.append(HEIGHT)
    canvas.create_polygon(coordinates, fill=generate_random_green())


def genereate_valley(iteration):
    x = random.randrange(0, WIDTH)
    y = random.randrange(HEIGHT//2 + iteration, HEIGHT - 50)
    x_coord = -10
    y_coord = y
    coordinates = [0, HEIGHT]
    while x_coord < x:
        x_coord += 10
        coordinates.append(x_coord)
        y_coord += random.randrange(0, 10)
        coordinates.append(y_coord)
    while x_coord < WIDTH:
        x_coord += 10
        coordinates.append(x_coord)
        y_coord -= random.randrange(0, 10)
        coordinates.append(y_coord)
    coordinates.append(WIDTH)
    coordinates.append(HEIGHT)
    canvas.create_polygon(coordinates, fill=generate_random_green())


def generate_country():
    for i in range(20):
        if random.choice([True, False]):
            generate_hill(i)
        else:
            genereate_valley(i)


root = tk.Tk()

WIDTH = 500
HEIGHT = 500
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='#ADD8E6')
canvas.pack()

generate_country()

root.mainloop()