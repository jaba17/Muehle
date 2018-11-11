from VARIABLES import *


def movePoint(point_x, point_y):
    for r in range(7):
        for s in range(7):
            if VARIABLES.location_set[r][s] == 1:
                if point_y == r and point_x == s:
                    VARIABLES.muehle_grid[r][s] = 0
                    VARIABLES.muehle_grid[s - 2][r - 1] = 1
