from collections.abc import MutableMapping

class SuperDict(MutableMapping):
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.table = [(None,None)] * self.size

    def __getitem__(self, key):
        h = hash(key) % self.size
        k,v = self.table[h]
        if k is None:
            raise KeyError("Invalid key")
        while k != key:
            h = (h + 1) % self.size
            k,v = self.table[h]
            if k is None:
                raise KeyError("Invalid key")
        return v

    def __setitem__(self, key, value):
        if self.count == self.size - 1:
            raise ValueError("Exceeded size limit")
        h = hash(key) % self.size
        k, v = self.table[h]
        while k is not None:
            h = (h + 1) % self.size
            k,v = self.table[h]

        self.table[h] = (key,value)
        self.count += 1

    def __len__(self):
        return self.count

    def __delitem__(self, key):
        raise NotImplementedError("Not implemented")

    def __iter__(self):
        for k,v in self.table:
            if k is not None:
                yield k

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __ne__(self, other):
        return self.start != other.start or self.end != other.end

    def __hash__(self):
        #return hash (self.start) ^ hash(self.end)
        return hash ((self.start, self.end)) 



dictionary = SuperDict(100)
dictionary[1] = '1'
dictionary[2] = '5'

for i in dictionary.keys():
    print(i)
    print(dictionary[i])

print(dictionary.get(5))
print(dictionary[5])


