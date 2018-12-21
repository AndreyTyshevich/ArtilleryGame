from tkinter import messagebox
screen_width = 1200
screen_height = 700
shell_radius = 10
dt = 0.2
g = -9.8


def screen(x, y):
    return x, screen_height - y


class Shell:
    def __init__(self, x, y, r, Vx, Vy, canvas, k):
        self.color = 'gray'
        self.x, self.y, self.r = x, y, r
        self.Vx, self.Vy = 3*Vx, 3*Vy
        self._canvas = canvas
        self.circle = canvas.create_oval(screen(x - r, y - r), screen(x + r, (y + r)), fill=self.color)
        self.damage_radius = 10
        self.damage = 30
        self.k = k

    def move(self):  # Метод описывает характер изменения координат между отрисовками и перемещает снаряд
        ax = self.k
        ay = g
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        self.Vx += ax * dt
        self.Vy += ay * dt

        x1, y1 = screen(self.x - self.r, self.y - self.r)
        x2, y2 = screen(self.x + self.r, self.y + self.r)
        self._canvas.coords(self.circle, x1, y1, x2, y2)

    def destroy(self):  # Метод убирает снаряд с холста
        try:
            self._canvas.delete(self.circle)
        except:
            pass


class Cannon:
    max_cannon_length = 30

    def __init__(self, x, y, canvas, root):
        self._canvas = canvas
        self.x, self.y = x, y
        self.length_x = 0
        self.length_y = -30
        self.r = 20

        self.cannon = self._canvas.create_line(screen(self.x, self.y,), screen(self.x +
                                                                               self.length_x, self.y + self.length_y),
                                               width=7, fill='black', tag='cannon')
        self.carriage = self._canvas.create_oval(screen(self.x - self.r, self.y-self.r),
                                                 screen(self.x+self.r, self.y+self.r), fill="black")
        self.health = 100

        self._root = root
        self.text_id = -500
        self.current_shell = -500
        self.money = 0

        if 100 <= self.x <= 550:
            self._canvas.create_text(100, 100, text="Прочность:")
            self.text_id = self._canvas.create_text(150, 100, text=self.health)
        else:
            self._canvas.create_text(1050, 100, text="Прочность:")
            self.text_id = self._canvas.create_text(1100, 100, text=self.health)

        if 100 <= self.x <= 550:
            self._canvas.create_text(100, 120, text="Очки:")
            self.money_id = self._canvas.create_text(150, 120, text=self.money)
        else:
            self._canvas.create_text(1050, 120, text="Очки:")
            self.money_id = self._canvas.create_text(1100, 120, text=self.money)

    def target(self, x, y):  # Метод описывает наведение
        self.length_x = (x - self.x)
        self.length_y = (y - self.y)
        l = (self.length_x ** 2 + self.length_y ** 2) ** 0.5
        self.length_x = self.max_cannon_length * self.length_x / l
        self.length_y = self.max_cannon_length * self.length_y / l

        x1, y1 = screen(self.x, self.y)
        x2, y2 = screen(self.x + self.length_x, self.y + self.length_y)
        self._canvas.delete('cannon')
        self.cannon = self._canvas.create_line(x1, y1, x2, y2, width=7, fill='black', tag='cannon')
        self._canvas.coords(self.cannon, x1, y1, x2, y2)

    def shoot(self, x, y, k):  # Метод описывает выстрел
        self.target(x, y)
        Vx = self.length_x
        Vy = self.length_y
        return Shell(self.x + self.length_x, self.y + self.length_y, shell_radius, Vx, Vy, self._canvas, k)

    def earn_points(self):
        self.money += 10
        self._canvas.itemconfig(self.money_id, text=self.money)

    def spend_points(self):
        self.money -= 20
        self._canvas.itemconfig(self.money_id, text=self.money)

    def armor_up(self):
        self.health += 20
        self._canvas.itemconfig(self.text_id, text=self.health)

    def take_damage(self, damage):
        self.health -= damage
        self._canvas.itemconfig(self.text_id, text=self.health)
        if self.health <= 0:
            self._canvas.delete("all")
            self._canvas.destroy()
            self._root.destroy()
            infotext = " "
            if 50 <= self.x <= 550:
                infotext = "Second player wins"
            else:
                infotext = "First player wins"
            messagebox.showinfo("Game Over", infotext)
