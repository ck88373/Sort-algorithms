def shellSort(arr):
    gaps = [1]
    while True:
        h = gaps[-1] * 3 + 1
        if h >= len(arr):
            break
        gaps.append(h)

    while gaps:
        gap = gaps.pop()
        for i in range(gap, len(arr)):
            current = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > current:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = current
    return arr


if __name__ == "__main__":
    import random
    import time

    start = time.time()
    a = list(range(100000))
    random.shuffle(a)
    print(a)
    print(shellSort(a))
    print("Time cost: %.5fs" % (time.time() - start))

