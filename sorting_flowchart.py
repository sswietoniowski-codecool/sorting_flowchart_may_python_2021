def bubble_sort():
    array = [1, 2, 56, 32, 51, 2, 8, 92, 15]

    print(array)

    n = len(array)
    i = 0
    j = 0

    while True:
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
        j += 1

        if j < n - i - 1:
            continue
        else:
            j = 0
            i += 1
            if j < n - i - 1:
                continue
            else:
                break

    print(array)


def binary_search(value):
    array = [1, 2, 4, 7, 11, 22, 38, 42, 43]
    start = 0
    end = len(array)

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == value:
            return mid
        else:
            if array[mid] > value:
                end = mid - 1
            else:
                start = mid + 1

    return -1


def main():
    bubble_sort()
    print(binary_search(7))
    print(binary_search(8))


if __name__ == "__main__":
    main()
