class Solution(object):
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        common = ""

        for s in strs:
            if len(s) > 0 and common == "":
                common = s[0]
            if len(s) > 0 and s[0] != common:
                return ""
            elif len(s) == 0:
                return ""
        if common == "":
            return ""
        return common + self.longestCommonPrefix([s[1:] for s in strs])