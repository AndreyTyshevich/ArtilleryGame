
from main import *
root = Tk()
frame = Frame(root)
root.geometry('1200x700')
canv = Canvas(root)
canv.pack(fill=BOTH, expand=1)
photo = PhotoImage(file="logo.png")
Label(root, image=photo).place(x=0, y=0)  # title
btn = Button(root,   text="Start game",  width=30, height=5, bg="white", fg="black")

'''
def foo(event):
    pass
'''

btn.bind("<Button-1>", start_game)  # при нажатии ЛКМ на кнопку вызывается функция
btn.pack()  # расположить кнопку на главном окне
root.mainloop()