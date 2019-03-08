import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anaDict = collections.defaultdict(list)
        for string in strs:
            anaDict[''.join(sorted(string))].append(string)
        return [val for val in anaDict.values()]