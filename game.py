from ground import *
from cannon import *
from flag import *

from tkinter import *
from math import *
from random import randrange as randint, choice
import time
from enum import Enum

sleep_time = 35
screen_width = 1200
screen_height = 700
shell_radius = 5
dt = 10  # времени между кадрами обсчёта
g = -9.8


class GameState(Enum):
    TANK_IS_AIMING = 1
    SHELL_IS_FLYING = 2


def screen(x, y):
    return x, screen_height - y


class Start_game():
    def __init__(self, root):
        global canvas
        canvas = Canvas(root)
        canvas["width"] = screen_width
        canvas["height"] = screen_height
        canvas.pack()
        self.cannons = []
        Background(canvas)
        self.ground = Ground(canvas)
        self.ground.draw()
        self.flag = 0

        x = randint(150, 1050)
        y = self.ground.height[round(x)]
        k = 0
        flag = Flag(canvas, x, y, k)
        self.flag = Flag(canvas, x, y, k)

        x = randint(50, 550)
        y = self.ground.height[round(x)]
        self.gamer1 = Cannon(x, y, canvas)
        self.cannons.append(Cannon(x, y, canvas))

        x = randint(750, 1150)
        y = self.ground.height[round(x)]
        self.gamer2 = Cannon(x, y, canvas)
        self.cannons.append(Cannon(x, y, canvas))

        self.current_player = 0
        self.shells = []

        canvas.bind("<Button-1>", self.mouse_click)
        canvas.bind("<Motion>", self.mouse_motion)
        # root.bind('<Key>', self.move)
        self.game_state = GameState.TANK_IS_AIMING

    def mouse_motion(self, event):
        if self.game_state != GameState.TANK_IS_AIMING:
            return
        cannon = self.cannons[self.current_player]
        cannon.target(event.x, screen_height - event.y)

    def mouse_click(self, event):
        if self.game_state != GameState.TANK_IS_AIMING:
            return
        cannon = self.cannons[self.current_player]
        x, y = screen(event.x, event.y)
        cannon.target(x, y)
        shell = cannon.shoot(x, y, self.flag.k)
        self.shells.append(shell)

        self.game_state = GameState.SHELL_IS_FLYING
        canvas.after(sleep_time, self.shell_flying)

        self.current_player = (self.current_player + 1) % 2

    def shell_flying(self, *ignore):
        if self.game_state != GameState.SHELL_IS_FLYING:
            return
        canvas.after(sleep_time, self.shell_flying)

        for shell in self.shells:
            shell.move()

        for shell in self.shells:
            if self.ground.check_collision(shell):
                self.ground.explode(shell)
                self.game_state = GameState.TANK_IS_AIMING
        if self.game_state != GameState.SHELL_IS_FLYING:
            self.shells.clear()

            k = randint(-7, 7)
            self.flag.change_power(k)

def start_game(event):
    root_window = Tk()
    Start_game(root_window)
    root_window.mainloop()

root = Tk()
frame = Frame(root)
root.geometry('1200x700')
canv = Canvas(root)
canv.pack(fill=BOTH, expand=1)
photo = PhotoImage(file="logo.png")
Label(root, image=photo).place(x=0, y=0)  # title
btn = Button(root, text="Start game",  width=30, height=5, bg="white", fg="black")
btn.bind("<Button-1>",start_game)  # при нажатии ЛКМ на кнопку вызывается функция
btn.pack()
root.mainloop()
