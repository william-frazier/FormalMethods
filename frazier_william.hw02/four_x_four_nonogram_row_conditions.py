######### BEGIN four_x_four_nonogram_row_conditions.py #############
######### Assaf Kfoury
######### 6 September 2019

from z3 import * 

# The 4x4 board is represented by a 4x4 matrix X of Boolean values :
X = [ [ Bool("x_%s_%s" % (i+1, j+1)) for j in range(4) ] for i in range(4) ]

# In the 4x4 nonogram game the conditions on the 4 rows and 4 columns are
# eight: { '0', '1', '1 1', '2', '1 2', '2 1', '3', '4' }.

ZeroInRow =   [ Bool("zero_in_row_%s" % (i+1)) for i in range(4) ]
OneInRow  =   [ Bool("one_in_row_%s" % (i+1)) for i in range(4) ]
OneOneInRow = [ Bool("one_one_in_row_%s" % (i+1)) for i in range(4) ]
TwoInRow  =   [ Bool("two_in_row_%s" % (i+1)) for i in range(4) ]
OneTwoInRow = [ Bool("one_two_in_row_%s" % (i+1)) for i in range(4) ]
TwoOneInRow = [ Bool("two_one_in_row_%s" % (i+1)) for i in range(4) ]
ThreeInRow  = [ Bool("three_in_row_%s" % (i+1)) for i in range(4) ]
FourInRow  =  [ Bool("four_in_row_%s" % (i+1)) for i in range(4) ]

for i in range(4) :
    ZeroInRow[i] = And(Not(X[i][0]),Not(X[i][1]),Not(X[i][2]),Not(X[i][3]))
for i in range(4) :
    OneInRow[i] = Or ([And(X[i][0],Not(X[i][1]),Not(X[i][2]),Not(X[i][3])),
                       And(Not(X[i][0]),X[i][1],Not(X[i][2]),Not(X[i][3])),
                       And(Not(X[i][0]),Not(X[i][1]),X[i][2],Not(X[i][3])),
                       And(Not(X[i][0]),Not(X[i][1]),Not(X[i][2]),X[i][3])])
for i in range(4) :
    OneOneInRow[i] = Or ([And(X[i][0],Not(X[i][1]),X[i][2],Not(X[i][3])),
                          And(X[i][0],Not(X[i][1]),Not(X[i][2]),X[i][3]),
                          And(Not(X[i][0]),X[i][1],Not(X[i][2]),X[i][3])])
for i in range(4) :
    TwoInRow[i] = Or([And(X[i][0],X[i][1],Not(X[i][2]),Not(X[i][3])),
                      And(Not(X[i][0]),X[i][1],X[i][2],Not(X[i][3])),
                      And(Not(X[i][0]),Not(X[i][1]),X[i][2],X[i][3]) ])
for i in range(4) :
    OneTwoInRow[i] = And(X[i][0],Not(X[i][1]),X[i][2],X[i][3])
for i in range(4) :
    TwoOneInRow[i] = And(X[i][0],X[i][1],Not(X[i][2]),X[i][3])
for i in range(4) :
    ThreeInRow[i] = Or ([And(X[i][0],X[i][1],X[i][2],Not(X[i][3])),
                         And(Not(X[i][0]),X[i][1],X[i][2],X[i][3])])
for i in range(4) :
    FourInRow[i] = And(X[i][0],X[i][1],X[i][2],X[i][3])

######### END four_x_four_nonogram_row_conditions.py #############