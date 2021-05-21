# BEGIN small_example_for_Z3Py.py
# 2019-09-04

# Two propositional wff's, wff1 and wff2, over 3 Boolean variables
# {x, y, z} and we want to check whether they are equivalent -- in this
# script, by using the function parse_smt2_string() of Z3Py.

### Look closely:
### wff1 is the DNF of the majority function,
### wff2 is the CNF of the majority function.              

from z3 import *

x, y, z = Bools ('x y z')

### For examples of how to use parse_smt2_string, see the webpage:
### See https://z3prover.github.io/api/html/namespacez3py.html
### which requires the use of a Python dictionary, here called ds:
#
ds = {'x':x, 'y':y, 'z':z}
#
### Note also that the logical operator {'or', 'and', 'not'} must be
### written in prefix position.

wff1 = parse_smt2_string ('(assert (or (or (and (and (not x) y) z) \
                                           (and (and x (not y)) z)) \
                                       (and (and x y) (not z)) ))',\
                          decls=ds)

wff2 = parse_smt2_string ('(assert (and (or x (or y z)) \
                                    (and (or x (or y (not z))) \
                                     (and (or x (or (not y) z)) \
                                      (and (or (not x) (or y z)) \
                                       (or (not x) (or (not y) (not z))))))))',\
                          decls=ds)

# To check whether wff1 and wff2 are equivalent, we show that
# (Not (wff1 == wff2)) is unsatisfiable :
constraint = (wff1[0] != wff2[0]) # alternatively: (Not (wff1[0] == wff2[0]))

s = Solver()
s.add (constraint)
print (s.check ())
#m = s.model()

# END small_example_for_Z3Py.py
