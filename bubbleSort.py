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