def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # print(arr)
    return arr


if __name__ == "__main__":
    import random
    import time
    start = time.time()
    a = list(range(10000))
    random.shuffle(a)
    print(a)
    print(bubbleSort(a))
    print("Time cost: %.5fs" % (time.time() - start))

