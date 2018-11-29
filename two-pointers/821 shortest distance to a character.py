#min 
class Solution(object):
    def shortestToChar(self, string, c):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        disList = [10000] * len(string)
        prev = 10000
        for i in range(len(string)):
            if string[i] == c:
                prev = i
            disList[i] = abs(i - prev)
        for i in range(len(string) - 1, -1, -1):
            if string[i] == c:
                prev = i
            disList[i] = min(abs(prev - i), disList[i])
        return disList

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]