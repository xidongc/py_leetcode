class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)  # remove duplicate
        maxv = 0
        while nums:
            x = nums.pop()
            before, after = x - 1, x + 1
            length = 1
            while before in nums:
                nums.remove(before)
                before -= 1
                length += 1
            while after in nums:
                nums.remove(after)
                after += 1
                length += 1
            maxv = max(maxv, length)
        
        return maxv
        
