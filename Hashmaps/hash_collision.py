class HashTable:
    """
        Hash table chaining
    """

    def __init__(self):
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        # check if the key already existed
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        # append the new key-value pair
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


if __name__ == '__main__':
    hm = HashTable()
    hm['march 6'] = 130
    hm['march 6'] = 178
    hm['march 8'] = 67
    hm['march 9'] = 459
    hm['march 17'] = 50
    hm['march 17'] = 51
    del hm['march 6']
    del hm['march 17']
    hm['march 6'] = 69
    hm['march 17'] = 70
    data = hm['march 17']
    data1 = hm['march 6']
    print(data)
    print(data1)
    print(hm.arr)
