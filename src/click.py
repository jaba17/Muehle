from tkinter import *

root = Tk()


def onObjectClick(event):
    print('Clicked', event.x, event.y, event.widget)
    print(event.widget.find_closest(event.x, event.y))


canv = Canvas(root, width=100, height=100)
#canv.bind("<Button-1>", callback)
obj1 = canv.create_oval(30, 30, 60, 60, fill='black')
canv.tag_bind(obj1, "<Button-1>", onObjectClick)
canv.pack()

root.mainloop()
