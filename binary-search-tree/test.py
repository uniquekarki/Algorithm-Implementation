from bst import BST

b = BST()
point_m = b.root
list1 = b.traverseBST()
s = " ".join(list1)
print("In order traversal is",s)
b.insert(30)
b.remove(30)
b.insert(30)

b.insert(20)
b.insert(10)
b.insert(25)
b.insert(40)
b.insert(45)
b.insert(41)
b.insert(50)
print("HELLO WORLD!")
# point_m = b.root
# b.remove(30)
# b.remove(50)
# b.remove(57)
# print("HELLO WORLD!")
s = " ".join(b.traverseBST())
print("In order traversal is",s)
