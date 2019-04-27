class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointers AC
        if len(nums) <= 1:
            return len(nums)

        i, j = 0, 1

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return i + 1
