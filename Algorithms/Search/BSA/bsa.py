class BSA:

    def __init__(self):
        self.arr = [21, 25, 31, 53, 55]

    def linear_approach(self, target : int):
        for i, el in enumerate(self.arr):
            if el == target:
                return f'Matched found at index {i}'
        return 0

    def iterative_approach(self, target):
        pass


    def recursive_approach(self, target):
        pass



if __name__ == '__main__':
    s = BSA()
    print(s.linear_approach(53))

