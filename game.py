from cannon import *
from ground import *
from flag import *

from tkinter import *
import random
import time

def create_background(canv):
    def mount(canv):
        mount_leftside = canv.create_polygon(-50, 700, 300, 75, 300, 700, fill='gray40', outline='gray40')
        mount_rightside = canv.create_polygon(300, 700, 300, 75, 650, 700, fill='gray45', outline='gray45')
        snow = canv.create_polygon(230, 200, 300, 75, 370, 200, 330, 170, 300, 200, 275, 165, fill='white',
                                     outline='white')
    mount(canv)

    def hill(canv):
        hill = canv.create_oval(-100, 400, 1700, 1600, fill='DarkGreen', outline='DarkGreen')

    hill(canv)

    def tree(canv):
        tree = canv.create_polygon(647, 400, 680, 300, 713, 400, fill='SpringGreen4', outline='SpringGreen4')
        canv.create_line(680, 400, 680, 423, width=15, fill='Sienna')

    tree(canv)

    def sun(canv):
        sun = canv.create_oval(1000, 100, 1200, -100, fill='gold', outline='gold')
        for end_x, end_y in [(855, 25), (875, 50), (810, 80), (860, 90), (1015, 130), (925, 125), (950, 170),
                             (960, 130), (1050, 140), (1090, 155)]:
            sunray = canv.create_line(1100, 0, end_x, end_y, width=2, fill='gold')

    sun(canv)

def start_game():
    root = Tk()
    frame = Frame(root)
    root.geometry('1200x700')
    canv = Canvas(root, bg='lavender')
    canv.pack(fill=BOTH, expand=1)

    create_background(canv)


    ground = Ground(canv)
    ground.draw()

    def unpack_coords():
        global x, y
        coords = random.choice(ground.coords)
        x, y = coords

    unpack_coords()
    k = random.randint(-1000, 1000)/1000
    if k >= 0:
        x_peak = x + k * 45
    else:
        x_peak = x - k * 45
    flag = Flag(canv, x_peak, x, y, k)
    flag.draw_flag()

    unpack_coords()
    cannon_player1 = Cannon(canv, x, y, k)

    canv.bind('<Button-1>', cannon_player1.fire_start)
    canv.bind('<ButtonRelease-1>', cannon_player1.fire_end)
    canv.bind('<Motion>', cannon_player1.targetting)

    while cannon_player1.balls:
        for ball in cannon_player1.balls:
            ball.move(700)
            ball.set_coords()
        canv.update()
        time.sleep(0.02)



    mainloop()

'''
def fire_start(event):
        active_gamer.fire_start(event)
        
def fire_end(self, event):
        active_gamer.fire_end(event)

def targetting(event):
        active_gamer.targetting(event)

def power_up(event):
        active_gamer.power_up(event)
        
def round():
        if active_gamer == gamer1:
            active_gamer = gamer2
            print('Gamer1')
        else:
            active_gamer = gamer1
            print('Gamer2')
'''
