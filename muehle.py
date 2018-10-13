import tkinter as tk
import tkinter
from tkinter import *
from PIL import Image
from PIL import ImageTk

num_pieces = 9
task = ""
active_player = TRUE

canvas = Canvas(width=900, height=1000, bg='white')
canvas.grid()
image = Image.open("muehle-1-spielfeld.png")
image = image.resize((900, 900))
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(2, 2, image=image_tk, anchor=NW)

# entryBox = tkinter.Entry(canvas)
# entryBox.grid(row=2, column=1)

# for r in range(3):
#    for c in range(3):
#        label = tkinter.Label(canvas, text='R%s/C%s' % (r, c),
#                              borderwidth=1, background="black").grid(row=r, column=c)

piece_display = tkinter.Label(canvas, text="Anzahl der Steine: " + str(num_pieces))
piece_display.place(x=100, y=950)
piece_display.pack_propagate()

task_display = tkinter.Label(canvas, text="Aufgabe: " + task)
task_display.place(x=300, y=950)
task_display.pack_propagate()

player_display = tkinter.Label(canvas, text="Aktiver Spieler: " + "")
player_display.place(x=500, y=950)
player_display.pack_propagate()

cleaned_location_set = [[1, 0, 0],
                        [0, 1, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0],
                        [1, 1, 1, 1, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0],
                        [1, 0, 0]]

muehle_grid = [[1, -1, -1, 1, -1, -1, 1],
               [-1, 1, -1, 1, -1, 1, -1],
               [-1, -1, 1, 1, 1, -1, -1],
               [1, 1, 1, -1, 1, 1, 1],
               [-1, -1, 1, 1, 1, -1, -1],
               [-1, 1, -1, 1, -1, 1, -1],
               [1, -1, -1, 1, -1, -1, 1]]

location_set = [[1, -1, -1, 1, -1, -1, 1],
                [0, 1, -1, 1, -1, 1, 0],
                [-1, 0, 1, 1, 1, 0, 0],
                [1, 1, 1, -1, 1, 0, 1],
                [-1, 0, 1, 1, 1, 0, 0],
                [-1, 1, -1, 1, -1, 1, 0],
                [1, -1, -1, 1, -1, -1, 1]]

full_location_set = [[1, -1, -1, 1, -1, -1, 1],
                     [0, 1, -1, 1, -1, 1, 0],
                     [-1, 0, 1, 1, 1, 0, 0],
                     [1, 1, 1, -1, 1, 0, 1],
                     [-1, 0, 1, 1, 1, 0, 0],
                     [-1, 1, -1, 1, -1, 1, 0],
                     [1, -1, -1, 1, -1, -1, 1]]

# "": nicht gesetzt
# "C": Computer
# "P": Player
pieces = [["", "-", "-", "", "-", "-", ""],
          ["-", "", "-", "", "-", "", "-"],
          ["-", "-", "", "", "", "-", "-"],
          ["", "", "", "-", "", "", ""],
          ["-", "-", "", "", "", "-", "-"],
          ["-", "", "-", "", "-", "", "-"],
          ["", "-", "-", "", "-", "-", ""]]

point_location = [10, 135, 255, 430, 590, 700, 830]


# for r in range(7):
#    for s in range(len(location_set[r])):
#        if (location_set[r][s] == 1):
#            x_loc = point_location[s]
#            y_loc = point_location[r]
#            canvas.create_oval(x_loc, y_loc, x_loc + 60, y_loc + 60, width=2, fill='black')


def locationClicked(event, x, y):
    print("X_Location: " + str(x))
    print("Y_Location: " + str(y))
    print("------------------------")
    print(event.widget.find_closest(event.x, event.y))


def onObjectClick(event):
    print('Got object click', event.x, event.y)
    print(event.widget.find_closest(event.x, event.y))


for r in range(7):
    for s in range(7):
        if muehle_grid[r][s] == 1:
            click_canvas = canvas.create_oval(point_location[s] + 10, point_location[r] + 10, point_location[s] + 40,
                                              point_location[r] + 40, width=2, fill='black')

           # canvas.tag_bind(click_canvas, '<ButtonPress-1>', locationClicked(e, x=s, y=r))


if active_player == TRUE:
    player_display["text"] = "Aktiver Spieler: Du"

canvas.pack(expand=YES, fill=BOTH)

# canvas.bind("<Button-1>", )
# for r in range(3):
#    for c in range(3):
#        label = tkinter.Label(canvas, text='R%s/C%s' % (r, c),
#                              borderwidth=1, background="black").grid(row=r, column=c)
#        label.pack_propagate()
mainloop()
