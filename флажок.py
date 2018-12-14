from tkinter import *
import random

root = Tk()
root.geometry('1200x700')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
k = random.randint(-1, 1)   #надо будет домножить на 0,3

class Flag:
    def __init__(self, x_peak, k):
        self.x_peak = x_peak
        self.y_peak = 50
        self.k = k
        self.design = self.draw_flag()

    def draw_flag(self):
        canv.create_line(500, 20, 500, 300, fill='#654321', width=7)
        canv.create_polygon(500, 20, self.x_peak, self.y_peak, 500, 80, fill='#7B917B')


if k >= 0:
    x_peak = 450 + k*45
else:
    x_peak = 550 - k*45

   
flag = Flag(x_peak, k)
flag.draw_flag()

root.mainloop()