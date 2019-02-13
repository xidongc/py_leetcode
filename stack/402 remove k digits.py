# 看了Topics知道这个是用栈来解决的题目。看了别人的解答才明白怎么回事。
#
# 使用一个栈作为辅助，遍历数字字符串，当当前的字符比栈最后的字符小的时候，说明要把栈的最后的这个字符删除掉。为什么呢？你想，把栈最后的字符删除掉，然后用现在的字符进行替换，是不是数字比以前的那种情况更小了？所以同样的道理，做一个while循环！这个很重要，可是我没有想到。在每一个数字处理的时候，都要做一个循环，使得栈里面最后的数字比当前数字大的都弹出去。
#
# 最后，如果K还没用完，那要删除哪里的字符呢？毋庸置疑肯定是最后的字符，因为前面的字符都是小字符。
class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        if k > len(num):
            return ''
        elif k == len(num):
            return '0'
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        while k:
            stack.pop()
            k -= 1
        return str(int(''.join(stack)))
s = Solution()
s.removeKdigits("1432219", 3)
