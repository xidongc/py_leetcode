#
# Complete the 'rearrange' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY elements as parameter.

# 按照二进制的1的树目排序。如果有一样的1的数量，那就按照值来排
import collections
def rearrange(elements):
    # Write your code here
    res = []
    map = collections.defaultdict(list)
    for element in elements:
        biRes = bin(element)[2:]
        if element not in map[biRes.count('1')]:
            map[biRes.count('1')].append(element)
    for key in sorted(map):
        for val in sorted(map[key]):
            res.append(val)
    return res
# list.sort(key = lambda n: (bin(n).count('1'),n))
print(rearrange([0,1,2,3,3,3,3]))

