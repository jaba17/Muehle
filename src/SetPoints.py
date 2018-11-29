from Functions import *


class SetPoints:

    def __init__(self):
        # checkMatrix(pieces)

        locations = func.describeBoard(VARIABLES.pieces)
        print(locations)
        self.setPoint(locations)

        # self.convertMatrix(VARIABLES.pieces)
        # self.checkPoints(locations)

    def setPoint(self, pnts):
        # Prüfung ob fast eine Mühle gebaut wurde
        comparison_mills_h = VARIABLES.mills_horizontal
        comparison_mills_v = VARIABLES.mills_vertical
        # horizontale Prüfung
        print("Horizontal: ")
        for m in range(len(comparison_mills_h)):
            counter = 0
            for r in range(len(pnts)):
                if pnts[r][0] == "P":
                    if comparison_mills_h[m][0][0] == pnts[r][1] and comparison_mills_h[m][0][1] == pnts[r][2]:
                        counter += 1
                    if comparison_mills_h[m][1][0] == pnts[r][1] and comparison_mills_h[m][1][1] == pnts[r][2]:
                        counter += 1

            if counter == 2:
                print("fast mühle")


func = Functions()

sp = SetPoints()
