def makeList2():
    # source https://stackoverflow.com/questions/17636567/python-initialize-multi-dimensional-list
    print("\nmakeList3");
    numCols=3
    numRows=6
    board = [[0] * numCols for i in range(numRows)]
    board[2][1] = 6 # row 2 colum 1
    print(board)

def makeList1():
    # source https://stackoverflow.com/questions/24023115/how-to-initialise-a-2d-array-in-python
    print("\nmakeList1");
    board = []
    numRows=6
    numCols=3
    for i in range(numRows):
        board.append([])
        for j in range(numCols):
            board[i].append(0)
    board[2][1] = 6 # row 2 colum 1
    print(board)

# function to run the program 
def main():
    makeList1()
    makeList2()
    



# Executes the main function 
if __name__ == '__main__': 
    main() 