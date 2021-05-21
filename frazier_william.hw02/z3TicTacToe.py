

#Will Frazier

from z3 import *
import copy


### various boards used for testing
#board=[["x","x","x","x"],["o","o","x","x"],["o","o","x","o"],["x","o","o","o"]]
#board=[["x","x","x","x"],["o","o","x","x"],["o","o","o","o"],["x","x","o","o"]]
#board=[["x","x","o","o"],["o","x","o","x"],["o","o","x","x"],["o","x","o","x"]]
#board=[["o","x","o","x","o"],["o","x","x","x","o"],["x","x","o","o","x"],["o","x","o","o","x"],["o","x","o","o","x"]]




#p_0_1 is in the 0th row and 1st column
# i = row
# j = column



def convert_board(board):
    p = copy.deepcopy(board)
    q = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "x":
                p[i][j] = True
                q[i][j] = False
            elif board[i][j] == "o":
                p[i][j] = False
                q[i][j] = True
    return p, q



def win_row(P, k):
    """
    Given a converted board, did the player win by filling a row?
    """
    output = Or ([(And([(P[i][j]) for j in range(k)])) for i in range(k)])
    return output

def win_column(P, k):
    """
    Given a converted board, did the player win by filling a column?
    """
    output = Or ([(And([(P[i][j]) for i in range(k)])) for j in range(k)])
    return output

def win_first_diag(P, k):
    """
    Given a converted board, did the player win by filling the first diagonal?
    """
    output = (And ([P[i][i] for i in range(k)]))
    return output

def win_second_diag(P, k):
    """
    Given a converted board, did the player win by filling the second diagonal?
    """
    output = (And ([P[i][k-i-1] for i in range(k)]))
    return output

def win(P, k):
    """
    Given a converted board, did the player win by using any of the above?
    """
    output = (Or (win_row(P, k), win_column(P, k), win_first_diag(P, k), win_second_diag(P, k)))
    return output

def P_but_not_Q(P, Q, k):
    """
    Given 2 converted boards representing the final state of the game, is it
    the case that player P won **and** that player Q lost?
    """
    output = And (win(P, k), Not(win(Q, k)))
    return output

def run(board):
    k=len(board)
    # P represents player X
    P = [[Bool("p_%s_%s" % (i, j)) for j in range(k)] for i in range(k)]
    # Q represents player O
    Q = [[Bool("q_%s_%s" % (i, j)) for j in range(k)] for i in range(k)]
    # change the board into a more readable format
    converted_board = convert_board(board)
    s = Solver()
    # add our constraints
    s.add(P_but_not_Q(converted_board[0], converted_board[1], k))
    if s.check() == sat:
        return("Player X won and player O lost!")
    else:
        return("It was either a tie or player X lost.")