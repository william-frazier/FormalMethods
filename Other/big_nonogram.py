########### BEGIN yurichev.nonograms.py ######################
##
## This script is largely due to Dennis Yurichev.
##

from z3 import *

########### Below are several instances of Nonogram, all from the Web :

# https://ocaml.org/learn/tutorials/99problems.html
#rows =[[3] ,[2 ,1] ,[3 ,2] ,[2 ,2] ,[6] ,[1 ,5] ,[6] ,[1] ,[2]]
#cols =[[1 ,2] ,[3 ,1] ,[1 ,5] ,[7 ,1] ,[5] ,[3] ,[4] ,[3]]

# https://ocaml.org/learn/tutorials/99problems.html
#rows= [[14] , [1,1], [7,1], [3,3], [2,3,2], [2,3,2], [1,3,6,1,1], [1,8,2,1], [1,4,6,1], [1,3,2,5,1,1], [1,5,1], [2,2], [2,1,1,1,2], [6,5,3], [12]]
#cols= [[7], [2,2], [2,2], [2,1,1,1,1], [1,2,4,2], [1,1,4,2], [1,1,2,3], [1,1,3,2],[1,1,1,2,2,1], [1,1,5,1,2], [1,1,7,2], [1,6,3], [1,1,3,2], [1,4,3], [1,3,1], [1,2,2], [2,1,1,1,1], [2,2], [2,2], [7]]

# https://en.wikipedia.org/wiki/File:Nonogram_wiki.svg
rows =[[8,7,5,7], [5,4,3,3], [3,3,2,3], [4,3,2,2], [3,3,2,2], [3,4,2,2], [4,5,2], [3,5,1], [4,3,2], [3,4,2], [4,4,2], [3,6,2], [3,2,3,1], [4,3,4,2], [3,2,3,2], [6,5], [4,5], [3,3], [3,3], [1,1]]
cols =[[1], [1], [2], [4], [7], [9], [2,8], [1,8], [8], [1,9], [2,7], [3,4], [6,4], [8,5], [1,11], [1,7], [8], [1,4,8], [6,8], [4,7], [2,4], [1,4], [5], [1,4], [1,5], [7], [5], [3], [1], [1]]

############ See also for other instances of Nonogram:

# http://puzzlygame.com/nonogram /11/

# http://puzzlygame.com/nonogram /24/

# http://puzzlygame.com/nonogram /792/

# http://puzzlygame.com/nonogram /561/

WIDTH =len(cols)
HEIGHT =len(rows)
s= Solver ()

# part I, for all rows:
row_islands = [[ BitVec ('row_islands_ %d_%d' % (j, i), WIDTH ) \
                 for i in range (len(rows[j]))] for j in range ( HEIGHT ) ]
row_island_shift = [[ BitVec ('row_island_shift_ %d_%d' % (j, i), WIDTH ) \
                      for i in range (len(rows[j]))] for j in range ( HEIGHT )]
# this is a bitvector representing final image , for all rows:
row_merged_islands = [ BitVec ('row_merged_islands_ %d' % j, WIDTH ) \
                       for j in range ( HEIGHT )]

for j in range (HEIGHT):
    q=rows[j]
    for i in range (len(q)):
        s.add( row_island_shift [j][i] >= 0)
        s.add( row_island_shift [j][i] <= WIDTH - q[i])
        s.add( row_islands [j][i ]==(2** q[i]-1) << row_island_shift [j][i])
    # must be an empty cell(s) between islands :
    for i in range (len(q) - 1):
        s.add( row_island_shift [j][i+1] > row_island_shift [j][i]+q[i])
    s.add( row_island_shift [j][ len(q) -1] < WIDTH )
    # OR all islands into one:
    expr= row_islands [j][0]
    for i in range (len(q) -1):
        expr=expr | row_islands [j][i+1]
    s.add( row_merged_islands [j]== expr)

# similar part , for all columns :
col_islands = [[ BitVec ('col_islands_ %d_%d' % (j, i), HEIGHT) \
                 for i in range (len(cols[j]))] for j in range ( WIDTH) ]
col_island_shift = [[ BitVec ('col_island_shift_ %d_%d' % (j, i), HEIGHT) \
                      for i in range (len(cols[j]))] for j in range (WIDTH) ]
# this is a bitvector representing final image , for all columns :
col_merged_islands = [ BitVec ('col_merged_islands_ %d' % j, HEIGHT) \
                       for j in range (WIDTH) ]

for j in range ( WIDTH ):
    q=cols[j]
    for i in range (len(q)):
        s.add( col_island_shift [j][i] >= 0)
        s.add( col_island_shift [j][i] <= HEIGHT - q[i])
        s.add( col_islands [j][i ]==(2** q[i]-1) << col_island_shift [j][i])
    # must be an empty cell(s) between islands :
    for i in range (len(q) - 1):
        s.add( col_island_shift [j][i+1] > col_island_shift [j][i]+q[i])
    s.add( col_island_shift [j][ len(q) -1]< HEIGHT )
    # OR all islands into one:
    expr= col_islands [j][0]
    for i in range (len(q) -1):
        expr=expr | col_islands [j][i+1]
    s.add( col_merged_islands [j]== expr)

# make " merged " vectors equal to each other :
for r in range ( HEIGHT ):
    for c in range ( WIDTH ):
        # lowest bits must be equal to each other :
        s.add( Extract (0,0, row_merged_islands [r]>>c) == \
               Extract (0,0, col_merged_islands [c]>>r))

def print_model(m):
    for r in range (HEIGHT):
        rt=""
        for c in range (WIDTH):
            if (m[row_merged_islands [r]]. as_long () >>c) & 1==1:
                rt=rt+"*"
            else:
                rt=rt+" "
        print (rt)

"""
print s.check ()
m= s.model ()
print_model (m)
exit (0)
"""

# ... or ...

# enumerate all solutions (it is usually a single one):
results =[]
while s.check () == sat:
    m = s.model ()
    print_model (m)
    results.append (m)
    block = []
    for d in m :
        t=d()
        block.append (t != m[d])
        s.add(Or(block))
        
print (" results total =", len(results))

########### END yurichev.nonograms.py ########################