class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
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

    # second way to look for only increasing seq
    def longest_consecutive_2(self, num) -> int:
        hashset = set(num)
        max_length = 1
        for n in num:
            if n - 1 not in hashset:
                length = 1
                curr = n + 1
                while curr in hashset:
                    curr = curr + 1
                    length += 1
                max_length = max(max_length, length)
        return max_length
