# https://leetcode.com/problems/jump-game/description/
# greedy alg, Accpeted, time complexity: O(n)

class Solution:

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 0:
            return True

        p1 = 0
        p2 = dis = nums[0]

        while dis < len(nums)-1:
            for i in range(p1, p2+1):
                dis = max(dis, nums[i]+i)
            if dis > p2:
                p1 = p2
                p2 = dis
            else:
                return False
        return True


# Solution in review
class Solution(object):
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[0] = True
        current_position = 0

        for i, num in enumerate(nums):
            if dp[i] is True:
                if i + nums[i] > current_position:
                    for t in range(nums[i] + 1):
                        if 0 <= i + t < len(nums):
                            dp[i + t] = True
                            current_position = max(current_position, i + t)

        return dp[len(nums) - 1]
