#!/usr/bin/python
from tkinter import *
root = Tk()
from PIL import Image

def callback(event):
    f.focus_set()
    print ("clicked at", event.x, event.y)



f = Frame(root, height=1000, width=900)
f.bind("<Button-1>", callback)

f.pack()


#image = Image.open("mühle.png")
#photo = ImageTk.PhotoImage(image)
#background = PhotoImage(file = "mühle.png")

label_1_1 = Label(f, text="df")
label_1_1.pack()

#label_1_2 = Label()

#im = Image.open('mühle.png')

#background_image=PhotoImage(photo)
label = Label(f, text="dsf")
label.pack()



#root.manloop()
#im.show()

#w = Label(root, image=im)
#w.image = im
#w.pack()

root.mainloop()