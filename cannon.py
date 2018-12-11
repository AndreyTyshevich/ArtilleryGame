import math


class Cannon():
    def __init__(self, canv, x, y):
        self.canvas = canv
        self.power = 10
        self.start = 0
        self.angle = 1
        self.carriage = self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="black")
        self.muzzle = self.canvas.create_line(x, y, x + 30, y + 40, width=5)
        self.health = 100

    def draw(self):
        pass

    def targetting(self, event=0):
        if event:
            self.angle = math.atan((event.y - 450) / (event.x - 20))
        if self.start:
            canv.itemconfig(self.muzzle, fill='red')
        else:
            self.canvas.itemconfig(self.muzzle, fill='black')
            self.canvas.coords(self.muzzle, x1, x2, 20 + max(self.power, 20) * math.cos(self.angle),
            450 + max(self.power, 20) * math.sin(self.angle))

    def fire_start(self, event):
        self.start = 1

    def fire_end(self, event):
        self.angle = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        self.start = 0
        self.power = 10
    def power_up(self):
        if self.start:
            if self.power < 100:
                self.power += 1
                canv.itemconfig(self.muzzle, fill='red')
        else:
            canv.itemconfig(self.muzzle, fill='black')
