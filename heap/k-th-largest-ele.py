import heapq

# cxd
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

# lmf
# quick-select
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def findKth(nums,k,start,end):
            pivot = nums[start]
            left,right = start,end
            while left < right:
                while nums[right] >= pivot and left < right:
                    right -= 1
                while nums[left] <= pivot and left < right:
                    left += 1
                nums[left],nums[right] = nums[right],nums[left]
            nums[start],nums[right] = nums[right],nums[start]
            if k == right:
                return pivot
            elif k < right:
                return findKth(nums,k,start,right-1)
            return findKth(nums,k,right+1,end)
        return findKth(nums,len(nums)-k,0,len(nums)-1)

s = Solution()
nums = [1,3,8,9,4,5,7]
print(s.findKthLargest(nums, 2))
