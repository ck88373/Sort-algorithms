import time
import random


def radixSort1(array):
    """method 1, from internet"""
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            bucket[num].append(array[i])
        array.clear()
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    return array


def radixSort2(nums):
    """
    my method
    nums: int numbers
    """
    d = len(str(max(nums)))
    for i in range(0, d):
        buckets = [[] for j in range(10)]
        for n in nums:
            buckets[(n // 10 ** i) % 10].append(n)
        nums = [k for b in buckets for k in b]
    return nums


if __name__ == '__main__':
    start = time.time()
    a = list(range(100000))
    # a = [4, 6, 7,7,3,4,2,1,1]
    random.shuffle(a)
    print(a)
    print(radixSort2(a))
    print("Time cost: %.5fs" % (time.time() - start))
