from VARIABLES import *


class CheckSetPoints:

    def __init__(self):

        # checkMatrix(pieces)

        locations = self.describeBoard(VARIABLES.pieces)
        self.checkForMills(locations)
        # self.convertMatrix(VARIABLES.pieces)
        # self.checkPoints(locations)

    def checkPoints(self, pnts):
        print("Set points:")
        print(pnts)
        print("----------------------------------------------")
        print("Mills: ")
        self.checkForMill(pnts)
        print("----------------------------------------------")

    def checkForDoubleMill(self, pnts):
        return pnts

    def checkForMill(self, pnts):
        print("\tNormal Mill:");
        print("\t----------------------------------------------")

        # Horizontale Suche nach möglichen Mühlen
        print("\t\tHorizontal:")
        num_neighbours = 0

        for r in range(len(pnts)):
            counter = 0

            if pnts[r][1] < 5:

                jumploc = 0
                if pnts[r][1] == 0 or pnts[r][1] == 6:
                    jumploc = 1

                if pnts[r][0] == "P":
                    # num_to_compare = pnts[r][2]
                    # num_to_compare += 1
                    # i=0
                    # while not num_to_compare == pnts[r + 1][2]:
                    #   i += 1
                    #   num_to_compare += 1
                    #   print("Zwei player")

                    if pnts[r + jumploc][2] - pnts[r][2] == 1:
                        num_neighbours += 1

                        if pnts[r + 2][2] - pnts[r + 1][2] == 1:
                            # num_neighbours += 1
                            print("Muehle für P von (" + str(pnts[r][1]) + "/" + str(pnts[r][2]) + ") bis (" + str(
                                pnts[r + 2][1]) + "/" + str(pnts[r + 2][2]) + ").")
                            r += 2

                        else:
                            print("2 nebeneinander für P")

                # if num_neighbours == 1:

                # if num_neighbours == 2:
                # print("Muehle für P")
                # num_neighbours = 0

            if counter == 0:
                print("Keine Gefahr")

            elif counter == 1:
                print("Mittlere Gefahr")

            elif counter == 2:
                print("Gefahr!!!")

    print("----------------------------------------------")

    # Vertikale Suche nach möglichen Mühlen
    # print("Vertikal")
    # for r in range(len(pnts)):
    #     counter = 0

    #     for s in range(7):

    def dangerIndicator(runthroughType, count):
        if count == 0:
            print("Keine Gefahr")

        elif count == 1:
            print("Mittlere Gefahr")

        elif count == 2:
            print("Gefahr!!!")

    # Beschreibt gesetzten Spielsteine (P = Spieler, C = Computer) sowie deren x und y Werte

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

        VARIABLES.points = board_array
        return board_array

    def convertMatrix(self, mat):
        for r in range(7):
            for s in range(7):
                if mat[r][s] == "-":
                    i = s
                    while mat[r][i] == "-" and i < 7:
                        i += 1

    # Bei dieser Methode wird der
    def checkForMills(self, pnts):
        comparison_mills_h = VARIABLES.mills_horizontal
        comparison_mills_v = VARIABLES.mills_vertical

        # horizontale Prüfung
        print("Horizontal: ");
        for m in range(len(comparison_mills_h)):
            counter = 0
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0

            for r in range(len(pnts)):
                if pnts[r][0] == "P":
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
                print("Mühle von (" + str(x1) + "/" + str(y1) + ") bis (" + str(x2) + "/" + str(y2) + ")")
                VARIABLES.mills.append("P")
                VARIABLES.mills.append([['i', x1, y1], ['i', x2, y2]])
                print(VARIABLES.mills)
        print("---------------------------------------------------------------------------------------------")
        # --------------------------------------------------------------------------------------------------------------------
        # vertikale Prüfung
        print("Vertikal: ")
        for m in range(len(comparison_mills_v)):
            counter = 0
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0

            for r in range(len(pnts)):
                if pnts[r][0] == "P":
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
                print("Mühle von (" + str(x1) + "/" + str(y1) + ") bis (" + str(x2) + "/" + str(y2) + ")")

                # if comparison_mills[m][1][0] == pnts[r+1][1] and comparison_mills[m][1][1] == pnts[r+1][2]:
                #  print("Two point of a Mill in common")
                # if comparison_mills[m][1][0] == pnts[r+2][1] and comparison_mills[m][1][1] == pnts[r+2][2]:
                # print("Two point of a Mill in common")


check = CheckSetPoints()
