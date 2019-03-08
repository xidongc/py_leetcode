##
# 128. Longest Consecutive Sequence
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
##


# hash O(n)
class Solution(object):

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


# O(nlgn) two pinters
class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        nums.append(-1)
        print(nums)
        max_num = 1
        p1 = 0
        p2 = 1
        while p2 <= len(nums) - 1:
            if nums[p2] == nums[p2-1]+1:
                p2 += 1
            else:
                max_num = max(max_num, p2 - p1)
                p1 = p2
                p2 += 1
        return max_num






