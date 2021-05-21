
#Will Frazier
#Adapted from Prof. Kfoury

from z3 import *

# all possible line segments
X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14 = Bools ("X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14") 


def yashi_solution(X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14):
    output = And ((Or (Not (X3), Not (X13))), \
        (Or (Not (X7), Not (X13))), \
        (Or (Not (X1), Not (X5), Not (X6), Not (X9), Not (X10), Not (X11))), \
        (Or (Not (X1), Not (X3), Not (X5), Not (X6), Not (X7), Not (X9), Not (X10), Not (X14))), \
        (Or (Not (X1), Not (X2), Not (X5), Not (X6), Not (X8), Not (X9), Not (X12), Not (X13))), \
        (Or (Not (X2), Not (X8), Not (X10), Not (X11), Not (X12), Not (X13))), \
        (Or (Not (X3), Not (X7), Not (X11), Not (X14))), \
        (Or (X1, X9)), \
        (Or (X1, X2, X10)), \
        (Or (X2, X13)), \
        (Or (X3, X10, X11)), \
        (Or (X3, X14)), \
         X4, \
        (Or (X4, X5, X9)), \
        (Or (X5, X6)), \
        (Or (X6, X7, X11, X12)), \
        (Or (X7, X14)), \
        (Or (X8, X12)), \
        (Or (X8, X13)), \
        (Or (X2, X9, X10)), \
        (Or (X1, X10, X13)), \
        (Or (X3, X7)), \
        (Or (X5, X9)), \
        (Or (X12, X13)), \
        (Or (X1, X5)), \
        (Or (X6, X9)), \
        (Or (X9, X10, X13)), \
        (Or (X1, X3, X11, X13)), \
        (Or (X1, X6)), \
        (Or (X3, X9, X11, X13)), \
        (Or (X5, X10, X13)), \
        (Or (X1, X7, X11, X13)), \
        (Or (X3, X6, X11, X13)), \
        (Or (X9, X11, X13, X14)), \
        (Or (X6, X10, X13)), \
        (Or (X7, X9, X11, X13)))
    return output

# this will return a possible solution to the problem
    # to hard code a line as drawn or not drawn, simply declare one of the variables
        # e.g., change X3 to False in the line below to leave it unconnected
solve(yashi_solution(X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14))

