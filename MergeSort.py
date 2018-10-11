def mergeSort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while left:
        res.append(left.pop(0))
    while right:
        res.append(right.pop(0))
    return res


if __name__ == "__main__":
    import random
    import time

    start = time.time()
    a = list(range(100000))
    random.shuffle(a)
    print(a)
    print(mergeSort(a))
    print("Time cost: %.5fs" % (time.time() - start))
