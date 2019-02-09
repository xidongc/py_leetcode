from collections import Counter

class Solution(object):
    def longestPalindrome(self, s: 'str') -> 'int':
        num = 0
        odd = 0
        if len(s) == 0:
            return 0
        c = Counter(list(s))
        for k, v in c.items():
            if v % 2 == 0:
               num += v
            else:
                odd = 1
                num += (v-1)
        num += odd
        return num