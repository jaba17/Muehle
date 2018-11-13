from core.VARIABLES import *


def isPossible(from_loc, to_loc):
    # Prüft, ob diagonal gezogen werden kann
    returnvalue = False
    if VARIABLES.muehle_grid[to_loc[0]][to_loc[1]] != -1:

        if from_loc[0] == to_loc[0]:
            i = 0
            while i < to_loc[0]-from_loc[0]:
                i += 1
            print("Possible")

        if from_loc[1] == to_loc[1]:

            i = 0
            while i < to_loc[0]-from_loc[0]:
                i += 1

            if VARIABLES.pieces[to_loc[0]][to_loc[1]]:
                returnvalue = True
        else:
            print("not possible")
            returnvalue = False

    return returnvalue


class MoveRound:

    def __init__(self):
        print(isPossible([0, 0], [0, 3]))

    @staticmethod
    def movePoint(point_x, point_y):
        for r in range(7):
            for s in range(7):
                if VARIABLES.location_set[r][s] == 1:
                    if point_y == r and point_x == s:
                        VARIABLES.muehle_grid[r][s] = 0
                        VARIABLES.muehle_grid[s - 2][r - 1] = 1


mr = MoveRound()
