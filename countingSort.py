import time
import random

def countingSort(nums):
    length = len(nums)
    C = [0] * (max(nums) + 1)
    B = [0] * length
    for i in nums:  # 计数
        C[i] += 1
    for i in range(1, len(C)):  # 转成小于等于的计数，即累加
        C[i] += C[i - 1]
    for i in nums:  # 输出序列
        B[C[i] - 1] = i
        C[i] -= 1
    return B


if __name__ == '__main__':
    start = time.time()
    a = list(range(100000))
    # a = [4,6,7,8,9]
    random.shuffle(a)
    print(a)
    print(countingSort(a))
    print("Time cost: %.5fs" % (time.time() - start))
