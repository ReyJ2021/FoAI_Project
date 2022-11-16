"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0
    for i in board:
        count_X = count_X + count_X.count(X)
        count_O = count_O + count_O.count(X)


    if count_X >= count_O:
        return O
    else:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # attempt at using list comprehension in python 
    moves = [[row,col] for col in range(3) if board[row][col] == EMPTY  for row in range(3)] 
    return moves

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # creating independent copy of board
    board_copy = copy.deepcopy(board) 

    try: 
        if board_copy[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            board_copy[action[0]][action[1]] = player(board_copy)
            return board_copy

    except IndexError:("Spot taken")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    count_X = 0
    count_O = 0
    cols = []

    for row in board:
        count_X = row.count(X)
        count_O = row.count(O)
        if count_X == 3:
            return X
        if count_O == 3:
            return O

    #using zip to Transpose board rows to columns
    for i in zip(*board):
        cols.append(list(i))


    # cols = [list(i) for i in zip(*board)]
    #iterating through the col to check max count of 3  
    for col in cols:
        count_X = col.count(X)
        count_O = col.count(O)
        if count_X == 3:
            return X
        if count_O == 3:
            return O 

    #checking diagonally
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[2][0] == X and board[1][1] == X and board[0][2] == X:
        return X

    else:
        return None
   


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or O:
        return True  # game over if wither X or O has won
    for row in range(3): #game not over if any single cell in game empty
        for col in range(3):
            if board[row][col] == EMPTY:
                return False

    else: # tie = game over.
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    current_player = player(board)

    if terminal(board) is True:
        return None

    if current_player == X: #X is max player
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))
            if k > v:
                v = k
                best_move = action
    else:
        v = math.inf
        for action in actions(board):
            k = max_value(result(board, action))
            if k < v:
                v = k
                best_move = action
    return best_move

  

def max_value(board):

    v = float('-inf')         
    if terminal(board):
        return board

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v  

def min_value(board):
    v = float('inf')         
    if terminal(board):
        return board

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v 
