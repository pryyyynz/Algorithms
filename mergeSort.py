def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    sort_left = mergeSort(left)
    sort_right = mergeSort(right)

    return merge(sort_left, sort_right)


def merge(left, right):
    array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array.append(left[i])
            i += 1

        else:
            array.append(right[j])
            j+= 1


    array.extend(left[i:])
    array.extend(right[j:])

    return array

print(mergeSort([5,4,3,2,1]))
print(mergeSort([3,6,1,6,0,43,1,12]))


