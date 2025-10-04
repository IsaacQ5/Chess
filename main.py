ROWS= 8
COLS = 8
boardlayout = [['--' for _ in range(COLS)] for _ in range(ROWS)]

#makes the pawns for the board 
def pawns(boardlayout):
    for pawn in range(len(boardlayout[1])):
        boardlayout[1][pawn] = 'BP'
    for pawn in range(len(boardlayout[6])):
        boardlayout[6][pawn] = 'WP'

#hard program the other peices
def otherpeices(boardlayout):
    boardlayout[0][0] = 'BR'
    boardlayout[0][1] = 'BN'
    boardlayout[0][2] = 'BB'
    boardlayout[0][3] = 'BQ'
    boardlayout[0][4] = 'BK'
    boardlayout[0][5] = 'BB'
    boardlayout[0][6] = 'BN'
    boardlayout[0][7] = 'BR'

    boardlayout[7][0] = 'WR'
    boardlayout[7][1] = 'WN'
    boardlayout[7][2] = 'WB'
    boardlayout[7][3] = 'WQ'
    boardlayout[7][4] = 'WK'
    boardlayout[7][5] = 'WB'
    boardlayout[7][6] = 'WN'
    boardlayout[7][7] = 'WR'

#put the peices in one function
def peices():
    otherpeices(boardlayout)
    pawns(boardlayout)
peices()

#function to move the peice to the sqaure it wants to go
def movePeice(startingRow, startingCol, endRow, endCol):
    if checkPeice(startingRow, startingCol, endRow, endCol):
        boardlayout[endRow][endCol] = boardlayout[startingRow][startingCol]
        boardlayout[startingRow][startingCol] = '--'
    else:
        print("make a valid move")

#checks if the peice can move 
def checkPeice(startingRow, startingCol, endRow, endCol):
    peice = boardlayout[startingRow][startingCol]
    if peice == 'WP' or peice == "BP":
        return checkPawn(startingRow, startingCol, endRow, endCol)

def checkPawn(startingRow, startingCol, endRow, endCol):
    #movement for the white pawn
    if boardlayout[startingRow][startingCol] == 'WP':
        #going straight 
        if (boardlayout[startingRow-1][startingCol]=='--'):
            if startingRow == 6:
                   #moving 2 if pawn didnt move 
                if(boardlayout[startingRow-2][startingCol]=='--'):
                    return 0 < startingRow - endRow <= 2
            return 0 < startingRow - endRow < 2
        else:
            return NotAMove('pawn')
    #movement for the black pawn
    else:
        #going straight 
        if (boardlayout[startingRow+1][startingCol]=='--'):
            if startingRow == 1:
                #moving 2 if pawn didnt move 
                if(boardlayout[startingRow-2][startingCol]=='--'):
                    return -2 <= startingRow - endRow < 0
            return -2 < startingRow - endRow < 0
        else:
            return NotAMove('pawn')

def NotAMove(name):
    print(f'Piece is blocking the {name}, make a new move')
    return False

def end(inputs):
    if inputs == 'kill':
        print("Program killed")
        return True

def Main():
    for line in range(len(boardlayout)):
            print(boardlayout[line])
    while True:
        vaildNumber = list(range(0,9))
        SR = (input("what is the row your peice is on: "))
        if (end(SR)):
            break
        SC = (input("What is the col that your peice is on: "))
        if (end(SC)):
            break
        ER = (input("What is the row you want your peice to go: "))
        if (end(ER)):
            break
        EC = (input("What is the col you want your peice to go: "))
        if (end(EC)):
            break
        elif (SR in vaildNumber and SC in vaildNumber and ER in vaildNumber and EC in vaildNumber):
            movePeice(SR,SC,ER,EC)
            for line in range(len(boardlayout)):
                print(boardlayout[line])
        else:
            print("put in a vaild number")
Main()