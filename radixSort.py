def radixSort(array):
    print("Unsorted Array", array)
    radix = [[], [], [], [], [], [], [], [], [], []]
    max_val = max(array)
    place = 1
    while max_val // place > 0:
        while len(array) > 0:
            val = array.pop()
            index = (val // place) % 10
            radix[index].append(val)
        for bucket in radix:
            while len(bucket) > 0:
                array.append(bucket.pop())
        place *= 10
    print("Sorted Array", array)

radixSort([5,4,3,2,1])
radixSort([3,6,1,6,0,43,1,12])
radixSort([3,6,1,6,0,43,1,12,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])