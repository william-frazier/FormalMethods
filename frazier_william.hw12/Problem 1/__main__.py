

# William Frazier
# HW12
# CS511


from z3 import *

def multiply():
    s = Solver()
    x, y, h_1 = BitVecs('x y h_1', 16)
    varphi_obvious = (x * 4 == y)
    varphi_smart = (x << h_1 == y)
    Phi_1 = ForAll([x,y], varphi_obvious == varphi_smart)
    s.add(Phi_1)
    s.check()
    return s.model()

def test():
    s = Solver()
    x, h_2 = BitVecs('x h_2', 32)
    y = Bool('y')
    varphi_obvious = (x % 4 == 0) == y
    varphi_smart = ((x & h_2) == 0) == y
    Phi_2 = ForAll([x,y], varphi_obvious == varphi_smart)
    s.add(Phi_2)
    s.check()
    return s.model()