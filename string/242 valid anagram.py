from collections import Counter


class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = Counter(s)
        dict2 = Counter(t)

        return dict1 == dict2