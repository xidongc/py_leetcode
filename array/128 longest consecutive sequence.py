class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        numSet = set()
        res = 1
        while nums:
            num = nums.pop(0)
            prev = num - 1
            next = num + 1
            while prev in nums:
                nums.remove(prev)
                prev -= 1
            while next in nums:
                nums.remove(next)
                next += 1
            res = max(res, next - prev - 1)
        return res

s = Solution()
s.longestConsecutive([100, 4, 200, 1, 3, 2])