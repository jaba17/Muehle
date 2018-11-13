from Functions import Functions
from core.VARIABLES import VARIABLES


class AnalyzePlayBoard:

    def __init__(self):
        # print("fg")
        self.analyzeMills()

    def analyzeMills(self):
        descr = Functions.describeBoard(VARIABLES.pieces)
        Functions.checkForMills(descr, "P")
        Functions.checkForMills(descr, "C")
        print("Mills: "+str(VARIABLES.mills))


apb = AnalyzePlayBoard()
