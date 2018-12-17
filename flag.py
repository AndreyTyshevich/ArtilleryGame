class Flag:
    def __init__(self, canv, x, y, k):
        self.x = x
        self.y = 700 - y
        self.k = k
        self.x_peak = x + self.k * 20
        self.y_peak = self.y - 180
        self.canvas = canv

    def draw_flag(self):
        self.canvas.create_line(self.x, self.y-200, self.x, self.y, fill='#654321', width=7)
        self.canvas.create_polygon(self.x, self.y-160, self.x_peak, self.y_peak, self.x, self.y-200, fill='#7B917B')
