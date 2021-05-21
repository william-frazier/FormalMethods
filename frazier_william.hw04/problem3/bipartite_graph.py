
#William Frazier
#CS511 HW04
#Bipartite Graph

from z3 import *


###### instances

# create_graph([[1,[2,4,5]],[2,[1,3,4,6]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]]])
# create_graph([[1,[2,3,4,5]],[2,[1,4]],[3,[1,5]],[4,[1,2,5]],[5,[1,3,4]]])
# create_graph([[1,[2,4,6]],[2,[1,3,5,7]],[3,[2,4]],[4,[1,3,7]],[5,[2]],[6,[1]],[7,[2,4,6]]])
# create_graph([[1,[2,4,5,9]],[2,[1,3,4,6,9]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2,9]],[7,[3]],[8,[4,9]],[9,[1,6,2,8]]])



def create_graph(graph_input):
    """
    Returns 'unsat' if the graph is not bipartite. Returns a valid separation 
    of the nodes if it is.
    """
    
    # if there is only one node, the graph isn't bipartite
    if len(graph_input) == 1:
        return 'This graph only contains 1 node.'
    num_nodes = len(graph_input)
    num_colors = 2 
    s = Solver()
    # this array stores the edges in our graph
    array = [ [ Bool("g_%s_%s" % (i+1, j+1)) for j in range(num_nodes) ] for i in range(num_nodes) ]
    # color stores the color of each node 
    #c_i_j is node i, color j
    color = [ [ Bool("c_%s_%s" % (i+1, j+1)) for j in range(num_colors) ] for i in range(num_nodes) ]
    for node in graph_input:
        for edge in node[1]:
            # add our edges
            s.add(array[node[0]-1][edge-1])
            s.add(array[edge-1][node[0]-1])
    #Each node must have at least one color
    all_constraint = And([Or([(color[i][j]) for j in range(num_colors)]) for i in range(num_nodes)  ])
    s.add(all_constraint)
    #Nodes have at most 1 color
    one_constraint = [ Not( And( color[j][i], color[j][p] ))
                   for j in range(num_nodes)
                   for i in range(num_colors) for p in range(i+1,num_colors) ]
    s.add(one_constraint)
    #connected nodes cannot have the same color
    adjacent_constraint = [Not( And (array[j][i], And(color[i][k], color[j][k]))) \
        for i in range(num_nodes) for j in range(i+1, num_nodes) for k in range(num_colors)]
    s.add(adjacent_constraint)
    if s.check() == sat:
        # two groupings to separate our bipartite graph
        group_one = []
        group_two = []
        m = s.model()
        # this cascade of code is kind of a mess but it was the best I could
        # do to list the two groupings of nodes
        for d in m.decls():
            if str(m[d]) == "True":
                if str(d.name())[0] == 'c':
                    if str(d.name())[-1] == '1':
                        group_one.append(str(d.name())[2:].split('_')[0])
                    else:
                        group_two.append(str(d.name())[2:].split('_')[0])
        return "We can partition into nodes " + str(group_one) + " and " + str(group_two)
    return "This is not a bipartite graph."