# # Design
# VMware
# class MyHashMap(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.dict = [-1] * 1000000
#
#     def put(self, key, value):
#         """
#         value will always be non-negative.
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         self.dict[key] = value
#
#     def get(self, key):
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         :type key: int
#         :rtype: int
#         """
#         return self.dict[key]
#
#     def remove(self, key):
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         :type key: int
#         :rtype: void
#         """
#         self.dict[key] = -1


class MyHashMap(object):

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key, value):
        if key in self.keys:
            self.values[self.keys.index(key)] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key):
        if key in self.keys:
            return self.values[self.keys.index(key)]
        else:
            return -1

    def remove(self, key):
        if key in self.keys:
            del self.values[self.keys.index(key)]
            del self.keys[self.keys.index(key)]
        # Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)