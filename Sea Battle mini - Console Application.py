#Sea Battle - Console application
import random
def setfield():
    field = [[".",".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".",".","."]]
    fieldX = field
    ships = { "1":{"1":[["", ""]], "2":[["", ""]], "3":[["", ""]], "4":[["", ""]]},
             "2":{"1":[["", ""], ["", ""]], "2":[["", ""], ["", ""]], "3":[["", ""], ["", ""]]},
             "3":{"1":[["", ""], ["", ""], ["", ""]], "2":[["", ""], ["", ""], ["", ""]]},
             "4":{"1":[["", ""], ["", ""], ["", ""], ["", ""]]} }
    #print(ships["2"]["1"][1], ships["2"]["1"])
    for s in ships:
        print(s)
        for i in ships[s]:
            print(i)
            #print(len(ships["2"]["1"]), "lal")
            if s == "1":
                #print("ship - 1")
                for r in range(len(ships[s]["1"])):
                    while True:
                        x = random.randint(0,9)
                        y = random.randint(0,9)
                        if fieldX[y][x] != "1":
                            ships[s][i][r-1][0] = x
                            ships[s][i][r-1][1] = y
                            fieldX[y][x] = "1"
                            break
            else:
                #print("ships - other")
                #print(r)
                #print(len(ships[s][i])) #all ships
                direction = 1
                while True:
                    #for t in range(0, len(ships[s][i])):
                    length = int(s)
                    x2 = None
                    y2 = None
                    if r == 0:
                        while True:
                            x2 = random.randint(0,9)
                            y2 = random.randint(0,9)
                            if fieldX[y2][x2] != "X":
                                ships[s][i][r][0] = x2
                                ships[s][i][r][1] = y2
                                fieldX[y2][x2] = "X"
                                break
                    else:
                        if direction == 1:
                            if not y2 + length > 9:
                                isX = False
                                for y in range(1, length+1):
                                    if fieldX[y2+y][x2] != "X":
                                        pass
                                    else:
                                        direction += 1
                                        isX = True
                                        break
                                if not isX:
                                    for o in range(0, length):
                                        y2 += 1
                                        ships[s][i][r][0] = y2
                                        ships[s][i][r][1] = x2
                                        fieldX[y2][x2] = "X"
                                    break
                            else:
                                direction += 1
                        elif direction == 2:
                            if not x2 + length > 9:
                                isX = False
                                for x in range(1, length + 1):
                                    if fieldX[y2][x2 + x] != "X":
                                        pass
                                    else:
                                        direction += 1
                                        isX = True
                                        break
                                if not isX:
                                    for o in range(0, length):
                                        x2 += 1
                                        ships[s][i][r][0] = y2
                                        ships[s][i][r][1] = x2
                                        fieldX[y2][x2] = "X"
                                    break
                            else:
                                direction += 1
                        elif direction == 3:
                            if not y2 - length < 0:
                                isX = False
                                for y in range(1, length + 1):
                                    if fieldX[y2 - y][x2] != "X":
                                        pass
                                    else:
                                        direction += 1
                                        isX = True
                                        break
                                if not isX:
                                    for o in range(0, length):
                                        y2 -= 1
                                        ships[s][i][r][0] = y2
                                        ships[s][i][r][1] = x2
                                        fieldX[y2][x2] = "X"
                                    break
                            else:
                                direction += 1
                        elif direction == 4:
                            if not x2 - length < 0:
                                isX = False
                                for x in range(1, length + 1):
                                    if fieldX[y2][x2 - x] != "X":
                                        pass
                                    else:
                                        direction += 1
                                        isX = True
                                        break
                                if not isX:
                                    for o in range(0, length):
                                        x2 -= 1
                                        ships[s][i][r][0] = y2
                                        ships[s][i][r][1] = x2
                                        fieldX[y2][x2] = "X"
                                    break
                            else:
                                direction += 1
    for i in range(0, len(fieldX)):
        print(fieldX[i])
setfield()