from stack import Stack
import os

if __name__=='__main__':
    size = int(input("Enter the size of your stack: "))
    s = Stack(size)
    while True:
        os.system('clear')
        print("Your options are:")
        print("0. Quit")
        print("1. Push")
        print("2. Pop")
        print("3. Print stack")
        n=int(input("Enter the option: "))
        if n==0:
            break
        elif n==1:
            os.system('clear')
            temp = int(input("Enter the number you want to push: "))
            s.push(temp)
        elif n==2:
            os.system('clear')
            s.pop()
        elif n==3:
            os.system('clear')
            s.print_all()
        elif n==4:
            s.is_full()
