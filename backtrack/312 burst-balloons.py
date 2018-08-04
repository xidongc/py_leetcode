# Divide and Conquer
# DP
import collections
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = collections.defaultdict(int)
        length = len(nums)
        map[0] = map[length + 1] = 1
        for i in range(1,length + 1):
            map[i] = nums[i-1]
        memo = [[0 for _ in range(length + 2)] for _ in range(length + 2)]
        return self.burst(memo, map, 0, length + 1)

    def burst(self, memo, map,left,right):
        if left + 1 == right:
            return 0
        if memo[left][right] > 0:
            return memo[left][right]
        ans = 0
        for i in range(left + 1, right):
            ans = max(ans, map[left]*map[i]*map[right] + self.burst(memo,map,left,i) + self.burst(memo,map,i,right))
        memo[left][right] = ans
        return ans
    # 不要写了