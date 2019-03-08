# 两种基本方法，一种2pointer，一种recursion
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
class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i],s[len(s)-i-1] = s[len(s)-i-1],s[i]