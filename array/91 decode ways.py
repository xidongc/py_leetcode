# Solution using dfs TLE
class Solution(object):

    def numDecodings(self, s: str) -> int:
        # corner case
        if len(s) == 0:
            return 0

        # corner case would be "01" if using int(s[currIndex:currIndex+i+1]) return True, however "01" != 1
        target = [str(i) for i in range(1, 27)]

        def dfs(s, stack, remainLength, currIndex, ret):
            if remainLength == 0:
                return

            elif remainLength < 0:
                return

            for i in range(remainLength):
                if 0 < currIndex + i + 1 <= len(s) and s[currIndex:currIndex + i + 1] in target:
                    stack.append(s[currIndex:currIndex + i + 1])
                    dfs(s, stack, remainLength - i - 1, currIndex + i + 1, ret)
                    stack.pop()

        ret = list()
        currIndex = 0
        remainLength = len(s)
        stack = list()

        dfs(s, stack, remainLength, currIndex, ret)
        return len(ret)


# solution using dp AC
class Solution(object):

    def numDecodings(self, s: str) -> int:

        # dp[i] = dp[i-1] + dp[i-2] and 10 < s[i-2:i] <= 26 rule out eg: "01"

        dp = [0 for _ in range(len(s) + 1)]
        dp[1] = 1 if 0 < int(s[0]) <= 9 else 0
        dp[0] = 1

        for i in range(2, len(s) + 1):
            dp[i] = dp[i - 1] if 0 < int(s[i - 1]) <= 9 else 0

            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]

