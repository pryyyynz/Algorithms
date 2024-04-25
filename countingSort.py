def countingSort(array):
    max_val = max(array)
    counter = [0]*(max_val+1)

    while len(array)>0:
        num = array.pop()
        counter[num] += 1

    for i in range(len(counter)):
        while counter[i]>0:
            array.append(i)
            counter[i] -= 1
    print(array)


countingSort([5,4,3,2,1])
countingSort([3,6,1,6,0,43,1,12])
countingSort([3,6,1,6,0,43,1,12,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])