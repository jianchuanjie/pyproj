import sys
import tkinter

widget = tkinter.Button(None, text='Hello event world', command=(lambda: print('Hello lambda world') or sys.exit()))
widget.pack()
widget.mainloop()
