# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:52:56 2019

@author: William
"""


#William Frazier
#CS511 HW04
#Equitable Graph Coloring

from z3 import *


###### instances

# create_graph([[1,[2,4,5]],[2,[1,3,4,6]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]]])
# create_graph([[1,[2,3,4,5]],[2,[1,4]],[3,[1,5]],[4,[1,2,5]],[5,[1,3,4]]])
# create_graph([[1,[2,4,6]],[2,[1,3,5,7]],[3,[2,4]],[4,[1,3,7]],[5,[2]],[6,[1]],[7,[2,4,6]]])
# create_graph([[1,[2,4,5,9]],[2,[1,3,4,6,9]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2,9]],[7,[3]],[8,[4,9]],[9,[1,6,2,8]]])

######


def create_graph(graph_input):
    """
    Returns a valid equitable coloring of size delta_G or delta_G + 1.
    Note, it does not search for equitable colorings of a smaller size
    """
    
    results = []
    num_nodes = len(graph_input)
    max_degree = 0
    # find the maximum degree of any node
    for node in graph_input:
        if len(node[1]) > max_degree:
            max_degree = len(node[1])
    num_colors = max_degree
    s = Solver()
    # begin searching at size of max degree
    while num_colors <= max_degree + 1:  
        # array stores our edges
        array = [ [ Bool("g_%s_%s" % (i+1, j+1)) for j in range(num_nodes) ] for i in range(num_nodes) ]
        #color stores the color of a given node
        color = [ Int("c_%s" % (i+1)) for i in range(num_nodes) ]
        for node in graph_input:
            for edge in node[1]:
                # add in our edges
                s.add(array[node[0]-1][edge-1])
                s.add(array[edge-1][node[0]-1])
        #Each node must have at least one color
        all_constraint = [0 < color[i] for i in range(num_nodes)  ]
        s.add(all_constraint)
        # restrict the number of colors
        max_constraint = [color[i] <= num_colors for i in range(num_nodes)]
        s.add(max_constraint)
        #connected nodes cannot have the same color
        adjacent_constraint = [Not( And (array[j][i], And(color[i] == color[j]))) \
            for i in range(num_nodes) for j in range(i+1, num_nodes)]
        s.add(adjacent_constraint)
        while s.check() == sat:
            m = s.model()
            color_array = [0] * num_colors
            count = 0
            # count how many nodes of each color
            for d in m.decls():
                if count < num_nodes:
                    try:
                        color_array[int(str(m[d]))-1] += 1
                        count += 1
                    except:
                        continue
                else:
                    count += 1
            # check if the graph is equitable
            if max(color_array) > (min(color_array) + 1):
               
                for d in m :
                    block = []
                    t = d()
                    # if the coloring isn't equitable then block it
                    block.append ( t != m[d] )
                    s.add (Or (block))
#############################################################
##### Uncomment this to see more coloring possibilities######
#############################################################
#            else:
#                results.append(m)
#                for d in m :
#                    block = []
#                    t = d()
#                    block.append ( t != m[d] )
#                    s.add (Or (block))
#       num_colors += 1
################################################################
#### Additionally, move this return statement back one tab #####
################################################################
            try:
                print(s.model())
            except:
                continue
            return "An equitable graph can be constructed with " + str(num_colors) + " colors."
        num_colors += 1
        s = Solver()
    return "unsat"