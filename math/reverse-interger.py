class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x > 2 ** 31 - 1 or x < -(2 ** 31):
            return 0
        positive = True
        if x < 0:
            x = abs(x)
            positive = False
        ret = []
        num = 0
        while x // 10 != 0:
            ret.append(x % 10)
            x //= 10
        ret.append(x)
        for i, x in enumerate(range(len(ret)-1, -1, -1)):
            num += (10**x) * ret[i]
        if positive:
            if num > 2 ** 31 - 1:
                return 0
            return num
        else:
            if num > (2 ** 31):
                return 0
            return -num
