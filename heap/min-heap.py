class Heap():
    def __init__(self, heap = None) -> None:
        if heap == None: # Handles if Heap class is initialized without any elements
            heap = []
        self.heap = heap

    def add(self, elem):
        self.heap.append(elem) # Adds element at the end of the heap
        self.heapify_up()

    def heapify_up(self):
        current = len(self.heap) - 1
        while current > 0:
            parent = (current - 1) // 2 # parent formula from children for 0-index heap
            if self.heap[current] < self.heap[parent]:
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
                current = parent
            else:
                break

    def delete(self):
        if not self.heap: # Handles if empty heap
            print("Nothing to delete")
            return
        
        if len(self.heap) == 1: # Handles if 1 element in heap
            self.heap.pop()
            return
        
        last_elem = self.heap.pop() # Handles if multiple elements in a heap
        self.heap[0] = last_elem
        self.heapify_down(0)

    def heapify_down(self, i):
        n = len(self.heap)
        while i < n:
            smallest = i
            left = (2 * i) + 1 # Formula for left child in 0-index heap
            right = (2 * i) + 2 # Formula for right child in 0-index heap

            # There are 2 seperate ifs so as to replace the current element with the smallest child possible among the two
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest != i:
                self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
                i = smallest
            else:
                break

    def show_heap(self):
        print("MIN HEAP:", self.heap)

if __name__ == '__main__':
    h = Heap()

    h.delete()

    h.add(10)
    h.show_heap()

    h.delete()
    h.show_heap()

    h.add(10)
    h.add(5)
    h.add(14)
    h.add(2)
    h.add(3)
    h.add(7)
    h.add(8)
    h.show_heap()

    h.delete()
    h.show_heap()