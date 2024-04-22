#The O(n2) algorithm for Bubble Sort

def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(i+1,n):
            if array[i]>array[j]:
                array[i], array[j] = array[j], array[i]
    print(array)


bubbleSort([5,4,3,2,1])
bubbleSort([3,6,1,6,0,43,1,12])
bubbleSort([3,6,1,6,0,43,1,12,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])
bubbleSort([1,2,3,4,5,6,7,8,9])