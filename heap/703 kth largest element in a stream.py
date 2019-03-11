from heapq import *

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = []
        for num in nums:
            heappush(self.heap, num)
        while len(self.heap) > k:
            heappop(self.heap)
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)