



from equitable_graph_coloring import *



print("Running on [[1,[2,3,4,5]],[2,[1,4]],[3,[1,5]],[4,[1,2,5]],[5,[1,3,4]]]")
print("")
print(create_graph([[1,[2,3,4,5]],[2,[1,4]],[3,[1,5]],[4,[1,2,5]],[5,[1,3,4]]]))
print("")
print("The above ran on [[1,[2,3,4,5]],[2,[1,4]],[3,[1,5]],[4,[1,2,5]],[5,[1,3,4]]]")
print("")

input("Press enter to continue.")
print("Running on [[1,[2]],[2,[1]]]")
print("")
print(create_graph([[1,[2]],[2,[1]]]))
print("")
print("The above ran on [[1,[2]],[2,[1]]]")
print("")

input("Press enter to continue.")
print("Running on [[1,[2,4,5]],[2,[1,3,4,6]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]]]")
print("")
print(create_graph([[1,[2,4,5]],[2,[1,3,4,6]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]]]))
print("")
print("The above ran on [[1,[2,4,5]],[2,[1,3,4,6]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]]]")
print("")

input("Press enter to continue.")
print("Running on [[1,[2,3,5,6,7]],[2,[1,4,6,8]],[3,[1,8]],[4,[2,6,9]],[5,[1,9]],[6,[1,2,4,10]],[7,[1,9,10]],[8,[2,3]],[9,[4,5,10]],[10,[6,7,9]]]")
print("")
print(create_graph([[1,[2,3,5,6,7]],[2,[1,4,6,8]],[3,[1,8]],[4,[2,6,9]],[5,[1,9]],[6,[1,2,4,10]],[7,[1,9,10]],[8,[2,3]],[9,[4,5,10]],[10,[6,7,9]]]))
print("")
print("The above ran on [[1,[2,3,5,6,7]],[2,[1,4,6,8]],[3,[1,8]],[4,[2,6,9]],[5,[1,9]],[6,[1,2,4,10]],[7,[1,9,10]],[8,[2,3]],[9,[4,5,10]],[10,[6,7,9]]]")
print("")

print("These are the only tests I coded but just run 'create_graph(input)' to test your own graphs.")