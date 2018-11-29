import collections
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.freqCache = collections.defaultdict(collections.OrderedDict)
        self.leastFrequency = 1
        self.cache = {}
    def update(self,key,newValue = None):
        value,freq = self.cache[key]
        if newValue != None:
            value = newValue
        self.freqCache[freq].pop(key)
        if len(self.freqCache[self.leastFrequency]) == 0:
            self.leastFrequency += 1
        self.freqCache[freq+1][key] = (value,freq+1)
        self.cache[key] = (value,freq+1)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            self.update(key)
            return self.cache[key][0]
        except KeyError:
            return -1
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.update(key,value)
        else:
            self.cache[key] = (value,1)
            self.freqCache[1][key] = (value,1)
            if self.capacity == 0:
                k,v = self.freqCache[self.leastFrequency].popitem(last = False)
                del self.cache[k]
            else:
                self.capacity -= 1
            self.leastFrequency = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)