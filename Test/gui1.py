import tkinter
import sys


def quit():
    print('Hello, I must be going...')
    sys.exit()


root = tkinter.Tk()
tkinter.Button(root, text='press', command=quit).pack(side=tkinter.LEFT, expand=tkinter.YES,fill=tkinter.BOTH)
root.mainloop()