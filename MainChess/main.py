ROWS= 8
COLS = 8
boardlayout = [['--' for _ in range(COLS)] for _ in range(ROWS)]
TURN = 0

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

#function to move the peice to the sqaure it wants to go
def movePeice(startingRow, startingCol, endRow, endCol):
    global TURN
    SavedPeice = boardlayout[endRow][endCol]
    if checkPeice(startingRow, startingCol, endRow, endCol):
        boardlayout[endRow][endCol] = boardlayout[startingRow][startingCol]
        boardlayout[startingRow][startingCol] = '--'
        if 'P' in boardlayout[endRow][endCol]:
            if "W" in boardlayout[endRow][endCol]:
                PawnPromotion(endRow, endCol, "W")
            else:
                PawnPromotion(endRow, endCol, "B")
    if KingInCheck():
        print("That move put your king in check, make a valid move")
        boardlayout[startingRow][startingCol] = boardlayout[endRow][endCol]
        boardlayout[endRow][endCol] = SavedPeice
        TURN -= 1
    else:
        print("make a valid move debug 2")

def KingInCheck():
    #find the kings
    WhiteKingRow = 0
    WhiteKingCol = 0
    BlackKingRow = 0
    BlackKingCol = 0
    #To break out of the loop when both kings are found
    FoundWK = False
    FoundBK = False
    #loops for king searching
    for row in range(ROWS):
        for col in range(COLS):
            if boardlayout[row][col] == 'WK':
                WhiteKingRow = row
                WhiteKingCol = col
                FoundWK = True
            elif boardlayout[row][col] == 'BK':
                BlackKingRow = row
                BlackKingCol = col
                FoundBK = True
            if FoundWK and FoundBK:
                break
    
    for row in range(ROWS):
        for col in range(COLS):
            if checkPeice(row, col, WhiteKingRow, WhiteKingCol) and TURN % 2 == 0:
                print(f"{boardlayout[row][col]} ({row},{col}) is putting the white king check")
                print(f"White King is at ({WhiteKingRow},{WhiteKingCol})")
                return True
            elif checkPeice(row, col, BlackKingRow, BlackKingCol) and TURN % 2 == 1:
                print(f"{boardlayout[row][col]} ({row},{col}) is putting the black king check")
                print(f"Black King is at ({BlackKingRow},{BlackKingCol})")
                return True
    return False

#checks if the peice can move 
def checkPeice(startingRow, startingCol, endRow, endCol):
    peice = boardlayout[startingRow][startingCol]
    #Pawn moves
    if peice == 'WP' or peice == "BP":
        return checkPawn(startingRow, startingCol, endRow, endCol)
    #Rook moves
    elif peice == 'WR' or peice == 'BR':
        return checkRook(startingRow, startingCol, endRow, endCol)
    #Bishop moves
    elif peice == 'WB' or peice == 'BB':
        return checkBishop(startingRow, startingCol, endRow, endCol)
    #Knight moves
    elif peice == 'WN' or peice == 'BN':
        return checkKnight(startingRow, startingCol, endRow, endCol)
    #Queen moves
    elif peice == 'WQ' or peice == 'BQ':
        return checkQueen(startingRow, startingCol, endRow, endCol)
    #King moves
    elif peice == 'WK' or peice == 'BK':
        return checkKing(startingRow, startingCol, endRow, endCol)
    else:
        return False 

def checkKing(startingRow, startingCol, endRow, endCol):
    if [startingRow, startingCol] != [endRow, endCol]:
        if (abs(startingRow - endRow) == 1 or startingRow - endRow == 0) and (abs(startingCol - endCol) == 1 or startingCol - endCol == 0): 
            if 'W' in boardlayout[startingRow][startingCol] and 'W' not in boardlayout[endRow][endCol]:
                return True 
            elif 'B' in boardlayout[startingRow][startingCol] and'B' not in boardlayout[endRow][endCol]:
                return True
            return False
        return False 
    return False 

