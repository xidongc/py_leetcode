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
