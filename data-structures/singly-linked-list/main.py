if __name__=='__main__':
    while True:
        print("Your options are:")
        print("0. Quit")
        print("1. Add node")
        print("2. Remove node")
        print("3. Show data")
        n = int(input("Enter your option"))
        if n == 0:
            break
        elif n ==1:
            pos = int(input("Enter the position you want your node: "))
            data = input("Enter the data you want in your note:")
            # pred = s.traversal(pos-2)
            # s.insert(data,pred)
        elif n==2:
            pos = int(input("Enter the position of node you want to delete: "))
            pos-=1
            # pred = s.traversal(pos -2)
            # curr = s.traversal(pos-1)
            # s.delete(curr,pred)
        elif n==3:
            # s.printLL()