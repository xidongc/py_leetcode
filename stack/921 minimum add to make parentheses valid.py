class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if s == ')' and stack and stack[-1] =='(':
                stack.pop()
            else:
                stack.append(s)
        return len(stack)
# 同22