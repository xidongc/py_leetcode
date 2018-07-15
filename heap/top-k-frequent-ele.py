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


s = Solution()
nums = [2,3,4,1,4,0,4,-1,-2,-1]
k = 2

print(s.topKFrequent(nums, k))