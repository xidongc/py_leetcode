class Solution:

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False

        sig = True
        while sig is True and num != 1:
            sig = False
            for x in [2,3,5]:
                if num % x == 0:
                    sig = True
                    num /= x

        if num == 1:
            return True
        else:
            return False


s = Solution()
print(s.isUgly(14))