
#Wiliam Frazier
#CS511
#HW06

from z3 import *
import json



def PB(encoding):
    """
    Function that combines all of our constraints to find an optimization.
    """
    
    s = z3.Optimize()
    # find the terms we use for our minimization
    fixed_encoding = make_constraint(encoding[0])
    minimize = fixed_encoding[0]
    X = fixed_encoding[1]
    #add our minimization
    s.minimize(minimize)
    #add our constraints
    for constraint in encoding[1:]:
        new_constraint_store = make_constraint(constraint)
        new_constraint = new_constraint_store[0]
        new_variables = new_constraint_store[1]
        s.add(new_constraint <= 0)
        #this is needed in case we have variables that 
        #don't show up in the initial minimization
        #(e.g., optimize x1+x2 over x3-x1<=0)
        for var in new_variables:
            if var not in X:
                X.append(var)
    #all terms are either 0 or 1
    for integer in X:
        s.add(integer <= 1, integer >= 0)
        #debugging code to ensure all constraints are correct
#    for c in s.assertions():
#        print( c)
    if s.check() == sat:
        return s.model()
    return False

def make_constraint(encoding):
    """
    A helper function which builds constraints.
    """
    
    #array to save every variable
    X = []
    minimize = 0
    #various loops to locate which term we are focusing on
    for term in encoding:
        for inner_term in term[1:]:
            #if we have a variable rather than a constant
            if inner_term != []:
                minim_term = 1
                for value in inner_term:
                    current = Int('x_%s' % value[1])
                    #if this is a new variable, add it to X
                    if current not in X:
                        X.append(current)
                    #if we have a 1 then we negate our variable
                    if value[0]:
                        minim_term *= (1-current)
                    #otherwise, keep it the same
                    else:
                        minim_term *= current
                #this is outside the loop to allow for things like 3*x_i*x_j
                #without it, we would only ever have addition
                minim_term *= term[0]
                minimize += minim_term
            # if we are adding a constant
            else:
                minimize += term[0] 
    #return both our constraint and the list of variables
    return [minimize, X]

def open_file(file):
    """
    Runs max_cut using an instance in a file.
    """
    
    f = open(file, 'r')
    if f.mode == 'r':
        contents = f.read()
    instance = json.loads(contents) 
    return PB(instance)