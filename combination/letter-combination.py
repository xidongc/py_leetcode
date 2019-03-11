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
        Solution.teleMap = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        Solution.res = []
        self.helper(digits,0,"")
        return Solution.res
    def helper(self,digits,pos,tempStr):
        if len(tempStr) == len(digits):
            Solution.res.append(tempStr)
            return 
        for c in Solution.teleMap[digits[pos]]:
            self.helper(digits,pos+1,tempStr + c)


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        charmap = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if not digits:
            return []
        res = ['']
        for digit in digits:
            tmp = []
            for w in res:
                tmp += [w + c for c in charmap[int(digit)] ]
            res = tmp
        return res
        
