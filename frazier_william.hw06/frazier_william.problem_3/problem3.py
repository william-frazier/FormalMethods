

#William Frazier
#CS511
#HW06


from z3 import *
import json

def max_weight(graph):
    """
    Calculate how to segment a graph in order to achieve the max weight.
    """
    
    w = graph[0]
    c = graph[1]
    max_w = max(w)
    s = z3.Optimize()
    #create our variables that indicated if each vertice is in S or V-S
    X = [Int("x_%s" % (k+1)) for k in range(len(w))]
    #initialization of our optimization
    maximize = 0
    #this loop builds our optimization
    for i in range(len(w)):
        maximize += w[i] * X[i]
        max_term = 0
        for j in range(i,len(w)):
            max_term += c[i][j] * X[i] * X[j]
        maximize -= (1+max_w) * max_term
    #add it to s
    s.maximize(maximize)
    #restrict each x to being either 0 or 1
    for term in X:
        s.add(term <= 1, term >= 0)
    s.check()
    return s.model()

def open_file(file):
    """
    Runs max_weight using an instance in a file.
    """
    
    f = open(file, 'r')
    if f.mode == 'r':
        contents = f.read()
    instance = json.loads(contents) 
    return max_weight(instance)
        