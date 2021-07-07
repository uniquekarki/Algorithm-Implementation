from singlyLinkedList import SinglyLL
from singlyLinkedList import title
from os import system

if __name__=='__main__':
    l = SinglyLL()
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
            data = int(input("Enter the data you want in your node: "))
            l.addToHead(data)
            print(f"Added {data} to the first position.")
            _ = input("Enter any key to continue...")
        elif n ==2:
            system("clear")
            title()
            pos = int(input("Enter the position you want your node: "))
            data = int(input("Enter the data you want in your note: "))
            if pos==1:
                l.addToHead(data)
                print(f"Added {data} to the {pos}-th position")
                _ = input("Enter any key to continue...")
            else:
                pred = l.traversal(pos-2)
                l.insert(data,pred)
                print(f"Added {data} to the {pos}-th position")
                _ = input("Enter any key to continue...")

        elif n ==3:
            system("clear")
            title()
            data = int(input("Enter the data you want in your note: "))
            l.addToTail(data)
            print(f"Added {data} to the last position.")
            _ = input("Enter any key to continue...")
        elif n ==4:
            system("clear")
            title()
            l.removeFromHead()
            _ = input("Enter any key to continue...")
        elif n==5:
            system("clear")
            title()
            pos = int(input("Enter the position of node you want to delete: "))
            if l.is_empty():
                print("Nothing in the end to kick out!")
                _ = input("Enter any key to continue...")
                pass
            pred = l.traversal(pos -2)
            curr = l.traversal(pos-1)
            if pred == None or curr == None:
                l.removeFromHead()
                _ = input("Enter any key to continue...")
            else:
                print(f"Removed {curr.data} from {pos}-th position.")
                l.delete(curr,pred)
                _ = input("Enter any key to continue...")
        elif n==6:
            system("clear")
            title()
            l.removeFromTail()
            _ = input("Enter any key to continue...")
        elif n==7:
            system("clear")
            title()
            l.printLL()
            _ = input("Enter any key to continue...")