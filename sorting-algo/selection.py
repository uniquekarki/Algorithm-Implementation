def selectionSort(ar):
    minVal = 0
    for i in range(len(ar)):
        minVal = i
        for j in range(i+1, len(ar)):
            if ar[j]<ar[minVal]:
                minVal = j
        ar[i],ar[minVal] = ar[minVal],ar[i]
    return ar

if __name__== "__main__":
    ar = []
    ar = list(map(int, input().rstrip().split()))
    print("The unsorted array:",ar)
    arr = selectionSort(ar)
    print("The sorted array:",arr)