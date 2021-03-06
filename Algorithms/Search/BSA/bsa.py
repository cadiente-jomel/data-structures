class BSA:
    def __init__(self):
        self.arr = [21, 25, 31, 53, 55]
        self.length = len(self.arr) - 1

    def linear_approach(self, target) -> int:
        for index, el in enumerate(self.arr):
            if el == target:
                return index
        return -1

    def iterative_approach(self, target):
        left_index = 0
        right_index = len(self.arr) - 1

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            mid_number = self.arr[mid_index]

            if mid_number == target:
                return mid_index

            if mid_number > target:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1

        return -1

    def recursive_approach(self, target, left_index, right_index):
        if right_index < left_index:
            return -1

        mid_index = (left_index + right_index) // 2
        mid_number = self.arr[mid_index]

        if target == mid_number:
            return mid_index

        if mid_number < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

        return self.recursive_approach(target, left_index, right_index)


if __name__ == '__main__':
    s = BSA()
    print(f'number found at index {s.linear_approach(16)} linearly')

    print(f'number found at index {s.iterative_approach(16)} iterative')

    print(
        f'number found at index {s.recursive_approach(55, 0, s.length)} recursively')
