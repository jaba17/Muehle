import tkinter

root = tkinter.Tk()
root.resizable(False, False)

root = tkinter.Frame(root, width=900, height=1000)
# root.grid(4, 4)


def key(event):
    print("pressed", repr(event.char))


def callback(event):
    # frame.focus_set()
    print("clicked at", event.x, event.y)


def callback_l(event):
    # frame.focus_set()
    print("label clicked at", event.x, event.y)


# frame = tkinter.Frame(root, width=900, height=1000)
# frame.bind("<Button-1>", callback)
# frame.pack()

# label1 = Label(root, text='dsadf', borderwidth=1).grid(row=0, column=0)
# label1.grid(row=0, column=0)
# label1.configure(background="black")
# label1.bind("<Button-1>", callback_l)
# label1.pack()
# entryBox = tkinter.Entry(root)
# entryBox.grid(row=2, column=1)

point_location = [32, 141, 250, 405, 549, 659, 767]

for r in range(7):
    for s in range(7):
        label_ = tkinter.Label(root, text='R%s/C%s')


root.mainloop()
