class Solution(object):

    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # dp[i][j] = dp[i-1][j-1] if S[i-1] == T[j-1] else dp[i-1][j]

        dp = [[0 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]

        for j in range(len(S) + 1):
            dp[j][0] = j + 1

        for i in range(1, len(S) + 1):
            for j in range(1, len(T) + 1):
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        start = 0
        end = len(S) + 1

        for i in range(len(S) + 1):
            if dp[i][len(T)] != 0:
                if i - dp[i][len(T)] + 1 < end - start:
                    end = i
                    start = dp[i][len(T)] - 1

        return S[start: end] if end - start != len(S) + 1 else ""
