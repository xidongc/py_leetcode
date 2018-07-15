class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 == None and version2 == None:
            return 0
        elif version1 == None and version2 != None:
            return -1
        elif version2 == None and version1 != None:
            return 1
        i = 0
        list1 = version1.split('.')
        list2 = version2.split('.')
        while i < len(list1) or i < len(list2):
            a = 0 if i >= len(list1) else int(list1[i])
            b = 0 if i >= len(list2) else int(list2[i])
            if a > b:
                return 1 
            elif a < b:
                return -1
            i += 1
        return 0
        # If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
        # Input: version1 = "7.5.2.4", version2 = "7.5.3"
        # Output: -1
