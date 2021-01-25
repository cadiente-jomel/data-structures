class HashMaps:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, val):
        h = 0
        for char in val:
            h += ord(char)
        return h % self.MAX

    # if you want to add value just like how you add new key value pair in dict
    # override __setitem__ this is a built-in operator

    # def add(self, key, val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    # if you want to get value just like how you get new value in dict
    # override __getitem__ this is a built-in operator
    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == '__main__':
    hm = HashMaps()
    hm['march 6'] = 130
    hm['march 7'] = 137
    hm['march 8'] = 138
    get_val = hm['march 7']
    print(hm.arr)
    print(get_val)
    del hm['march 7']
    print(hm.arr)
