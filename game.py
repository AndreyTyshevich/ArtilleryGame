from ground import *
from cannon import *
from flag import *

from tkinter import *
from random import randrange as randint
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

        x = randint(100, 550)
        y = self.ground.height[round(x)]
        self.gamer1 = Cannon(x, y, canvas, root)
        self.cannons.append(self.gamer1)

        x = randint(750, 1100)
        y = self.ground.height[round(x)]
        self.gamer2 = Cannon(x, y, canvas, root)
        self.cannons.append(self.gamer2)

        self.current_player = 0
        self.inactive = 1
        self.shells = []

        btn1 = Button(root, text="Armor Up",  width=30, height=5, bg="white", fg="black")
        btn1.pack()

        canvas.bind("<Button-1>", self.mouse_click)
        canvas.bind("<Motion>", self.mouse_motion)
        btn1.bind("<Button-1>", self.buy_health)

        self.game_state = GameState.TANK_IS_AIMING

    def mouse_motion(self, event):  # Метод описывает движение мышкой
        if self.game_state != GameState.TANK_IS_AIMING:
            return
        cannon = self.cannons[self.current_player]
        cannon.target(event.x, screen_height - event.y)

    def buy_health(self):
        cannon = self.cannons[self.current_player]
        if cannon.money >= 20:
            cannon.heal_up()
            cannon.spend_points()

    def mouse_click(self, event):  # Метод описывает клик мышкой
        if self.game_state != GameState.TANK_IS_AIMING:
            return
        cannon = self.cannons[self.current_player]
        x, y = screen(event.x, event.y)
        cannon.target(x, y)
        shell = cannon.shoot(x, y, self.flag.k)
        self.shells.append(shell)

        self.game_state = GameState.SHELL_IS_FLYING
        canvas.after(sleep_time, self.shell_flying)

        self.inactive = self.current_player
        self.current_player = (self.current_player + 1) % 2

    def shell_flying(self, *ignore):  # Метод описывает полёт снаряда
        if self.game_state != GameState.SHELL_IS_FLYING:
            return
        canvas.after(sleep_time, self.shell_flying)

        for shell in self.shells:
            shell.move()

        for shell in self.shells:
            if self.ground.check_collision(shell):
                self.ground.explode(shell)
                self.game_state = GameState.TANK_IS_AIMING
            for cannon_object in self.cannons:
                if self.ground.check_direct_hit(shell, cannon_object):
                    enemy = self.cannons[self.inactive]
                    enemy.earn_points()
                    cannon_object.take_damage(shell.damage)
                    self.ground.explode(shell)
                    self.game_state = GameState.TANK_IS_AIMING
        if self.game_state != GameState.SHELL_IS_FLYING:
            self.shells.clear()

            k = randint(-10, 10)
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
btn.bind("<Button-1>", start_game)  # при нажатии ЛКМ на кнопку вызывается функция
btn.pack()
root.mainloop()
