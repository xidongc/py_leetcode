class Solution:

    def pow(self, base, power):
        if power == 0:
            return 1
        if power == 1:
            return base
        if power == -1:
            return 1/base
        if power % 2 == 0:
            res = self.pow(base, power / 2)
            return res * res
        else:
            return base * self.pow(base, power - 1)

    def isPowerOfThree(self, n) -> bool:
        if n == 0:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n //= 3

        return n == 1

    def isPowerOfTwo(self, num: int) -> bool:
        # standard way refer above isPowerOfThree
        # (num & (num - 1)) == 0 means num is power of two eg: 1000 && 0111 == 0
        return num > 0 and (num & (num - 1)) == 0

    def isPowerOfFour(self, num):
        # (num & (num - 1)) == 0 means num is power of two eg: 1000 && 0111 == 0
        # 0xaaaaaaaa = 10101010101010101010101010101010 (偶数位为1，奇数位为0）
        return num > 0 and (num & (num - 1)) == 0 and (num & 0xaaaaaaaa) == 0
