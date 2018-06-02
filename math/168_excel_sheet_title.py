class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        slist = [chr(x) for x in range(ord('A'),ord('Z')+1)]
        res = ""
        while n > 0:
            res += slist[(n-1)%26]
            n = (n-1)//26
        return res[::-1]
# Input: 28
# Output: "AB"

# Input: 701
# Output: "ZY"
        
