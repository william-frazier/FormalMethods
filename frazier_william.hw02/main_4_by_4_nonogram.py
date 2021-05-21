

#Will Frazier
#Adapted from Prof. Kfoury


from z3 import * 

from four_x_four_nonogram_row_conditions import *
from four_x_four_nonogram_col_conditions import *

# The 4x4 board is represented by a 4x4 matrix X of Boolean values :
X = [ [ Bool("x_%s_%s" % (i+1, j+1)) for j in range(4) ] for i in range(4) ]



#### An instance of the 4x4 Nonogram game with the following conditions:
#### '1 1' (row 1), '1' (row 2), '1' (row 3), '1' (row 4)
#### '1 1' (col 1), '1' (col 2), '1' (col 3), '1' (col 4)
#s.add (OneOneInRow[0], OneInRow[1], OneInRow[2], OneInRow[3])
#s.add (OneOneInCol[0], OneInCol[1], OneInCol[2], OneInCol[3])

def run(rows, cols):
    s = Solver()
    possible = [[ZeroInRow, OneInRow, OneOneInRow, TwoInRow, OneTwoInRow, TwoOneInRow, ThreeInRow, FourInRow],
                [ZeroInCol, OneInCol, OneOneInCol, TwoInCol, OneTwoInCol, TwoOneInCol, ThreeInCol, FourInCol],]

    loop = 0
    # two loops, the 0th for row contraints, the 1st for column constraints
    while loop <= 1:
        if loop == 0:
            which = rows
        else:
            which = cols
        for i in range(len(which)):
            # select the correct restraint and add it to our solver
            if which[i] == [0]:
                s.add(possible[loop][0][i])
            elif which[i] == [1]:
                s.add(possible[loop][1][i])
            elif which[i] == [1,1]:
                s.add(possible[loop][2][i])
            elif which[i] == [2]:
                s.add(possible[loop][3][i])
            elif which[i] == [1, 2]:
                s.add(possible[loop][4][i])
            elif which[i] == [2,1]:
                s.add(possible[loop][5][i])
            elif which[i] == [3]:
                s.add(possible[loop][6][i])
            elif which[i] == [4]:
                s.add(possible[loop][7][i])
        loop += 1
    results = []
    # can the nonogram be solved?
    while s.check() == sat :
        # then create a model
        m = s.model()
        sorted_model = sorted([ (d, m[d]) for d in m], key= lambda x: str(x))
        # save that model to a list
        results.append (sorted_model)
        block = []
        for d in m :
            t = d()
            block.append ( t != m[d] )
        s.add (Or (block))
    # display all possible solutions
    for n in range (len (results)) :
        print()
        print("new solution:")
        count = 0
        for elt in results[n]:
            if elt[1] == True:
                print("*", end='')
            else:
                print(" ", end='')
            count += 1
            if count == 4:
                print()
                count = 0
    print("results total =", len(results))
    return results
