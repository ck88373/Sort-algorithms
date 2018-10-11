# -*- coding:utf-8 -*-
import time
import random


def heapSort1(input_list):
    """
    函数说明:堆排序（升序）
    Parameters:
        input_list - 待排序列表
    Returns:
        input_list - 升序排序好的列表
    """

    def HeapAdjust(input_list, parent, length):
        """
        函数说明:堆调整，调整为最大堆
        Parameters:
            input_list - 待排序列表
            parent - 堆的父结点
            length - 数组长度
        Returns:
            无
        """
        temp = input_list[parent]
        child = 2 * parent + 1
        while child < length:
            if child + 1 < length and input_list[child] < input_list[child + 1]:
                child += 1
            if temp >= input_list[child]:
                break
            input_list[parent] = input_list[child]
            parent = child
            child = 2 * parent + 1
        input_list[parent] = temp

    length = len(input_list)
    if length < 2:
        return

    for i in range(0, length // 2)[::-1]:
        HeapAdjust(input_list, i, length)

    for j in range(1, length)[::-1]:
        input_list[j], input_list[0] = input_list[0], input_list[j]
        HeapAdjust(input_list, 0, j)
        # print('第%d趟排序:' % (length - j), end='')
        # print(input_list)


# 第二种实现
def heapSort2(nums):
    """my method, in place"""

    def heap_adjust(parent, length):
        """adjust a heap"""
        child = parent * 2 + 1
        temp = nums[parent]
        while child < length:
            if child + 1 < length and nums[child + 1] > nums[child]:
                child += 1
            if nums[child] <= temp:
                break
            nums[parent] = nums[child]
            parent = child
            child = 2 * parent + 1
        nums[parent] = temp  # insert temp here

    length = len(nums)
    # start = time.time()
    for i in range(length // 2 - 1, -1, -1):  # initial to max heap
        heap_adjust(i, length)
    # print("Initial Time cost: %.5fs" % (time.time() - start))

    # start = time.time()
    for i in range(length, 1, -1):  # current length
        heap_adjust(0, i)  # adjust 0 index number to the right place
        nums[0], nums[i - 1] = nums[i - 1], nums[0]  # shift max number (index 0) to index i
    # print("2nd Time cost: %.5fs" % (time.time() - start))


if __name__ == '__main__':
    start = time.time()
    a = list(range(100000))
    # a = [4,6,7]
    random.shuffle(a)
    print(a)
    heapSort2(a)
    print(a)
    print("Time cost: %.5fs" % (time.time() - start))
