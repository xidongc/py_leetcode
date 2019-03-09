class Solution(object):

    def strStr(self, haystack: str, needle: str) -> int:

        # corner case
        if len(needle) == 0:
            return 0

        if len(needle) > len(haystack) or len(haystack) == 0:
            return -1

        windowSize = len(needle)

        for i in range(len(haystack) - windowSize + 1):
            if haystack[i:i + windowSize] == needle:
                return i

        return -1
