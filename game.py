from shell import *
from cannon import *
from ground import *
from flag import *

from tkinter import *
import random


def start_game():
    root = Tk()
    frame = Frame(root)
    root.geometry('1200x700')
    canv = Canvas(root, bg='lavender')
    canv.pack(fill=BOTH, expand=1)

    ground = Ground(canv)
    ground.draw()

    coords = random.choice(ground.coords)
    x, y = coords
    cannon_player1 = Cannon(canv, x, y)

    coords = random.choice(ground.coords)
    x, y = coords
    k = random.randint(-1000, 1000)/1000
    if k >= 0:
        x_peak = x + k * 45
    else:
        x_peak = x - k * 45
    flag = Flag(canv, x_peak, x, y, k)
    flag.draw_flag()

    mainloop()
