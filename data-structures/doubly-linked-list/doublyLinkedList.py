class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    def __init(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def traversal(self,pos):
        count = 0
        currNode = self.head
        while count != pos:
            currNode = currNode.next
            count+=1
        return currNode
    
    def addToHead(self,data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            frontNode = self.head
            node.next = frontNode
            frontNode.prev = node.next
            self.head = node

    def addToTail(self,data):
        if self.is_empty():
            self.addToHead(data)
        else:
            node = Node(data)
            currNode = self.head
            while currNode.next != None:
                currNode = currNode.next
            currNode.next = node
            node.prev = currNode
    
    def add(self,curr,data):
        node = None(data)
        prec = curr.prev
        node.next = curr
        node.prev = prec
        prec.next = node
        curr.prev = node

    def removeFromHead(self):
        currNode = self.head
        self.head = currNode.next
        del currNode.data
        del currNode.next
        del currNode.prev
        currNode = self.head
        currNode.prev = None

    def removeFromTail(self):
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
        prevNode = currNode.prev
        prevNode.next = None
        del currNode.data
        del currNode.next
        del currNode.prev

    def remove(self,curr):
        if curr.next ==None:
            self.removeFromTail()
        else:
            node1 = curr.prev
            node2 = curr.next
            node1.next = node2
            node2.prev = node1
            del curr.data
            del curr.prev
            del curr.next

    def printAll(self):
        if self.is_empty():
            print("Your Linked List Is Empty :(")
            pass
        else:
            arr = []
            currNode = self.head
            while currNode.next != None:
                arr.append(str(currNode.data))
                currNode = currNode.next
            arr.append(str(currNode.data))
            if len(arr)==1:
                print("HEAD"+"<-->"+arr[0])
            else:
                string = '<-->'.join(arr)
                print("HEAD"+"<-->"+string)
