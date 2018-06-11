class Solution(object):
    def __init__(self):
        self.ret = []

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) < 1:
            return self.ret

        charmap = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        letters = []
        for digit in digits:
            letters.append(charmap[int(digit)])
        print(letters)
        curr = []
        self.dfs(curr, 1, len(digits), letters)
        return self.ret

    def dfs(self, curr, k, n, letters):
        if len(curr) == n:
            st = ""
            for c in curr:
                st += c
            self.ret.append(st)
            return

        elif len(curr) > n:
            return

        for l in letters[k-1]:
            curr.append(l)
            self.dfs(curr, k+1, n, letters)
            curr.pop()
            
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits or len(digits) == 0:
            return []
        Solution.teleMap = [0,1,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        Solution.res = []
        self.helper(digits,0,"")
        return Solution.res
    def helper(self,digits,pos,tempStr):
        if len(tempStr) == len(digits):
            Solution.res.append(tempStr)
            return 
        for c in Solution.teleMap[int(digits[pos])]:
            self.helper(digits,pos+1,tempStr + c)

        
