#swap head and tail
#edge case 2222


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # length = len(nums)
        # i, j = 0,0
        # while j < length:
        #     if nums[j] == val:
        #         while nums[j] == val and j < length:
        #             j += 1
        #         nums[i] = nums[j]
        #     i += 1
        #     j += 1
        if not nums:
            return 0
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start],nums[end],end = nums[end],nums[start],end - 1
            else:
                start += 1
        return start
