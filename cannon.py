import math
from tkinter import *
from random import *

screen_width = 1200
screen_height = 700
shell_radius = 10
dt = 0.3
g = -9.8


def screen(x, y):
    return x, screen_height - y


class Shell:
    def __init__(self, x, y, r, Vx, Vy, canvas, k):
        self.color = 'gray'
        self.x, self.y, self.r = x, y, r
        self.Vx, self.Vy = Vx, Vy
        self._canvas = canvas
        self.circle = canvas.create_oval(screen(x - r, y - r), screen(x + r, (y + r)), fill=self.color)
        self.damage_radius = 40
        self.damage = 10
        self.k = k

    def move(self):
        ax = self.k
        ay = g
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        self.Vx += ax * dt
        self.Vy += ay * dt

        x1, y1 = screen(self.x - self.r, self.y - self.r)
        x2, y2 = screen(self.x + self.r, self.y + self.r)
        self._canvas.coords(self.circle, x1, y1, x2, y2)

    def check_collision(self, x, y):
       l = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
       return l <= self.r

    def destroy(self):
        self._canvas.delete(self.circle)


class Cannon:
    max_cannon_length = 30

    def __init__(self, x, y, canvas, k):
        self._canvas = canvas
        self.x, self.y = x, y
        # self.power = 10
        # self.on = 0 дописать
        self.length_x = 0
        self.length_y = -30
        self.r = 20
        self.cannon = self._canvas.create_line(screen(self.x, self.y,), screen(self.x + self.length_x, self.y + self.length_y),
                                               width=7, fill='black', tag='cannon')
        self.carriage = self._canvas.create_oval(screen(self.x - self.r, self.y-self.r), screen(self.x+self.r, self.y+self.r),
                                                fill="black")
        self.k = k
        self.health = 100

    def target(self, x, y):
        self.length_x = (x - self.x)
        self.length_y = (y - self.y)
        l = (self.length_x ** 2 + self.length_y ** 2) ** 0.5
        self.length_x = self.max_cannon_length * self.length_x / l
        self.length_y = self.max_cannon_length * self.length_y / l

        x1, y1 = screen(self.x, self.y)
        x2, y2 = screen(self.x + self.length_x, self.y + self.length_y)
        self._canvas.delete('cannon')   # нужно исправить
        self.cannon = self._canvas.create_line(x1, y1, x2, y2, width=7, fill='black', tag='cannon')
        self._canvas.coords(self.cannon, x1, y1, x2, y2)

    # еще не дописана
    def power_up(self):
        if self.on:
            if self.power < 100:
                self.power += 1
            self._canvas.itemconfig(self.cannon, fill='orange')
        else:
            self._canvas.itemconfig(self.cannon, fill='black')

    def shoot(self, x, y):
        self.target(x, y)
        Vx = self.length_x
        Vy = self.length_y
        return Shell(self.x + self.length_x, self.y + self.length_y, shell_radius, Vx, Vy, self._canvas, self.k)

    def take_damage(self, damage):  #дописать
        self.health -= damage
