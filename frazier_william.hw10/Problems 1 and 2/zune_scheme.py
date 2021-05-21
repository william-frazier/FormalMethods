#### BEGIN zune_scheme.py
#### Assaf Kfoury
#### 6 July 2019

# To run this script, issue the command:
#       execfile ('zune_scheme.py')
# at the Python prompt, after which you can try to execute the
# function 'buggy' on different inputs (try integers < 100 to start).

# However, this is only the SCHEME of the actual Zune Buggy Function; that is,
# all the constant symbols, function symbols, and relation symbols, are left
# uninterpreted. Without an interpretation of these symbols, we are only able
# to compile the program scheme, not not to execute it on inputs. The original
# Zune Buggy Function is in the Python script called 'zune.py'.

# To recover the orginal Zune Buggy Function, we interpret the symbols
# in its signature { c1,c2,c3, f(), g( , ), r( , ), p( ) } as follows.

# constant symbols -- buggy (6), buggy (27), buggy (48), ... diverge
c1 = 1 # instead of 1980 in the original
c2 = 5 # instead of 365 in the original
c3 = 6 # instead of 366 in the original

# function symbols:
def f (x) : return (x+1)
def g (x,y) : return (x-y)

# relation symbols:
def r (x,y) : return (x > y)
def p (x) : return ((x - c1) % 4) == 0 

# the scheme of the Zune Buggy Function follows next:
def buggy (x1) :
    x2 = c1 
    while r (x1, c2) :
        if p (x2) :
            if r (x1, c3) :
                x1 = g(x1, c3)
                x2 = f(x2)
        else :
            x1 = g(x1,c2)
            x2 = f(x2)
    return x2

#### END zune_scheme.py
