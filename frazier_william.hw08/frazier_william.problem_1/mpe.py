

# William Frazier
# HW 8
# CS511
# Problem 1

from z3 import *
from math import *


def MPE(cpts, obs):
    """
    Main function which creates our variables, notes our observations, and
    makes calls to the helper function in order to add all of the soft
    clauses. Returns the model.
    """
    s = z3.Optimize()
    # we store our variables in a dictionary because it makes retrieval easier
    var = {}
    for variable in cpts:
         var[variable[0]] = (Bool(variable[0]))
    # we use this loop to make our hard assertions
    for observations in obs:
        if observations != []:
            if observations[1] == '0':
                s.add(Not(var[observations[0]]))
            else:
                s.add(var[observations[0]])
    # call our helper function to add all of our soft assertions
    for cpt in cpts:
        weighted_clause(cpt, var, s)
    s.check()
    return s.model()

    
    


                        
def weighted_clause(cpt, lookup, s):
    """
    Helper function which creates all of the soft constraints.
    """
    
    # the variable we are working with 
    var = lookup[cpt[0]]  


    # cpt[1] is everything after the variable
    for i in range(len(cpt[1])):
        # are there any preconditions
        prereqs = cpt[1][i][0]
        # if not then it has no parents so we simply add it
        if prereqs[0] == []:
            if cpt[1][i][1][1] == '1':
                s.add_soft(Not(var), -log(cpt[1][i][-1],2))
            else:
                s.add_soft(var, -log(cpt[1][i][-1],2))
        else:
            # create a blank slate to be our clause
            others = []
            # cpt[1][i][0] is our list of preconditions
            # so other is a precondition
            for other in cpt[1][i][0]:
                # if true
                if other[1] == '1':
                    others.append(Not(lookup[other[0]]))
                # if false
                else:
                    others.append(lookup[other[0]])
            # append the variable we're working with
            if cpt[1][i][1][1] == '0':
                others.append(var)
            else:
                others.append(Not(var))
            # OR all of this together
            others = Or(others)
            # add it as a soft clause with the proper weight
            s.add_soft(others, -log(cpt[1][i][-1],2))
   
