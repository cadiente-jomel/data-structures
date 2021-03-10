def insertion_sort(arr : list) -> list:
    arr_len = len(arr)

    for i in range(1, arr_len):
        while arr[i - 1] > arr[i] and i > 0:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1

    return arr 
 
if __name__ == '__main__':
    num_list = [-2, 124, 421, 12, 5, 20, 2, 1]
    res = insertion_sort(num_list)
    print(res)