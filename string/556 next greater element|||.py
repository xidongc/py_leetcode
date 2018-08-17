class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = list(map(int, str(n)))
        length = len(num)
        if length == 1:
            return -1
        pos = 0
        for i in range(length - 1, 0, -1):
            if num[i] > num[i - 1]:
                pos = i
                break
        if pos == 0:
            return -1
        # if pos == length-1:
        #     num[-1], num[-2] = num[-2],num[-1]
        #     return int(''.join(num))
        for i in range(length - 1, pos - 1, -1):
            if num[i] > num[pos - 1]:
                num[i], num[pos - 1] = num[pos - 1], num[i]
                break
        # return num[:pos] + num[pos:].sort()
        # 交换完之后就不用再交换了呀，直接用排序了。这里换成num.sort()是不行的因为returnnone
        res = int(''.join(map(str, num[:pos] + sorted(num[pos:]))))
        return -1 if res > 2 ** 31 else res
s = Solution()
print(s.nextGreaterElement(125265431))