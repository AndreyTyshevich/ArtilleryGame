from shell import *
import math


class Cannon():
    def __init__(self, canv, x, y, k):
        self.canvas = canv
        self.power = 10
        self.start = 0
        self.on = 1
        self.angle = 1
        self.x = x
        self.y = y
        self.r = 20
        self.l = 50
        self.k = k
        self.carriage = self.canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r,
        fill="black")
        self.muzzle = self.canvas.create_line(self.x, self.y, self.x + self.l, self.y, width=5)
        self.health = 100

    def draw(self):
        pass

    def targetting(self, event=0):
        if event:
            try:
                self.angle = math.atan((event.y - self.y) / (event.x - self.x))
            except ZeroDivisionError:
                self.angle = math.pi/2
        if self.start:
            self.canvas.itemconfig(self.muzzle, fill='red')
        else:
            self.canvas.itemconfig(self.muzzle, fill='black')
            if event.x > self.x:
                self.canvas.coords(self.muzzle, self.x, self.y, self.x + self.l * math.cos(self.angle),
                self.y + self.l * math.sin(self.angle))
            else:
                self.canvas.coords(self.muzzle, self.x, self.y, self.x - self.l * math.cos(self.angle),
                self.y - self.l * math.sin(self.angle))

    def fire_start(self, event):
        if self.on:
            self.start = 1

    def stop(self):
        self.start = 0
        self.on = 0

    def fire_end(self, event):
        if self.on:
            new_ball = Shell(self.canvas, self.k)
            new_ball.x = self.x
            new_ball.x = self.y
            new_ball.vx = self.power * math.cos(self.angle)
            new_ball.vy = -self.power * math.sin(self.angle)
            self.start = 0
            self.power = 10

    def power_up(self):
        if self.start:
            if self.power < 100:
                self.power += 1
                canv.itemconfig(self.muzzle, fill='red')
        else:
            canv.itemconfig(self.muzzle, fill='black')
