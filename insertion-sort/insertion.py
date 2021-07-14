def insertionSort(ar):
    for i in range(1,len(ar)):
        key = ar[i]
        j = i -1
        while j>=0 and key < ar[j]:
            ar[j+1] = ar[j]
            j -=1
        ar[j+1] = key
    return ar

if __name__=='__main__':
    ar = list(map(int, input().rstrip().split()))
    print("The unsorted array:",ar)
    arr = insertionSort(ar)
    print("The sorted array:",arr)