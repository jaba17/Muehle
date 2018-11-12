import threading
import tkinter
from tkinter import *
from PIL import Image
from PIL import ImageTk

from AI.AI import AI
from core.VARIABLES import *

task = ""
active_player = TRUE

canvas = Canvas(width=900, height=1000, bg='white')
canvas.grid()
image = Image.open("res/muehle_spielbrett.png")
image = image.resize((900, 900))
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(2, 2, image=image_tk, anchor=NW)


class Muehle:

    def __init__(self):

        self.num_pieces = 6
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

        self.recognizeClick()
        self.showSettedPoints(VARIABLES.pieces)
        canvas.mainloop()

    def onObjectClick(self, event):
        x = event.x - 25
        y = event.y - 25

        y_index = self.getIndexFromCoord(y)
        x_index = self.getIndexFromCoord(x)

        # "Setzenmodus"
        if VARIABLES.gamemode == 1:
            if VARIABLES.muehle_grid[y_index][x_index] == 1 and VARIABLES.pieces[y_index][x_index] == "":
                self.setPoint(y_index, x_index, "P")
                self.num_pieces -= 1
                self.showSettedPoints(VARIABLES.pieces)
                threading.Timer(2, self.game).start()

        # "Schiebmodus"
        if VARIABLES.gamemode == 2:
            if VARIABLES.pieces[y_index][x_index] == "P":
                # self.setPoint(y_index, x_index, "P")
                # self.num_pieces -= 1
                # self.showSettedPoints(VARIABLES.pieces)
                # threading.Timer(2, self.game).start()
                canvas.bind("<Button-1>", self.moveObject)
                print(x_index)

    def moveObject(self, event):
        x = event.x - 25
        y = event.y - 25

        y_index = self.getIndexFromCoord(y)
        x_index = self.getIndexFromCoord(x)

        print("move object "+str(y_index))


    def getIndexFromCoord(self, coord):
        index = 0

        loc = VARIABLES.point_location

        for r in range(7):
            if loc[r] - 20 < coord < loc[r] + 20:
                index = r
        return index

    def game(self):
        print()
        # Übergibt an die KI
            # AI.gameSet()

#         elif VARIABLES.gamemode == 2:
  #           print("GameMode2")

        # self.showSettedPoints(VARIABLES.pieces)

    def setPoint(self, y_index, x_index, player):
        VARIABLES.pieces[y_index][x_index] = player
        print(VARIABLES.pieces)

    def recognizeClick(self):
        canvas.bind("<Button-1>", self.onObjectClick)

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


    canvas.pack(expand=YES, fill=BOTH)


m = Muehle()
