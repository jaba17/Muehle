class VARIABLES:

    muehle_grid = [[1, -1, -1, 1, -1, -1, 1],
                   [-1, 1, -1, 1, -1, 1, -1],
                   [-1, -1, 1, 1, 1, -1, -1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [-1, -1, 1, 1, 1, -1, -1],
                   [-1, 1, -1, 1, -1, 1, -1],
                   [1, -1, -1, 1, -1, -1, 1]]

    full_muehle_grid = [[0, -1, -1, 0, -1, -1, 0],
                        [-1, 0, -1, 0, -1, 0, -1],
                        [-1, -1, 0, 0, 0, -1, -1],
                        [0, 0, 0, -1, 0, 0, 0],
                        [-1, -1, 0, 0, 0, -1, -1],
                        [-1, 0, -1, 0, -1, 0, -1],
                        [0, -1, -1, 0, -1, -1, 0]]

    location_set = [[1, -1, -1, 1, -1, -1, 1],
                    [0, 1, -1, 1, -1, 1, 0],
                    [-1, 0, 1, 1, 1, 0, 0],
                    [1, 1, 1, -1, 1, 0, 1],
                    [-1, 0, 1, 1, 1, 0, 0],
                    [-1, 1, -1, 1, -1, 1, 0],
                    [1, -1, -1, 1, -1, -1, 1]]

    full_location_set = [[1, -1, -1, 1, -1, -1, 1],
                         [0, 1, -1, 1, -1, 1, 0],
                         [-1, 0, 1, 1, 1, 0, 0],
                         [1, 1, 1, -1, 1, 0, 1],
                         [-1, 0, 1, 1, 1, 0, 0],
                         [-1, 1, -1, 1, -1, 1, 0],
                         [1, -1, -1, 1, -1, -1, 1]]

    # "": nicht gesetzt
    # "C": Computer
    # "P": Player
    # "-": Nicht möglic
    pieces = [["", "-", "-", "", "-", "-", ""],
              ["-", "", "-", "", "-", "", "-"],
              ["-", "-", "", "", "", "-", "-"],
              ["", "", "", "-", "", "", ""],
              ["-", "-", "", "", "", "-", "-"],
              ["-", "", "-", "", "-", "", "-"],
              ["", "-", "-", "", "-", "-", ""]]

    # adj_mat = [[[1, 1, -1, -1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, -1], [-1, 1, 1, -1], [0, 0, 0, 0], [-1, 1, 1, -1]],
    #            [[0, 0, 0, 0], [1, 1, -1, -1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [-1, 1, 1, -1], [0, 0, 0, 0]],
    #            [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, -1, -1], [1, -1, 1, 1], [-1, 1, 1, -1]]]

    setzenTest = [["P", "-", "-", "P", "-", "-", ""],
                  ["-", "", "-", "", "-", "", "-"],
                  ["-", "-", "P", "", "", "-", "-"],
                  ["P", "", "P", "-", "", "", "P"],
                  ["-", "-", "", "", "", "-", "-"],
                  ["-", "", "-", "", "-", "", "-"],
                  ["", "-", "-", "C", "-", "-", ""]]

    point_location = [20, 135, 255, 430, 590, 715, 835]

    mills_horizontal = [[[0, 0], [0, 3], [0, 6]],
                        [[1, 1], [1, 3], [1, 5]],
                        [[2, 2], [2, 3], [2, 4]],
                        [[3, 0], [3, 1], [3, 2]], [[3, 4], [3, 5], [3, 6]],
                        [[4, 2], [4, 3], [4, 4]],
                        [[5, 1], [5, 3], [5, 5]],
                        [[6, 0], [6, 3], [6, 6]]]

    mills_vertical = [[[0, 0], [3, 0], [6, 0]],
                      [[1, 1], [3, 1], [5, 1]],
                      [[2, 2], [3, 2], [4, 2]],
                      [[0, 3], [1, 3], [2, 3]], [[4, 3], [5, 3], [6, 3]],
                      [[2, 4], [3, 4], [4, 4]],
                      [[1, 5], [3, 5], [5, 5]],
                      [[0, 6], [3, 6], [6, 6]]]

    mills = []

    points = []

    activeMillIndex = 0

    # Hiermit werden die Spielmodi gemanaged
    # Spielmodus 1: Setzen
    # Spielmodus 2: Bewegen
    # Spielmodus 3: Springen
    gamemode = 1

    active_player = "P"
