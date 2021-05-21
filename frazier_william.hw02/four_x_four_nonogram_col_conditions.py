######### BEGIN four_x_four_nonogram_col_conditions.py #############
######### Assaf Kfoury
######### 6 September 2019

from z3 import * 

# The 4x4 board is represented by a 4x4 matrix X of Boolean values :
X = [ [ Bool("x_%s_%s" % (i+1, j+1)) for j in range(4) ] for i in range(4) ]

# In the 4x4 nonogram game the conditions on the 4 rows and 4 columns are
# eight: { '0', '1', '1 1', '2', '1 2', '2 1', '3', '4' }.

ZeroInCol =   [ Bool("zero_in_row_%s" % (i+1)) for i in range(4) ]
OneInCol  =   [ Bool("one_in_row_%s" % (i+1)) for i in range(4) ]
OneOneInCol = [ Bool("one_one_in_row_%s" % (i+1)) for i in range(4) ]
TwoInCol  =   [ Bool("two_in_row_%s" % (i+1)) for i in range(4) ]
OneTwoInCol = [ Bool("one_two_in_row_%s" % (i+1)) for i in range(4) ]
TwoOneInCol = [ Bool("two_one_in_row_%s" % (i+1)) for i in range(4) ]
ThreeInCol  = [ Bool("three_in_row_%s" % (i+1)) for i in range(4) ]
FourInCol  =  [ Bool("four_in_row_%s" % (i+1)) for i in range(4) ]

for i in range(4) :
    ZeroInCol[i] = And(Not(X[0][i]),Not(X[1][i]),Not(X[2][i]),Not(X[3][i]))
for i in range(4) :
    OneInCol[i] = Or ([And(X[0][i],Not(X[1][i]),Not(X[2][i]),Not(X[3][i])),
                       And(Not(X[0][i]),X[1][i],Not(X[2][i]),Not(X[3][i])),
                       And(Not(X[0][i]),Not(X[1][i]),X[2][i],Not(X[3][i])),
                       And(Not(X[0][i]),Not(X[1][i]),Not(X[2][i]),X[3][i])])
for i in range(4) :
    OneOneInCol[i] = Or ([And(X[0][i],Not(X[1][i]),X[2][i],Not(X[3][i])),
                          And(X[0][i],Not(X[1][i]),Not(X[2][i]),X[3][i]),
                          And(Not(X[0][i]),X[1][i],Not(X[2][i]),X[3][i])])
for i in range(4) :
    TwoInCol[i] = Or([And(X[0][i],X[1][i],Not(X[2][i]),Not(X[3][i])),
                      And(Not(X[0][i]),X[1][i],X[2][i],Not(X[3][i])),
                      And(Not(X[0][i]),Not(X[1][i]),X[2][i],X[3][i]) ])
for i in range(4) :
    OneTwoInCol[i] = And(X[0][i],Not(X[1][i]),X[2][i],X[3][i])
for i in range(4) :
    TwoOneInCol[i] = And(X[0][i],X[1][i],Not(X[2][i]),X[3][i])
for i in range(4) :
    ThreeInCol[i] = Or ([And(X[0][i],X[1][i],X[2][i],Not(X[3][i])),
                         And(Not(X[0][i]),X[1][i],X[2][i],X[3][i])])
for i in range(4) :
    FourInCol[i] = And(X[0][i],X[1][i],X[2][i],X[3][i])

######### END four_x_four_nonogram_col_conditions.py #############