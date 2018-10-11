def selectionSort(arr):
    for i in range(len(arr)):
        minindex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        if i != minindex:
            arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr


if __name__ == "__main__":
    import random
    import time
    start = time.time()
    a = list(range(10000))
    random.shuffle(a)
    print(a)
    print(selectionSort(a))
    print("Time cost: %.5fs" % (time.time() - start))
