from random import randint

from Functions import *


# Gibt alle freien äußersten Eckenpunkte des Spielfeldes zurück
def checkCorners():
    possible_corners = []

    if VARIABLES.pieces[0][0] == "":
        possible_corners.append([0, 0])
    if VARIABLES.pieces[0][6] == "":
        possible_corners.append([0, 6])
    if VARIABLES.pieces[6][6] == "":
        possible_corners.append([6, 6])
    if VARIABLES.pieces[6][0] == "":
        possible_corners.append([6, 0])

    return possible_corners


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
    forbidden_points = []
    accepted_points = []
    point_to_delete = [-1, -1]
    # Ermittelt alle Punkte, die nicht besetzt werden dürfen, da sie Teil einer Mühle sind
    for r in range(len(VARIABLES.mills_horizontal)):
        if VARIABLES.pieces[VARIABLES.mills_horizontal[r][0][0]][VARIABLES.mills_horizontal[r][0][1]] == "P" and \
                VARIABLES.pieces[VARIABLES.mills_horizontal[r][1][0]][VARIABLES.mills_horizontal[r][1][1]] == "P" and \
                VARIABLES.pieces[VARIABLES.mills_horizontal[r][1][0]][VARIABLES.mills_horizontal[r][2][1]] == "P":
            forbidden_points.append(VARIABLES.mills_horizontal[r][0])
            forbidden_points.append(VARIABLES.mills_horizontal[r][1])
            forbidden_points.append(VARIABLES.mills_horizontal[r][2])

    for r in range(len(VARIABLES.mills_vertical)):
        if VARIABLES.pieces[VARIABLES.mills_vertical[r][0][0]][VARIABLES.mills_vertical[r][0][1]] == "P" and \
                VARIABLES.pieces[VARIABLES.mills_vertical[r][1][0]][VARIABLES.mills_vertical[r][1][1]] == "P" and \
                VARIABLES.pieces[VARIABLES.mills_vertical[r][1][0]][VARIABLES.mills_vertical[r][2][1]] == "P":
            forbidden_points.append(VARIABLES.mills_vertical[r][0])
            forbidden_points.append(VARIABLES.mills_vertical[r][1])
            forbidden_points.append(VARIABLES.mills_vertical[r][2])


    # Ermittelt alle erlaubten Punkte
    for r in range(len(VARIABLES.pieces)):
        for s in range(len(VARIABLES.pieces[r])):
            if VARIABLES.pieces[r][s] == "P":
                if [r, s] not in forbidden_points:
                    accepted_points.append([r, s])

    print(accepted_points)
    # sucht die Eckpunkte aus
    for r in range(len(accepted_points)):
        if accepted_points[r] == [0, 0]:
            print("Eckpunkt 0/0")

        if accepted_points[r] == [0, 6]:
            print("Eckpunkt 0/6")

        if accepted_points[r] == [6, 0]:
            print("Eckpunkt 6/0")

        if accepted_points[r] == [6, 6]:
            print("Eckpunkt 6/6")
            # point_to_delete == [0, 0]
    # print(accepted_points)

    #
        # if accepted_points[r] in


def missingMiddle():
    locations = Functions.describeBoard(VARIABLES.pieces)
    # self.checkForMills(locations)
    Functions.checkForMills(locations, "P")
    for r in range(len(VARIABLES.mills_horizontal)):
        span_sum = VARIABLES.mills_horizontal[r][2][1] - VARIABLES.mills_horizontal[r][0][1]
        middle_index = int(VARIABLES.mills_horizontal[r][0][1]+span_sum/2)
        print(str(VARIABLES.mills_horizontal[r][1][0])+"/"+str(middle_index))
        for s in range(len(VARIABLES.mills)):
            if [VARIABLES.mills_horizontal[r][1][0], middle_index] == VARIABLES.mills[s][2]:
                print("df")

def missingRight():
    locations = Functions.describeBoard(VARIABLES.pieces)
    # self.checkForMills(locations)
    Functions.checkForMills(locations, "P")
    for r in range(len(VARIABLES.mills_horizontal)):
        for s in range(len(VARIABLES.points)-1):
            if locations[s][0] == "P":
                if [[locations[s][1], locations[s][2]], [locations[s+1][1], locations[s+1][2]]] == [VARIABLES.mills_horizontal[r][0], VARIABLES.mills_horizontal[r][1]]:
                    print("df")
    pass


def missingLeft():

    pass

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
        # removeEnemyPoint()
        # print(recognizePossibleMills())
        # removeEnemyPoint()
        missingRight()
    @staticmethod
    def setPoint():

        point = [-1][-1]

        # Bei jeder Runde werden zuerst mögliche Mühlen des Gegners überprüft
        # if analyzeEnemyMill() ==
        # Wenn der Gegner fast eine Mühle gebaut hat wird diese verschlossen.
        # TODO: Verschließen

        # Anschließend wird überprüft, ob Ecken frei sind
        possible_corners = checkCorners()
        if possible_corners:
            rand_corner_index = randint(0, len(possible_corners) - 1)

            # Wemm ja wird dorthin ein Spielstein gesetzt
            point = possible_corners[rand_corner_index]
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
