class Shell():
    def __init__(self, canv, x, y, vx, vy, k):
        self.canvas = canv
        self.x = x
        self.y = y
        self.r = 10
        self.vx = vx
        self.vy = vy
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
