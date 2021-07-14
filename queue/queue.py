class Queue:
    def __init__(self,size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.arr = [None]*size

    def is_empty(self):
        if self.front == -1 and self.rear == -1:
            print("No one lining up here! Your queue is empty!")
            return True
        else:
            return False

    def is_full(self):
        if self.rear == self.size-1:
            print("Too many! TOO MANY!! Your queue is full!!!")
            return True
        else:
            return False

    def print_all(self):
        print('Your stack is:')
        str1 = '|'.join(filter(None, map(str, self.arr)))
        print(str1)
        _ = input("Press Enter to continue...")

    def enqueue(self):
        if self.front==-1 and self.rear ==-1:
            self.front,self.rear = 0,0
            val = int(input("Enter the number you want in queue: "))
            self.arr[self.rear] = val
            print(f"Successfully added {val} to the queue")
            _ = input("Press any key to continue...")
        else:
            self.rear+=1
            val = int(input("Enter the number you want in queue: "))
            self.arr[self.rear]= val
            print(f"Successfully added {val} to the queue")
            _ = input("Press any key to continue...")

    def dequeue(self):
        if self.front==0 and self.rear ==0:
            print(f"Kicking out {self.arr[self.front]} from queue")
            self.arr[self.front]= None
            self.front,self.rear = -1,-1
            _ = input("Press any key to continue...")
        else:
            print(f"Kicking out {self.arr[self.front]} from queue")
            self.arr[self.front] = None
            for i in range(len(self.arr[:self.rear])):
                self.arr[i]= self.arr[i+1]
            self.arr[self.rear]=None
            self.rear-=1
            _ = input("Press any key to continue...")