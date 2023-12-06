def binary_search(array, target):
    #make two pointers
    left = 0
    right = len(array) - 1
   # while left is before or equal to right
    while left <= right:
        # identify the current midpoint - add both pointers, divide by two, round down
        mid = (left+right) // 2
        # if the midpoint value is the target value, return that index
        if array[mid] == target:
            return mid
        # if midpoint value is less than the target value, eliminate elements left of mid from subsequent searches
        if array[mid] < target:
            left = mid + 1
        else:
            # if midpoint value is more than the target value, eliminate elements right of mid from subsequent searches
            right = mid - 1
    return -1