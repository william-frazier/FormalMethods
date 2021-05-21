




from problem2 import open_file, max_cut

def run(instance):
    return max_cut(instance)

def run_from_file(file):
    return open_file(file)



#run([[1,2,3,4,5,6],[[0,1,0,0,4,0],[1,0,0,3,3,1],[0,0,0,7,0,2],[0,3,7,0,0,1],[4,3,0,0,0,1],[0,1,2,1,1,0]]])
#run([[1,2,3,4,5],[[0,1,4,1,0],[1,0,0,3,3],[4,0,0,1,0],[1,3,1,0,0],[0,3,0,0,0]]])    

