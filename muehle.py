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


def onObjectClick(event):
    # print('Clicked', event.x, event.y, event.widget)
    id = event.widget.find_closest(event.x, event.y)[0]
    # if id:
    setPointAsClicked(id)


def setPointAsClicked(number):
    counter = 0
    for r in range(len(pieces)):
        for s in range(len(pieces[r])):
            if pieces[r][s] != "-":
                counter += 1
                if counter == number:
                    print(str(r) + " " + str(s))


def hide_me(event):
    event.widget.pack_forget()


def drawClickOverlay(grid):
    for r in range(7):
        for s in range(7):
            if grid[r][s] == 1:
                click_element = canvas.create_oval(point_location[s], point_location[r],
                                                   point_location[s] + 40,
                                                   point_location[r] + 40, width=6, fill='black')
                canvas.tag_bind(click_element, "<Button-1>", onObjectClick)


# entryBox = tkinter.Entry(canvas)
# entryBox.grid(row=2, column=1)

# for r in range(7):
#     for c in range(7):
#         label = tkinter.Label(canvas, text='R%s/C%s' % (r, c),
#                               borderwidth=1, background="black").grid(row=r, column=c)

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

full_muehle_grid = [[1, -1, -1, 1, -1, -1, 1],
                    [-1, 1, -1, 1, -1, 1, -1],
                    [-1, -1, 1, 1, 1, -1, -1],
                    [1, 1, 1, -1, 1, 1, 1],
                    [-1, -1, 1, 1, 1, -1, -1],
                    [-1, 1, -1, 1, -1, 1, -1],
                    [1, -1, -1, 1, -1, -1, 1]]

muehle_grid = [[0, -1, -1, 0, -1, -1, 0],
               [-1, 0, -1, 0, -1, 0, -1],
               [-1, -1, 0, 0, 0, -1, -1],
               [0, 0, 0, -1, 0, 0, 0],
               [-1, -1, 0, 0, 0, -1, -1],
               [-1, 0, -1, 0, -1, 0, -1],
               [0, -1, -1, 0, -1, -1, 0]]

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

point_location = [19, 135, 255, 430, 600, 720, 840]


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
    # print(event.widget.find_closest(event.x, event.y))


def showSettedPoints(grid):
    for r in range(7):
        for s in range(7):
            if grid[r][s] == 1:
                click_canvas = canvas.create_oval(point_location[s] + 10, point_location[r] + 10,
                                                  point_location[s] + 40,
                                                  point_location[r] + 40, width=2, fill='black')

        # canvas.tag_bind(click_canvas, '<ButtonPress-1>', locationClicked(e, x=s, y=r))


def movePoint(point_x, point_y):
    for r in range(7):
        for s in range(7):
            if location_set[r][s] == 1:
                if point_y == r and point_x == s:
                    muehle_grid[r][s] = 0
                    muehle_grid[r - 1][s - 1] = 1


# drawClickOverlay(full_muehle_grid)
movePoint(3, 2)
showSettedPoints(muehle_grid)

if active_player == TRUE:
    player_display["text"] = "Aktiver Spieler: Du"

canvas.pack(expand=YES, fill=BOTH)

mainloop()
