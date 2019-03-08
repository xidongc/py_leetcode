class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        adict = {}
        bdict = {}
        strList = list(str.split(" "))
        if len(pattern) != len(strList):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in adict:
                adict[pattern[i]] = strList[i]
            if strList[i] not in bdict:
                bdict[strList[i]] = pattern[i]
            if adict[pattern[i]] != strList[i] or bdict[strList[i]] != pattern[i]:
                return False
        return True