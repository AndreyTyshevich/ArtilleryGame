class Shell():
    def __init__(self, canv, x, y):
        self.canvas = canv
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = 'gray'
        self.id = canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color)
        self.live = 100

    def draw(self):
        pass

    def set_coords(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        pass

    def hittest(self):
        pass
