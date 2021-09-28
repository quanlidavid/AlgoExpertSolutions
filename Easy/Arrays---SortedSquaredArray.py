# Sorted Squared Array
# Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.
#
# Sample Input
# array = [1, 2, 3, 5, 6, 8, 9]
# Sample Output
# [1, 4, 9, 25, 36, 64, 81]

# 先遍历生成时间是O(n),再排序. 有个排序的时间,最好的排序时间是O(nlogn), 所以总时间是n + nlogn,  n < nlogn, 假设为2nlogn, 2是常量所以可以去掉.
# O(nlogn) time | O(n) space
def sortedSquaredArray(array):
    sortedSquaresArray = []
    for i in range(len(array)):
        sortedSquaresArray.append(array[i] * array[i])
    sortedSquaresArray.sort()
    print(sortedSquaresArray)
    return sortedSquaresArray


# 先遍历循环, 再查找插入
# O(n^2) time | O(n) space
def sortedSquaredArraySecond(array):
    sortedSquaresArray = []
    for i in range(len(array)):
        if len(sortedSquaresArray) == 0:
            sortedSquaresArray.append(array[i] * array[i])
        else:
            if sortedSquaresArray[len(sortedSquaresArray) - 1] <= array[i] * array[i]:
                sortedSquaresArray.append(array[i] * array[i])
            else:
                for j in range(0, len(sortedSquaresArray)):
                    if sortedSquaresArray[j] > array[i] * array[i]:
                        sortedSquaresArray.insert(j, array[i] * array[i])
                        break
    print(sortedSquaresArray)
    return sortedSquaresArray


# 因为数组已经排过序了,用两个指针, 第一个在最左边, 第二个在最右边, 从右向左构建新的数组, 比较两个数的绝对值大小,把绝对值大的放在新数组里.
# O(n) time | O(n) space
def sortedSquaredArrayThird(array):
    sortedSquaresArray = [0 for _ in array]
    start = 0
    end = len(array) - 1
    for i in reversed(range(len(array))):
        smallerValue = array[start]
        largerValue = array[end]
        if abs(smallerValue) > abs(largerValue):
            sortedSquaresArray[i] = array[start] * array[start]
            start += 1
        else:
            sortedSquaresArray[i] = array[end] * array[end]
            end -= 1
    print(sortedSquaresArray)
    return sortedSquaresArray


array = [-5, -4, -3, -2, -1, 2, 4]
sortedSquaredArrayThird(array)
