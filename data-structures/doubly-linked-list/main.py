from doublyLinkedList import DoublyLL
from doublyLinkedList import title
from os import system

if __name__=='__main__':
    d=DoublyLL()
    while True:
        system("clear")
        title()
        print("Your options are:")
        print("0. Quit")
        print("1. Add node in beginning")
        print("2. Add node in n-th position")
        print("3. Add to the last")
        print("4. Remove node from the beginning")
        print("5. Remove node from n-th position")
        print("6. Remove from the last")
        print("7. Show data")
        n = int(input("Enter your option: "))
        if n == 0:
            break
        elif n==1:
            system("clear")
            title()
            data = int(input("Enter the data you want to add: "))
            d.addToHead(data)
            print(f"Successfully added {data} at the beginning")
        elif n==2:
            system("clear")
            title()
            pos = int(input("Enter the position you want your data in: "))
            data = int(input("Enter the data you want to add: "))
            curr = d.traversal(pos-1)
            d.add(curr,data)
            print(f"Successfully added {data} to the {pos}-th position")
        elif n==3:
            system("clear")
            title()
            data = int(input("Enter the data you want to add: "))
            if d.is_empty():
                d.addToHead(data)
            else:
                d.addToTail(data)
            print(f"Successfully added {data} at the end.")
        elif n==4:
            system("clear")
            title()
            if d.is_empty():
                d.addToHead(data)
            else:
                d.removeFromHead()
        elif n==5:
            system("clear")
            title()
            if d.is_empty():
                print("Nothing to kick out")
                pass
            pos = int(input("Enter the position of the node to remove: "))
            curr = d.traversal(pos-1)
            if curr.prev==None and curr.next==None:
                d.removeFromHead()
            else:
                print(f"Successfully Kicked out {curr.data} from the {pos}-th position")
                d.remove(curr)
        elif n==6:
            system("clear")
            title()
            if d.is_empty():
                print("Nothing to kick out")
                pass
            else:
                d.removeFromTail()
        elif n==7:
            system("clear")
            title()
            d.printLL()