class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
    
    def find_node(self, point, data):
        if point == None:
            print(f"{data} id not present in the BST!")
        else:
            if point.data == data:
                return point
            else:
                if data < point.data:
                    self.find_node(point.left, data)
                elif data > point.data:
                    self.find_node(point.right,data)
    
    def minVal(self, node):
        if node.left == None:
            return node
        else:
            self.minVal(node.left)

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insertFromRoot(self.root,data)
    
    def insertFromRoot(self, point, data):
        if data < point.data:
            if point.left == None:
                point.left = Node(data)
            else:
                self.insertFromRoot(point.left, data)
        elif data > point.data:
            if point.right == None:
                point.right = Node(data)
            else:
                self.insertFromRoot(point.right, data)
        elif data == point.data:
            print(f"{data} already exists on the BST!")
    
    def remove(self, data):
        if self.root == None:
            print("Nothing to delete!")
        elif self.root.data == data and  self.root.right == None and self.root.left == None:
            print(f"Successfully kicked out {data}!")
            self.root = None
        else: 
            self.removeFromRoot(self.root, self.root,data)
    
    def removeFromRoot(self, parent ,point, data):
        if point == None:
            print(f"{data} id not present in the BST!")
        else:
            if data < point.data:
                self.removeFromRoot(point, point.left, data)
            elif data > point.data:
                self.removeFromRoot(point, point.right, data)
            else:
                if point.right == None and point.left == None:
                    if parent.right.data == point.data:
                        parent.right = None
                    else:
                        parent.left = None
                    del point.data
                    del point.left
                    del point.right
                    del point
                    print(f"Successfully kicked out {data}!")
                elif point.left == None:
                    temp = point.right
                    point.data = temp.data
                    point.left = temp.left
                    point.right = temp.right
                    print(f"Successfully kicked out {data}!")
                elif point.right == None:
                    temp = point.left
                    point.data = temp.data
                    point.left = temp.left
                    point.right = temp.right 
                    print(f"Successfully kicked out {data}!")               
                else:
                    minNode = self.minVal(point.right)
                    point.data = minNode.data
                    self.removeFromRoot(point, point.right, minNode.data)
    
    def traverseBST(self):
        show= []
        if self.root == None:
            return False
        else:
            self.inorderBST(self.root,show)
            return show

    def inorderBST(self,currentNode,show):
        if currentNode!=None:
            self.inorderBST(currentNode.left,show)
            show.append(str(currentNode.data))
            self.inorderBST(currentNode.right,show)


def title():
    print("----------------Binary Search Tree----------------")