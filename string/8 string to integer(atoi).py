class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        #         这种操作都是浅拷贝吗
        res = 0
        s = s.strip()
        label = '+'
        for i in range(len(s)):
            if not s[i].isdigit():
                if i == 0 and s[i] in ['-','+']:
                    label = s[i]
                    continue
                else:
                    # 比如如果前面是数字后面开始出现字母，这时候就return出去了
                    if label == '-':
                        res = -res
                    return max(-2147483648,min(res,2147483648))
            else:
                res = 10 * res + int(s[i])
        if label == '-':
            res = -res
        return max(-2147483648,min(res,2147483647))
        # max(-2147483648,min(res,2147483648))
        return res
# "  -0012a42" -> -12