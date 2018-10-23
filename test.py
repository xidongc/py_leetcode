# LRU

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

