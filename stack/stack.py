class Stack:

    def __init__(self,size):
        self.size = size
        self.top = -1
        self.arr = [None]*size
    
    def is_empty(self):
        if self.top==-1:
            print("Your stack is starving. It's empty!")
            return True
        else:
            return False
    
    def is_full(self):
        if self.top == (self.size-1):
            print("AHHH... Stack is already full!!!")
            return True
        else:
            return False
    
    def push(self):
        temp = int(input("Enter the number you want to push: "))
        self.top+=1
        self.arr[self.top]=temp
        print(f"Successfully added {temp} to the stack")
        _ = input("Press Enter to continue")
    
    def pop(self):
        print(f"Kicking out {self.arr[self.top]} from stack")
        self.arr[self.top]=None
        self.top-=1
        _ = input("Press Enter to continue")
    
    def print_all(self):
        print('Your stack is:')
        str1 = '|'.join(filter(None, map(str, self.arr)))
        print(str1)
        _ = input("Press Enter to continue")