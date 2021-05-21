# BEGIN small_example_for_Z3Py.py
# 2019-09-04

# Two propositional wff's, wff1 and wff2, over 3 Boolean variables
# {x, y, z} and we want to check whether they are equivalent.

### Look closely:
### wff1 is the DNF of the majority function,
### wff2 is the CNF of the majority function.              

from z3 import *

x, y, z, a, b, c = Bools ('x y z a b c')

def wff1 (a,b,c) :
    output = ((not a) and b and c) or \
             (a and (not b) and c) or \
             (a and b and (not c))
    return output

def wff2 (a,b,c) :
    output = (a or b or c) and \
             (a or b or (not c)) and \
             (a or (not b) or c) and \
             ((not a) or b or c) and \
             ((not a) or (not b) or (not c))
    return output

# constraint1 = (wff1(x,y,z) == wff2(x,y,z))
constraint1 = Not (wff1(x,y,z) == wff2(x,y,z))

s = Solver()
s.add (constraint1)
print (s.check ())
#m = s.model()

# END small_example_for_Z3Py.py