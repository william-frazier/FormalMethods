

# William Frazier
# HW12
# CS511

from z3 import *
import math


s = SolverFor("LIA") # Quantified Linear Integer Arithmetic
x, const = BitVecs('x const', 8)
y = Bool('y')
k = Function('k', BitVecSort(8), BitVecSort(8))




phi_zero = Implies(x <= 0, y == False)
phi_one = Implies(x == 1, y == True)
phi_two = Implies(x == 2, y == True)
phi_odd = Implies(And(x > 2, x % 2 != 0), y == False)  
phi_four = Implies(And(x > 2, x % 2 == 0, x>>2 == 1, (x >> 1) % 2 == 0), y == True)
phi_six = Implies(And(x > 2, x>>1 != 1, (x>>1)%2!=0), y == False)
phi_double = Implies(And(x > 2, x>>2 != 1,x>>1 != 1, (x>>1)%2!=0), y == False)
phi_eight = Implies(And(x > 2, x % 2 == 0, x>>3 == 1, (x >> 2) % 2 == 0, (x >> 1) % 2 == 0), y == True)
phi_twelve =  Implies(And(x > 2, x>>2 != 1, (x>>2)%2!=0, x>>1 != 1, (x>>1)%2!=0), y == False)

phi_smart = (y == And(x != 0, (x & k(x)) == 0))
phi_obv = And(phi_zero, phi_one, phi_two, phi_odd, phi_four, phi_six, phi_eight, phi_twelve)





## Either use this
s.add(Or(ForAll(x, k(x) == x + const), (ForAll(x, k(x) == x - const))))
s.add(const <= 0)
##s.add(const >= 0)

# Or this
#phi_k = ForAll(x,Or(k(x) == x + 1, k(x) == x + 2, k(x) == x + 3, k(x) == x - 1, k(x) == x - 2, k(x) == x - 3))
#s.add(phi_k)




s.add(ForAll([x,y],Or(Implies(phi_obv, phi_smart), x>=128)))
s.check()
print(s.model())
