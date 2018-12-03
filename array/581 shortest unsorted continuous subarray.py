# 845 longest mountain
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    #     TLE
    #     if not nums or len(nums) == 1:
    #         return 0
    #     start = -1
    #     res = 0
    #     for i in range(1,len(nums)):
    #         if nums[i] < nums[i-1]:
    #             j = i
    #             while j > 0 and nums[j] < nums[j-1]:
    #                 self.swap(nums,j,j-1)
    #                 j -= 1
    #             if start == -1 or start > j:
    #                 start = j
    #             res = i - start + 1
    #     return res
    # def swap(self, nums,i,j):
    #     tmp = nums[i]
    #     nums[i] = nums[j]
    #     nums[j] = tmp
    #
        if not nums or len(nums) == 1:
            return 0
        i,j = 0,-1
        largest,smallest = -(2**32)+1,2**32-1
        left,right = 0,len(nums)-1
        while right >= 0:
            largest = max(largest,nums[left])
            if nums[left] != largest:
                j = left
            smallest = min(smallest,nums[right])
            if nums[right] != smallest:
                i = right
            left += 1
            right -= 1
        return j - i + 1

s = Solution()
s.findUnsortedSubarray([2,6,4,8,10,9,15])