import tkinter


def greeting():
    print('Hello stuout world!...')


win = tkinter.Frame()
win.pack()
tkinter.Label(win, text='Hello container world').pack(side=tkinter.TOP)
tkinter.Button(win, text='Hello', command=greeting).pack(side=tkinter.LEFT)
tkinter.Button(win, text='Quit', command=win.quit).pack(side=tkinter.RIGHT)

win.mainloop()