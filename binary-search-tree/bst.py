class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
    
    def find_node(self, point, data):
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

    def remove(self, point, data):
        if point == None:
            print("Nothing to delete!")
        
        if data < point.data:
            self.remove(point.left, data)
        elif data > point.data:
            self.remove(point.right, data)
        else:
            if point.left == None:
                point = point.right
    
            elif point.right == None:
                point = point.left
            
            else:
                minNode = self.minVal(point.right)
                minNode.left = point.left
                minNode.right = point.right
                point = minNode
                # print(f"{minNode}")
                del minNode
