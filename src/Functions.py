from VARIABLES import *


class Functions:

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


var = Functions()
