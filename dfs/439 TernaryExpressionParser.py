class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        if not expression:
            return expression
        for s in expression[::-1]:
            if stack and stack[-1] == "?":
                stack.pop()
                first = stack.pop()
                stack.pop()
                second = stack.pop()
                if s == "T":
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(s)
        return stack[-1]

# T?T?F:5:3
# F?1:T?4:5
# 从后往前！！！！
# 为什么要从后面往前找呢？？？因为如果有一个expression包着一个experssion的话必定从最里面的expression开始判断
# 换言之最里面的肯定是最简的
# 把这个expression计算之后只把结果push进去