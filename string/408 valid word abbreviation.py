class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """

        if not word or not abbr:
            return False
        i,j = 0,0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                val = 0
                # Cannot start from 0
                if int(abbr[j]) == 0:
                    return False
                while j < len(abbr) and abbr[j].isdigit():
                    val = val * 10 + int(abbr[j])
                    j += 1
                i += val
            else:
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)
#Number could be 23, not just 2/3
#     题意w0rd 不能匹配 wrd