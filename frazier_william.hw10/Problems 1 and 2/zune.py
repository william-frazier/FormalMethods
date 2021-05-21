


# William Frazier
# CS511 HW10

from zune_flowchart import zune_fc, zune_fc_S



def paths(fc, k, lbl1, lbl2):
    """
    Returns a list of all paths of at most length k. 
    Inputs: fc- a flowchart encoding of a program, k- an integer representing
    the max length of a path, lbl1 and lbl2- string encodings of the label
    """
    
    # We begin with a set (we will convert it to a list later)
    # The set is just an easier way for me to avoid duplicates
    path_list = set()
    # if k is 0 then we return an empty list
    if k == 0:
        return list(path_list)
    # if the max path length is 1 then we simply check if such a path exists
    elif k == 1:
        # we scan every row
        for row in fc:
            # looking for an instruction that completes the path
            if row[0] == lbl1 and row[2] == lbl2:
                path_list.add((row[0], row[1], row[2]))
        return list(path_list)
    # if the path is longer than 1, we can simply look recursively    
    else:
        # we scan every row
        for row in fc:
            # if we find a row that starts at the correct label
            if row[0] == lbl1:   
                # then we recursively look for possible extensions from that 
                # instruction. With the requirement that k is now 1 less
                # because we already have the first instruction
                poss_paths = paths(fc, k-1, row[2], lbl2)
                # now loop through the paths we have identified
                for possibility in poss_paths:
                    # and add the starting label and its instruction
                    path = (lbl1, row[1]) + possibility
                    # add it the path to our set
                    path_list.add(path)
    # now we combine all of the paths we have identified
    while k > 0:
        k -= 1
        path_list = union(path_list, paths(fc, k, lbl1, lbl2))
    
    return path_list


def full_paths(fc, k):
    """
    Returns a list of all full paths of at most length k.
    Inputs: fc- a flowchart encoding of a program, k- an integer representing
    the max length of a path
    """
    
    # exit_nodes will keep track of all exit nodes
    # I leave open the possibility that there is more than one
    exit_nodes = set()
    # non_exit_nodes will keep track of all nodes that have an associated
    # instruction (and are therefore not exit nodes)
    non_exit_nodes = set()
    # full_paths will be the list we return of all possible full paths
    full_paths = set()
    # collect all nodes associated with an instruction
    for row in fc:
        non_exit_nodes.add(row[0])
    # find all nodes that don't have an associated instruction
    for row in fc:
        if row[2] not in non_exit_nodes:
            exit_nodes.add(row[2])
    # now look for all paths from the init node to the exit nodes
    # NB: I assume (without loss of generality) that the init node is "1"
    for possible_exits in exit_nodes:
        full_paths = union(full_paths, paths(fc, k, "1", possible_exits))
    return full_paths








def union(a, b):
    """ 
    Helper function from the internet. Returns the union of two lists. 
    """
    return list(set(a) | set(b))

