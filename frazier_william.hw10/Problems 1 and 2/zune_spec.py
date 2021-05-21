#### BEGIN zune_spec.py ################################################
#### Assaf Kfoury
#### 6 July 2019

# Run this script from the Python prompt in one of two ways (there are other):
#
#   >>> execfile ('zune_spec.py')   or   from zune_spec import *
#
# These two ways are not really equivalent, but neither will cause an error.

from z3 import *

s = SolverFor("LIA") # Quantified Linear Integer Arithmetic

x, y, z, a, b, diff = Ints('x y z a b diff')

# The numbers used in the formulation of 'specOfZune' below correspond to
# the following interpretations of the constants in the Zune program scheme:
#   c1 == 1980
#   c2 == 365
#   c3 == 366

# Try different values of the input x to test whether the specification
# correctly enforces the expected value of the output y; for example, try: 
# x = 1828 # x = 1461 # x = 366 # x = 367 #  x = 1462 # x = 2922 # ...

constraints = And( x >= 100, y >= 0 ) # 
         # And( x == 15922, y >= 0 )
         # And( x == 5922, y >= 0 )
         # And( x == 1828, y >= 0 )
         # And( x == 1462, y >= 0 )

# Use command 's.reset()' at the Python prompt >>> and try again the
# command "execfile ('zune_spec.py')" with a different constraint on 'x'.

specOfZune = Exists([a,b,diff],
                    And(a*1461 <= x,
                        ForAll(z, Implies(z*1461 <= x, z <= a)),
                        diff == x-a*1461,
                        Implies(0 == diff, b==-1),
                        Implies(And(1 <= diff, diff <= 366),b==0),
                        Implies(And(367 <= diff, diff <= 731),b==1),
                        Implies(And(732 <= diff, diff <= 1096),b==2),
                        Implies(1097 <= diff, b==3),
                        Implies(x == 0, y == 1980),
                        Implies(x > 0, y == 1980 + 4*a + b)
                        ))

s.add (constraints, specOfZune)
print (s.check())
print (s.model())

## COMMENT: An invocation of "execfile ('zune_spec.py')" produces
## a model with 4 entries, e.g., [y = 1985, diff!0 = 367, a!2 = 1, b!1 = 1]
## where the variables {y, diff!0, a!2, b!1} are interpreted appropriately
## in order to satisfy the constraints. Note that the model is limited to
## the free variable/constant y and the existentially quantified variables
## {diff!0, a!2, b!1}.

## Every new invocation of "execfile ('zune_spec.py')" produces a new
## indexing of the existentially quantified variables, e.g., on the next
## invocation we get [a!9 = 1, y = 1985, b!8 = 1, diff!7 = 367], and this
## indexing increases from one invocation to the next.

# for different ways of printing the model, consider one of the following:
"""
m = s.model()
print ('\n')
print ( [ (d, m[d]) for d in m ] )
print (sorted ([(d, m[d]) for d in m], key= lambda x: str(x)))
print (sorted ([(d, m[d]) for d in m], key= lambda x: str(x), reverse=True))
"""

#### END zune_spec.py ################################################
