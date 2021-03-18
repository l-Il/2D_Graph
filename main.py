from random import shuffle
from tkinter import *


class Plot:
    def __init__(self):
        self.i = 0
        self.color = ['#8AEA92', '#177E89', '#585481', '#FFBA49', '#A4243B', '#F05D23', '#4D6CFA', '#31E981', '#FAA300']
        shuffle(self.color)
        self.root = Tk()
        self.root.geometry('597x435')
        self.root.title('График:')
        self.t1 = Frame(self.root)
        self.canvas = Canvas(self.root, bg='#FFFFFF', width=400, height=400)
        self.canvas_set()
        Button(self.root, relief='groove', text='Перенести на график', command=self.place).place(x=7, y=410, width=130, height=20)
        Button(self.root, relief='groove', text='Создать новую прямую', command=self.new).place(x=142, y=410, width=140, height=20)
        self.new()
        Button(self.root, relief='groove', text='Очистить всё', command=self.clear).place(x=287, y=410, width=120, height=20)
        self.status = Label(self.root, text='Введите координаты:')
        self.status.place(x=412, y=410, width=180)
        self.root.mainloop()

    def canvas_set(self):
        self.canvas = Canvas(self.root, bg='#FFFFFF', width=400, height=400)
        # Сетка, одна клетка = 20х20
        for x in range(22):  # Х - переменная обхода
            self.canvas.create_line(20 * x, 400, 20 * x, 0, fill='gray')
            self.canvas.create_line(0, 20 * x, 400, 20 * x, fill='gray')
        # Оси
        self.canvas.create_line(400, 200, 0, 200, arrow=FIRST, fill='black', width=2)  # X
        self.canvas.create_line(200, 0, 200, 400, arrow=FIRST, fill='black', width=2)  # Y
        self.canvas.place(x=5, y=5)

    def new(self):
        if self.i < 9:
            exec(f'self.t{self.i} = Frame(self.root, bg=self.color[self.i])')
            exec(f'Label(self.t{self.i}, bg=self.color[self.i], text="Введите X0:").place(x=0, y=0, width=70, height=20)')
            exec(f'self.entry_x0{self.i} = Entry(self.t{self.i})')
            exec(f'self.entry_x0{self.i}.place(x=70, y=0, width=20, height=20)')
            exec(f'Label(self.t{self.i}, bg=self.color[self.i], text="Введите Y0:").place(x=90, y=0, width=70, height=20)')
            exec(f'self.entry_y0{self.i} = Entry(self.t{self.i})')
            exec(f'self.entry_y0{self.i}.place(x=160, y=0, width=20, height=20)')
            exec(f'Label(self.t{self.i}, bg=self.color[self.i], text="Введите X1:").place(x=0, y=20, width=70, height=20)')
            exec(f'self.entry_x1{self.i} = Entry(self.t{self.i})')
            exec(f'self.entry_x1{self.i}.place(x=70, y=20, width=20, height=20)')
            exec(f'Label(self.t{self.i}, bg=self.color[self.i], text="Введите Y1:").place(x=90, y=20, width=70, height=20)')
            exec(f'self.entry_y1{self.i} = Entry(self.t{self.i})')
            exec(f'self.entry_y1{self.i}.place(x=160, y=20, width=20, height=20)')
            exec(f'self.t{self.i}.place(x=412,y=7+45*{self.i}, width=180, height=40)')
            self.i += 1
        else:
            pass

    def place(self):
        try:
            for x in range(self.i):
                exec(f'''self.canvas.create_line(200+float(self.entry_x0{x}.get())*20, 
                                                200-float(self.entry_y0{x}.get())*20, 
                                                200+float(self.entry_x1{x}.get())*20, 
                                                200-float(self.entry_y1{x}.get())*20, width=2, fill=self.color[x])''')
        except Exception as _:
            pass

    def clear(self):
        self.canvas.destroy()
        self.canvas_set()
        for x in range(self.i):
            exec(f'self.t{x}.destroy()')
        self.i = 0
        self.new()
        self.status.config(text='Очищено.')
        shuffle(self.color)


if __name__ == '__main__':
    _ = Plot()
