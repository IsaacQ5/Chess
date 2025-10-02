ROWS= 8
COLS = 8
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def pawns(board):
    for pawn in range(len(board[1])):
        board[1][pawn] = 'p'
    for pawn in range(len(board[6])):
        board[6][pawn] = 'p'

def otherpeices(board):
    board[0][0] = 'r'
    board[0][1] = 'n'
    board[0][2] = 'b'
    board[0][3] = 'q'
    board[0][4] = 'k'
    board[0][5] = 'b'
    board[0][6] = 'n'
    board[0][7] = 'r'

    board[7][0] = 'r'
    board[7][1] = 'n'
    board[7][2] = 'b'
    board[7][3] = 'q'
    board[7][4] = 'k'
    board[7][5] = 'b'
    board[7][6] = 'n'
    board[7][7] = 'r'
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