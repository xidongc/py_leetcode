import collections
# 大数据扩展lru-k
# LRU-K需要多维护一个队列，用于记录所有缓存数据被访问的历史。
# 只有当数据的访问次数达到K次的时候，才将数据放入缓存。
# 当需要淘汰数据时，LRU-K会淘汰第K次访问时间距当前时间最大的数据
# 1. 数据第一次被访问，加入到访问历史列表；
#
# 2. 如果数据在访问历史列表里后没有达到K次访问，则按照一定规则（FIFO，LRU）淘汰；
#
# 3. 当访问历史队列中的数据访问次数达到K次后，将数据索引从历史队列删除，将数据移到缓存队列中，并缓存此数据，缓存队列重新按照时间排序；
#
# 4. 缓存数据队列中被再次访问后，重新排序；
#
# 5. 需要淘汰数据时，淘汰缓存队列中排在末尾的数据，即：淘汰“倒数第K次访问离现在最久”的数据。
# pop and add to keep priority


class LRUCache(object):

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
