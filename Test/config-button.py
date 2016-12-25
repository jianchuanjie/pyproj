import tkinter
import sys


def q1(event):
    print('good bye')
    sys.exit()


widget = tkinter.Button(text='Spam', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='hand2')
widget.config(bd=8, relief=tkinter.RAISED)
widget.config(bg='dark red', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
widget.bind('<Button-1>', q1)
tkinter.mainloop()



