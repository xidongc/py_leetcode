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