class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""
        s = s.split(' ')
        for i in s:
            ret += self.reverse_word(i)

        return ret.rstrip(" ")

    def reverse_word(self, s):
        s = list(s)
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            tmp = s[p1]
            s[p1] = s[p2]
            s[p2] = tmp
            p1 += 1
            p2 -= 1
        return "".join(s) + " "