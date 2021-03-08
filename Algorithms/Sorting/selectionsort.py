def selection_sort(arr: list) -> list:
    min_val = min_idx = 0
    arr_len = len(arr)

    for i in range(arr_len):
        min_val = arr[i]
        min_idx = i
        for j in range(i + 1, arr_len):
            if arr[j] < min_val:
                min_val = arr[j]
                min_idx = j
        
        if min_val < arr[i]:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

if __name__ == '__main__':
    num_list = [7, 8, 69, 5, 1, 4, 9, 0, 2, -1]
    sorted_list = selection_sort(num_list)
    print(sorted_list)