def checkQueen(startingRow, startingCol, endRow, endCol):
    if boardlayout[startingRow][startingCol] == 'WQ':
        if RookMove(startingRow, startingCol, endRow, endCol, "W") or BishopMove(startingRow, startingCol, endRow, endCol, "W"):
            return True
        return False
    else:
        if RookMove(startingRow, startingCol, endRow, endCol, "B") or BishopMove(startingRow, startingCol, endRow, endCol, "B"):
            return True
        return False
    
def checkKnight(startingRow, startingCol, endRow, endCol):
    if boardlayout[startingRow][startingCol] == 'WN':
        return KnightMove(startingRow,startingCol, endRow, endCol, "W")
    else:
        return KnightMove(startingRow, startingCol, endRow, endCol, "B")

def KnightMove(startingRow, startingCol, endRow, endCol, color):
    #going up

    if startingRow - 2 == endRow:
        #going right 
        if startingCol + 1 == endCol and color not in boardlayout[endRow][endCol]:

            return True
        #going left
        elif startingCol - 1 == endCol and color not in boardlayout[endRow][endCol]:
            return True
        return False 
    #going down 
    elif startingRow + 2 == endRow:
        #going right 
        if startingCol + 1 == endCol and color not in boardlayout[endRow][endCol]:
            return True
        #going left
        elif startingCol - 1 == endCol and color not in boardlayout[endRow][endCol]:
            return True
        return False
    #going to the right 
    elif startingCol + 2 == endCol:
        #going up
        if startingRow - 1 == endRow and color not in boardlayout[endRow][endCol]:
            return True
        #going down
        elif startingRow + 1 == endRow and color not in boardlayout[endRow][endCol]:
            return True 
        return False 
    #going to the left
    elif startingCol - 2 == endCol:
        #going up
        if startingRow - 1 == endRow and color not in boardlayout[endRow][endCol]:
            return True
        #going down
        elif startingRow + 1 == endRow and color not in boardlayout[endRow][endCol]:
            return True 
        return False 


def checkBishop(startingRow, startingCol, endRow, endCol):
    if boardlayout[startingRow][startingCol] == "WB":
        return BishopMove(startingRow, startingCol, endRow, endCol, "W")
    else:
        return BishopMove(startingRow, startingCol, endRow, endCol, "B")

def BishopMove(startingRow, startingCol, endRow, endCol, color):
    #going to the left up
    if startingRow - endRow > 0 and startingCol - endCol > 0:
        for i in range(abs(startingRow - endRow)-1):
            if ((startingRow - 1- i) < 0 or (startingCol -1 -i)<0) or boardlayout[startingRow - 1 - i][startingCol - 1 - i] != '--' or color in boardlayout[startingRow - 1 - i][startingCol - 1 - i]:
                return False
        if (startingRow - abs(startingRow - endRow) < 0 or startingCol - abs(startingRow - endRow) < 0) or boardlayout[startingRow - abs(startingRow - endRow)][startingCol - abs(startingRow - endRow)] != boardlayout[endRow][endCol]:
            return False
        if(color in boardlayout[endRow][endCol]):
            return False
        else:
            return True 
    #going to the right up 
    elif startingRow - endRow > 0 and startingCol - endCol < 0:
        for i in range(abs(startingRow - endRow)-1):
            if ((startingRow - 1 - i) < 0 or (startingCol + 1 + i) > 7) or boardlayout[startingRow - 1 -i][startingCol + 1 + i] != '--' or color in boardlayout[startingRow - 1 -i][startingCol + 1 + i]:
                return False
        if (startingRow - abs(startingRow - endRow) < 0 or startingCol + abs(startingRow - endRow) > 7) or  boardlayout[startingRow - abs(startingRow - endRow)][startingCol + abs(startingRow - endRow)] != boardlayout[endRow][endCol]:
            return False
        if(color in boardlayout[endRow][endCol]):
            return False
        else:
            return True 
    #Going to the left down
    elif startingRow - endRow < 0 and startingCol - endCol > 0:
        for i in range(abs(startingRow - endRow)-1):
            if ((startingRow +1 +i) >7 or (startingCol -1 -i)<0) or boardlayout[startingRow + 1 +i][startingCol - 1 - i] != '--' or color in boardlayout[startingRow + 1 +i][startingCol - 1 - i]:
                return False
        if (startingRow + abs(startingRow - endRow) > 7 or startingCol - abs(startingRow - endRow)< 0) or  boardlayout[startingRow + abs(startingRow - endRow)][startingCol - abs(startingRow - endRow)] != boardlayout[endRow][endCol]:
            return False
        if(color in boardlayout[endRow][endCol]):
            return False
        else:
            return True 
    #going to the right down
    elif startingRow - endRow < 0 and startingCol - endCol < 0:
        for i in range(abs(startingRow - endRow)-1):
            if  ((startingRow + 1 + i) > 7 or (startingCol + 1 + i) > 7) or boardlayout[startingRow + 1 +i][startingCol + 1 + i] != '--' or color in boardlayout[startingRow + 1 +i][startingCol + 1 + i]:
                return False
        if ((startingRow + abs(startingRow - endRow)) > 7 or (startingCol + abs(startingRow - endRow) > 7)) or boardlayout[startingRow + abs(startingRow - endRow)][startingCol + abs(startingRow - endRow)] != boardlayout[endRow][endCol]:
            return False 
        if(color in boardlayout[endRow][endCol]):
            return False
        else:
            return True   
    
    
    
