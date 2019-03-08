class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        digitDict = {}
        if not numerator or not denominator:
            return 0
        neg = False
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            neg = True
        if numerator % denominator == 0:
            return str(numerator/denominator)
        else:
            numerator = abs(numerator)
            denominator = abs(denominator)
            res = "-" if neg else ""
            res += str(numerator // denominator)
            res += "."
            numerator = numerator % denominator
            i = len(res)
            while numerator:
                if numerator not in digitDict:
                    digitDict[numerator] = i
                else:
                    i = digitDict[numerator]
                    res = res[:i] + "(" + res[i:] + ")"
                    return res
                numerator = 10 * numerator
                res += str(numerator // denominator)
                numerator = numerator % denominator
                i += 1
            return res
        #     curRemain = numerator - integer * denominator
        #     while curRemain not in digitDict:
        #         curNumerator = 10 * curRemain
        #         digitDict[curRemain] = 1
        #         res += str(curRemain)
        #         temp = curRemain
        #         curRemain = curNumerator - curRemain * denominator
        #         curNumerator = temp
        #         curRemain = curNumerator // denominator
        # res += ")"
        # return res
s = Solution()
print(s.fractionToDecimal(1,2))
print(s.fractionToDecimal(1,7))



# 原来除法不能得出无限不循环小数啊
# 1/2 = "0.5"
# 2/3 = "0.(6)"
# 1/7 = "0.(142857)" 10//7 = 1 10 - 1*7 = 3 3*10 // 7 = 4 3*10 - 4*7 = 2
# 重复numerator就是停止之时。
