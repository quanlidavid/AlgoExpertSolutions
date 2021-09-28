# Binary Search
# Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.
#
# If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.
#
# Sample Input
# array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
# target = 33
# Sample Output
# 3

# O(logn) Time | O(1) Space
def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (right - left) // 2 + left
        if array[middle] > target:
            right = middle - 1
        elif array[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1


# 递归实现, 函数调用需要占用一定的内存, 函数调用栈占用的空间是O(logn)
# O(logn) Time | O(logn) Space
def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    if array[middle] == target:
        return middle
    elif array[middle] > target:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)


def binarySearchRecursion(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print(binarySearchRecursion(array, target))
