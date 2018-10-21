class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        #         这种操作都是浅拷贝吗
        string = string.strip()
        if not string:
            return 0
        i = 0
        flag = True
        if string[i] in ['+', '-']:
            flag = False if string[i] == '-' else True
            i += 1
        res = 0
        while i < len(string) and string[i].isdigit():
            res = res * 10 + int(string[i])
            i += 1
        if res:
            res = (-res) if not flag else (+res)
        res = max(min(2 ** 31 - 1, res), -2 ** 31)
        return res
