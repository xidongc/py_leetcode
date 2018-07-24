import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # letter and its times
        need = collections.Counter(t)
        missing = len(t)
        i = I = J = 0
        for j, ch in enumerate(s, 1):
            missing -= 1 if need[ch] > 0 else 0
            need[ch] -= 1
#             need is negative means this char could be removed
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or J - I > j - i:
                    J,I = j,i
        return s[I:J]
#     Since J starts from 1
S = "ADOBECODEBANC"
T = "AABC"
s = Solution()
s.minWindow(S,T)
# enumerate(object, start)
# a -= 1 if c > 0 else 0 等价于
# a -= c > 0
# Find the first window that contains all letters in t;
# Keep expanding the window to the right by 1 char at a time, reducing left side if possible.
# The best part is to make sure that THE ACTIVE WINDOW ALWAYS CONTAINS ALL LETTERS IN t.
# In this case, every time the window is expanded, only the new char need to be checked.