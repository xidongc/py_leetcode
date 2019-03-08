class Solution(object):

    def generateParenthesis(self, n):

        # corner case
        if n == 0:
            return []

        # level: tree level
        # openCount: open bracket count
        def dfs(level, n1, n2, n, stack, ret, openCount):
            if level == 2 * n:
                ret.append("".join(stack[:]))

            # dfs
            if n1 < n:
                stack.append("(")
                dfs(level + 1, n1 + 1, n2, n, stack, ret, openCount + 1)
                stack.pop()

            if openCount >= 1 and n2 < n:
                stack.append(")")
                dfs(level + 1, n1, n2 + 1, n, stack, ret, openCount - 1)
                stack.pop()

        stack = list()
        ret = list()
        dfs(0, 0, 0, n, stack, ret, 0)
        return ret