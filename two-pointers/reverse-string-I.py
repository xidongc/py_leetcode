class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        p1 = 0
        p2 = len(s) - 1
        s = list(s)

        while p1 < p2:
            tmp = s[p1]
            s[p1] = s[p2]
            s[p2] = tmp
            p1 += 1
            p2 -= 1

        s = ''.join(s)

        return str(s)