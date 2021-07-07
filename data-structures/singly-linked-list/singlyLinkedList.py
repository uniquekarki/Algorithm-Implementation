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
    
    def addToHead(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addToTail(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.addToHead(data)
        else:
            currNode = self.head
            while currNode.next !=None:
                currNode = currNode.next
            currNode.next = newNode

    def insert(self,data,pred):
        newNode = Node(data)
        newNode.next = pred.next
        pred.next = newNode

    def removeFromHead(self):
        if self.is_empty():
            print("Nothing in the beggining to kick out!")
        else:
            currNode = self.head
            self.head = currNode.next
            print(f"Removed {currNode.data} from the beginning")
            del currNode.data
            del currNode.next
    
    def removeFromTail(self):
        if self.is_empty():
            print("Nothing in the end to kick out!")
        else:
            predNode = self.head
            nextNode = predNode.next
            while nextNode.next !=None:
                predNode = predNode.next
                nextNode = nextNode.next
            predNode.next = None
            print(f"Removed {nextNode.data} from the end.")
            del nextNode.data
            del nextNode.next
        
    
    def delete(self,curr, pred):
        if self.is_empty():
            print("Nothing in the beggining to kick out!")
        else:
            pred.next = curr.next
            del curr.data
            del curr.next

    def printLL(self):
        currNode = self.head
        arr = []
        if self.is_empty():
            print("Seems quiet. Your linked list is empty!!!")
            pass
        else:
            while currNode.next != None:
                arr.append(str(currNode.data))
                currNode = currNode.next
            arr.append(str(currNode.data))
            if len(arr)==1:
                print("HEAD"+"-->"+arr[0])
            else:
                string = '-->'.join(arr)
                print("HEAD"+"-->"+string)
