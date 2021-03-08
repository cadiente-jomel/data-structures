def bubble_sort(number_list: list) -> list:
    num_length = len(number_list)

    for i in range(num_length):
        for j in range(0, num_length - i - 1):
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j +
                                            1] = number_list[j + 1], number_list[j]
    return number_list


if __name__ == '__main__':
    num_list = [59, 1, 51, 2, 31, 23, 0]
    res = bubble_sort(num_list)
    print(res)
