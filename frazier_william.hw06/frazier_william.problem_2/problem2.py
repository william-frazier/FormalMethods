

#William Frazier
#CS511
#HW06


from z3 import *
import json

def max_cut(graph):
    """
    Calculate how to cut a graph in order to achieve the max cut value.
    """
    
    #we don't actually need w but since it is given in the encoding, I store it here
    w = graph[0]
    c = graph[1]
    s = z3.Optimize()
    X = [Int("x_%s" % (k+1)) for k in range(len(w))]
    #initialize our optimization
    maximize = 0
    #this loop builds our optimization
    for i in range(len(w)):
        for j in range(i+1,len(w)):
            maximize += c[i][j] * ((1-X[i])*X[j]+X[i]*(1-X[j]))
    s.maximize(maximize)
    #restrict every x to being either 0 or 1
    for term in X:
        s.add(term <= 1, term >= 0)
    s.check()
    return s.model()

def open_file(file):
    """
    Runs max_cut using an instance in a file.
    """
    
    f = open(file, 'r')
    if f.mode == 'r':
        contents = f.read()
    instance = json.loads(contents) 
    return max_cut(instance)