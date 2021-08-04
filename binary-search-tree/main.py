from bst import BST
from bst import title
from os import system

if __name__=='__main__':
    b = BST()
    while True:
        system("clear")
        title()
        print("Your options are:")
        print("0. Quit")
        print("1. Add node")
        print("2. Remove node")
        print("3. Search Node")
        print("4. Traverse BST")
        n = int(input("Enter your option: "))
        if n == 0:
            break
        elif n==1:
            system("clear")
            title()
            data = int(input("Enter the data you want to add: "))
            b.insert(data)
            print(f"Successfully added {data} at the beginning")
            _ = input("Enter any key to continue...")
        elif n==2:
            system("clear")
            title()
            data = int(input("Enter the data you want to delete: "))
            b.remove(data)
            _ = input("Enter any key to continue...")
        elif n==3:
            system("clear")
            title()
            data = int(input("Enter the data you want to find in BST: "))
            b.find_node(data)
            _ = input("Enter any key to continue...")
        elif n==4:
            system("clear")
            title()
            list1 = b.traverseBST()
            if list1 == False:
                print("No items in the BST!")
            else:
                s = " ".join(list1)
                print("In order traversal is",s)
            _ = input("Enter any key to continue...")