import heapq


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k <= n//2:
            l = list(map(lambda x: -x, nums))
            heapq.heapify(l)
            for _ in range(k-1):
                heapq.heappop(l)
            return -l[0]
        else:
            heapq.heapify(nums)
            for _ in range(n-k):
                heapq.heappop(nums)
            return nums[0]

s = Solution()
nums = [1,2,3,4,5]
print(s.findKthLargest(nums, 3))
