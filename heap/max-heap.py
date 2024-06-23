class Heap():
    def __init__(self, heap = None) -> None:
        if not heap: # Handles if Heap class is initialized without any elements
            heap = []
        self.heap = heap
    
    def add(self, elem):
        self.heap.append(elem)
        self.heapify_up()
    
    def heapify_up(self):
        current = len(self.heap) - 1
        while current > 0:
            parent = (current - 1) // 2
            if self.heap[current] > self.heap[parent]:
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
                current = parent
            else:
                break
    
    def delete(self):
        if not self.heap:
            print('NOTHING TO DELETE')
            return

        if len(self.heap) == 1:
            self.heap.pop()
            return
        
        last_elem = self.heap.pop()
        self.heap[0] = last_elem
        self.heapify_down(0, len(self.heap))

    def heapify_down(self, i, n):
        while i < n:
            greatest = i
            left = (2 * greatest) + 1
            right = (2 * greatest) + 2
            if left < len(self.heap[:n]) and self.heap[greatest] < self.heap[left]:
                greatest = left

            if right < len(self.heap[:n]) and self.heap[greatest] < self.heap[right]:
                greatest = right
            
            if greatest != i:
                self.heap[i], self.heap[greatest] = self.heap[greatest], self.heap[i]
                i = greatest
            else:
                break


    def heap_sort(self):
        n = len(self.heap)
        if not self.heap:
            print('Empty Heap')
            return
        
        if n == 1:
            return self.heap
        
        last_elem = n - 1
        while last_elem > 0:
            self.heap[last_elem], self.heap[0] = self.heap[0], self.heap[last_elem]
            self.heapify_down(0, last_elem)
            last_elem -= 1


    def show_heap(self):
        print('MAX HEAP:', self.heap)
        
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

    h.heap_sort()
    h.show_heap()