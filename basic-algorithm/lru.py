import collections

# pop and add to keep priority
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



# LRU 2

from collections import OrderedDict
import hashlib


class Cache(object):

    def __init__(self, max_lru_size=10):
        self.max_lru_size = max_lru_size
        self.lru_cache = OrderedDict()

    def find(self, addr):
        if addr in self.lru_cache:
            data = self.lru_cache[addr]
            self.lru_cache.pop(addr)
            self.lru_cache[addr] = data
            return data
        else:
            data = self.fetch_from_disk(addr)
            if len(self.lru_cache) >= self.max_lru_size:
                self.lru_cache.popitem(last=False)
            self.lru_cache[addr] = data
            return data

    def fetch_from_disk(self, addr):
        return hashlib.sha1(bytes(addr))

c = Cache()
for i in range(100):
    c.find(i)
c.find(95)

print(c.lru_cache)