class Solution(object):

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        Solution.count = 0
        # extend the palindrome from middle to both sides
        for i in range(len(s)):
            self.countPalindrom(s,i,i) #Odd length
            self.countPalindrom(s,i,i+1) #Even length
        return Solution.count

    def countPalindrom(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            Solution.count += 1
            left -= 1
            right += 1


# Sol-2 using dp (O(n**2)) AC
class Solution(object):

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if j == i + 1:
                    dp[i][j] = (s[j] == s[i])
                else:
                    dp[i][j] = (s[j] == s[i] and dp[i + 1][j - 1])

        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j]:
                    count += 1

        return count
