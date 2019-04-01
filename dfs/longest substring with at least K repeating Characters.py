from collections import Counter


class Solution(object):

    def longestSubstring(self, s: str, k: int) -> int:

        maxValue = 0

        def helper(s, k):
            nonlocal maxValue
            c = Counter(s)
            found = False
            for key, v in c.items():
                if v < k:
                    found = True
                    break

            if not found:
                maxValue = max(len(s), maxValue)
            else:
                for subString in s.split(key):
                    helper(subString, k)

        helper(s, k)
        return maxValue


# better solution
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87768/4-lines-Python
def longestSubstring(self, s, k):
    for c in set(s):
        if s.count(c) < k:
            return max(self.longestSubstring(t, k) for t in s.split(c))
    return len(s)
