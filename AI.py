import numpy


def checkMatrix(mat):
    print("----------------------------------------------")

    # Horizontale Suche nach möglichen Mühlen
    print("Horizontal")
    for r in range(7):
        counter = 0

        for s in range(7):

            if mat[r][s] == "P":
                counter += 1

        if counter == 0:
            print("Keine Gefahr")

        elif counter == 1:
            print("Mittlere Gefahr")

        elif counter == 2:
            print("Gefahr!!!")

    print("----------------------------------------------")

    # Vertikale Suche nach möglichen Mühlen
    print("Vertikal")
    for r in range(7):
        counter = 0

        for s in range(7):

            if mat[s][r] == "P":
                counter += 1

        print(dangerIndicator("vertikal", counter))


def dangerIndicator(runthroughType, count):
    if count == 0:
        print("Keine Gefahr")

    elif count == 1:
        print("Mittlere Gefahr")

    elif count == 2:
        print("Gefahr!!!")


def describeBoard(mat):

    board_array = numpy.array([["P", 4, 5]])
    # board_array = [[0 for x in range(5)] for y in range(40)]
    i = 1

    for r in range(7):
        for s in range(7):
            if mat[r][s] == "P" or mat[r][s] == "C":

                numpy.append(board_array, [[mat[r][s], r, s]], 1)
            #    board_array[i] = board_array[i] = [mat[r][s], r, s]
                i += 1
    return board_array


class AI:

    def __init__(self):
        pieces = [["P", "-", "-", "", "-", "-", "P"],
                  ["-", "", "-", "", "-", "", "-"],
                  ["-", "-", "", "", "", "-", "-"],
                  ["P", "", "C", "-", "", "", ""],
                  ["-", "-", "", "", "", "-", "-"],
                  ["-", "", "-", "", "-", "", "-"],
                  ["", "-", "-", "", "-", "-", ""]]

        # checkMatrix(pieces)
        print(describeBoard(pieces))


ai = AI()
