

# William Frazier
# HW12
# CS511
# Code adapted from Professor Kfoury


from z3 import *

"""
# Sam Aleck's code with three holes {h1, h2, h3}, which you will not be
# able to execute unless you replace the holes by non-negative integers:
"""

def sam_aleck_mod_15 (x) :
    v1 = (x  >> 14) + (x  & 0xFFFF)
    v2 = (v1 >> 8) + (v1 & 0xFF)
    v3 = (v2 >> 4) + (v2 & 0xF)
    if v3 < 15 : y = v3
    if v3 >= 15 and v3 < 30 : y = v3 -15
    if v3 >= 30 : y = v3 - 30
    return y

x, y          = BitVecs('x y', 16)
w1, w2, w3, z = BitVecs('w1 w2 w3 z', 16)  
h1, h2, h3    = BitVecs('h1 h2 h3', 16)

constraint1 = (w1 == (x >> h1) + (x & 0xFFFF))
constraint2 = (w2 == (w1 >> h2) + (w1 & 0xFF))
constraint3 = (w3 == (w2 >> h3) + (w2 & 0xF))

phi = Exists([w1,w2,w3], And \
                   (constraint1, constraint2, constraint3, \
                    Implies(w3 < 15, y == w3), \
                    Implies(And (w3 >= 15, w3 < 30), y == w3-15), \
                    Implies(w3 >= 30, y == w3-30)))


# Increasingly larger sets of test cases:
theta = Or ( And (x == 20, y == 5),\
             And (x == 30, y == 0),\
             And (x == 40, y == 10))
theta_1 = Or ( theta,\
               And (x == 41, y == 11),\
               And (x == 42, y == 12),\
               And (x == 43, y == 13))
theta_2 = Or ( theta_1,\
               And (x == 66, y == 6),\
               And (x == 67, y == 7),\
               And (x == 68, y == 8))
theta_3 = Or ( theta_2,\
               And (x == 91, y == 1),\
               And (x == 92, y == 2),\
               And (x == 93, y == 3))
theta_4 = Or ( theta_3,\
               And (x == 94, y == 4),\
               And (x == 99, y == 9),\
               And (x == 104, y == 14))

theta_5 = Or ( theta_4,\
               And (x == 1500, y == 0))

theta_6 = Or(theta_5, \
             ForAll([x,y], Implies(And(x<32000, x>0), x%15==y)))

Theta = ForAll([x,y], Implies(theta_6, phi))

s = SolverFor("LIA")
s.add(Theta)
print( s.check())
m = s.model()
print (m)


