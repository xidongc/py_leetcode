# 300, https://leetcode.com/problems/longest-increasing-subsequence/description/


# Sol-1: normal dp with time complexity O(n^2)
class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        dp = [1 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)


# Sol-2: tricky way inspired from:
# https://leetcode.com/problems/russian-doll-envelopes/discuss/157840/Concise-8-line-Python-O(nlogn)-solution-(easy-to-understand)
# time complexity: O(n*log(n))
# (1) if x is larger than all tails, append it, increase the size by 1
# (2) if tails[i-1] < x <= tails[i], update tails[i]

from bisect import bisect_left


class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return 0

        tail = [nums[0]]
        for num in nums[1:]:
            pos = bisect_left(tail, num)
            if pos == len(tail):
                tail.append(num)
            else:
                tail[pos] = num

        return len(tail)

# of course, bisect_left is just the bisect, and we could write it via start < end-1 with mid = (end-start)/2 + start

