class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        start = 0
        end = len(nums)-1
        min_val = nums[0]

        # only have two elements, so ned start < end-1
        while start < end-1:
            mid = (end+start) // 2
            if nums[mid] > nums[start]:
                min_val = min(min_val, nums[start])
                start = mid+1
            elif nums[mid] < nums[start]:
                min_val = min(min_val, nums[mid])
                end = mid-1

        return min(min_val, nums[start], nums[end])
#lmf
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        target = nums[0]
        l,r = 0,len(nums)-1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                l = mid + 1
            else:
                r = mid
        return min(nums[l],nums[r])
