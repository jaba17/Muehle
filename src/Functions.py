from VARIABLES import *


class Functions:

    def __init__(self):
        self.checkNeighbours(2, 3)

    # beschreibt die Steine, welche sich auf dem Brett befinden in der jeweiligen Schreibweise (siehe Konzept)
    def describeBoard(self, mat):
        board_array = []
        i = 4

        for r in range(7):
            for s in range(7):
                if mat[r][s] == "P" or mat[r][s] == "C":
                    board_array.append([mat[r][s], r, s])
                    #   board_array[i] = board_array[i] = [mat[r][s], r, s]
                    i += 1
        return board_array

    def locIsPossible(self, x_koord, y_koord):
        if VARIABLES.pieces[y_koord][x_koord] == "":
            return True
        else:
            return False

    # überprüft die Nachbarsteine eines Feldes mit den Koordinaten x_coord und y_coord
    def checkNeighbours(self, x_coord, y_coord):

        self.checkDirection(y_coord, x_coord, "u")
        self.checkDirection(y_coord, x_coord, "d")
        self.checkDirection(y_coord, x_coord, "l")
        self.checkDirection(y_coord, x_coord, "r")

    # überprüft, ob der nächste mögliche Punkt möglich ist, also ob dort schon ein Spielstein ist
    def checkDirection(self, x_coord, y_coord, dir):
        print(self.nextPossiblePoint(x_coord, y_coord, dir))

    # sucht den nächsten Punkt auf dem Brett
    def nextPossiblePoint(self, x_koord, y_koord, dir):
        returnvalue = [-1, -1]
        if dir == 'u':
            counter = 1
            while counter <= y_koord:

                if VARIABLES.pieces[y_koord][x_koord - counter] != "-":
                    print("Nächster Punkt: (" + str(y_koord - counter), "/" + str(x_koord) + ")")
                    returnvalue = [y_koord - counter, x_koord]
                    break

                else:
                    counter += 1

        if dir == 'd':
            counter = 1
            while counter <= y_koord:

                if VARIABLES.pieces[y_koord + counter][x_koord] != "-":
                    print("Nächster Punkt: (" + str(y_koord + counter), "/" + str(x_koord) + ")")
                    returnvalue = [y_koord + counter, x_koord]
                    break

                else:
                    counter += 1

        if dir == 'l':
            counter = 1
            while counter <= y_koord:

                if VARIABLES.pieces[y_koord][x_koord - counter] != "-":
                    print("Nächster Punkt: (" + str(y_koord), "/" + str(x_koord - counter) + ")")
                    returnvalue = [y_koord, x_koord - counter]
                    break

                else:
                    counter += 1

        if dir == 'r':
            counter = 1
            while counter <= y_koord:

                if VARIABLES.pieces[y_koord][x_koord - counter] != "-":
                    print("Nächster Punkt: (" + str(y_koord), "/" + str(x_koord + counter) + ")")
                    returnvalue = [y_koord, x_koord - counter]
                    break

                else:
                    counter += 1

        print(returnvalue)
        return returnvalue


var = Functions()
