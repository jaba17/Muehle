import threading
import tkinter
from tkinter import *
from PIL import Image
from PIL import ImageTk

from AI.SetRound import SetRound
from VARIABLES import *

task = ""
active_player = TRUE

canvas = Canvas(width=900, height=1000, bg='white')
canvas.grid()
image = Image.open("res/muehle-1-spielfeld.png")
image = image.resize((900, 900))
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(2, 2, image=image_tk, anchor=NW)


class Muehle:

    def __init__(self):

        self.num_pieces = 9
        print("Welcoime to muehle")
        self.setupBoard()

        canvas.mainloop()

    def setupBoard(self):
        piece_display = tkinter.Label(canvas, text="Anzahl der Steine: " + str(self.num_pieces))
        piece_display.place(x=100, y=950)
        piece_display.pack_propagate()

        task_display = tkinter.Label(canvas, text="Aufgabe: " + task)
        task_display.place(x=300, y=950)
        task_display.pack_propagate()

        player_display = tkinter.Label(canvas, text="Aktiver Spieler: " + "")
        player_display.place(x=500, y=950)
        player_display.pack_propagate()

        self.drawClickOverlay(VARIABLES.muehle_grid)
        self.showSettedPoints(VARIABLES.pieces)

    def onObjectClick(self, event):
        print('Clicked', event.x, event.y, event.widget)
        loc = VARIABLES.point_location
        x = event.x - 25
        y = event.y - 25  # if id:
        print(str(x) + " " + str(y))

        y_index = self.getIndFromCoord(y)
        x_index = self.getIndFromCoord(x)

        if VARIABLES.muehle_grid[y_index][x_index] == 1 and VARIABLES.pieces[y_index][x_index] == "":
            self.setPoint(y_index, x_index, "P")
            self.num_pieces -= 1
            self.game()
        # setPointAsClicked(id)

    def getIndFromCoord(self, coord):
        index = 0

        loc = VARIABLES.point_location

        for r in range(7):
            if loc[r] - 20 < coord < loc[r] + 20:
                index = r
        return index

    def game(self):
        self.showSettedPoints(VARIABLES.pieces)
        threading.Timer(2, self.test).start()

        # time.sleep(2)

    def test(self):
        SetRound.setPoint()
        self.showSettedPoints(VARIABLES.pieces)

    def setPoint(self, y_index, x_index, player):
        VARIABLES.pieces[y_index][x_index] = player
        print(VARIABLES.pieces)

    def drawPoint(self, x_index, y_index, player):
        canvas.create_oval()

    def setPointAsClicked(self, number):
        counter = 0
        for r in range(len(VARIABLES.pieces)):
            for s in range(len(VARIABLES.pieces[r])):
                if VARIABLES.pieces[r][s] != "-":
                    counter += 1
                    if counter == number:
                        print(str(r) + " " + str(s))

    # https://stackoverflow.com/questions/9581384/how-to-create-a-transparent-rectangle-responding-to-click-event-in-tkinter
    def drawClickOverlay(self, grid):
        for r in range(7):
            for s in range(7):
                if grid[r][s] == 1:
                    canvas.bind("<Button-1>", self.onObjectClick)

    # entryBox = tkinter.Entry(canvas)
    # entryBox.grid(row=2, column=1)

    # for r in range(7):
    #     for c in range(7):
    #         label = tkinter.Label(canvas, text='R%s/C%s' % (r, c),
    #                               borderwidth=1, background="black").grid(row=r, column=c)

    def locationClicked(self, event, x, y):
        print("X_Location: " + str(x))
        print("Y_Location: " + str(y))
        print("------------------------")
        # print(event.widget.find_closest(event.x, event.y))

    def showSettedPoints(self, grid):

        for r in range(7):
            for s in range(7):
                if grid[r][s] == "P":
                    canvas.create_oval(VARIABLES.point_location[s] + 10,
                                       VARIABLES.point_location[r] + 10,
                                       VARIABLES.point_location[s] + 40,
                                       VARIABLES.point_location[r] + 40, width=3.5, fill='black')

                if grid[r][s] == "C":
                    canvas.create_oval(VARIABLES.point_location[s] + 10,
                                       VARIABLES.point_location[r] + 10,
                                       VARIABLES.point_location[s] + 40,
                                       VARIABLES.point_location[r] + 40, width=3.5, fill='white')

        # canvas.tag_bind(click_canvas, '<ButtonPress-1>', locationClicked(e, x=s, y=r))

    def movePoint(self, point_x, point_y):
        for r in range(7):
            for s in range(7):
                if VARIABLES.location_set[r][s] == 1:
                    if point_y == r and point_x == s:
                        VARIABLES.muehle_grid[r][s] = 0
                        VARIABLES.muehle_grid[s - 2][r - 1] = 1

    # drawClickOverlay(full_muehle_grid)
    # movePoint(3, 2)
    # showSettedPoints(VARIABLES.muehle_grid)

    # if active_player == TRUE:
    # player_display["text"] = "Aktiver Spieler: Du"

    canvas.pack(expand=YES, fill=BOTH)


m = Muehle()
