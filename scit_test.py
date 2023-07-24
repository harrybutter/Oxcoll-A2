def init_array():
    array = []
    for y in range(8):
        row = []
        for x in range(8):
            if y <= 1:
                row.append("B")
            elif y >= 6:
                row.append("W")
            else:
                row.append("E")
        array.append(row)
    return array


def validMoves(array, pieceColour, xCurrent, yCurrnet):
    xCurrent -= 1
    row = array[yCurrnet-1]
    print("Possible moves are: ")
    print("Moving LEFT")
    currentX = xCurrent
    while row[currentX-1] != pieceColour:
        if currentX == 0:
            break
        currentX -= 1
        if row[currentX] == "E":
            print(currentX+1, yCurrnet)
        else:
            print(currentX+1, yCurrnet, "REMOVE piece")
            break
    currentX = xCurrent
    print("Moving LEFT")
    while row[currentX+1] != pieceColour:
        if currentX == 7:
            break
        currentX += 1
        if row[currentX] == "E":
            print(currentX+1, yCurrnet)
        else:
            print(currentX+1, yCurrnet, "REMOVE piece")


def main():
    array = init_array()
    array[3][1] = "W"
    array[3][7] = "B"
    validMoves(array, "B", 4, 4)


main()
