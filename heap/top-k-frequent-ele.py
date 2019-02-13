from collections import Counter
import heapq


class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        li = []
        if not nums:
            return -1

        dic = Counter(nums)
        l = [(-val, key) for key, val in dic.items()]
        heapq.heapify(l)
        for _ in range(k):
            li.append(heapq.heappop(l))
        return [y for (x, y) in li[0:k]]

#         data, res, pq = {}, [], []
#         for i in nums:
#             data[i] = data[i] + 1 if i in data else 1
#         for key in data:
#             heapq.heappush(pq, (-data[key], key))
#         for i in xrange(k):
#             res.append(heapq.heappop(pq)[1])
#         return res

# sol2

class Dict(tuple):

    def __lt__(self, other):
        (k1, v1) = self
        (k2, v2) = other
        return v1 > v2


class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        li = []
        if not nums:
            return -1

        dic = Counter(nums)
        print(dic)
        l = [Dict((key, val)) for key, val in dic.items()]
        print(l)
        heapq.heapify(l)
        for _ in range(k):
            print(heapq.heappop(l))

# lmf ->collections.Counter().most_common()
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [k for k,v in collections.Counter(nums).most_common(k)]
s = Solution()
nums = [2,3,4,1,4,0,4,-1,-2,-1]
k = 2

print(s.topKFrequent(nums, k))