import collections


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()


    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            # The pairs are returned in LIFO order if last is true or FIFO order if false.
            # if key not exists, check current length
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

c = LRUCache(5)

for i in range(5,10):
    c.set(i,10*i)


print(c.cache, c.cache.keys())

c.get(5)
c.get(7)

print(c.cache, c.cache.keys())

c.set(10,100)
print(c.cache, c.cache.keys())

c.set(9,44)
print(c.cache, c.cache.keys())