from random import randint

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


def isPossible(point):
    if VARIABLES.pieces[point[0]][point[1]] == "":
        return True
    else:
        return False


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


def setPointAsClicked(number):
    counter = 0
    for r in range(len(VARIABLES.pieces)):
        for s in range(len(VARIABLES.pieces[r])):
            if VARIABLES.pieces[r][s] != "-":
                counter += 1
                if counter == number:
                    print(str(r) + " " + str(s))


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

    print(enemy_points)


    # if points != []:
    #    for r in range(len(VARIABLES.mills_horizontal)):
    #        if enemy_points[0] == VARIABLES.mills_horizontal[r][0] and enemy_points[1] == VARIABLES.mills_horizontal[r][1]:
    #           print("set to the right")
    #           break

    #       if enemy_points[0] == VARIABLES.mills_horizontal[r][0] and enemy_points[2] == VARIABLES.mills_horizontal[r][2]:
    #         print("set to the middle")

    # for r in range(len(enemy_points)):
    # for s in range(len(VARIABLES.mills_horizontal)):
    # for t in range(len(VARIABLES.mills_horizontal[s])):
    # if enemy_points[r] == VARIABLES.mills_horizontal[s][t]:

    # for s in range(len(VARIABLES.mills_horizontal)):
    # for t in range(len(VARIABLES.mills_horizontal[s])):
    # for v in range(len(enemy_points)-1):
    #  print(enemy_points[r])
    # print(enemy_points)

# Diese Funktion entfernt einen Stein des Gegners
def removeEnemyPoint():

    # for i in range(len(VARIABLES.pieces)):
     #    for r in range(len(VARIABLES.pieces[i])):
     #        if

    print(VARIABLES.mills)


def checkMill():
    # Nun werden alle möglichen Mühlen aufgespürt und eine zufällige ausgewählt
    recognized_mills = recognizePossibleMills()
    rand_mill = randint(0, len(recognized_mills) - 1)
    # Falls es mögliche Mühlen gibt werden diese gefüllt.
    if recognized_mills != "[]":
        mill = recognized_mills[rand_mill]
        point = mill[VARIABLES.activeMillIndex]
        # VARIABLES.pieces[recognized_mills[1][0]][recognized_mills[1][1]] = "C"
        # VARIABLES.pieces[recognized_mills[2][0]][recognized_mills[2][1]] = "C"

    # Anschließend werden Punkte zwischen zwei vorhandenen Mühlen mit einem Punkt
    if point != [-1, -1]:
        VARIABLES.pieces[point[0]][point[1]] = "C"
        VARIABLES.activeMillIndex += 1
        print(VARIABLES.pieces)


class SetRound:

    def __init__(self):
        # self.blockEnemyMill()
        # self.createMill()
        # analyzeEnemyMill()
        removeEnemyPoint()
        checkMill()

    @staticmethod
    def setPoint():

        point = [-1][-1]

        # Bei jeder Runde werden zuerst mögliche Mühlen des Gegners überprüft
        # if analyzeEnemyMill() ==
        # Wenn der Gegner fast eine Mühle gebaut hat wird diese verschlossen.
        # TODO: Verschließen

        # Anschließend wird überprüft, ob Ecken frei sind
        if checkCorner() != [-1, -1]:
            # Wemm ja wird dorthin ein Spielstein gesetzt
            point = checkCorner()
            VARIABLES.pieces[point[0]][point[1]] = "C"

        # Wenn der Computer nicht mehr weiter weiß setzt er seinen Stein auf ein zufälliges freies Feld
        else:
            found = False

            while not found:

                rand_point = [randint(0, 6), randint(0, 6)]

                if isPossible(rand_point):
                    VARIABLES.pieces[rand_point[0]][rand_point[1]] = "C"
                    found = True

    # direction = randint(0,1)
    # rand_num = randint(0, len(mills_horizontal + mills_vertical))

    #        if rand_num <= len(mills_horizontal):
    #           print(mills_horizontal[rand_num])
    #      else:
    #         print(mills_vertical[rand_num])

    # nach möglichen Mühlenorten suchen

    # wenn die KI keinen passenden Ort findet, wird ein zufälliger ausgewählt


sr = SetRound()
