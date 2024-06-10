def heap(arr):
    for i in range(len(arr)):
        if not i == 0:
            current = i
            if (current % 2 == 0):
                parent_pos = (i // 2) - 1
            else:
                parent_pos = i // 2
            while arr[parent_pos] < arr[current]:
                if arr[parent_pos] < arr[current]:
                    arr[parent_pos], arr[current] = arr[current], arr[parent_pos]
                    current = parent_pos
                    if current % 2 == 0:
                        parent_pos = (current // 2) - 1
                    else:
                        parent_pos = current // 2
                    parent_pos = current // 2
    return arr

def heap_sort(arr):
    heap(arr)
    last_elem = len(arr) - 1
    while last_elem > 0:
        arr[0], arr[last_elem] = arr[last_elem], arr[0]
        arr[0:last_elem] = heap(arr[0:last_elem])
        last_elem -= 1
    return arr
    
arr = [6,99,33,54,11,2,9,1,100,0]
print('Max Heap:', heap(arr))

times = 1
print(f'Heap after {times} deletion:', heap_sort(arr))