#give a code for each player to mean thier peices (two player)
#make a single player mode

ROWS= 8
COLS = 8
board = [['--' for _ in range(COLS)] for _ in range(ROWS)]

def pawns(board):
    for pawn in range(len(board[1])):
        board[1][pawn] = 'BP'
    for pawn in range(len(board[6])):
        board[6][pawn] = 'WP'

def otherpeices(board):
    board[0][0] = 'BR'
    board[0][1] = 'BN'
    board[0][2] = 'BB'
    board[0][3] = 'BQ'
    board[0][4] = 'BK'
    board[0][5] = 'BB'
    board[0][6] = 'BN'
    board[0][7] = 'BR'

    board[7][0] = 'WR'
    board[7][1] = 'WN'
    board[7][2] = 'WB'
    board[7][3] = 'WQ'
    board[7][4] = 'WK'
    board[7][5] = 'WB'
    board[7][6] = 'WN'
    board[7][7] = 'WR'

def peices():
    otherpeices(board)
    pawns(board)

def displayboard(board):
    peices()
    for line in range(len(board)):
        print(board[line])

def Main():
    displayboard(board)

Main()