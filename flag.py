class Flag:
    def __init__(self, canv, x_peak, x, y, k):
        self.x_peak = x_peak
        self.y_peak = y - 220
        self.x = x
        self.y = y
        self.k = k
        self.canvas = canv

    def draw_flag(self):
        self.canvas.create_line(self.x, self.y-250, self.x, self.y, fill='#654321', width=7)
        self.canvas.create_polygon(self.x, self.y-250, self.x_peak, self.y_peak, self.x, self.y-190, fill='#7B917B')
