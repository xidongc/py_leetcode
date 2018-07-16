class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n //= 3

        return n == 1
