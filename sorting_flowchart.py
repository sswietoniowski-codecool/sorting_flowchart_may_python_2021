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


def main():
    bubble_sort()


if __name__ == "__main__":
    main()
