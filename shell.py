class Shell():
    def __init__(self, canv, k):
        self.canvas = canv
        self.x = 0
        self.y = 0
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.k = k
        self.color = 'gray'
        self.id = canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color)
        self.live = 100

    def set_coords(self):
        self.canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self, y):
        if self.y <= y:
            self.live = -1
            self.vy -= 1
            self.y -= self.vy
            self.x += (1 + self.k) * self.vx
        else:
            self.canvas.delete(self.id)
        if self.live < 0:
            self.canvas.delete(self.id)
        else:
            self.live -= 1

    def hittest(self):
        pass
