class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

s = Solution()
print(s.climbStairs(3))