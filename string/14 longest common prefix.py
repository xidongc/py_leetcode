class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i,letter in enumerate(zip(*strs)):
            if len(set(letter)) > 1:
                return strs[0][:i]
        return min(strs)
s = Solution()
s.longestCommonPrefix(["flower","flow","flight"])