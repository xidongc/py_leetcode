class Solution(object):
    def peakIndexInMountainArray(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] > nums[right] else right
s = Solution()
s.peakIndexInMountainArray([0,1,0])
# or
# return nums.index(max(nums))