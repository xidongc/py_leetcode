# O(LOGN)
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start,end = 0,len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            mid -= 1 if mid % 2 == 1 else 0
            if nums[mid] == nums[mid + 1]:
                start = mid + 2
            else:
                end = mid
        return nums[start]