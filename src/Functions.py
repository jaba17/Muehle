from core.VARIABLES import *


class Functions:

    def __init__(self):
        self.checkNeighbours(2, 3)

    # beschreibt die Steine, welche sich auf dem Brett befinden in der jeweiligen Schreibweise (siehe Konzept)
    @staticmethod
    def describeBoard(mat):
        board_array = []
        i = 4

        for r in range(7):
            for s in range(7):
                if mat[r][s] == "P" or mat[r][s] == "C":
                    board_array.append([mat[r][s], r, s])
                    #   board_array[i] = board_array[i] = [mat[r][s], r, s]
                    i += 1
        return board_array

    @classmethod
    def locIsPossible(y_koord, x_koord):
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

        # Bei dieser Methode wird der

    @staticmethod
    def checkForMills(pnts, user):
        comparison_mills_h = VARIABLES.mills_horizontal
        comparison_mills_v = VARIABLES.mills_vertical

        # horizontale Prüfung
        for m in range(len(comparison_mills_h)):
            counter = 0
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0

            for r in range(len(pnts)):
                if pnts[r][0] == user:
                    if comparison_mills_h[m][0][0] == pnts[r][1] and comparison_mills_h[m][0][1] == pnts[r][2]:
                        x1 = pnts[r][1]
                        y1 = pnts[r][2]
                        counter += 1

                    if comparison_mills_h[m][1][0] == pnts[r][1] and comparison_mills_h[m][1][1] == pnts[r][2]:
                        counter += 1

                    if comparison_mills_h[m][2][0] == pnts[r][1] and comparison_mills_h[m][2][1] == pnts[r][2]:
                        x2 = pnts[r][1]
                        y2 = pnts[r][2]
                        counter += 1

            if counter == 2:
                print("2")
                return
            if counter == 3:
                VARIABLES.mills.append([user, [x1, y1], [x2, y2]])



        # --------------------------------------------------------------------------------------------------------------------
        # vertikale Prüfung
        for m in range(len(comparison_mills_v)):
            counter = 0
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0

            for r in range(len(pnts)):
                if pnts[r][0] == user:
                    if comparison_mills_v[m][0][0] == pnts[r][1] and comparison_mills_v[m][0][1] == pnts[r][2]:
                        x1 = pnts[r][1]
                        y1 = pnts[r][2]
                        counter += 1

                    if comparison_mills_v[m][1][0] == pnts[r][1] and comparison_mills_v[m][1][1] == pnts[r][2]:
                        counter += 1

                    if comparison_mills_v[m][2][0] == pnts[r][1] and comparison_mills_v[m][2][1] == pnts[r][2]:
                        x2 = pnts[r][1]
                        y2 = pnts[r][2]
                        counter += 1

            if counter == 2:
                print("2")
                return
            if counter == 3:
                VARIABLES.mills.append([user, [x1, y1], [x2, y2]])
                # if comparison_mills[m][1][0] == pnts[r+1][1] and comparison_mills[m][1][1] == pnts[r+1][2]:
                #  print("Two point of a Mill in common")
                # if comparison_mills[m][1][0] == pnts[r+2][1] and comparison_mills[m][1][1] == pnts[r+2][2]:
                # print("Two point of a Mill in common")

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
