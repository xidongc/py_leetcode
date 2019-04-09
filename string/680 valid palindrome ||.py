# palindrome中间也是palindrome呀
class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # 不要left或者不要right
                a, b = s[left:right], s[left+1:right+1]
                return a == a[::-1] or b == b[::-1]
            left +=1
            right -= 1
        return True


# recursive way
class Solution(object):

    def validPalindrome(self, s: str) -> bool:

        def helper(s, tolerant, p1, p2):
            if tolerant < 0:
                return False

            elif p1 >= p2:
                return True

            if s[p1] == s[p2]:
                return helper(s, tolerant, p1 + 1, p2 - 1)
            else:
                con1 = helper(s, tolerant - 1, p1, p2 - 1)
                con2 = helper(s, tolerant - 1, p1 + 1, p2)
                return con1 or con2

        return helper(s, 1, 0, len(s) - 1)
