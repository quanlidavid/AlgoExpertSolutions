# Two Number Sum
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order.
# If no two numbers sum up to the target sum, the function should return an empty array.
#
# Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.
#
# You can assume that there will be at most one pair of numbers summing up to the target sum.
#
# Sample Input
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10
# Sample Output
# [-1, 11] // the numbers could be in reverse order

# 用两个循环,可以得到任意两个数的和, 然后和目标值作比较, 一致的存起来,最后返回出来. 不需要额外的空间.所以时间复杂度和空间复杂度是:
# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    # Write your code here.
    result_array = []
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                result_array.append(firstNum)
                result_array.append(secondNum)

    print(result_array)
    return result_array


# dict采用了哈希表，最低能在 O(1)时间内完成搜索。
# 使用hash table 把数组存入hashtable, 空间花销是 O(n), 然后只需要遍历数组一遍, 对数组里的每个数判断hashtable里是否存在targetSum-x(常数时间)
# O(n) time | O(n) space
def twoNumberSumDict(array, targetSum):
    result_array = []
    dic = dict(zip(array, array))
    print(dic)
    for k in array:
        del dic[k]
        if (targetSum - k) in dic.keys():
            result_array.append(k)
            result_array.append(targetSum - k)
    print(result_array)
    return result_array


# 先把数组排序, 左边用一个指针指向最左边的最小的数, 右边用一个指针指向最右边的最大的数, 最小的加上最大的, 如果加起来的结果比目标结果小就把左边的下标往右移, 如果比目标结果大就把右边的下标往左移
# 不需要额外的空间. 好的数组排序只需要花O(log(n))的时间, 找到对应的值需要O(n)的时间, 所以总共的时间是O(n), 不需要额外的空间
# O(nlog(n)) time | O(1) space
def twoNumberSumBest(array, targetSum):
    result_array = []
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] < targetSum:
            left += 1
        elif array[left] + array[right] > targetSum:
            right -= 1
        elif array[left] + array[right] == targetSum:
            result_array.append(array[left])
            result_array.append(array[right])
            left += 1
            right -= 1
    print(result_array)
    return result_array


# array = [3, 5, -4, 8, 11, 1, -1, 6]
array = [4, 6, 1, -3]
targetSum = 3
# twoNumberSum(array, targetSum)
twoNumberSumBest(array, targetSum)
