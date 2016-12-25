import tkinter


def greeting():
    print('Hello stdout world!...')


win = tkinter.Frame()
win.pack()
tkinter.Label(win, text='Hello container world!').pack(side=tkinter.TOP)
tkinter.Button(win, text='Hello', commman=greeting).pack(side=tkinter.LEFT)
tkinter.Button(win, text='quit', command=win.quit).pack(side=tkinter.RIGHT)

win.mainloop()
