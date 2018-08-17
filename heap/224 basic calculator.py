# Stack Hard
# 遇到operator就对前面的sign和num做结算sign*num，并把sign设置为当前operator
# >>> import re
# >>> a = "Hello world!How are you?My friend.Tom"
# >>> re.split(" |!|\?|\.", a)
import re
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = 1
        res = 0
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c in '+-':
                res += sign * num
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                sign = 1
                num = 0
        if num:
            res += sign * num
        return res
s = Solution()
print(s.calculate("1-11"))


