class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sList = list(s)
        return self.backtrack(sList)
    def backtrack(self, sList):
        for i in range(len(sList)-1):
            if sList[i] == sList[i+1] == "+":
                sList[i], sList[i + 1] = "-", "-"
                bool = not self.backtrack(sList)
                sList[i], sList[i + 1] = "+", "+"
                if bool:
                    return True
        return False
        
