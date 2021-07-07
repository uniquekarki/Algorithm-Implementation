from singlyLinkedList import SinglyLL

if __name__=='__main__':
    l = SinglyLL()
    while True:
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
            data = int(input("Enter the data you want in your node: "))
            l.addToHead(data)
            print(f"Added {data} to the first position.")
        elif n ==2:
            pos = int(input("Enter the position you want your node: "))
            data = int(input("Enter the data you want in your note: "))
            if pos==1:
                l.addToHead(data)
                print(f"Added {data} to the {pos}-th position")
            else:
                pred = l.traversal(pos-2)
                l.insert(data,pred)
                print(f"Added {data} to the {pos}-th position")
        elif n ==3:
            data = int(input("Enter the data you want in your note: "))
            l.addToTail(data)
            print(f"Added {data} to the last position.")
        elif n ==4:
            l.removeFromHead()
        elif n==5:
            pos = int(input("Enter the position of node you want to delete: "))
            pred = l.traversal(pos -2)
            curr = l.traversal(pos-1)
            l.delete(curr,pred)
            print(f"Removed {curr.data} from {pos}-th position.")
        elif n==6:
            l.removeFromTail()
        elif n==7:
            l.printLL()