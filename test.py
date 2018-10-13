multd = [[1, -1, -1, 1, -1, -1, 1],
         [1, 1, -1, 1, -1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, -1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1],
         [1, 1, -1, 1, -1, 1, 1],
         [1, -1, -1, 1, -1, -1, 1]]

point_location = [32, 141, 250, 405, 549, 659, 767]

# Die vom Spieler gesetzten Punkte werden in diesem Array gespeichert
# 0: kein Punkt gesetzt
# 1: Punkt gesetzt
# -1: Setzen nicht möglich
location_set = [[0, -1, -1, 0, -1, -1, 0],
                [0, 0, -1, 0, -1, 0, 0],
                [1, 0, 1, 0, 0, 0, 0],
                [1, 0, 0, -1, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [0, 0, -1, 0, -1, 0, 0],
                [0, -1, -1, 0, -1, -1, 0]]


cleaned_location_set = [[0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0]]


def setLocation(x_location, y_location):
    location_set[x_location][y_location] = 1


#def cleanLocationSet():
#    for r in range(7):
#        for s in range(7):
#            if location_set[r][s] == -1
#        print(location_set[r])

def showLocationSet():
    for r in range(7):
        print(location_set[r])


def checkForMill():
    for r in range(7):
        for s in range(len(cleaned_location_set[r])):
            if cleaned_location_set[r][s] == 1 and cleaned_location_set[r][s + 1] == 1 and cleaned_location_set[r][s + 2] == 1 \
                    or cleaned_location_set[r][s] == 1 and cleaned_location_set[r + 1][s] == 1 and cleaned_location_set[r+2][s] == 1:
                        print("Mill")


checkForMill()
