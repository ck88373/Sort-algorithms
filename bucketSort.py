import time
import random


def bucketSort(nums):
    buckets = [0] * (max(nums) - min(nums) + 1)
    for i in nums:
        buckets[i - min(nums)] += 1
    re = []
    for j in range(len(buckets)):
        if buckets[j] != 0:
            re += [j + min(nums)] * buckets[j]
    return re


if __name__ == '__main__':
    start = time.time()
    a = list(range(10000))
    # a = [4, 6, 7]
    random.shuffle(a)
    print(a)
    print(bucketSort(a))
    print("Time cost: %.5fs" % (time.time() - start))
