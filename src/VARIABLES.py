class VARIABLES:
    cleaned_location_set = [[1, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 0, 1, 1, 1, 0, 0],
                            [1, 1, 1, 1, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [1, 0, 0]]

    full_muehle_grid = [[1, -1, -1, 1, -1, -1, 1],
                        [-1, 1, -1, 1, -1, 1, -1],
                        [-1, -1, 1, 1, 1, -1, -1],
                        [1, 1, 1, -1, 1, 1, 1],
                        [-1, -1, 1, 1, 1, -1, -1],
                        [-1, 1, -1, 1, -1, 1, -1],
                        [1, -1, -1, 1, -1, -1, 1]]

    muehle_grid = [[0, -1, -1, 0, -1, -1, 0],
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
    pieces = [["", "-", "-", "P", "-", "-", ""],
              ["-", "", "-", "P", "-", "", "-"],
              ["-", "-", "", "P", "", "-", "-"],
              ["P", "P", "", "-", "P", "P", "P"],
              ["-", "-", "", "", "", "-", "-"],
              ["-", "P", "-", "P", "-", "P", "-"],
              ["", "-", "-", "", "-", "-", ""]]

    setzenTest = [["", "-", "-", "P", "-", "-", ""],
                  ["-", "", "-", "", "-", "", "-"],
                  ["-", "-", "", "", "", "-", "-"],
                  ["P", "", "P", "-", "", "", ""],
                  ["-", "-", "", "", "", "-", "-"],
                  ["-", "", "-", "", "-", "", "-"],
                  ["", "-", "-", "", "-", "-", ""]]

    point_location = [19, 135, 255, 430, 600, 720, 840]

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