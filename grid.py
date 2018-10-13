from tkinter import *
import tkinter

root = tkinter.Tk()
root.geometry("900x1000")
for r in range(7):
    for c in range(7):
        label_ = tkinter.Label(root, text='R%s/C%s' % (r, c), borderwidth=10)
        label_.grid(row=r, column=c)

root.mainloop()
