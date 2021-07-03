from queue import Queue
from os import system
from typing import Sized

if __name__ == '__main__':
    system('clear')
    size = int(input("Enter the size of the queue: "))
    q = Queue(size)
    while True:
        system('clear')
        print("Your options for queue are:")
        print("0. Quit")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Print your Queue")
        n = int(input("Enter your option: "))
        if n == 0:
            break
        elif n ==1:
            system('clear')
            if q.is_full():
                _ = input("Press any key to continue...")
                pass
            else:
                q.enqueue()
        elif n == 2:
            system('clear')
            if q.is_empty():
                _ = input("Press any key to continue...")
                pass
            else:
                q.dequeue()
        elif n ==3:
            system('clear')
            if q.is_empty():
                _ = input("Press any key to continue...")
                pass
            else:
                q.print_all()