from core.VARIABLES import *

# Prüft, ob diagonal gezogen werden will
def isPossible(from_loc, to_loc):
    if VARIABLES.muehle_grid[to_loc[0]][to_loc[1]] != -1:

        if from_loc[0] == to_loc[0] or from_loc[1] == to_loc[1]:
            print("Possible")
        else:
            print("not possible")


class MoveRound:

    def __init__(self):
        isPossible([0, 0], [3, 0])

    @staticmethod
    def movePoint(point_x, point_y):
        for r in range(7):
            for s in range(7):
                if VARIABLES.location_set[r][s] == 1:
                    if point_y == r and point_x == s:
                        VARIABLES.muehle_grid[r][s] = 0
                        VARIABLES.muehle_grid[s - 2][r - 1] = 1


mr = MoveRound()
