class Solution:

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True

        fast = 0
        slow = 0

        while fast <= len(t) - 1:
            if s[slow] == t[fast]:
                slow += 1
            fast += 1
            if slow == len(s):
                break
        if slow == len(s):
            return True
        else:
            return False