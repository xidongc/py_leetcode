from collections import OrderedDict

a = dict()
a['e'] = 1
a['a'] = 2
a.update({'banana': 3, 'apple':4, 'pear': 1, 'orange': 2})

a = OrderedDict(sorted(a.items(), key=lambda x:x[1]))
print(a)
d = a.popitem(0)
print(d[1])
print("a" < "aa")