from collections import Counter


class Solution(object):

    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1

        counter = Counter(s)
        for i, si in enumerate(s):
            if counter[si] == 1:
                return i
        return -1
