def merge_sort(arr: list):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a: list, b: list, arr: list) -> list:
    a_len = len(a)
    b_len = len(b)
    i = j = k = 0

    while i < a_len and j < b_len:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < a_len:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < b_len:
        arr[k] = b[j]
        j += 1
        k += 1

    return arr


if __name__ == '__main__':

    test_cases = [
        [2, 5, 4, 7, 6, 55, 8, 1, 10, 3],
        [],
        [3],
        [2, 1],
        [4, 5, 2, 10, 9, 22, 3]
    ]
    for arr in test_cases:
        merge_sort(arr)
        print(arr)
