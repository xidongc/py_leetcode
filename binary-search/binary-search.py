class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1

        start = 0
        end = len(nums)-1

        while start < end -1:
            mid = (end - start)/2 + start
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                return mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1
