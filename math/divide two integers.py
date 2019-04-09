class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sig = 1 if dividend * divisor >= 0 else -1
        ret = pow(2, 31) - 1

        start = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        end = dividend

        while start < end - 1:
            mid = start + (end - start) // 2
            if mid * divisor > dividend:
                end = mid
            elif mid * divisor == dividend:
                return mid * sig if -pow(2, 31) <= mid * sig <= pow(2, 31) - 1 else ret
            else:
                start = mid

        if end * divisor <= dividend and -pow(2, 31) <= end * sig <= pow(2, 31) - 1:
            return sig * end
        elif -pow(2, 31) <= start * sig <= pow(2, 31) - 1:
            return sig * start
        return ret
