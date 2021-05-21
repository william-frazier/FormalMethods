# BEGIN small_example_for_Z3Py.py
# 2019-09-04

# Two propositional wff's, wff1 and wff2, over 3 Boolean variables
# {x, y, z} and we want to check whether they are equivalent.

### Look closely:
### wff1 is the DNF of the majority function,
### wff2 is the CNF of the majority function.              

from z3 import *

x, y, z = Bools ('x y z')

def phi (a,b,c) :
    output = Or (And (Not (a), b, c), \
             (And (a, Not (b), c)), \
             (And (a, b, Not (c))),
             (And (a, b, c)))
    return output

def psi (a,b,c) :
    output = And( Or (a, b, c), \
             (Or (a, b, Not (c))), \
             (Or (a, Not (b), c)), \
             (Or (Not (a), b, c)))
    return output

constraint1 = (phi(x,y,z) == psi(x,y,z))
#constraint1 = Not (phi(x,y,z) == psi(x,y,z))

s = Solver()
#solve(phi(True,False,False))
s.add (constraint1)
print (s.check ())
try:
    m = s.model()
    print(m)
except:
    print("no model")

# END small_example_for_Z3Py.py