class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        return self.helper(nums, 0, len(nums)-1)
    def helper(self,nums,start,end):
        if start == end or start + 1 == end:
            return start if nums[start] > nums[end] else end
        mid = (start + end) // 2
        # mid is local minimum
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return mid
        # descending case
        elif nums[mid - 1] > nums[mid] and nums[mid] > nums[mid + 1]:
            return self.helper(nums, start, mid - 1)
        # ascending case
        else:
            return self.helper(nums, mid + 1, end)