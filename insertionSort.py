def insertionSort(arr):
    for i in range(1, len(arr)):
        pre_index = i - 1
        current = arr[i]
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr


if __name__ == "__main__":
    import random
    import time
    # import numpy

    start = time.time()
    a = list(range(10000))
    random.shuffle(a)
    print(a)
    print(insertionSort(a))
    print("Time cost: %.5fs" % (time.time() - start))

