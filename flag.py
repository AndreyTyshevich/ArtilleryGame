class Flag:
    def __init__(self, canvas, x, y, k):
        self.x = x
        self.y = 700 - y
        self.k = k
        self.x_peak = x + self.k * 10
        self.y_peak = self.y - 180
        self.canvas = canvas
        self.stick = self.canvas.create_line(self.x, self.y-200, self.x, self.y, fill='#654321', width=7)
        self.triangle = self.canvas.create_polygon(self.x, self.y-160,
                                                   self.x_peak, self.y_peak, self.x, self.y-200, fill='#7B917B')

    def change_power(self, k):  # Метод описывает изменение геометрии флага и ускореня, сообщаемого ветром
        x_peak = self.x + k * 20
        self.k = k
        self.canvas.coords(self.triangle, self.x, self.y - 160, x_peak, self.y_peak, self.x, self.y - 200)
