from random import randint

from VARIABLES import *
from Functions import *


def checkCorner():
    returnvalue = [-1, -1]

    if VARIABLES.pieces[0][0] == "":
        returnvalue = [0, 0]
    if VARIABLES.pieces[0][6] == "":
        returnvalue = [0, 6]
    if VARIABLES.pieces[6][6] == "":
        returnvalue = [6, 6]
    if VARIABLES.pieces[6][0] == "":
        returnvalue = [6, 0]

    return returnvalue


def recognizePossibleMills():
    points = Functions.describeBoard(VARIABLES.pieces)
    mills_horizontal = VARIABLES.mills_horizontal
    mills_vertical = VARIABLES.mills_vertical

    possible_mills = []

    for r in range(len(mills_horizontal)):
        if VARIABLES.pieces[mills_horizontal[r][0][0]][mills_horizontal[r][0][1]] == "C" or \
                VARIABLES.pieces[mills_horizontal[r][0][0]][mills_horizontal[r][0][1]] == "":
            if VARIABLES.pieces[mills_horizontal[r][1][0]][mills_horizontal[r][1][1]] == "C" or \
                    VARIABLES.pieces[mills_horizontal[r][1][0]][mills_horizontal[r][1][1]] == "":
                if VARIABLES.pieces[mills_horizontal[r][2][0]][mills_horizontal[r][2][1]] == "C" or \
                        VARIABLES.pieces[mills_horizontal[r][2][0]][mills_horizontal[r][2][1]] == "":

                    possible_mills.append(mills_horizontal[r])

                else:
                    print(" ")

            else:
                print(" ")
        #           for s in range(7):

        else:
            print("")

    return possible_mills


def createMill():
    recognizePossibleMills()

    # for r in range(len(possible_mills)):
    # print()
    # Entscheidet ob horrizontal oder vertikal


def blockEnemyMill():
    print()


def analyzeEnemyMill():
    points = Functions.describeBoard(VARIABLES.pieces)
    enemy_points = []
    for r in range(len(points)):
        if points[r][0] == "P":
            enemy_points.append([points[r][1], points[r][2]])

    for r in range(len(enemy_points)):
        for s in range(len(VARIABLES.mills_horizontal)):
            if enemy_points[r] == VARIABLES.mills_horizontal[s][0]:
                # for s in range(len(VARIABLES.mills_horizontal)):
                # for t in range(len(VARIABLES.mills_horizontal[s])):
                # for v in range(len(enemy_points)-1):
                print(enemy_points[r])

        # print(enemy_points)


def removeEnemyPoint():
    print()


class SetRound():

    def __init__(self):
        # self.blockEnemyMill()
        # self.createMill()
        print("df")

    @staticmethod
    def setPoint():
        point = [-1][-1]
        # Zuerst wird überprüft, ob Ecken frei sind
        if checkCorner() != [-1, -1]:
            point = checkCorner()

        recognizedMills = recognizePossibleMills()[1]

        VARIABLES.pieces[recognizedMills[0][0]][recognizedMills[0][1]] = "C"
        VARIABLES.pieces[recognizedMills[1][0]][recognizedMills[1][1]] = "C"
        VARIABLES.pieces[recognizedMills[2][0]][recognizedMills[2][1]] = "C"

        # Bei jeder Runde werden zudem mögliche Mühlen des Gegners überprüft
        # analyzeEnemyMill()
        # Wenn der Gegner fast eine Mühle gebaut hat wird diese verschlossen.
        # TODO: Verschließen

        recognizePossibleMills()

        # Anschließend werden Punkte zwischen zwei vorhandenen Mühlen mit einem Punkt

        if (point != [-1][-1]):
            VARIABLES.pieces[point[0]][point[1]] = "C"
            print(VARIABLES.pieces)

    # direction = randint(0,1)
    # rand_num = randint(0, len(mills_horizontal + mills_vertical))

    #        if rand_num <= len(mills_horizontal):
    #           print(mills_horizontal[rand_num])
    #      else:
    #         print(mills_vertical[rand_num])

    # nach möglichen Mühlenorten suchen


sr = SetRound()
