class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = False
        res = 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            neg = True
        dividend, divisor = abs(dividend),abs(divisor)
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if neg:
            res = -res
        return min(max(-2 **31,res),2 ** 31 - 1)

s = Solution()
print(s.divide(6,3))
print(s.divide(10,3))



