def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    print(array)

insertionSort([5,4,3,2,1])
insertionSort([3,6,1,6,0,43,1,12])
insertionSort([3,6,1,6,0,43,1,12,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])