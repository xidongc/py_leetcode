class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        def abbr(string, pos):
            return string[:pos] + str(len(string) - pos - 1) + string[-1] if pos < len(string) - 2 else string
        length = len(dict)
        prefix = [1] * length
        res = [0] * length
        for i in range(length):
            res[i] = abbr(dict[i],1)
        for i in range(length):
            while True:
                dupSet = set()
                for j in range(i+1,length):
                    if res[j] == res[i]:
                        dupSet.add(j)
                        dupSet.add(i)
                if not dupSet:
                    break
                for pos in dupSet:
                    prefix[pos] += 1
                    res[pos] = abbr(dict[pos],prefix[pos])
        return res
s = Solution()
print(s.wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]))
