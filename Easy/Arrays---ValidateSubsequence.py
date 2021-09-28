# Validate Subsequence
# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
#
# A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array.
# For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4].
# Note that a single number in an array and the array itself are both valid subsequences of the array.
# 字串里所有的字符都出现在母串里,且出现的顺序也一致,不需要相邻.
# Sample Input
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# Sample Output
# true

# 两个指针
# O(n) Time | O(1) Space
def isValidSubsequenceThird(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if value == sequence[seqIdx]:
            seqIdx += 1
    return seqIdx == len(sequence)


# 两个指针
# O(n) Time | O(1) Space
def isValidSubsequenceThird(array, sequence):
    seqInx = 0
    arrInx = 0
    while arrInx < len(array) and seqInx < len(sequence):
        if array[arrInx] == sequence[seqInx]:
            seqInx += 1
        arrInx += 1
    return seqInx == len(sequence)


# 两个指针, 一个在subsequence, 从头到尾走一遍, 另外一个指向array, 找到了对应的字符就把第一个指针指到下一个字符. 两个循环
# O(n) Time | O(1) Space
def isValidSubsequence(array, sequence):
    # Write your code here.
    if len(sequence) == 1:
        if sequence[0] in array:
            return True
        else:
            return False
    elif array == sequence:
        return True
    elif len(sequence) > len(array):
        return False
    else:
        j = 0
        print(len(sequence) - 1)
        for numberInSequence in range(len(sequence)):
            print(numberInSequence)
            foundInArray = False
            for numberInArray in range(j, len(array)):
                j += 1
                if sequence[numberInSequence] == array[numberInArray]:
                    foundInArray = True
                    break
            if not foundInArray:
                return False
        return True


# O(n) Time | O(1) Space
def isValidSubsequenceSecond(array, sequence):
    if len(sequence) > len(array):
        return False
    while len(sequence) != 0:
        x = sequence.pop()
        if len(array) != 0:
            y = array.pop()
        else:
            return False
        while x != y:
            if len(array) == 0:
                return False
            else:
                y = array.pop()
    return True


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, -1]
print(isValidSubsequence(array, sequence))
print(isValidSubsequenceSecond(array, sequence))
