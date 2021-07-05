class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False

    def traversal(self, pos):
        currNode = self.head
        start = 0
        while start != pos:
            currNode= currNode.next
            start+=1
        return currNode

    def insert(self,data,pred):
        newNode = Node(data)
        newNode.next = pred.next
        pred.next = newNode

    def delete(self,curr, pred):
        pred.next = curr.next
        del curr.data
        del curr.next

    def printLL(self):
        currNode = self.head
        arr = []
        if self.is_empty():
            pass
        while currNode.next != None:
            arr.append(str(currNode.data))
            currNode = currNode.next
        arr.append(str(currNode.data))
        string = '-->'.join(arr)
        print("HEAD"+string)