def checkRook(startingRow, startingCol, endRow, endCol):
    
    if boardlayout[startingRow][startingCol] == 'WR':
        return RookMove(startingRow, startingCol, endRow, endCol, 'W')
    
    else:
        return RookMove(startingRow, startingCol, endRow, endCol, 'B')

def RookMove(startingRow, startingCol, endRow, endCol, color):
    # For left to Right movement
    if startingRow == endRow : 
        #check if there are peices in the way going to the right 
        if startingCol - endCol < 0:
            #check each sqaure for the right
            for col in range(endCol - startingCol):
                if boardlayout[startingRow][startingCol+1 + col] != '--':
                    if boardlayout[startingRow][startingCol + abs(endCol - startingCol)] != boardlayout[startingRow][startingCol+1 + col] or color in boardlayout[startingRow][startingCol+1 + col]:
                        return False
            return True
        else:
            #check each sqaure for the left 
            for col in range(startingCol - endCol):
                if boardlayout[startingRow][startingCol-1 -col] != '--':
                    if boardlayout[startingRow][startingCol - abs(startingCol - endCol)] != boardlayout[startingRow][startingCol -1 -col] or color in boardlayout[startingRow][startingCol-1 -col]:
                        return False 
            return True  
    elif startingCol == endCol:
        #check if there are peices in the way going up
        if startingRow - endRow < 0:
            #check each sqaure for the going up
            for row in range(endRow - startingRow): 
                if boardlayout[startingRow + 1 + row][startingCol] != '--':
                    if boardlayout[startingRow + abs(endRow- startingRow)][startingCol] != boardlayout[startingRow + 1 + row][startingCol] or color in boardlayout[startingRow + 1 + row][startingCol]:
                        return False
            return True
        #check if there are peices in the way of going down
        else:
            #check each sqaure for going down
            for row in range(startingRow - endRow):
                if boardlayout[startingRow - 1 - row][startingCol] != '--':
                    if boardlayout[startingRow - abs(endRow- startingRow)][startingCol] != boardlayout[startingRow - 1 - row][startingCol] or color in boardlayout[startingRow - 1 - row][startingCol]:
                        return False 
            return True
    return False  

def checkPawn(startingRow, startingCol, endRow, endCol):
    #movement for the white pawn
    if boardlayout[startingRow][startingCol] == 'WP':
        return whitePawn(startingRow, startingCol, endRow, endCol)
    
    
    #movement for the black pawn
    else:
        return blackPawn(startingRow, startingCol, endRow, endCol)

