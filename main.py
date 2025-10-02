ROWS= 8
COLS = 8
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def pawns(board):
    for pawn in range(len(board[1])):
        board[1][pawn] = 'p'
    for pawn in range(len(board[6])):
        board[6][pawn] = 'p'

def peices():
    pawns(board)

def displayboard(board):
    peices()
    for line in range(len(board)):
        print(board[line])

def Main():
    displayboard(board)

Main()