import tkinter
root = tkinter.Tk()
labelfont = ('times', 20, 'bold')
widget = tkinter.Label(root, text='Hello config world')
widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)
widget.pack(expand=tkinter.YES, fill=tkinter.BOTH)
root.mainloop()
