import random


class Ground:
    def __init__(self, canv):
        self.canvas = canv
        self.coords = []
        self.coord = 0

    def draw(self):
        h = random.randint(300, 500)
        d = 1
        for x in range(1200):
            self.coord = (x, h)
            self.coords.append(self.coord)
            self.canvas.create_line(x, 700, x, h, width=7, fill='ForestGreen')
            if h > 500 or h < 300:
                d = -d
                i = d*random.randint(0, 1)
            elif 380 < h < 420:
                i = d*random.randint(0, 2)
            elif 300 <= h <= 380 or 420 <= h <= 500:
                i = d*random.randint(0, 1)
            h = h + i
