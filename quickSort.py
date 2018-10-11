def quickSort1(num, l, r):
    """测试时此性能差"""
    if l >= r:  # 如果只有一个数字时，结束递归
        return
    flag = l
    for i in range(l + 1, r + 1):  # 默认以第一个数字作为基准数，从第二个数开始比较，生成索引时要注意右部的值
        if num[flag] > num[i]:
            num.insert(flag, num.pop(i))
            flag += 1
    quickSort1(num, l, flag - 1)  # 将基准数前后部分分别递归排序
    quickSort1(num, flag + 1, r)


# 一行版本
quickSort2 = lambda array: array if len(array) <= 1 else quickSort2(
    [item for item in array[1:] if item <= array[0]]) + [array[0]] + quickSort2(
    [item for item in array[1:] if item > array[0]])


# 百度百科
def quickSort3(array):
    """easy to understand, out-place"""
    if len(array) < 2:
        return array
    else:
        baseValue = array[0]  # 选择基准值
        less = [m for m in array[1:] if m <= baseValue]
        greater = [n for n in array[1:] if n > baseValue]
    return quickSort3(less) + [baseValue] + quickSort3(greater)


def quickSort4(list, start, end):
    if start > end:
        return
    i, j = start, end
    flag = list[start]
    while True:
        while j > i and list[j] >= flag:  # 先从右往左找
            j = j - 1
        while i < j and list[i] <= flag:  # 再从左往右找
            i += 1
        if i < j:
            list[i], list[j] = list[j], list[i]
        elif i == j:  # 当左右相等时第一次递归结束
            list[start], list[i] = list[i], list[start]
            break
    quickSort4(list, start, i - 1)
    quickSort4(list, i + 1, end)


def quickSort5(ql, start, end):
    """in-place"""
    if start > end:
        return
    mark = ql[start]
    i, j = start, end
    while i < j:
        while i < j and ql[j] >= mark:
            j -= 1
        while i < j and ql[i] <= mark:
            i += 1
        ql[i], ql[j] = ql[j], ql[i]

    ql[start], ql[i] = ql[i], ql[start]
    quickSort5(ql, start, i - 1)
    quickSort5(ql, i + 1, end)


def quickSort6(nums, start, end):
    """my method, in-place"""
    if start >= end:
        return
    l, r = start, end
    flag = nums[start]
    while l < r:
        while l < r and nums[r] > flag:
            r -= 1
        while l < r and nums[l] <= flag:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    nums[l], nums[start] = nums[start], nums[l]
    quickSort6(nums, start, l - 1)
    quickSort6(nums, l + 1, end)


# ==========================just for test=======================================#
def testquick(nums):
    if len(nums) < 2:
        return nums
    flag = nums[0]
    less = [i for i in nums[1:] if i <= flag]
    large = [i for i in nums[1:] if i > flag]
    return testquick(less) + [flag] + testquick(large)


def testquick_in(nums, start, end):
    if start >= end:
        return
    l, r = start, end
    flag = nums[l]
    while l < r:
        while l < r and nums[r] >= flag:
            r -= 1
        while l < r and nums[l] <= flag:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    nums[start], nums[l] = nums[l], nums[start]
    testquick_in(nums, start, l - 1)
    testquick_in(nums, l + 1, end)


# ====================================end=======================================#

if __name__ == "__main__":
    import random
    import time

    start = time.time()
    a = list(range(100000))
    # a = [2, 3, 4, 4, 4, 5, 34, 3, 4, 1, 6]
    random.shuffle(a)
    # print(a)
    # quickSort1(a, 0, 99999)
    # print(a)
    print(a)
    quickSort6(a, 0, 10)
    print(a)
    # print(a)
    # testquick_in(a, 0, len(a) - 1)
    # print(a)
    print("Time cost: %.5fs" % (time.time() - start))
