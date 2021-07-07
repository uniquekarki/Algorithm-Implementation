from  singlyLinkedList import SinglyLL
l = SinglyLL()

# l.is_empty()
# l.removeFromHead()


l.addToHead(1)

l.printLL()

l.addToTail(2)

l.printLL()

l.removeFromTail()
l.printLL()

l.addToTail(4)
l.printLL()

l.removeFromHead()
l.printLL()
l.removeFromHead()
l.printLL()

l.addToHead(6)
l.addToHead(5)
l.addToHead(4)
l.addToHead(3)
l.addToHead(2)
l.addToHead(1)

l.printLL()

pos =2
pred = l.traversal(pos-2)
l.insert(7,pred)
l.printLL()

pos = 2
pred = l.traversal(pos-2)
curr = l.traversal(pos-1)
l.delete(curr,pred)
l.printLL()

print(l.is_empty())