from Functions import Functions
from core.VARIABLES import *


class CheckSetPoints:

    def __init__(self):

        # checkMatrix(pieces)

        locations = Functions.describeBoard(VARIABLES.pieces)
        # self.checkForMills(locations)
        Functions.checkForMills(locations)
        # self.convertMatrix(VARIABLES.pieces)
        # self.checkPoints(locations)

    def checkPoints(self, pnts):
        print("Set points:")
        print(pnts)
        print("----------------------------------------------")
        print("Mills: ")
        Functions.checkForMills(pnts)
        print("----------------------------------------------")

    def checkForDoubleMill(self, pnts):
        return pnts


check = CheckSetPoints()
