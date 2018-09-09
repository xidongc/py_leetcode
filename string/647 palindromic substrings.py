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
