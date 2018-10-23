# ord(char) returns the ASCII number
# sliding window
import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1:
            return True
        if len(s1) > len(s2):
            return False
        s1List = [ord(x) - ord('a')for x in s1]
        s2List = [ord(x) - ord('a') for x in s2]
        target = [0] * 26
        window = [0] * 26
        for x in s1List:
            target[x] += 1
        for i in range(len(s2List)):
            window[s2List[i]] += 1
            if i >= len(s1):
                window[s2List[i-len(s1)]] -= 1
            if target == window:
                return True
        return False
s = Solution()
s.checkInclusion('adc','dcda')
# char转数字，再数字转成位置