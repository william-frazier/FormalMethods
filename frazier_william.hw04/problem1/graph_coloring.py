
#William Frazier
#CS511 HW04
#Graph Coloring

from z3 import *


###### instances

# create_graph([[1,[2,4,5]],[2,[1,3,4,6]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]]])
# create_graph([[1,[2,3,4,5]],[2,[1,4]],[3,[1,5]],[4,[1,2,5]],[5,[1,3,4]]])


def create_graph(graph_input):
    """
    Produces a graph coloring with as few colors as possible. Returns 'unsat'
    if it cannot be done with 20 colors.
    """
    
    num_nodes = len(graph_input)
    # This program works by starting with 1 color and slowly building until
    # a graph coloring can be built. This ensures we use the minimum required
    # number of colors. It works well for most graphs but is a bit
    # slower of an approach as the graph approaches needing 20 colors.
    num_colors = 1
    while num_colors <= 20:   
        s = Solver()
        # array stores the edges in the graph
        array = [ [ Bool("g_%s_%s" % (i+1, j+1)) for j in range(num_nodes) ] for i in range(num_nodes) ]
        #color stores the color of each node
        #c_i_j is node i, color j
        color = [ [ Bool("c_%s_%s" % (i+1, j+1)) for j in range(num_colors) ] for i in range(num_nodes) ]
        for node in graph_input:
            # add in our edges
            for edge in node[1]:
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
            print(s.model())
            return "Minimum number of colors required: " + str(num_colors)
        else:
            num_colors += 1
    return "unsat"