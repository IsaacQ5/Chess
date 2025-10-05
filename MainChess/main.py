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
        print("make a valid move debug 2")

#checks if the peice can move 
def checkPeice(startingRow, startingCol, endRow, endCol):
    peice = boardlayout[startingRow][startingCol]
    if peice == 'WP' or peice == "BP":
        return checkPawn(startingRow, startingCol, endRow, endCol)

def checkPawn(startingRow, startingCol, endRow, endCol):
    #movement for the white pawn
    if boardlayout[startingRow][startingCol] == 'WP':
     #going straight 
        if (startingCol == endCol and startingRow > endRow):
            #if anything is infront of the peice
            if (boardlayout[startingRow-1][startingCol]=='--'):
                #if the player wants to move 2 squares
                if startingRow == 6 and startingRow - endRow == 2:
                    #if nothing is front of two sqaures 
                    if(boardlayout[startingRow-2][startingCol]=='--'):
                        print("here")
                        return True
                elif startingRow - endRow == 1:    
                    return True
        elif (startingRow > endRow):
            #going to the right
            if (startingCol - endCol<0):
                #only moving one space 
                if (startingRow < endRow):
                    #checking if a peice is there
                    if(boardlayout[endRow][endCol] != '--'):
                        return True
        return NotAMove('pawn')
    #movement for the black pawn
    else:
        #going straight 
        if (startingRow < endRow):
            #if anything is infront of the peice
            if (boardlayout[startingRow+1][startingCol]=='--'):
                #if the player wants to move 2 squares
                if startingRow == 1 and startingRow - endRow == -2:
                    #if nothing is front of two sqaures 
                    if(boardlayout[startingRow+2][startingCol]=='--'):
                        return True
                elif startingRow - endRow == -1:    
                    return True
    return NotAMove('pawn')

def NotAMove(name):
    print(f'Piece is blocking the {name}')
    return False

def end(inputs):
    if 'kill' in inputs:
        print("Program killed")
        return True

def Main():
    while True:
        #for formating the list into a board 
        for line in range(len(boardlayout)):
            print(boardlayout[line])    
        vaildNumber = list(range(0,9))
        #getting inputs 
        SR = int(input("what is the row your peice is on: "))
        if (end(str(SR))):
            break
        SC = int(input("What is the col that your peice is on: "))
        if (end(str(SC))):
            break
        ER = int(input("What is the row you want your peice to go: "))
        if (end(str(ER))):
            break
        EC = int(input("What is the col you want your peice to go: "))
        if (end(str(EC))):
            break
        elif (int(SR) in vaildNumber and SC in vaildNumber and ER in vaildNumber and EC in vaildNumber):
            movePeice(SR,SC,ER,EC)
        else:
            print("Put in a vaild number debug 1")
            
Main()