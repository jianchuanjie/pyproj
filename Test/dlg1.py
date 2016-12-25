import tkinter
import tkinter.messagebox
import sys


def callback():
    if tkinter.messagebox.askyesno('Verify', 'Do you really want to quit?'):
        tkinter.messagebox.showwarning('Yes', 'Quit not yet implemented?')
        sys.exit()
    else:
        tkinter.messagebox.showinfo('No', 'Quit has been cancelled')


errmsg = 'Sorry, no Spqm allowed!'
tkinter.Button(text='Quit', command=callback).pack(fill=tkinter.X)
tkinter.Button(text='Spam', command=(lambda: tkinter.messagebox.showerror('Spam', errmsg))).pack(fill=tkinter.X)
tkinter.mainloop()
