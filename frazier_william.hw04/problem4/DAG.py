
#William Frazier
#CS511 HW04
#DAG

from z3 import *


###### instances

# create_graph([[1,[2,4,5]],[2,[1,3,4,6]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]]])
# create_graph([[1,[2,3,4,5]],[2,[1,4]],[3,[1,5]],[4,[1,2,5]],[5,[1,3,4]]])
# create_graph([[1,[2,4]],[2,[3]],[3,[5]],[4,[2,5]],[5,[6]],[6,[]]])
# create_graph([[1,[2,4]],[2,[1,3]],[3,[2,6]],[4,[1]],[5,[6]],[6,[3,5]],[7,[]],[8,[1,2]],[9,[1,8]]])
# create_graph([[1,[2,4,5,10]],[2,[3,10]],[3,[4,7]],[4,[1,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]],[9,[]],[10,[9]]])
# create_graph([[1,[2,4]],[2,[3,5]],[3,[5]],[4,[2,3,5]],[5,[6]],[6,[]]])


def create_graph(graph_input):
    """
    If a given graph contains a loop, returns 'unsat'. Else, returns, 'This is a DAG.'
    """
    
    num_nodes = len(graph_input)
    s = Solver()
    # see if there is a DAG in the first few or last few nodes because it 
    # doesn't take much time and could potentially save a lot of time
    if len(graph_input) > 6:
        if create_graph(graph_input[:5]) == 'unsat':
            return 'unsat'
        if create_graph(graph_input[-5:]) == 'unsat':
            return 'unsat'
    # array to store our edges
    array = [ [ Bool("g_%s_%s" % (i+1, j+1)) for j in range(num_nodes) ] for i in range(num_nodes) ]
    for node in graph_input:
        # try and except needed because of my recursive calls above
        try:
            possible_links = [x+1 for x in range(num_nodes)]
            for edge in node[1]:
                #add in all edges
                possible_links.remove(edge)
                s.add(array[node[0]-1][edge-1])
            # prevent z3 from adding in edges
            # I don't think this is actually needed but it just ensure the
            # behavior that I want
            for no_edge in possible_links:
                s.add(Not(array[node[0]-1][no_edge-1]))
        except:
            continue
    # an array to build the main constraint
    all_constraint = []
    # create all possible permutations of the nodes in order to check if 
    # this graph can be topographically sorted
    for arrangement in permutation([x+1 for x in range(num_nodes)]):
        # previous stores all nodes left of the current position, if any egdes
        # connect to a previous node then this permutation fails
        previous = []
        constraint = []
        for node in arrangement:
            # ensure no nodes connect to a previous node
            arrangement_constraint = Not(Or([array[node-1][x-1] for x in previous]))
            constraint.append(arrangement_constraint)
            previous.append(node)
        # it must be the case that no node in a given permutation connects to
        # nodes that came before it
        one_test = And(constraint)
        all_constraint.append(one_test)
    # we only need one of these constraints to be true
    s.add(Or(all_constraint))
    
    if s.check() == sat:
        m = s.model()
        #print(m)
        return "This is a DAG."
    return "unsat"


def permutation(lst): 
    """
    A helper function which creates all possible permutations of a list. 
    Copied from https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
    """
    
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 



 