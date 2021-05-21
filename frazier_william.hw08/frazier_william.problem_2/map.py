
# William Frazier
# HW 8
# CS511
# Problem 2

from z3 import *
from math import *
import itertools



#### Heads up, this code looks awful. It's really poorly designed
#### I had some things come up and couldn't devote the time I wanted to
#### this problem and for some reason the logic just didn't click for
#### me. I think it works, just a warning that it's some serious
#### spaghetti code at times.

def probability(cpts, term, obs):
    """
    Give a CPT, a term to look for, and a list of observations, this program
    returns the odds that the term is true or false (depending on the input).
    """
    
    
    # term is a list e.g., ['x_1', '0']
    # flip refers to the assignment either '0' false or '1' true
    flip = term[1]
    # the term itself
    term = term[0]
    # accumulator variable
    answer = 0
    # this loop locates where in the CPT we're looking
    for clause in range(len(cpts)):
        if cpts[clause][0] == term:
            index = clause
    # focus on our term
    cpt = cpts[index]
    # this loop checks if there are no preconditions
    # if not, then we immediately know the probability and can return
    for m in range(len(cpt[1])):
        if cpt[1][m][-2][1] == '1':
            if cpt[1][m][0] == [[]]:
                answer = cpt[1][m][-1]
    # list of the variables we have observed
    have = []
    if obs != []:
        for k in obs:
            have.append(k[0])
    # list of variables we need to know in order to calculate the probability
    needed = []
    for prob in range(len(cpt[1])):
        for j in cpt[1][prob][0]:
            if j != []:
                if j[0] not in needed:
                    needed.append(j[0])
        # conditional logic based on the known variables
        for required in needed:
            if required not in have:
                # deep copy our observations list
                obs2 = []
                obs3 = []
                for observs in obs:
                    obs2.append(observs)
                    obs3.append(observs)
                # if we need to know a variable but don't have it
                # then we allow it to be either 0 or 1
                obs3.append([required,'1'])
                obs2.append([required,'0'])
                # computes probability if the unknown term is true, times 
                # the probability that the unknown term is true, plus the
                # probability if the unknown term is false, times the 
                # probability that the unknown term is false
                answer = (probability(cpts, [term,flip], obs3) * probability(cpts, [required,'1'], obs)) + (probability(cpts, [term,flip], obs2) * (probability(cpts, [required,'0'], obs)))
        # this loop looks complicated but all it's doing is finding the correct
        # line in the CPT
        if cpt[1][prob][-2][1] == '1':
            count = 1
            for i in range(len(cpt[1][prob][0])):
                if cpt[1][prob][0][i] in obs:
                    count *= 1
                else:
                    count = 0
            if count == 1:
                answer += cpt[1][prob][-1]


    # this computes the probability that the term is true, so if we asked 
    # for the probability that it is false, just return 1 - answer
    if flip == '0':
        return 1 - answer
    return answer
    



def MAP(cpts, obs, terms):
    """
    Main function which takes a CPT, a list of observations, and a list of
    terms. Returns truth assignment for those variables such that they have the 
    greatest chance of occuring given the observations.
    """

    # a list to store the computed probabilities
    all_sums = []
    # initialize all terms to false
    for value in range(len(terms)):
        terms[value] = [terms[value], '0']
    search_array = terms + obs
    # if all terms are being watched, just call MPE
    if len(search_array) == len(cpts):
        return MPE(cpts, obs)
    # we need to know what terms we aren't interested in so we start with 
    # or terms and observations and note the variables that appear in CPT but
    # not in those
    dont_count = []
    for var in cpts:
        if [var[0], '0'] not in search_array and [var[0], '1'] not in search_array:
            dont_count.append(var[0])
            terms.append([var[0],'1'])
    # sort the terms to ensure correct ordering
    terms.sort()
    # creates a list of all possible bit strings
    # just an easy way to create all possible truth assignments
    seq = ["".join(seq) for seq in itertools.product("01", repeat=len(terms))]
    # loop through all possible truth assignments
    for j in range(len(seq)):
        # we initialize at probability = 100%
        chance = 1
        # assign the truth values
        for k in range(len(seq[j])):
            terms[k][1] = seq[j][k]
        # this computes the probability using the chaining rule
        for i in range(len(terms)):
            new_terms = terms[:-i-1] + obs
            new_terms.sort()
            chance *= probability(cpts,terms[-i-1], new_terms)
        # add the probabilities to our list
        all_sums.append(chance)
    combine = []
    # note all variables which weren't in obs or Vs
    for i in dont_count:
        combine.append(terms.index([i,'1']))
    # this will store the final probabilities
    final_array = [0] * len(seq)
    # another complicated looking loop, it just serves to combine probabilities
    # for example, if we have a CPT with x_1, x_2, x_3, x_4 and we observe 
    # x_1 to be true and have Vs = [x_3, x_4] then we need to combine the 
    # probabilities that are the same except for x_2 = true vs false
    for loc in combine:
        for sequence in range(len(seq)):
            for alt_sequence in range(sequence+1,len(seq)):
                if (seq[sequence][:loc] + seq[sequence][loc+1:]) == (seq[alt_sequence][:loc] + seq[alt_sequence][loc+1:]):
                    final_array[sequence] = all_sums[sequence] + all_sums[alt_sequence]

    # get the truth assignment for the highest probability
    location = seq[final_array.index(max(final_array))]
    truth_assignment = []
    # place the truth assignment in a more readable fashion
    for value in range(len(terms)):
        if terms[value] in search_array:
            if location[value] == '0':
                truth_assignment.append(terms[value][0]+ ' = False')
            else:
                truth_assignment.append(terms[value][0]+ ' = True')
    return (truth_assignment)
    
        
    
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
   
        
        
        

            
    
        
        

