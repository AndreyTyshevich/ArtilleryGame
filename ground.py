from tkinter import *
import random

from math import *

screen_width = 1200
screen_height = 700


def screen(x, y):
    return x, screen_height - y


class Background:
    def __init__(self, canvas):
        self._canvas = canvas
        self.dr(canvas)
        self.draw()

        photo = PhotoImage(file="15452117468811.png")
        Label(canvas, image=photo).place(x=790, y=505)
    def draw(self):
 #       root = Tk()
  #      frame = Frame(root)
   #     root.overrideredirect(True)
    #    root.overrideredirect(False)
     #   root.attributes('-fullscreen', True)
      #  canv = Canvas(root, bg='white')
       # canv.pack(fill=BOTH, expand=1)
#        photo = PhotoImage(file="msIeloztIBU.png")
 #       screen_width = root.winfo_screenwidth()
  #      screen_height = root.winfo_screenheight()

#        Label(root, image=photo).place(x=screen_width / 2, y=screen_height / 2, anchor= CENTER)

        mount_leftside = self._canvas.create_polygon(-50, 700, 300, 75, 300, 700, fill='gray40', outline='gray40')
        mount_rightside = self._canvas.create_polygon(300, 700, 300, 75, 650, 700, fill='gray45', outline='gray45')
        snow = self._canvas.create_polygon(230, 200, 300, 75, 370, 200, 330, 170, 300, 200, 275, 165, fill='white',
                                           outline='white')

        hill = self._canvas.create_oval(-100, 400, 1700, 1600, fill='DarkGreen', outline='DarkGreen')

        tree = self._canvas.create_polygon(647, 400, 680, 300, 713, 400, fill='SpringGreen4', outline='SpringGreen4')
        self._canvas.create_line(680, 400, 680, 423, width=15, fill='Sienna')

        sun = self._canvas.create_oval(1000, 100, 1200, -100, fill='gold', outline='gold')
        for end_x, end_y in [(855, 25), (875, 50), (810, 80), (860, 90), (1015, 130), (925, 125), (950, 170),
                             (960, 130), (1050, 140), (1090, 155)]:
            sunray = self._canvas.create_line(1100, 0, end_x, end_y, width=2, fill='gold')

    def dr(self, canvas):
        photo = PhotoImage(file="123456.png")
        Label(canvas, image=photo).place(x=690, y=205)

class Ground:

    def __init__(self, canvas):
        self.height = list()
        self.min_height = screen_height - 300
        self.max_height = screen_height - 200
        self.dx = int(screen_width)
        self.canvas = canvas
        self.generate()

    """
        Генерируется список высот на момент запуска
    """
    def generate(self):
        height = random.randint(self.min_height, self.max_height)
        i = 1
        for _ in range(1200):
            self.height.append(height)
            if height > 500 or height < 200:
                i = - i
                dh = i * random.randint(0, 1)
            elif 200 <= height <= 500:
                dh = i * random.randint(0, 1)
            height += dh

    """
         Функция отрисовывает землю по списку высот
    """
    def draw(self):
        for i in range(1200):
            self.canvas.create_line(i, screen_height, screen(i, self.height[i]), width=5, fill='Sienna', tag='ground')
    """
         Функция проверяет столкновение снаяряда с землей
    """
    def check_collision(self, shell):
        return (shell.y - shell.r) <= self.height[round(shell.x)]

    """
         Функция уменьшает координаты столбиков земли в радиусе поражения снаряда
    """
    def explode(self, shell):
        shell.destroy()

    def damage(self): #дописать
        return self.damage