def whitePawn(startingRow, startingCol, endRow, endCol):
    
     #going straight 
        if (startingCol == endCol and startingRow > endRow):
            #if anything is infront of the peice
            if (boardlayout[startingRow-1][startingCol]=='--'):
                #if the player wants to move 2 squares
                if startingRow == 6 and startingRow - endRow == 2:
                    #if nothing is front of two sqaures 
                    if(boardlayout[startingRow-2][startingCol]=='--'):
                        return True
                elif startingRow - endRow == 1:    
                    return True
        #taking a peice 
        elif (startingRow - endRow == 1):
             #only moving one space 
            if (abs(startingCol - endCol)==1):
                if (startingRow > endRow):
                    #checking if a peice is there
                    if(boardlayout[endRow][endCol] != '--' and 'W' not in boardlayout[endRow][endCol]):
                        return True
    # en passant
        if (startingRow == 3 and endRow == 2 and abs(startingCol - endCol) == 1):
            if (boardlayout[3][endCol] == 'BP' and boardlayout[2][endCol] == '--'):
                boardlayout[3][endCol] = '--'
                return True
        return NotAMove('pawn')
                
def blackPawn(startingRow, startingCol, endRow, endCol):
    #going straight 
        if (startingCol == endCol and startingRow < endRow):
            #if anything is infront of the peice
            if (boardlayout[startingRow+1][startingCol]=='--'):
                #if the player wants to move 2 squares
                if startingRow == 1 and startingRow - endRow == -2:
                    #if nothing is front of two sqaures 
                    if(boardlayout[startingRow+2][startingCol]=='--'):
                        return True
                elif startingRow - endRow == -1:    
                    return True
     #taking a peice
        if (startingRow - endRow == -1):
           #only moving one space 
            if (abs(startingCol - endCol)==1):
                if (startingRow < endRow):
                    #checking if a peice is there
                    if(boardlayout[endRow][endCol] != '--' and 'B' not in boardlayout[endRow][endCol]):
                        return True
        
    #en passant 
        if (startingRow == 4 and endRow == 5 and abs(startingCol - endCol) == 1):
            if (boardlayout[4][endCol] == 'WP' and boardlayout[5][endCol] == '--'):
                boardlayout[4][endCol] = '--'
                return True
        return NotAMove('pawn')

def PawnPromotion(endRow, endCol,color):
    if color == 'W':
        if endRow == 0:
            promotion = input("What do you want to promote your pawn to? (Enter as shorthand)")
            while promotion not in ['WR', 'WN', 'WB', 'WQ']:
                promotion = input("Invalid choice. Please enter WR, WN, WB, or WQ: ")
            boardlayout[endRow][endCol] = promotion
    else:
        if endRow == 7:
            promotion = input("What do you want to promote your pawn to? (Enter as shorthand)")
            while promotion not in ['BR', 'BN', 'BB', 'BQ']:
                promotion = input("Invalid choice. Please enter BR, BN, BB, or BQ: ")
            boardlayout[endRow][endCol] = promotion

def NotAMove(name):
    return False

def end(inputs):
    if 'kill' in inputs:
        print("Program killed")
        return True

def Main():
    global TURN
    while True:
        #for formating the list into a board 
        for line in range(len(boardlayout)):
            print(boardlayout[line])    
        vaildNumber = list(range(0,9))
        #getting inputs 
        print("Where would White like to move" if TURN % 2 == 0 else "Where would Black like to move")
        SR = (input("what is the row your peice is on: "))
        if (end(SR)):
            break
        SC = (input("What is the col that your peice is on: "))
        if (end((SC))):
            break
        ER = (input("What is the row you want your peice to go: "))
        if (end((ER))):
            break
        EC = (input("What is the col you want your peice to go: "))
        if (end((EC))):
            break
        elif (int(SR) in vaildNumber and int(SC) in vaildNumber and int(ER) in vaildNumber and int(EC) in vaildNumber):
            if TURN % 2 == 0 and 'W' in boardlayout[int(SR)][int(SC)]:
                movePeice(int(SR),int(SC),int(ER),int(EC))
                TURN += 1
            elif TURN % 2 == 1 and 'B' in boardlayout[int(SR)][int(SC)]:
                movePeice(int(SR),int(SC),int(ER),int(EC))
                TURN += 1
            else: 
                print("That is not your peice")
        else:
            print("Put in a vaild number debug 1")
if __name__ == "__main__":
    peices()
    Main()