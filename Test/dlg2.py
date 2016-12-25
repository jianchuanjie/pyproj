import tkinter.simpledialog
import tkinter


def shuru():
    s = tkinter.simpledialog.askstring('input', 'Please input something')
    print(s)


class Demo(tkinter.Frame):
    def __init__(self, parent=None, **options):
        tkinter.Frame.__init__(self, parent, **options)
        self.pack()
        tkinter.Label(self, text='Basic demo').pack()
        tkinter.Button(self, text='input', command=shuru).pack(side=tkinter.TOP, fill=tkinter.BOTH)


if __name__ == '__main__':
    Demo().mainloop()