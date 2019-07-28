import numpy as np
ROW_COUNT = 6 #No of rows in the board
COLUMN_COUNT = 7 #No of columns in the board
GAME_OVER = False #To check wether the game is over or not
TURN = 0 #To decide whose turn it is
def create_board():
    '''
    function to create the board for the connect4 game

    returns a numpy array of zeros with shape (ROW_COUNT,COLUMN_COUNT)
    '''
    return np.zeros((ROW_COUNT,COLUMN_COUNT))
def is_valid_loc(board,loc):
    '''
    checks for validity of the move being made.
    Basically checks if all the rows of the column
    are filled or not

    arguments:
        board: numpy array that represents the board.
        col: Column number given by the user to add the piece.(int)

    returns True if the column is not full
    '''
    return board[ROW_COUNT-1][col] == 0
def get_next_open_row(board,col):
    '''
    It returns the row number of the column which is empty.
    This is done basically to stack the pieces.

    arguments:
        board: numpy array that represents the board.
        col: Column number given by the user to add the piece.(int)
        
    returns the row number
    '''
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r
def drop_piece(board,row,col,piece):
    '''
    changes the board number from 0 to 1/2 according to row and column number.
    arguments:
        board: numpy array that represents the board.
        row: row number where the piece will be inserted.(int)
        col: Column number given by the user to add the piece.(int)
        piece: One of the player's piece.(int)
    '''
    board[row][col] = piece
def winning_strike(board,piece):
    '''
    This is the function which checks if the move 
    made by the player is winning or not by checking
    various cases like horizontal,vertical,diagonal etc

    arguments:
        board: numpy array that represents the board.
        piece: One of the player's piece.(int)
    '''
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
board = create_board()
def print_board(board):
    print(np.flip(board,0))

while not GAME_OVER:
    '''
    The main game loop.
    The players get a chance to put the piece turn by turn and the winning move is check on every turn
    '''
    # for player 1
    if(TURN==0):
        #getting column number
        col = int(input("Enter your choice between (0-6):"))
        if is_valid_loc(board,col):#checks for the validity of the move
            row = get_next_open_row(board,col)#gets the open row for the column specified
            drop_piece(board,row,col,1)#drops the piece for the player
            if winning_strike(board,1):#checks if the move is winning move or not
                print("PLAYER 1 WINS")
                GAME_OVER=True
        
    # for player 2
    else:
        #getting column number
        col = int(input("Enter your choice between (0-6):"))
        if is_valid_loc(board,col):#checks for the validity of the move
            row = get_next_open_row(board,col)#gets the open row for the column specified
            drop_piece(board,row,col,2)#drops the piece for the player
            if winning_strike(board,2):#checks if the move is winning move or not
                print("PLAYER 2 WINS")
                GAME_OVER=True
    TURN +=1
    TURN = TURN%2
    print_board(board)