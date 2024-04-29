def binarySearch(array, target):
    n = len(array)
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

array = [3, 4, 5, 6, 7, 8, 9]
target = 6

result = binarySearch(array, target)

if result != -1:
    print("Target", target, "found at index", result)
else:
    print("Not found!")
