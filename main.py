from tkinter import *


class Plot:
    def __init__(self):
        self.A = []
        self.i = 0
        self.root = Tk()
        self.root.geometry('595x450')
        self.root.title('График:')
        self.t1 = Frame(self.root)
        Canvas(self.root, bg='#202020', width=400, height=400).place(x=5, y=5)
        Button(self.root, text='Создать новую прямую.', command=self.new).place(x=5, y=410, width=140, height=20)
        self.new()
        Button(self.root, text='Перенести на график', command=self.place).place(x=275, y=410, width=130, height=20)

        self.root.mainloop()

    def new(self):
        if self.i < 9:
            exec(f'self.t{self.i} = Frame(self.root)')
            exec(f'Label(self.t{self.i}, text="Введите X0:").place(x=0, y=0, width=70, height=20)')
            exec(f'self.entry_x0{self.i} = Entry(self.t{self.i})')
            exec(f'self.entry_x0{self.i}.place(x=70, y=0, width=20, height=20)')
            exec(f'Label(self.t{self.i}, text="Введите Y0:").place(x=90, y=0, width=70, height=20)')
            exec(f'self.entry_y0{self.i} = Entry(self.t{self.i})')
            exec(f'self.entry_y0{self.i}.place(x=160, y=0, width=20, height=20)')
            exec(f'Label(self.t{self.i}, text="Введите X1:").place(x=0, y=20, width=70, height=20)')
            exec(f'self.entry_x1{self.i} = Entry(self.t{self.i})')
            exec(f'self.entry_x1{self.i}.place(x=70, y=20, width=20, height=20)')
            exec(f'Label(self.t{self.i}, text="Введите Y1:").place(x=90, y=20, width=70, height=20)')
            exec(f'self.entry_y1{self.i} = Entry(self.t{self.i})')
            exec(f'self.entry_y1{self.i}.place(x=160, y=20, width=20, height=20)')
            exec(f'self.t{self.i}.place(x=410,y=5+45*{self.i}, width=180, height=40)')
            self.i += 1
        else:
            pass

    def place(self):
        self.A = []
        for x in range(self.i):
            exec(f'self.A.append([self.entry_x0{x}.get(), self.entry_y0{x}.get(), self.entry_x1{x}.get(), self.entry_y1{x}.get()])')
        print(self.A)


if __name__ == '__main__':
    _ = Plot()
