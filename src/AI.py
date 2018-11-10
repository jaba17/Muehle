import numpy


def checkPoints(pnts):
    checkForDoubleMill(pnts)
    # checkForMill(pnts)


def checkForMill(pnts):
    print("----------------------------------------------")

    # Horizontale Suche nach möglichen Mühlen
    print("Horizontal")
    num_neighbours = 0

    pieces = [["P", "P", "P", "-", "-", "P"],
              ["-", "", "-", "", "-", "", "-"],
              ["-", "-", "", "", "", "-", "-"],
              ["P", "", "C", "-", "", "", ""],
              ["-", "-", "", "", "", "-", "-"],
              ["-", "", "-", "", "-", "", "-"],
              ["", "-", "-", "", "-", "-", ""]]

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

    #         if pnts[s][r] == "P":
    #           counter += 1

    #    print(dangerIndicator("vertikal", counter))


def checkForDoubleMill(pnts):
    print(pnts)


def dangerIndicator(runthroughType, count):
    if count == 0:
        print("Keine Gefahr")

    elif count == 1:
        print("Mittlere Gefahr")

    elif count == 2:
        print("Gefahr!!!")


# Beschreibt gesetzten Spielsteine (P = Spieler, C = Computer) sowie deren x und y Werte
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


class AI:

    def __init__(self):
        pieces = [["P", "P", "P", "", "-", "-", "P"],
                  ["-", "", "-", "", "-", "", "-"],
                  ["-", "-", "", "", "", "-", "-"],
                  ["P", "", "C", "-", "", "", ""],
                  ["-", "-", "", "", "", "-", "-"],
                  ["-", "", "-", "", "-", "", "-"],
                  ["", "-", "-", "", "-", "-", ""]]

        # checkMatrix(pieces)

        locations = describeBoard(pieces)

        checkPoints(locations);


ai = AI()