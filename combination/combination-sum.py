class Solution(object):

    def __init__(self):
        self.ret = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        if not candidates or candidates[0] <= 0:
            return self.ret
        curr = []
        self.dfs(curr, candidates, target)
        return self.ret

    def dfs(self, curr, candidates, target):
        if target == 0:
            self.ret.append(curr[:])

        for i, c in enumerate(candidates):
            if c <= target:
                curr.append(c)
                self.dfs(curr, candidates[i:], target-c)
                curr.pop()

s = Solution()
candidates = [2,3,5]
target = 8
print(s.combinationSum(candidates, target))