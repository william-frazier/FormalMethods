





from DAG import *



print("Running on [[1,[2,4,5]],[2,[1,3,4,6]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]]]")
print("")
print(create_graph([[1,[2,4,5]],[2,[1,3,4,6]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]]]))
print("")
print("The above ran on [[1,[2,4,5]],[2,[1,3,4,6]],[3,[2,4,7]],[4,[1,2,3,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]]]")
print("")

input("Press enter to continue.")
print("Running on [[1,[2]],[2,[1]]]")
print("")
print(create_graph([[1,[2]],[2,[1]]]))
print("")
print("The above ran on [[1,[2]],[2,[1]]]")
print("")

input("Press enter to continue.")
print("Running on [[1,[2,4]],[2,[3]],[3,[5]],[4,[2,5]],[5,[6]],[6,[]]]")
print("")
print(create_graph([[1,[2,4]],[2,[3]],[3,[5]],[4,[2,5]],[5,[6]],[6,[]]]))
print("")
print("The above ran on [[1,[2,4]],[2,[3]],[3,[5]],[4,[2,5]],[5,[6]],[6,[]]]")
print("")

input("Press enter to continue.")
print("Running on [[1,[2,4,5,10]],[2,[3,10]],[3,[4,7]],[4,[1,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]],[9,[]],[10,[9]]]")
print("")
print(create_graph([[1,[2,4,5,10]],[2,[3,10]],[3,[4,7]],[4,[1,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]],[9,[]],[10,[9]]]))
print("")
print("The above ran on [[1,[2,4,5,10]],[2,[3,10]],[3,[4,7]],[4,[1,8]],[5,[1]],[6,[2]],[7,[3]],[8,[4]],[9,[]],[10,[9]]]")
print("")

input("Press enter to continue.")
print("Running on [[1,[2,4]],[2,[3,5]],[3,[5]],[4,[2,3,5]],[5,[6]],[6,[]]]")
print("")
print(create_graph([[1,[2,4]],[2,[3,5]],[3,[5]],[4,[2,3,5]],[5,[6]],[6,[]]]))
print("")
print("The above ran on [[1,[2,4]],[2,[3,5]],[3,[5]],[4,[2,3,5]],[5,[6]],[6,[]]]")
print("")

print("These are the only tests I coded but just run 'create_graph(input)' to test your own graphs.")